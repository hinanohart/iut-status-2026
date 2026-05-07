#!/usr/bin/env python3
"""Unit tests for ``tools/render_md.py``.

Architect Sec 8 deferred coverage (closed at v0.7.10): the renderer is on
the critical drift-zero contract path (regenerates committed
``docs/{overview,disputes,timeline}.md``), but it had no direct unit
tests until now. The CI ``Render docs and check committed artefacts in
sync`` step exercised the renderer end-to-end against a real graph,
which catches *some* regressions but cannot pinpoint failures and runs
on every PR rather than expressing the contract.

These tests pin the contract per render function:

- ``render_overview``  — entity grouping by section, claim count line
- ``render_disputes``  — opposing pairs, evidence URL + archive_url
- ``render_timeline``  — chronological sort, actor formatting
- ``_render_claim``    — every dataclass field that should surface

Tests construct minimal in-memory ``IutGraph`` instances so they are
independent of the live ``data/`` files and stable under additions to
the real graph.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from loaders.python_minimal import (  # noqa: E402
    Claim, Entity, Evidence, IutGraph, TimelineEvent,
)
from tools.render_md import (  # noqa: E402
    GENERATED_BANNER,
    _render_claim,
    render_disputes,
    render_overview,
    render_timeline,
)


def _make_minimal_graph() -> IutGraph:
    """Construct a deterministic 2-entity / 2-claim / 1-evidence /
    1-timeline graph for assertion convenience."""
    graph = IutGraph()
    graph.entities["iut:Cor.3.12"] = Entity(
        id="iut:Cor.3.12",
        type="Corollary",
        label="Corollary 3.12 (multiradial)",
        section="06_cor_3_12",
        verified_at="2026-05-07",
        alt_labels=("Cor 3.12",),
        introduced_by="paper:IUTchIII",
        introduced_year="2012",
        depends_on=("iut:multiradial_algorithm",),
        lean_module="IutStatus.Cor312",
    )
    graph.entities["iut:multiradial_algorithm"] = Entity(
        id="iut:multiradial_algorithm",
        type="Concept",
        label="Multiradial algorithm",
        section="05_multiradial",
        verified_at="2026-05-07",
    )
    graph.evidence["evidence:iutchiii"] = Evidence(
        id="evidence:iutchiii",
        type="Paper",
        label="IUTchIII paper",
        url="https://example.org/iut3.pdf",
        archive_url="https://web.archive.org/web/2026/iut3.pdf",
        doi="10.4171/PRIMS/57-1-3",
    )
    graph.claims["claim:mochizuki_cor312_proof"] = Claim(
        id="claim:mochizuki_cor312_proof",
        type="Claim",
        label="Mochizuki asserts the proof of Corollary 3.12 is valid.",
        about="iut:Cor.3.12",
        position="valid",
        stance="supportive",
        proponents=("Mochizuki",),
        asserted_at="2012-08-01",
        evidence=("evidence:iutchiii",),
        verified_at="2026-05-07",
        specific_support="Cor.3.12 closes the indeterminacy chain via §3.10–3.11.",
        peer_review_status="peer_reviewed",
    )
    graph.claims["claim:scholze_stix_objection"] = Claim(
        id="claim:scholze_stix_objection",
        type="Claim",
        label="Scholze and Stix object that §3.11 collapses to identity.",
        about="iut:Cor.3.12",
        position="alleged_gap",
        stance="critical",
        proponents=("Scholze", "Stix"),
        asserted_at="2018-09-20",
        evidence=("evidence:iutchiii",),
        counters=("claim:mochizuki_cor312_proof",),
        verified_at="2026-05-07",
        specific_objection="The redundant copies are identified mod natural isomorphism.",
    )
    graph.timeline["event:ss_visit"] = TimelineEvent(
        id="event:ss_visit",
        type="event",
        label="Scholze + Stix visit RIMS for week-long discussion",
        date="2018-03-15",
        actors=("Mochizuki", "Scholze", "Stix"),
        url="https://example.org/ss-visit-2018.html",
    )
    return graph


class OverviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = _make_minimal_graph()
        self.out = render_overview(self.graph)

    def test_starts_with_generated_banner(self) -> None:
        self.assertTrue(self.out.startswith(GENERATED_BANNER))

    def test_groups_entities_by_section(self) -> None:
        self.assertIn("## 05_multiradial", self.out)
        self.assertIn("## 06_cor_3_12", self.out)

    def test_section_groups_appear_alphabetically(self) -> None:
        # 05 must come before 06 (sorted)
        self.assertLess(
            self.out.index("## 05_multiradial"),
            self.out.index("## 06_cor_3_12"),
        )

    def test_renders_iri_as_inline_code_anchor(self) -> None:
        self.assertIn("`iut:Cor.3.12`", self.out)
        self.assertIn("`iut:multiradial_algorithm`", self.out)

    def test_alt_labels_emitted_when_present(self) -> None:
        self.assertIn("aliases: Cor 3.12", self.out)

    def test_introduced_by_and_year_emitted(self) -> None:
        self.assertIn("introduced by: paper:IUTchIII", self.out)
        self.assertIn("year: 2012", self.out)

    def test_depends_on_inline_code_listing(self) -> None:
        self.assertIn("depends on: `iut:multiradial_algorithm`", self.out)

    def test_lean_module_surfaced(self) -> None:
        self.assertIn("Lean module: `IutStatus.Cor312`", self.out)

    def test_claim_count_line_for_entity_with_claims(self) -> None:
        # Cor.3.12 has 2 claims pointing at it
        self.assertIn("claims about: 2", self.out)

    def test_no_claim_line_for_entity_without_claims(self) -> None:
        # multiradial_algorithm has 0 claims about it directly in fixture
        # — assert the line is absent for that section. We split by the
        # section header to be precise.
        idx = self.out.index("## 05_multiradial")
        next_section = self.out.index("## 06_cor_3_12")
        block = self.out[idx:next_section]
        self.assertNotIn("claims about:", block)


class DisputesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = _make_minimal_graph()
        self.out = render_disputes(self.graph)

    def test_opposing_pairs_section_lists_counter(self) -> None:
        self.assertIn("Opposing pairs", self.out)
        self.assertIn(
            "`claim:scholze_stix_objection` counters `claim:mochizuki_cor312_proof`",
            self.out,
        )

    def test_no_synthesis_label_neutrality(self) -> None:
        # Renderer must NOT introduce editorial words like "wrong" /
        # "correct" / "consensus". Probe a few canaries.
        for canary in ("consensus", "settled", "debunked", "obviously"):
            self.assertNotIn(canary, self.out.lower())

    def test_claims_sorted_by_assertion_date(self) -> None:
        # Within the "All claims" section, 2012-08-01 (Mochizuki) must
        # precede 2018-09-20 (SS). Note: ids appear earlier in the
        # "Opposing pairs" section too, so we anchor the search after
        # the "All claims" header.
        all_claims_idx = self.out.index("All claims")
        section = self.out[all_claims_idx:]
        self.assertLess(
            section.index("claim:mochizuki_cor312_proof"),
            section.index("claim:scholze_stix_objection"),
        )

    def test_evidence_link_emits_archive_url_when_present(self) -> None:
        self.assertIn(
            "[IUTchIII paper](https://example.org/iut3.pdf)",
            self.out,
        )
        self.assertIn(
            "([archive](https://web.archive.org/web/2026/iut3.pdf))",
            self.out,
        )

    def test_evidence_link_omits_archive_when_absent(self) -> None:
        # Mutate the fixture to drop archive_url
        graph = _make_minimal_graph()
        ev = graph.evidence["evidence:iutchiii"]
        graph.evidence["evidence:iutchiii"] = Evidence(
            id=ev.id, type=ev.type, label=ev.label, url=ev.url,
        )
        out = render_disputes(graph)
        self.assertIn("[IUTchIII paper](https://example.org/iut3.pdf)", out)
        self.assertNotIn("([archive]", out)


class ClaimRenderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = _make_minimal_graph()

    def test_specific_support_surfaces_only_when_set(self) -> None:
        claim = self.graph.claims["claim:mochizuki_cor312_proof"]
        out = _render_claim(claim, self.graph)
        self.assertIn("specific support:", out)
        self.assertIn("§3.10–3.11", out)

    def test_specific_objection_surfaces_only_when_set(self) -> None:
        claim = self.graph.claims["claim:scholze_stix_objection"]
        out = _render_claim(claim, self.graph)
        self.assertIn("specific objection:", out)

    def test_neither_field_surfaces_when_absent(self) -> None:
        graph = _make_minimal_graph()
        c = graph.claims["claim:mochizuki_cor312_proof"]
        cleared = Claim(
            id=c.id, type=c.type, label=c.label, about=c.about,
            position=c.position, stance=c.stance,
            proponents=c.proponents, asserted_at=c.asserted_at,
            evidence=c.evidence, verified_at=c.verified_at,
        )
        out = _render_claim(cleared, graph)
        self.assertNotIn("specific support:", out)
        self.assertNotIn("specific objection:", out)

    def test_position_and_stance_both_surfaced(self) -> None:
        claim = self.graph.claims["claim:mochizuki_cor312_proof"]
        out = _render_claim(claim, self.graph)
        self.assertIn("position: **valid**", out)
        self.assertIn("stance: **supportive**", out)

    def test_missing_evidence_record_surfaces_iri_placeholder(self) -> None:
        graph = _make_minimal_graph()
        graph.evidence.pop("evidence:iutchiii")
        claim = graph.claims["claim:mochizuki_cor312_proof"]
        out = _render_claim(claim, graph)
        self.assertIn("`evidence:iutchiii` (record not yet in evidence.json)", out)


class TimelineRenderTests(unittest.TestCase):
    def test_renders_with_actors(self) -> None:
        graph = _make_minimal_graph()
        out = render_timeline(graph)
        self.assertIn(
            "**2018-03-15** — Scholze + Stix visit RIMS for week-long discussion",
            out,
        )
        self.assertIn(
            "actors: Mochizuki, Scholze, Stix",
            out,
        )

    def test_renders_em_dash_when_no_actors(self) -> None:
        graph = _make_minimal_graph()
        ev = graph.timeline["event:ss_visit"]
        graph.timeline["event:ss_visit"] = TimelineEvent(
            id=ev.id, type=ev.type, label=ev.label, date=ev.date,
        )
        out = render_timeline(graph)
        self.assertIn("(actors: —)", out)

    def test_chronological_sort(self) -> None:
        graph = _make_minimal_graph()
        graph.timeline["event:earlier"] = TimelineEvent(
            id="event:earlier", type="event",
            label="2012 IUTchIII posted", date="2012-08-01",
        )
        out = render_timeline(graph)
        self.assertLess(out.index("2012-08-01"), out.index("2018-03-15"))


class GeneratedBannerInvariantTests(unittest.TestCase):
    """The auto-generated banner must precede every rendered file so
    the `Render docs and check committed artefacts in sync` CI gate
    has a canonical ``DO NOT EDIT BY HAND`` marker.
    """

    def test_overview_has_banner(self) -> None:
        graph = _make_minimal_graph()
        self.assertTrue(render_overview(graph).startswith(GENERATED_BANNER))

    def test_disputes_has_banner(self) -> None:
        graph = _make_minimal_graph()
        self.assertTrue(render_disputes(graph).startswith(GENERATED_BANNER))

    def test_timeline_has_banner(self) -> None:
        graph = _make_minimal_graph()
        self.assertTrue(render_timeline(graph).startswith(GENERATED_BANNER))

    def test_banner_contains_do_not_edit(self) -> None:
        self.assertIn("DO NOT EDIT BY HAND", GENERATED_BANNER)


if __name__ == "__main__":
    unittest.main()
