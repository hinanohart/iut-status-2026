#!/usr/bin/env python3
"""Validate JSON-LD data files against JSON Schema.

This guards drift at structural level. CI runs this on every PR.

Validation rules (in addition to JSON Schema):
1. Every claim's `about` IRI exists in `entities.json` or `claims.json`.
2. Every claim's `evidence` IRI exists in `evidence.json`.
3. Every claim's `counters` and `supports` IRIs exist in `claims.json`.
4. Every entity's `depends_on` IRI exists in `entities.json`.

Usage::

    python tools/validate.py
    # exit 0 = pass, exit 1 = errors found

No external dependencies. Uses stdlib `json` only. JSON Schema
validation is reimplemented at minimal level (required + type +
pattern + enum + format=date).
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


class ValidationError(Exception):
    """Raised when a record fails validation."""


def _check_type(value: Any, expected: str, path: str) -> None:
    type_map = {
        "string": str,
        "array": list,
        "object": dict,
        "number": (int, float),
        "integer": int,
        "boolean": bool,
        "null": type(None),
    }
    py_type = type_map.get(expected)
    if py_type and not isinstance(value, py_type):
        raise ValidationError(
            f"{path}: expected type {expected}, got {type(value).__name__}"
        )


def _check_format_date(value: str, path: str) -> None:
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{path}: invalid date '{value}': {exc}") from exc


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
        if "pattern" in prop_schema and isinstance(value, str):
            if not re.match(prop_schema["pattern"], value):
                raise ValidationError(
                    f"{sub_path}: value '{value}' does not match pattern "
                    f"{prop_schema['pattern']}"
                )
        if prop_schema.get("format") == "date" and isinstance(value, str):
            _check_format_date(value, sub_path)
        if prop_schema.get("type") == "string":
            min_len = prop_schema.get("minLength")
            if min_len is not None and len(value) < min_len:
                raise ValidationError(
                    f"{sub_path}: minLength {min_len} violated (got {len(value)})"
                )
        if prop_schema.get("type") == "array":
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


def validate_all() -> list[str]:
    """Run validation, return list of error strings (empty = pass)."""
    errors: list[str] = []

    entity_schema = _load_schema("entity.json")
    claim_schema = _load_schema("claim.json")

    entities = _load_graph(DATA_DIR / "entities.json")
    claims = _load_graph(DATA_DIR / "claims.json")
    evidence = _load_graph(DATA_DIR / "evidence.json")

    entity_ids = {e["id"] for e in entities}
    claim_ids = {c["id"] for c in claims}
    evidence_ids = {e["id"] for e in evidence}

    for entity in entities:
        try:
            _validate_record(entity, entity_schema, f"entities[{entity.get('id', '?')}]")
            for dep in entity.get("depends_on", []):
                if dep not in entity_ids:
                    errors.append(
                        f"entity {entity['id']}: depends_on '{dep}' not in entities"
                    )
        except ValidationError as exc:
            errors.append(str(exc))

    for claim in claims:
        try:
            _validate_record(claim, claim_schema, f"claims[{claim.get('id', '?')}]")
            about = claim.get("about", "")
            if about and about not in entity_ids and about not in claim_ids:
                errors.append(
                    f"claim {claim['id']}: about '{about}' not in entities or claims"
                )
            for ev in claim.get("evidence", []):
                if ev not in evidence_ids:
                    errors.append(
                        f"claim {claim['id']}: evidence '{ev}' not in evidence"
                    )
            for counter in claim.get("counters", []):
                if counter not in claim_ids:
                    errors.append(
                        f"claim {claim['id']}: counters '{counter}' not in claims"
                    )
            for support in claim.get("supports", []):
                if support not in claim_ids:
                    errors.append(
                        f"claim {claim['id']}: supports '{support}' not in claims"
                    )
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
