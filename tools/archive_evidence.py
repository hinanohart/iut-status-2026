#!/usr/bin/env python3
"""Wayback Machine archival bootstrap for iut-status-2026 graph.

Round 4-7 audits surfaced four fabrication-class defects whose common
root cause is **external reality drift**: papers move, ISBNs change,
PRIMS issue identifiers rotate, news index pages cycle their entries,
and blog posts get edited or deleted. ``tools/verify_urls.py`` (v0.6)
catches the easiest sub-class of this drift (URL becomes un-resolvable)
but cannot recover content once it has rotated; without an archival
snapshot the original cited material is lost.

This tool fills that capability gap. It is **opt-in network access**
(default mode is offline) and produces a reproducible JSON report.

Operating modes
---------------

``offline`` (default)
    Read ``data/evidence.json`` and ``data/timeline.json``, list every
    record carrying a ``url`` field with its current ``archive_url``
    status (present / missing). No network access. Useful as a
    preflight check before a populate run.

``--network --lookup``
    Query the Wayback Machine **Availability API**
    (``https://archive.org/wayback/available?url=<URL>``) for every
    record whose ``archive_url`` is missing. The API returns the
    closest existing snapshot or an empty response if no snapshot
    exists. Found snapshots are written into a JSON report and (with
    ``--apply``) merged back into ``data/evidence.json`` /
    ``data/timeline.json``.

``--network --submit``
    Issue ``https://web.archive.org/save/<URL>`` for every record
    whose ``archive_url`` is missing. Anonymous Save Page Now (SPN)
    has rate limits (~10 req / minute / IP) and may be blocked for
    paywalled hosts. The tool serialises requests with a
    ``--delay`` (default 12 s) between submissions. After submission
    a ``--lookup`` pass should follow once the snapshot indexer
    catches up (typically 1-3 minutes per submitted URL).

Limitations
-----------

* SPN anonymous quota is a moving target. The tool detects 429 and
  503 responses and aborts the remaining batch with a clear error
  message rather than silently failing partial records.
* Wayback Machine does not snapshot every URL (paywalled hosts,
  ``robots.txt`` exclusions, large PDFs). Missing snapshots after a
  successful submit are normal and do not indicate a tool defect.
* ISBNs are not URLs and are not archived by this tool. Use a
  separate ISBN-resolution check (planned for v0.7.x via
  ``tools/verify_urls.py`` extension).

Drift-zero contract
-------------------
The tool never invents a ``web.archive.org/web/<timestamp>`` value.
Every populated ``archive_url`` either comes verbatim from the
Availability API response (for ``--lookup``) or from the redirect
``Location`` header of a successful ``save`` response. Synthesising
a snapshot URL without API confirmation would itself be a
fabrication-class defect of the type Round-7 audit closed.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

USER_AGENT = (
    "iut-status-2026/0.7 (Wayback bootstrap; "
    "https://github.com/hinanohart/iut-status-2026)"
)
AVAILABILITY_API = "https://archive.org/wayback/available?url={url}"
SAVE_PAGE_NOW = "https://web.archive.org/save/{url}"
HTTP_TIMEOUT_SECONDS = 30.0


@dataclass(frozen=True, slots=True)
class ArchiveOutcome:
    """One record's archival lookup / submit result.

    Attributes:
        record_id: IRI of the evidence or timeline event.
        kind: ``"evidence"`` or ``"timeline"``.
        url: Original URL recorded in the graph.
        archive_url: Existing or newly-fetched snapshot URL.
        action: ``"present"`` (already had archive_url),
            ``"found"`` (lookup discovered a snapshot),
            ``"submitted"`` (submit succeeded),
            ``"missing"`` (no snapshot available),
            ``"skipped"`` (no primary url field),
            ``"error"`` (transport / API failure).
        detail: Human-readable diagnostic.
    """

    record_id: str
    kind: str
    url: str | None
    archive_url: str | None
    action: str
    detail: str = ""


def _read_graph(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    with path.open("r", encoding="utf-8") as fh:
        doc = json.load(fh)
    if "@graph" not in doc or not isinstance(doc["@graph"], list):
        raise ValueError(f"{path} missing @graph array")
    return doc, doc["@graph"]


def collect_records(data_dir: Path) -> list[ArchiveOutcome]:
    """Snapshot the current archival state for evidence + timeline records."""
    out: list[ArchiveOutcome] = []
    for kind, fname in (("evidence", "evidence.json"), ("timeline", "timeline.json")):
        _, records = _read_graph(data_dir / fname)
        for record in records:
            url = record.get("url")
            archive_url = record.get("archive_url")
            if url is None:
                action = "skipped"
                detail = "no primary url field"
            elif archive_url is not None:
                action = "present"
                detail = "archive_url already populated"
            else:
                action = "missing"
                detail = "needs lookup or submit"
            out.append(
                ArchiveOutcome(
                    record_id=record["id"],
                    kind=kind,
                    url=url,
                    archive_url=archive_url,
                    action=action,
                    detail=detail,
                )
            )
    return out


def _http_get_json(url: str) -> dict[str, Any]:
    """Issue GET, parse JSON. Raises on transport / parse error."""
    request = Request(url, method="GET", headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
        body = response.read()
    return json.loads(body.decode("utf-8"))


def lookup_one(url: str) -> tuple[str | None, str]:
    """Query Wayback Availability API for *url*.

    Returns ``(archive_url_or_None, detail)``. The archive URL, if
    present, is taken verbatim from ``closest.url`` in the API
    response — never synthesised.
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None, f"non-http scheme: {parsed.scheme!r}"
    api_url = AVAILABILITY_API.format(url=quote(url, safe=":/?&="))
    try:
        payload = _http_get_json(api_url)
    except HTTPError as exc:
        return None, f"availability http error: {exc.code} {exc.reason}"
    except URLError as exc:
        return None, f"availability url error: {exc.reason}"
    except TimeoutError:
        return None, f"availability timeout after {HTTP_TIMEOUT_SECONDS}s"
    except json.JSONDecodeError as exc:
        return None, f"availability json parse error: {exc}"
    except Exception as exc:  # noqa: BLE001 — defensive against transport bugs
        return None, f"availability unexpected: {type(exc).__name__}: {exc}"

    snapshots = payload.get("archived_snapshots", {})
    closest = snapshots.get("closest")
    if not closest or not closest.get("available"):
        return None, "no snapshot available"
    snapshot_url = closest.get("url")
    if not isinstance(snapshot_url, str) or not snapshot_url:
        return None, "snapshot url missing in API response"
    return snapshot_url, f"snapshot {closest.get('timestamp', '?')}"


def submit_one(url: str) -> tuple[str | None, str]:
    """Submit *url* to Wayback Save Page Now (anonymous).

    SPN is rate-limited; the caller must serialise submissions.
    Returns ``(archive_url_or_None, detail)``. The archive URL, if
    present, is taken from the redirect ``Location`` header — never
    synthesised.
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None, f"non-http scheme: {parsed.scheme!r}"
    save_url = SAVE_PAGE_NOW.format(url=quote(url, safe=":/?&="))
    request = Request(save_url, method="GET", headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            final_url = response.geturl()
            status = response.status
    except HTTPError as exc:
        if exc.code in (429, 503):
            raise RuntimeError(
                f"SPN rate-limit ({exc.code}); abort batch and retry later"
            ) from exc
        return None, f"submit http error: {exc.code} {exc.reason}"
    except URLError as exc:
        return None, f"submit url error: {exc.reason}"
    except TimeoutError:
        return None, f"submit timeout after {HTTP_TIMEOUT_SECONDS}s"
    except Exception as exc:  # noqa: BLE001 — defensive against transport bugs
        return None, f"submit unexpected: {type(exc).__name__}: {exc}"

    if not final_url.startswith("https://web.archive.org/web/"):
        return None, f"submit returned unexpected url: {final_url!r}"
    return final_url, f"submitted (status {status})"


def run_lookup(
    outcomes: list[ArchiveOutcome], delay: float
) -> list[ArchiveOutcome]:
    """Resolve missing archive_url values via Availability API."""
    updated: list[ArchiveOutcome] = []
    for o in outcomes:
        if o.action != "missing" or o.url is None:
            updated.append(o)
            continue
        snapshot, detail = lookup_one(o.url)
        if snapshot is not None:
            updated.append(
                ArchiveOutcome(
                    record_id=o.record_id,
                    kind=o.kind,
                    url=o.url,
                    archive_url=snapshot,
                    action="found",
                    detail=detail,
                )
            )
        else:
            updated.append(
                ArchiveOutcome(
                    record_id=o.record_id,
                    kind=o.kind,
                    url=o.url,
                    archive_url=None,
                    action="missing",
                    detail=detail,
                )
            )
        if delay > 0:
            time.sleep(delay)
    return updated


def run_submit(
    outcomes: list[ArchiveOutcome], delay: float
) -> list[ArchiveOutcome]:
    """Submit missing URLs to Wayback Save Page Now."""
    updated: list[ArchiveOutcome] = []
    for o in outcomes:
        if o.action != "missing" or o.url is None:
            updated.append(o)
            continue
        try:
            snapshot, detail = submit_one(o.url)
        except RuntimeError as exc:
            updated.append(
                ArchiveOutcome(
                    record_id=o.record_id,
                    kind=o.kind,
                    url=o.url,
                    archive_url=None,
                    action="error",
                    detail=str(exc),
                )
            )
            logger.error("aborting batch: %s", exc)
            updated.extend(outcomes[outcomes.index(o) + 1:])
            return updated
        if snapshot is not None:
            updated.append(
                ArchiveOutcome(
                    record_id=o.record_id,
                    kind=o.kind,
                    url=o.url,
                    archive_url=snapshot,
                    action="submitted",
                    detail=detail,
                )
            )
        else:
            updated.append(
                ArchiveOutcome(
                    record_id=o.record_id,
                    kind=o.kind,
                    url=o.url,
                    archive_url=None,
                    action="error",
                    detail=detail,
                )
            )
        if delay > 0:
            time.sleep(delay)
    return updated


def apply_to_data(outcomes: list[ArchiveOutcome], data_dir: Path) -> int:
    """Merge ``found`` / ``submitted`` archive_urls back into data files.

    Returns the number of records updated. Files are written with a
    trailing newline preserved, 2-space indent matching existing files.
    """
    by_kind: dict[str, dict[str, str]] = {"evidence": {}, "timeline": {}}
    for o in outcomes:
        if o.action in {"found", "submitted"} and o.archive_url is not None:
            by_kind[o.kind][o.record_id] = o.archive_url

    written = 0
    for kind, fname in (("evidence", "evidence.json"), ("timeline", "timeline.json")):
        updates = by_kind[kind]
        if not updates:
            continue
        path = data_dir / fname
        doc, records = _read_graph(path)
        for record in records:
            if record["id"] in updates:
                if "archive_url" not in record:
                    record["archive_url"] = updates[record["id"]]
                    written += 1
        path.write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return written


def render_summary(outcomes: list[ArchiveOutcome]) -> str:
    """Return human-readable grouped summary."""
    parts: list[str] = []
    parts.append(f"total: {len(outcomes)} record(s)")
    by_action: dict[str, list[ArchiveOutcome]] = {}
    for o in outcomes:
        by_action.setdefault(o.action, []).append(o)
    for action in (
        "present", "found", "submitted", "missing", "skipped", "error"
    ):
        rows = by_action.get(action, [])
        if not rows:
            continue
        parts.append(f"\n{action}: {len(rows)}")
        for o in rows:
            head = f"  [{o.kind}] {o.record_id}"
            tail_bits: list[str] = []
            if o.url:
                tail_bits.append(o.url)
            if o.archive_url:
                tail_bits.append(f"-> {o.archive_url}")
            if o.detail:
                tail_bits.append(f"({o.detail})")
            parts.append(head)
            if tail_bits:
                parts.append("  " + "  ".join(tail_bits))
    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Wayback Machine archival bootstrap for the IUT graph."
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
        help="enable network access (Availability API or Save Page Now)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--lookup",
        action="store_true",
        help="lookup missing archive_urls via Availability API (requires --network)",
    )
    mode.add_argument(
        "--submit",
        action="store_true",
        help="submit missing URLs via Save Page Now (requires --network)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="merge found / submitted archive_urls back into data/*.json",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=12.0,
        help="seconds between successive API calls (default: 12.0)",
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

    if (args.lookup or args.submit) and not args.network:
        logger.error("--lookup / --submit require --network")
        return 2

    outcomes = collect_records(args.data)

    if args.network and args.lookup:
        outcomes = run_lookup(outcomes, args.delay)
    elif args.network and args.submit:
        outcomes = run_submit(outcomes, args.delay)

    print(render_summary(outcomes))

    if args.apply:
        if not (args.lookup or args.submit):
            logger.error("--apply requires --lookup or --submit")
            return 2
        written = apply_to_data(outcomes, args.data)
        print(f"\nupdated {written} record(s) in {args.data}")

    if args.report is not None:
        payload = [
            {
                "record_id": o.record_id,
                "kind": o.kind,
                "url": o.url,
                "archive_url": o.archive_url,
                "action": o.action,
                "detail": o.detail,
            }
            for o in outcomes
        ]
        args.report.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info("wrote report to %s", args.report)

    errors = [o for o in outcomes if o.action == "error"]
    if errors:
        logger.error("%d error(s)", len(errors))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
