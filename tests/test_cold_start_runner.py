"""Tests for tests/cold_start/run_cold_start.py — structural rubric + excerpt.

Network paths (call_claude) are not exercised in CI; they are
exercised by the weekly schedule with real API keys. These tests
cover the offline contract: excerpt selection, structural rubric,
IRI fabrication detection, evidence-row formatting, and CLI dry-run.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "tests" / "cold_start"))

import run_cold_start as rcs  # type: ignore  # noqa: E402


SAMPLE_RESPONSE_GOOD = """
1. Mochizuki: Cor 3.12 holds; see iut:Cor.3.12.
2. Scholze-Stix: alleged gap; see claim:scholze_stix_2018_main.
3. Alternative: Joshi ATS; see claim:joshi_2025_alternative.
4. Pending: peer review status; see evidence:Joshi_arxiv_2505_10568.
5. Unresolved: third-party rebuttal not yet published.
"""

SAMPLE_RESPONSE_MISSING_BLOCKS = """
1. Mochizuki view: Cor 3.12 stands.
2. Scholze-Stix: there are issues.
"""

SAMPLE_RESPONSE_FABRICATES_IRI = """
1. Mochizuki: see iut:Cor.3.12.
2. Scholze-Stix: see claim:scholze_stix_2018_main.
3. Alternative: see claim:joshi_2025_alternative.
4. Pending: see evidence:Joshi_arxiv_2505_10568.
5. Unresolved: see iut:nonexistent_concept_invented_by_llm.
"""

SAMPLE_CONTEXT = (
    "iut:Cor.3.12 claim:scholze_stix_2018_main claim:joshi_2025_alternative "
    "evidence:Joshi_arxiv_2505_10568"
)


class StructuralVerifyTests(unittest.TestCase):
    def test_pass_on_complete_response(self) -> None:
        result = rcs.verify_structure(SAMPLE_RESPONSE_GOOD, SAMPLE_CONTEXT)
        self.assertEqual(result.overall, "pass")
        self.assertEqual(len(result.blocks_found), 5)
        self.assertEqual(result.missing_blocks, ())

    def test_fail_on_missing_blocks(self) -> None:
        result = rcs.verify_structure(
            SAMPLE_RESPONSE_MISSING_BLOCKS, SAMPLE_CONTEXT
        )
        self.assertEqual(result.overall, "fail")
        self.assertIn("alternative", result.missing_blocks)
        self.assertIn("pending", result.missing_blocks)
        self.assertIn("unresolved", result.missing_blocks)

    def test_fail_on_fabricated_iri(self) -> None:
        result = rcs.verify_structure(
            SAMPLE_RESPONSE_FABRICATES_IRI, SAMPLE_CONTEXT
        )
        self.assertEqual(result.overall, "fail")
        self.assertIn("iut:nonexistent_concept_invented_by_llm", result.unknown_iris)


class CollectKnownIrisTests(unittest.TestCase):
    def test_extracts_all_namespace_prefixes(self) -> None:
        text = (
            "iut:foo person:bar paper:baz claim:qux evidence:abc event:event_x "
            "but not iutNot or iut: or random:thing"
        )
        iris = rcs.collect_known_iris(text)
        self.assertIn("iut:foo", iris)
        self.assertIn("person:bar", iris)
        self.assertIn("paper:baz", iris)
        self.assertIn("claim:qux", iris)
        self.assertIn("evidence:abc", iris)
        self.assertIn("event:event_x", iris)
        self.assertNotIn("random:thing", iris)


class ExcerptSelectionTests(unittest.TestCase):
    def test_excerpt_loads_from_real_data(self) -> None:
        # Real repo data must support cold-start fixture excerpt-building.
        excerpt = rcs.load_excerpt(REPO_ROOT / "data")
        self.assertGreater(len(excerpt), 1000)
        # Seed entities must all appear in excerpt
        for seed in rcs.SEED_ENTITIES:
            self.assertIn(seed, excerpt, f"seed {seed} missing")
        # Cor.3.12 claims must appear
        self.assertIn("iut:Cor.3.12", excerpt)


class AppendEvidenceRowTests(unittest.TestCase):
    def test_row_format(self) -> None:
        with TemporaryDirectory() as td:
            path = Path(td) / "evidence.md"
            # monkey-patch the module-level constant
            original = rcs.EVIDENCE_LOG
            rcs.EVIDENCE_LOG = path
            try:
                rcs.append_evidence_row(
                    vendor="claude", model="claude-test",
                    overall="pass", detail="5/5 blocks present",
                )
                rcs.append_evidence_row(
                    vendor="claude", model="claude-test",
                    overall="fail", detail="missing=alternative",
                )
                content = path.read_text(encoding="utf-8")
            finally:
                rcs.EVIDENCE_LOG = original
            lines = [line for line in content.split("\n") if line.strip()]
            self.assertEqual(len(lines), 2)
            self.assertIn("claude-test", lines[0])
            self.assertIn("pass", lines[0])
            self.assertIn("fail", lines[1])


class CLIDryRunTests(unittest.TestCase):
    def test_dry_run_returns_zero(self) -> None:
        rc = rcs.main(["--vendor", "claude", "--dry-run"])
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
