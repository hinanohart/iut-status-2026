"""Tests for JSON-LD validation, loader, and structural assertions.

These tests guard the drift-zero invariants:
- Every IUT concept's IRI is uniquely resolvable.
- Every claim is grounded in at least one evidence record.
- Every claim has a position from the 6-value enum.
- The Mochizuki / Scholze-Stix / Joshi / LANA quartet is each
  represented by at least one claim.
- The 5-block answer template can be filled from the graph.

Run with::

    python -m unittest tests.test_validation -v
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
    """Structural validation against JSON Schema and cross-references."""

    def test_no_validation_errors(self) -> None:
        errors = validate_all()
        self.assertEqual(errors, [], f"validation errors: {errors}")


class GraphTopologyTests(unittest.TestCase):
    """Tests on the graph topology (independent of any specific content)."""

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
        self.assertIn("valid", positions, "Mochizuki-position claim missing for Cor.3.12")
        self.assertIn("alleged_gap", positions, "Scholze-Stix-position claim missing for Cor.3.12")

    def test_dispute_pairs_nonempty(self) -> None:
        pairs = self.graph.opposing_pairs()
        self.assertGreater(len(pairs), 0)

    def test_evidence_records_resolve(self) -> None:
        for claim in self.graph.claims.values():
            for ev_id in claim.evidence:
                self.assertIn(ev_id, self.graph.evidence,
                              f"claim {claim.id} cites missing evidence {ev_id}")


class FiveBlockTemplateTests(unittest.TestCase):
    """The graph must be able to fill all five blocks of the answer template."""

    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_block_1_mochizuki_position_filled(self) -> None:
        valid_claims = self.graph.claims_by_position("valid")
        self.assertTrue(any("Mochizuki" in c.proponents for c in valid_claims),
                        "Block 1: no claim with Mochizuki as proponent and position=valid")

    def test_block_2_scholze_stix_position_filled(self) -> None:
        gap_claims = self.graph.claims_by_position("alleged_gap")
        self.assertTrue(
            any("Scholze" in c.proponents and "Stix" in c.proponents for c in gap_claims),
            "Block 2: no Scholze+Stix claim with position=alleged_gap",
        )

    def test_block_3_alternative_position_filled(self) -> None:
        alt_claims = self.graph.claims_by_position("alternative")
        self.assertTrue(any("Joshi" in c.proponents for c in alt_claims),
                        "Block 3: no Joshi alternative reformulation")

    def test_block_4_pending_investigation_filled(self) -> None:
        pending_claims = self.graph.claims_by_position("pending")
        self.assertTrue(len(pending_claims) >= 1,
                        "Block 4: no pending investigation (LANA?)")

    def test_block_5_unresolved_flag_implicit(self) -> None:
        for claim in self.graph.claims.values():
            if claim.position in ("valid", "alleged_gap"):
                if not claim.status:
                    continue
                status = claim.status.lower()
                forbidden_resolved_phrases = (
                    "is resolved",
                    "now resolved",
                    "has been resolved",
                    "issue resolved",
                    "verdict",
                )
                for phrase in forbidden_resolved_phrases:
                    self.assertNotIn(
                        phrase, status,
                        f"claim {claim.id} status appears to declare resolution: '{claim.status}'",
                    )


class TimelineTests(unittest.TestCase):
    """Timeline integrity checks."""

    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_timeline_chronological_loadable(self) -> None:
        self.assertGreater(len(self.graph.timeline), 10)
        events = sorted(self.graph.timeline.values(), key=lambda e: e.date)
        self.assertEqual(events[0].date, "1985-01-01")
        last = events[-1]
        self.assertGreaterEqual(last.date, "2026-07-17")

    def test_required_milestones_present(self) -> None:
        labels_concat = " ".join(e.label for e in self.graph.timeline.values())
        for keyword in ["abc conjecture proposed", "RIMS preprints", "Why abc is still a conjecture",
                        "Report on Discussions", "PRIMS Vol.57", "Joshi", "LANA"]:
            self.assertIn(keyword, labels_concat,
                          f"timeline missing milestone keyword: {keyword}")


class PeerReviewStatusTests(unittest.TestCase):
    """The peer_review_status field must be set on every claim and orthogonal to position."""

    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_all_claims_have_peer_review_status(self) -> None:
        for claim in self.graph.claims.values():
            self.assertIsNotNone(claim.peer_review_status,
                                 f"claim {claim.id} missing peer_review_status")

    def test_western_majority_skeptical_is_informal(self) -> None:
        c = self.graph.claim("claim:western_majority_skeptical")
        self.assertIsNotNone(c)
        assert c is not None
        self.assertEqual(c.peer_review_status, "informal_blog")


class GenericityTests(unittest.TestCase):
    """The schema is intended to generalize; spot-check generic-applicable invariants."""

    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_no_value_laden_adjectives_in_claim_labels(self) -> None:
        forbidden = ["fatal", "groundbreaking", "definitive", "fringe", "absurd"]
        for claim in self.graph.claims.values():
            for word in forbidden:
                self.assertNotIn(word, claim.label.lower(),
                                 f"claim {claim.id} label has value-laden word '{word}'")

    def test_no_orphan_evidence(self) -> None:
        from tools.validate import BACKGROUND_EVIDENCE_ALLOWLIST
        referenced: set[str] = set()
        for claim in self.graph.claims.values():
            referenced.update(claim.evidence)
        all_evidence = set(self.graph.evidence.keys())
        orphans = all_evidence - referenced - BACKGROUND_EVIDENCE_ALLOWLIST
        self.assertEqual(orphans, set(), f"orphan evidence: {orphans}")


class LeanModuleTests(unittest.TestCase):
    """v0.7.5 invariant: every entity referencing a Lean module path must
    resolve to an existing .lean file under lean/."""

    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_every_lean_module_resolves(self) -> None:
        for entity in self.graph.entities.values():
            module = entity.lean_module
            if module is None:
                continue
            path = REPO_ROOT / "lean" / (module.replace(".", "/") + ".lean")
            self.assertTrue(
                path.exists(),
                f"{entity.id}: lean_module {module!r} -> "
                f"{path.relative_to(REPO_ROOT)} does not exist",
            )

    def test_basic_imports_every_per_section_module(self) -> None:
        basic = (REPO_ROOT / "lean" / "IutStatus" / "Basic.lean").read_text(
            encoding="utf-8"
        )
        for entity in self.graph.entities.values():
            if entity.lean_module is None:
                continue
            short = entity.lean_module.split(".")[-1]
            self.assertIn(
                f"import IutStatus.{short}",
                basic,
                f"Basic.lean missing import IutStatus.{short} for {entity.id}",
            )


class PersonRoleTests(unittest.TestCase):
    """v0.7.2 invariant: every Person record either connects via the claim
    graph (proponent or introduced_by) OR carries a role qualifier
    documenting why disconnection is intentional."""

    def setUp(self) -> None:
        self.graph = IutGraph.load(DATA_DIR)

    def test_zero_edge_persons_carry_role(self) -> None:
        proponent_strings: set[str] = set()
        for claim in self.graph.claims.values():
            proponent_strings.update(claim.proponents)
        introduced_by_targets = {
            e.introduced_by for e in self.graph.entities.values()
            if e.introduced_by is not None
        }
        exempt = {"background_reference", "historical_foundation"}
        for entity in self.graph.entities.values():
            if entity.type != "Person":
                continue
            if entity.role in exempt:
                continue
            suffix = entity.id.split(":", 1)[1]
            candidates = {suffix, suffix.replace("_", " "), suffix.split("_")[0]}
            connected = bool(candidates & proponent_strings) or (
                entity.id in introduced_by_targets
            )
            self.assertTrue(
                connected,
                f"{entity.id}: Person without role and without claim-graph "
                f"edge — tag with role or connect",
            )

    def test_known_zero_edge_persons_have_expected_roles(self) -> None:
        # Pin the v0.7.2 decisions so future audits cannot silently
        # drop the role tags and re-introduce orphans.
        expected = {
            "person:Grothendieck": "historical_foundation",
            "person:Pop": "background_reference",
            "person:Sawin": "background_reference",
        }
        for pid, role in expected.items():
            entity = self.graph.entity(pid)
            self.assertIsNotNone(entity, f"{pid} missing")
            assert entity is not None
            self.assertEqual(
                entity.role, role,
                f"{pid}: expected role={role!r}, got {entity.role!r}",
            )


if __name__ == "__main__":
    unittest.main()
