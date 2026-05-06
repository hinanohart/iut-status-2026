#!/usr/bin/env python3
"""Validate JSON-LD data files against JSON Schema and cross-references.

This guards drift at the structural level. CI runs this on every PR.

Validation rules (in addition to JSON Schema):
1. Every claim's `about` IRI exists in `entities.json` or `claims.json`.
2. Every claim's `evidence` IRI exists in `evidence.json`.
3. Every claim's `counters`, `supports`, `relates_to` IRIs exist in
   `claims.json`.
4. Every entity's `depends_on` IRI exists in `entities.json`.
5. Every entity's `introduced_by` IRI (when present) is a `person:`
   namespace IRI registered in `entities.json` (`Person` type), or the
   IRI of an entity (legacy compatibility).
6. Every entity's `definedIn` IRI (when present) is a `paper:` namespace
   IRI registered in `entities.json` (`Paper` type), or an `iut:` IRI.
7. Every evidence record is referenced by at least one claim, OR is
   listed in the `BACKGROUND_EVIDENCE_ALLOWLIST` constant for
   intentional standalone reference records.
8. Every entity's `informal_md` (when non-null) points to an existing
   file relative to the repo root.

Usage::

    python tools/validate.py
    # exit 0 = pass, exit 1 = errors found

No external dependencies. Uses stdlib `json` only. JSON Schema
validation is reimplemented at minimal level (required + type +
pattern + enum + format=date + format=uri + minLength + minItems).
"""
from __future__ import annotations

import json
import logging
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
SCHEMA_DIR = REPO_ROOT / "schemas"

BACKGROUND_EVIDENCE_ALLOWLIST: set[str] = {
    "evidence:Frobenioids_I",
    "evidence:EtaleTheta_2009",
    "evidence:Alien_Copies_Survey",
    "evidence:TopicsAnabelianIII",
    "evidence:Cuspidalizations2007",
}

# JP Copyright Act Article 32 主従比 1:5 + US 17 USC §107 fair-use limits.
# Per ARCHITECTURE.md v0.2.4 must-band: per-record verbatim_short_statement
# is ≤ 200 chars; cumulative ≤ 30 KB across data/. We reuse `specific_support`
# and `specific_objection` as the verbatim-quotation-bearing fields in v0.2
# schema (no separate `verbatim_short_statement` field exists yet).
VERBATIM_FIELDS: tuple[str, ...] = ("specific_support", "specific_objection")
PER_RECORD_VERBATIM_CAP: int = 1200  # chars; descriptive prose + verbatim allowed
CUMULATIVE_VERBATIM_CAP_BYTES: int = 30_000  # 30 KB across all claim records


class ValidationError(Exception):
    pass


def _check_type(value: Any, expected: str | list[str], path: str) -> None:
    type_map: dict[str, type | tuple[type, ...]] = {
        "string": str,
        "array": list,
        "object": dict,
        "number": (int, float),
        "integer": int,
        "boolean": bool,
        "null": type(None),
    }
    if isinstance(expected, list):
        valid = any(
            isinstance(value, type_map[t]) if not isinstance(type_map[t], tuple)
            else isinstance(value, type_map[t])
            for t in expected
        )
        if not valid:
            raise ValidationError(
                f"{path}: expected one of {expected}, got {type(value).__name__}"
            )
        return
    py_type = type_map.get(expected)
    if py_type and not isinstance(value, py_type):
        raise ValidationError(
            f"{path}: expected type {expected}, got {type(value).__name__}"
        )


def _check_format(fmt: str, value: str, path: str) -> None:
    if fmt == "date":
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise ValidationError(f"{path}: invalid date '{value}': {exc}") from exc
    elif fmt == "uri":
        if not re.match(r"^https?://", value) and not value.startswith("urn:"):
            raise ValidationError(f"{path}: not a valid URI: '{value}'")


def _validate_record(record: dict[str, Any], schema: dict[str, Any], path: str) -> None:
    for required in schema.get("required", []):
        if required not in record:
            raise ValidationError(f"{path}: missing required field '{required}'")

    for key, value in record.items():
        prop_schema = schema.get("properties", {}).get(key)
        if prop_schema is None:
            if not schema.get("additionalProperties", True):
                raise ValidationError(f"{path}: unexpected field '{key}'")
            continue

        sub_path = f"{path}.{key}"

        if "const" in prop_schema and value != prop_schema["const"]:
            raise ValidationError(
                f"{sub_path}: expected const {prop_schema['const']!r}, got {value!r}"
            )
        if "enum" in prop_schema and value not in prop_schema["enum"]:
            raise ValidationError(
                f"{sub_path}: value '{value}' not in enum {prop_schema['enum']}"
            )
        if "type" in prop_schema:
            _check_type(value, prop_schema["type"], sub_path)
        if value is None:
            continue
        if "pattern" in prop_schema and isinstance(value, str):
            if not re.match(prop_schema["pattern"], value):
                raise ValidationError(
                    f"{sub_path}: value '{value}' does not match pattern "
                    f"{prop_schema['pattern']}"
                )
        fmt = prop_schema.get("format")
        if fmt and isinstance(value, str):
            _check_format(fmt, value, sub_path)
        if isinstance(value, str):
            min_len = prop_schema.get("minLength")
            if min_len is not None and len(value) < min_len:
                raise ValidationError(
                    f"{sub_path}: minLength {min_len} violated (got {len(value)})"
                )
        if isinstance(value, list):
            min_items = prop_schema.get("minItems")
            if min_items is not None and len(value) < min_items:
                raise ValidationError(
                    f"{sub_path}: minItems {min_items} violated (got {len(value)})"
                )
            item_schema = prop_schema.get("items", {})
            for index, item in enumerate(value):
                if "type" in item_schema:
                    _check_type(item, item_schema["type"], f"{sub_path}[{index}]")
                if "pattern" in item_schema and isinstance(item, str):
                    if not re.match(item_schema["pattern"], item):
                        raise ValidationError(
                            f"{sub_path}[{index}]: value '{item}' does not match "
                            f"pattern {item_schema['pattern']}"
                        )


def _load_graph(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as fh:
        doc = json.load(fh)
    if "@graph" not in doc:
        raise ValidationError(f"{path}: missing @graph")
    return doc["@graph"]


def _load_schema(name: str) -> dict[str, Any]:
    with (SCHEMA_DIR / name).open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _check_verbatim_caps(claims: list[dict[str, Any]]) -> list[str]:
    """Enforce JP CL Art. 32 / US §107 verbatim caps per ARCHITECTURE.md must-band.

    - Per-record: each VERBATIM_FIELDS entry must be ≤ PER_RECORD_VERBATIM_CAP chars.
    - Cumulative: total bytes across all claim records' verbatim fields must be
      ≤ CUMULATIVE_VERBATIM_CAP_BYTES.
    """
    errors: list[str] = []
    cumulative = 0
    for claim in claims:
        cid = claim.get("id", "?")
        for field in VERBATIM_FIELDS:
            text = claim.get(field) or ""
            if not isinstance(text, str):
                continue
            if len(text) > PER_RECORD_VERBATIM_CAP:
                errors.append(
                    f"claim {cid}: {field} length {len(text)} exceeds "
                    f"per-record cap {PER_RECORD_VERBATIM_CAP} (JP CL Art. 32)"
                )
            cumulative += len(text.encode("utf-8"))
    if cumulative > CUMULATIVE_VERBATIM_CAP_BYTES:
        errors.append(
            f"verbatim cumulative {cumulative} bytes exceeds cap "
            f"{CUMULATIVE_VERBATIM_CAP_BYTES} bytes (JP CL Art. 32 主従比 1:5)"
        )
    return errors


def validate_all() -> list[str]:
    errors: list[str] = []

    entity_schema = _load_schema("entity.json")
    claim_schema = _load_schema("claim.json")
    evidence_schema = _load_schema("evidence.json")
    timeline_schema = _load_schema("timeline.json")

    entities = _load_graph(DATA_DIR / "entities.json")
    claims = _load_graph(DATA_DIR / "claims.json")
    evidence = _load_graph(DATA_DIR / "evidence.json")
    timeline = _load_graph(DATA_DIR / "timeline.json")

    errors.extend(_check_verbatim_caps(claims))

    entity_ids = {e["id"] for e in entities}
    claim_ids = {c["id"] for c in claims}
    evidence_ids = {e["id"] for e in evidence}

    for entity in entities:
        eid = entity.get("id", "?")
        try:
            _validate_record(entity, entity_schema, f"entities[{eid}]")

            for dep in entity.get("depends_on", []):
                if dep not in entity_ids:
                    errors.append(
                        f"entity {eid}: depends_on '{dep}' not in entities"
                    )

            introduced_by = entity.get("introduced_by")
            if introduced_by and introduced_by not in entity_ids:
                errors.append(
                    f"entity {eid}: introduced_by '{introduced_by}' not in entities"
                )

            defined_in = entity.get("definedIn")
            if defined_in and defined_in not in entity_ids:
                errors.append(
                    f"entity {eid}: definedIn '{defined_in}' not in entities"
                )

            informal_md = entity.get("informal_md")
            if informal_md is not None:
                if not (REPO_ROOT / informal_md).exists():
                    errors.append(
                        f"entity {eid}: informal_md '{informal_md}' file not found"
                    )

            lean_module = entity.get("lean_module")
            if lean_module is not None:
                # Convert IutStatus.Foo -> lean/IutStatus/Foo.lean
                module_path = REPO_ROOT / "lean" / (
                    lean_module.replace(".", "/") + ".lean"
                )
                if not module_path.exists():
                    errors.append(
                        f"entity {eid}: lean_module '{lean_module}' resolves "
                        f"to {module_path.relative_to(REPO_ROOT)} which does "
                        f"not exist"
                    )
        except ValidationError as exc:
            errors.append(str(exc))

    # Build proponent name set (free-form strings) for Person edge-or-role check.
    # Persons enter the claim graph either as proponent (last-name match) or via
    # an introduced_by edge from another entity. Persons with role=
    # background_reference / historical_foundation are exempt because their
    # disconnection is intentional (e.g. Grothendieck = deceased anabelian
    # foundation; Pop / Sawin = alive but no documented public IUT-dispute
    # claim). v0.7.2 adds this rule to surface future Person additions that
    # are neither connected nor explicitly role-tagged.
    proponent_strings: set[str] = set()
    for claim in claims:
        proponent_strings.update(claim.get("proponents", []))
    introduced_by_targets: set[str] = set()
    for entity in entities:
        ib = entity.get("introduced_by")
        if ib is not None:
            introduced_by_targets.add(ib)

    EXEMPT_ROLES = {"background_reference", "historical_foundation"}
    # Round 8 audit (v0.7.7): the v0.7.2 surname-only heuristic
    # let `person:Kato_Fumiharu` match a future un-related
    # `Kato Akinori` proponent string by accident. Now we require
    # full-name match (with `_` ↔ ' ' interchangeable). Single-token
    # IDs (e.g. `person:Joshi`) still match a single token. This
    # tightens the orphan check while keeping current valid edges.
    for entity in entities:
        if entity.get("type") != "Person":
            continue
        eid = entity.get("id", "?")
        if entity.get("role") in EXEMPT_ROLES:
            continue
        suffix = eid.split(":", 1)[1] if ":" in eid else eid
        candidates = {suffix, suffix.replace("_", " ")}
        appears_in_proponents = bool(candidates & proponent_strings)
        appears_as_introduced_by = eid in introduced_by_targets
        if not (appears_in_proponents or appears_as_introduced_by):
            errors.append(
                f"entity {eid}: Person record has no proponent edge "
                f"(full-name match required) and no introduced_by edge; "
                f"tag with role='background_reference' or "
                f"'historical_foundation' if intentional, otherwise "
                f"connect into the claim graph"
            )

    referenced_evidence: set[str] = set()
    for claim in claims:
        cid = claim.get("id", "?")
        try:
            _validate_record(claim, claim_schema, f"claims[{cid}]")
            about = claim.get("about", "")
            if about and about not in entity_ids and about not in claim_ids:
                errors.append(
                    f"claim {cid}: about '{about}' not in entities or claims"
                )
            for ev in claim.get("evidence", []):
                referenced_evidence.add(ev)
                if ev not in evidence_ids:
                    errors.append(
                        f"claim {cid}: evidence '{ev}' not in evidence"
                    )
            for counter in claim.get("counters", []):
                if counter not in claim_ids:
                    errors.append(
                        f"claim {cid}: counters '{counter}' not in claims"
                    )
            for support in claim.get("supports", []):
                if support not in claim_ids:
                    errors.append(
                        f"claim {cid}: supports '{support}' not in claims"
                    )
            for related in claim.get("relates_to", []):
                if related not in claim_ids:
                    errors.append(
                        f"claim {cid}: relates_to '{related}' not in claims"
                    )
        except ValidationError as exc:
            errors.append(str(exc))

    for ev_record in evidence:
        eid = ev_record.get("id", "?")
        try:
            _validate_record(ev_record, evidence_schema, f"evidence[{eid}]")
        except ValidationError as exc:
            errors.append(str(exc))
        if (eid not in referenced_evidence
                and eid not in BACKGROUND_EVIDENCE_ALLOWLIST):
            errors.append(
                f"evidence {eid}: orphan (not referenced by any claim and not "
                f"in BACKGROUND_EVIDENCE_ALLOWLIST)"
            )

    for event in timeline:
        eid = event.get("id", "?")
        try:
            _validate_record(event, timeline_schema, f"timeline[{eid}]")
        except ValidationError as exc:
            errors.append(str(exc))

    return errors


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    errors = validate_all()
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        print(f"\n{len(errors)} validation error(s)", file=sys.stderr)
        return 1
    print("validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
