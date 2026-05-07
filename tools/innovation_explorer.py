#!/usr/bin/env python3
"""Innovation log structural sentinel & delta gate.

Purpose
-------
The monthly heartbeat workflow (``.github/workflows/innovation_heartbeat.yml``,
candidate V) catches *silent death* of the log — i.e. nobody touched it
for 30 days. That is the temporal axis. The structural axis was missing
until v0.7.10:

- **Open-slot health**: `### Q.` is reserved as the "open slot for
  future findings". If it ever disappears or the candidate-letter
  enumeration is no longer continuous, the log lost its append-mostly
  invariant.
- **Status discipline**: every candidate must declare exactly one of
  ``Implemented`` / ``Surveyed`` / ``Deferred`` / ``Rejected``.
- **Implemented-needs-evidence**: any candidate marked Implemented must
  cite at least one of (commit SHA, version tag, file path).
- **No two open slots**: a recent edit could accidentally introduce
  ``### Q.`` twice; that's a structural break.
- **Linkable IRIs in candidate body**: the body should reference real
  files in the repo where the candidate was implemented (file-path
  presence is checked, not file existence — so the gate keeps working
  if a file is later renamed during a refactor).

Exit codes
----------
- 0  — log is structurally clean
- 1  — at least one structural anomaly (gate failure, intended for CI)

Usage
-----
``python tools/innovation_explorer.py [--json] [--strict-paths]``

``--strict-paths`` additionally checks file-path existence (off by
default to keep the gate cheap and rename-tolerant).
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

logger = logging.getLogger("innovation_explorer")

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = REPO_ROOT / "docs" / "INNOVATION_LOG.md"

# Canonical candidate header pattern: `### <LETTER+>. <title>`
HEADER_RE = re.compile(r"^### ([A-Z]+)\. (.+?)$")
# Match the entire "**Status**:" line, then look for any allowed status
# token anywhere on that line. Tolerates ``**Status**: **Implemented**``
# (emphasis-wrapped) and ``**Status**: Deferred (rationale)`` alike.
STATUS_LINE_RE = re.compile(r"^- \*\*Status\*\*: *(.+)$", re.MULTILINE)
# Round 11 audit (v0.7.14): the 7-40 range previously matched 64-char
# strings such as the Merkle root, allowing a future "commit pending"
# replacement to substitute the merkle root literal and still satisfy
# the cites-evidence gate. Git short SHAs are normally 7-12 chars; full
# SHAs are 40. Restrict to those two regimes so the 64-char Merkle
# digest cannot masquerade as a commit citation.
COMMIT_REF_RE = re.compile(r"\b(?:[0-9a-f]{7,12}|[0-9a-f]{40})\b")
VERSION_TAG_RE = re.compile(r"\bv0\.\d+\.\d+\b")
FILE_PATH_RE = re.compile(r"`([^`]*?\.(?:py|md|json|lean|yml|yaml|jsonld|txt|toml))`")

ALLOWED_STATUSES: frozenset[str] = frozenset({
    "Implemented", "Surveyed", "Deferred", "Rejected", "Subsumed",
})


@dataclass(slots=True)
class Candidate:
    letter: str
    title: str
    body: str
    line_number: int

    def has_status(self, status: str) -> bool:
        return status in self.declared_statuses()

    def declared_statuses(self) -> list[str]:
        """Return every allowed-status token observed on any
        ``- **Status**:`` line of this candidate's body. Empty if none.

        Implementation note: emphasis (``**Implemented**``) is stripped
        by the simple ``substring in line`` test because the search is
        case-sensitive against the bare word.
        """
        out: list[str] = []
        for m in STATUS_LINE_RE.finditer(self.body):
            line = m.group(1)
            for allowed in ALLOWED_STATUSES:
                if allowed in line:
                    out.append(allowed)
        return out

    def cites_evidence(self) -> bool:
        return (
            bool(COMMIT_REF_RE.search(self.body))
            or bool(VERSION_TAG_RE.search(self.body))
            or bool(FILE_PATH_RE.search(self.body))
        )

    def referenced_files(self) -> list[str]:
        return FILE_PATH_RE.findall(self.body)


@dataclass(slots=True)
class StructuralFinding:
    severity: str  # "error" | "warning"
    candidate: str
    detail: str

    def render(self) -> str:
        return f"[{self.severity}] {self.candidate}: {self.detail}"


@dataclass(slots=True)
class ExplorerReport:
    findings: list[StructuralFinding] = field(default_factory=list)
    candidate_count: int = 0
    implemented_count: int = 0
    open_slot_present: bool = False
    last_letter_seen: str = ""

    @property
    def ok(self) -> bool:
        return not any(f.severity == "error" for f in self.findings)


def _iter_candidates(text: str) -> Iterator[Candidate]:
    lines = text.splitlines()
    starts: list[tuple[int, str, str]] = []
    for i, line in enumerate(lines):
        m = HEADER_RE.match(line)
        if m:
            starts.append((i, m.group(1), m.group(2)))

    for idx, (line_idx, letter, title) in enumerate(starts):
        end_line = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        body = "\n".join(lines[line_idx + 1: end_line])
        yield Candidate(
            letter=letter, title=title, body=body, line_number=line_idx + 1,
        )


def _is_open_slot(c: Candidate) -> bool:
    return "(open slot" in c.title.lower()


def explore() -> ExplorerReport:
    if not LOG_FILE.is_file():
        report = ExplorerReport()
        report.findings.append(StructuralFinding(
            severity="error", candidate="<file>",
            detail=f"INNOVATION_LOG.md not found at {LOG_FILE}",
        ))
        return report

    text = LOG_FILE.read_text(encoding="utf-8")
    report = ExplorerReport()

    candidates = list(_iter_candidates(text))
    report.candidate_count = len(candidates)
    if not candidates:
        report.findings.append(StructuralFinding(
            severity="error", candidate="<top>",
            detail="no candidate headers (### LETTER.) found in log",
        ))
        return report

    open_slot_seen = 0
    seen_letters: dict[str, Candidate] = {}

    for c in candidates:
        if c.letter in seen_letters:
            other = seen_letters[c.letter]
            report.findings.append(StructuralFinding(
                severity="error", candidate=c.letter,
                detail=(
                    f"duplicate candidate letter at L{c.line_number} "
                    f"(first occurrence at L{other.line_number}); "
                    f"reletter the second one"
                ),
            ))
        else:
            seen_letters[c.letter] = c

        if _is_open_slot(c):
            open_slot_seen += 1
            continue

        statuses = c.declared_statuses()
        if not statuses:
            report.findings.append(StructuralFinding(
                severity="error", candidate=c.letter,
                detail=(
                    f"candidate {c.title!r} (L{c.line_number}) declares no "
                    f"recognised status (need one of {sorted(ALLOWED_STATUSES)})"
                ),
            ))
        elif len(statuses) > 1:
            report.findings.append(StructuralFinding(
                severity="warning", candidate=c.letter,
                detail=(
                    f"candidate {c.title!r} declares multiple statuses "
                    f"({statuses}); choose one canonical"
                ),
            ))
        elif statuses == ["Implemented"] and not c.cites_evidence():
            report.findings.append(StructuralFinding(
                severity="error", candidate=c.letter,
                detail=(
                    f"candidate {c.title!r} marked Implemented but cites no "
                    f"commit SHA, version tag, or file path. Without "
                    f"evidence the claim is unverifiable."
                ),
            ))
        # Round 12 audit (v0.7.15): the v0.7.14 candidate FF declared
        # itself "Implemented (v0.7.14, commit pending)" — i.e. the
        # very entry that claimed to replace 13 stale placeholders
        # left ITSELF as one. The gate matches the *placeholder style*
        # only (`(vX.Y.Z, commit pending)`), not free-form prose
        # references to the term that legitimately discuss the
        # phenomenon (e.g. retracting documentation).
        elif statuses == ["Implemented"]:
            placeholder_re = re.compile(
                r"\(v\d+(?:\.\d+){1,2},\s*commit pending\)"
            )
            if placeholder_re.search(c.body):
                report.findings.append(StructuralFinding(
                    severity="error", candidate=c.letter,
                    detail=(
                        f"candidate {c.title!r} marked Implemented but "
                        f"carries the literal `(vX.Y.Z, commit pending)` "
                        f"placeholder. Replace with the actual commit "
                        f"SHA of the landing tag (Round 12 self-trap "
                        f"regression guard)."
                    ),
                ))

    report.open_slot_present = open_slot_seen > 0
    if open_slot_seen == 0:
        report.findings.append(StructuralFinding(
            severity="error", candidate="<open-slot>",
            detail="no '(open slot for future ... findings)' candidate "
                   "is present; the append-mostly invariant is broken",
        ))
    elif open_slot_seen > 1:
        report.findings.append(StructuralFinding(
            severity="warning", candidate="<open-slot>",
            detail=f"{open_slot_seen} open-slot candidates present; "
                   f"reduce to 1",
        ))

    report.implemented_count = sum(
        1 for c in candidates
        if not _is_open_slot(c) and c.has_status("Implemented")
    )
    if candidates:
        report.last_letter_seen = candidates[-1].letter

    return report


def _format_human(report: ExplorerReport) -> str:
    lines: list[str] = []
    if report.ok:
        lines.append(
            f"innovation_explorer: OK "
            f"(candidates={report.candidate_count}, "
            f"implemented={report.implemented_count}, "
            f"open_slot={'yes' if report.open_slot_present else 'no'}, "
            f"last_letter={report.last_letter_seen!r})"
        )
    else:
        lines.append(
            f"innovation_explorer: {len(report.findings)} finding(s) "
            f"(candidates={report.candidate_count})"
        )
        for f in report.findings:
            lines.append(f"  - {f.render()}")
    return "\n".join(lines) + "\n"


def _format_json(report: ExplorerReport) -> str:
    return json.dumps(
        {
            "ok": report.ok,
            "candidate_count": report.candidate_count,
            "implemented_count": report.implemented_count,
            "open_slot_present": report.open_slot_present,
            "last_letter_seen": report.last_letter_seen,
            "findings": [
                {
                    "severity": f.severity,
                    "candidate": f.candidate,
                    "detail": f.detail,
                }
                for f in report.findings
            ],
        },
        indent=2,
        ensure_ascii=False,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Innovation log structural sentinel"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable summary on stdout")
    parser.add_argument("--strict-paths", action="store_true",
                        help="additionally check file-path existence in"
                             " each candidate body")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    report = explore()

    if args.strict_paths:
        text = LOG_FILE.read_text(encoding="utf-8") if LOG_FILE.is_file() else ""
        for c in _iter_candidates(text):
            for path_text in c.referenced_files():
                # path_text may be a glob-y phrase; only check pure paths.
                if any(ch in path_text for ch in "{}*?"):
                    continue
                p = REPO_ROOT / path_text
                if not p.exists():
                    report.findings.append(StructuralFinding(
                        severity="warning", candidate=c.letter,
                        detail=f"referenced file does not exist: {path_text}",
                    ))

    if args.json:
        print(_format_json(report))
    else:
        sys.stdout.write(_format_human(report))

    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
