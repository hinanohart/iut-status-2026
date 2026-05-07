#!/usr/bin/env python3
"""MCP (Model Context Protocol) server for iut-status-2026.

Exposes the IUT claim graph to any MCP-compatible LLM client (Claude
Desktop, Claude Code, custom agents) as four read-only tools:

- `iut_entity(iri)` — fetch an entity record
- `iut_claims_about(iri)` — fetch all claims about an entity or claim
- `iut_evidence(iri)` — fetch an evidence record
- `iut_timeline()` — fetch the full chronological timeline

The server is stdlib-only and implements the MCP JSON-RPC protocol
manually. No external dependencies. The intent is that this file be
trivially copyable into other dispute-preservation repositories with
only the data path changed.

Run::

    python mcp/server.py
    # speaks JSON-RPC over stdin/stdout

Wire it into Claude Desktop's `claude_desktop_config.json`::

    {
      "mcpServers": {
        "iut-status-2026": {
          "command": "python",
          "args": ["/path/to/iut-status-2026/mcp/server.py"]
        }
      }
    }

Drift-zero contract: every tool returns deterministic JSON straight
from the JSON-LD source. The server never paraphrases, summarizes, or
synthesizes. LLMs receiving the tool output must apply the 5-block
answer protocol from `LLM_CONTEXT.md` §3.3.
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from loaders.python_minimal import IutGraph  # noqa: E402

logger = logging.getLogger(__name__)


PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "iut-status-2026"
SERVER_VERSION = "0.1.1"


def _make_response(request_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def _make_error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": message},
    }


def _entity_to_json(graph: IutGraph, iri: str) -> dict[str, Any] | None:
    entity = graph.entity(iri)
    if entity is None:
        return None
    # Round 9 audit (v0.7.8): role / lean_stub were silently dropped
    # by the MCP serializer even though the schema and loader carry
    # them. drift-zero contract requires every dataclass field to be
    # exposed (or explicitly excluded with rationale) — see Round 9
    # architect Sec 1.
    return {
        "id": entity.id,
        "type": entity.type,
        "label": entity.label,
        "alt_labels": list(entity.alt_labels),
        "section": entity.section,
        "introduced_by": entity.introduced_by,
        "introduced_year": entity.introduced_year,
        "defined_in": entity.defined_in,
        "depends_on": list(entity.depends_on),
        "informal_md": entity.informal_md,
        "lean_stub": entity.lean_stub,
        "lean_module": entity.lean_module,
        "role": entity.role,
        "verified_at": entity.verified_at,
    }


def _claim_to_json(graph: IutGraph, claim_iri: str) -> dict[str, Any] | None:
    claim = graph.claim(claim_iri)
    if claim is None:
        return None
    # Round 9 audit (v0.7.8): specific_support was silently dropped
    # by the loader (Claim dataclass) and the MCP serializer. With
    # 8+ active records carrying the field in data/claims.json,
    # downstream LLMs were missing supportive context entirely.
    return {
        "id": claim.id,
        "type": claim.type,
        "label": claim.label,
        "about": claim.about,
        "position": claim.position,
        "stance": claim.stance,
        "proponents": list(claim.proponents),
        "asserted_at": claim.asserted_at,
        "evidence": list(claim.evidence),
        "counters": list(claim.counters),
        "supports": list(claim.supports),
        "relates_to": list(claim.relates_to),
        "specific_support": claim.specific_support,
        "specific_objection": claim.specific_objection,
        "fair_use_note": claim.fair_use_note,
        "status": claim.status,
        "peer_review_status": claim.peer_review_status,
        "verified_at": claim.verified_at,
    }


TOOLS = [
    {
        "name": "iut_entity",
        "description": (
            "Fetch the JSON-LD entity record for an IUT concept, person, "
            "or paper by stable IRI (e.g. iut:Cor.3.12, person:Mochizuki, "
            "paper:IUTchIII). Returns null if the IRI is not registered."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "iri": {
                    "type": "string",
                    "pattern": "^(iut|person|paper):[A-Za-z][A-Za-z0-9_.]*$",
                }
            },
            "required": ["iri"],
        },
    },
    {
        "name": "iut_claims_about",
        "description": (
            "Fetch all claim records whose `about` field equals the given "
            "IRI. Returns the dispute graph local to that target."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "iri": {"type": "string"}
            },
            "required": ["iri"],
        },
    },
    {
        "name": "iut_evidence",
        "description": "Fetch a bibliographic evidence record by IRI.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "iri": {
                    "type": "string",
                    "pattern": "^evidence:[A-Za-z][A-Za-z0-9_]*$",
                }
            },
            "required": ["iri"],
        },
    },
    {
        "name": "iut_timeline",
        "description": (
            "Fetch the full chronological timeline of dispute events as a "
            "list, sorted ascending by date."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "iut_protocol",
        "description": (
            "Return the mandatory drift-zero answer protocol "
            "(LLM_CONTEXT.md §3) as plain text. LLM clients should call "
            "this once per session before answering IUT questions."
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
    },
]


def handle_initialize(request_id: Any) -> dict[str, Any]:
    return _make_response(
        request_id,
        {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        },
    )


def handle_tools_list(request_id: Any) -> dict[str, Any]:
    return _make_response(request_id, {"tools": TOOLS})


def handle_tools_call(
    request_id: Any, params: dict[str, Any], graph: IutGraph
) -> dict[str, Any]:
    """Dispatch a tools/call. Wraps every tool body in try/except so that
    malformed parameters (missing IRI, wrong type, unknown tool) become
    JSON-RPC error responses rather than process-killing exceptions.
    """
    name = params.get("name")
    args = params.get("arguments", {}) or {}

    try:
        return _dispatch_tool(request_id, name, args, graph)
    except KeyError as exc:
        return _make_error(request_id, -32602, f"missing required argument: {exc}")
    except Exception as exc:  # noqa: BLE001 — JSON-RPC server must not crash
        logger.exception("tools/call failed: %s", name)
        return _make_error(request_id, -32603, f"internal error: {exc}")


def _dispatch_tool(
    request_id: Any, name: Any, args: dict[str, Any], graph: IutGraph
) -> dict[str, Any]:
    if name == "iut_entity":
        record = _entity_to_json(graph, args["iri"])
        return _make_response(
            request_id,
            {"content": [{"type": "text", "text": json.dumps(record, ensure_ascii=False, indent=2)}]},
        )

    if name == "iut_claims_about":
        target = args["iri"]
        claims = [_claim_to_json(graph, c.id) for c in graph.claims_about(target)]
        return _make_response(
            request_id,
            {"content": [{"type": "text", "text": json.dumps(claims, ensure_ascii=False, indent=2)}]},
        )

    if name == "iut_evidence":
        ev = graph.evidence.get(args["iri"])
        if ev is None:
            payload: Any = None
        else:
            # Round 9 audit (v0.7.8): archive_url was silently dropped.
            payload = {
                "id": ev.id,
                "type": ev.type,
                "label": ev.label,
                "url": ev.url,
                "archive_url": ev.archive_url,
                "doi": ev.doi,
                "isbn": ev.isbn,
                "publisher": ev.publisher,
                "asserted_at": ev.asserted_at,
            }
        return _make_response(
            request_id,
            {"content": [{"type": "text", "text": json.dumps(payload, ensure_ascii=False, indent=2)}]},
        )

    if name == "iut_timeline":
        events = sorted(graph.timeline.values(), key=lambda e: e.date)
        # Round 9 audit (v0.7.8): url + archive_url were silently
        # dropped; LLM consumers asking "where can I read about this
        # event?" got nothing back.
        # Round 10 audit (v0.7.13): the `type` field was being silently
        # dropped here even though property_audit's substring match
        # accidentally PASSed (the MCP envelope `{"type": "text"}`
        # below provided a false-positive substring hit). Re-emitting
        # the field; envelope-mask added to property_audit closes the
        # checker bypass.
        payload_list = [
            {
                "id": e.id,
                "type": e.type,
                "label": e.label,
                "date": e.date,
                "actors": list(e.actors),
                "url": e.url,
                "archive_url": e.archive_url,
            }
            for e in events
        ]
        return _make_response(
            request_id,
            {"content": [{"type": "text", "text": json.dumps(payload_list, ensure_ascii=False, indent=2)}]},
        )

    if name == "iut_protocol":
        protocol_path = REPO_ROOT / "LLM_CONTEXT.md"
        text = protocol_path.read_text(encoding="utf-8")
        return _make_response(
            request_id,
            {"content": [{"type": "text", "text": text}]},
        )

    return _make_error(request_id, -32601, f"unknown tool: {name}")


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(message)s",
        stream=sys.stderr,
    )

    graph = IutGraph.load(REPO_ROOT / "data")
    logger.info("MCP server ready: %d entities, %d claims",
                len(graph.entities), len(graph.claims))

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            # JSON-RPC 2.0 §4.4: parse error response carries id=null.
            sys.stdout.write(
                json.dumps(_make_error(None, -32700, "parse error"), ensure_ascii=False) + "\n"
            )
            sys.stdout.flush()
            continue

        # Round 10 audit (v0.7.13): JSON-RPC 2.0 §6 batch handling +
        # §1.2 notification (no `id` key) handling + §4.4 invalid-type
        # rejection. Prior versions crashed on `[…]` / null / 42 /
        # "string" inputs with `'list' object has no attribute 'get'`.
        responses = _handle_jsonrpc(req, graph)
        for response in responses:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()

    return 0


def _handle_jsonrpc(req: object, graph: IutGraph) -> list[dict]:
    """Dispatch a single or batch JSON-RPC 2.0 message.

    Returns the list of response objects to emit (possibly empty for
    notifications and notification-only batches).
    """
    if isinstance(req, list):
        # JSON-RPC 2.0 §6: batch — empty array → invalid request.
        if not req:
            return [_make_error(None, -32600, "invalid request: empty batch")]
        out: list[dict] = []
        for item in req:
            out.extend(_handle_jsonrpc(item, graph))
        return out

    if not isinstance(req, dict):
        return [_make_error(None, -32600, "invalid request: not an object")]

    method = req.get("method")
    # JSON-RPC 2.0 §1.2: a notification is a Request object that has no
    # `id` member. `id: null` is NOT a notification; it is a Request
    # whose response id is null. Use `"id" in req` to distinguish.
    is_notification = "id" not in req
    request_id = req.get("id")

    if not isinstance(method, str):
        if is_notification:
            return []
        return [_make_error(request_id, -32600, "invalid request: missing or non-string method")]

    if method == "initialize":
        response = handle_initialize(request_id)
    elif method == "tools/list":
        response = handle_tools_list(request_id)
    elif method == "tools/call":
        response = handle_tools_call(request_id, req.get("params", {}), graph)
    elif method == "notifications/initialized":
        return []
    else:
        if is_notification:
            return []
        response = _make_error(request_id, -32601, f"unknown method: {method}")

    if is_notification:
        return []
    return [response]


if __name__ == "__main__":
    raise SystemExit(main())
