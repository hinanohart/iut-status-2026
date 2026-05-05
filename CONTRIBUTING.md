# Contributing to iut-status-2026

This repository is a neutral, machine-checkable index of the current
status of Inter-universal Teichmüller theory and surrounding dispute.
Contributions are welcome under the rules below.

## What this repository accepts

- New evidence records (papers, blog posts, talks, formalization
  progress) with stable URLs and dates.
- New claim records that point to specific evidence.
- Corrections to existing records (typos, dates, URLs).
- Lean 4 stubs that compile (still `sorry`-bodied is fine).
- Schema improvements that strengthen drift-resistance.

## What this repository does NOT accept

- Personal opinions about who is right.
- Synthesizing multiple claims into a single "consensus" claim.
- Removing claims by any party (Mochizuki, Scholze, Stix, Joshi, et al.).
- Translating IUT concepts into Scholze-school vocabulary in `data/*.json`.
- Direct redistribution of copyrighted PDFs, figures, or prose passages.
- Editorial commentary in claim labels (labels must be neutral
  statements of fact about what the claim says, not about its merit).

## PR rules

1. PR must carry exactly one of these labels: `evidence-only`,
   `claim-add`, `entity-add`, `lean-stub`, `schema`, `docs-fix`,
   `infra`.
2. PR description must list every IRI added/modified.
3. CI must pass:
   - `python tools/validate.py` (structural)
   - `python -m unittest tests.test_validation` (semantic)
   - Lean build (when applicable)
4. PR that adds a claim must also add its evidence record in the same PR.
5. PR that asserts "the dispute is over" or any equivalent will be closed.

## Citation policy

- Quote statement-level material only (theorems, corollaries,
  definitions). These are not subject to copyright.
- Always include DOI or stable URL + page/section.
- Do not embed copyrighted PDF excerpts as prose blockquotes longer than
  one sentence.

## Conduct

See `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).
Anti-harassment rules are enforced. Real-name accusations or
ad-hominem about mathematicians (Mochizuki, Scholze, Stix, Joshi, or
any commenter) result in immediate PR/Issue closure.

## Take-down

If you are an author or rights holder of cited material and believe
this repository's use of your statement-level quotation falls outside
fair use, please open a GitHub Issue with the `takedown` label or
contact the repository owner via GitHub. Legitimate take-down
requests are honoured promptly.
