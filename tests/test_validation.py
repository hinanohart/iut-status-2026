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

import json
import re
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

    def test_every_schema_property_has_context_mapping(self) -> None:
        # Round 8 audit (v0.7.7): archive_url (added v0.7.0) and role
        # (added v0.7.2) were defined in schemas but missing from
        # data/context.jsonld → JSON-LD processors silently dropped
        # the values on expansion. This test pins down that every
        # property declared in any schemas/*.json has a context entry.
        import json
        ctx = json.loads(
            (REPO_ROOT / "data" / "context.jsonld").read_text(encoding="utf-8")
        )["@context"]
        ctx_keys = set(ctx.keys())
        # Schema-only synthetic JSON-Schema vocabulary terms that don't
        # belong in the JSON-LD context.
        EXEMPT = {"id", "type"}
        for schema_file in ("entity.json", "claim.json", "evidence.json", "timeline.json"):
            schema = json.loads(
                (REPO_ROOT / "schemas" / schema_file).read_text(encoding="utf-8")
            )
            properties = set(schema.get("properties", {}).keys())
            missing = properties - ctx_keys - EXEMPT
            self.assertEqual(
                missing, set(),
                f"schemas/{schema_file}: properties {missing} have no "
                f"data/context.jsonld mapping (JSON-LD processors will "
                f"drop them on expansion)",
            )

    def test_audit_known_corrections_not_in_docs(self) -> None:
        # Round 9 audit (v0.7.8): generalised the Round 8 single-needle
        # ISBN regression to a list of "known corrections" — strings
        # that were once cited but proven fabricated / drifted, and
        # must therefore not survive in any docs/*.md outside the
        # explicit fabrication-record allowlist. Adding a new entry
        # here closes a future drift class in one line.
        # Round 10 audit (v0.7.13): expanded both ways. (a) FABRICATIONS
        # now covers Joshi v2 (R5 closure regression — a "v2 (2026-05-02)"
        # link survived in README.md:276 across 5 releases because the
        # scan scope was docs/ only). (b) scan scope expanded to repo
        # root *.md (README, LLM_CONTEXT, CONTRIBUTING, NOTICE) so the
        # next regression at this layer surfaces immediately.
        FABRICATIONS: list[tuple[str, str]] = [
            # (needle, round-where-fixed)
            ("978-4-04-110262-7", "R7 Kato ISBN"),
            ("ems.press/journals/prims/issues/249", "R7 PRIMS issue ID"),
            ("2505.10568v2", "R5 Joshi v2 fictional version (R10 readded check)"),
            ("2026-05-02", "R5 Joshi v2 fictional date (R10 readded check)"),
            ("Joshi v1+v2", "R5 Joshi v2 prose retention (R10)"),
            ("Joshi v1 / v2", "R5 Joshi v2 prose retention (R10)"),
            ("iut:Theta-link", "R10 docs IRI typo (snake_case is canonical)"),
            ("iut:log-link", "R10 docs IRI typo (snake_case is canonical)"),
            ("woit_blog_2025_skeptical", "R10 docs Woit IRI mismatch with data/"),
            ("evidence:Woit_blog_2025", "R10 docs Woit IRI mismatch with data/"),
        ]
        ALLOWED = {
            REPO_ROOT / "docs" / "INNOVATION_LOG.md",
            REPO_ROOT / "docs" / "AUDIT_PROVENANCE.md",
            # The validation test file itself enumerates the needles:
            REPO_ROOT / "tests" / "test_validation.py",
        }
        # Round 10 (v0.7.13): per-(file, needle) allowlist for legitimate
        # historical records — release notes / audit prose that *document*
        # a past fabrication for transparency. Anything not here is treated
        # as a regression.
        DOCUMENTED_AS_FABRICATION: set[tuple[Path, str]] = {
            # README v0.7.11 release-table entry references the R7 Kato ISBN
            # while explaining that NDL Search now flags it as `invalid`.
            (REPO_ROOT / "README.md", "978-4-04-110262-7"),
            # section_6 explicitly notes Round 5 removed the fictional v2.
            (REPO_ROOT / "docs" / "section_6_cor_3_12.md", "2026-05-02"),
        }
        offenders: list[tuple[Path, str]] = []
        # Round 10 (v0.7.13): scan repo-root *.md too (README, LLM_CONTEXT,
        # CONTRIBUTING, NOTICE), not just docs/.
        md_files: list[Path] = list((REPO_ROOT / "docs").rglob("*.md"))
        md_files += [p for p in REPO_ROOT.glob("*.md")]
        for path in md_files:
            if path in ALLOWED:
                continue
            text = path.read_text(encoding="utf-8")
            for needle, label in FABRICATIONS:
                if needle in text and (path, needle) not in DOCUMENTED_AS_FABRICATION:
                    offenders.append((path, label))
        self.assertEqual(
            offenders, [],
            "fabricated / drifted strings retained in docs/: "
            + ", ".join(
                f"{p.relative_to(REPO_ROOT)} ({label})"
                for p, label in offenders
            ),
        )

    def test_section_docs_iris_resolve_in_data(self) -> None:
        """Round 10 audit (v0.7.13) gate: every (iut|claim|evidence|event):*
        IRI cited inside ``docs/section_*.md`` must resolve to a record
        in ``data/``.

        Class background: Round 5/6/8/9 each surfaced "docs cite an IRI
        that has been renamed or never existed" as a CRITICAL
        fabrication-class defect. The auto-generated docs (overview /
        disputes / timeline) are diff-gated against ``render_md.py``
        output, but the curated ``section_*.md`` family was not. This
        test closes that gap.
        """
        graph = IutGraph.load(DATA_DIR)
        known_ids: set[str] = (
            set(graph.entities.keys())
            | set(graph.claims.keys())
            | set(graph.evidence.keys())
            | set(graph.timeline.keys())
        )
        # Pattern matches IRI tokens of the form `prefix:identifier`
        # inside backtick-quoted spans only — bare prose words like
        # "iut: introduction" are intentionally excluded by the
        # backtick anchor.
        # Round 11 audit (v0.7.14): char class extended to include
        # `.` and `-`. Without the `.` the regex was silently failing
        # to match `iut:Cor.3.12` — the central disputed corollary
        # cited 28 times across 6 section docs. The character class
        # now follows the `entity.json` pattern `[A-Za-z][A-Za-z0-9_.]*`
        # and additionally allows `-` for safety.
        iri_re = re.compile(
            r"`((?:iut|claim|evidence|event|person|paper|org):[A-Za-z][A-Za-z0-9_.\-]*)`"
        )
        offenders: list[tuple[Path, str]] = []
        for path in sorted((REPO_ROOT / "docs").glob("section_*.md")):
            text = path.read_text(encoding="utf-8")
            for match in iri_re.finditer(text):
                iri = match.group(1)
                if iri.startswith(("person:", "paper:", "org:")):
                    # person/paper/org are entities — also check entity registry.
                    if iri in graph.entities:
                        continue
                if iri in known_ids:
                    continue
                offenders.append((path, iri))
        self.assertEqual(
            offenders, [],
            "section docs cite IRIs that don't resolve in data/: "
            + ", ".join(
                f"{p.relative_to(REPO_ROOT)}:{iri}" for p, iri in offenders
            ),
        )

    def test_javascript_url_in_timeline_rejected(self) -> None:
        """Round 10 audit (v0.7.13) gate: timeline schema's `url` field
        must enforce ``format: uri`` + ``http(s)`` scheme, otherwise
        ``javascript:alert(1)`` / ``file:///etc/passwd`` / ``data:...``
        are silently accepted and propagate to MCP / docs.
        """
        schema_path = REPO_ROOT / "schemas" / "timeline.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        url_props = schema["properties"]["url"]
        self.assertEqual(
            url_props.get("format"), "uri",
            "timeline.json url field must declare format=uri",
        )
        pattern = url_props.get("pattern", "")
        self.assertTrue(
            pattern.startswith("^https?"),
            f"timeline.json url pattern must restrict to http(s); got {pattern!r}",
        )

    def test_url_scheme_pattern_uniform_across_schemas(self) -> None:
        """Round 11 audit (v0.7.14) gate: ``timeline.json`` was hardened
        in Round 10 but ``evidence.json`` was left half-fixed. Every URL
        field in every schema (``url`` and ``archive_url``) must enforce
        ``format=uri`` + ``^https?://`` pattern. Otherwise
        ``javascript:alert(1)`` / ``data:`` / ``file:`` survive at the
        schema layer and propagate to render_md → docs → static-site
        consumers.
        """
        url_field_locations = [
            ("schemas/timeline.json", "url"),
            ("schemas/timeline.json", "archive_url"),
            ("schemas/evidence.json", "url"),
            ("schemas/evidence.json", "archive_url"),
        ]
        for schema_rel, field in url_field_locations:
            schema = json.loads(
                (REPO_ROOT / schema_rel).read_text(encoding="utf-8")
            )
            props = schema["properties"].get(field, {})
            self.assertEqual(
                props.get("format"), "uri",
                f"{schema_rel}#properties.{field} must declare format=uri",
            )
            pattern = props.get("pattern", "")
            self.assertTrue(
                pattern.startswith("^https?"),
                f"{schema_rel}#properties.{field} must restrict to http(s); "
                f"got pattern={pattern!r}",
            )

    def test_documented_test_count_matches_collected(self) -> None:
        """Round 12 audit (v0.7.15) gate: README / ARCHITECTURE /
        INNOVATION_LOG documented test counts must be **at least** the
        real test count. Drift between those documents (R12 critic M1
        found 201/189/204 mismatch across the three) is a
        cosmetic-but-erodes-trust class. The gate accepts documents
        that say "204+ cases" / "204 cases" but rejects any document
        that understates the real count.

        Round 12.1 (v0.7.16) follow-up: switched from subprocess
        pytest invocation (returned 0 in CI because pytest isn't
        installed under unittest-driven CI) to `unittest.TestLoader`
        which is stdlib-only and matches the way CI runs tests.
        """
        loader = unittest.TestLoader()
        suite = loader.discover(start_dir=str(REPO_ROOT / "tests"), pattern="test_*.py")

        def _count_tests(s: unittest.TestSuite) -> int:
            n = 0
            for child in s:
                if isinstance(child, unittest.TestSuite):
                    n += _count_tests(child)
                else:
                    n += 1
            return n

        actual = _count_tests(suite)
        # Count anchor regex: matches "NNN cases" / "NNN unittest cases"
        # / "NNN tests" / "NNN tests PASS" in narrative prose. Documents
        # may use the "NNN+" suffix to mean "at least NNN".
        count_re = re.compile(r"\b(\d{2,4})\+?\s*(?:unittest\s+)?(?:cases|tests)\b")
        for rel in (
            "README.md",
            "docs/ARCHITECTURE.md",
            "docs/INNOVATION_LOG.md",
        ):
            text = (REPO_ROOT / rel).read_text(encoding="utf-8")
            for match in count_re.finditer(text):
                claimed = int(match.group(1))
                self.assertLessEqual(
                    claimed, actual,
                    f"{rel} claims {claimed} tests but unittest discovered "
                    f"{actual}; documented count must not exceed real count "
                    f"(matched fragment near offset {match.start()})",
                )

    def test_no_commit_pending_on_implemented_status(self) -> None:
        """Round 12 audit (v0.7.15) regression: v0.7.14 candidate FF
        itself left ``commit pending`` on its own ``Implemented`` line —
        a self-contradiction the v0.7.13 candidate-FF text claimed to
        have closed. Going forward, no candidate whose ``Status`` line
        contains ``Implemented`` may carry the literal text ``commit
        pending`` anywhere in its body.
        """
        log = (REPO_ROOT / "docs" / "INNOVATION_LOG.md").read_text(encoding="utf-8")
        # Split by the "### X." header pattern — innovation_explorer
        # uses the same regex, so this aligns with the live sentinel.
        sections = re.split(r"(?m)^### ([A-Z]+)\. ", log)
        # `sections[0]` is preamble; rest alternate (letter, body).
        # Match the placeholder STYLE only (the literal `(vX.Y.Z,
        # commit pending)`); free-form prose mentions of the term
        # (e.g. retraction notes) are legitimate and must not trip
        # the gate. Mirrors innovation_explorer's regex.
        placeholder_re = re.compile(r"\(v\d+(?:\.\d+){1,2},\s*commit pending\)")
        offenders: list[str] = []
        for i in range(1, len(sections), 2):
            letter = sections[i]
            body = sections[i + 1] if i + 1 < len(sections) else ""
            status_match = re.search(r"^- \*\*Status\*\*: *(.+)$", body, re.MULTILINE)
            if status_match is None:
                continue
            status_line = status_match.group(1)
            if "Implemented" not in status_line:
                continue
            if placeholder_re.search(body):
                offenders.append(letter)
        self.assertEqual(
            offenders, [],
            "INNOVATION_LOG.md candidates with Implemented status must "
            "carry an actual commit SHA, not the placeholder "
            f"'(vX.Y.Z, commit pending)'. Offenders: {offenders}",
        )

    def test_javascript_url_in_evidence_rejected(self) -> None:
        """Round 12 audit (v0.7.15) gate: parity with the v0.7.13
        timeline.url regression — both evidence.url and evidence.archive_url
        must enforce ``format: uri`` + ``^https?://`` pattern.
        """
        schema = json.loads(
            (REPO_ROOT / "schemas" / "evidence.json").read_text(encoding="utf-8")
        )
        for field in ("url", "archive_url"):
            props = schema["properties"].get(field, {})
            self.assertEqual(
                props.get("format"), "uri",
                f"evidence.json {field} must declare format=uri",
            )
            pattern = props.get("pattern", "")
            self.assertTrue(
                pattern.startswith("^https?"),
                f"evidence.json {field} must restrict to http(s); "
                f"got pattern={pattern!r}",
            )

    def test_section_iri_gate_finds_dotted_iris(self) -> None:
        """Round 11 audit (v0.7.14) positive control: the section IRI
        gate must observe at least one IRI containing a dot (e.g.
        ``iut:Cor.3.12``) when scanning ``docs/section_*.md``. Without
        this control the Round-10 regex character class
        ``[A-Za-z0-9_]+`` silently bypassed the central disputed
        corollary across 28 citations.
        """
        iri_re = re.compile(
            r"`((?:iut|claim|evidence|event|person|paper|org):[A-Za-z][A-Za-z0-9_.\-]*)`"
        )
        seen_dotted = False
        for path in (REPO_ROOT / "docs").glob("section_*.md"):
            text = path.read_text(encoding="utf-8")
            for match in iri_re.finditer(text):
                if "." in match.group(1):
                    seen_dotted = True
                    break
            if seen_dotted:
                break
        self.assertTrue(
            seen_dotted,
            "section IRI regex did not observe any dotted IRI; "
            "iut:Cor.3.12 (the central disputed corollary) must be visible "
            "to the gate. Round 11 regression guard.",
        )


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
        # Round 8 audit (v0.7.7): substring match was vulnerable to
        # comment / docstring text accidentally containing
        # `import IutStatus.X` — that would let a per-section file be
        # silently deleted while the test still passed. Now we strip
        # Lean comments first and match `^import\s+IutStatus\.\w+$`
        # only on code lines.
        import re
        basic = (REPO_ROOT / "lean" / "IutStatus" / "Basic.lean").read_text(
            encoding="utf-8"
        )
        # Strip /- ... -/ block comments (non-greedy, multi-line).
        basic_no_block = re.sub(r"/-.*?-/", "", basic, flags=re.DOTALL)
        # Strip `--` line comments.
        code_lines: list[str] = []
        for raw in basic_no_block.splitlines():
            stripped = raw.split("--", 1)[0].rstrip()
            if stripped:
                code_lines.append(stripped)
        actually_imported: set[str] = set()
        for line in code_lines:
            match = re.match(r"^import\s+(IutStatus\.\w+)\s*$", line)
            if match:
                actually_imported.add(match.group(1))
        for entity in self.graph.entities.values():
            if entity.lean_module is None:
                continue
            self.assertIn(
                entity.lean_module,
                actually_imported,
                f"Basic.lean missing import {entity.lean_module} for "
                f"{entity.id} (or import is inside a comment / docstring)",
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
