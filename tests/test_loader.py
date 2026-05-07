#!/usr/bin/env python3
"""Unit tests for ``loaders/python_minimal.py``.

Architect Sec 8 deferred coverage (closed at v0.7.10): the loader is the
gate every downstream consumer (renderer, MCP server, validate.py,
property_audit.py drift detector) reads from. Until v0.7.10 the loader
had only indirect coverage via ``test_validation`` (which loads the live
graph). These tests pin the contract per dataclass and per factory.

Tests use temporary on-disk JSON-LD files instead of the live ``data/``
fixtures, so additions to the real graph do not flake the tests.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from loaders.python_minimal import (  # noqa: E402
    Claim, Entity, Evidence, IutGraph, TimelineEvent,
)


def _write_graph(dir_path: Path, name: str, records: list[dict]) -> None:
    """Write a minimal JSON-LD ``@graph`` document to ``dir_path / name``."""
    doc = {"@context": "../data/context.jsonld", "@graph": records}
    (dir_path / name).write_text(json.dumps(doc), encoding="utf-8")


def _baseline_records() -> dict[str, list[dict]]:
    return {
        "entities.json": [
            {
                "id": "iut:Cor.3.12",
                "type": "Corollary",
                "label": "Corollary 3.12",
                "section": "06_cor_3_12",
                "verified_at": "2026-05-07",
                "alt_labels": ["Cor 3.12"],
                "introduced_by": "paper:IUTchIII",
                "introduced_year": "2012",
                "definedIn": "paper:IUTchIII",
                "depends_on": ["iut:multiradial_algorithm"],
                "informal_md": "docs/section_6_cor_3_12.md",
                "lean_stub": "lean/IutStatus/Cor312.lean",
                "lean_module": "IutStatus.Cor312",
                "role": None,
            },
        ],
        "claims.json": [
            {
                "id": "claim:test_claim",
                "type": "Claim",
                "label": "Test claim asserting something neutral.",
                "about": "iut:Cor.3.12",
                "position": "valid",
                "stance": "supportive",
                "proponents": ["A"],
                "asserted_at": "2020-01-01",
                "evidence": ["evidence:test"],
                "counters": ["claim:other"],
                "supports": ["claim:another"],
                "relates_to": ["claim:third"],
                "specific_support": "Reason for support.",
                "specific_objection": None,
                "fair_use_note": "Quoted under fair use.",
                "status": "draft",
                "peer_review_status": "peer_reviewed",
                "verified_at": "2026-05-07",
            },
        ],
        "evidence.json": [
            {
                "id": "evidence:test",
                "type": "Paper",
                "label": "Test evidence",
                "url": "https://example.org/x.pdf",
                "archive_url": "https://web.archive.org/web/x.pdf",
                "doi": "10.0000/test",
                "isbn": "978-0-00-000000-0",
                "publisher": "Test Press",
                "asserted_at": "2020-01-01",
            },
        ],
        "timeline.json": [
            {
                "id": "event:test",
                "type": "event",
                "label": "Test event happens",
                "date": "2020-01-01",
                "actors": ["A", "B"],
                "url": "https://example.org/event",
                "archive_url": "https://web.archive.org/web/event",
            },
        ],
    }


class LoadGraphTests(unittest.TestCase):
    def test_load_full_graph_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dir_path = Path(tmp)
            for name, records in _baseline_records().items():
                _write_graph(dir_path, name, records)
            graph = IutGraph.load(dir_path)
        self.assertEqual(len(graph.entities), 1)
        self.assertEqual(len(graph.claims), 1)
        self.assertEqual(len(graph.evidence), 1)
        self.assertEqual(len(graph.timeline), 1)

    def test_load_missing_directory_raises(self) -> None:
        with self.assertRaises(FileNotFoundError):
            IutGraph.load("/nonexistent-iut-status-2026-test-path-xyz")

    def test_load_missing_required_file_raises(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dir_path = Path(tmp)
            # Only entities — claims.json missing → must raise
            _write_graph(dir_path, "entities.json", _baseline_records()["entities.json"])
            with self.assertRaises(FileNotFoundError):
                IutGraph.load(dir_path)

    def test_load_evidence_optional(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dir_path = Path(tmp)
            recs = _baseline_records()
            recs.pop("evidence.json")
            for name, records in recs.items():
                _write_graph(dir_path, name, records)
            graph = IutGraph.load(dir_path)
        self.assertEqual(len(graph.evidence), 0)

    def test_load_rejects_non_graph_document(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dir_path = Path(tmp)
            (dir_path / "entities.json").write_text(
                json.dumps({"@context": {}, "items": []}), encoding="utf-8",
            )
            with self.assertRaises(ValueError) as ctx:
                IutGraph.load(dir_path)
            self.assertIn("@graph", str(ctx.exception))


class EntityDataclassTests(unittest.TestCase):
    def test_full_field_population(self) -> None:
        record = _baseline_records()["entities.json"][0]
        entity = IutGraph._to_entity(record)
        self.assertEqual(entity.id, "iut:Cor.3.12")
        self.assertEqual(entity.type, "Corollary")
        self.assertEqual(entity.alt_labels, ("Cor 3.12",))
        self.assertEqual(entity.depends_on, ("iut:multiradial_algorithm",))
        self.assertEqual(entity.introduced_by, "paper:IUTchIII")
        self.assertEqual(entity.defined_in, "paper:IUTchIII")
        self.assertEqual(entity.informal_md, "docs/section_6_cor_3_12.md")
        self.assertEqual(entity.lean_module, "IutStatus.Cor312")
        self.assertIsNone(entity.role)

    def test_optional_fields_default_none_or_empty(self) -> None:
        minimal = {
            "id": "iut:bare",
            "type": "Concept",
            "label": "Bare concept",
            "section": "01_prerequisites",
            "verified_at": "2026-05-07",
        }
        entity = IutGraph._to_entity(minimal)
        self.assertEqual(entity.alt_labels, ())
        self.assertEqual(entity.depends_on, ())
        self.assertIsNone(entity.introduced_by)
        self.assertIsNone(entity.role)

    def test_missing_required_field_raises_value_error(self) -> None:
        broken = {"id": "iut:x", "type": "Concept", "label": "x"}
        with self.assertRaises(ValueError) as ctx:
            IutGraph._to_entity(broken)
        self.assertIn("missing required field", str(ctx.exception))


class ClaimDataclassTests(unittest.TestCase):
    def test_full_field_population(self) -> None:
        record = _baseline_records()["claims.json"][0]
        claim = IutGraph._to_claim(record)
        self.assertEqual(claim.id, "claim:test_claim")
        self.assertEqual(claim.type, "Claim")
        self.assertEqual(claim.proponents, ("A",))
        self.assertEqual(claim.counters, ("claim:other",))
        self.assertEqual(claim.relates_to, ("claim:third",))
        self.assertEqual(claim.specific_support, "Reason for support.")
        self.assertEqual(claim.peer_review_status, "peer_reviewed")
        self.assertIsNone(claim.specific_objection)


class EvidenceDataclassTests(unittest.TestCase):
    def test_full_field_population(self) -> None:
        record = _baseline_records()["evidence.json"][0]
        ev = IutGraph._to_evidence(record)
        self.assertEqual(ev.id, "evidence:test")
        self.assertEqual(ev.type, "Paper")
        self.assertEqual(ev.url, "https://example.org/x.pdf")
        self.assertEqual(ev.archive_url, "https://web.archive.org/web/x.pdf")
        self.assertEqual(ev.doi, "10.0000/test")
        self.assertEqual(ev.publisher, "Test Press")


class TimelineDataclassTests(unittest.TestCase):
    def test_full_field_population(self) -> None:
        record = _baseline_records()["timeline.json"][0]
        ev = IutGraph._to_timeline(record)
        self.assertEqual(ev.id, "event:test")
        self.assertEqual(ev.actors, ("A", "B"))
        self.assertEqual(ev.url, "https://example.org/event")
        self.assertEqual(ev.archive_url, "https://web.archive.org/web/event")

    def test_actors_default_empty_tuple(self) -> None:
        record = {
            "id": "event:bare",
            "type": "event",
            "label": "Bare event",
            "date": "2020-01-01",
        }
        ev = IutGraph._to_timeline(record)
        self.assertEqual(ev.actors, ())
        self.assertIsNone(ev.url)
        self.assertIsNone(ev.archive_url)


class GraphQueryTests(unittest.TestCase):
    def setUp(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            dir_path = Path(tmp)
            recs = _baseline_records()
            # add a counter-claim so opposing_pairs has a hit
            recs["claims.json"].append({
                "id": "claim:other",
                "type": "Claim",
                "label": "Other claim that opposes the first one.",
                "about": "iut:Cor.3.12",
                "position": "alleged_gap",
                "stance": "critical",
                "proponents": ["B"],
                "asserted_at": "2021-01-01",
                "evidence": ["evidence:test"],
                "counters": ["claim:test_claim"],
                "verified_at": "2026-05-07",
            })
            for name, records in recs.items():
                _write_graph(dir_path, name, records)
            self.graph = IutGraph.load(dir_path)

    def test_entity_lookup(self) -> None:
        self.assertIsInstance(self.graph.entity("iut:Cor.3.12"), Entity)
        self.assertIsNone(self.graph.entity("iut:does_not_exist"))

    def test_claim_lookup(self) -> None:
        self.assertIsInstance(self.graph.claim("claim:test_claim"), Claim)
        self.assertIsNone(self.graph.claim("claim:does_not_exist"))

    def test_claims_about_returns_all_pointing_at_target(self) -> None:
        cs = self.graph.claims_about("iut:Cor.3.12")
        self.assertEqual(len(cs), 2)
        ids = {c.id for c in cs}
        self.assertEqual(ids, {"claim:test_claim", "claim:other"})

    def test_opposing_pairs_returns_directed_pairs(self) -> None:
        pairs = self.graph.opposing_pairs()
        # Both fixture claims carry a `counters` edge pointing at the
        # other → 2 directed pairs returned (one per direction). The
        # iterator order follows graph.claims insertion order.
        self.assertEqual(len(pairs), 2)
        ids = {(c.id, t.id) for c, t in pairs}
        self.assertEqual(
            ids,
            {("claim:test_claim", "claim:other"),
             ("claim:other", "claim:test_claim")},
        )

    def test_claims_by_position(self) -> None:
        valid = self.graph.claims_by_position("valid")
        gap = self.graph.claims_by_position("alleged_gap")
        self.assertEqual([c.id for c in valid], ["claim:test_claim"])
        self.assertEqual([c.id for c in gap], ["claim:other"])

    def test_claims_by_peer_review(self) -> None:
        peer = self.graph.claims_by_peer_review("peer_reviewed")
        self.assertEqual([c.id for c in peer], ["claim:test_claim"])

    def test_frozen_dataclass_immutability(self) -> None:
        entity = self.graph.entity("iut:Cor.3.12")
        with self.assertRaises(Exception):
            # frozen=True on the dataclass makes setattr raise
            entity.label = "mutated"  # type: ignore[misc]


class LiveGraphSmokeTests(unittest.TestCase):
    """Sanity check that loading the actual ``data/`` succeeds.

    This is a lightweight smoke test only — semantic content is the
    domain of test_validation. Here we verify that the loader can
    consume what's currently checked in.
    """

    def test_load_live_data(self) -> None:
        graph = IutGraph.load(REPO_ROOT / "data")
        self.assertGreater(len(graph.entities), 50)
        self.assertGreater(len(graph.claims), 20)
        self.assertGreater(len(graph.evidence), 10)
        self.assertGreater(len(graph.timeline), 5)


if __name__ == "__main__":
    unittest.main()
