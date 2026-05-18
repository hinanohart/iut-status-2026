# iut-status-2026

[![CI](https://github.com/hinanohart/iut-status-2026/actions/workflows/ci.yml/badge.svg)](https://github.com/hinanohart/iut-status-2026/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


> A vendor-neutral, drift-resistant, dispute-preserving status index for
> Inter-universal Teichmüller theory (IUT) and the surrounding
> mathematical controversy.

This repository encodes the current (2026-05) status of:
1. Mochizuki's original 2012 IUT proof of the abc conjecture
2. The Scholze-Stix 2018 counter-claim
3. Mochizuki's 2018 / 2025 responses
4. The Joshi 2025 / 2026 reformulation
5. The LANA Lean 4 formalization project (founded 2026-03-31, mid-report scheduled 2026-07-17)

…in a format engineered to **eliminate interpretation drift across
LLMs** (Claude / GPT / Gemini / Llama / Qwen / DeepSeek / Mistral / …)
**and across human readers**.

## Why this repository exists

When asked about IUT, contemporary LLMs frequently:
1. assert "abc is proved" without mentioning Scholze-Stix, OR
2. assert "IUT is broken" without mentioning Mochizuki's response, OR
3. silently fuse the two positions into a fictional consensus.

All three are factually wrong as of 2026-05-06. The dispute is
unresolved. This repository encodes the unresolved status in a format
that does not collapse under summarization.

## Drift-resistance at four layers

| Layer | Mechanism | Drift guarantee |
|---|---|---|
| **Physical layer** (`data/merkle_root.txt`) | SHA-256 Merkle root over all canonical-JSON records; verified in CI on every PR | **Cryptographic** (deterministic): a single-byte change anywhere changes the root |
| **JSON-LD core** (`data/*.json`) | Stable IRIs (`iut:Cor.3.12`), claim graph with `counters`/`supports`/`relates_to` edges, structured `peer_review_status` orthogonal to `position` | Strong (~95%) at IRI level |
| **Lean 4 stubs** (`lean/IutStatus/`) | `theorem cor_3_12 : Prop := sorry` placeholders, mathlib4-compatible | Semantic (when `sorry` is replaced by LANA) |
| **Markdown view** (`docs/`) | Auto-generated from JSON-LD via `tools/render_md.py` | Human-readable; not source of truth |

**Honest scope.** Drift is eliminated at the IRI/structure level.
Full semantic drift-zero requires Lean 4 formalization, which is
being attempted by the
[LANA project](https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f)
(Commelin, Kedlaya, Hoshi, Topaz, Kato, et al.; founded 2026-03-31;
mid-report scheduled 2026-07-17). When LANA produces formal
`theorem` bodies, the `sorry` stubs in this repository will be
replaced.

## What "100% understanding" means here

This repository operates at three levels of "understanding", with sharply
different feasibility. See `docs/UNDERSTANDING_LEVELS.md` for the full
operational definition.

| Level | Statement | Feasibility |
|---|---|---|
| **L1** AI Navigation Capability | A fresh LLM session can resolve every IRI, apply the 5-block answer template, and decline gracefully when the graph is silent. | Achievable in this OSS alone; auto-verifiable. |
| **L2** Asymptotic Statement Coverage | Every numbered statement in IUTchI–IV, Frobenioids I–II, *Étale Theta*, *Alien Copies*, Mochizuki *Rpt2018* / *Cmt2018-05* / *IUT-2025-10*, Yamashita FAQ, Scholze–Stix 2018, Joshi v1, and Joshi FAQ 2025-11 is registered. | **Asymptotic, never absolute** — new papers re-extend the goalpost. |
| **L3** Mathematical Understanding (validity judgement) | Decide whether IUT proves abc; whether SS critique is terminal; whether Joshi reformulation succeeds. | **Out of scope, intentionally and permanently.** Delegated to LANA + future external reviews. |

The repository's "100 %" target is L1 = 100 % + L2 best-effort asymptote.
L3 is never claimed. Roadmap and current % are tracked in
`docs/UNDERSTANDING_LEVELS.md`.

## Cold-start contract (best-effort, vendor-tested where evidence exists)

A fresh LLM session with no prior memory of this repository should be
able to:
1. Read `LLM_CONTEXT.md`
2. Read `data/*.json`
3. Answer any IUT question with the mandatory 5-block template

…and arrive at the same set of citations as any other LLM doing the
same. This is the operational *intent* of "drift-resistant" in this
repo. **Conformance has not yet been empirically demonstrated across
multiple LLM vendors** — `docs/cold_start_evidence.md` shows 0 / 0 / 0
across the 7 advertised vendors as of v0.7.15; the L1 fixture in
`tests/cold_start/` exists and the `cold_start_weekly.yml` workflow
will populate the table once the API budget is approved. The contract
is best-effort, not unconditional, and the multi-vendor empirical
evidence remains future work. The 5-block template is mandatory for
conforming LLMs; see `LLM_CONTEXT.md` §3.3.

> **Stable IRI caveat (v0.7.15)**: The `iut:` / `claim:` / `evidence:`
> namespace base URLs (`https://hinanohart.github.io/iut-status-2026/iri/…`)
> and JSON-Schema `$id` URLs are currently **opaque identifiers**, not
> dereferenceable URLs — GitHub Pages is not yet deployed for this
> repo. The "Strong (~95 %) at IRI level" drift-resistance claim
> refers to *internal* identifier stability (every reference resolves
> in `data/`, enforced by `tests/test_validation.py`), not to external
> HTTP dereference. Pages deploy or `urn:` rebase is on the v0.8
> roadmap.

## Multi-consumer design

| Consumer | Entry point |
|---|---|
| Any LLM (Claude / GPT / Gemini / Llama / Qwen / DeepSeek / Mistral / …) | `LLM_CONTEXT.md` |
| Claude Code specifically | `CLAUDE.md` (thin shim → `LLM_CONTEXT.md`) |
| MCP-compatible LLM client | `mcp/server.py` (`iut_protocol`, `iut_entity`, `iut_claims_about`, `iut_evidence`, `iut_timeline`) |
| Human researcher | `README.md` → `docs/overview.md` → `docs/section_*.md` |
| Program (Python) | `loaders/python_minimal.py` (stdlib-only, no deps) |
| Program (jq / shell) | `data/*.json` directly |
| Lean 4 | `lean/lakefile.lean` |
| Validator (CI) | `tools/validate.py` + `schemas/*.json` |

## Repository layout

```
iut-status-2026/
├── LLM_CONTEXT.md         # Vendor-neutral system prompt for any LLM
├── CLAUDE.md              # Claude Code shim → LLM_CONTEXT.md
├── README.md              # this file
├── data/                  # JSON-LD source of truth
│   ├── context.jsonld     # @context for all data files
│   ├── entities.json      # IUT concepts + persons + papers (104 entries as of v0.7.0)
│   ├── claims.json        # Mochizuki / Scholze-Stix / Joshi / LANA / Woit / Yamashita / nLab claim graph (53 entries)
│   ├── evidence.json      # 34 bibliographic evidence records (papers, blogs, books, projects)
│   └── timeline.json      # 1985-2026 dispute timeline (25 events)
├── schemas/               # JSON Schema 2020-12 validators
│   ├── entity.json
│   ├── claim.json
│   ├── evidence.json
│   └── timeline.json
├── lean/                  # Lean 4 theorem stubs (mathlib4-compatible, v0.7.5 per-section split)
│   ├── lakefile.lean
│   └── IutStatus/
│       ├── Basic.lean              # orchestrator — imports every per-section module
│       ├── Anabelian.lean          # iut:anabelian_geometry
│       ├── AbsoluteAnabelian.lean  # iut:absolute_anabelian
│       ├── MonoAnabelian.lean      # iut:mono_anabelian
│       ├── Frobenioid.lean         # iut:Frobenioid
│       ├── EtaleTheta.lean         # iut:etale_theta
│       ├── MonoTheta.lean          # iut:mono_theta_environment
│       ├── TemperedRigidity.lean   # iut:tempered_rigidity
│       ├── Cuspidalization.lean    # iut:cuspidalization
│       ├── HodgeTheater.lean       # iut:HodgeTheater
│       ├── ThetaLink.lean          # iut:theta_link
│       ├── LogLink.lean            # iut:log_link
│       ├── Multiradial.lean        # iut:multiradial_algorithm + Ind1/Ind2/Ind3
│       ├── Cor312.lean             # iut:Cor.3.12
│       ├── HeightInequality.lean   # iut:height_inequality
│       ├── Diophantine.lean        # iut:diophantine_inequality
│       └── ABC.lean                # iut:abc_conjecture + iut:abc_special_case_via_iut
├── mcp/                   # MCP server for any MCP-compatible LLM client
│   ├── server.py
│   └── README.md
├── loaders/               # Reference parsers
│   └── python_minimal.py  # Python 3.10+, stdlib only
├── tools/                 # Maintenance utilities (all stdlib-only)
│   ├── validate.py             # JSON Schema + cross-reference + verbatim-cap + Person edge-or-role + lean_module resolution
│   ├── build_merkle.py         # Bitcoin-style Merkle tree over canonical JSON
│   ├── verify_merkle.py        # recompute and compare to data/merkle_root.txt
│   ├── verify_urls.py          # URL liveness verifier (offline syntax + opt-in --network HEAD/GET)
│   ├── verify_identifiers.py   # DOI structural + ISBN-10/13 ISO 2108 + opt-in --check-doi / --check-isbn
│   ├── archive_evidence.py     # Wayback Machine bootstrap (offline / --lookup / --submit / --apply)
│   └── render_md.py            # JSON-LD → Markdown view generator
├── docs/                  # Human-readable view (auto-generated + curated)
│   ├── overview.md / disputes.md / timeline.md  # auto-generated by render_md.py
│   ├── concepts/                # per-side drafts (mochizuki-side / SS-side)
│   ├── section_*.md             # 3-agent verified merge per section
│   ├── UNDERSTANDING_LEVELS.md  # L1 / L1.5 / L2 / L3 definitions + roadmap
│   ├── ARCHITECTURE.md          # scaling design + v0.2.4 priority bands
│   ├── FAILURE_MODES.md         # top-5 + hidden modes
│   ├── INNOVATION_LOG.md        # candidate A-X catalogue (B/R/S/T/U/V/W/X implemented)
│   ├── AUDIT_PROVENANCE.md      # round 1-7 disclosure + governance honest revision
│   └── cold_start_evidence.md   # multi-vendor cold-start run log (v0.7.4 weekly auto-append)
├── tests/                 # CI validation (204+ cases — count tracked by tests/test_validation.py::test_documented_test_count_matches_collected)
│   ├── test_validation.py / test_merkle.py
│   ├── test_verify_urls.py / test_verify_identifiers.py
│   ├── test_archive_evidence.py / test_cold_start_runner.py
│   └── cold_start/              # multi-vendor L1 fixtures (v0.7.4)
│       ├── README.md / prompt.txt / expected_5_block_structure.md
│       └── run_cold_start.py    # stdlib-only Anthropic Messages API client
├── .github/workflows/
│   ├── ci.yml                       # per-commit structural + Merkle + URL syntax + identifier offline + render + MCP smoke
│   ├── cold_start_weekly.yml        # weekly Sunday 03:00 UTC L1 verification (advisory, secret-gated)
│   └── innovation_heartbeat.yml     # monthly 1st 02:30 UTC issue auto-open (silent-death detector)
├── LICENSE                # MIT
├── NOTICE                 # Citation policy + neutrality statement
├── CONTRIBUTING.md        # PR rules (evidence-only label gate)
└── CODE_OF_CONDUCT.md     # Contributor Covenant 2.1
```

## What changed in v0.7.x (2026-05-07)

| version | item | rationale |
|---|---|---|
| v0.7.0 | `archive_url` schema field + `tools/archive_evidence.py` + `docs/cold_start_evidence.md` (was 5-way dead reference) + stale-count fix | groundwork for Round-4-7 fabrication root-cause closure |
| v0.7.1 | `tools/verify_identifiers.py` (DOI structural + ISBN-10/13 ISO 2108 checksum) | closes Round-7 Kato-ISBN fabrication class structurally |
| v0.7.2 | `role` enum on entity schema (Pop / Sawin = `background_reference`; Grothendieck = `historical_foundation`) + Person edge-or-role invariant | closes architect-flagged 0-edge orphan check without fabricating proponent edges |
| v0.7.3 | `.github/workflows/innovation_heartbeat.yml` (monthly auto-issue) | closes silent-death class for `INNOVATION_LOG.md` |
| v0.7.4 | `tests/cold_start/run_cold_start.py` (Anthropic API) + `cold_start_weekly.yml` | begins multi-vendor L1 evidence; previously 0 real runs |
| v0.7.5 | 16 `lean/IutStatus/<Module>.lean` per-section files + Basic.lean orchestrator + `lean_module` resolution rule | closes architect-flagged G8 module-file drift |
| v0.7.6 | ARCHITECTURE.md band table updated with v0.7 status; UNDERSTANDING_LEVELS.md roadmap row sync; this README block | documentation coherence after 6 incremental releases |
| v0.7.7 | Round 8 user-override audit close (1 CRITICAL + 5 HIGH + 4 MEDIUM): docs prose-scrub class identified; `docs/section_8_disputes_timeline.md` ISBN scrub miss; `data/context.jsonld` archive_url + role mapping; cold_start runner repairs (model id + system role + IRI check + BLOCK pattern); validate.py surname full-name match; verify_identifiers Unicode dash | systemic prose-retention class surfaced |
| v0.7.8 | Round 9 user-override audit close (4 CRITICAL + 9 HIGH + 6 MEDIUM): 6-release stale auto-gen `docs/disputes.md` + `timeline.md` + `overview.md` regenerated + CI diff gate; BLOCK_LABEL_PATTERNS 2-tier (header + proximity) repaired natural-prose regression introduced by v0.7.7; `mcp/server.py` exposes `archive_url` / `role` / `specific_support` / `lean_stub` (was silently dropping 5 fields); `loaders/python_minimal.py` Claim dataclass `specific_support`; `LICENSE` short-form → MIT official 11264-byte text; `tools/render_md.py` surfaces archive_url + specific_support; CI gains MCP initialize handshake + lake build advisory + render-diff gate; ISBN regression generalised to PROSE_SCRUB_INVARIANTS; ARCHITECTURE.md schemas/v0.{2,3} 6 dead refs honestly repositioned as planned-not-yet | drift-zero contract repaired across consumer chain (loader → MCP → render); audit-process meta-finding: per-release mini-audit recommendation |
| v0.7.9 | **Structural close of R4-R9 systemic root cause** — `tools/property_audit.py` (323 lines) enumerates every schema property and verifies propagation through L1 (context.jsonld) / L2 (loaders/python_minimal.py) / L3 (mcp/server.py) / L4 (tools/render_md.py, opt-in via per-property allow-list); indent-bounded source slicing handles nested `_dispatch_tool` branches; `tests/test_property_audit.py` (9 cases) pins clean-repo + L1/L2/L3 drift-injection + policy contract; CI gains `Property propagation audit` blocking step; first audit run uncovered `_claim_to_json` silently dropping `type` field (entity-side emitted, claim-side did not) — fix shipped in same commit; `docs/PROPERTY_PROPAGATION.md` (new) gives the human-readable checklist; `CONTRIBUTING.md` PR rule #3 + #5 reference both. | the R4-R9 multi-layer-drift class can no longer survive a green build |
| v0.7.10 | **Architect-Sec-8 + HIGH-2 deferred coverage close + governance machinery** — `tests/test_render_md.py` (24 cases) pins per-render-function contract (overview / disputes / timeline / `_render_claim` neutrality + sort + archive_url + specific_support surfaces); `tests/test_loader.py` (23 cases) pins loader dataclass + factory + graph queries + frozen invariant + live-data smoke; `tests/test_context_bidirectional.py` (12 cases) verifies reverse-direction (every `@context` term has a justification: schema property / JSON-LD reserved / type alias / namespace prefix), structural well-formedness (string-or-object, `@id` presence, `@type` and `@container` allow-list), no-collision (no two properties expand to same IRI), and round-trip expansion of selected canonical IRIs; `tools/innovation_explorer.py` (new, 305 lines) is the structural sentinel for `INNOVATION_LOG.md` (open-slot health, status discipline, Implemented-needs-evidence, no-duplicate-letter, optional `--strict-paths`); `tests/test_innovation_explorer.py` (9 cases) including emphasis-wrapped + Subsumed status recognition; `.github/workflows/pr_label_gate.yml` mechanically enforces CONTRIBUTING.md PR rule #1 (closes governance honest-revision gap); 6 new CI steps wire all of the above. | drift-zero contract is now fully tested at every layer; INNOVATION_LOG silent-degradation (status-claim drift) blocked structurally |
| v0.7.11 | **NDL Search API integration for verify_identifiers.py** — Round-7 fabricated Kato ISBN (`978-4-04-110262-7`) was caught only by maintainer review; the existing `--check-isbn` flag relied on Open Library which has sparse Japanese-language coverage. v0.7.11 adds a fallback to NDL (National Diet Library) OpenSearch API for ISBNs in the Japanese registration group (978-4-/4-…). Open Library 404 + NDL 0-hits on a Japanese ISBN now returns `invalid` (the R7-class fabrication signal), while NDL transport flake preserves `unresolved` (no false-positive on network failure). Non-Japanese ISBNs are unchanged. New `_is_japanese_isbn` helper + `_query_ndl_isbn` (stdlib-only XML substring match against `<openSearch:totalResults>`). Tests cover all 6 paths via mocked urlopen (jp+OL2xx → alive; jp+OL404+NDL_hit → alive; jp+OL404+NDL0 → invalid; jp+OL404+NDL_transport_error → unresolved; non-jp+OL404 → unresolved without NDL call; jp+OL2xx → no NDL call). | R7-class Japanese-ISBN fabrication is now an automatable signal; checksum-only validation no longer suffices for jp books |
| v0.7.12 | **Wayback archive_url passive-lookup population (data rotation)** — `tools/archive_evidence.py --network --lookup --apply` against Wayback Availability API for every evidence + timeline record with a primary URL. **Empirical: 3 / 55 with-URL records had a pre-existing snapshot** (5.5 % hit rate, on `evidence:IUTchII_2012`, `evidence:Joshi_FAQ_2025_11`, `event:2025_11_joshi_faq`); 52 records returned "no snapshot available" — meaningful signal that the IUT corpus is largely *not* on the open archival web. Merkle root rotated **`6736c24a…` → `c516d24f28d9686f6632d147f714bd855e26533701b3e63b366a825b6af63cbd`** (first rotation since v0.5.2 consumer-chain repair). `docs/{overview,disputes,timeline}.md` regenerated to surface the new archive links. Drift-zero contract preserved (property_audit green). The 52 missing-snapshot records are deferred to v0.7.13 Save Page Now sweep. | passive-lookup population is now data; URL rot for the 3 archived records is detectable post-hoc; the empirical 5.5 % hit rate justifies a future SPN-based active-archive sweep |
| v0.7.13 | **Round 10 closure** — README.md scrub-scope expanded to repo-root *.md (Joshi v2 fictional clickable link survived 5 releases because R8 scrub test only scanned docs/); `mcp/server.py` `iut_timeline` re-emitted `type` field (silently dropped because the substring-based property_audit was fooled by the MCP envelope `{"type": "text"}`); `tools/property_audit.py` upgraded from substring-match to AST-based payload-dict-key extraction; `mcp/server.py` main loop refactored into `_handle_jsonrpc()` with proper §6 batch / §1.2 notification / §4.4 non-object handling; `schemas/timeline.json:url` added `format: uri` + `pattern: ^https?://` (closes javascript:/data:/file: injection); `docs/section_2/8_*.md` IRI typos repaired; new `test_section_docs_iris_resolve_in_data` for structural section-IRI gate. | meta-failure (audit gates themselves drifting) closed at the per-release mini-audit cadence |
| v0.7.14 | **Round 11 closure** — Round 10's "gate-drift class closure" claim was empirically refuted on 3 of 4 layers by independent Round-11 sub-agents. Fixes: `tests/test_validation.py:294` IRI regex char-class extended to `[A-Za-z0-9_.\-]+` (Round-10 missed `iut:Cor.3.12`, the central disputed corollary, cited 28 times across 6 section docs); `schemas/evidence.json` `url`/`archive_url` gained `^https?://` pattern (Round-10 hardened only `timeline.json`); `schemas/timeline.json:archive_url` ditto for parity; `tools/property_audit.py` `_extract_payload_dict_keys` narrowed from "any-Dict-with-id-key" (sibling-pollution + dict-comp + dict()-Call bypass) to "ast.Assign target named `payload`/`payload_list`" + "ast.Return of ast.Dict literal"; `mcp/server.py:_handle_jsonrpc` added `jsonrpc` version validation (§4), `params: null` rejection (§4.2), nested-batch rejection (§6); `mcp/server.py` new `_validate_tool_arguments` enforces declared `inputSchema.pattern`/`required`/`type` at runtime (R10 was declarative-only); 13 "commit pending" placeholders in `INNOVATION_LOG.md` replaced with actual commit SHAs; `data/context.jsonld` `proponents`/`actors` carry explicit literal-only `@language` documentation; `tools/archive_evidence.py` netloc check upgraded from `startswith("http://web.archive.org/")` to `urllib.parse.urlparse(...).netloc == "web.archive.org"`; `.github/workflows/ci.yml` Python matrix expanded to 3.10/3.11/3.12; `data/timeline.json` 3 synthetic Jan-1 dates gained explicit `date_precision: "year"` field with schema support; `tools/innovation_explorer.py` `COMMIT_REF_RE` length-bounded 7-12 to prevent merkle-root masquerade; `tools/render_md.py` URL emission gains scheme allowlist defense-in-depth; new tests added for every Round-11 finding (regression-protected). 9 new CI test cases. | per-release mini-audit cadence is now official; gate-drift class is a recurring (not closed) class with dedicated Round-N rotation guards |

## Citation policy

- We quote **statements** (theorems, corollaries, definitions) which
  are not subject to copyright. Each quotation carries DOI + paper +
  section + page number + URL.
- We do **not** redistribute original PDFs, figures, or prose passages
  from copyrighted sources.
- We treat this as fair use under US 17 U.S.C. §107 and Japanese
  Copyright Act Article 32.
- Take-down requests: open a GitHub Issue or contact the repository
  owner via GitHub.

## Cryptographic provenance

The file `data/merkle_root.txt` contains a SHA-256 Merkle root over
every record in `data/{entities,claims,evidence,timeline}.json`,
computed by `tools/build_merkle.py`. CI verifies the committed root
matches the recomputed root (`tools/verify_merkle.py`); a mismatch
fails the build.

External auditors can independently verify any past state of the
graph by checking out the corresponding git commit and running:

```bash
python tools/verify_merkle.py
```

Combined with git's own commit hash chain, this gives a two-layer
cryptographic anchor: git commits prove "this was the state at this
time"; the Merkle root proves "no record was tampered with".

When LANA produces formal `theorem` bodies in 2026-Q3+, the Merkle
root at the moment of formalization can be embedded in the Lean
artefact, giving a cryptographic anchor between the unformalized
JSON-LD and the formalized Lean.

## Versioning

Semantic Versioning. v0.x is unstable; the JSON-LD `@context` may
break. v1.0 is gated on either:
- LANA mid-report (2026-07-17) confirming or refuting the dispute, OR
- one full year of stable claim graph (~2027-05).

## Generic reusability

The schema and protocol in this repository are deliberately
domain-generic. The IUT case is one instance of a broader pattern:
**multi-perspective preservation of unresolved disputes**. The same
infrastructure can be adapted to other unresolved scientific or
mathematical controversies by:
1. Forking the repository
2. Renaming the IRI namespace (`iut:` → `your_domain:`)
3. Replacing `data/entities.json` and `data/claims.json` content
4. Keeping `schemas/*.json`, `LLM_CONTEXT.md` §3 protocol, and
   `mcp/server.py` shape unchanged

The 5-block answer template, the `position`/`stance`/`peer_review_status`
enums, and the `counters`/`supports`/`relates_to` edge types are
intended as the stable invariants.

See `LLM_CONTEXT.md` §8 for the full reusability checklist.

## Known limitations (v0.x)

- Some entity records have `informal_md: null` because the prose
  document does not yet exist. LLMs encountering null `informal_md`
  must follow the **decline-gracefully** protocol in
  `LLM_CONTEXT.md` §3.5; they must NOT fall back to pre-training
  prose.
- Lean 4 theorem bodies are all `sorry`. The naming aligns with the
  IRI namespace; LANA-produced formalizations can replace the bodies
  module-for-module without renaming.
- Some informal third-party objections to Joshi 2025
  (Scholze MathOverflow rebuttal, Sawin locality critique) are
  reported in community channels but lack stable URLs verifiable as
  of 2026-05-06; they are noted in
  `claim:joshi_2025_alternative.status` but not registered as
  evidence records until URLs stabilize.

## License

- Code, schemas, JSON-LD structure, Lean stubs, MCP server: **MIT**
- Quoted mathematical statements: not copyrighted (academic convention)
- Quoted prose passages from copyrighted papers: fair-use educational excerpt

## See also

- [LANA project](https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f) — Lean 4 formalization (2026-03-31, ongoing)
- [Mochizuki, "On the Formalization of IUT" (2026-04)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20(2026-04).pdf)
- [Joshi, arXiv:2505.10568 v1 (2025-04-29)](https://arxiv.org/abs/2505.10568v1)
- [Joshi, "FAQ on Mochizuki–Joshi" (2025-11)](https://math.arizona.edu/~kirti/joshi-mochizuki-FAQ.pdf)
- [Scholze-Stix, "Why abc is still a conjecture" (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [Mochizuki, "Report on Discussions" (2018-09)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Rpt2018.pdf)
- [Yamashita, "A proof of abc conjecture after Mochizuki" (2024-06)](https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2024Jun25.pdf)
- [nLab: inter-universal Teichmüller theory](https://ncatlab.org/nlab/show/inter-universal+Teichm%C3%BCller+theory)
