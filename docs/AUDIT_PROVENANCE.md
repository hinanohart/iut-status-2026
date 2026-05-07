# AUDIT_PROVENANCE.md — honest record of audit independence

The architecture documents (`UNDERSTANDING_LEVELS.md`, `ARCHITECTURE.md`,
`FAILURE_MODES.md`, this `INNOVATION_LOG.md` entries) were produced by
multiple "audit rounds" run inside a single LLM family. This file
records that fact transparently so any reader can calibrate the level
of independence behind the design.

## Disclaimer (top of every audit doc)

> All audit rounds for this repository, through commit `591fab2`
> (v0.2.3), were produced inside a single Claude (Anthropic) family
> session, by sub-agents with shared model weights. **Independence
> across LLM vendors is not established at this time.** Multi-vendor
> evidence is the responsibility of the L1 cold-start CI matrix in
> `docs/cold_start_evidence.md`; that file is the source of truth for
> independence claims, not the audit documents themselves.

## Round table

| Round | Date | Trigger | Agents | Same conversation? | Independence claim | Critical defect found |
|---|---|---|---|---|---|---|
| 1 | 2026-05-06 | initial design | analyst + architect + critic + premise-monitor + tracer + 10-trial verifier (4–6 agents) | Same Claude session | None — single LLM family | structural foundations |
| 2 | 2026-05-06 | "ここさらに固めて" (further harden) | analyst + architect + critic | Same Claude session | None — same family | 5 hidden failure modes |
| 3 | 2026-05-06 | "ここさらに固めて" (further harden) | architect + analyst + critic | Same Claude session | None — same family. Round 3 explicitly identified the independence gap. | 3 internal inconsistencies + 1 numerical-premise drift |
| 4 | 2026-05-06 | user override「欠陥や漏れがないか徹底的にチェック前提すら疑って」 | analyst + architect + critic | Same Claude session | None — same family | tempered_rigidity misattribution / paper duplication / SS silent error / verbatim cap mismatch |
| 5 | 2026-05-06 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **Joshi v2 (2026-05-02) fictional evidence** + §1.4 verbatim mis-quote + 6 ATS arXiv IRI drift |
| 6 | 2026-05-07 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **Woit blog dating drift (1.5y)** + timeline url gap + Joshi URL canonical + verbatim cap doc sync |
| 6.5 | 2026-05-07 | systemic root-cause repair | architect + analyst | Same Claude session | None — same family | URL liveness verifier added (closes round 4-6 systemic gap: validate.py never compared graph URLs to external reality) |
| 7 | 2026-05-07 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **Kato ISBN fabrication (978-4-04-110262-7 → 978-4-04-400417-0)** + PRIMS issue ID drift (/249→/1507, 2 records) + Frobenioids_I URL filename typo + 2018 SS visit actors over-listed (Yamashita removed) + governance gate honest revision |
| 8 | 2026-05-07 | user override (same phrase, after Round 7 analyst recommended skip) | analyst + architect + critic | Same Claude session | None — same family | **fabricated ISBN scrub miss in `docs/section_8_disputes_timeline.md`** (R7 thought it was closed; data/ was repaired but docs/ prose retained the fabrication) + placeholder model id `claude-opus-4-5` (not real) + JSON-LD context.jsonld missing v0.7.0/v0.7.2 mappings + cold-start IRI check structurally false-fails + Wayback URL scheme drift + 6 minor pattern-matching gaps |
| 9 | 2026-05-07 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **`docs/disputes.md` + `timeline.md` + `overview.md` 6-release stale auto-generated artefacts** (R6/R7 fix values absent at 4 sites — PRIMS /249 ×3, Frobenioids URL typo, 2018 SS visit Yamashita actor — survived 6 release boundaries despite v0.7.6 "documentation coherence pass" claim) + **`mcp/server.py` silently dropped 5 fields** (`archive_url` ×2, `role`, `specific_support`, `lean_stub`) and `loaders/python_minimal.py` Claim dataclass missing `specific_support` (drift-zero contract violation across consumer chain) + **v0.7.7 BLOCK_LABEL_PATTERNS over-tightened** (false-positive close → false-negative regression for natural-prose responses) + **`LICENSE` short-form** (Apache-2.0 §4.a violation; full text required for SPDX `Apache-2.0` identification) + 2 hand-written prose retentions (`section_8` 2018 SS visit Yamashita actor + `section_6_cor_3_12.md:421` Joshi v1+v2) + ARCHITECTURE.md 6 dead schemas/v0.{2,3} refs (Round 8 commit message claimed "6 eliminated" but 3 remained); meta-finding: 8 connected releases in 1 day exceeded audit cadence, batch-end audit detected systemic but per-release mini-audit was recommended for Round 9+ |
| 9.5 | 2026-05-07 | systemic root-cause repair (post-Round-9, no new audit) | architect + analyst | Same Claude session | None — same family. v0.7.9 ships `tools/property_audit.py` + CI gate to close the R4-R9 multi-layer-drift class structurally rather than via further per-round detection. Empirical validation: the audit caught a fresh CRITICAL on its first execution (`_claim_to_json` silently dropped the `type` field — entity serializer emitted, claim serializer did not). Fix shipped in the same commit. | `_claim_to_json` `type` field drop (R9-class drift that survived R9); structural gate now blocks this class going forward |

## Numerical premises and their verification status

Round-3 critic flagged that audit prompts contained numerical premises
that the agents accepted without verification. The verified record:

| Claim in prompt | Source-of-claim | Actual value | Status |
|---|---|---|---|
| "docs 5500 行" | round-3 prompt | 4357 lines (`wc -l docs/**/*.md`, 2026-05-06) | OVERSTATED |
| "code 1000 行" | round-3 prompt | 1582 lines | UNDERSTATED |
| "docs / code = 5.5 : 1" | round-3 prompt | 2.75 : 1 | OVERSTATED |
| "10 / 10 cold-start PASS" | v0.2.0 verifier | 10 / 10 in single-Claude simulation; **0 / 10** real multi-vendor runs | MISLEADING UNTIL CI MATRIX RUNS |

Future audit prompts must inline the verification command and date for
every numerical premise (e.g. `docs lines: 4357 (verified by wc -l on
2026-05-06, commit 591fab2)`). Audit agents must reject prompts that
quote unverified numbers.

## Re-opening conditions for additional audit rounds

Original gate (v0.2.4 — formally maintained but **functionally bypassed
by user override in rounds 4 / 5 / 6 / 7**):

> Audit rounds are paused indefinitely until at least one of the
> following triggers fires:
> (a) actual non-Claude vendor cold-start run; (b) external reviewer
> report; (c) v0.3 schema-changing PR.

**Honest revision (v0.6.1, after round 7 analyst critique)**: the gate
above is preserved as the long-term ideal but does NOT actually block
audit rounds in practice. The de-facto governance is:

- **User override is the operative gate**: when the maintainer types
  「欠陥や漏れがないか徹底的にチェック前提すら疑って」 or equivalent,
  a new audit round runs.
- Each user-override round is recorded in the corresponding patch
  commit message ("Round N was permitted by user override of the
  indefinite pause set at v0.2.4").
- Rounds 4-7 each found at least one CRITICAL fabrication-class
  defect that prior rounds missed; the gate, if strictly enforced,
  would have shipped those defects.

The right reading: the original gate was a hedge against audit fatigue,
but in practice external-reality verification gaps surface faster than
multi-vendor evidence accrues. The user-override mechanism produces
healthier outcomes and is the documented operative protocol going
forward.

Original triggers (a) (b) (c) are still desirable — they raise the
quality of audits beyond Claude-family bias — but they are
**aspirations**, not gates.

## Why this gate exists

Without a real-vendor independence signal, additional Claude-only audit
rounds add documentation lines but do not increase the actual
independence of the design. Round-2 caught five hidden failure modes
that round-1 missed; round-3 caught three internal inconsistencies and
one numerical-premise drift; round-4 is forecast to be marginal at
best, NO-OP at worst, while continuing to push the meta-doc /
object-doc ratio into the red. The gate is a structural commitment,
not a polite suggestion.
