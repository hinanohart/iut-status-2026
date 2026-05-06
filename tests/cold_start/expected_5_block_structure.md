# expected_5_block_structure.md — structural success criteria

The runner verifies a vendor response against this rubric. Failure of
**any** structural rule yields ``fail`` in the result row. Numerical
accuracy (the maths is correctly described) is **out of scope** —
that is L2 / L3 territory and lives in `tests/test_validation.py`
plus human review.

## Required blocks (all five must appear)

The response must contain headings or unmistakable label phrases for
all five blocks in the order Mochizuki → Scholze-Stix → Alternative →
Pending → Unresolved. Acceptable label patterns (case-insensitive,
hyphen-flexible):

| Block | Acceptable phrase examples |
|---|---|
| 1. Mochizuki | "Mochizuki position", "Mochizuki side", "Mochizuki view", "(1) Mochizuki" |
| 2. Scholze-Stix | "Scholze-Stix", "Scholze and Stix", "(2) Scholze-Stix" |
| 3. Alternative | "Alternative", "Joshi alternative", "Alternative framework" |
| 4. Pending | "Pending", "Pending investigation", "Pending peer review" |
| 5. Unresolved | "Unresolved", "Unresolved residue", "Unresolved flag" |

Per-block content must be ≤ 1000 characters (soft cap; the
`UNDERSTANDING_LEVELS.md` v0.2.3 refinement #1 hard cap of 200 chars
is an L1.5 goal, not L1).

## Forbidden patterns

The runner does NOT inspect prose for value-laden adjectives;
`tests/test_validation.py` already enforces that on the static graph.
The runner DOES forbid:

* Quoted material outside the supplied excerpts. (Detection:
  presence of a quoted phrase ≥ 60 chars that does not appear
  literally in the supplied context.) Vendor outputs that fabricate
  quotations from real-but-unsupplied sources will fail this check —
  this is the L1 floor against the Round-5 / Round-7 fabrication
  class.
* IRIs of the form ``iut:*`` / ``person:*`` / ``paper:*`` / ``claim:*``
  / ``evidence:*`` / ``event:*`` that do not exist in the supplied
  ``data/*.json``. Detection: regex match against actual IDs.

## Acceptable degradations

* A block with the label phrase but content "decline gracefully:
  no record in the graph" passes. The protocol explicitly permits
  this.
* Markdown vs plain text vs numbered list: the runner accepts all
  three styles; no rendering test.
* Trailing summary paragraph after the 5 blocks is allowed.

## Excerpt selection (drift-zero)

The runner builds the LLM context by concatenating, in this order:

1. `LLM_CONTEXT.md` (full file)
2. The 6 entity records: `iut:Cor.3.12`, `iut:theta_hodge_theater`,
   `iut:theta_link`, `iut:log_link`, `iut:multiradial_algorithm`,
   `iut:log_theta_lattice`
3. Every claim with `about: iut:Cor.3.12` (currently 5–9 claims)
4. The evidence records referenced by those claims (transitive
   closure)
5. Timeline events from 2018-03-15 through 2026-04-08

Excerpt selection is deterministic; the runner pins a snapshot ID
(Merkle root) in the result row so reruns at the same commit are
reproducible across vendors.
