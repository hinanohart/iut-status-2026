#!/usr/bin/env python3
"""Schema-to-consumer-chain drift detector (R4-R9 systemic root-cause closer).

Class background
----------------
Audit Rounds 4 through 9 each surfaced at least one CRITICAL drift between
the JSON-Schema source of truth and one of the four downstream surfaces:

    L1. ``data/context.jsonld``  — JSON-LD @context mapping
    L2. ``loaders/python_minimal.py`` — typed Python loader
    L3. ``mcp/server.py``       — MCP JSON-RPC serializer (LLM tool-use surface)
    L4. ``tools/render_md.py``  — Markdown view rendered into ``docs/``

Round 9 critic recommended a *property-add checklist enforced by CI*. This
script is the machine-checkable form of that checklist. Adding or renaming
a property in ``schemas/*.json`` without propagating to L1-L4 (or marking
the property *exempt* via the explicit ``RENDER_OPTIONAL`` allow-list) makes
this audit fail and blocks the merge.

Drift-zero contract
-------------------
L1, L2, L3 are *mandatory* for every schema property. L4 is *opt-in* with
explicit per-property allow-list — render is a curated human view, not an
exhaustive serializer, and forcing a render would dilute the docs.

The audit deliberately does NOT use AST parsing; plain substring matching
is more robust to whitespace / formatter changes and to alternative
attribute access patterns (``record["x"]`` vs ``record.get("x")`` vs
``getattr(record, "x")``). False negatives (a literal that happens to
match in a comment) are acceptable since adding a property always also
requires production-code changes elsewhere.

Exit code 0 = clean, non-zero = drift.

Usage::

    python tools/property_audit.py            # full audit (default)
    python tools/property_audit.py --json     # machine-readable summary
    python tools/property_audit.py --schema entity.json  # audit one schema
"""
from __future__ import annotations

import argparse
import ast
import json
import logging
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger("property_audit")

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "schemas"
CONTEXT_FILE = REPO_ROOT / "data" / "context.jsonld"
LOADER_FILE = REPO_ROOT / "loaders" / "python_minimal.py"
MCP_FILE = REPO_ROOT / "mcp" / "server.py"
RENDER_FILE = REPO_ROOT / "tools" / "render_md.py"


@dataclass(frozen=True, slots=True)
class SchemaPolicy:
    """Per-schema configuration for the audit.

    Attributes
    ----------
    schema_file:
        Filename under ``schemas/`` (e.g. ``entity.json``).
    loader_class:
        Dataclass name in ``loaders/python_minimal.py`` representing the
        record. Used as a sanity-check anchor in L2.
    loader_factory:
        Static method name on ``IutGraph`` that builds the dataclass
        from a raw record (e.g. ``_to_entity``). Property reads must
        appear inside this function.
    mcp_emitter:
        Anchor used in L3 detection. For ``entity.json`` and
        ``claim.json`` this is the dedicated serializer function name;
        for ``evidence.json`` and ``timeline.json`` MCP inlines the
        dict literal inside ``_dispatch_tool``, so we anchor on a
        unique substring of that branch.
    render_optional:
        Schema properties that are *not* required to be rendered into
        the Markdown view. Adding a new property to schema *not* in this
        set forces a render update OR an explicit exemption; either is
        a conscious decision, which is the point.
    schema_to_python_rename:
        camelCase schema property → snake_case Python attribute.
        L3 rename map (the MCP serializer emits Python-style keys for
        readability). L1 and L2 use the schema name verbatim; L4 may
        use either.
    """

    schema_file: str
    loader_class: str
    loader_factory: str
    mcp_emitter: str
    render_optional: frozenset[str]
    schema_to_python_rename: dict[str, str] = field(default_factory=dict)


# Rationale for each render_optional entry is in PROPERTY_PROPAGATION.md.
POLICIES: tuple[SchemaPolicy, ...] = (
    SchemaPolicy(
        schema_file="entity.json",
        loader_class="Entity",
        loader_factory="_to_entity",
        mcp_emitter="_entity_to_json",
        # render_overview surfaces label / type / alt_labels / introduced_by /
        # introduced_year / depends_on / lean_module / claim count. Other
        # fields are intentionally omitted from the human-readable Overview.
        render_optional=frozenset({
            "id",  # surfaced as section header anchor, not as a body line
            "section",  # used as grouping key in render_overview
            "definedIn",
            "informal_md",  # path-only, exposed via `iut_entity` MCP tool
            "lean_stub",
            "role",
            "verified_at",  # noisy on every entity card
        }),
        schema_to_python_rename={"definedIn": "defined_in"},
    ),
    SchemaPolicy(
        schema_file="claim.json",
        loader_class="Claim",
        loader_factory="_to_claim",
        mcp_emitter="_claim_to_json",
        render_optional=frozenset({
            "type",  # constant "Claim"; trivial
            "peer_review_status",  # surfaced via MCP, not docs (avoid clutter)
            "fair_use_note",  # legal prose, not for human dispute browsing
            "relates_to",  # non-directional; opposing_pairs already covers
        }),
    ),
    SchemaPolicy(
        schema_file="evidence.json",
        loader_class="Evidence",
        loader_factory="_to_evidence",
        # MCP inlines the evidence emitter inside _dispatch_tool; anchor on
        # the unique branch identifier.
        mcp_emitter='if name == "iut_evidence":',
        # render_disputes surfaces evidence indirectly inside _render_claim
        # (label + url + archive_url). Other evidence fields stay loader-only.
        render_optional=frozenset({
            "id",  # used as fallback when label missing
            "type",
            "doi",
            "isbn",
            "publisher",
            "asserted_at",
        }),
    ),
    SchemaPolicy(
        schema_file="timeline.json",
        loader_class="TimelineEvent",
        loader_factory="_to_timeline",
        mcp_emitter='if name == "iut_timeline":',
        # render_timeline surfaces date / label / actors only.
        render_optional=frozenset({
            "id",
            "type",
            "url",
            "archive_url",
        }),
    ),
)


@dataclass(slots=True)
class AuditFinding:
    schema: str
    layer: str
    property: str
    detail: str

    def render(self) -> str:
        return f"[{self.schema}] L:{self.layer} prop={self.property!r}: {self.detail}"


def _load_schema_properties(schema_path: Path) -> tuple[str, ...]:
    if not schema_path.is_file():
        raise FileNotFoundError(f"schema file missing: {schema_path}")
    with schema_path.open("r", encoding="utf-8") as fh:
        doc = json.load(fh)
    properties = doc.get("properties")
    if not isinstance(properties, dict):
        raise ValueError(f"{schema_path} has no `properties` object")
    return tuple(sorted(properties.keys()))


def _load_context_keys() -> frozenset[str]:
    if not CONTEXT_FILE.is_file():
        raise FileNotFoundError(f"context file missing: {CONTEXT_FILE}")
    with CONTEXT_FILE.open("r", encoding="utf-8") as fh:
        ctx = json.load(fh)
    mapping = ctx.get("@context", {})
    if not isinstance(mapping, dict):
        raise ValueError(f"{CONTEXT_FILE} @context is not a dict")
    return frozenset(mapping.keys())


def _read(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"required source file missing: {path}")
    return path.read_text(encoding="utf-8")


def _extract_function_body(source: str, anchor: str) -> str:
    """Return the indent-bounded slice of source starting at ``anchor``.

    The slice begins at the line containing ``anchor`` and ends at the
    first subsequent line whose indentation is *less than or equal to*
    the anchor line's indentation (= the next sibling construct).

    This catches nested branches correctly: anchoring on
    ``if name == "iut_evidence":`` (4-space indent inside
    ``_dispatch_tool``) yields only that branch and stops at
    ``if name == "iut_timeline":`` (same 4-space indent).
    """
    idx = source.find(anchor)
    if idx == -1:
        return ""

    line_start = source.rfind("\n", 0, idx) + 1
    leading = source[line_start:idx]
    anchor_indent = len(leading) - len(leading.lstrip(" \t"))

    tail = source[line_start:]
    lines = tail.splitlines(keepends=True)
    if not lines:
        return ""

    out: list[str] = [lines[0]]
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped:
            out.append(line)
            continue
        if stripped.startswith("#"):
            out.append(line)
            continue
        leading_ws = line[: len(line) - len(line.lstrip(" \t"))]
        line_indent = len(leading_ws.expandtabs(4))
        if line_indent <= anchor_indent:
            break
        out.append(line)
    return "".join(out)


def _check_l1_context(
    properties: tuple[str, ...], context_keys: frozenset[str], schema: str
) -> list[AuditFinding]:
    findings: list[AuditFinding] = []
    for prop in properties:
        if prop not in context_keys:
            findings.append(AuditFinding(
                schema=schema, layer="1-context",
                property=prop,
                detail=f"@context mapping missing in {CONTEXT_FILE.name}",
            ))
    return findings


def _check_l2_loader(
    properties: tuple[str, ...], policy: SchemaPolicy, source: str
) -> list[AuditFinding]:
    findings: list[AuditFinding] = []

    if f"class {policy.loader_class}:" not in source and \
            f"class {policy.loader_class}(" not in source:
        findings.append(AuditFinding(
            schema=policy.schema_file, layer="2-loader",
            property="<class>",
            detail=f"dataclass {policy.loader_class!r} not found in loader",
        ))
        return findings

    factory_anchor = f"def {policy.loader_factory}("
    body = _extract_function_body(source, factory_anchor)
    if not body:
        findings.append(AuditFinding(
            schema=policy.schema_file, layer="2-loader",
            property="<factory>",
            detail=f"factory {policy.loader_factory!r} not found in loader",
        ))
        return findings

    for prop in properties:
        # Loader reads the schema field name verbatim (camelCase preserved).
        # Match common access patterns; presence in body of the factory is
        # enough — loader handles both record["x"] and record.get("x").
        token = f'"{prop}"'
        if token not in body:
            findings.append(AuditFinding(
                schema=policy.schema_file, layer="2-loader",
                property=prop,
                detail=(
                    f"property literal {token} not read inside "
                    f"{policy.loader_factory}() — schema property silently dropped"
                ),
            ))
    return findings


def _extract_payload_dict_keys(body: str) -> set[str]:
    """Collect string keys from *payload* dict literals inside ``body``.

    Round 10 audit (v0.7.13) replaced the prior "any-substring-match"
    heuristic. The earlier check was bypassed by the MCP response
    envelope ``{"content": [{"type": "text", "text": ...}]}``: the
    envelope contains ``"type"`` and ``"text"`` as keys regardless of
    whether the payload dict emits them, so a forgotten payload key was
    silently passing whenever the envelope happened to share its name
    (e.g. ``iut_timeline`` payload omitted ``type`` for two releases).

    The fix: parse the function body as Python AST, walk every dict
    literal, and only consider literals that include ``"id"`` as a key
    — a stable invariant of every payload dict (entity / claim /
    evidence / timeline). The MCP envelope never carries ``"id"``, so
    this discriminator cleanly separates payload from framing.
    """
    # Dedent: the extracted body keeps the original column from the
    # surrounding function (typically 4 or 8 spaces deep), but ast.parse
    # requires column-0 code. textwrap.dedent strips the common leading
    # whitespace.
    dedented = textwrap.dedent(body)
    try:
        tree = ast.parse(dedented)
    except SyntaxError:
        return set()
    keys: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        string_keys = {
            k.value
            for k in node.keys
            if isinstance(k, ast.Constant) and isinstance(k.value, str)
        }
        if "id" in string_keys:
            keys |= string_keys
    return keys


def _check_l3_mcp(
    properties: tuple[str, ...], policy: SchemaPolicy, source: str
) -> list[AuditFinding]:
    findings: list[AuditFinding] = []
    body = _extract_function_body(source, policy.mcp_emitter)
    if not body:
        findings.append(AuditFinding(
            schema=policy.schema_file, layer="3-mcp",
            property="<emitter>",
            detail=f"MCP emitter anchor {policy.mcp_emitter!r} not found",
        ))
        return findings

    payload_keys = _extract_payload_dict_keys(body)
    if not payload_keys:
        findings.append(AuditFinding(
            schema=policy.schema_file, layer="3-mcp",
            property="<payload>",
            detail=(
                f"could not locate any payload dict literal containing 'id' "
                f"inside {policy.mcp_emitter}; emitter may have been "
                f"refactored away or the dispatch shape changed. AST-based "
                f"check requires at least one `{{\"id\": …, …}}` literal."
            ),
        ))
        return findings

    for prop in properties:
        py_name = policy.schema_to_python_rename.get(prop, prop)
        if py_name in payload_keys or prop in payload_keys:
            continue
        findings.append(AuditFinding(
            schema=policy.schema_file, layer="3-mcp",
            property=prop,
            detail=(
                f"property not emitted by MCP serializer "
                f"({policy.mcp_emitter}). schema_name={prop!r} "
                f"python_name={py_name!r} absent from any payload dict "
                f"(dict literal containing 'id' key) inside the dispatch branch"
            ),
        ))
    return findings


def _check_l4_render(
    properties: tuple[str, ...], policy: SchemaPolicy, source: str
) -> list[AuditFinding]:
    findings: list[AuditFinding] = []
    for prop in properties:
        if prop in policy.render_optional:
            continue
        py_name = policy.schema_to_python_rename.get(prop, prop)
        # Renderer is allowed to use either attribute access (claim.x) or
        # f-string interpolation. Substring presence anywhere in the file
        # is sufficient because render is a small file and false-positive
        # collisions are unlikely.
        if py_name in source or prop in source:
            continue
        findings.append(AuditFinding(
            schema=policy.schema_file, layer="4-render",
            property=prop,
            detail=(
                f"required-rendered property absent from {RENDER_FILE.name}. "
                f"Either render it, or add to render_optional in policy "
                f"with rationale in PROPERTY_PROPAGATION.md."
            ),
        ))
    return findings


def run_audit(
    *, only_schema: str | None = None
) -> list[AuditFinding]:
    context_keys = _load_context_keys()
    loader_src = _read(LOADER_FILE)
    mcp_src = _read(MCP_FILE)
    render_src = _read(RENDER_FILE)

    findings: list[AuditFinding] = []
    for policy in POLICIES:
        if only_schema and policy.schema_file != only_schema:
            continue
        schema_path = SCHEMAS_DIR / policy.schema_file
        properties = _load_schema_properties(schema_path)
        findings.extend(_check_l1_context(properties, context_keys, policy.schema_file))
        findings.extend(_check_l2_loader(properties, policy, loader_src))
        findings.extend(_check_l3_mcp(properties, policy, mcp_src))
        findings.extend(_check_l4_render(properties, policy, render_src))
    return findings


def _format_human(findings: list[AuditFinding]) -> str:
    if not findings:
        return "property_audit: OK (all schemas propagate to L1-L4)\n"

    out = [f"property_audit: {len(findings)} drift(s) detected\n", ""]
    by_schema: dict[str, list[AuditFinding]] = {}
    for f in findings:
        by_schema.setdefault(f.schema, []).append(f)
    for schema in sorted(by_schema):
        out.append(f"  {schema}:")
        for f in by_schema[schema]:
            out.append(f"    - {f.render()}")
        out.append("")
    return "\n".join(out)


def _format_json(findings: list[AuditFinding]) -> str:
    return json.dumps(
        {
            "ok": not findings,
            "count": len(findings),
            "findings": [
                {"schema": f.schema, "layer": f.layer,
                 "property": f.property, "detail": f.detail}
                for f in findings
            ],
        },
        indent=2,
        ensure_ascii=False,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Schema-to-consumer-chain drift detector"
    )
    parser.add_argument(
        "--schema",
        help="Audit a single schema file by name (e.g. entity.json)",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Emit machine-readable summary on stdout",
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    findings = run_audit(only_schema=args.schema)
    if args.json:
        print(_format_json(findings))
    else:
        sys.stdout.write(_format_human(findings))

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
