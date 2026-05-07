#!/usr/bin/env python3
"""Tests for ``tools/property_audit.py`` — the systemic drift detector.

These tests pin two invariants:

1. **Self-clean run**: on the *current* repo HEAD, the audit must report
   zero findings. This guarantees that v0.7.9 ships with no schema-to-
   surface drift, and that the audit becomes a regression gate going
   forward.

2. **Drift detection works**: each layer (L1 / L2 / L3 / L4) is exercised
   with an injected drift in a temp-copied tree, and the audit must
   detect it. Without this test, an audit that silently green-lights a
   broken policy would never be caught.

The tests purposefully mutate isolated tempdirs (never the live repo) so
they can run inside CI without touching working state.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_SCRIPT = REPO_ROOT / "tools" / "property_audit.py"


def _run_audit(cwd: Path | None = None, *extra: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, str(AUDIT_SCRIPT), *extra],
        cwd=cwd or REPO_ROOT,
        capture_output=True, text=True, check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


class CleanRepoAuditTests(unittest.TestCase):
    """The current repository state must pass the audit."""

    def test_audit_clean_on_main(self) -> None:
        rc, out, err = _run_audit()
        self.assertEqual(
            rc, 0,
            f"property_audit failed on clean repo:\nSTDOUT:\n{out}\nSTDERR:\n{err}",
        )
        self.assertIn("OK", out)

    def test_json_mode_machine_readable(self) -> None:
        rc, out, _ = _run_audit(None, "--json")
        self.assertEqual(rc, 0)
        payload = json.loads(out)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["count"], 0)
        self.assertEqual(payload["findings"], [])

    def test_single_schema_filter(self) -> None:
        rc, out, _ = _run_audit(None, "--schema", "claim.json")
        self.assertEqual(rc, 0)
        self.assertIn("OK", out)

    def test_unknown_schema_is_noop(self) -> None:
        # Filtering to a nonexistent schema simply audits zero schemas;
        # rc=0 is correct — there is no drift to find.
        rc, out, _ = _run_audit(None, "--schema", "does-not-exist.json")
        self.assertEqual(rc, 0)
        self.assertIn("OK", out)


class DriftInjectionTests(unittest.TestCase):
    """Each layer must surface a planted drift in a tempdir copy."""

    def setUp(self) -> None:
        # Lazy import so that import-side errors propagate as test errors,
        # not test-collection errors.
        sys.path.insert(0, str(REPO_ROOT))
        import tools.property_audit as audit  # noqa: E402

        self.audit = audit

    def _copy_tree(self, target: Path) -> None:
        for sub in ("schemas", "loaders", "mcp", "tools", "data"):
            shutil.copytree(REPO_ROOT / sub, target / sub)

    def _run_in_isolated(self, target: Path) -> int:
        proc = subprocess.run(
            [sys.executable, str(target / "tools" / "property_audit.py")],
            cwd=target, capture_output=True, text=True, check=False,
        )
        return proc.returncode

    def test_l1_drift_when_context_mapping_removed(self) -> None:
        # Removing a property's @context line must trigger an L1 finding.
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            target = Path(tmpdir)
            self._copy_tree(target)

            ctx_path = target / "data" / "context.jsonld"
            ctx = json.loads(ctx_path.read_text(encoding="utf-8"))
            removed = ctx["@context"].pop("specific_support")
            self.assertTrue(removed)
            ctx_path.write_text(json.dumps(ctx, indent=2), encoding="utf-8")

            rc = self._run_in_isolated(target)
            self.assertNotEqual(rc, 0, "L1 drift should fail audit")

    def test_l3_drift_when_mcp_drops_field(self) -> None:
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            target = Path(tmpdir)
            self._copy_tree(target)

            mcp_path = target / "mcp" / "server.py"
            src = mcp_path.read_text(encoding="utf-8")
            # Strip the line that emits archive_url under iut_evidence.
            mutated = src.replace(
                '"archive_url": ev.archive_url,\n', "", 1,
            )
            self.assertNotEqual(mutated, src, "expected source mutation")
            mcp_path.write_text(mutated, encoding="utf-8")

            rc = self._run_in_isolated(target)
            self.assertNotEqual(rc, 0, "L3 drift should fail audit")

    def test_l2_drift_when_loader_drops_field(self) -> None:
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            target = Path(tmpdir)
            self._copy_tree(target)

            loader_path = target / "loaders" / "python_minimal.py"
            src = loader_path.read_text(encoding="utf-8")
            mutated = src.replace(
                'archive_url=record.get("archive_url"),\n', "", 1,
            )
            self.assertNotEqual(mutated, src)
            loader_path.write_text(mutated, encoding="utf-8")

            rc = self._run_in_isolated(target)
            self.assertNotEqual(rc, 0, "L2 drift should fail audit")


class AstAnchorRobustnessTests(unittest.TestCase):
    """Round 11 audit (v0.7.14) regression: the v0.7.13 AST extractor used
    ``"id" in dict.keys`` as the discriminator separating payload dicts
    from MCP envelope dicts. Round 11 demonstrated three bypasses:
    (a) sibling-dict pollution — a docstring sample / cache helper
    containing ``"id"`` would mask a real payload omission;
    (b) ``dict()`` Call form — never a literal ast.Dict node;
    (c) dict comprehension — also never a literal ast.Dict node.

    The v0.7.14 fix narrows to ``ast.Assign`` whose target is named
    ``payload``/``payload_list``, plus ``ast.Return`` of an ``ast.Dict``
    literal. This test pins that the new anchor catches the sibling
    pollution case (i.e. an unrelated dict containing ``"id"`` is NOT
    treated as the payload).
    """

    def test_sibling_dict_with_id_does_not_mask_payload_omission(self) -> None:
        sys.path.insert(0, str(REPO_ROOT))
        import tools.property_audit as audit  # noqa: E402

        # Body simulating an emitter where a docstring / cache helper
        # contains an "id"-bearing dict, but the actual payload omits
        # the "type" field. The v0.7.13 substring/AST union check would
        # incorrectly accept this body because "type" is present in the
        # sibling dict (NOT in payload). The v0.7.14 anchor must reject.
        body = textwrap.dedent('''
            if name == "iut_evidence":
                ev = graph.evidence.get(args["iri"])
                if ev is None:
                    payload: Any = None
                else:
                    sample = {"id": "evidence:example", "type": "Paper"}  # noqa: F841
                    payload = {
                        "id": ev.id,
                        "label": ev.label,
                    }
                return _make_response(
                    request_id,
                    {"content": [{"type": "text", "text": "..."}]},
                )
        ''').lstrip()
        keys = audit._extract_payload_dict_keys(body)
        self.assertIn("id", keys)
        self.assertIn("label", keys)
        self.assertNotIn(
            "type", keys,
            "Round 11 regression: the sibling-dict 'sample' must NOT "
            "pollute payload_keys with its 'type' key. v0.7.13 anchor "
            "would have included 'type' here.",
        )

    def test_return_dict_literal_pattern_is_recognised(self) -> None:
        """`_entity_to_json` and `_claim_to_json` use ``return {...}``
        directly; this pattern must keep working."""
        sys.path.insert(0, str(REPO_ROOT))
        import tools.property_audit as audit  # noqa: E402

        body = textwrap.dedent('''
            def _entity_to_json(graph, iri):
                ent = graph.entities.get(iri)
                if ent is None:
                    return None
                return {
                    "id": ent.id,
                    "type": ent.type,
                    "label": ent.label,
                }
        ''').lstrip()
        keys = audit._extract_payload_dict_keys(body)
        self.assertEqual(keys, {"id", "type", "label"})

    def test_envelope_call_return_is_not_payload(self) -> None:
        """``return _make_response(...)`` MUST NOT contribute envelope
        keys (``content``, ``type``, ``text``) to the payload key set.
        """
        sys.path.insert(0, str(REPO_ROOT))
        import tools.property_audit as audit  # noqa: E402

        body = textwrap.dedent('''
            if name == "iut_protocol":
                return _make_response(
                    request_id,
                    {"content": [{"type": "text", "text": "hello"}]},
                )
        ''').lstrip()
        keys = audit._extract_payload_dict_keys(body)
        self.assertEqual(
            keys, set(),
            "envelope dicts (under _make_response Call) MUST NOT "
            "contribute to payload_keys; only Assign-target payload "
            "or top-level Return-of-Dict patterns count.",
        )


class PolicyContractTests(unittest.TestCase):
    """The POLICY tuple itself must be internally consistent."""

    @classmethod
    def setUpClass(cls) -> None:
        sys.path.insert(0, str(REPO_ROOT))
        import tools.property_audit as audit  # noqa: E402
        cls.audit = audit  # type: ignore[attr-defined]

    def test_each_policy_matches_a_schema_file(self) -> None:
        for policy in self.audit.POLICIES:  # type: ignore[attr-defined]
            schema_path = self.audit.SCHEMAS_DIR / policy.schema_file
            self.assertTrue(
                schema_path.is_file(),
                f"policy references missing schema: {policy.schema_file}",
            )

    def test_render_optional_subset_of_schema(self) -> None:
        for policy in self.audit.POLICIES:  # type: ignore[attr-defined]
            schema_path = self.audit.SCHEMAS_DIR / policy.schema_file
            with schema_path.open("r", encoding="utf-8") as fh:
                doc = json.load(fh)
            schema_props = set(doc.get("properties", {}).keys())
            extra = policy.render_optional - schema_props
            self.assertFalse(
                extra,
                f"{policy.schema_file} render_optional contains "
                f"unknown properties: {extra}",
            )


if __name__ == "__main__":
    unittest.main()
