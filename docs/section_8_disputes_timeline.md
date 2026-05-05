# Section 8: disputes timeline (1985 → 2026 → 2026-07-17 PENDING)

> Curated narrative reading of `data/timeline.json` (20 events) cross-referenced with claims and evidence.
> Last verified: 2026-05-06.
> drift-zero contract: every fact is anchored to an `event:*` ID in `data/timeline.json`. Ordering is chronological; no editorial synthesis is performed. Evaluative adjectives are excluded from the narrator's voice.

## 8.1 Pre-IUT background (1985–2011)

- **1985** — abc conjecture stated by Masser and Oesterle.
  `event:1985_abc_conjecture`
- **2008** — Frobenioids I and II published. `event:2008_frobenioids` / `evidence:Frobenioids_I`
- **2009** — Étale theta function paper published. `event:2009_etale_theta` / `evidence:EtaleTheta_2009`

These three items establish the technical prerequisites cited by IUT I–IV; no claim in `claims.json` is asserted against this period.

## 8.2 IUT release (2012)

- **2012-08-30** — Mochizuki releases IUTch I–IV as RIMS preprints. `event:2012_iut_release`
  | `evidence:IUTchI_2012` DOI 10.4171/PRIMS/57-1-1
  | `evidence:IUTchII_2012` DOI 10.4171/PRIMS/57-1-2
  | `evidence:IUTchIII_2012` DOI 10.4171/PRIMS/57-1-3
  | `evidence:IUTchIV_2012` DOI 10.4171/PRIMS/57-1-4

  Two claims originate at this date:
  - `claim:mochizuki_2012_proves_abc` (stance: supportive; status: `unresolved-as-of-2026-05`; `peer_review_status: peer_reviewed`)
  - `claim:cor_3_12_neutral_statement`: existence and shape of Cor.3.12 (`iut:Cor.3.12`) as a neutral-existence statement (status: `neutral-existence-statement`)

## 8.3 First public skeptical commentary (2017)

- **2017-12-17** — Frank Calegari publishes "The ABC conjecture has (still) not been proved."
  `event:2017_calegari_blog` / `evidence:Calegari_blog_2017`
  Cited in `claim:western_majority_skeptical` (status: `ongoing-as-of-2026-05`; `peer_review_status: informal_blog`).

## 8.4 The Scholze–Stix exchange (2018)

- **2018-03-15** (date approximate per `timeline.json`) — Scholze and Stix visit RIMS in person.
  `event:2018_scholze_stix_visit` | actors: Scholze, Stix, Mochizuki, Hoshi, Yamashita
- **2018-05-01** — Mochizuki publishes Cmt2018-05.
  `event:2018_05_mochizuki_cmt` / `evidence:Cmt2018_05_Mochizuki`
- **2018-07-16** — Scholze and Stix release "Why abc is still a conjecture."
  `event:2018_07_ss_report` / `evidence:WhyABCisStillaConjecture_2018`

  Claims asserted here (all `unresolved-as-of-2026-05`; `peer_review_status: preprint_not_peer_reviewed`):
  - `claim:scholze_stix_2018_main`: Cor.3.12 reduces to a trivial inequality under harmless simplification; `counters` `claim:mochizuki_2012_proves_abc`
  - `claim:scholze_stix_2018_sub_1`: distinct copies of `iut:HodgeTheater` do not exist in the required form
  - `claim:scholze_stix_2018_sub_2`: anabelian geometry plays no essential role at the disputed step
  - `claim:scholze_stix_2018_sub_3`: commutativity of fundamental groups renders the multiradial operations trivial

- **2018-09-01** — Mochizuki publishes "Report on Discussions."
  `event:2018_09_mochizuki_response` / `evidence:Rpt2018_Mochizuki`
  `claim:mochizuki_2018_response`: the Scholze–Stix simplification is not harmless and destroys the inter-universal un-entangling structure; `counters` `claim:scholze_stix_2018_main`
  (status: `unresolved-as-of-2026-05`; `peer_review_status: self_published_preprint`)

- **2018-09-20** — Quanta Magazine article by Hartnett.
  `event:2018_09_quanta_article` / `evidence:Quanta_2018`; cited in `claim:western_majority_skeptical`

## 8.5 Publication and re-exposition (2019–2024)

- **2019-04-26** — Kato Fumiharu book published (KADOKAWA, ISBN 978-4-04-110262-7).
  `event:2019_kato_book` / `evidence:Kato_book_2019`
- **2020-04-03** — PRIMS editorial board announces acceptance of IUT I–IV.
  `event:2020_prims_acceptance`
- **2021-03-05** — IUT I–IV published in PRIMS Vol.57.
  `event:2021_prims_publication` / `evidence:PRIMS_2021_publication` DOI 10.4171/PRIMS/57-1
  `claim:prims_2021_acceptance` records this as a factual publication event (status: `factual-publication-not-verdict`).
- **2024-06-25** — Yamashita updates survey "A proof of abc conjecture after Mochizuki."
  `event:2024_yamashita_survey` / `evidence:Yamashita_2024`
  `claim:yamashita_2024_independent_exposition` records this (status: `survey-not-peer-reviewed`).
  Note per `claims.json` `fair_use_note`: "Yamashita is a Mochizuki-aligned proponent; this exposition is a re-presentation, not an independent verification."

## 8.6 Joshi reformulation (2025–2026)

- **2025-04-29** — Joshi posts "Final Report on Mochizuki–Scholze–Stix Controversy" v1 (arXiv:2505.10568v1).
  `event:2025_joshi_v1` / `evidence:Joshi_arxiv_2505_10568`
  `claim:joshi_2025_alternative`: Arithmetic Teichmuller Spaces yield a corrected framework (stance: `reformulation`; status: `preprint-not-peer-reviewed-as-of-2026-05`); `relates_to` `claim:scholze_stix_2018_main` and `claim:mochizuki_2018_response`

- **2025-10-28** — Mochizuki posts IUT progress report.
  `event:2025_mochizuki_october_report` / `evidence:Mochizuki_IUT_report_2025_10`
  `claim:mochizuki_2025_october_report`: continued defense of original framework (status: `self-published-RIMS-preprint`)
  Peter Woit's Not Even Wrong blog carries ongoing commentary.
  `claim:woit_blog_2025_skeptical` / `evidence:Woit_blog_2025` (status: `informal-blog-commentary`)

- **2026-05-02** — Joshi v2 update (arXiv:2505.10568v2).
  `event:2026_joshi_v2` / `evidence:Joshi_arxiv_2505_10568_v2`; status: `preprint-not-peer-reviewed-as-of-2026-05`

## 8.7 Formalization era (2026–)

- **2026-03-31** — LANA (Lean for ANabelian geometry) project announced by ZMC.
  `event:2026_lana_announcement` / `evidence:LANA_announcement_2026`
  actors: Commelin, Kedlaya, Hoshi, Topaz, Kato Fumiharu

- **2026-04-07** — Mochizuki, Hoshi, Yamashita, Yang post "On the Formalization of IUT: a preliminary progress report."
  `event:2026_mochizuki_formalization_report` / `evidence:Mochizuki_formalization_2026_04`
  `claim:lana_formalization_in_progress` status: "mid-report-scheduled-2026-07-17; team has articulated a specific contentious point but not yet resolved it" (`peer_review_status: project_announcement`)

- **2026-07-17 (SCHEDULED, PENDING)** — LANA mid-report.
  `event:2026_lana_midreport_scheduled`
  This event has not occurred as of `verified_at` 2026-05-06.

## 8.8 Current status (2026-05-06)

| Claim | Status |
|---|---|
| `claim:mochizuki_2012_proves_abc` | `unresolved-as-of-2026-05` |
| `claim:scholze_stix_2018_main` | `unresolved-as-of-2026-05` |
| `claim:joshi_2025_alternative` | `preprint-not-peer-reviewed-as-of-2026-05` |
| `claim:lana_formalization_in_progress` | PENDING mid-report 2026-07-17 |

No claim in `claims.json` carries status `resolved` as of 2026-05-06.

## 8.9 Deliberate exclusions

- Private correspondence before the 2018 RIMS visit (no stable URL).
- Individual SNS posts without stable archival URLs.
- RIMS workshop talks for which no published transcript is indexed.
- Wikipedia / nLab edit history (only current snapshot `evidence:nLab_IUT` is linked).

## Cross-reference

- `data/timeline.json`: 20 dated events (`event:*`)
- `data/claims.json`: 16 claims (`claim:*`)
- `data/evidence.json`: 24 evidence records (`evidence:*`)
- `data/entities.json`: concept / person / paper records (`iut:*`, `person:*`, `paper:*`)

*No editorial verdict expressed. All `unresolved-as-of-2026-05` claims remain open.*
