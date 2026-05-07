# Property Propagation Checklist

**Status**: enforced by CI step `Property propagation audit` (v0.7.9+).

This document defines the contract for adding, renaming, or removing a
JSON-Schema property in `schemas/*.json`. It exists because audit Rounds
4 through 9 each surfaced at least one CRITICAL drift between the schema
source of truth and one of four downstream surfaces, and the Round 9
critic concluded that *per-release audits cannot replace a structural
gate*. The structural gate is `tools/property_audit.py`; this document
is the human-readable form of what that script enforces.

## The four downstream surfaces

| Layer | File | Purpose | Required? |
|---|---|---|---|
| L1 | `data/context.jsonld` | JSON-LD `@context` mapping that gives the property a stable IRI | **always** |
| L2 | `loaders/python_minimal.py` | Typed Python loader (`Entity` / `Claim` / `Evidence` / `TimelineEvent` dataclass + `_to_*` factory) | **always** |
| L3 | `mcp/server.py` | MCP JSON-RPC serializer surfaced to LLM clients (`_entity_to_json`, `_claim_to_json`, `iut_evidence` branch, `iut_timeline` branch) | **always** |
| L4 | `tools/render_md.py` | Markdown view rendered into `docs/{overview,disputes,timeline}.md` | opt-in (allow-list per-property) |

L1, L2, and L3 together constitute the **drift-zero contract**: any
property declared by the schema must reach every consumer. L4 is opt-in
because the Markdown view is a curated reading surface, not an
exhaustive serializer.

## How to add a new schema property

1. **Edit the schema** in `schemas/<entity|claim|evidence|timeline>.json`:
   add the property under `properties`, plus `required` if appropriate.
2. **L1 — add `@context` mapping** in `data/context.jsonld`. Pick a
   namespaced IRI under `iut:` (or a `schema:` parent if the property
   has an obvious schema.org analogue).
3. **L2 — extend the loader** in `loaders/python_minimal.py`:
   - add the field to the relevant `@dataclass` (defaulting to `None` if
     optional, or a typed default for collections);
   - read the property inside the matching `_to_*` factory using
     `record.get("<schema_field_name>")` (camelCase preserved if the
     schema uses it).
4. **L3 — extend the MCP serializer** in `mcp/server.py`:
   - for entity / claim, add the field to the dict returned by
     `_entity_to_json` / `_claim_to_json`;
   - for evidence / timeline, add the field to the dict literal inside
     the `iut_evidence` / `iut_timeline` branch of `_dispatch_tool`.
5. **L4 (decision)** — choose one of:
   - **render** the property in `tools/render_md.py` (preferred for
     human-meaningful prose like `specific_support`); OR
   - **declare exempt** by adding the property name to the corresponding
     `SchemaPolicy.render_optional` set in
     `tools/property_audit.py`, with a one-line rationale.
6. **Re-render the docs**: `python tools/render_md.py --data data --out docs`
   then commit the regenerated `docs/{overview,disputes,timeline}.md`.
   (CI step `Render docs and check committed artefacts in sync` blocks
   merge if you forget.)
7. **Run the audit locally**: `python tools/property_audit.py`. It must
   print `OK` before commit. The CI step will run it again on the PR.
8. **Update tests** in `tests/test_property_audit.py` if any of the
   policy data structures changed.

## How to remove a schema property

1. Edit the schema (delete the property from `properties`, `required`,
   any `dependentRequired` clauses).
2. Remove the `@context` line in `data/context.jsonld`.
3. Remove the dataclass field and the `_to_*` factory line that reads
   it.
4. Remove the MCP serializer line that emits it.
5. Remove the renderer line, OR remove the property from
   `render_optional` in `tools/property_audit.py`.
6. Re-render docs, run audit, run tests.

## How to rename a schema property

A rename is logically a `remove + add`. Audit a removed-only or added-
only state — if you split the rename across commits, the audit will
fail mid-rename, which is the correct behaviour.

## What the audit does NOT enforce

- **Semantic correctness** of the property value: the audit checks
  presence, not whether the data is right.
- **`required` vs optional**: the audit treats every declared property
  the same; whether the schema lists it under `required` is a separate
  concern enforced by `tools/validate.py`.
- **Lean stub propagation**: the `lean_stub` field is L1-L3 enforced
  but the actual Lean module file under `lean/IutStatus/` is checked
  by `tools/validate.py`'s `lean_module` resolver, not here.
- **External archival population**: `archive_url` propagation is
  enforced; whether the URL actually points at a Wayback snapshot is
  the job of `tools/archive_evidence.py --network --lookup`.

## Audit rounds that motivated this gate

- **R4** (2026-05-06): tempered_rigidity misattribution.
- **R5** (2026-05-06): Joshi v2 fictional evidence + §1.4 mis-quote.
- **R6** (2026-05-07): Woit blog dating drift + timeline url gap.
- **R6.5** (2026-05-07): URL liveness verifier added (network layer).
- **R7** (2026-05-07): Kato ISBN fabrication + PRIMS issue ID drift.
- **R8** (2026-05-07): hand-edited prose retention of repaired data.
- **R9** (2026-05-07): auto-gen 6-release stale + MCP 5-field drop +
  loader Claim missing `specific_support` + LICENSE short-form.

Every round found at least one CRITICAL fabrication-class or drift-class
defect. The systemic root cause was not lazy reviewers; it was the
absence of a machine-checkable gate over the consumer chain. The audit
implemented in v0.7.9 closes this class.

## Forward-looking guarantees

If the audit is enforced as a CI gate (and the gate is not bypassed),
then schema-to-consumer drift cannot survive a green build. A future
audit round (R10+) discovering a CRITICAL of class **multi-layer
property drift** would indicate either:

1. The audit policy `render_optional` is too permissive (a property
   that should be visible in docs was exempted); or
2. A new consumer surface was added that the policy does not cover
   (e.g. a new tool that consumes the JSON-LD).

In either case the fix is to tighten the policy or add a new layer to
the audit.
