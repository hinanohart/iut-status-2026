# ARCHITECTURE.md — scaling design (v0.3 → v1.0)

This document specifies the architecture for scaling `iut-status-2026` from
33 entities / 16 claims / ~2 500 lines (v0.2.x) to ~200 entities / ~80
claims / ~15 000 + lines (v1.0). It complements `UNDERSTANDING_LEVELS.md`
(what we are scaling toward) and `FAILURE_MODES.md` (what to avoid).

## Decision summary

| Concern | Decision |
|---|---|
| JSON sharding | **`entities/all.json` single file** (per-type sharding deferred to v1.0+ when entities > 500); per-section for `claims/by_section/` (≤ 8 shards); `data/manifest.json` lists shards |
| Schema versioning | `schemas/v0.2/` and `schemas/v0.3/` coexist; loader supports both via `oneOf` |
| Cross-reference | **on-the-fly dict comprehension in loader** (≤ 5 ms at v0.5 scale); static `_indexes/` deferred to v1.0+ when entities > 500 |
| Sub-section docs | `docs/section_<n>_<name>/<n><letter>_*.md` + `_verification_log.md` per section |
| PDF cache | NOT in repository; `cache/` is `.gitignore`-d; `verbatim_short_statement` **≤ 200 chars/record (lifted from 100 to admit existing PDF-verified verbatim like the 108-char SS p.6 quotation); cumulative ≤ 30 KB across all data/** (JP CL Art. 32 主従比 1:5 constraint, computed against ≥ 5× larger original prose in `docs/section_*/`); PDF SHA-256 in `evidence.json`; `archive_url` (Wayback) mandatory on every Paper/Blog evidence record from v0.3 onward |
| LLM context window | `data/manifest.json` + `data/_summary.json` cold-start; details lazy-loaded via MCP tools |
| Merkle | per-shard Merkle root → top-level Merkle of Merkles; incremental rebuild |
| Innovation explorer | GitHub Actions CRON daily arXiv / RIMS watch |
| Verbatim verification | SHA-256 over verbatim_short_statement; CI compares to PDF cache when `--with-pdf-cache` |

## Layout (v0.3 +)

```
iut-status-2026/
├── data/
│   ├── manifest.json               # canonical shard list + per-shard SHA-256
│   ├── context.jsonld
│   ├── _summary.json               # IRI + label + type + section, ~30 KB
│   ├── _indexes/                   # build-time, excluded from Merkle
│   │   ├── by_paper.json
│   │   ├── by_section.json
│   │   ├── by_type.json
│   │   └── depends_on_reverse.json
│   ├── entities/
│   │   ├── concept.json
│   │   ├── definition.json
│   │   ├── construction.json
│   │   ├── theorem.json
│   │   ├── corollary.json
│   │   ├── person.json
│   │   └── paper.json
│   ├── claims/
│   │   └── by_section/
│   │       ├── 01_prerequisites.json
│   │       ├── 02_hodge_theater.json
│   │       └── … 08_disputes_timeline.json
│   ├── evidence.json
│   ├── timeline.json
│   └── merkle_root.txt
├── schemas/
│   ├── v0.2/                       # frozen
│   ├── v0.3/                       # current
│   └── latest -> v0.3
├── docs/
│   ├── section_1_prerequisites/
│   │   ├── README.md
│   │   ├── 1a_anabelian.md
│   │   ├── 1b_frobenioid_i.md
│   │   ├── 1c_frobenioid_ii.md
│   │   ├── 1d_etale_theta.md
│   │   ├── 1e_mono_theta_environment.md
│   │   └── _verification_log.md
│   ├── section_2_hodge_theater/
│   │   └── …
│   └── … section_8_disputes_timeline/
├── cache/                          # .gitignore-d, host-local PDFs and extracts
├── tools/
│   ├── build_merkle.py             # per-shard + top-level
│   ├── build_indexes.py            # static index generator
│   ├── extract_pdf_cache.py        # populates ./cache/ from local PDFs
│   ├── verify_verbatim.py          # SHA-256 against cache when present
│   ├── render_md.py
│   └── validate.py
├── mcp/
│   └── server.py                   # gains 5+ tools (by_section / by_paper / ...)
└── …
```

## Schema v0.3 additions

`schemas/v0.3/entity.json`:
- `verbatim_short_statement` — string, ≤ 200 chars, fair-use snippet, optional
- `verbatim_sha256` — string, SHA-256 hex of `verbatim_short_statement`, optional but required when `verbatim_short_statement` is present
- `definition_locator` — string, e.g. `"IUTchI Def 3.6, p.87 (PDF SHA-256 prefix abc123…)"`, optional
- `theorem_number` — string, separate from `label`, optional
- `axiom_count` — integer, count of `axiom` lines in the corresponding Lean module, optional
- `subsection` — string, e.g. `"2a"`, optional
- `schema_version` — const `"0.3"`, required

`schemas/v0.3/claim.json`:
- `verbatim_short_statement` — same form as above
- `verbatim_sha256` — same
- `depends_on_section` — array of section enum, optional
- `schema_version` — const `"0.3"`, required

`schemas/v0.3/evidence.json`:
- `pdf_sha256` — string, hex SHA-256 of the canonical PDF as fetched on a recorded date
- `pdf_fetched_at` — date, when the SHA-256 was recorded
- `pymupdf_version_used` — string, pinned version for reproducible extraction

Backward compatibility: `loaders/python_minimal.py` reads either v0.2 or
v0.3 records (uses `record.get(field)` with safe defaults). Validators
require explicit `schema_version` from v0.3 onward.

## Sharding loader contract

`data/manifest.json`:
```json
{
  "schema_version": "0.3",
  "shards": [
    {"path": "entities/concept.json",    "sha256": "…", "record_count": 12},
    {"path": "entities/definition.json", "sha256": "…", "record_count": 25},
    …
    {"path": "claims/by_section/06_cor_3_12.json", "sha256": "…", "record_count": 11},
    …
  ],
  "summary_path": "_summary.json",
  "indexes_path": "_indexes/",
  "merkle_root": "…"
}
```

`IutGraph.load(data_dir)` walks `manifest.json` and concatenates shards
transparently. A new method `IutGraph.load_summary(data_dir)` reads only
`_summary.json` for cold-start LLM context (~30 KB instead of full ~500 KB
at v1.0 scale).

## Merkle architecture

```
Layer 1: per-record SHA-256 over canonical JSON                 (leaf hash)
Layer 2: per-shard Merkle root                                  (in manifest)
Layer 3: top-level Merkle of (shard_path || shard_root) sorted  (data/merkle_root.txt)
```

Incremental rebuild: a single shard change → recompute that shard's leaves
+ root, then top-level = O(num_shards). At v1.0 scale (≈ 20 shards) this is
≪ 100 ms.

## MCP server tools (v0.3)

Existing 5 (kept):
- `iut_protocol`, `iut_entity`, `iut_claims_about`, `iut_evidence`, `iut_timeline`

New 5+ (added):
- `iut_summary` — returns `_summary.json` (cold-start context)
- `iut_entities_by_section(section)` — narrow context window
- `iut_entities_by_paper(paper_iri)` — narrow context window
- `iut_entities_by_type(type)` — narrow context window
- `iut_dependency_closure(iri)` — transitive `depends_on` for one IRI
- `iut_verify_verbatim(iri)` — recompute SHA-256 of stored
  `verbatim_short_statement`; cross-check against cache when available

## CI architecture

Two jobs:
- **`validate`** (Python only, < 30 s) — schema, cross-refs, Merkle, tests
- **`lean-build`** (Lean 4 + mathlib4 v4.10.0, 5–10 min, parallel) — `lake build`; allowed to fail until LANA-driven content lands; warning-only

A future job `cold-start-multi-vendor` (gated on user-provided API keys)
runs the L1 fixture against 3–7 LLM vendors and posts the matrix to
`docs/cold_start_evidence.md` via PR.

## Innovation explorer (continuous guard)

`.github/workflows/innovation_scan.yml` (CRON `0 9 * * *`):
1. checkout
2. arXiv API search keywords: `"inter-universal Teichmüller"`, `"Mochizuki abc"`, `"Cor 3.12"`, `"anabelian"`
3. RIMS preprint server `Last-Modified` poll for `~motizuki/*.pdf`
4. diff against `data/evidence.json` URLs
5. on hit: append to `docs/INNOVATION_LOG.md` and open auto-PR
6. on miss: no-op

Cost: free GitHub Actions tier; ≤ 60 minutes / month.

## v0.2.3 / v0.2.4 stress-test refinements (with priority bands)

The round-2 / round-3 architecture stress-tests (2026-05-06) flagged the
following items. Round-3 reclassified them into **must / should / could**
bands; only the `must` band blocks v0.3 work.

| # | Item | Band | Reason |
|---|---|---|---|
| 1 | Backward-compat contract (v0.2 schemas frozen, loader tolerant) | **must** | Without this, any v0.3 schema change silently breaks v0.2 readers. |
| 2 | JP CL Art. 32 verbatim caps (≤ 200 chars/record, ≤ 30 KB cumulative) | **must** | Legal posture; non-negotiable. |
| 3 | shard_id (UUID-like) invariant for Merkle reproducibility | **should** | Helpful for v0.5 + when sharding becomes nontrivial; premature at v0.3 entity = single file. Defer. |
| 4 | Multi-vendor CI (weekly 3-vendor) + monthly 7-vendor | **should** | L1 evidence; can land as a v0.3.x patch. |
| 5 | Innovation explorer regex / heartbeat / delta gating | **should** | Operational, not blocking. |
| 6 | `archive_url` mandatory on Paper / Blog evidence | **could** | Useful for H3 mitigation; can be added per-record as Wayback snapshots are taken. Not gating. |

### 1. Backward-compat contract (frozen)

- v0.2 schemas under `schemas/v0.2/` are **frozen**; no edits.
- v0.3 schemas under `schemas/v0.3/` add fields with explicit
  `dependentRequired` (Draft 2020-12): `verbatim_short_statement` →
  requires `verbatim_sha256`.
- The loader (`loaders/python_minimal.py`) is **tolerant** — it reads
  v0.2 records by ignoring v0.3-only fields and reads v0.3 records by
  treating new fields as optional with `record.get(field)`. v0.2 *schema*
  validation will fail-fast on a v0.3 record by design; this is intentional
  to prevent silent downgrade.

### 2. JP Copyright Act Article 32 主従比 (mandatory)

- Per-record `verbatim_short_statement` is **≤ 200 characters** (revised
  upward at round-3 stress-test from 100 to admit the PDF-verified
  108-character SS p.6 quotation that was already in the graph).
- Cumulative `verbatim_short_statement` total across `data/` is **≤ 30 KB**.
- `tools/validate.py` enforces both bounds with hard exit codes.
- The 主 (main) text of `docs/section_*/<n><letter>_*.md` must exceed
  the corresponding section's verbatim total by **5 ×** before that
  section's verbatim records may be added.

### 3. Merkle historical reproducibility (shard_id invariant)

- Every shard has a stable `shard_id` (UUID-like) that is independent of
  its `path`. Renaming a shard does not break historical Merkle
  verification.
- `tools/verify_merkle.py` auto-detects v0.2 (4-file flat) vs v0.3+
  (sharded with `shard_id`) layouts and uses the matching algorithm.
- `tests/test_merkle_history.py` (added before v0.3) asserts that the
  v0.2 root `8dbc6334…` (then `348662ce…` after the v0.1.1 audit) is
  recomputable from v0.3-era code given the v0.2 layout.

### 4. Multi-vendor CI cadence

- Daily multi-vendor cold-start is **descoped to weekly with 3 vendors**
  (Claude / Gemini / GPT) on cost grounds (≈ $3-5 / month).
- 7-vendor full matrix is run **monthly** as a separate job.
- API keys are stored as GitHub Actions secrets; rotation is reminded
  via a 6-monthly auto-issue, not enforced automatically.

### 5. Innovation explorer robustness

- arXiv keyword set widened to include the regex
  `[Cc]or(ollary)?\s*\.?\s*3\.?12` plus "IUTT", "IUT-T", "universal
  Teichmüller", "ABC conjecture proof".
- Watchlist extends beyond RIMS / arXiv: Yamashita Twitter, Hoshi page,
  any co-author personal page registered as a `Person` entity.
- `.github/workflows/innovation_heartbeat.yml` opens a monthly issue
  even when no hits are found, so silent death of the cron is detectable.
- PR cadence is **gated by a delta threshold**: only if the new
  evidence introduces at least one claim graph difference (new IRI, new
  edge, new locator) does the explorer open a PR. Pure noise is silently
  filtered.

### 6. Schema v0.3 evidence record gains `archive_url`

- Every `Paper` / `Blog` evidence record gains `archive_url` (Wayback
  Machine snapshot URL) as **required** at v0.3 schema.
- `tools/archive_evidence.py` is the canonical helper that submits the
  URL to the Wayback Machine and stores the snapshot URL.

## Migration plan (v0.2.x → v0.3)

1. `tools/migrate_v0_2_to_v0_3.py` reads v0.2 monolithic JSON, writes
   per-type / per-section shards, generates `manifest.json`, computes new
   Merkle root.
2. `schemas/v0.2/` is preserved; `schemas/v0.3/` is added.
3. Loader becomes shard-aware in the same commit.
4. Tests are adapted; existing 26 unit tests must continue to pass.
5. Tagged as `v0.3.0`. Subsequent commits add new entities / claims at the
   target rate (cap at 80 entities / 40 claims for the v0.3 milestone).
