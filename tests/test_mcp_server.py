"""Tests for mcp/server.py — JSON-RPC tool dispatch + serializer parity.

Round 9 audit (v0.7.8) found that ``archive_url`` (v0.7.0), ``role``
(v0.7.2), ``specific_support`` (longstanding) and ``lean_stub`` were
silently dropped by the MCP serializers. The drift-zero contract
demands every dataclass field reachable via ``IutGraph`` be exposable
through the MCP tools (or explicitly excluded with rationale).

These tests pin that invariant: every public field of every dataclass
must appear in the corresponding MCP serializer output.
"""
from __future__ import annotations

import dataclasses
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "mcp"))

from loaders.python_minimal import IutGraph  # noqa: E402
from mcp import server as mcp_server  # noqa: E402


DATA_DIR = REPO_ROOT / "data"


# Fields that are intentionally excluded from MCP responses with
# documented rationale. Empty for now; if a field is added that
# legitimately should not be exposed (e.g., raw PDF blob), document
# it here so the invariant test does not regress.
EXCLUDED: dict[str, set[str]] = {
    "Entity": set(),
    "Claim": {"type"},  # type is constant "Claim"; redundant with tool name
    "Evidence": set(),
    "TimelineEvent": set(),
}


class SerializerParityTests(unittest.TestCase):
    """Each MCP serializer must emit every public dataclass field."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = IutGraph.load(DATA_DIR)

    def _dataclass_fields(self, cls_name: str) -> set[str]:
        from loaders.python_minimal import (
            Entity, Claim, Evidence, TimelineEvent,
        )
        cls_map = {
            "Entity": Entity, "Claim": Claim,
            "Evidence": Evidence, "TimelineEvent": TimelineEvent,
        }
        return {f.name for f in dataclasses.fields(cls_map[cls_name])}

    def test_entity_serializer_emits_every_dataclass_field(self) -> None:
        sample = next(iter(self.graph.entities))
        payload = mcp_server._entity_to_json(self.graph, sample)
        self.assertIsNotNone(payload)
        emitted = set(payload.keys())  # type: ignore[union-attr]
        expected = self._dataclass_fields("Entity") - EXCLUDED["Entity"]
        # Allow the serializer to use `defined_in` rather than `defined_in`
        # vocabulary differences, but verify each canonical name has a slot.
        missing = expected - emitted
        self.assertEqual(
            missing, set(),
            f"_entity_to_json missing fields: {missing}",
        )

    def test_claim_serializer_emits_every_dataclass_field(self) -> None:
        sample = next(iter(self.graph.claims))
        payload = mcp_server._claim_to_json(self.graph, sample)
        self.assertIsNotNone(payload)
        emitted = set(payload.keys())  # type: ignore[union-attr]
        expected = self._dataclass_fields("Claim") - EXCLUDED["Claim"]
        missing = expected - emitted
        self.assertEqual(
            missing, set(),
            f"_claim_to_json missing fields: {missing}",
        )

    def test_specific_support_field_round_trips(self) -> None:
        # Pin a known claim with non-null specific_support to verify
        # the loader → MCP path delivers the field.
        for cid, claim in self.graph.claims.items():
            if claim.specific_support is not None:
                payload = mcp_server._claim_to_json(self.graph, cid)
                self.assertIsNotNone(payload)
                self.assertIn("specific_support", payload)  # type: ignore[arg-type]
                self.assertEqual(
                    payload["specific_support"],  # type: ignore[index]
                    claim.specific_support,
                )
                return
        self.skipTest("no claim in data has specific_support populated")

    def test_role_field_round_trips(self) -> None:
        # Pin a known person entity with non-null role.
        for eid, entity in self.graph.entities.items():
            if entity.role is not None:
                payload = mcp_server._entity_to_json(self.graph, eid)
                self.assertIsNotNone(payload)
                self.assertIn("role", payload)  # type: ignore[arg-type]
                self.assertEqual(payload["role"], entity.role)  # type: ignore[index]
                return
        self.skipTest("no entity has role populated")


class JsonRpcTests(unittest.TestCase):
    def test_initialize_response_shape(self) -> None:
        response = mcp_server.handle_initialize(request_id=1)
        self.assertEqual(response["jsonrpc"], "2.0")
        self.assertEqual(response["id"], 1)
        self.assertIn("result", response)
        self.assertIn("protocolVersion", response["result"])
        self.assertIn("serverInfo", response["result"])

    def test_make_error_shape(self) -> None:
        err = mcp_server._make_error(request_id=2, code=-32602, message="boom")
        self.assertEqual(err["jsonrpc"], "2.0")
        self.assertEqual(err["id"], 2)
        self.assertEqual(err["error"]["code"], -32602)
        self.assertEqual(err["error"]["message"], "boom")


class JsonRpcProtocolEdgeCaseTests(unittest.TestCase):
    """Round 10 audit (v0.7.13) regression suite for JSON-RPC 2.0
    spec compliance. Pre-v0.7.13 ``main`` loop crashed on batch
    inputs, sent responses to notifications (JSON-RPC §4.1
    forbids), and never produced a parse-error for non-object
    roots. The dispatcher is now factored into ``_handle_jsonrpc``
    and exercised here directly without spawning subprocesses.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = mcp_server.IutGraph.load(mcp_server.REPO_ROOT / "data")

    def test_batch_request_returns_array_of_responses(self) -> None:
        batch = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        ]
        responses = mcp_server._handle_jsonrpc(batch, self.graph)
        self.assertEqual(len(responses), 2)
        self.assertEqual({r["id"] for r in responses}, {1, 2})

    def test_batch_with_notification_omits_response(self) -> None:
        batch = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},  # no id => notif
        ]
        responses = mcp_server._handle_jsonrpc(batch, self.graph)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["id"], 1)

    def test_empty_batch_returns_invalid_request_error(self) -> None:
        responses = mcp_server._handle_jsonrpc([], self.graph)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["error"]["code"], -32600)
        self.assertIsNone(responses[0]["id"])

    def test_non_object_non_array_root_returns_invalid_request(self) -> None:
        for bad in (None, 42, "string", True):
            responses = mcp_server._handle_jsonrpc(bad, self.graph)
            self.assertEqual(len(responses), 1)
            self.assertEqual(responses[0]["error"]["code"], -32600)
            self.assertIsNone(responses[0]["id"])

    def test_notification_unknown_method_returns_no_response(self) -> None:
        # JSON-RPC 2.0 §4.1: server MUST NOT reply to a Notification.
        notif = {"jsonrpc": "2.0", "method": "totally/made/up"}
        responses = mcp_server._handle_jsonrpc(notif, self.graph)
        self.assertEqual(responses, [])

    def test_request_with_id_null_receives_response(self) -> None:
        # `id: null` is a Request (not a Notification); response carries id=null.
        req = {"jsonrpc": "2.0", "id": None, "method": "initialize", "params": {}}
        responses = mcp_server._handle_jsonrpc(req, self.graph)
        self.assertEqual(len(responses), 1)
        self.assertIsNone(responses[0]["id"])

    def test_request_missing_method_field_returns_invalid_request(self) -> None:
        req = {"jsonrpc": "2.0", "id": 5, "params": {}}
        responses = mcp_server._handle_jsonrpc(req, self.graph)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["error"]["code"], -32600)

    def test_wrong_jsonrpc_version_returns_invalid_request(self) -> None:
        # Round 11 audit (v0.7.14): JSON-RPC 2.0 §4 mandates the
        # `jsonrpc` field be the literal string "2.0". Earlier versions
        # silently accepted "1.0" / missing field.
        for bad in ({"jsonrpc": "1.0", "id": 1, "method": "tools/list"},
                    {"id": 1, "method": "tools/list"},
                    {"jsonrpc": 2.0, "id": 1, "method": "tools/list"}):
            responses = mcp_server._handle_jsonrpc(bad, self.graph)
            self.assertEqual(len(responses), 1, f"failed on {bad!r}")
            self.assertEqual(
                responses[0]["error"]["code"], -32600,
                f"wrong jsonrpc field must produce -32600; got {responses[0]!r}",
            )

    def test_params_null_returns_invalid_params(self) -> None:
        # Round 11 audit (v0.7.14): `params: null` made req.get("params", {})
        # return None and crashed downstream `params.get(...)`. JSON-RPC
        # 2.0 §4.2 says params, when present, MUST be Array or Object.
        req = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": None}
        responses = mcp_server._handle_jsonrpc(req, self.graph)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["error"]["code"], -32602)

    def test_params_non_object_non_array_returns_invalid_params(self) -> None:
        for bad in (42, "string", True):
            req = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": bad}
            responses = mcp_server._handle_jsonrpc(req, self.graph)
            self.assertEqual(len(responses), 1, f"failed on params={bad!r}")
            self.assertEqual(
                responses[0]["error"]["code"], -32602,
                f"non-Object/Array params must produce -32602; got {responses[0]!r}",
            )

    def test_nested_batch_rejected_at_inner_level(self) -> None:
        # Round 11 audit (v0.7.14): JSON-RPC 2.0 §6 says batches MUST be
        # flat arrays of Request objects. v0.7.13 silently consumed
        # nested arrays without producing an error.
        nested = [[{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}]]
        responses = mcp_server._handle_jsonrpc(nested, self.graph)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["error"]["code"], -32600)


class IutInputSchemaEnforcementTests(unittest.TestCase):
    """Round 11 audit (v0.7.14) regression: the ``tools/list`` response
    advertises ``inputSchema.pattern`` constraints that v0.7.13 did NOT
    enforce at the runtime dispatch boundary. A confused or malicious
    client supplying ``{"iri": ["array"]}`` to ``iut_entity`` crashed
    the loader (TypeError → -32603 internal error). This suite pins
    the explicit -32602 invalid-params behaviour.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = mcp_server.IutGraph.load(mcp_server.REPO_ROOT / "data")

    def _call(self, name: str, args: dict) -> dict:
        return mcp_server.handle_tools_call(
            request_id=1,
            params={"name": name, "arguments": args},
            graph=self.graph,
        )

    def test_iut_entity_rejects_non_string_iri(self) -> None:
        resp = self._call("iut_entity", {"iri": ["array"]})
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32602)

    def test_iut_entity_rejects_pattern_violation(self) -> None:
        resp = self._call("iut_entity", {"iri": "iut:abc; DROP TABLE"})
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32602)

    def test_iut_entity_rejects_wrong_namespace(self) -> None:
        # claim:foo violates the (iut|person|paper) namespace constraint.
        resp = self._call("iut_entity", {"iri": "claim:something"})
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32602)

    def test_iut_entity_accepts_dotted_iri(self) -> None:
        # Round 10 schema permits Cor.3.12; v0.7.14 runtime check honors it.
        resp = self._call("iut_entity", {"iri": "iut:Cor.3.12"})
        self.assertIn("result", resp)

    def test_iut_evidence_rejects_pattern_violation(self) -> None:
        resp = self._call("iut_evidence", {"iri": "evidence:has spaces"})
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32602)

    def test_iut_entity_missing_required_iri_returns_invalid_params(self) -> None:
        resp = self._call("iut_entity", {})
        self.assertIn("error", resp)
        self.assertEqual(resp["error"]["code"], -32602)


class IutTimelinePayloadFieldTests(unittest.TestCase):
    """Round 10 audit (v0.7.13) regression: the ``iut_timeline`` MCP
    branch was silently dropping the ``type`` field of timeline
    events because the prior property_audit substring check was
    fooled by the response envelope ``{"type": "text"}``. The
    AST-based check now distinguishes payload from envelope; this
    suite pins the actually-emitted shape so the regression cannot
    silently return.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = mcp_server.IutGraph.load(mcp_server.REPO_ROOT / "data")

    def _call_iut_timeline(self) -> list[dict]:
        response = mcp_server.handle_tools_call(
            request_id=99,
            params={"name": "iut_timeline", "arguments": {}},
            graph=self.graph,
        )
        text = response["result"]["content"][0]["text"]
        return json.loads(text)

    def test_iut_timeline_emits_type_field(self) -> None:
        events = self._call_iut_timeline()
        self.assertGreater(len(events), 0)
        for ev in events:
            self.assertIn("type", ev, f"event missing type: {ev}")

    def test_iut_timeline_emits_url_and_archive_url(self) -> None:
        events = self._call_iut_timeline()
        for ev in events:
            self.assertIn("url", ev)
            self.assertIn("archive_url", ev)

    def test_iut_timeline_actor_list_is_jsonable(self) -> None:
        events = self._call_iut_timeline()
        for ev in events:
            self.assertIsInstance(ev["actors"], list)


if __name__ == "__main__":
    unittest.main()
