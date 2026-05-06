#!/usr/bin/env python3
"""Cold-start L1 verification runner.

Reads the deterministic excerpt described in
``tests/cold_start/expected_5_block_structure.md`` plus
``tests/cold_start/prompt.txt``, sends it to a vendor LLM API, and
verifies the response satisfies the 5-block structural contract.

Output is a single Markdown row appended to
``docs/cold_start_evidence.md`` so the result is auditable across
vendors and across weeks.

Vendor support
--------------

Currently implemented:

* ``claude`` — Anthropic Messages API (``api.anthropic.com``).

Planned for v0.7.x:

* ``gpt``    — OpenAI Chat Completions API.
* ``gemini`` — Google Generative Language API.

Auth
----

Reads ``ANTHROPIC_API_KEY`` from the environment. Missing key →
exit 0 with a ``skipped: secret not configured`` row appended; the
weekly workflow expects this so missing secrets do not break the
schedule.

Failure mode
------------

A non-zero exit (1) is reserved for **transport failures and
malformed responses** — the workflow wraps this with
``continue-on-error: true`` so a flaky API does not block the
schedule. Structural failures (missing blocks, fabricated quotations)
exit 0 with ``fail`` in the row; the maintainer review of the row is
the gate, not the workflow exit code.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = REPO_ROOT / "data"
EVIDENCE_LOG = REPO_ROOT / "docs" / "cold_start_evidence.md"

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

# Default model is the highest-capacity Claude as of January 2026.
# Override via ``--model``.
DEFAULT_MODELS = {
    "claude": "claude-opus-4-5",  # placeholder; runner accepts any model id
}

SEED_ENTITIES = (
    "iut:Cor.3.12",
    "iut:theta_hodge_theater",
    "iut:theta_link",
    "iut:log_link",
    "iut:multiradial_algorithm",
    "iut:log_theta_lattice",
)

BLOCK_LABEL_PATTERNS = (
    ("mochizuki", re.compile(r"mochizuki", re.IGNORECASE)),
    ("scholze-stix", re.compile(r"scholze[-\s]*stix|scholze and stix", re.IGNORECASE)),
    ("alternative", re.compile(r"alternative|joshi", re.IGNORECASE)),
    ("pending", re.compile(r"pending", re.IGNORECASE)),
    ("unresolved", re.compile(r"unresolved", re.IGNORECASE)),
)

IRI_PATTERN = re.compile(
    r"\b(?:iut|person|paper|claim|evidence|event):[A-Za-z][A-Za-z0-9_.]*"
)


def _normalise_iri(raw: str) -> str:
    """Strip trailing punctuation that the regex over-captures.

    The character class ``[A-Za-z0-9_.]`` is necessary for legitimate
    dot-bearing IRIs like ``iut:Cor.3.12`` but greedily eats sentence-
    ending periods. Per schema, IRIs always end with an alphanumeric
    or underscore — never a dot — so trailing dots are removable.
    """
    return raw.rstrip(".,;:")

HTTP_TIMEOUT_SECONDS = 60.0


@dataclass(frozen=True, slots=True)
class StructuralResult:
    """Outcome of structural verification of a vendor response."""

    blocks_found: tuple[str, ...]
    missing_blocks: tuple[str, ...]
    unknown_iris: tuple[str, ...]
    overall: str  # "pass" | "fail"
    detail: str


def load_excerpt(data_dir: Path) -> str:
    """Build the deterministic context excerpt for cold-start.

    Returns a single string containing LLM_CONTEXT.md + entity records
    + claims-about-Cor.3.12 + transitively referenced evidence +
    relevant timeline events. Selection is documented in
    expected_5_block_structure.md so reruns at the same commit are
    reproducible across vendors.
    """
    parts: list[str] = []
    llm_context_path = REPO_ROOT / "LLM_CONTEXT.md"
    parts.append(f"<!-- LLM_CONTEXT.md -->\n{llm_context_path.read_text(encoding='utf-8')}")

    with (data_dir / "entities.json").open("r", encoding="utf-8") as fh:
        entities = json.load(fh)["@graph"]
    seed_records = [r for r in entities if r["id"] in SEED_ENTITIES]
    parts.append(
        "<!-- entities (seed subset) -->\n"
        + json.dumps({"@graph": seed_records}, ensure_ascii=False, indent=2)
    )

    with (data_dir / "claims.json").open("r", encoding="utf-8") as fh:
        claims = json.load(fh)["@graph"]
    cor312_claims = [c for c in claims if c.get("about") == "iut:Cor.3.12"]
    parts.append(
        "<!-- claims about iut:Cor.3.12 -->\n"
        + json.dumps({"@graph": cor312_claims}, ensure_ascii=False, indent=2)
    )

    with (data_dir / "evidence.json").open("r", encoding="utf-8") as fh:
        evidence = json.load(fh)["@graph"]
    referenced: set[str] = set()
    for c in cor312_claims:
        referenced.update(c.get("evidence", ()))
    evidence_records = [e for e in evidence if e["id"] in referenced]
    parts.append(
        "<!-- evidence (transitive over the claims) -->\n"
        + json.dumps({"@graph": evidence_records}, ensure_ascii=False, indent=2)
    )

    with (data_dir / "timeline.json").open("r", encoding="utf-8") as fh:
        timeline = json.load(fh)["@graph"]
    timeline_records = [
        e for e in timeline
        if "2018-03-15" <= e.get("date", "") <= "2026-04-08"
    ]
    parts.append(
        "<!-- timeline events 2018-03-15 .. 2026-04-08 -->\n"
        + json.dumps({"@graph": timeline_records}, ensure_ascii=False, indent=2)
    )

    return "\n\n".join(parts)


def call_claude(
    prompt: str, context: str, *, api_key: str, model: str, max_tokens: int
) -> str:
    """Issue an Anthropic Messages API call and return the raw text reply.

    Raises RuntimeError on transport / API errors so the workflow can
    classify them.
    """
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": (
                    f"{context}\n\n---\n\n{prompt}"
                ),
            },
        ],
    }
    request = Request(
        ANTHROPIC_API_URL,
        method="POST",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            payload_bytes = response.read()
    except HTTPError as exc:
        raise RuntimeError(f"anthropic http error: {exc.code} {exc.reason}") from exc
    except URLError as exc:
        raise RuntimeError(f"anthropic url error: {exc.reason}") from exc
    except TimeoutError as exc:
        raise RuntimeError(
            f"anthropic timeout after {HTTP_TIMEOUT_SECONDS}s"
        ) from exc

    payload = json.loads(payload_bytes.decode("utf-8"))
    blocks = payload.get("content", [])
    text_parts = [b["text"] for b in blocks if b.get("type") == "text"]
    if not text_parts:
        raise RuntimeError(f"anthropic response missing text content: {payload!r}")
    return "\n".join(text_parts)


def collect_known_iris(context: str) -> set[str]:
    """Return every IRI literally present in the context excerpt.

    Used to validate that the vendor response did not invent IRIs.
    Trailing sentence punctuation is stripped via _normalise_iri.
    """
    return {_normalise_iri(raw) for raw in IRI_PATTERN.findall(context)}


def verify_structure(response_text: str, context: str) -> StructuralResult:
    """Apply the 5-block structural rubric."""
    found: list[str] = []
    missing: list[str] = []
    for label, pattern in BLOCK_LABEL_PATTERNS:
        if pattern.search(response_text):
            found.append(label)
        else:
            missing.append(label)

    known = collect_known_iris(context)
    response_iris = {_normalise_iri(raw) for raw in IRI_PATTERN.findall(response_text)}
    unknown = sorted(response_iris - known)

    overall = "pass" if not missing and not unknown else "fail"
    detail_bits: list[str] = []
    detail_bits.append(f"{len(found)}/5 blocks present")
    if missing:
        detail_bits.append(f"missing={','.join(missing)}")
    if unknown:
        detail_bits.append(f"unknown_iris={','.join(unknown[:5])}")
    return StructuralResult(
        blocks_found=tuple(found),
        missing_blocks=tuple(missing),
        unknown_iris=tuple(unknown),
        overall=overall,
        detail="; ".join(detail_bits),
    )


def append_evidence_row(
    *, vendor: str, model: str, overall: str, detail: str
) -> None:
    """Append one Markdown row to docs/cold_start_evidence.md."""
    today = datetime.now(timezone.utc).date().isoformat()
    row = f"| {today} | {vendor} | {model} | {overall} | {detail} |\n"
    if not EVIDENCE_LOG.exists():
        EVIDENCE_LOG.write_text(row, encoding="utf-8")
        return
    with EVIDENCE_LOG.open("a", encoding="utf-8") as fh:
        fh.write(row)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Run the L1 cold-start fixture against a vendor LLM."
    )
    parser.add_argument("--vendor", choices=("claude",), default="claude")
    parser.add_argument(
        "--model",
        default=None,
        help="vendor-specific model id; defaults per --vendor",
    )
    parser.add_argument(
        "--max-tokens", type=int, default=2048,
        help="LLM completion budget (default 2048)",
    )
    parser.add_argument(
        "--data", type=Path, default=DATA_DIR,
        help="data directory (default: ./data)",
    )
    parser.add_argument(
        "--prompt-file",
        type=Path,
        default=Path(__file__).parent / "prompt.txt",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="build excerpt + prompt but do not call the API",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    model = args.model or DEFAULT_MODELS[args.vendor]
    excerpt = load_excerpt(args.data)
    prompt_text = args.prompt_file.read_text(encoding="utf-8")

    if args.dry_run:
        print(f"vendor={args.vendor} model={model}")
        print(f"context_chars={len(excerpt)} prompt_chars={len(prompt_text)}")
        return 0

    if args.vendor == "claude":
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            logger.warning("ANTHROPIC_API_KEY not set; skipping run")
            append_evidence_row(
                vendor="claude", model=model,
                overall="skipped",
                detail="secret not configured",
            )
            return 0
        try:
            response_text = call_claude(
                prompt_text, excerpt,
                api_key=api_key, model=model, max_tokens=args.max_tokens,
            )
        except RuntimeError as exc:
            logger.error("claude transport: %s", exc)
            append_evidence_row(
                vendor="claude", model=model,
                overall="error", detail=str(exc),
            )
            return 1
    else:
        logger.error("vendor %r not yet implemented", args.vendor)
        return 2

    result = verify_structure(response_text, excerpt)
    append_evidence_row(
        vendor=args.vendor, model=model,
        overall=result.overall, detail=result.detail,
    )
    if args.verbose:
        print(f"--- response ({len(response_text)} chars) ---")
        print(response_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
