# AUDIT_PROVENANCE.md — honest record of audit independence

The architecture documents (`UNDERSTANDING_LEVELS.md`, `ARCHITECTURE.md`,
`FAILURE_MODES.md`, this `INNOVATION_LOG.md` entries) were produced by
multiple "audit rounds" run inside a single LLM family. This file
records that fact transparently so any reader can calibrate the level
of independence behind the design.

## Disclaimer (top of every audit doc)

> All audit rounds for this repository, through commit `a0de80e`
> (v0.7.12) and Round 10 closure at v0.7.13, were produced inside a
> single Claude (Anthropic) family session, by sub-agents with shared
> model weights. **Independence across LLM vendors is not established
> at this time.** Multi-vendor evidence is the responsibility of the
> L1 cold-start CI matrix in `docs/cold_start_evidence.md`; that file
> is the source of truth for independence claims, not the audit
> documents themselves. Round 10 (v0.7.13) was the first round to
> empirically falsify the v0.7.9 / 9.5 claim that the property-drift
> class was "structurally closed" — `iut_timeline` was silently
> dropping the `type` field while the substring-based property_audit
> kept reporting OK, because the MCP response envelope
> `{"type": "text"}` shared the schema property name. The fix
> upgrades property_audit to AST-based payload-dict-key extraction.

## Round table

| Round | Date | Trigger | Agents | Same conversation? | Independence claim | Critical defect found |
|---|---|---|---|---|---|---|
| 1 | 2026-05-06 | initial design | analyst + architect + critic + premise-monitor + tracer + 10-trial verifier (4–6 agents) | Same Claude session | None — single LLM family | structural foundations |
| 2 | 2026-05-06 | "ここさらに固めて" (further harden) | analyst + architect + critic | Same Claude session | None — same family | 5 hidden failure modes |
| 3 | 2026-05-06 | "ここさらに固めて" (further harden) | architect + analyst + critic | Same Claude session | None — same family. Round 3 explicitly identified the independence gap. | 3 internal inconsistencies + 1 numerical-premise drift |
| 4 | 2026-05-06 | user override「欠陥や漏れがないか徹底的にチェック前提すら疑って」 | analyst + architect + critic | Same Claude session | None — same family | tempered_rigidity misattribution / paper duplication / SS silent error / verbatim cap mismatch |
| 5 | 2026-05-06 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **Joshi v2 (2026-05-02) fictional evidence** + §1.4 verbatim mis-quote + 6 ATS arXiv IRI drift |
| 6 | 2026-05-07 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **Woit blog dating drift (1.5y)** + timeline url gap + Joshi URL canonical + verbatim cap doc sync |
| 6.5 | 2026-05-07 | systemic root-cause repair | architect + analyst | Same Claude session | None — same family | URL liveness verifier added (closes round 4-6 systemic gap: validate.py never compared graph URLs to external reality) |
| 7 | 2026-05-07 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **Kato ISBN fabrication (978-4-04-110262-7 → 978-4-04-400417-0)** + PRIMS issue ID drift (/249→/1507, 2 records) + Frobenioids_I URL filename typo + 2018 SS visit actors over-listed (Yamashita removed) + governance gate honest revision |
| 8 | 2026-05-07 | user override (same phrase, after Round 7 analyst recommended skip) | analyst + architect + critic | Same Claude session | None — same family | **fabricated ISBN scrub miss in `docs/section_8_disputes_timeline.md`** (R7 thought it was closed; data/ was repaired but docs/ prose retained the fabrication) + placeholder model id `claude-opus-4-5` (not real) + JSON-LD context.jsonld missing v0.7.0/v0.7.2 mappings + cold-start IRI check structurally false-fails + Wayback URL scheme drift + 6 minor pattern-matching gaps |
| 9 | 2026-05-07 | user override (same phrase) | analyst + architect + critic | Same Claude session | None — same family | **`docs/disputes.md` + `timeline.md` + `overview.md` 6-release stale auto-generated artefacts** (R6/R7 fix values absent at 4 sites — PRIMS /249 ×3, Frobenioids URL typo, 2018 SS visit Yamashita actor — survived 6 release boundaries despite v0.7.6 "documentation coherence pass" claim) + **`mcp/server.py` silently dropped 5 fields** (`archive_url` ×2, `role`, `specific_support`, `lean_stub`) and `loaders/python_minimal.py` Claim dataclass missing `specific_support` (drift-zero contract violation across consumer chain) + **v0.7.7 BLOCK_LABEL_PATTERNS over-tightened** (false-positive close → false-negative regression for natural-prose responses) + **`LICENSE` short-form** (Apache-2.0 §4.a violation; full text required for SPDX `Apache-2.0` identification) + 2 hand-written prose retentions (`section_8` 2018 SS visit Yamashita actor + `section_6_cor_3_12.md:421` Joshi v1+v2) + ARCHITECTURE.md 6 dead schemas/v0.{2,3} refs (Round 8 commit message claimed "6 eliminated" but 3 remained); meta-finding: 8 connected releases in 1 day exceeded audit cadence, batch-end audit detected systemic but per-release mini-audit was recommended for Round 9+ |
| 9.5 | 2026-05-07 | systemic root-cause repair (post-Round-9, no new audit) | architect + analyst | Same Claude session | None — same family. v0.7.9 ships `tools/property_audit.py` + CI gate to close the R4-R9 multi-layer-drift class structurally rather than via further per-round detection. Empirical validation: the audit caught a fresh CRITICAL on its first execution (`_claim_to_json` silently dropped the `type` field — entity serializer emitted, claim serializer did not). Fix shipped in the same commit. | `_claim_to_json` `type` field drop (R9-class drift that survived R9); structural gate now blocks this class going forward |
| 9.6 | 2026-05-07 | deferred-finding cleanup (Architect Sec-8 + HIGH-2 + governance honest-revision) | n/a (test + governance machinery, not an audit round) | Same Claude session | None — same family. v0.7.10 closes three deferred items: (i) `tools/render_md.py` and `loaders/python_minimal.py` had no direct unit tests (Architect Sec-8); (ii) `data/context.jsonld` had only forward-direction coverage from property_audit (HIGH-2); (iii) CONTRIBUTING.md PR rule #1 had no machinery (Round 7 honest-revision). | n/a — no new finding; repairs Architect Sec-8 / HIGH-2 / Round-7 governance gaps. Test count 100 → 168. |
| 9.7 | 2026-05-07 | deferred-finding cleanup (R7 jp-ISBN fabrication-class + v0.7.0 schema population) | n/a (resolver extension + data rotation, not an audit round) | Same Claude session | None — same family. v0.7.11 extends `verify_identifiers.py` with NDL Search API fallback for Japanese-group ISBNs; v0.7.12 runs a passive Wayback Availability lookup against the live graph and applies the 3 found snapshots (5.5 % hit rate of with-URL records). Merkle root rotated `6736c24a…` → `c516d24f…`. | n/a — no new finding; closes R7 fabrication-class gap (jp ISBN now machine-checkable) + v0.7.0 archive_url empty-state. 52 records deferred to v0.7.13 Save Page Now sweep. |
| 10 | 2026-05-07 | user override「3エージェントで欠陥や漏れがないか徹底的にチェック前提すら疑って修正したり改善したり」(after Round 9.7 deferred-finding closure) | analyst + architect + critic (independent prompts, no cross-pollination) | Same Claude session | None — same family. Three independent sub-agents converged on overlapping CRITICAL findings (multiple agents independently surfaced the README Joshi v2 fabrication regression and the MCP `type`-field drop), strengthening confidence beyond single-agent variance. | **README.md:276 Joshi v2 fictional URL** (R5 closure regression — `arXiv:2505.10568v2 (2026-05-02)` clickable link survived 5 release boundaries because `test_audit_known_corrections_not_in_docs` only scanned `docs/`, not repo-root `*.md`) + **`mcp/server.py` iut_timeline silently drops `type` field** (R9.5 closure regression — substring-based property_audit was fooled by the MCP envelope `{"type": "text"}`, so the same drift class R9.5 claimed to "structurally close" survived in a different emitter) + **`schemas/timeline.json` url field had no format/scheme constraint** (`javascript:alert(1)` / `file:///` / `data:` were silently accepted; XSS surface for any future renderer) + **MCP server JSON-RPC 2.0 spec violations** (batch crash, notification responses sent against §4.1, non-object root crash) + **`docs/section_2_hodge_theater.md:83` IRI typo** (`iut:Theta-link, iut:log-link` — data/ uses snake_case `theta_link, log_link`) + **`docs/section_8_disputes_timeline.md:188` Woit IRIs reference 2025 records that don't exist in data/** (only 2024 records exist; this is the same R5/R6/R8/R9 docs-cite-nonexistent-IRI class re-surfacing in curated section docs which had no structural gate, so v0.7.13 added `test_section_docs_iris_resolve_in_data`); meta-finding: per-release mini-audit cadence is now operationally established and continues to surface real CRITICAL each round. |
| 11 | 2026-05-07 | user override「欠陥や漏れがないか徹底的にチェック前提すら疑って」(after Round 10 v0.7.13 closure) | analyst + architect + critic (independent prompts, instructed to *attempt to refute* the Round-10 closure claim) | Same Claude session | None — same family. The Round-10 INNOVATION_LOG candidate-EE claim that "Round 10 closes the gate-drift class" was **empirically refuted on 3 of 4 layers** by independent sub-agents. The "gate-drift class" remains a recurring (not closed) class, requiring per-release rotation guards. | **`tests/test_validation.py:294` IRI gate regex `[A-Za-z0-9_]+` excludes `.`** so `iut:Cor.3.12` (the central disputed corollary, cited 28 times across 6 section docs) was silently invisible to the Round-10 section-IRI gate the very release after it was added (regex char-class extended to `[A-Za-z0-9_.\-]+`) + **`schemas/evidence.json` `url`/`archive_url` lacks the `^https?://` pattern** that Round 10 added to `schemas/timeline.json` (half-fix — `javascript:alert(1)` / `data:` / `file:` still slipped through schema validation for evidence records, propagating to render_md → docs Markdown links) + **`tools/property_audit.py:_extract_payload_dict_keys` "id"-discriminator bypassed** by 3 attack vectors (sibling-dict pollution: any docstring sample / cache / helper dict containing `"id"` would mask a real payload omission; dict comprehension `{k: v for k, v in [...]}` returns no `ast.Dict` literal at the AST level; `dict(id=…, type=…)` Call form similarly) — fix narrows to `ast.Assign` whose target name is in `PAYLOAD_VARIABLE_NAMES` + `ast.Return` of an `ast.Dict` literal + **`mcp/server.py:_handle_jsonrpc` `params: null` crashes server** with `AttributeError: 'NoneType' object has no attribute 'get'` (Round 10 added non-dict request rejection but missed the `params` field validation; §4.2 says params, when present, MUST be Object or Array — null is invalid) + **`mcp/server.py` accepts `jsonrpc: "1.0"` and `jsonrpc` missing** (§4 mandates the literal "2.0"; Round 10 added every other §6/§1.2/§4.1/§4.4 check but skipped §4 itself) + **`mcp/server.py` `inputSchema.pattern` declared but not enforced** at runtime (declarative-only — `{"iri": ["array"]}` crashed loader with -32603 internal error rather than the expected -32602 invalid params; `{"iri": "iut:abc; DROP TABLE"}` returned OK with null) + **`mcp/server.py:_handle_jsonrpc` accepts nested batches** (§6 forbids; v0.7.13 silently consumed `[[…]]` rather than -32600 invalid request) + **`README.md` release notes table lacked v0.7.13 row** (internal contradiction with `INNOVATION_LOG.md` candidate EE marking v0.7.13 as Implemented) + **`docs/INNOVATION_LOG.md` had 13 "commit pending" placeholders** for already-shipped commits (Round 10 deferred to v0.7.14) + **`tools/innovation_explorer.py:COMMIT_REF_RE` `[0-9a-f]{7,40}`** matched the 64-char Merkle root, allowing future "commit pending" replacement to substitute the merkle root literal as evidence (length-bounded to short SHA `7-12` OR full SHA `40` to disambiguate) + **`tools/archive_evidence.py:200,235` host check is `startswith("http://web.archive.org/")`** prefix-only — would silently accept `web.archive.org.evil.com/…` redirects (upgraded to `urlparse(...).netloc.lower() == "web.archive.org"`) + **`.github/workflows/ci.yml` Python 3.12 only** despite README claiming 3.10+ (matrix expanded to 3.10/3.11/3.12) + **`data/timeline.json` 3 synthetic Jan-1 dates** (1985 / 2008 / 2009) — fabrication-class same as R7 jp-ISBN, gained explicit `date_precision: "year"` field with schema support; **AST sibling-pollution counter-example test** added to drift-injection suite. Test count 189 → 201. Merkle root rotated `c516d24f…` → `e6d1d1b5…` (timeline.json 3-record date_precision addition). meta-finding: Round 10's "gate-drift closure" claim was overconfident. The honest framing: per-release mini-audit cadence is the operating norm; each release ships with at least one Round-N CRITICAL surface, and the structural gates are repeatedly **narrow patches** that require adversarial-form testing to hold. |

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

Original gate (v0.2.4 — formally maintained but **functionally bypassed
by user override in rounds 4 / 5 / 6 / 7**):

> Audit rounds are paused indefinitely until at least one of the
> following triggers fires:
> (a) actual non-Claude vendor cold-start run; (b) external reviewer
> report; (c) v0.3 schema-changing PR.

**Honest revision (v0.6.1, after round 7 analyst critique)**: the gate
above is preserved as the long-term ideal but does NOT actually block
audit rounds in practice. The de-facto governance is:

- **User override is the operative gate**: when the maintainer types
  「欠陥や漏れがないか徹底的にチェック前提すら疑って」 or equivalent,
  a new audit round runs.
- Each user-override round is recorded in the corresponding patch
  commit message ("Round N was permitted by user override of the
  indefinite pause set at v0.2.4").
- Rounds 4-7 each found at least one CRITICAL fabrication-class
  defect that prior rounds missed; the gate, if strictly enforced,
  would have shipped those defects.

The right reading: the original gate was a hedge against audit fatigue,
but in practice external-reality verification gaps surface faster than
multi-vendor evidence accrues. The user-override mechanism produces
healthier outcomes and is the documented operative protocol going
forward.

Original triggers (a) (b) (c) are still desirable — they raise the
quality of audits beyond Claude-family bias — but they are
**aspirations**, not gates.

## Why this gate exists

Without a real-vendor independence signal, additional Claude-only audit
rounds add documentation lines but do not increase the actual
independence of the design. Round-2 caught five hidden failure modes
that round-1 missed; round-3 caught three internal inconsistencies and
one numerical-premise drift; round-4 is forecast to be marginal at
best, NO-OP at worst, while continuing to push the meta-doc /
object-doc ratio into the red. The gate is a structural commitment,
not a polite suggestion.
