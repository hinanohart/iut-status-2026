#!/usr/bin/env python3
"""URL liveness verifier for iut-status-2026 graph.

Round 4-6 audits surfaced three fabrication-class defects (Joshi v2,
Woit dating, IRI drift) where ``data/*.json`` recorded URLs that did
not match external reality. ``tools/validate.py`` only checks internal
graph consistency, so those errors persisted through round 1-5 audits.

This tool fills that capability gap. It is **opt-in** (network access
is not assumed in the default CI path) and is reproducible: the same
URL list always produces the same per-URL outcome.

Operating modes
---------------

``offline`` (default)
    Read ``data/evidence.json`` and ``data/timeline.json``, print the
    list of URLs grouped by hostname, and verify URL syntax (RFC 3986
    via ``urllib.parse``). Useful as a pre-flight check before a
    network run.

``--network``
    Issue an HTTP HEAD request to every URL with a 10-second timeout
    and a small descriptive User-Agent. Successful responses (2xx, 3xx)
    are recorded as ``alive``. 4xx/5xx, DNS failures, and timeouts are
    recorded as ``dead``. The tool exits non-zero if any record is
    ``dead``, which is suitable for a manually-triggered CI job that
    runs on a schedule rather than on every push.

``--report PATH``
    Write a JSON report of per-URL outcomes to PATH for archiving.

Limitations
-----------

* HEAD requests are not always honoured by hosts (some return 405).
  In that case the tool falls back to a small GET request that reads
  no body. False-negatives are still possible for unusually
  configured hosts; the report should be reviewed manually.
* Wayback Machine fallback is not integrated yet. A future iteration
  may try ``http://web.archive.org/web/<URL>`` when a primary URL
  fails.
* The tool does not verify that the URL **content** matches the
  graph claim — only that the URL resolves. Round-6 Woit fabrication
  was a content-vs-metadata mismatch (URL alive, but date and topic
  wrong), so this tool catches the easier half of the problem.
  Content verification remains a manual step.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

USER_AGENT = (
    "iut-status-2026/0.6 (URL liveness verifier; "
    "https://github.com/hinanohart/iut-status-2026)"
)
HEAD_TIMEOUT_SECONDS = 10.0


@dataclass(frozen=True, slots=True)
class UrlOutcome:
    """One URL's verification result.

    Attributes:
        record_id: IRI of the evidence or timeline event.
        url: The URL string as recorded in the graph.
        kind: ``"evidence"`` or ``"timeline"``.
        status: One of ``"alive"``, ``"dead"``, ``"unchecked"``.
        http_code: HTTP status when applicable; ``None`` otherwise.
        detail: Human-readable diagnostic.
    """

    record_id: str
    url: str
    kind: str
    status: str
    http_code: int | None = None
    detail: str = ""


def collect_urls(data_dir: Path) -> list[tuple[str, str, str]]:
    """Return ``[(record_id, url, kind), ...]`` from evidence + timeline."""
    out: list[tuple[str, str, str]] = []
    with (data_dir / "evidence.json").open("r", encoding="utf-8") as fh:
        for record in json.load(fh).get("@graph", []):
            url = record.get("url")
            if url:
                out.append((record["id"], url, "evidence"))
    with (data_dir / "timeline.json").open("r", encoding="utf-8") as fh:
        for record in json.load(fh).get("@graph", []):
            url = record.get("url")
            if url:
                out.append((record["id"], url, "timeline"))
    return out


def verify_syntax(url: str) -> tuple[bool, str]:
    """Verify URL syntax. Returns ``(is_valid, diagnostic)``."""
    try:
        parsed = urlparse(url)
    except ValueError as exc:
        return False, f"parse error: {exc}"
    if parsed.scheme not in {"http", "https"}:
        return False, f"non-http scheme: {parsed.scheme!r}"
    if not parsed.netloc:
        return False, "empty netloc"
    return True, "syntax ok"


def head_or_get(url: str) -> tuple[int | None, str]:
    """Issue HEAD then fall back to GET. Return ``(http_code, detail)``."""
    request_head = Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request_head, timeout=HEAD_TIMEOUT_SECONDS) as response:
            return response.status, "head ok"
    except HTTPError as exc:
        if exc.code == 405:  # method not allowed → fall back to GET
            request_get = Request(
                url, method="GET", headers={"User-Agent": USER_AGENT}
            )
            try:
                with urlopen(request_get, timeout=HEAD_TIMEOUT_SECONDS) as response:
                    return response.status, "get ok (head 405)"
            except HTTPError as get_exc:
                return get_exc.code, f"get http error: {get_exc.reason}"
            except URLError as get_exc:
                return None, f"get url error: {get_exc.reason}"
        return exc.code, f"http error: {exc.reason}"
    except URLError as exc:
        return None, f"url error: {exc.reason}"
    except TimeoutError:
        return None, f"timeout after {HEAD_TIMEOUT_SECONDS}s"
    except Exception as exc:  # noqa: BLE001 — defensive against transport bugs
        return None, f"unexpected: {type(exc).__name__}: {exc}"


def verify_one(record_id: str, url: str, kind: str, network: bool) -> UrlOutcome:
    """Return verification result for one record."""
    syntax_ok, syntax_detail = verify_syntax(url)
    if not syntax_ok:
        return UrlOutcome(record_id, url, kind, "dead", None, syntax_detail)
    if not network:
        return UrlOutcome(record_id, url, kind, "unchecked", None, syntax_detail)
    http_code, detail = head_or_get(url)
    if http_code is None:
        return UrlOutcome(record_id, url, kind, "dead", None, detail)
    if 200 <= http_code < 400:
        return UrlOutcome(record_id, url, kind, "alive", http_code, detail)
    return UrlOutcome(record_id, url, kind, "dead", http_code, detail)


def render_summary(outcomes: list[UrlOutcome]) -> str:
    """Return a human-readable grouped summary."""
    parts: list[str] = []
    parts.append(f"total: {len(outcomes)} url(s)")
    by_status: dict[str, list[UrlOutcome]] = {}
    for outcome in outcomes:
        by_status.setdefault(outcome.status, []).append(outcome)
    for status in ("alive", "unchecked", "dead"):
        rows = by_status.get(status, [])
        if not rows:
            continue
        parts.append(f"\n{status}: {len(rows)}")
        for outcome in rows:
            head = f"  [{outcome.kind}] {outcome.record_id}"
            tail = f"  {outcome.url}"
            if outcome.http_code is not None:
                tail += f" (HTTP {outcome.http_code})"
            if outcome.detail:
                tail += f"  — {outcome.detail}"
            parts.append(head)
            parts.append(tail)
    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Verify evidence + timeline URLs for the IUT graph."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=DATA_DIR,
        help="data directory (default: ./data)",
    )
    parser.add_argument(
        "--network",
        action="store_true",
        help="issue HEAD/GET requests (default: syntax only)",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="optional path to write a JSON report of outcomes",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="enable debug-level logging",
    )
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    triples = collect_urls(args.data)
    if not triples:
        logger.warning("no URLs found in %s", args.data)
        return 0

    outcomes = [
        verify_one(rid, url, kind, args.network) for rid, url, kind in triples
    ]
    print(render_summary(outcomes))

    if args.report is not None:
        payload = [
            {
                "record_id": o.record_id,
                "url": o.url,
                "kind": o.kind,
                "status": o.status,
                "http_code": o.http_code,
                "detail": o.detail,
            }
            for o in outcomes
        ]
        args.report.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info("wrote report to %s", args.report)

    dead = [o for o in outcomes if o.status == "dead"]
    if dead:
        logger.error("%d dead URL(s)", len(dead))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
