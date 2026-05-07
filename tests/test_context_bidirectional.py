#!/usr/bin/env python3
"""JSON-LD bidirectional context tests (HIGH-2 deferred from v0.7.8 → closed v0.7.10).

`tools/property_audit.py` (v0.7.9) verifies that every schema property
has a key in `data/context.jsonld`. That is forward direction only:
schema → context. This module adds the reverse and structural
invariants:

1. **Reverse direction**: every non-built-in `@context` key
   (excluding namespace prefixes and JSON-LD reserved keys) corresponds
   either to a schema property or to a built-in JSON-LD term.
2. **Term value well-formedness**: each property mapping is either a
   string IRI or an object with `@id`. If an object, optional `@type`
   is `"@id"` or a known namespace IRI (xsd:date, xsd:gYear,
   schema:inLanguage); `@container` is `"@set"`.
3. **No collisions**: no two schema properties expand to the same IRI
   except where the schema deliberately overlaps (none currently).
4. **Drift-zero IRI level**: every namespace prefix used in the
   `@context` mapping (`iut:`, `schema:`, `xsd:`) is itself defined.
5. **Context expand round-trip**: a small synthetic record expands into
   keys whose IRIs match the declared `@id` mappings.

Property_audit covers (1) forward + minimal presence; this file pins
the structural well-formedness that protects the IRI-level drift-zero
contract.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from tools.property_audit import POLICIES  # noqa: E402

CONTEXT_FILE = REPO_ROOT / "data" / "context.jsonld"

# JSON-LD reserved keys / structural keys that legitimately appear in
# @context but are NOT schema properties.
JSONLD_RESERVED: frozenset[str] = frozenset({
    "@version", "@base", "@vocab", "@language", "@protected",
    "id", "type",  # mapped to @id / @type — JSON-LD canonical aliases
})

# Type/Class terms used by data records under "type": "..." values.
# These are not schema properties but legal JSON-LD `@type` aliases.
TYPE_ALIASES: frozenset[str] = frozenset({
    "Concept", "Theorem", "Corollary", "Definition", "Construction",
    "Claim", "Evidence", "Person", "Paper", "event",
})

# Auxiliary terms used inside claim records' `evidence` array entries
# (page / quote / quote_lang) when claims cite verbatim. These are not
# top-level schema properties but legitimate context entries.
EVIDENCE_DETAIL_TERMS: frozenset[str] = frozenset({
    "page", "quote", "quote_lang", "claims",
})

# Allowed namespace prefixes (defined inside the context).
EXPECTED_PREFIXES: frozenset[str] = frozenset({
    "iut", "claim", "evidence", "math", "schema", "xsd",
})

# Allowed @type values inside property mappings.
ALLOWED_TYPE_VALUES: frozenset[str] = frozenset({
    "@id", "xsd:date", "xsd:gYear",
})


def _load_context() -> dict[str, object]:
    with CONTEXT_FILE.open("r", encoding="utf-8") as fh:
        doc = json.load(fh)
    ctx = doc.get("@context")
    if not isinstance(ctx, dict):
        raise ValueError(f"{CONTEXT_FILE} @context is not a dict")
    return ctx


def _all_schema_properties() -> set[str]:
    out: set[str] = set()
    for policy in POLICIES:
        path = REPO_ROOT / "schemas" / policy.schema_file
        with path.open("r", encoding="utf-8") as fh:
            schema = json.load(fh)
        out.update(schema.get("properties", {}).keys())
    return out


class ReverseDirectionTests(unittest.TestCase):
    """Every @context key must justify its existence."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.ctx = _load_context()
        cls.schema_props = _all_schema_properties()

    def test_no_orphan_context_terms(self) -> None:
        legit = (
            self.schema_props
            | JSONLD_RESERVED
            | TYPE_ALIASES
            | EVIDENCE_DETAIL_TERMS
            | EXPECTED_PREFIXES
        )
        orphans = []
        for key in self.ctx:
            if key in legit:
                continue
            orphans.append(key)
        self.assertFalse(
            orphans,
            (
                f"@context contains orphan terms (no schema property, no "
                f"JSON-LD reserved, no allow-listed alias): {orphans}. "
                f"Either add as a schema property, or add to an allow-list "
                f"in test_context_bidirectional.py with rationale."
            ),
        )

    def test_namespace_prefixes_resolve(self) -> None:
        """Every prefix the context uses (iut:, schema:, xsd:) must be
        defined in the same context. Catches typos like ``schema2:`` or
        unknown prefixes that would expand to broken IRIs."""
        defined_prefixes = {
            k for k, v in self.ctx.items()
            if isinstance(v, str) and v.endswith(("/", "#"))
        }
        for key, value in self.ctx.items():
            iri_text = ""
            if isinstance(value, str):
                iri_text = value
            elif isinstance(value, dict):
                iri_text = str(value.get("@id", ""))
            if ":" not in iri_text or iri_text.startswith(("@", "http", "/")):
                continue
            prefix = iri_text.split(":", 1)[0]
            self.assertIn(
                prefix, defined_prefixes,
                f"context term {key!r} → IRI {iri_text!r} uses undefined "
                f"prefix {prefix!r}",
            )


class TermStructureTests(unittest.TestCase):
    """Structural well-formedness of each context entry."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.ctx = _load_context()

    def test_each_property_term_is_string_or_object(self) -> None:
        for key, value in self.ctx.items():
            if key.startswith("@"):
                continue
            self.assertIsInstance(
                value, (str, dict),
                f"context term {key!r} has unexpected type {type(value).__name__}",
            )

    def test_object_terms_have_id(self) -> None:
        for key, value in self.ctx.items():
            if not isinstance(value, dict):
                continue
            self.assertIn(
                "@id", value,
                f"object-form context term {key!r} missing @id",
            )

    def test_type_values_are_allowed(self) -> None:
        for key, value in self.ctx.items():
            if not isinstance(value, dict):
                continue
            if "@type" not in value:
                continue
            self.assertIn(
                value["@type"], ALLOWED_TYPE_VALUES,
                f"context term {key!r} @type {value['@type']!r} is not in "
                f"the allowed set; if intentional, extend ALLOWED_TYPE_VALUES",
            )

    def test_container_values_are_set(self) -> None:
        for key, value in self.ctx.items():
            if not isinstance(value, dict):
                continue
            if "@container" not in value:
                continue
            self.assertEqual(
                value["@container"], "@set",
                f"context term {key!r} unexpected @container "
                f"{value['@container']!r}; only @set is currently used",
            )


class CollisionTests(unittest.TestCase):
    """No two schema properties expand to the same IRI."""

    def test_no_duplicate_iri_expansion(self) -> None:
        ctx = _load_context()
        schema_props = _all_schema_properties()
        seen: dict[str, str] = {}
        for prop in schema_props:
            value = ctx.get(prop)
            if value is None:
                continue
            iri = value if isinstance(value, str) else str(value.get("@id", ""))
            if not iri:
                continue
            if iri in seen and seen[iri] != prop:
                self.fail(
                    f"properties {seen[iri]!r} and {prop!r} both expand to "
                    f"the same IRI {iri!r}; this collapses the JSON-LD "
                    f"distinction between them"
                )
            seen[iri] = prop


class RoundTripExpansionTests(unittest.TestCase):
    """Smoke test: a synthetic record + the context produces the
    expected expanded IRIs for a few well-known properties."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.ctx = _load_context()

    def _expand_key(self, key: str) -> str:
        """Mini IRI expander — handles only the cases this repo needs.
        Not a full JSON-LD expander."""
        value = self.ctx.get(key)
        if value is None:
            return ""
        iri = value if isinstance(value, str) else str(value.get("@id", ""))
        if ":" in iri and not iri.startswith(("http", "/")):
            prefix, suffix = iri.split(":", 1)
            base = self.ctx.get(prefix)
            if isinstance(base, str):
                return base + suffix
        return iri

    def test_label_expands_to_schema_name(self) -> None:
        self.assertEqual(self._expand_key("label"), "https://schema.org/name")

    def test_archive_url_expands_to_iut_namespace(self) -> None:
        self.assertEqual(
            self._expand_key("archive_url"),
            "https://hinanohart.github.io/iut-status-2026/iri/archiveUrl",
        )

    def test_specific_support_expands_to_iut_namespace(self) -> None:
        self.assertEqual(
            self._expand_key("specific_support"),
            "https://hinanohart.github.io/iut-status-2026/iri/specificSupport",
        )

    def test_role_expands_to_iut_namespace(self) -> None:
        self.assertEqual(
            self._expand_key("role"),
            "https://hinanohart.github.io/iut-status-2026/iri/personRole",
        )

    def test_url_expands_to_schema_org(self) -> None:
        self.assertEqual(self._expand_key("url"), "https://schema.org/url")


if __name__ == "__main__":
    unittest.main()
