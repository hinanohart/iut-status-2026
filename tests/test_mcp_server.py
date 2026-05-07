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
