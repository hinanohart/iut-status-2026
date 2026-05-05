# FAILURE_MODES.md — predicted failure modes of large-scale expansion + mitigations

Catalogues the failure modes identified by the v0.2.2 architecture review
(3-agent design audit, 2026-05-06) and pairs each with a concrete mitigation
that is enforced before the corresponding scale milestone.

## Top-5 (probability × impact)

### 1. Verbatim accuracy collapse (≈ 85 % probability, fatal impact)

When 200 + verbatim short quotations need to be PDF-verified one by one,
agents tend to settle for "approximately the same" wording. The v0.1.1
audit caught one such drift (`claim:scholze_stix_2018_sub_1` had three
co-existing wordings of the same SS p.6 sentence).

**Mitigation.**
- `verbatim_sha256` is REQUIRED on every record that has
  `verbatim_short_statement`.
- `tools/verify_verbatim.py --with-pdf-cache` recomputes the SHA-256
  from the cached PDF text at the locator and fails CI on mismatch.
- The PDF cache is local (gitignored) but its SHA-256 + pymupdf version
  are pinned in `evidence.json` so any agent or CI runner extracts the
  same bytes.
- Auditing 200 records by hand is acknowledged infeasible; the chain
  must be machine-verifiable end-to-end.

### 2. Citation bloat / fair-use red zone (≈ 70 % probability, legal impact)

200 + short quotations across four Mochizuki PDFs accumulate to a
"substantial portion" risk under US fair-use's `amount` factor and Japanese
Copyright Act Article 32's necessity test, even if each individual
quotation is a single sentence.

**Mitigation.**
- `verbatim_short_statement` is ≤ 200 characters by schema constraint.
- Quotation **bodies** are NOT redistributed; only locators
  (`(paper_iri, page, line, sha256)`) and short snippets are in the repo.
- Full PDF content lives in the host-local `cache/` (gitignored).
- `NOTICE` is updated to make the fair-use posture explicit per record
  type, with reference to US 17 USC §107 four-factor analysis and JP CL
  Art. 32.
- Periodic legal review noted: when total `verbatim_short_statement` byte
  count exceeds 50 KB (≈ 250 records × 200 chars), a human review is
  required before the next minor release.

### 3. Maintenance burden / bus factor 1 (≈ 95 % probability, sustainability impact)

A single maintainer cannot manually re-verify 200 + records each time a
new Mochizuki / Joshi / LANA update appears.

**Mitigation.**
- `verified_at` is removed from individual records; CI populates it
  from `git log --format="%ad" -- <file>` per shard, eliminating manual
  drift.
- The innovation-explorer GitHub Actions CRON surfaces new arXiv / RIMS
  publications and opens a draft PR for triage; the maintainer reviews
  and merges, rather than monitoring manually.
- All cross-reference checks are CI-enforced; a missing `evidence` link
  fails the build.
- A `maintainers.md` is added with explicit hand-off documentation so
  the bus factor is one only de jure, not de facto.

### 4. PDF reproducibility / page-number drift (≈ 60 % probability, medium impact)

PRIMS pre-publication preprints and post-publication versions can have
slightly different pagination. `pymupdf` minor-version upgrades change
whitespace normalisation.

**Mitigation.**
- `evidence.json` records `pdf_sha256` and `pymupdf_version_used`.
- `tools/extract_pdf_cache.py` aborts when the local PDF SHA-256 does
  not match the recorded one, with clear error pointing at the canonical
  version.
- `definition_locator` includes `(page, line)` plus a SHA-256 prefix
  triangulating the paragraph, surviving minor whitespace shifts.

### 5. Schema drift / silent field omission (≈ 75 % probability, medium impact)

When v0.3 adds new fields (`verbatim_short_statement`, `verbatim_sha256`,
`definition_locator`), one record among 200 may quietly omit them and pass
loose validation.

**Mitigation.**
- All v0.3 schemas use `additionalProperties: false` plus an explicit
  `required` array including the new mandatory fields.
- `tools/validate.py` rejects any record that lacks `schema_version`.
- `tools/migrate_v0_2_to_v0_3.py` is idempotent and exhaustive: every
  v0.2 record is touched and emitted as v0.3.

## Lesser modes (probability < 60 %)

- **LLM context-window overflow.** Mitigated by `_summary.json` (~ 30 KB
  cold-start) plus per-IRI MCP tools.
- **Cross-reference cycles.** Mitigated by CI-side DAG check on
  `depends_on` and `counters` graphs.
- **Section docs cross-inconsistency.** Mitigated by docs being
  rendered from JSON, not hand-written prose, where feasible. Section
  merge documents continue to be hand-written but cite IRIs not literals.
- **Lean stub explosion.** Mitigated by per-module file split
  (`lean/IutStatus/<concept>.lean` instead of monolithic `Basic.lean`).
- **Innovation log self-contradiction.** Mitigated by the v0.2.1
  audit-driven "log refers to `data/`, never duplicates literals" rule.
- **Multi-vendor claim hollowness.** Mitigated by the
  `cold-start-multi-vendor` CI job (gated on user-provided API keys);
  the README badge state reflects the most recent matrix run.
- **User-intent ambiguity ("really long" = breadth or depth).** Resolved
  by phased expansion: v0.3 broadens (entities), v0.5 deepens (verbatim
  + multi-vendor), v1.0 reconciles. Both interpretations are addressed.

## Devil's-advocate option (recorded, not adopted)

A devil's-advocate review (in the same architecture audit) suggested
freezing at v0.2.x scale (33 entities / 16 claims / ~ 2 500 lines) and
investing exclusively in Level 1 = 100 % (multi-vendor evidence). This is
not the chosen path because it under-delivers on user intent ("really
long"); however, the L1-investment portion of that proposal is folded
into the v0.3 roadmap (multi-vendor CI, verbatim SHA-256 enforcement).

## Audit cadence

- Every v0.x.0 minor release: 3-agent re-audit (analyst + architect +
  critic) before the tag.
- Every v0.x.y patch release: lightweight critic-only diff audit.
- Independent third-party (non-Claude) audit attempted at v0.5 against a
  GPT or Gemini fresh session, with results recorded in
  `docs/cold_start_evidence.md` whether PASS or FAIL.
