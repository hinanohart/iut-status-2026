#!/usr/bin/env python3
"""Tests for ``tools/innovation_explorer.py``."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPLORER = REPO_ROOT / "tools" / "innovation_explorer.py"

sys.path.insert(0, str(REPO_ROOT))
import tools.innovation_explorer as ie  # noqa: E402


def _run(*extra: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, str(EXPLORER), *extra],
        capture_output=True, text=True, check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


class CleanLogTests(unittest.TestCase):
    def test_live_log_is_clean(self) -> None:
        rc, out, err = _run()
        self.assertEqual(
            rc, 0,
            f"innovation_explorer failed on live log:\nSTDOUT:\n{out}\nSTDERR:\n{err}",
        )
        self.assertIn("OK", out)

    def test_json_mode_well_formed(self) -> None:
        rc, out, _ = _run("--json")
        self.assertEqual(rc, 0)
        payload = json.loads(out)
        self.assertTrue(payload["ok"])
        self.assertGreater(payload["candidate_count"], 20)
        self.assertGreaterEqual(payload["implemented_count"], 5)
        self.assertTrue(payload["open_slot_present"])


class StructureTests(unittest.TestCase):
    """Pin the parser against a synthetic INNOVATION_LOG."""

    def _patched_explore(self, content: str) -> ie.ExplorerReport:
        # Rather than patch globals, write to a temp file and patch
        # LOG_FILE for the duration of the call.
        original = ie.LOG_FILE
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp) / "INNOVATION_LOG.md"
            tmp_path.write_text(content, encoding="utf-8")
            try:
                ie.LOG_FILE = tmp_path
                return ie.explore()
            finally:
                ie.LOG_FILE = original

    def test_clean_synthetic_log_passes(self) -> None:
        log = (
            "### A. Test idea\n"
            "- **Status**: Implemented (commit `abcdef1`).\n"
            "- File: `tools/test.py`\n"
            "\n"
            "### Q. (open slot for future findings)\n"
        )
        report = self._patched_explore(log)
        self.assertTrue(report.ok)
        self.assertEqual(report.candidate_count, 2)
        self.assertEqual(report.implemented_count, 1)
        self.assertTrue(report.open_slot_present)

    def test_missing_open_slot_fails(self) -> None:
        log = (
            "### A. Test idea\n"
            "- **Status**: Implemented (commit `abcdef1`).\n"
        )
        report = self._patched_explore(log)
        self.assertFalse(report.ok)
        msg = "\n".join(f.detail for f in report.findings)
        self.assertIn("open slot", msg.lower())

    def test_implemented_without_evidence_fails(self) -> None:
        log = (
            "### A. Test idea\n"
            "- **Status**: Implemented (no commit ref or file path).\n"
            "\n"
            "### Q. (open slot)\n"
        )
        report = self._patched_explore(log)
        self.assertFalse(report.ok)
        msg = "\n".join(f.detail for f in report.findings)
        self.assertIn("cites no", msg)

    def test_duplicate_letter_flagged(self) -> None:
        log = (
            "### A. First\n"
            "- **Status**: Surveyed.\n"
            "\n"
            "### A. Second with same letter\n"
            "- **Status**: Deferred.\n"
            "\n"
            "### Q. (open slot)\n"
        )
        report = self._patched_explore(log)
        self.assertFalse(report.ok)
        msg = "\n".join(f.detail for f in report.findings)
        self.assertIn("duplicate", msg.lower())

    def test_unknown_status_flagged(self) -> None:
        log = (
            "### A. Test idea\n"
            "- **Status**: Pondered (not in allow-list).\n"
            "\n"
            "### Q. (open slot)\n"
        )
        report = self._patched_explore(log)
        self.assertFalse(report.ok)
        msg = "\n".join(f.detail for f in report.findings)
        self.assertIn("no recognised status", msg)

    def test_emphasis_wrapped_status_recognised(self) -> None:
        log = (
            "### A. Test idea\n"
            "- **Status**: **Implemented** (v0.1.2, commit `abcdef1`).\n"
            "\n"
            "### Q. (open slot)\n"
        )
        report = self._patched_explore(log)
        self.assertTrue(report.ok)
        self.assertEqual(report.implemented_count, 1)

    def test_subsumed_status_recognised(self) -> None:
        log = (
            "### A. Folded idea\n"
            "- **Status**: Subsumed by candidate B.\n"
            "\n"
            "### B. Owning idea\n"
            "- **Status**: Implemented (file `tools/x.py`).\n"
            "\n"
            "### Q. (open slot)\n"
        )
        report = self._patched_explore(log)
        self.assertTrue(report.ok)


if __name__ == "__main__":
    unittest.main()
