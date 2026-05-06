# tests/cold_start/ — multi-vendor L1 verification fixtures

This directory contains the fixtures used by
`.github/workflows/cold_start_weekly.yml` to verify the L1 cold-start
contract on real LLM vendors. The contract is stated in
`docs/UNDERSTANDING_LEVELS.md`:

> A fresh LLM session, given only ``LLM_CONTEXT.md`` + a sample of
> ``data/*.json``, must produce an answer in the 5-block format
> (Mochizuki / Scholze-Stix / Alternative / Pending / Unresolved).

## Files

| File | Role |
|---|---|
| `prompt.txt` | Fixed user question; never mutate without bumping fixture version. |
| `run_cold_start.py` | Stdlib-only runner. `--vendor` selects API target. Writes one row to `docs/cold_start_evidence.md`. |
| `expected_5_block_structure.md` | Structural success criteria the runner verifies. |

## Vendor contract

The runner currently supports `--vendor claude` (Anthropic Messages
API). Future v0.7.x will add `gpt`, `gemini`, `llama`. Each vendor
requires its own secret in the GitHub Actions environment:

* `ANTHROPIC_API_KEY` (Claude)
* `OPENAI_API_KEY` (GPT)
* `GOOGLE_API_KEY` (Gemini)

If a secret is absent, the corresponding job exits 0 with a
``skipped: secret not configured`` row appended to
`docs/cold_start_evidence.md`. Cold-start is treated as
**advisory CI**: failures do not block PR merges, only inform the
roadmap.

## Result format

Each runner appends one Markdown row to
`docs/cold_start_evidence.md`:

```
| 2026-05-07 | claude-opus-4-7 | pass | 5/5 blocks present, ≤200 chars per block |
```

Failures still append a row with `fail` and a one-line diagnostic;
the row is the audit trail.

## Why advisory only

L1 success is a measurement, not a gate. PRs that improve the graph
should not be blocked because OpenAI's API rate-limited the runner
this hour. The weekly schedule and workflow_dispatch trigger are the
correct cadence: a maintainer-readable signal, not a per-commit
guard. Per-commit guards belong in `.github/workflows/ci.yml` (the
structural / Merkle / verbatim-cap layer).

## Drift-zero contract

The runner sends only the contents of `LLM_CONTEXT.md` plus a
deterministic excerpt of `data/*.json` (the seed records named in
`prompt.txt`). It does NOT include the maintainer's git history,
branch state, or unrelated docs; this keeps each run reproducible
across vendors and across weeks. Excerpt selection is documented in
`expected_5_block_structure.md` so a third-party can replay the
fixture without access to this repository's CI environment.
