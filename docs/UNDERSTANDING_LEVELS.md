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
- L2a: `scripts/coverage_report.py --paper IUTchI` prints registered fraction (target ≥ 80 % at v0.5, ≥ 95 % at v1.0).
- L2b: every Yamashita FAQ "Q" has a corresponding `claim:yamashita_faq_q###`.
- L2c: every section of SS 2018 (10 pp.), Mochizuki Rpt 2018, and Joshi v2 has at least one anchored entity or claim.

**Current status.** Approximately 5 % of L2 (heads of major theorems only;
no FAQ coverage; no per-section SS claims yet).

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

| Version | L1 target | L2 target | scale (entities / claims / lines) |
|---|---|---|---|
| v0.2.x (current) | ~30 % (Claude-only) | ~5 % | 33 / 16 / ~2 500 |
| v0.3 | 50 % (3 vendors, symmetry CI) | 30 % | 80 / 40 / ~5 000 |
| v0.5 | 80 % (5 vendors, full L1 CI) | 60 % | 150 / 65 / ~10 000 |
| v1.0 (gated on LANA mid-report + 6 mo) | 95 % (7 vendors, full CI) | 80 % | 200 + / 80 + / ~15 000 + |
| absolute 100 % | feasible (L1) | **forever asymptotic** (L2) | grows with new papers |

L2 100 % is a category error. New papers redefine the goalpost
continuously. L1 100 % is reachable with 7-vendor multi-vendor CI plus
verbatim-SHA256 enforcement; the engineering for that exists in this
repository's architecture (see `ARCHITECTURE.md`) but is implemented
incrementally.

## What this repository will never promise

- Level 3 (mathematical validity).
- Static "100 %" in any meaningful sense across the entire literature.
- Vendor neutrality without empirical evidence per vendor.
- Drift-zero at the prose level (only at the IRI / Merkle layer).
