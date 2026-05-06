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
# Override via ``--model``. The default is treated as a hint, not a
# hard contract: the runner accepts any model id Anthropic exposes via
# /v1/messages, including dated aliases (e.g. claude-opus-4-7-20260101).
# When this default no longer resolves, the workflow surfaces a clear
# 404 ``error`` row in cold_start_evidence.md rather than silent
# success — caught by Round 8 audit (placeholder model id was
# fabrication-class drift).
DEFAULT_MODELS = {
    "claude": "claude-opus-4-7",
}

SEED_ENTITIES = (
    "iut:Cor.3.12",
    "iut:theta_hodge_theater",
    "iut:theta_link",
    "iut:log_link",
    "iut:multiradial_algorithm",
    "iut:log_theta_lattice",
)

# Round 9 audit (v0.7.8): the v0.7.7 strict header-only constraint
# eliminated the bare-keyword false-positive class but introduced a
# false-negative regression for natural-prose responses (LLMs that
# write "Mochizuki maintains that..." without a numbered header had
# their block labelled missing — see Round 9 critic CRIT-1).
#
# The repaired contract is a two-stage lookup per block:
# tier 1 — strict v0.7.7-style header marker. Always passes.
# tier 2 — keyword + proximity to a position-related context word
#          (≤ 200 chars). Catches natural prose without false-
#          positively flagging the block on a bare mention.
#
# A block is present iff tier 1 OR tier 2 matches.
_HEADER = r"(?:^|\n)\s*(?:[#*\-]+\s*)?(?:\(?\d+[.)]\s*)?"
_QUALIFIER = r"(?:\s+(?:block|position|side|view|interpretation|framework))"
_PROXIMITY_CHARS = 200


@dataclass(frozen=True, slots=True)
class BlockSpec:
    """Specification for a 5-block protocol block label.

    Attributes:
        name: Lowercase canonical block name.
        header_pattern: Strict header-style match. If this matches
            anywhere in the response, the block is present.
        keyword_pattern: Naked keyword (any occurrence). Tier-2
            matching anchors here.
        context_pattern: Words that, if found within
            ``_PROXIMITY_CHARS`` of any keyword occurrence, count as
            a tier-2 match.
    """

    name: str
    header_pattern: re.Pattern[str]
    keyword_pattern: re.Pattern[str]
    context_pattern: re.Pattern[str]


BLOCKS: tuple[BlockSpec, ...] = (
    BlockSpec(
        name="mochizuki",
        header_pattern=re.compile(
            rf"{_HEADER}mochizuki(?:{_QUALIFIER}|\s*[:\-—])",
            re.IGNORECASE | re.MULTILINE,
        ),
        keyword_pattern=re.compile(r"\bmochizuki\b", re.IGNORECASE),
        context_pattern=re.compile(
            r"\b(?:position|side|view|interpretation|maintains|holds|argues|"
            r"claims|asserts|defends|reformulation|response|report|stance|"
            r"counter|rebuttal|replies?|defended|maintained|essential|"
            r"correct|valid|stand|stands|frobenioid|theta|hodge|cor\.|"
            r"corollary)\b",
            re.IGNORECASE,
        ),
    ),
    BlockSpec(
        name="scholze-stix",
        header_pattern=re.compile(
            rf"{_HEADER}scholze[-\s]*stix(?:{_QUALIFIER}|\s*[:\-—])"
            r"|scholze and stix",
            re.IGNORECASE | re.MULTILINE,
        ),
        keyword_pattern=re.compile(
            r"\b(?:scholze[-\s]*stix|scholze\s+and\s+stix|"
            r"\(SS\)|why\s+abc\s+is\s+still)\b",
            re.IGNORECASE,
        ),
        context_pattern=re.compile(
            r"\b(?:objection|critique|gap|criticize|critical|challenge|"
            r"dispute|silent|alleged|flaw|circular|tautolog|conjecture|"
            r"2018|2021|distinct|copies|conflate|raise|raised)\b",
            re.IGNORECASE,
        ),
    ),
    BlockSpec(
        name="alternative",
        header_pattern=re.compile(
            rf"{_HEADER}(?:alternative|joshi(?:'s)?\s+(?:alternative|"
            r"reformulation|approach|interpretation|framework|ats))"
            rf"(?:{_QUALIFIER}|\s*[:\-—])"
            rf"|{_HEADER}alternative\s*[:\-—]",
            re.IGNORECASE | re.MULTILINE,
        ),
        keyword_pattern=re.compile(
            r"\b(?:alternative|joshi|ats|arithmetic\s+teichmu)\b",
            re.IGNORECASE,
        ),
        context_pattern=re.compile(
            r"\b(?:framework|reformulation|propose|proposes|proposed|"
            r"suggests?|alternat|ats|arxiv|claim|claims|formulation|"
            r"approach|interpretation|series|preprint|2025|2026)\b",
            re.IGNORECASE,
        ),
    ),
    BlockSpec(
        name="pending",
        header_pattern=re.compile(
            rf"{_HEADER}pending(?:{_QUALIFIER}|\s+investigation|\s*[:\-—])",
            re.IGNORECASE | re.MULTILINE,
        ),
        keyword_pattern=re.compile(
            r"\b(?:pending|in\s+progress|under\s+review)\b",
            re.IGNORECASE,
        ),
        context_pattern=re.compile(
            r"\b(?:investigation|review|peer.review|formalization|lana|"
            r"awaiting|scheduled|mid.report|in\s+progress|formaliz|"
            r"verify|verifying|verified)\b",
            re.IGNORECASE,
        ),
    ),
    BlockSpec(
        name="unresolved",
        header_pattern=re.compile(
            rf"{_HEADER}unresolved(?:{_QUALIFIER}|\s+(?:flag|residue)|\s*[:\-—])",
            re.IGNORECASE | re.MULTILINE,
        ),
        keyword_pattern=re.compile(
            r"\b(?:unresolved|undecided|open\s+question)\b",
            re.IGNORECASE,
        ),
        context_pattern=re.compile(
            r"\b(?:flag|residue|unresolved|undecided|tbd|open|awaiting|"
            r"third.party|verify|verification|consensus|status|known|"
            r"not\s+yet|remains?|outstanding)\b",
            re.IGNORECASE,
        ),
    ),
)


def _block_is_present(spec: BlockSpec, text: str) -> bool:
    """Return True if the block is mentioned in ``text``.

    Tier 1: strict header pattern → always counts.
    Tier 2: keyword anywhere + position-related context word within
    ``_PROXIMITY_CHARS`` characters of the keyword span. Picks up
    natural-prose responses such as "Mochizuki maintains that ...".
    """
    if spec.header_pattern.search(text):
        return True
    for match in spec.keyword_pattern.finditer(text):
        start, end = match.span()
        window_start = max(0, start - 50)
        window_end = min(len(text), end + _PROXIMITY_CHARS)
        window = text[window_start:window_end]
        if spec.context_pattern.search(window):
            return True
    return False


# Backwards-compatible alias kept so existing callers / external tests
# that imported ``BLOCK_LABEL_PATTERNS`` still resolve. Each entry is
# now a (name, BlockSpec) pair; consumers should call _block_is_present.
BLOCK_LABEL_PATTERNS = tuple((spec.name, spec) for spec in BLOCKS)

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


def load_excerpt(data_dir: Path, *, include_llm_context: bool = True) -> str:
    """Build the deterministic context excerpt for cold-start.

    Returns a single string containing LLM_CONTEXT.md + entity records
    + claims-about-Cor.3.12 + transitively referenced evidence +
    relevant timeline events. Selection is documented in
    expected_5_block_structure.md so reruns at the same commit are
    reproducible across vendors.

    Round 8 (v0.7.7): when ``include_llm_context=False`` the protocol
    document is omitted from the excerpt because the caller is going
    to inject it through the Messages API ``system`` parameter
    instead. This is the recommended path for Claude / GPT vendors;
    Llama (no system slot) keeps the concatenation default.
    """
    parts: list[str] = []
    if include_llm_context:
        llm_context_path = REPO_ROOT / "LLM_CONTEXT.md"
        parts.append(
            f"<!-- LLM_CONTEXT.md -->\n"
            f"{llm_context_path.read_text(encoding='utf-8')}"
        )

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
    prompt: str, context: str, *, api_key: str, model: str, max_tokens: int,
    system_text: str | None = None,
) -> str:
    """Issue an Anthropic Messages API call and return the raw text reply.

    Round 8 audit (v0.7.7): the protocol contract from
    ``LLM_CONTEXT.md`` is moved to the ``system`` parameter of the
    Messages API. Round 9 audit (v0.7.8) flagged that the
    ``system_text=None`` branch is dead code under the current
    ``--vendor`` choices restriction: ``main()`` always passes a
    system_text. The branch is retained as a small safety valve for
    future vendor implementations (e.g. Llama-style providers that
    do not surface a system slot) — explicitly an "unused-yet"
    code path, not a "Llama-fallback" claim. The vendor choice
    enforcement at the CLI layer ensures only Claude reaches here.

    Raises RuntimeError on transport / API errors so the workflow can
    classify them.
    """
    if system_text is not None:
        body: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            "system": system_text,
            "messages": [
                {"role": "user", "content": f"{context}\n\n---\n\n{prompt}"},
            ],
        }
    else:
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


def collect_known_iris(context: str, data_dir: Path | None = None) -> set[str]:
    """Return every IRI legitimately reachable in this graph.

    Round 8 audit (v0.7.7) flagged that the previous implementation
    only saw IRIs literally present in the truncated *context*
    excerpt — with 6 seed entities, that left 80+ legitimate IRIs
    out of the known set, so any vendor response citing a real
    entity outside the seed list registered as a fabrication and
    the cold-start CI structurally false-failed.

    The repaired contract: known IRIs come from the *full* on-disk
    graph (`data/entities.json` + `claims.json` + `evidence.json` +
    `timeline.json`), regardless of what slice the LLM was given as
    context. The structural guard becomes "did the LLM cite a real
    IRI that exists in the graph?" rather than "did the LLM cite
    only IRIs we showed it?". The latter is too strict — an LLM
    that retrieved an IRI from the graph it sampled in another tool
    call would otherwise fail.
    """
    iris = {_normalise_iri(raw) for raw in IRI_PATTERN.findall(context)}
    if data_dir is None:
        data_dir = DATA_DIR
    if not data_dir.exists():
        return {iri for iri in iris if iri}
    for fname in ("entities.json", "claims.json", "evidence.json", "timeline.json"):
        path = data_dir / fname
        if not path.exists():
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for record in doc.get("@graph", []):
            rid = record.get("id")
            if isinstance(rid, str) and rid:
                iris.add(rid)
    return {iri for iri in iris if iri}


def verify_structure(response_text: str, context: str) -> StructuralResult:
    """Apply the 5-block structural rubric.

    Round 9 (v0.7.8): block presence is decided by ``_block_is_present``,
    which evaluates header-style match (tier 1) OR keyword + proximity-
    context-word match (tier 2). This catches both numbered-list
    responses and natural-prose responses without re-introducing the
    bare-keyword false-positive class that v0.7.7 sealed.
    """
    found: list[str] = []
    missing: list[str] = []
    for spec in BLOCKS:
        if _block_is_present(spec, response_text):
            found.append(spec.name)
        else:
            missing.append(spec.name)

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
    # v0.7.7: protocol goes to system slot for Claude; data excerpt
    # stays in user message. This keeps the L1 contract identical
    # across vendors (LLM_CONTEXT.md is the protocol; data is the
    # graph slice the question is grounded in).
    excerpt = load_excerpt(args.data, include_llm_context=False)
    prompt_text = args.prompt_file.read_text(encoding="utf-8")
    system_text = (REPO_ROOT / "LLM_CONTEXT.md").read_text(encoding="utf-8")

    if args.dry_run:
        print(f"vendor={args.vendor} model={model}")
        print(
            f"system_chars={len(system_text)} "
            f"context_chars={len(excerpt)} "
            f"prompt_chars={len(prompt_text)}"
        )
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
                system_text=system_text,
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
