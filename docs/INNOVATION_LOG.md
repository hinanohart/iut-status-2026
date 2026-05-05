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
- **Current root**: `ff8cdef62ad9386f8eab037613c3364e2eb996bdee6a5b1f48e14ba6f8691b34` (entities=33 / claims=16 / evidence=24 / timeline=20).

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

### Q. (open slot for future innovation-explorer findings)

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
