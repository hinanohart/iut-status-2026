#!/usr/bin/env python3
"""DOI / ISBN identifier verifier for iut-status-2026 graph.

Round 7 audit (v0.6.1) closed a Kato-book ISBN fabrication
(``978-4-04-110262-7`` was a syntactically and check-digit-valid
**but non-existent** ISBN). ``tools/verify_urls.py`` cannot detect this
class because URL liveness alone never queries identifier registries.

Companion tool to ``verify_urls.py``: it inspects the ``doi`` and
``isbn`` fields of ``data/evidence.json`` and validates them at two
levels:

* **Offline (default)**: structural validation. DOI must match
  ``10.NNNNN/<suffix>``; ISBN-10 / ISBN-13 must satisfy their official
  check-digit formulas (ISO 2108).
* **Network (opt-in)**: ``--check-doi`` resolves
  ``https://doi.org/<doi>`` via HEAD, expecting 2xx / 3xx;
  ``--check-isbn`` queries Open Library
  ``https://openlibrary.org/isbn/<digits>.json`` expecting 2xx for
  registered ISBNs. Open Library coverage of Japanese-language books
  is partial; a 404 is **not** treated as a failure (only as
  ``unresolved``) so that absent metadata does not block CI for
  legitimately-rare titles. Round-7-class fabrications still surface
  because the maintainer reviews the JSON report before re-acceptance.

Drift-zero contract
-------------------
Like ``verify_urls.py``, this tool never repairs data in place. It
reports identifier states; corrections to ``data/evidence.json`` are
maintainer-driven and pass through normal git review.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

USER_AGENT = (
    "iut-status-2026/0.7 (DOI/ISBN verifier; "
    "https://github.com/hinanohart/iut-status-2026)"
)
DOI_RESOLVER = "https://doi.org/{doi}"
OPEN_LIBRARY_API = "https://openlibrary.org/isbn/{isbn}.json"
HTTP_TIMEOUT_SECONDS = 15.0

DOI_PATTERN = re.compile(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")


@dataclass(frozen=True, slots=True)
class IdOutcome:
    """One identifier's verification result."""

    record_id: str
    kind: str  # "doi" or "isbn"
    value: str
    status: str  # "valid_offline" | "alive" | "unresolved" | "invalid" | "skipped"
    detail: str = ""


def _strip_isbn_separators(isbn: str) -> str:
    """Remove hyphens and spaces from an ISBN string."""
    return isbn.replace("-", "").replace(" ", "")


def validate_isbn10(digits: str) -> tuple[bool, str]:
    """Return ``(is_valid, diagnostic)`` for a 10-character ISBN-10 string.

    ISO 2108 ISBN-10 check: sum of (digit_i * (10 - i)) for i in [0, 10)
    must be divisible by 11. The 10th character may be 'X' representing 10.
    """
    if len(digits) != 10:
        return False, f"isbn-10 must be 10 chars, got {len(digits)}"
    if not (digits[:9].isdigit() and (digits[9].isdigit() or digits[9] == "X")):
        return False, "isbn-10 contains non-digit (and non-X tail)"
    total = 0
    for index, char in enumerate(digits):
        value = 10 if char == "X" else int(char)
        total += value * (10 - index)
    if total % 11 != 0:
        return False, f"isbn-10 checksum failed (sum {total} mod 11 = {total % 11})"
    return True, "isbn-10 checksum ok"


def validate_isbn13(digits: str) -> tuple[bool, str]:
    """Return ``(is_valid, diagnostic)`` for a 13-character ISBN-13 string.

    ISO 2108 ISBN-13 check: alternating weights 1, 3, 1, 3, ...; sum must be
    divisible by 10.
    """
    if len(digits) != 13:
        return False, f"isbn-13 must be 13 chars, got {len(digits)}"
    if not digits.isdigit():
        return False, "isbn-13 contains non-digit"
    if digits[:3] not in {"978", "979"}:
        return False, f"isbn-13 prefix '{digits[:3]}' not in {{978, 979}}"
    total = sum(
        int(char) * (1 if index % 2 == 0 else 3)
        for index, char in enumerate(digits)
    )
    if total % 10 != 0:
        return False, f"isbn-13 checksum failed (sum {total} mod 10 = {total % 10})"
    return True, "isbn-13 checksum ok"


def validate_isbn(isbn: str) -> tuple[bool, str]:
    """Validate ISBN-10 or ISBN-13 by detecting length after separator strip."""
    digits = _strip_isbn_separators(isbn).upper()
    if len(digits) == 10:
        return validate_isbn10(digits)
    if len(digits) == 13:
        return validate_isbn13(digits)
    return False, f"isbn length {len(digits)} not 10 or 13 (separator-stripped)"


def validate_doi(doi: str) -> tuple[bool, str]:
    """Validate DOI structural format per ANSI/NISO Z39.84-2010."""
    if not DOI_PATTERN.match(doi):
        return False, f"doi does not match pattern '10.NNNNN/<suffix>'"
    return True, "doi structural ok"


def collect_identifiers(data_dir: Path) -> list[tuple[str, str, str]]:
    """Return ``[(record_id, kind, value), ...]`` from evidence records."""
    out: list[tuple[str, str, str]] = []
    with (data_dir / "evidence.json").open("r", encoding="utf-8") as fh:
        for record in json.load(fh).get("@graph", []):
            if record.get("doi"):
                out.append((record["id"], "doi", record["doi"]))
            if record.get("isbn"):
                out.append((record["id"], "isbn", record["isbn"]))
    return out


def _http_head(url: str) -> tuple[int | None, str]:
    """Issue HEAD; on 405 fall back to GET. Return ``(http_code, detail)``."""
    request = Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            return response.status, "head ok"
    except HTTPError as exc:
        if exc.code == 405:
            request_get = Request(
                url, method="GET", headers={"User-Agent": USER_AGENT}
            )
            try:
                with urlopen(request_get, timeout=HTTP_TIMEOUT_SECONDS) as response:
                    return response.status, "get ok (head 405)"
            except HTTPError as get_exc:
                return get_exc.code, f"get http error: {get_exc.reason}"
            except URLError as get_exc:
                return None, f"get url error: {get_exc.reason}"
        return exc.code, f"http error: {exc.reason}"
    except URLError as exc:
        return None, f"url error: {exc.reason}"
    except TimeoutError:
        return None, f"timeout after {HTTP_TIMEOUT_SECONDS}s"
    except Exception as exc:  # noqa: BLE001 — defensive against transport bugs
        return None, f"unexpected: {type(exc).__name__}: {exc}"


def verify_doi_network(doi: str) -> tuple[str, str]:
    """Resolve DOI via doi.org and classify outcome.

    Returns ``(status, detail)`` where ``status`` is one of
    ``"alive"`` (HTTP 2xx/3xx), ``"unresolved"`` (transport failure),
    or ``"invalid"`` (HTTP 4xx/5xx — DOI is registered but broken).
    """
    url = DOI_RESOLVER.format(doi=quote(doi, safe="/."))
    code, detail = _http_head(url)
    if code is None:
        return "unresolved", detail
    if 200 <= code < 400:
        return "alive", f"http {code} ({detail})"
    return "invalid", f"http {code} ({detail})"


def verify_isbn_network(isbn: str) -> tuple[str, str]:
    """Query Open Library for the given ISBN.

    Returns ``(status, detail)``. A 200 response means Open Library
    has metadata; 404 means **not registered there**, which is mapped
    to ``unresolved`` rather than ``invalid`` because Open Library's
    Japanese-language coverage is partial.
    """
    digits = _strip_isbn_separators(isbn).upper()
    url = OPEN_LIBRARY_API.format(isbn=digits)
    request = Request(url, method="GET", headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            code = response.status
        if 200 <= code < 300:
            return "alive", f"open-library http {code}"
        return "unresolved", f"open-library http {code}"
    except HTTPError as exc:
        if exc.code == 404:
            return "unresolved", "open-library 404 (jp coverage partial)"
        return "unresolved", f"open-library http error: {exc.code} {exc.reason}"
    except URLError as exc:
        return "unresolved", f"open-library url error: {exc.reason}"
    except TimeoutError:
        return "unresolved", f"open-library timeout after {HTTP_TIMEOUT_SECONDS}s"
    except Exception as exc:  # noqa: BLE001 — defensive against transport bugs
        return "unresolved", f"open-library unexpected: {type(exc).__name__}: {exc}"


def verify_one(
    record_id: str, kind: str, value: str, *, check_doi: bool, check_isbn: bool
) -> IdOutcome:
    """Apply offline + (optional) network validation."""
    if kind == "doi":
        offline_ok, detail = validate_doi(value)
        if not offline_ok:
            return IdOutcome(record_id, kind, value, "invalid", detail)
        if not check_doi:
            return IdOutcome(record_id, kind, value, "valid_offline", detail)
        status, net_detail = verify_doi_network(value)
        return IdOutcome(record_id, kind, value, status, net_detail)
    if kind == "isbn":
        offline_ok, detail = validate_isbn(value)
        if not offline_ok:
            return IdOutcome(record_id, kind, value, "invalid", detail)
        if not check_isbn:
            return IdOutcome(record_id, kind, value, "valid_offline", detail)
        status, net_detail = verify_isbn_network(value)
        return IdOutcome(record_id, kind, value, status, net_detail)
    return IdOutcome(record_id, kind, value, "skipped", f"unknown kind: {kind}")


def render_summary(outcomes: list[IdOutcome]) -> str:
    """Return human-readable grouped summary."""
    parts: list[str] = [f"total: {len(outcomes)} identifier(s)"]
    by_status: dict[str, list[IdOutcome]] = {}
    for o in outcomes:
        by_status.setdefault(o.status, []).append(o)
    for status in ("alive", "valid_offline", "unresolved", "invalid", "skipped"):
        rows = by_status.get(status, [])
        if not rows:
            continue
        parts.append(f"\n{status}: {len(rows)}")
        for o in rows:
            parts.append(f"  [{o.kind}] {o.record_id}  {o.value}  — {o.detail}")
    return "\n".join(parts)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="DOI / ISBN identifier verifier for the IUT graph."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=DATA_DIR,
        help="data directory (default: ./data)",
    )
    parser.add_argument(
        "--check-doi",
        action="store_true",
        help="resolve every DOI via doi.org (network)",
    )
    parser.add_argument(
        "--check-isbn",
        action="store_true",
        help="query Open Library for every ISBN (network)",
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

    triples = collect_identifiers(args.data)
    if not triples:
        logger.warning("no DOI or ISBN identifiers found in %s", args.data)
        return 0

    outcomes = [
        verify_one(
            rid, kind, value,
            check_doi=args.check_doi, check_isbn=args.check_isbn,
        )
        for rid, kind, value in triples
    ]
    print(render_summary(outcomes))

    if args.report is not None:
        payload = [
            {
                "record_id": o.record_id,
                "kind": o.kind,
                "value": o.value,
                "status": o.status,
                "detail": o.detail,
            }
            for o in outcomes
        ]
        args.report.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info("wrote report to %s", args.report)

    invalid = [o for o in outcomes if o.status == "invalid"]
    if invalid:
        logger.error(
            "%d invalid identifier(s) — graph contains broken DOI/ISBN",
            len(invalid),
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
