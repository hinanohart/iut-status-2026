# cold_start_evidence.md — multi-vendor cold-start record

This file is referenced by ``docs/UNDERSTANDING_LEVELS.md`` (L1
specification refinement #6), ``docs/AUDIT_PROVENANCE.md`` (independence
disclaimer), ``docs/FAILURE_MODES.md`` (mode VC-1 mitigation),
``LLM_CONTEXT.md`` §3.2, and ``README.md`` Roadmap. It is the **single
source of truth for L1 cold-start independence claims**; the audit
documents themselves are not.

## Status (v0.7.0, 2026-05-07)

**No real multi-vendor cold-start runs have been performed.**

Every audit round through v0.6.1 (rounds 1-7) was conducted inside a
single Anthropic Claude family session. The L1 success criterion
"a fresh LLM session, given only ``LLM_CONTEXT.md`` + ``data/*.json``,
can answer every IUT-status question via the 5-block protocol" is
**unverified** at multi-vendor scale.

| Vendor | Cold-start runs (real) | Cold-start runs (Claude-simulated) | Outcome |
|---|---|---|---|
| Anthropic Claude | 0 | 10 / 10 | passed in single-Claude simulation only |
| OpenAI GPT | 0 | 0 | not yet attempted |
| Google Gemini | 0 | 0 | not yet attempted |
| Meta Llama | 0 | 0 | not yet attempted |
| Mistral | 0 | 0 | not yet attempted |
| Alibaba Qwen | 0 | 0 | not yet attempted |
| DeepSeek | 0 | 0 | not yet attempted |
| **total** | **0** | **10 / 10** | **single-vendor simulation only — not vendor-neutral evidence** |

The single-Claude "10 / 10 pass" figure was reported in
``tests/test_validation.py`` as a 5-block-template structural check on
synthetic prompts. It is not external evidence of vendor-neutrality.

## Why this file exists empty

L1 spec refinement #6 (``UNDERSTANDING_LEVELS.md``) declares
"consumer-class L1 fixtures" mandatory. Without an actual run, the
auto-verifiable success criterion is empty and any "vendor-neutral"
claim in the audit documents is aspirational rather than evidenced.
Documenting this state explicitly avoids the failure mode where a
reader assumes evidence exists somewhere because it is referenced.

## v0.7+ plan

1. ``tests/cold_start/`` fixture directory: chat-context (LLM_CONTEXT
   + data/*.json pasted), MCP-only (vendor-neutral MCP server),
   RAG-style (no-prompt, only retrieval).
2. ``.github/workflows/cold_start_weekly.yml``: 3-vendor matrix
   (Claude / GPT / Gemini), gated on API key secrets, allowed-to-fail.
3. ``.github/workflows/cold_start_monthly.yml``: 7-vendor matrix
   (adds Llama / Mistral / Qwen / DeepSeek).
4. Each run writes a row to this file (vendor / date / pass-rate /
   commit hash / fixture used). The file becomes the longitudinal
   evidence base for L1 independence claims.

## Honest reading

A reader coming from ``UNDERSTANDING_LEVELS.md`` Roadmap "v0.2.x
(current) | ~30 % (Claude-only) | ~5 % | 33 / 16 / ~2 500" should
understand:

- The ~30 % L1 figure is a **single-Claude** estimate.
- Real multi-vendor pass-rate is **unknown** until the workflows
  above land.
- "vendor-neutral" in this repository means **the schema, IRIs, and
  protocol are designed to be vendor-neutral**, not that
  vendor-neutrality has been **demonstrated**.

The distinction matters: the same misreading is what produced the
Round-3 "10 / 10" overstatement that ``AUDIT_PROVENANCE.md`` records.

## Reference

- ``docs/UNDERSTANDING_LEVELS.md`` L1 success criteria L1a-e
- ``docs/AUDIT_PROVENANCE.md`` independence disclaimer
- ``docs/FAILURE_MODES.md`` VC-1 vendor-class collapse
- ``LLM_CONTEXT.md`` §3.2 cold-start protocol
- ``README.md`` "Roadmap (revised v0.2.2, post-architecture review)"
