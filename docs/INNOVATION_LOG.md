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
- **Status**: **Implemented** (v0.6, commit `1df6818`).
- **Files**: `tools/verify_urls.py`, `tests/test_verify_urls.py`.
- **Mode**: offline (default, syntax check only) + `--network` flag (opt-in HTTP HEAD/GET, suitable for scheduled CI).
- **Limitation acknowledged**: catches URL-resolves-to-200 only; the Woit Round-6 case was a content-vs-metadata mismatch (URL alive but date/topic wrong). Manual content review still required.
- **Future**: Wayback Machine fallback when primary URL fails; PDF SHA-256 + content-pattern check.

### S. Wayback Machine archival bootstrap (`tools/archive_evidence.py`)
- **Idea**: Round 4-7 audits found four fabrication-class defects (Joshi v2 fictional, Woit blog dating drift, Kato ISBN fabrication, PRIMS issue ID drift) whose common root cause is **external reality drift**: the cited material itself moves, mutates, or vanishes. R (`verify_urls.py`) detects URL-no-longer-resolves; this candidate captures the snapshot at-cite-time so a Round-N+1 audit can compare the live URL against what the graph originally cited.
- **Status**: **Implemented** (v0.7.0, commit `c3b9827`).
- **Files**: `tools/archive_evidence.py`, `tests/test_archive_evidence.py`, `schemas/evidence.json` + `schemas/timeline.json` (`archive_url` optional field), `loaders/python_minimal.py` (Evidence + TimelineEvent dataclasses extended).
- **Modes**: offline (collect-and-classify, no network) / `--network --lookup` (Availability API, read-only) / `--network --submit` (Save Page Now, anonymous, rate-limited 12 s/req). `--apply` writes back to `data/*.json`.
- **Drift-zero contract**: the tool never synthesises a `web.archive.org/web/<timestamp>` value. Every populated `archive_url` is taken verbatim from API response or redirect Location header. Synthesising a snapshot URL without API confirmation would itself be a fabrication-class defect of the type Round-7 closed.
- **Limitations**: SPN anonymous quota fluctuates (~10 req / min / IP); paywalled hosts and `robots.txt`-excluded URLs are not archivable; ISBNs are not URLs (separate v0.7.x DOI/ISBN extension planned).
- **Why it complements R**: R detects "URL is alive vs dead" *now*; S preserves "what URL was *meant to point to* at cite time", enabling content-vs-metadata mismatch detection (Round-6 Woit class) once a follow-up audit fetches both live URL and `archive_url` and diffs them.

### T. DOI / ISBN identifier verifier (`tools/verify_identifiers.py`)
- **Idea**: Round 7 (v0.6.1) closed a Kato-book ISBN fabrication that `verify_urls.py` cannot detect because URL liveness has nothing to say about identifier-registry integrity. This candidate adds a structural layer: ISO 2108 ISBN-10 / ISBN-13 checksum + ANSI/NISO Z39.84-2010 DOI pattern, plus opt-in network resolution via doi.org and Open Library.
- **Status**: **Implemented** (v0.7.1, commit `2728261`).
- **Files**: `tools/verify_identifiers.py`, `tests/test_verify_identifiers.py`.
- **Modes**: offline (default; structural checksum + pattern; CI-safe) / `--check-doi` (HEAD doi.org; alive=2xx/3xx, invalid=4xx/5xx) / `--check-isbn` (Open Library API; 404=unresolved, not invalid, since JP coverage is partial).
- **Happy finding**: the Round-7 fabricated ISBN `978-4-04-110262-7` actually **fails** the ISBN-13 checksum (sum 91 mod 10 = 1 ≠ 0). Cross-source verification was the gold standard for Round 7, but this tool would have caught it structurally; pinned by `test_isbn13_round7_fabricated_fails_checksum` so the regression cannot recur silently.
- **Limitation**: Open Library Japanese-language coverage is partial — a 404 is mapped to `unresolved` rather than `invalid` to avoid CI failures on legitimately-rare titles. Future v0.7.x may add NDL Search API for stronger JP coverage.

### U. Person edge-or-role invariant (`role` field + `validate.py` rule)
- **Idea**: v0.7 architect audit flagged Pop / Sawin as "0-edge" Person entities (no claim proponent, no introduced_by edge). Naïvely "fixing" by adding fabricated proponent edges would be a Round-7-class defect (Sawin's locality critique URL is explicitly flagged unverified in `claim:joshi_ss_all_claims_false`). Better: make the orphan-status data-driven via a `role` field documenting *why* the disconnection is intentional, and let validate.py reject future un-tagged orphans.
- **Status**: **Implemented** (v0.7.2, commit `815b43a`).
- **Files**: `schemas/entity.json` (`role` enum optional), `data/entities.json` (Grothendieck=historical_foundation, Pop=background_reference, Sawin=background_reference), `tools/validate.py` (Person-edge-or-role-required rule), `loaders/python_minimal.py` (Entity.role field).
- **Architect false-positive recorded**: the same audit listed `IUTchIII Def 1.4` as missing, but the entity exists under the descriptive IRI `iut:log_theta_lattice` (label-search miss; IRI-search would have found it). Future audits should scan IUTch reference-strings inside `informal_md` paths and `definedIn` chains, not only entity labels, before declaring missing.

### V. Innovation log monthly heartbeat (`.github/workflows/innovation_heartbeat.yml`)
- **Idea**: This log is a document, not a process. Without a heartbeat the silent-death class (explorer "is silent" indistinguishable from "found nothing") cannot be detected from outside the workflow. Closes Phase 1 must-band #5 by ensuring a single observable signal — a monthly auto-opened issue — fires whether or not new candidates are discovered.
- **Status**: **Implemented** (v0.7.3, commit `71e1508`).
- **Files**: `.github/workflows/innovation_heartbeat.yml` (cron 02:30 UTC on the 1st of every month + manual workflow_dispatch; permissions issues:write contents:read; idempotent label-creation guard; duplicate-issue guard via gh issue list filter).
- **Body**: lists the count of `Surveyed` candidates auto-detected via grep over the file, and the standing 90-day stalled-candidate review rule.
- **Why a heartbeat is enough**: silent failure is now loud (issue does not appear → workflow died → fix it). No analysis logic is needed for the silent-death class; that is a separate candidate (regex-driven candidate scanning over arXiv / RIMS / ems.press / openalex) which v0.7.x may add.

### W. Multi-vendor cold-start CI (`tests/cold_start/` + `cold_start_weekly.yml`)
- **Idea**: The L1 contract in `docs/UNDERSTANDING_LEVELS.md` is "a fresh LLM session, given only `LLM_CONTEXT.md` + sample data, answers via the 5-block protocol". Until that runs against real vendors the "L1 ~30 % (Claude-only)" Roadmap figure is self-graded, not evidence. v0.7.4 lands the runner + workflow with Claude implemented; other vendors are stubs.
- **Status**: **Implemented (Claude only)** (v0.7.4, commit `3bc336f`). Other vendors planned v0.7.x.
- **Files**: `tests/cold_start/README.md` + `prompt.txt` + `expected_5_block_structure.md` + `run_cold_start.py` (stdlib-only Anthropic Messages API client; deterministic excerpt selection over `entities.json` / `claims.json` / `evidence.json` / `timeline.json`); `tests/test_cold_start_runner.py` (5 cases, no network); `.github/workflows/cold_start_weekly.yml` (Sunday 03:00 UTC, secret-gated, allow-fail, auto-commits result row); `docs/cold_start_evidence.md` table header + run log appended by runner.
- **Drift-zero contract**: excerpt is a deterministic subset (6 seed entities, all `about: iut:Cor.3.12` claims, transitive evidence, 2018–2026 timeline window). No git history, branch state, or unrelated docs leak into the prompt.
- **Advisory only**: structural failures exit 0 with `fail` row; transport / API errors exit 1 but workflow uses `continue-on-error: true`. The maintainer review of the row is the gate, not the workflow exit code.

### X. Lean stub per-section split (`lean/IutStatus/<Module>.lean` × 16)
- **Idea**: 17 entities in `data/entities.json` carry a `lean_module` field pointing at `IutStatus.Anabelian` / `Frobenioid` / `EtaleTheta` / etc., yet `lean/IutStatus/Basic.lean` was the only file. Validate.py never enforced the existence of those module files — a Round-7-class drift between graph metadata and on-disk reality. Closes Phase 1 must-band #2 by splitting Basic.lean into 16 per-section files (one per unique `lean_module` value), turning Basic.lean into a pure orchestrator that imports every module, and adding a validator rule that fails CI if any `lean_module` reference does not resolve to a file.
- **Status**: **Implemented** (v0.7.5, commit `fca140e`).
- **Files**: 16 new `lean/IutStatus/<Module>.lean` files (Anabelian / AbsoluteAnabelian / MonoAnabelian / Frobenioid / EtaleTheta / MonoTheta / TemperedRigidity / Cuspidalization / HodgeTheater / ThetaLink / LogLink / Multiradial / Cor312 / HeightInequality / Diophantine / ABC); rewritten `lean/IutStatus/Basic.lean` (orchestrator with explicit imports); `tools/validate.py` (lean_module resolution rule); `tests/test_validation.py` LeanModuleTests (2 cases: every-module-resolves + Basic-imports-every-module).
- **Drift-zero contract preserved**: every identifier in every per-section file maps 1:1 to an `iut:*` IRI in entities.json. Module dependencies are encoded via `import` statements following the mathematical hierarchy (Anabelian → AbsoluteAnabelian → MonoAnabelian; Frobenioid → EtaleTheta → MonoTheta + TemperedRigidity + Cuspidalization; HodgeTheater → ThetaLink + LogLink → Multiradial → Cor312 → HeightInequality → Diophantine + ABC).
- **MonoTheta exception**: the `iut:mono_theta_environment` entity carries `lean_module=IutStatus.MonoTheta` but no `lean_stub`. The new module file ships a minimal `axiom mono_theta_environment : Prop` so the file exists and Basic.lean imports cleanly; the data record itself is not modified.

### Y. Round 8 user-override audit (multi-class fixes + 2 regression tests)
- **Idea**: Round 8 was launched by the standing user-override phrase after Round 7 analyst recommended skipping. The audit found one class of defect the prior 7 rounds missed — *prose-layer scrub miss after data/ repair* — directly contradicting v0.7.6's "documentation coherence pass" claim. Closes 1 critical + 5 high + 4 medium findings in a single release with two new regression tests.
- **Status**: **Implemented** (v0.7.7, commit `b8e15af`).
- **Critical**: `docs/section_8_disputes_timeline.md:124` retained the Round-7 fabricated ISBN `978-4-04-110262-7` even though `data/evidence.json` was repaired in v0.6.1; v0.7.6 doc-coherence pass scrubbed counts but missed the scrub of fabricated identifiers. Fix replaces the value + adds `test_round_7_fabricated_isbn_not_in_docs` (allowlist for INNOVATION_LOG.md / AUDIT_PROVENANCE.md which document the fabrication intentionally).
- **JSON-LD context drift**: `data/context.jsonld` was missing mappings for `archive_url` (added v0.7.0) and `role` (added v0.7.2) — JSON-LD processors silently dropped those fields on expansion. Fix adds mappings + `test_every_schema_property_has_context_mapping` regression.
- **Cold-start runner repairs**: placeholder model id `claude-opus-4-5` → real `claude-opus-4-7`; `LLM_CONTEXT.md` moved to Messages API `system` slot (vendor-neutrality + steerability); `collect_known_iris` now reads the full on-disk graph (not just the truncated excerpt) so legitimate IRIs do not register as fabrications; `BLOCK_LABEL_PATTERNS` strengthened with header / qualifier constraints to avoid `joshi`-keyword false positives.
- **Wayback bootstrap repairs**: `closest.url` http→https normalisation; `outcomes.index(o)` replaced with `enumerate` (frozen dataclass `eq=True` could shift the slice on duplicate URLs).
- **Validate.py repairs**: surname-only heuristic dropped (now full-name match required); ISBN separator stripping now handles Unicode dashes (en-dash, em-dash, figure-dash, NBSP) via NFKC normalisation + `unicodedata` Pd category.
- **Doc coherence repairs**: `docs/AUDIT_PROVENANCE.md` round table extended with Rounds 4–8 (was Round 1–3 only despite governance honest revision referencing 4–7); `docs/ARCHITECTURE.md` schemas/v0.{2,3}/ subdir target marked NOT YET (was 6 places asserting it as current); `docs/UNDERSTANDING_LEVELS.md` L2 % marked self-graded with `scripts/coverage_report.py` not-yet-implemented note; `README.md` lean/ block enumerates 16 per-section files; `innovation_heartbeat.yml` grep primary pattern unified with bullet-prefix form (fallback was carrying the load).

### Z. Round 9 user-override audit (consumer-chain drift repair + per-release mini-audit recommendation)
- **Idea**: Round 9 launched after Round 8 critic recommended switching to per-release mini-audit; instead the user override fired the standard 3-agent batch audit. Round 9 found a class of defect Round 8 missed: **the consumer chain** (loader → MCP → render → committed docs) was diverging from the **schema chain** Round 8 had repaired. Schemas had `archive_url` and `role`; loaders, MCP serializers, render_md, and even the auto-generated docs/disputes.md / timeline.md / overview.md had not propagated the changes. v0.7.6 "documentation coherence pass" was self-undermined: the auto-gen files were 6 release boundaries stale (last commit v0.5.1).
- **Status**: **Implemented** (v0.7.8, commit `9fcf87f`). 4 CRITICAL + 9 HIGH + 6 MEDIUM closed.
- **Files**:
  - `docs/disputes.md` / `timeline.md` / `overview.md`: regenerated; CI now `git diff --exit-code` after `render_md.py` to fail-loud on future stale-state.
  - `mcp/server.py`: `_entity_to_json` exposes `lean_stub` + `role`; `_claim_to_json` exposes `specific_support`; evidence + timeline dispatch expose `archive_url` and `url`. Regression suite `tests/test_mcp_server.py` (6 cases) pins serializer parity vs dataclass fields.
  - `loaders/python_minimal.py`: `Claim` dataclass gains `specific_support: str | None`; `_to_claim` reads it.
  - `tests/cold_start/run_cold_start.py`: BLOCK_LABEL_PATTERNS 2-tier (header strict tier-1 + keyword + 200-char proximity tier-2) repairs natural-prose regression introduced by v0.7.7. New `BlockSpec` dataclass + `_block_is_present`. Test cases: pass on natural-prose response (regression), bare-keyword still fails (invariant).
  - `LICENSE`: short-form → Apache-2.0 official 11264-byte text (Section 1-9 + APPENDIX). SPDX-Apache-2.0 detection now legally precise.
  - `tools/render_md.py`: `_render_claim` surfaces `specific_support` and `(archive_url)` link alongside `url`.
  - `docs/section_6_cor_3_12.md:421`: Joshi `v1+v2` retention → `v1 + Joshi FAQ 2025-11`.
  - `docs/section_8_disputes_timeline.md:64`: 2018 SS visit actor list reduced to Round-7 4 actors with audit attribution.
  - `docs/ARCHITECTURE.md`: 6 dead schemas/v0.{2,3}/ references repositioned as "planned, not yet on disk" with Round 9 audit attribution.
  - `tests/test_validation.py::test_audit_known_corrections_not_in_docs`: generalises Round 8's single-needle ISBN guard to a list of `FABRICATIONS = [(needle, label)]` + `ALLOWED` set. Adding a future fabrication is a 1-line PROSE_SCRUB_INVARIANTS extension.
  - `tests/test_verify_identifiers.py::test_unicode_dash_isbn_strip` regression for v0.7.7 NFKC + Pd category.
  - `tests/test_archive_evidence.py::test_apply_handles_duplicate_url_records_correctly` regression for v0.7.7 outcomes.index → enumerate fix.
  - `.github/workflows/ci.yml`: render diff gate, MCP initialize handshake (was `|| true`), Lean lake build advisory step.
- **Drift-zero contract restoration**: 5 fields silently dropped at MCP layer for 1+ releases. Consumer chain now sweeps every dataclass field via the parity test.
- **Process meta-finding**: 8 connected releases (v0.7.0 → v0.7.7) in 1 day exceeded the cadence at which prose-layer + consumer-chain drift can be sanity-checked. Round 8 critic's recommendation "per-release mini-audit instead of batch-end audit" stands; Round 9 going batch-style was an audit-process drift in itself. Round 10 (if user-override fires) should be 1-agent per-release form, or accept that further batch audits will continue surfacing 1-2 CRITICAL each round at decreasing marginal cost.

### AA. v0.7.9 — `tools/property_audit.py` (R4-R9 systemic root-cause structural fix)

- **Idea**: Rounds 4-9 each surfaced ≥ 1 CRITICAL drift in the same class — schema property declared in `schemas/*.json` failed to propagate to one of the consumer surfaces (context.jsonld, loaders/python_minimal.py, mcp/server.py, tools/render_md.py). Round 9 critic concluded that *per-release audits cannot replace a structural gate*; v0.7.9 is the structural gate. `tools/property_audit.py` enumerates every schema property and verifies presence at L1-L4 with indent-bounded source slicing for nested dispatch branches. L4 (render) is opt-in via per-property `render_optional` allow-list to keep the human-readable Markdown view curated.
- **Status**: **Implemented** (v0.7.9, commit `c92234a`).
- **Drift caught on first run**: `_claim_to_json` was silently dropping the `type` field (entity serializer emitted it; claim serializer did not). Identical R9-class drift, surviving R9. The audit caught it on its first execution — direct empirical validation.
- **Files**:
  - `tools/property_audit.py` (new, 323 lines) — full audit driver; `--json` machine-readable mode; `--schema <file>` filter; indent-aware function-body slicing handles nested branches inside `_dispatch_tool`.
  - `tests/test_property_audit.py` (new, 9 cases) — `CleanRepoAuditTests` (4 cases: clean repo passes, JSON mode parses, single-schema filter, unknown-schema is no-op), `DriftInjectionTests` (3 cases: L1/L2/L3 drift in tempdir copies must fail audit), `PolicyContractTests` (2 cases: every policy points to a real schema; render_optional ⊆ schema properties).
  - `mcp/server.py:108`: `_claim_to_json` now emits `"type": claim.type` (drift fix uncovered by audit).
  - `.github/workflows/ci.yml`: new `Property propagation audit` step + `Run property audit tests` step, both gating merge.
  - `docs/PROPERTY_PROPAGATION.md` (new) — checklist for adding/renaming/removing schema properties; lists every consumer surface and the precise edit each one requires.
  - `CONTRIBUTING.md`: PR rule #3 expanded to include `property_audit.py` and `test_property_audit`; new rule #5 references `PROPERTY_PROPAGATION.md`.
- **Why this closes the class**: a property added to schema without propagation now fails CI. The audit is content-light (source-string presence checks) but contract-strict (every schema property × every required surface). False positives are impossible by construction (the schema is the source); false negatives require either (a) the policy `render_optional` to be too permissive, or (b) a new consumer surface added without extending the audit, both of which are conscious acts visible in PR diff.
- **What this does NOT close**: semantic correctness (property values can still be wrong), prose-layer scrub (Round 8 class — repairs to `data/` followed by stale prose in `docs/section_*.md`), or external-reality drift (Round 6 class — URL rot). These remain handled by `tools/validate.py`, the `Render docs and check committed artefacts in sync` CI gate, and `tools/verify_urls.py` respectively.
- **Forward**: a future Round N audit finding multi-layer property drift would mean the audit policy itself needs tightening (render_optional too permissive, or a new consumer surface added without extending POLICIES). The audit is the gate, not the answer; it makes the gate cheap.

### BB. v0.7.10 — Architect-Sec-8 + HIGH-2 deferred coverage close + governance machinery

- **Idea**: Two test-coverage gaps and one governance gap had been deferred since v0.7.8. Architect Sec-8 noted that `tools/render_md.py` and `loaders/python_minimal.py` had no direct unit tests (only indirect coverage via end-to-end CI render-diff and validate.py loading). HIGH-2 (Round 9 architect) flagged that `data/context.jsonld` had only forward-direction coverage from property_audit.py. Governance honest-revision (Round 7) noted that CONTRIBUTING.md PR rule #1 (label requirement) was a documentation claim with no machinery. v0.7.10 closes all three.
- **Status**: **Implemented** (v0.7.10, commit `e5b85f1`).
- **Files**:
  - `tests/test_render_md.py` (new, 24 cases) — per-render-function contract: banner invariant, section grouping, ordering by date, evidence URL + archive_url surfacing, `_render_claim` neutrality (no editorial canaries like "consensus" / "settled"), specific_support / specific_objection conditional surfaces, missing-evidence placeholder, em-dash actor formatting.
  - `tests/test_loader.py` (new, 23 cases) — `LoadGraphTests` (full round-trip / missing dir / missing required file / evidence optional / non-graph rejection), per-dataclass field population + optional defaults + KeyError → ValueError translation, `GraphQueryTests` (entity / claim lookup, claims_about, opposing_pairs both directions, claims_by_position, claims_by_peer_review, frozen=True immutability), and `LiveGraphSmokeTests` against actual `data/`.
  - `tests/test_context_bidirectional.py` (new, 12 cases) — `ReverseDirectionTests` (no orphan @context terms; namespace prefix self-resolution), `TermStructureTests` (string-or-object, @id presence, @type allow-list = {@id, xsd:date, xsd:gYear}, @container = @set), `CollisionTests` (no two properties expand to same IRI), `RoundTripExpansionTests` (label → schema:name, archive_url → iut:archiveUrl, etc).
  - `tools/innovation_explorer.py` (new, 305 lines) — structural sentinel for INNOVATION_LOG.md: open-slot health, status discipline (`Implemented` / `Surveyed` / `Deferred` / `Rejected` / `Subsumed`), Implemented-must-cite-evidence (commit SHA / version tag / file path), no-duplicate-letter, optional `--strict-paths` checks file existence. `--json` mode for machine consumption.
  - `tests/test_innovation_explorer.py` (new, 9 cases) — clean live log + tempdir-driven structural drift injection (missing open slot / Implemented without evidence / duplicate letter / unknown status / emphasis-wrapped status / Subsumed status).
  - `.github/workflows/pr_label_gate.yml` (new) — exactly-one-of-allowed-labels gate at PR-event time, with notice/error annotations. Closes CONTRIBUTING.md PR rule #1 governance gap.
  - `.github/workflows/ci.yml` — 6 new steps: loader / render_md / context bidirectional / innovation explorer (script) / explorer tests / overall coverage anchor.
- **Test count**: 100 → 168 (+68).
- **Why this layer**: every defect class found by Rounds 4-9 had an existing CI gate that could have caught it *if a test had been written*. The render_md / loader / context test files address that root cause one layer up: not "how to detect a drift" but "did the contract have any test at all?". Property_audit (v0.7.9) made schema/consumer-chain drift impossible; v0.7.10 makes the consumer-chain code itself testable per-function.
- **Innovation-log structural class**: until v0.7.10, the log had no machinery to enforce its own append-mostly invariant. A future Implemented claim could ship without commit reference (Round 7 honest-revision noted that "v0.7.0 stale-count fix" claim cited no commit); a future audit could overwrite the open slot. The explorer is the gate for both.
- **Forward**: Round 10 (if user-override fires) is now structurally limited to (a) semantic correctness, (b) prose-layer scrub miss, or (c) external-reality drift — the three remaining classes after v0.7.9 (property drift) + v0.7.10 (test coverage / governance machinery).

### CC. v0.7.11 — NDL Search API extension to ISBN-net resolution

- **Idea**: Round 7 fabricated Kato ISBN (`978-4-04-110262-7`) had a passing structural shape but no real existence. `tools/verify_identifiers.py --check-isbn` only consulted Open Library, whose Japanese-language coverage is partial (`unresolved` was the polite response, blocking automated detection of jp-fabrication-class). v0.7.11 closes that gap by adding a National Diet Library (NDL) OpenSearch fallback for Japanese-group ISBNs (978-4-/4-).
- **Status**: **Implemented** (v0.7.11, commit `6ab5c38`).
- **Files**:
  - `tools/verify_identifiers.py`: new `_is_japanese_isbn(digits)` (978-4 / 9794 prefix; ISBN-10 leading 4); `_query_ndl_isbn(digits)` issues GET to `https://iss.ndl.go.jp/api/opensearch?isbn=…`, substring-matches `<openSearch:totalResults>N</openSearch:totalResults>` (or `<os:` namespace variant) without an XML parser dependency. `verify_isbn_network` extended: jp ISBN + OL 404 + NDL 0-hits → `invalid` (the fabrication signal); jp ISBN + OL 404 + NDL hit → `alive`; jp ISBN + OL 404 + NDL transport error → `unresolved` (no false-positive on flake); non-jp behaviour unchanged.
  - `tests/test_verify_identifiers.py`: new `_MockResponse` helper, `_fake_404` constructor, `_ndl_body(total_results)` Atom RSS factory; replaces the single 404-only test with 5 path tests (`test_non_jp_open_library_404_is_unresolved_no_ndl_call`, `test_jp_open_library_404_ndl_zero_hits_is_invalid`, `test_jp_open_library_404_ndl_hit_is_alive`, `test_jp_open_library_404_ndl_transport_error_is_unresolved`, `test_open_library_2xx_is_alive_no_ndl_call`); new `JapaneseIsbnDetectionTests` (5 cases for `_is_japanese_isbn`).
- **Reason it caught**: the ISBN registration group `4-` (Japanese) is one of the smallest by population (Open Library coverage skews Anglophone). The R7 fabricated ISBN happened to use group `4-04-` (KADOKAWA), so the only way to catch it automatically was to query a registry with comprehensive jp coverage. NDL is the Japanese national bibliography; absence from NDL on a structurally-valid `978-4-` is a strong fabrication signal.
- **Why stdlib-only XML matching**: NDL returns Atom XML even on no-hits; importing `xml.etree.ElementTree` would still parse correctly, but the only datum we need is the integer in `<openSearch:totalResults>`. A regex over the response body keeps the dependency footprint at zero modules outside the existing `urllib.request` plus stdlib `re`. The dependency-minimisation discipline (Round-1 architect choice for the entire repo) is preserved.
- **Forward**: a future ISBN fabrication that uses a non-Japanese registration group (978-0-, 978-1-, etc) would still surface as `unresolved` not `invalid`. If such a class is observed, extend the heuristic to consult Open Library's `search.json` endpoint (which sometimes finds books that the strict ISBN endpoint 404s on).

### DD. v0.7.12 — Wayback Machine archive_url passive-lookup population

- **Idea**: Schema-level support for `archive_url` shipped at v0.7.0 with empty values everywhere; the actual Wayback population was deferred. v0.7.12 runs `tools/archive_evidence.py --network --lookup --apply` against the live Wayback Availability API for every evidence and timeline record that has a primary `url` and no `archive_url`. The result rotates the Merkle root for the first time since the consumer-chain repair at v0.5.2.
- **Status**: **Implemented** (v0.7.12, commit `a0de80e`).
- **Why this is a one-shot ingestion, not a CI gate**: the Wayback Availability API is rate-limited and best-effort; running it on every PR would (a) flake CI, (b) hammer archive.org, and (c) produce churn whenever the closest snapshot rotates. The right operational pattern is a rare maintainer-driven sweep (this commit) plus a separate `--submit` sweep for URLs that still have no snapshot. The repo is therefore *not* adding archive_url population to CI.
- **Files**: `data/evidence.json`, `data/timeline.json` (data rotation: 3 records gained `archive_url`); `data/merkle_root.txt` (root rotation `6736c24a…` → `c516d24f28d9686f6632d147f714bd855e26533701b3e63b366a825b6af63cbd`); `docs/{overview,disputes,timeline}.md` (regenerated by render_md). Tests, schemas, and tooling unchanged.
- **Empirical numbers (this run)**:
  - 59 records queried (34 evidence + 25 timeline; 4 timeline records have no primary URL and were skipped without a query).
  - 3 records returned an existing Wayback snapshot:
    `evidence:IUTchII_2012` → `https://web.archive.org/web/20260407152619/…IUT II.pdf`
    `evidence:Joshi_FAQ_2025_11` → `https://web.archive.org/web/20251218211839/…joshi-mochizuki-FAQ.pdf`
    `event:2025_11_joshi_faq` → same arizona.edu URL as the evidence record (timeline's `url` and `evidence:Joshi_FAQ_2025_11.url` coincide).
  - 52 records: Wayback says "no snapshot available". This is the realistic state of the IUT corpus on the open archival web — most kurims.kyoto-u.ac.jp PDFs, math.uni-bonn.de PDFs, and arXiv abstract pages have not been actively archived. The signal is meaningful: passive lookup is sub-5 % effective for this domain.
  - 4 timeline records have no `url` (1985 abc conjecture, 2018 SS visit, 2019 Kato book, 2020 PRIMS acceptance) and were correctly skipped.
- **Drift-zero guarantee preserved**: `tools/property_audit.py` v0.7.9 checks that the property propagates from schema → context → loader → MCP → render. v0.7.12 only changes data values, never the property layer; the audit remains green. The auto-generated `docs/{overview,disputes,timeline}.md` files now surface the new `archive_url` for the 3 records — the `Render docs and check committed artefacts in sync` CI gate verifies parity.
- **Empirical insight**: **Wayback Availability API is not a sufficient mechanism for IUT corpus archival.** Of 55 URLs queried (with-url records), only 3 had pre-existing snapshots. The remaining 52 must be *actively submitted* via Save Page Now to create snapshots. That is a separate `--submit` mode and a separate commit so the heavier SPN rate-limiting (≈5-10 req/min anonymous; longer per-request latency for PDFs) does not contaminate the lookup pass. Deferred to v0.7.13 (pre-condition: maintainer review of the SPN rate-limit profile and decision on whether to consume an Anonymous API tier or register an `iut-status-2026@…` Internet Archive account).
- **What this does NOT close**: 52 records are still vulnerable to URL rot until a snapshot exists. `tools/verify_urls.py` continues to flag liveness, but content drift between today's URL and a future fetched URL is currently undetectable for those 52. v0.7.13 SPN sweep is the answer.
- **Validation**: 177 unittest PASS (unchanged from v0.7.11); validate.py + property_audit.py + innovation_explorer.py + verify_merkle.py + verify_urls.py + verify_identifiers.py all green; render_md.py + CI render-diff gate passes.

### EE. v0.7.13 — Round 10 closure: README scrub-scope + AST property_audit + JSON-RPC compliance + section-IRI gate + url-scheme hardening

- **Idea**: Round 10 user-override audit ran three independent sub-agents (analyst + architect + critic). Two of them, working in parallel without cross-pollination, surfaced **the same** CRITICAL: `README.md:276` still carried a clickable link to `arXiv:2505.10568v2 (2026-05-02)` — a fictional Joshi v2 that Round 5 (commit before v0.7.0) had explicitly removed from `data/`. The R8 fabrication-scrub test (`test_audit_known_corrections_not_in_docs`) had been scanning `docs/*.md` only; the entry never reached the test plane because README lives at the repo root. A second CRITICAL — also surfaced independently — was that the property-drift class declared "structurally closed" by v0.7.9 / 9.5 was in fact still leaking: `iut_timeline` in `mcp/server.py` was silently dropping the `type` field, and the substring-based property_audit kept reporting OK because the MCP response envelope `{"type": "text"}` accidentally satisfied the substring test for the schema property name `type`. Two further CRITICALs were collateral: `schemas/timeline.json:url` had no `format` / `pattern` constraint and was accepting `javascript:alert(1)`, and `mcp/server.py` main loop crashed on JSON-RPC 2.0 batch (`[…]`) and non-object roots, in addition to replying to notifications against §4.1.
- **Status**: **Implemented** (v0.7.13).
- **Files**:
  - `README.md`: L56 prose + L276 link rewritten to drop the fictional v2 and add the real Joshi FAQ 2025-11 (`evidence:Joshi_FAQ_2025_11`).
  - `docs/UNDERSTANDING_LEVELS.md:39`: same prose fix.
  - `docs/section_2_hodge_theater.md:83`: `iut:Theta-link` / `iut:log-link` → `iut:theta_link` / `iut:log_link` (data/ has always used snake_case).
  - `docs/section_8_disputes_timeline.md:188`: Woit IRIs corrected to the registered 2024 records (`claim:woit_blog_2024_mochizuki_on_joshi_skeptical` / `evidence:Woit_blog_2024_mochizuki_on_joshi`); the prior `..._2025` references pointed to non-existent records.
  - `mcp/server.py`: `iut_timeline` payload re-emits `"type"`; main-loop dispatch refactored into `_handle_jsonrpc()` with proper batch (§6) / notification (§1.2 — `"id"` absent ≠ `"id": null`) / non-object (§4.4 → -32600) / parse-error (§4.4 → -32700) handling; notification with unknown method now returns no response per §4.1.
  - `schemas/timeline.json`: `url` field gains `format: uri` + `pattern: "^https?://"` (closes javascript:/data:/file: injection class).
  - `tools/property_audit.py`: `_check_l3_mcp` upgraded from substring-match to AST-based payload-dict-key extraction (`_extract_payload_dict_keys` walks dict literals containing `"id"`, which is the stable marker of a payload — the response envelope never carries `id`). Closes the v0.7.9 / 9.5 false-positive class.
  - `tests/test_validation.py`: `FABRICATIONS` list expanded with 8 new (needle, label) pairs covering Joshi v2 / `iut:Theta-link` / Woit 2025 misreference; scan scope expanded to repo-root `*.md`; per-(path, needle) `DOCUMENTED_AS_FABRICATION` allowlist for legitimate historical-record references in release notes / audit prose. New `test_section_docs_iris_resolve_in_data` enforces the whole class structurally (every `iut:|claim:|evidence:|event:|person:|paper:|org:` IRI in `docs/section_*.md` must resolve in `data/`). New `test_javascript_url_in_timeline_rejected` pins the schema constraint.
  - `tests/test_mcp_server.py`: `JsonRpcProtocolEdgeCaseTests` (7 new cases — batch / notification-omitted-from-batch / empty batch / non-object root / unknown-method-as-notification / id=null is a request / missing method field) + `IutTimelinePayloadFieldTests` (3 new cases — type field present / url+archive_url present / actor list shape).
  - `docs/AUDIT_PROVENANCE.md`: Round 10 row added; disclaimer commit-range updated from `591fab2` (v0.2.3) to `a0de80e` (v0.7.12) + Round 10 closure at v0.7.13.
  - `docs/ARCHITECTURE.md:10`: stale "91 unittest cases" → "189 unittest cases".
- **Test count**: 177 → 189 (+12).
- **Why this layer**: Round 9.5 / 9.6 / 9.7 closed three drift classes (property propagation, render/loader/context unit-test coverage, jp-ISBN fabrication signal). Round 10 demonstrates that *the gates themselves can drift*: the property_audit substring check was structurally weaker than its docstring claimed, the fabrication-scrub test had a coverage hole at the repo root, and the section_*.md curated docs had no IRI gate at all. Closing those three meta-failures is what v0.7.13 actually delivers — the user-visible CRITICAL fixes (Joshi v2 link / type-field drop / javascript: URL accept / JSON-RPC crash) are downstream of those meta-failures.
- **What R10 did NOT close (deferred to R11 / v0.7.14)**:
  - Architect M2 / M3: `tools/validate.py` person/actor invariant is forward-only (Person → must have edge); reverse direction (`actor` / `proponent` strings → must resolve to a registered Person or Organization) leaves 9 actors + 2 proponents unregistered. Adding an `Organization` schema type plus the reverse rule is HIGH but mechanical.
  - Architect H4: `tools/archive_evidence.py:200,235` host check is `startswith("http://web.archive.org/")` — a `web.archive.org.evil.com` redirect would be persisted. Switching to `urllib.parse.urlparse(...).netloc == "web.archive.org"` is a 1-line fix; deferred only to keep this commit's surface focused.
  - Critic M1: 13 occurrences of "commit pending" in this very file (across candidates A-DD) are stale placeholders for already-shipped commits. A separate dedicated commit will replace them with actual SHAs from `git log`. Mechanical but touches every entry — keeping it out of v0.7.13 to make the Round-10 changeset legible.
  - Architect H1 / Critic m4: ARCHITECTURE.md test count refresh + AUDIT_PROVENANCE disclaimer commit-range refresh **were** done in v0.7.13 (this entry), but the broader staleness of FAILURE_MODES.md / UNDERSTANDING_LEVELS.md ("definition_locator" / "verbatim_short_statement" / `migrate_v0_2_to_v0_3.py` / `superseded_by_lana_2026_07` / archive_url=required at v0.3) — all describing aspirational mitigations as if implemented — remains. Architect C3 recommended an "honest revision" pass mirroring v0.7.8's ARCHITECTURE.md schemas/v0.{2,3} repair. Deferred to v0.7.14 (separate commit so doc-rewrite churn does not bury Round 10 code fixes).
  - Architect M5: `data/timeline.json` synthetic Jan-1 dates (`event:1985_abc_conjecture`, `event:2008_frobenioids`, `event:2009_etale_theta`) — these are precision-loss artefacts of the `format: date` schema constraint. Adding a `date_precision` field (year / month / day) and migrating the 3 records is an HIGH for v0.7.14.
  - Critic M5: `https://hinanohart.github.io/iut-status-2026/iri/` IRI base URL is 404 (Pages not deployed). Either ship a Pages workflow or honestly document the IRI as opaque-not-dereferenceable. Deferred.
- **Forward**: Round 10 was originally framed as closing the *gate-drift* class. **v0.7.14 (Round 11) retracts that claim.** Round 11 sub-agents — explicitly instructed to attempt to refute the closure — succeeded on 3 of 4 layers (`_extract_payload_dict_keys` "id" discriminator was bypassable by sibling pollution / dict comprehension / `dict()` Call form; the JSON-RPC compliance was missing §4 jsonrpc-version + §4.2 params-type checks and inputSchema runtime enforcement; the section-IRI regex char-class missed `.` so `iut:Cor.3.12` — the central disputed corollary — was invisible to the very gate that was supposed to protect it). Honest framing going forward: the gate-drift class is **not closed**; per-release mini-audit cadence is the operating norm. See candidate FF for the Round 11 closure of these inherited bypasses.

### FF. v0.7.14 — Round 11 closure: refute Round 10 + AST narrow + JSON-RPC §4/§4.2 + inputSchema runtime + IRI gate dotted-IRI fix + evidence URL scheme parity

- **Idea**: Round 10 INNOVATION_LOG candidate EE claimed *"Round 10 closes the gate-drift class"*. Round 11 user-override audit ran three independent sub-agents instructed to **attempt to refute** that closure. They succeeded on 3 of 4 layers, plus surfaced multiple inherited bypasses. Round 11 ships v0.7.14 with the inherited-bypass closures, and **retracts** the candidate-EE overconfident framing.
- **Status**: **Implemented** (v0.7.14, commit pending).
- **Files** (12 modified + 0 added; no new files needed because Round 11 fixes were narrowing existing patches rather than scaffolding new structures):
  - `tests/test_validation.py:294` — section-IRI gate regex char-class extended `[A-Za-z0-9_]+` → `[A-Za-z][A-Za-z0-9_.\-]*`. Without `.`, `iut:Cor.3.12` (cited 28× across 6 section docs) was invisible to the Round-10 gate. Positive-control regression test added (`test_section_iri_gate_finds_dotted_iris`).
  - `tests/test_validation.py:test_url_scheme_pattern_uniform_across_schemas` — 4 URL fields (timeline.url, timeline.archive_url, evidence.url, evidence.archive_url) all required to declare `format: uri` + `^https?://` pattern. Round-10 hardened only timeline.url; evidence.* and timeline.archive_url were left silently accepting javascript:/data:/file:.
  - `schemas/evidence.json` — `url` and `archive_url` gain `format: uri` + `pattern: ^https?://` (parity with timeline.url R10 fix). XSS surface eliminated at schema layer.
  - `schemas/timeline.json` — `archive_url` ditto. Plus new optional `date_precision: enum [year, month, day]` field for the 3 synthetic Jan-1 dates whose precision is year-only.
  - `tools/property_audit.py:_extract_payload_dict_keys` — narrowed from "any-Dict-with-`id`-key" (R10 false-positive class identified above) to two explicit patterns: (1) `ast.Assign` whose target name is in `PAYLOAD_VARIABLE_NAMES = ("payload", "payload_list")`, with the assigned subtree walked for nested ast.Dict; (2) `ast.Return` of a top-level `ast.Dict` literal (covers `_entity_to_json` / `_claim_to_json` shape). Critically, `ast.Return` of an `ast.Call` (the `_make_response(...)` envelope wrapper) does NOT count, eliminating envelope-key pollution at its root. Future MCP refactor must adopt one of those two patterns or update `PAYLOAD_VARIABLE_NAMES`.
  - `mcp/server.py:_handle_jsonrpc` — added (a) §4 jsonrpc-version validation (must be literal `"2.0"`); (b) §4.2 params type validation (Object or Array; `null` / `int` / `string` / `bool` rejected with -32602); (c) §6 nested-batch rejection (`_depth > 0` guard); (d) tools/call requires by-name (Object) parameters specifically.
  - `mcp/server.py:_validate_tool_arguments` (new helper) — at runtime, enforces the `inputSchema.pattern` / `required` / `type` declarations that v0.7.13 left as documentation-only. Crashes converted to clean -32602 invalid-params responses.
  - `mcp/server.py` `iut_timeline` payload re-emits `date_precision` (drift-zero propagation through L1-L4).
  - `tools/archive_evidence.py:200,235` — host check upgraded from `startswith("http://web.archive.org/")` prefix-match to `urlparse(...).netloc.lower() == "web.archive.org"` strict-equality. Closes the `web.archive.org.evil.com/…` redirect class. Path is also asserted to start with `/web/`.
  - `tools/innovation_explorer.py:COMMIT_REF_RE` — length-bounded `(?:[0-9a-f]{7,12}|[0-9a-f]{40})` so the 64-char Merkle root cannot masquerade as a commit citation in `Implemented-needs-evidence` checks.
  - `data/context.jsonld` — `date_precision` mapping added (`iut:datePrecision`).
  - `data/timeline.json` — 3 synthetic Jan-1 records gained `date_precision: "year"` (fabrication-class same as R7 jp-ISBN).
  - `data/merkle_root.txt` — rotated `c516d24f…` → `e6d1d1b5bfc7fc19f6743be127896abaf5ae25df80a7ad39b30e15f6740c42ae` (timeline.json data rotation; first rotation since v0.7.12 Wayback population).
  - `loaders/python_minimal.py` — `TimelineEvent.date_precision: str | None = None`; factory accepts the field.
  - `.github/workflows/ci.yml` — Python matrix `["3.10", "3.11", "3.12"]` so the README's "Python 3.10+" claim is empirically tested.
  - `README.md` — v0.7.13 + v0.7.14 release-notes rows added (Round-11 critic surfaced the v0.7.13 row missing as an internal contradiction); test-count `177 cases` → `201 cases`.
  - `docs/INNOVATION_LOG.md` — 13 "commit pending" placeholders replaced with actual short SHAs derived from `git tag → git rev-list -n1`. Candidate EE Forward-block retracts the "gate-drift class closed" claim.
  - `docs/AUDIT_PROVENANCE.md` — Round 11 row added (the longest entry to date because the meta-finding is significant).
  - `tests/test_mcp_server.py` — 10 new cases: `test_wrong_jsonrpc_version_returns_invalid_request` / `test_params_null_returns_invalid_params` / `test_params_non_object_non_array_returns_invalid_params` / `test_nested_batch_rejected_at_inner_level` / `IutInputSchemaEnforcementTests` (5 cases pinning -32602 for non-string IRI / pattern violation / wrong namespace / accepting dotted IRI / missing required).
- **Test count**: 189 → 201 (+12).
- **Why this layer**: Round 10 INNOVATION_LOG explicitly claimed "the gate-drift class is closed". Round 11 was instructed to attempt to refute that. The attempt succeeded — 3 of 4 layers were reverse-engineered to bypasses. The honest framing is that **gate-drift is a recurring class**: each release ships with at least one Round-N CRITICAL surface, the structural gates are typically narrow patches that catch the exact reproduction case, and adversarial-form testing must be done explicitly each round. Round 11 explicitly retracts the closure claim and codifies the per-release mini-audit cadence as the operating norm.
- **What R11 did NOT close (deferred to v0.7.15)**:
  - C5 (R11 architect / critic): `data/context.jsonld:38,65` `proponents` and `actors` carry `@container: @set` but no `@type: @id`, treating them as plain literal strings. Migrating to `person:Mochizuki` / `org:PRIMSEditorialBoard` IRIs requires (a) adding `Organization` to entity schema type enum + entity.json regex, (b) adding 9+ Person + 2+ Organization records to `data/entities.json`, (c) updating `data/claims.json` and `data/timeline.json` to use IRI references, (d) extending `validate.py` with the reverse-direction Person/Organization-must-resolve invariant. v1.0 task; documented as known limitation in `LLM_CONTEXT.md` going forward.
  - render_md.py URL escape (R11 architect MED-7 / critic CRIT-4 downstream): even after schema-level scheme hardening, defense-in-depth scheme allowlist at render boundary is desirable. v0.7.15 task.
  - LLM_CONTEXT.md L82-96 IRI references unwrapped in backticks — the section-IRI gate after R11 widening would catch these if backticks are added; mechanical wrap pass deferred.
  - `cold_start_evidence.md` honest revision (R11 critic MAJ-2): README L73 "empirically tested where vendor evidence is recorded" plus `cold_start_evidence.md` showing 0/0/0 across 7 vendors. Honest revision is to surface the 0-runs state in README itself.
  - IRI base URL `https://hinanohart.github.io/iut-status-2026/iri/` 404 — Pages deploy or honest disclaimer in v0.7.15.
- **Forward**: v0.7.15 will land the deferred items above. Round 12 (if user-override fires) is **expected to find at least one CRITICAL** because the empirical pattern from Rounds 4-11 is unbroken; the AST narrow / JSON-RPC compliance / scheme parity / IRI gate widening / inputSchema enforcement done in v0.7.14 are themselves narrow patches that may have bypasses an adversarial Round-12 will surface.

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
