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

| Round | Date | Trigger | Agents | Same conversation? | Independence claim |
|---|---|---|---|---|---|
| 1 | 2026-05-06 | initial design | analyst + architect + critic + premise-monitor + tracer + 10-trial verifier (4–6 agents) | Same Claude session | None — single LLM family |
| 2 | 2026-05-06 | "ここさらに固めて" (further harden) | analyst + architect + critic | Same Claude session | None — same family |
| 3 | 2026-05-06 | "ここさらに固めて" (further harden) | architect + analyst + critic | Same Claude session | None — same family. Round 3 explicitly identified the independence gap. |

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

Audit rounds are **paused indefinitely** until at least one of the
following triggers fires:

- (a) An actual cold-start fixture run completes against a non-Claude
  vendor (Gemini, GPT, Llama, Qwen, DeepSeek, Mistral, …), with results
  recorded in `docs/cold_start_evidence.md`.
- (b) An external (non-Anthropic-family) reviewer publishes a report on
  the repository, even informally (blog post, GitHub Issue, conference
  abstract).
- (c) A v0.3 schema-changing PR is merged, requiring a fresh design
  review.

Re-opening requires a public GitHub Issue documenting which condition
fired, before the new round may begin. Audit rounds outside this gate
are NO-OP; their output is not merged.

## Why this gate exists

Without a real-vendor independence signal, additional Claude-only audit
rounds add documentation lines but do not increase the actual
independence of the design. Round-2 caught five hidden failure modes
that round-1 missed; round-3 caught three internal inconsistencies and
one numerical-premise drift; round-4 is forecast to be marginal at
best, NO-OP at worst, while continuing to push the meta-doc /
object-doc ratio into the red. The gate is a structural commitment,
not a polite suggestion.
