# UNDERSTANDING_LEVELS.md — what "100% understanding" actually means here

This document is the **operational definition** of "100% understanding" for
`iut-status-2026`. It must be read alongside `LLM_CONTEXT.md` §4 (honest scope).

User intent in casual language is "have an LLM (Claude / any AI) understand
IUT 100% from a cold start." That intent decomposes into three levels with
sharply different feasibility.

## Level 1 — AI Navigation Capability

**Statement.** A fresh LLM session, given only `LLM_CONTEXT.md` plus
`data/*.json`, can:
- resolve any IUT IRI registered in the graph,
- apply the 5-block answer template (Mochizuki / SS / Alternative / Pending / Unresolved),
- cite verbatim short statements with their `definition_locator`,
- preserve symmetry between Mochizuki-side and SS-side citations,
- decline gracefully when the graph is silent on a question.

**Feasibility.** Achievable in this OSS, by this OSS alone. No external
dependencies.

**Auto-verifiable success criteria.**
- L1a: `tests/cold_start/` passes 10 prompts × N vendors (target: 7 vendors — Claude / GPT / Gemini / Grok / Llama / Mistral / Qwen / DeepSeek). Today: Claude only.
- L1b: every claim's `evidence` IRI resolves; every entity's `depends_on` IRI resolves.
- L1c: per-claim Mochizuki-side / SS-side verbatim character ratio in [0.7, 1.3].
- L1d: every disputed claim carries an explicit unresolved flag (no claim labelled "resolved").
- L1e: 5-block conformance ≥ 8 / 10 on the cold-start fixture.

**Current status (2026-05-06).** Approximately 30 % of L1 (single-vendor
simulation only; multi-vendor test pending; symmetry not yet auto-checked).

## Level 2 — Asymptotic Statement Coverage

**Statement.** Every numbered statement (Theorem / Definition / Corollary)
in IUTchI – IUTchIV, in Frobenioids I & II, in *The étale theta function*, in
the Mochizuki survey *Mathematics of Mutually Alien Copies*, in the Mochizuki
*Report on Discussions* and *Cmt2018-05* and *IUT-report-2025-10*, in the
Yamashita FAQ, in Scholze–Stix 2018, and in Joshi v1 / v2, is registered as
an entity or claim with a stable IRI and a `definition_locator`. Every
position any party has publicly published is registered as a claim.

**Feasibility.** **Asymptotic, not absolute.** New papers will continue to
appear (e.g. LANA mid-report 2026-07-17, Joshi v3, Mochizuki future
updates). The asymptote can be approached but not reached; "100 %" is a
limit, not an achievable state.

**Auto-verifiable success criteria.**
- L2a: `scripts/coverage_report.py --paper IUTchI` prints registered fraction (target ≥ 80 % at v0.5, ≥ 95 % at v1.0). **As of v0.7.7 the script does not yet exist; the figures in the Roadmap table are self-graded estimates and Round 8 audit recorded that gap. Implementation tracked under v0.8.**
- L2b: every Yamashita FAQ "Q" has a corresponding `claim:yamashita_faq_q###`.
- L2c: every section of SS 2018 (10 pp.), Mochizuki Rpt 2018, and Joshi FAQ 2025-11 has at least one anchored entity or claim.

**Current status.** Approximately 5 % of L2 (heads of major theorems only;
no FAQ coverage; no per-section SS claims yet).

## Level 1.5 — Formally-Verified Navigation (interim, post-LANA)

**Statement.** Every Lean stub in `lean/IutStatus/*.lean` has its `sorry`
replaced by a body that compiles against `mathlib4` plus the LANA library
(once published), and every entity carries a `lean_path` field pointing to
the corresponding formal definition. Navigation answers can cite a Lean
theorem name in addition to (not instead of) a paper / page locator.

**Feasibility.** Achievable **only after** LANA delivers a usable formal
library. The Lean naming convention in this repository is forward-compatible
with LANA module conventions; bodies are replaceable mechanically.

**Auto-verifiable success criteria.**
- L1.5a: `lake build` exits 0 with no `sorry` remaining.
- L1.5b: every entity has a populated `lean_path`.
- L1.5c: an L1 cold-start fixture answer cites a Lean theorem name where
  one is registered.

**Current status (2026-05-06).** 0 % (LANA in progress; mid-report
2026-07-17). L1.5 status is gated externally; the OSS implementation is
ready to absorb LANA output as soon as it is published.

## Level 3 — Mathematical Understanding (validity judgment)

**Statement.** Decide whether IUT, as Mochizuki formulated it, proves the
abc conjecture; decide whether the Scholze–Stix critique is terminal; decide
whether the Joshi reformulation succeeds.

**Feasibility.** **Out of scope for this repository, intentionally and
permanently.** Validity judgement is not delegated to an LLM-readable
artefact. It is the work of the human mathematical community and of formal
proof assistants (LANA Lean 4 formalization).

**This OSS does not, and will not, claim Level 3.** Pointers are provided
to where Level 3 is being pursued externally:
- LANA project (Lean 4 formalization, mid-report scheduled 2026-07-17)
- Future RIMS, PRIMS, EMS Press, Annals, JAMS reviews
- Future independent third-party formalizations

## Roadmap (revised v0.2.2, post-architecture review)

| Version | L1 target | L2 target | scale (entities / claims / evidence / timeline) |
|---|---|---|---|
| v0.2.x (closed 2026-05-06) | ~30 % (Claude-only) | ~5 % | 33 / 16 / 24 / 20 |
| **v0.7.x (current, 2026-05-07)** | **~30 %** (still Claude-only — see `cold_start_evidence.md`; cold-start CI scaffolding shipped v0.7.4 awaiting `ANTHROPIC_API_KEY` secret) | **~10 % (self-graded; `scripts/coverage_report.py` not yet implemented)** | **104 / 53 / 34 / 25** |
| v0.8 (cold-start 3-vendor matrix) | 50 % (3 vendors, symmetry CI) | 30 % | 130 / 70 / 50 / 35 |
| v0.9 (5-vendor matrix + full L1 CI) | 80 % | 60 % | 150 / 80 / 60 / 40 |
| v1.0 (gated on LANA mid-report 2026-07-17 + 6 mo) | 95 % (7 vendors) | 80 % | 200 + / 100 + / 80 + / 50 + |
| absolute 100 % | feasible (L1) | **forever asymptotic** (L2) | grows with new papers |

L2 100 % is a category error. New papers redefine the goalpost
continuously. L1 100 % is reachable with 7-vendor multi-vendor CI plus
verbatim-SHA256 enforcement; the engineering for that exists in this
repository's architecture (see `ARCHITECTURE.md`) but is implemented
incrementally.

## L1 specification refinements (v0.2.3 stress-test)

The following additions resolve ambiguities found by the round-2
analyst stress-test (2026-05-06). They are normative; CI will gate them
once implemented.

1. **L1 prose quality bound.** A prose answer derived from an IRI must be
   ≤ 200 characters per block, must contain ≥ 1 verbatim short quotation
   from the cited evidence, and must contain 0 value-laden adjectives in
   the LLM's own voice (cross-reference `LLM_CONTEXT.md` §3.4).
2. **5-block content floor.** Each of the five blocks must contain ≥ 1
   sentence. The Pending block, while
   `claim:lana_formalization_in_progress.status` indicates the
   investigation is active, must cite that claim explicitly; "no pending
   investigation indexed" is non-conforming during that period.
3. **Symmetry secondary axis.** In addition to character ratio in
   [0.7, 1.3], the Mochizuki-side and SS-side citation counts must each
   be ≥ 1, and the verbs framing each side must come from a small
   approved list ("asserts", "writes", "argues", "states") rather than
   evaluative verbs ("admits", "concedes", "claims wrongly").
4. **Coverage denominator freeze.** L2 percentages are computed against
   a paper-version-frozen denominator. New paper versions add a separate
   row in the L2 report rather than overwriting the existing percentage.
5. **L3 reclassification protocol.** The "out-of-scope" status of L3 is
   revisable only if all three gates fire: (a) LANA produces a verified
   formalization of the disputed corollary, (b) at least 6 calendar
   months elapse without contradicting external publication, (c) ≥ 1
   independent third-party (non-LANA) verification appears. Any
   reclassification proposal opens a 30-day public comment period via
   GitHub Issue before merge.
6. **Consumer-class L1 specifications.** Three classes — chat-context,
   MCP-only, and RAG / multi-document — each have separate L1 fixtures.
   The current cold-start fixture is the chat-context class; MCP-only
   and RAG fixtures are added at v0.3.
7. **L1.5 forward-compatibility.** When LANA publishes any IUT-relevant
   formalization, every affected entity gains a `lean_path` field in the
   same commit that ingests the LANA artefact. L1.5 progress is tracked
   in `docs/cold_start_evidence.md` alongside L1.

## Common misreadings of "100 % understanding" (warnings)

These misreadings have been observed or predicted; they are wrong.

1. **"LANA mid-report 2026-07-17 = L3 achieved."** The mid-report is a
   formalization progress update, not a validity judgement. L3 reclassification
   requires the triple gate above.
2. **"L1 = 95 % means IUT is 95 % understood."** L1 is protocol
   compliance: navigation, citation, decline-gracefully. It is not a
   measure of mathematical content mastery.
3. **"L2 = 80 % means 80 % of the IUT literature is indexed."** L2 is
   computed against papers registered in `data/entities.json` of type
   `Paper`. Papers outside that set (e.g. Hoshi survey, Tan thesis,
   Dupuy–Hilado preprints) are out of denominator until registered.

## Glossary (single source of truth)

To prevent terminology drift identified at round-3:

- **drift-zero (cryptographic)**: deterministic and machine-verifiable
  at the Merkle / IRI layer. Used only for the physical and IRI levels.
- **drift-resistant**: best-effort at the claim graph and prose layers;
  not deterministic.
- **L1 / L1.5 / L2 / L3**: the level numbers from this document. Always
  use the level number, never paraphrases such as "navigation" alone.
- **L1-100**: shorthand for "L1 = 100 % cold-start conformance,
  multi-vendor evidence on file". Distinct from "100 % understanding"
  in lay usage.
- **Cold-start**: an LLM session with no prior memory of this
  repository. Conformance is verified against the `tests/cold_start/`
  fixture (chat-context class) plus the multi-vendor CI matrix.

## What this repository will never promise

- Level 3 (mathematical validity).
- Static "100 %" in any meaningful sense across the entire literature.
- Vendor neutrality without empirical evidence per vendor.
- Drift-zero at the prose level (only at the IRI / Merkle layer).
