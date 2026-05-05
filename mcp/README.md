# MCP server for iut-status-2026

A vendor-neutral MCP (Model Context Protocol) server that exposes the
IUT claim graph as five tools. Any MCP-compatible LLM client (Claude
Desktop, Claude Code, custom agents) can wire this in.

## Tools

| Tool | Purpose |
|---|---|
| `iut_protocol` | Return the mandatory drift-zero answer protocol (call this first per session) |
| `iut_entity(iri)` | Fetch an entity record by IRI |
| `iut_claims_about(iri)` | Fetch all claims about a target IRI (entity or claim) |
| `iut_evidence(iri)` | Fetch an evidence record |
| `iut_timeline()` | Fetch the full chronological timeline |

## Wiring (Claude Desktop)

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`
(macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "iut-status-2026": {
      "command": "python",
      "args": ["/absolute/path/to/iut-status-2026/mcp/server.py"]
    }
  }
}
```

Restart Claude Desktop. The tools become available in any chat.

## Wiring (Claude Code)

```bash
claude mcp add iut-status-2026 -- python /absolute/path/to/iut-status-2026/mcp/server.py
```

## Wiring (custom agent / CLI)

The server speaks JSON-RPC 2.0 over stdin/stdout. See `mcp/server.py`
for the wire format. Standard MCP SDKs (Python `mcp` package, TS
`@modelcontextprotocol/sdk`) work too.

## Drift-zero contract

The server never paraphrases. Every tool returns deterministic JSON
straight from the JSON-LD source. The LLM client is responsible for
applying the 5-block answer template from `LLM_CONTEXT.md` §3.3.

## Reusability

This server is intentionally domain-generic. To adapt it to another
multi-perspective dispute repository:
1. Copy `mcp/server.py` to the new repository.
2. Change `REPO_ROOT` resolution if the directory layout differs.
3. Rename the tool name prefix (`iut_*` → `<your-domain>_*`).
4. Update `SERVER_NAME` and `SERVER_VERSION`.

The data schema (`schemas/*.json`) and protocol (`LLM_CONTEXT.md`) are
also reusable; only the IRI namespace and content change.
