#!/usr/bin/env python3
"""Minimal stdlib-only loader for iut-status-2026 JSON-LD data files.

Zero external dependencies. Python 3.10+. Reads `data/*.json` files
shipped with the repository and exposes a typed object graph for
inspection by humans, programs, and LLM tool-use sandboxes.

The loader does NOT perform JSON-LD expansion (no `@context`
resolution to absolute IRIs). For full RDF semantics, use a separate
`pyld` install.

Drift-zero contract
-------------------
This loader and the JSON-LD files together form the source of truth.
The `@id` of an entity, claim, evidence record, or timeline event is
the stable IRI; cross-tool consistency is guaranteed at the IRI
level by `tools/validate.py`. Prose in `docs/` is a human-readable
view, not source of truth.

Usage::

    from loaders.python_minimal import IutGraph
    graph = IutGraph.load("data/")
    cor312 = graph.entity("iut:Cor.3.12")
    claims = graph.claims_about("iut:Cor.3.12")
    for c in claims:
        print(c.label, c.position, c.proponents)
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class Entity:
    id: str
    type: str
    label: str
    section: str
    verified_at: str
    alt_labels: tuple[str, ...] = ()
    introduced_by: str | None = None
    introduced_year: str | None = None
    defined_in: str | None = None
    depends_on: tuple[str, ...] = ()
    informal_md: str | None = None
    lean_stub: str | None = None
    lean_module: str | None = None


@dataclass(frozen=True, slots=True)
class Claim:
    id: str
    type: str
    label: str
    about: str
    position: str
    stance: str
    proponents: tuple[str, ...]
    asserted_at: str
    evidence: tuple[str, ...]
    verified_at: str
    counters: tuple[str, ...] = ()
    supports: tuple[str, ...] = ()
    relates_to: tuple[str, ...] = ()
    specific_objection: str | None = None
    fair_use_note: str | None = None
    status: str | None = None
    peer_review_status: str | None = None


@dataclass(frozen=True, slots=True)
class Evidence:
    id: str
    type: str
    label: str
    url: str | None = None
    doi: str | None = None
    isbn: str | None = None
    publisher: str | None = None
    asserted_at: str | None = None


@dataclass(frozen=True, slots=True)
class TimelineEvent:
    id: str
    type: str
    label: str
    date: str
    actors: tuple[str, ...] = ()


@dataclass
class IutGraph:
    entities: dict[str, Entity] = field(default_factory=dict)
    claims: dict[str, Claim] = field(default_factory=dict)
    evidence: dict[str, Evidence] = field(default_factory=dict)
    timeline: dict[str, TimelineEvent] = field(default_factory=dict)

    @classmethod
    def load(cls, data_dir: str | Path) -> "IutGraph":
        data_path = Path(data_dir)
        if not data_path.is_dir():
            raise FileNotFoundError(f"data_dir not a directory: {data_path}")

        graph = cls()

        for record in cls._read_graph(data_path / "entities.json"):
            entity = cls._to_entity(record)
            graph.entities[entity.id] = entity

        for record in cls._read_graph(data_path / "claims.json"):
            claim = cls._to_claim(record)
            graph.claims[claim.id] = claim

        evidence_path = data_path / "evidence.json"
        if evidence_path.exists():
            for record in cls._read_graph(evidence_path):
                ev = cls._to_evidence(record)
                graph.evidence[ev.id] = ev

        for record in cls._read_graph(data_path / "timeline.json"):
            event = cls._to_timeline(record)
            graph.timeline[event.id] = event

        logger.info(
            "loaded graph: entities=%d claims=%d evidence=%d timeline=%d",
            len(graph.entities), len(graph.claims),
            len(graph.evidence), len(graph.timeline),
        )
        return graph

    def entity(self, iri: str) -> Entity | None:
        return self.entities.get(iri)

    def claim(self, iri: str) -> Claim | None:
        return self.claims.get(iri)

    def claims_about(self, target_iri: str) -> list[Claim]:
        return [c for c in self.claims.values() if c.about == target_iri]

    def opposing_pairs(self) -> list[tuple[Claim, Claim]]:
        pairs: list[tuple[Claim, Claim]] = []
        for claim in self.claims.values():
            for other_id in claim.counters:
                other = self.claims.get(other_id)
                if other is not None:
                    pairs.append((claim, other))
        return pairs

    def claims_by_position(self, position: str) -> list[Claim]:
        return [c for c in self.claims.values() if c.position == position]

    def claims_by_peer_review(self, status: str) -> list[Claim]:
        return [c for c in self.claims.values() if c.peer_review_status == status]

    @staticmethod
    def _read_graph(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            raise FileNotFoundError(f"required data file missing: {path}")
        with path.open("r", encoding="utf-8") as fh:
            doc = json.load(fh)
        if "@graph" not in doc or not isinstance(doc["@graph"], list):
            raise ValueError(f"{path} missing @graph array")
        return doc["@graph"]

    @staticmethod
    def _to_entity(record: dict[str, Any]) -> Entity:
        try:
            return Entity(
                id=record["id"],
                type=record["type"],
                label=record["label"],
                section=record["section"],
                verified_at=record["verified_at"],
                alt_labels=tuple(record.get("alt_labels", ())),
                introduced_by=record.get("introduced_by"),
                introduced_year=record.get("introduced_year"),
                defined_in=record.get("definedIn"),
                depends_on=tuple(record.get("depends_on", ())),
                informal_md=record.get("informal_md"),
                lean_stub=record.get("lean_stub"),
                lean_module=record.get("lean_module"),
            )
        except KeyError as exc:
            raise ValueError(f"entity missing required field {exc}: {record}") from exc

    @staticmethod
    def _to_claim(record: dict[str, Any]) -> Claim:
        try:
            return Claim(
                id=record["id"],
                type=record["type"],
                label=record["label"],
                about=record["about"],
                position=record["position"],
                stance=record["stance"],
                proponents=tuple(record["proponents"]),
                asserted_at=record["asserted_at"],
                evidence=tuple(record["evidence"]),
                verified_at=record["verified_at"],
                counters=tuple(record.get("counters", ())),
                supports=tuple(record.get("supports", ())),
                relates_to=tuple(record.get("relates_to", ())),
                specific_objection=record.get("specific_objection"),
                fair_use_note=record.get("fair_use_note"),
                status=record.get("status"),
                peer_review_status=record.get("peer_review_status"),
            )
        except KeyError as exc:
            raise ValueError(f"claim missing required field {exc}: {record}") from exc

    @staticmethod
    def _to_evidence(record: dict[str, Any]) -> Evidence:
        try:
            return Evidence(
                id=record["id"],
                type=record["type"],
                label=record["label"],
                url=record.get("url"),
                doi=record.get("doi"),
                isbn=record.get("isbn"),
                publisher=record.get("publisher"),
                asserted_at=record.get("asserted_at"),
            )
        except KeyError as exc:
            raise ValueError(f"evidence missing required field {exc}: {record}") from exc

    @staticmethod
    def _to_timeline(record: dict[str, Any]) -> TimelineEvent:
        try:
            return TimelineEvent(
                id=record["id"],
                type=record["type"],
                label=record["label"],
                date=record["date"],
                actors=tuple(record.get("actors", ())),
            )
        except KeyError as exc:
            raise ValueError(f"timeline missing required field {exc}: {record}") from exc


def main() -> int:
    """CLI: print summary of the graph at ./data/."""
    import argparse

    parser = argparse.ArgumentParser(description="iut-status-2026 minimal loader")
    parser.add_argument("--data", default="data", help="data directory")
    parser.add_argument("--iri", help="optional: print entity or claim by IRI")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    graph = IutGraph.load(args.data)

    if args.iri:
        entity = graph.entity(args.iri)
        if entity:
            print(json.dumps(entity.__dict__, indent=2, default=list, ensure_ascii=False))
            return 0
        claim = graph.claim(args.iri)
        if claim:
            print(json.dumps(claim.__dict__, indent=2, default=list, ensure_ascii=False))
            return 0
        print(f"unknown IRI: {args.iri}")
        return 2

    print(f"entities: {len(graph.entities)}")
    print(f"claims:   {len(graph.claims)}")
    print(f"evidence: {len(graph.evidence)}")
    print(f"timeline: {len(graph.timeline)}")
    print(f"opposing pairs: {len(graph.opposing_pairs())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
