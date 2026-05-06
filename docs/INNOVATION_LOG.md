# Innovation Log — revolutionary-candidate exploration

> Continuous record of revolutionary / 0→1 / Linux-like candidates
> surveyed for `iut-status-2026`, with rationale, status, and external
> references. Updated by the standing innovation-explorer agent.

This log is append-mostly. Status transitions (`Surveyed →
Implemented` / `Surveyed → Deferred` / `Surveyed → Rejected`) are
recorded with date and commit SHA where relevant.

---

## Candidate Catalogue

### A. CRDT-ised claim graph (Yjs / Automerge / m-ld)
- **Idea**: Multi-author concurrent editing of `claims.json` with
  conflict-free merge; PR review becomes "graph diff with semantic
  merge".
- **Status**: Deferred (over-engineering at 16-claim scale).
- **References**: m-ld JSON-LD CRDT https://m-ld.org/ ; Yjs https://yjs.dev/ ; Automerge https://automerge.org/
- **Reconsider when**: claims > 200 OR multiple maintainers.

### B. Merkle-rooted provenance chain (SHA-256 over canonical JSON)
- **Idea**: Cryptographic hash of every record; deterministic
  tamper-detection independent of git history.
- **Status**: **Implemented** (v0.1.2, commit `04b3fc4`).
- **Files**: `tools/build_merkle.py`, `tools/verify_merkle.py`, `data/merkle_root.txt`, `tests/test_merkle.py`.
- **Current root**: see `data/merkle_root.txt` (canonical source). Update this entry only as a history marker; never let the two diverge.
- **Audit fix 2026-05-06**: A v0.1.2 root (`ff8cdef6...8691b34`) was inadvertently embedded in this log; the v0.2.1 audit caught the divergence and replaced this line with a pointer to `data/merkle_root.txt`. Rationale: `data/` is the source of truth for graph state; this log is advisory and must reference the canonical root by file path, not by literal value.

### C. Verifiable LLM response (signed-IRI manifest)
- **Idea**: LLM appends `{touched_iris: [...], graph_root: <hash>}` to
  every IUT-related answer; readers can verify with
  `tools/verify_response.py` whether the IRIs cited actually exist
  and whether the cited graph root matches.
- **Status**: Surveyed; defer to v0.2.
- **Sketch**: ~150 LOC; new MCP tool `iut_verify_response(text)`;
  uses Merkle root from B as anchor.
- **Why deferred**: 5-block protocol already enforces decline-gracefully;
  adding signature validation pipes onto a not-yet-broken layer. Wait
  for first observed drift incident.

### D. Embedding-space drift sensor (vector-level)
- **Status**: Rejected. Vendor-specific embedding spaces; not
  reproducible across LLMs; introduces vendor lock-in.

### E. Auto-formalization bridge (NL claim → Lean stub)
- **Status**: Rejected. Duplicates LANA's effort; risk of injecting
  hallucinated formalizations into the repo.

### F. dispute-graph-core library extraction
- **Idea**: Move `schemas/`, `loaders/python_minimal.py`,
  `mcp/server.py`, `LLM_CONTEXT.md` §3 protocol to a separate
  `Apache-2.0` Python package; IUT becomes a thin `data/` consumer.
- **Status**: Surveyed; defer to v0.5.
- **Why deferred**: Premature; need >=2 forks demanding it. Document
  the generic invariants in-repo (`LLM_CONTEXT.md` §8, README "Generic
  reusability") to make extraction trivial when triggered.
- **Future scenarios**: see Section "Linux-like fork scenarios" below.

### G. Time-locked predictions (cryptographic seal)
- **Status**: Rejected. Gimmick; predictions are already in the graph
  with `verified_at` dates.

### H. Multi-LLM consensus log (disagreement-as-evidence)
- **Status**: Surveyed; supplanted by candidate **N** (Counterfactual
  Drift Probe), which adds longitudinal time-series and is more
  rigorous.

### I. WASM Lean-light verifier
- **Status**: Rejected. LANA owns this layer; collision risk.

### J. Differential PDF watcher (kurims update detection)
- **Status**: Surveyed; defer.
- **Sketch**: GitHub Action CRON, `curl -I` Last-Modified header check
  on RIMS PDFs; surface new commits as evidence-add candidates.
- **~50 LOC**, low risk.

### K. Provenance-bound RAG citation enforcement
- **Status**: Subsumed by candidate **C** (Verifiable LLM response).

### L. Cryptographic citation proof ("I read this URL at this time")
- **Status**: Rejected. RFC 3161 timestamping is overkill; URL
  immutability is the actual problem (Wayback Machine fork is the
  honest fix).

### M. Drift cookies (canary phrases per claim)
- **Status**: Rejected. Adversarial vs LLMs; encourages prompt
  injection style mitigations.

### N. Counterfactual Drift Probe (CDP) — longitudinal multi-vendor diff
- **Idea**: GitHub Action CRON that asks 7 LLM vendors a fixed prompt
  set, extracts touched IRIs from each answer, computes Jaccard
  distance pair-wise, persists time-series in SQLite.
- **Status**: Surveyed; recommended for v0.1.3 but deferred until
  vendor-API budget approved (each cron tick costs $0.10-$0.30 across
  7 vendors).
- **Sketch**: ~280 LOC; `tools/drift_probe.py` + `tools/drift_score.py`
  + `.github/workflows/drift_probe.yml` + 5-prompt fixed set.
- **Output**: README badge `drift: 0.03` ; `reports/drift_*.md`.
- **Why deferred (not rejected)**: The Adversarial Drift Bounty (P)
  achieves similar evidence collection with zero recurring cost.
  Reconsider once OSS hosting budget covers cron API fees.

### O. Anti-Hallucination Evidence Hook (AHEH) — MCP trigger extension
- **Status**: Surveyed; depends on MCP 2026 spec extensions
  (currently "horizon" per the 2026 roadmap).
- **References**: MCP 2026 roadmap https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- **Reconsider when**: MCP triggers/event-driven becomes stable.

### P. Adversarial Drift Bounty (community-sourced drift evidence)
- **Idea**: Public challenge — submit a `(prompt, vendor, response)`
  tuple where the response violates the 5-block protocol. CI
  re-runs the prompt n=10 times against the named vendor; if the
  violation reproduces ≥3/10, the tuple lands in `drift-bounty/` as
  evidence and the responsible vendor + version is logged.
- **Status**: Surveyed; defer until first organic submission arrives
  via Issue tracker.
- **Why this matters**: builds an open dataset of LLM drift on a
  factually-grounded controversy; useful for academic LLM evaluation
  research.

### R. URL liveness verifier (`tools/verify_urls.py`)
- **Idea**: Bridge the round-4-5-6 systemic gap where `validate.py` only checks internal graph consistency; never compares graph URLs to external reality. Three fabrication-class defects (Joshi v2, Woit dating, IRI drift) survived four audit rounds before this gap was diagnosed.
- **Status**: **Implemented** (v0.6, commit pending).
- **Files**: `tools/verify_urls.py`, `tests/test_verify_urls.py`.
- **Mode**: offline (default, syntax check only) + `--network` flag (opt-in HTTP HEAD/GET, suitable for scheduled CI).
- **Limitation acknowledged**: catches URL-resolves-to-200 only; the Woit Round-6 case was a content-vs-metadata mismatch (URL alive but date/topic wrong). Manual content review still required.
- **Future**: Wayback Machine fallback when primary URL fails; PDF SHA-256 + content-pattern check.

### S. Wayback Machine archival bootstrap (`tools/archive_evidence.py`)
- **Idea**: Round 4-7 audits found four fabrication-class defects (Joshi v2 fictional, Woit blog dating drift, Kato ISBN fabrication, PRIMS issue ID drift) whose common root cause is **external reality drift**: the cited material itself moves, mutates, or vanishes. R (`verify_urls.py`) detects URL-no-longer-resolves; this candidate captures the snapshot at-cite-time so a Round-N+1 audit can compare the live URL against what the graph originally cited.
- **Status**: **Implemented** (v0.7.0, commit pending).
- **Files**: `tools/archive_evidence.py`, `tests/test_archive_evidence.py`, `schemas/evidence.json` + `schemas/timeline.json` (`archive_url` optional field), `loaders/python_minimal.py` (Evidence + TimelineEvent dataclasses extended).
- **Modes**: offline (collect-and-classify, no network) / `--network --lookup` (Availability API, read-only) / `--network --submit` (Save Page Now, anonymous, rate-limited 12 s/req). `--apply` writes back to `data/*.json`.
- **Drift-zero contract**: the tool never synthesises a `web.archive.org/web/<timestamp>` value. Every populated `archive_url` is taken verbatim from API response or redirect Location header. Synthesising a snapshot URL without API confirmation would itself be a fabrication-class defect of the type Round-7 closed.
- **Limitations**: SPN anonymous quota fluctuates (~10 req / min / IP); paywalled hosts and `robots.txt`-excluded URLs are not archivable; ISBNs are not URLs (separate v0.7.x DOI/ISBN extension planned).
- **Why it complements R**: R detects "URL is alive vs dead" *now*; S preserves "what URL was *meant to point to* at cite time", enabling content-vs-metadata mismatch detection (Round-6 Woit class) once a follow-up audit fetches both live URL and `archive_url` and diffs them.

### T. DOI / ISBN identifier verifier (`tools/verify_identifiers.py`)
- **Idea**: Round 7 (v0.6.1) closed a Kato-book ISBN fabrication that `verify_urls.py` cannot detect because URL liveness has nothing to say about identifier-registry integrity. This candidate adds a structural layer: ISO 2108 ISBN-10 / ISBN-13 checksum + ANSI/NISO Z39.84-2010 DOI pattern, plus opt-in network resolution via doi.org and Open Library.
- **Status**: **Implemented** (v0.7.1, commit pending).
- **Files**: `tools/verify_identifiers.py`, `tests/test_verify_identifiers.py`.
- **Modes**: offline (default; structural checksum + pattern; CI-safe) / `--check-doi` (HEAD doi.org; alive=2xx/3xx, invalid=4xx/5xx) / `--check-isbn` (Open Library API; 404=unresolved, not invalid, since JP coverage is partial).
- **Happy finding**: the Round-7 fabricated ISBN `978-4-04-110262-7` actually **fails** the ISBN-13 checksum (sum 91 mod 10 = 1 ≠ 0). Cross-source verification was the gold standard for Round 7, but this tool would have caught it structurally; pinned by `test_isbn13_round7_fabricated_fails_checksum` so the regression cannot recur silently.
- **Limitation**: Open Library Japanese-language coverage is partial — a 404 is mapped to `unresolved` rather than `invalid` to avoid CI failures on legitimately-rare titles. Future v0.7.x may add NDL Search API for stronger JP coverage.

### U. Person edge-or-role invariant (`role` field + `validate.py` rule)
- **Idea**: v0.7 architect audit flagged Pop / Sawin as "0-edge" Person entities (no claim proponent, no introduced_by edge). Naïvely "fixing" by adding fabricated proponent edges would be a Round-7-class defect (Sawin's locality critique URL is explicitly flagged unverified in `claim:joshi_ss_all_claims_false`). Better: make the orphan-status data-driven via a `role` field documenting *why* the disconnection is intentional, and let validate.py reject future un-tagged orphans.
- **Status**: **Implemented** (v0.7.2, commit pending).
- **Files**: `schemas/entity.json` (`role` enum optional), `data/entities.json` (Grothendieck=historical_foundation, Pop=background_reference, Sawin=background_reference), `tools/validate.py` (Person-edge-or-role-required rule), `loaders/python_minimal.py` (Entity.role field).
- **Architect false-positive recorded**: the same audit listed `IUTchIII Def 1.4` as missing, but the entity exists under the descriptive IRI `iut:log_theta_lattice` (label-search miss; IRI-search would have found it). Future audits should scan IUTch reference-strings inside `informal_md` paths and `definedIn` chains, not only entity labels, before declaring missing.

### V. Innovation log monthly heartbeat (`.github/workflows/innovation_heartbeat.yml`)
- **Idea**: This log is a document, not a process. Without a heartbeat the silent-death class (explorer "is silent" indistinguishable from "found nothing") cannot be detected from outside the workflow. Closes Phase 1 must-band #5 by ensuring a single observable signal — a monthly auto-opened issue — fires whether or not new candidates are discovered.
- **Status**: **Implemented** (v0.7.3, commit pending).
- **Files**: `.github/workflows/innovation_heartbeat.yml` (cron 02:30 UTC on the 1st of every month + manual workflow_dispatch; permissions issues:write contents:read; idempotent label-creation guard; duplicate-issue guard via gh issue list filter).
- **Body**: lists the count of `Surveyed` candidates auto-detected via grep over the file, and the standing 90-day stalled-candidate review rule.
- **Why a heartbeat is enough**: silent failure is now loud (issue does not appear → workflow died → fix it). No analysis logic is needed for the silent-death class; that is a separate candidate (regex-driven candidate scanning over arXiv / RIMS / ems.press / openalex) which v0.7.x may add.

### W. Multi-vendor cold-start CI (`tests/cold_start/` + `cold_start_weekly.yml`)
- **Idea**: The L1 contract in `docs/UNDERSTANDING_LEVELS.md` is "a fresh LLM session, given only `LLM_CONTEXT.md` + sample data, answers via the 5-block protocol". Until that runs against real vendors the "L1 ~30 % (Claude-only)" Roadmap figure is self-graded, not evidence. v0.7.4 lands the runner + workflow with Claude implemented; other vendors are stubs.
- **Status**: **Implemented (Claude only)** (v0.7.4, commit pending). Other vendors planned v0.7.x.
- **Files**: `tests/cold_start/README.md` + `prompt.txt` + `expected_5_block_structure.md` + `run_cold_start.py` (stdlib-only Anthropic Messages API client; deterministic excerpt selection over `entities.json` / `claims.json` / `evidence.json` / `timeline.json`); `tests/test_cold_start_runner.py` (5 cases, no network); `.github/workflows/cold_start_weekly.yml` (Sunday 03:00 UTC, secret-gated, allow-fail, auto-commits result row); `docs/cold_start_evidence.md` table header + run log appended by runner.
- **Drift-zero contract**: excerpt is a deterministic subset (6 seed entities, all `about: iut:Cor.3.12` claims, transitive evidence, 2018–2026 timeline window). No git history, branch state, or unrelated docs leak into the prompt.
- **Advisory only**: structural failures exit 0 with `fail` row; transport / API errors exit 1 but workflow uses `continue-on-error: true`. The maintainer review of the row is the gate, not the workflow exit code.

### X. Lean stub per-section split (`lean/IutStatus/<Module>.lean` × 16)
- **Idea**: 17 entities in `data/entities.json` carry a `lean_module` field pointing at `IutStatus.Anabelian` / `Frobenioid` / `EtaleTheta` / etc., yet `lean/IutStatus/Basic.lean` was the only file. Validate.py never enforced the existence of those module files — a Round-7-class drift between graph metadata and on-disk reality. Closes Phase 1 must-band #2 by splitting Basic.lean into 16 per-section files (one per unique `lean_module` value), turning Basic.lean into a pure orchestrator that imports every module, and adding a validator rule that fails CI if any `lean_module` reference does not resolve to a file.
- **Status**: **Implemented** (v0.7.5, commit pending).
- **Files**: 16 new `lean/IutStatus/<Module>.lean` files (Anabelian / AbsoluteAnabelian / MonoAnabelian / Frobenioid / EtaleTheta / MonoTheta / TemperedRigidity / Cuspidalization / HodgeTheater / ThetaLink / LogLink / Multiradial / Cor312 / HeightInequality / Diophantine / ABC); rewritten `lean/IutStatus/Basic.lean` (orchestrator with explicit imports); `tools/validate.py` (lean_module resolution rule); `tests/test_validation.py` LeanModuleTests (2 cases: every-module-resolves + Basic-imports-every-module).
- **Drift-zero contract preserved**: every identifier in every per-section file maps 1:1 to an `iut:*` IRI in entities.json. Module dependencies are encoded via `import` statements following the mathematical hierarchy (Anabelian → AbsoluteAnabelian → MonoAnabelian; Frobenioid → EtaleTheta → MonoTheta + TemperedRigidity + Cuspidalization; HodgeTheater → ThetaLink + LogLink → Multiradial → Cor312 → HeightInequality → Diophantine + ABC).
- **MonoTheta exception**: the `iut:mono_theta_environment` entity carries `lean_module=IutStatus.MonoTheta` but no `lean_stub`. The new module file ships a minimal `axiom mono_theta_environment : Prop` so the file exists and Basic.lean imports cleanly; the data record itself is not modified.

### Y. Round 8 user-override audit (multi-class fixes + 2 regression tests)
- **Idea**: Round 8 was launched by the standing user-override phrase after Round 7 analyst recommended skipping. The audit found one class of defect the prior 7 rounds missed — *prose-layer scrub miss after data/ repair* — directly contradicting v0.7.6's "documentation coherence pass" claim. Closes 1 critical + 5 high + 4 medium findings in a single release with two new regression tests.
- **Status**: **Implemented** (v0.7.7, commit pending).
- **Critical**: `docs/section_8_disputes_timeline.md:124` retained the Round-7 fabricated ISBN `978-4-04-110262-7` even though `data/evidence.json` was repaired in v0.6.1; v0.7.6 doc-coherence pass scrubbed counts but missed the scrub of fabricated identifiers. Fix replaces the value + adds `test_round_7_fabricated_isbn_not_in_docs` (allowlist for INNOVATION_LOG.md / AUDIT_PROVENANCE.md which document the fabrication intentionally).
- **JSON-LD context drift**: `data/context.jsonld` was missing mappings for `archive_url` (added v0.7.0) and `role` (added v0.7.2) — JSON-LD processors silently dropped those fields on expansion. Fix adds mappings + `test_every_schema_property_has_context_mapping` regression.
- **Cold-start runner repairs**: placeholder model id `claude-opus-4-5` → real `claude-opus-4-7`; `LLM_CONTEXT.md` moved to Messages API `system` slot (vendor-neutrality + steerability); `collect_known_iris` now reads the full on-disk graph (not just the truncated excerpt) so legitimate IRIs do not register as fabrications; `BLOCK_LABEL_PATTERNS` strengthened with header / qualifier constraints to avoid `joshi`-keyword false positives.
- **Wayback bootstrap repairs**: `closest.url` http→https normalisation; `outcomes.index(o)` replaced with `enumerate` (frozen dataclass `eq=True` could shift the slice on duplicate URLs).
- **Validate.py repairs**: surname-only heuristic dropped (now full-name match required); ISBN separator stripping now handles Unicode dashes (en-dash, em-dash, figure-dash, NBSP) via NFKC normalisation + `unicodedata` Pd category.
- **Doc coherence repairs**: `docs/AUDIT_PROVENANCE.md` round table extended with Rounds 4–8 (was Round 1–3 only despite governance honest revision referencing 4–7); `docs/ARCHITECTURE.md` schemas/v0.{2,3}/ subdir target marked NOT YET (was 6 places asserting it as current); `docs/UNDERSTANDING_LEVELS.md` L2 % marked self-graded with `scripts/coverage_report.py` not-yet-implemented note; `README.md` lean/ block enumerates 16 per-section files; `innovation_heartbeat.yml` grep primary pattern unified with bullet-prefix form (fallback was carrying the load).

### Q. (open slot for future innovation-explorer findings)

---

## v0.2.2 architecture review (2026-05-06, before any v0.3 work)

A 3-agent design audit (analyst + architect + critic) was run before
attempting the large-scale expansion the user requested ("ものすごく長い").
Outputs are persisted as the three architecture documents below.

| Document | Role |
|---|---|
| `docs/UNDERSTANDING_LEVELS.md` | Operational definition of "100 % understanding" as L1 / L2 / L3 with measurable success criteria and a multi-version roadmap. |
| `docs/ARCHITECTURE.md` | Sharding strategy, schema v0.3, cross-reference indexes, sub-section docs layout, PDF cache policy, MCP tool extension, Merkle architecture, CI design. |
| `docs/FAILURE_MODES.md` | Top-5 failure modes with probability / impact / mitigation, plus the recorded devil's-advocate "freeze at v0.2" alternative. |

The three documents are co-equal and must be read together by anyone
attempting v0.3 work.

Decision (round 1): phased expansion (v0.3 → v0.5 → v1.0) with
verbatim-SHA256 enforcement, multi-vendor CI, and PDF cache as
host-local-only.

## v0.2.3 architecture stress-test (round 2, 2026-05-06)

A second-round 3-agent stress-test of the round-1 documents identified
substantive gaps. The three documents were updated in the same commit:

- **UNDERSTANDING_LEVELS.md** gained an interim Level 1.5
  (Formally-Verified Navigation, post-LANA), seven L1 specification
  refinements (prose quality bound, 5-block content floor, symmetry
  secondary axis, coverage denominator freeze, L3 reclassification
  protocol, consumer-class L1 spec, L1.5 forward-compatibility), and
  three explicit warnings against common misreadings.
- **ARCHITECTURE.md** revised three round-1 decisions: `entities/` is
  a single file at v0.3 scale (per-type sharding deferred to v1.0+);
  cross-reference indexes are computed on-the-fly (no `_indexes/`
  directory at v0.3); `verbatim_short_statement` is constrained to
  ≤ 100 chars per record and ≤ 25 KB cumulative across `data/` to
  satisfy the JP Copyright Act Article 32 主従比 1:5 requirement.
  Six v0.2.3 refinements (backward-compat contract, JP CL Art. 32,
  shard_id invariant, multi-vendor cadence, explorer robustness,
  archive_url mandatory) are mandated before any v0.3 expansion.
- **FAILURE_MODES.md** gained five hidden modes (H1 Wikipedia
  WP:RS war, H2 LANA overnight obsolescence, H3 RIMS link-rot
  synchronous failure, H4 explorer triage fatigue silent death,
  H5 dual-side false-balance accusation), an acceptance-only modes
  list, repository sustainability horizons (3 mo / 12 mo / 5 y), and
  a re-evaluated devil's-advocate `v0.2.5 hybrid` proposal recorded
  as an available alternative path.

These updates are normative; the architecture is now considered frozen
at the document layer for the duration of v0.3 work. Any subsequent
revision opens a new round-3 stress-test entry.

## v0.2.4 stress-test (round 3, 2026-05-06)

A third-round 3-agent stress-test (architect + analyst + critic) was
run to assess whether v0.3 implementation is ready and whether the
documentation has over-specified itself.

Round 3 found:

- The Round-2 hour estimate of 25-40 h for v0.3 was 2-3x too low; the
  honest range is 63-113 h. v0.3 will not finish before the LANA
  mid-report (2026-07-17), so part of v0.3 expansion may be partially
  sunk-cost; the schema's `superseded_by_lana_2026_07` field exists to
  recover from this.
- The verbatim length cap was internally inconsistent (100 / 200 / 200
  characters across the three architecture documents). Unified to
  ≤ 200 chars per record / ≤ 30 KB cumulative, which admits the
  PDF-verified 108-character SS p.6 quotation already in the graph.
- The v0.2.3 mandatory pre-v0.3 refinements (six items) were
  reclassified into must / should / could bands. Only two are
  blocking: backward-compat contract and JP CL Art. 32 caps. The
  remaining four are deferred to v0.3.x patches.
- A glossary section was added to UNDERSTANDING_LEVELS.md to prevent
  the "drift-zero / drift-resistant / 100% understanding / L1-100"
  terminology drift identified by analyst.
- A new `docs/AUDIT_PROVENANCE.md` was created to honestly record that
  all three audit rounds were produced inside a single Claude family
  session, with **no LLM-vendor independence**. The
  `docs/cold_start_evidence.md` (when populated) is the only legitimate
  source of multi-vendor independence claims, not these audit
  documents.
- Future audit rounds are **paused indefinitely** until at least one
  of: (a) an actual non-Claude vendor cold-start run, (b) an external
  (non-Anthropic-family) reviewer report, (c) a v0.3 schema-changing
  PR merged. Re-opening requires a public Issue documenting which
  condition fired.

The architecture is now considered frozen at the document layer with
priority-banded refinements. v0.3 implementation can begin against the
two `must` items.

---

## v0.2.1 audit-driven hardening (2026-05-06)

A 3-agent re-audit at v0.2.0 surfaced that the repository itself drifted
in two ways. Both are now closed.

| Drift | Where | Resolution |
|---|---|---|
| Merkle root literal embedded in this log diverged from `data/merkle_root.txt` after the v0.1.1 audit fixes | `docs/INNOVATION_LOG.md` candidate B | Replaced with a pointer to `data/merkle_root.txt`; no literal in this log |
| `CLAUDE.md` instructed "4-block answer template" while every other doc enforces 5-block | `CLAUDE.md` | Updated to "5-block answer template" with the canonical block names |
| "100% understanding" / "guarantee" wording in `LLM_CONTEXT.md` and `README.md` overstated what an LLM-readable spec can deliver | both | Downgraded to "best-effort cold-start contract"; level-by-level guarantee table preserved |
| `lakefile.lean` required mathlib4 unpinned, breaking reproducibility | `lean/lakefile.lean` | Pinned to `v4.10.0` |
| `schemas/claim.json#about` allowed `.` in claim IRIs while `claim:` self-pattern did not | `schemas/claim.json` | Pattern split: `iut:` allows `.`, `claim:` does not |
| `data/context.jsonld` missing `@context` mappings for `isbn` / `publisher` / `peer_review_status` / `relates_to` | `data/context.jsonld` | Four mappings added (schema.org + iut: namespaces) |
| `mcp/server.py` raised `KeyError` on missing arguments instead of returning a JSON-RPC error response | `mcp/server.py` | Wrapped tool dispatch in try/except → `_make_error -32602/-32603` |
| `multiradial_ss_view.md` cited footnote 12 as "p.10" while the PDF (verified 2026-05-06) has it on p.9 | `docs/concepts/multiradial_ss_view.md` | Corrected to "p.9 fn.12 (PDF-verified 2026-05-06)" |
| `claim:scholze_stix_2018_sub_1` verbatim diverged from the SS PDF | `data/claims.json` | Replaced with the PDF-verified literal: "up to equivalence of categories, choosing a Hodge theater is equivalent to choosing a once-punctured elliptic curve abstractly isomorphic to X" |
| `claim:scholze_stix_2018_sub_3` verbatim diverged | `data/claims.json` | Replaced with PDF-verified: "the critical [IUTT-3, Theorem 3.11] does not become false, but trivial" |
| `claim:joshi_2025_alternative.status` field had implementation TODOs (URL not verified) | `data/claims.json` | Moved TODO to `fair_use_note`, `status` is now a clean state value |

This entry is itself an example of the standing innovation-explorer
agent's contract: discoveries that the repository has drifted from its
own invariants are surfaced, recorded with file-line evidence, and
closed by a small fix rather than a redesign.

---

## External findings (continuously updated)

| Date | Finding | URL |
|---|---|---|
| 2026-05-06 | MCP 2026 roadmap: SEP triggers/event-driven on horizon | https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/ |
| 2026-05-06 | MCP Authorization Extensions live (OAuth Client Credentials, Enterprise-Managed Auth) | https://blog.modelcontextprotocol.io/posts/2026-03-11-understanding-mcp-extensions/ |
| 2026-05-06 | LANA project mid-report 2026-07-17 confirmed; team currently states "unresolved gap or understanding limit, undecided" | https://zen.ac.jp/news/zmcpostevent0331e |
| 2026-05-06 | Citation faithfulness study: up to 57% of LLM citations are post-rationalised; line-range enforcement + interval-arithmetic verification effective | https://arxiv.org/pdf/2412.18004 |
| 2026-05-06 | Guardrails AI ProvenanceLLM: OSS reference for citation provenance enforcement | https://github.com/guardrails-ai/provenance_llm |
| 2026-05-06 | m-ld: JSON-LD-native CRDT (decentralised replica + query API), distinct from Yjs/Automerge | https://m-ld.org/ |

---

## Linux-like fork scenarios (where the framework transfers)

The combination of `schemas/*.json` + `LLM_CONTEXT.md` 5-block
protocol + `mcp/server.py` + `tools/build_merkle.py` is
**dispute-domain agnostic**. The IUT case is one instance.

| Domain | Fork name (suggested) | Core controversies preserved |
|---|---|---|
| COVID-origin | `covid-origin-status-2026` | Lab-leak vs zoonotic; WHO/Lancet positions |
| Climate attribution | `climate-attribution-disputes` | IPCC mainstream vs Lindzen/Curry |
| P vs NP attempts | `p-vs-np-status` | Razborov-Rudich; GCT; Deolalikar 2010 |
| Vaccine efficacy by variant | `vaccine-efficacy-by-variant` | Phase III vs real-world; per-country regulatory positions |
| Legal precedent graph | `legal-precedent-graph` | Roe→Dobbs; landmark reversals |
| Security CVE disputes | `security-CVE-dispute-graph` | Severity discord between MITRE / vendor / researcher |
| Mass-loss in cosmology | `cosmology-tension-graph` | Hubble tension; sigma-8 tension |
| Origins of life | `origins-of-life-status` | RNA-world vs metabolism-first vs PAH-world |

The fork checklist (in repo: `LLM_CONTEXT.md` §8):
1. Rename IRI namespace (`iut:` → `domain:`)
2. Replace `data/entities.json` and `data/claims.json` content
3. Keep schema, protocol, MCP server, Merkle tooling unchanged
4. Update README scope to the new domain
5. Re-run `tools/build_merkle.py` for the new graph

---

## Update protocol

- The standing innovation-explorer agent updates this log on each
  pass: new candidates → new sections; status transitions →
  inline-edited; external findings → table append.
- Implementations refer back here from their commit messages.
- Rejection rationale must be preserved (no silent deletion).
- This log is itself drift-resistant: under the Merkle root for
  `data/` only — `docs/INNOVATION_LOG.md` is *advisory*, not source
  of truth.
