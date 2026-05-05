"""Tests for JSON-LD validation and minimal loader.

Run with::

    python -m unittest tests.test_validation
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from loaders.python_minimal import IutGraph  # noqa: E402
from tools.validate import validate_all  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"


class ValidationTests(unittest.TestCase):
    def test_no_validation_errors(self) -> None:
        errors = validate_all()
        self.assertEqual(errors, [], f"validation errors: {errors}")


class GraphLoadingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_cor_3_12_present(self) -> None:
        cor = self.graph.entity("iut:Cor.3.12")
        self.assertIsNotNone(cor)
        assert cor is not None
        self.assertEqual(cor.type, "Corollary")
        self.assertEqual(cor.section, "06_cor_3_12")

    def test_cor_3_12_has_opposing_claims(self) -> None:
        claims = self.graph.claims_about("iut:Cor.3.12")
        positions = {c.position for c in claims}
        self.assertIn(
            "valid", positions,
            "Mochizuki-position claim missing for Cor.3.12",
        )
        self.assertIn(
            "gap", positions,
            "Scholze-Stix-position claim missing for Cor.3.12",
        )

    def test_dispute_pairs_nonempty(self) -> None:
        pairs = self.graph.opposing_pairs()
        self.assertGreater(
            len(pairs), 0,
            "expected at least one (counter, target) pair",
        )

    def test_evidence_records_resolve(self) -> None:
        for claim in self.graph.claims.values():
            for ev_id in claim.evidence:
                self.assertIn(
                    ev_id, self.graph.evidence,
                    f"claim {claim.id} cites missing evidence {ev_id}",
                )

    def test_timeline_chronological_loadable(self) -> None:
        self.assertGreater(len(self.graph.timeline), 5)
        events = sorted(self.graph.timeline.values(), key=lambda e: e.date)
        self.assertEqual(events[0].date, "1985-01-01")
        last = events[-1]
        self.assertGreaterEqual(last.date, "2026-03-31")


if __name__ == "__main__":
    unittest.main()
