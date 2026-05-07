# Section 8: disputes timeline (1985 → 2026 → 2026-07-17 PENDING)

> Curated narrative reading of `data/timeline.json` (25 events) cross-referenced with claims and evidence.
> Last verified: 2026-05-06.
> drift-zero contract: every fact is anchored to an `event:*` ID in `data/timeline.json`. Ordering is chronological; no editorial synthesis is performed. Evaluative adjectives are excluded from the narrator's voice.

---

## 8.1 Pre-IUT background (1985–2011)

- **1985** — abc conjecture stated by Masser and Oesterle.
  `event:1985_abc_conjecture`
- **2008** — Frobenioids I and II published. `event:2008_frobenioids` / `evidence:Frobenioids_I` / `evidence:Frobenioids_II`
- **2009** — Étale theta function paper published. `event:2009_etale_theta` / `evidence:EtaleTheta_2009`

These three items establish the technical prerequisites cited by IUT I–IV; no claim in `claims.json` is asserted against this period.

Key concepts established: `iut:Frobenioid`, `iut:etale_theta`, `iut:mono_theta_environment`.

---

## 8.2 IUT release (2012)

- **2012-08-30** — Mochizuki releases IUTch I–IV as RIMS preprints. `event:2012_iut_release`

  | Evidence | DOI |
  |---|---|
  | `evidence:IUTchI_2012` | 10.4171/PRIMS/57-1-1 |
  | `evidence:IUTchII_2012` | 10.4171/PRIMS/57-1-2 |
  | `evidence:IUTchIII_2012` | 10.4171/PRIMS/57-1-3 |
  | `evidence:IUTchIV_2012` | 10.4171/PRIMS/57-1-4 |

  Two claims originate at this date:
  - `claim:mochizuki_2012_proves_abc` (stance: supportive; status: `unresolved-as-of-2026-05`; `peer_review_status: peer_reviewed`)
  - `claim:cor_3_12_neutral_statement`: existence and shape of Cor.3.12 (`iut:Cor.3.12`) as a neutral-existence statement (status: `neutral-existence-statement`)

  **Cor.3.12 claim chain** (load-bearing path through IUT I–III):

  ```
  iut:anabelian_geometry
    → iut:mono_theta_environment (EtTh Cor 2.19: 3 rigidities)
      → iut:HodgeTheater (IUTchI Def 3.6)
        → iut:log_theta_lattice (IUTchIII Def 1.4: non-commutative)
          → iut:multiradial_representation_thm_3_11 (IUTchIII Thm 3.11)
            → iut:Cor.3.12 (log-volume bound, Ind1+Ind2+Ind3)
              → iut:abc_conjecture (IUTchIV)
  ```

  Each step in this chain is asserted essential by one or more claims in `claims.json`. The SS dispute (`claim:scholze_stix_2018_main`) targets the penultimate step.

---

## 8.3 First public skeptical commentary (2017)

- **2017-12-17** — Frank Calegari publishes "The ABC conjecture has (still) not been proved."
  `event:2017_calegari_blog` / `evidence:Calegari_blog_2017`
  Cited in `claim:western_majority_skeptical` (status: `ongoing-as-of-2026-05`; `peer_review_status: informal_blog`).

---

## 8.4 The Scholze–Stix exchange (2018)

- **2018-03-15** (date approximate per `timeline.json`) — Scholze and Stix visit RIMS in person (5-day session, Kyoto).
  `event:2018_scholze_stix_visit` | actors: Scholze, Stix, Mochizuki, Hoshi (Round 7 audit removed Yamashita: primary sources Wikipedia + ncatlab corroborate the four named only)

  During the visit, Mochizuki acknowledged some of Scholze–Stix's simplifications regarding the description of F-circ-times-mu-prime strips (`claim:ss_simplifications_kyoto_agreement_scope`). The scope of this agreement is itself subsequently disputed.

- **2018-05-01** — Mochizuki publishes Cmt2018-05.
  `event:2018_05_mochizuki_cmt` / `evidence:Cmt2018_05_Mochizuki`
  Source: https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-05.pdf

  This document records Mochizuki's reaction to an early draft of the SS critique, providing the first written response post-visit. It is cited as supporting evidence for `claim:mochizuki_2018_response`.

- **2018-07-16** — Scholze and Stix release "Why abc is still a conjecture."
  `event:2018_07_ss_report` / `evidence:WhyABCisStillaConjecture_2018`

  **SS claim chain (all `unresolved-as-of-2026-05`; `peer_review_status: preprint_not_peer_reviewed`):**

  | Claim | About | SS assertion (short) |
  |---|---|---|
  | `claim:scholze_stix_2018_main` | `iut:Cor.3.12` | Cor.3.12 reduces to trivial inequality under harmless simplification |
  | `claim:scholze_stix_2018_sub_1` | `iut:HodgeTheater` | Distinct copies of HT do not exist in required form |
  | `claim:scholze_stix_2018_sub_2` | `iut:Cor.3.12` | Anabelian geometry plays no essential role at disputed step |
  | `claim:scholze_stix_2018_sub_3` | `iut:multiradial_algorithm` | Fundamental-group/geometry equivalence renders operations trivial |
  | `claim:ss_canonically_same_strips` | `iut:F_circ_theta_strip` | F-circ-times-mu-prime strips are canonically the same on both sides |
  | `claim:ss_global_realified_canonical_trivial` | `iut:global_realified_frobenioid` | Global realified Frobenioids always canonically trivial via gamma_can |
  | `claim:ss_global_realified_elementary` | `iut:degree_function` | Global realified Frobenioid equivalent to ordered 1-dim R-vector spaces |
  | `claim:ss_j_squared_monodromy_inconsistent` | `iut:Cor.3.12` | j-squared scalars produce monodromy inconsistency in diagram |
  | `claim:ss_o_l_squared_blurring_useless` | `iut:Cor.3.12` | Required blurring is O(l-squared), rendering inequality useless |
  | `claim:ss_log_link_naturally_equivalent_to_identity` | `iut:log_link_construction` | log endofunctor naturally equivalent to identity |

  **SS analytical scope boundary:** SS 2018 (10 pp, PDF-verified 2026-05-06) does not analyze: Theta-gau-link, log-theta-lattice non-commutativity, Thm 3.11 construction, Ind2 two-component decomposition, mono-theta 3 rigidities (EtTh Cor 2.19), F-pm-ell symmetry, F-star-l symmetry, procession Ind1 reduction, log-Kummer correspondence construction. These are out of SS analytical scope, not denied by SS.

- **2018-09-01** — Mochizuki publishes "Report on Discussions."
  `event:2018_09_mochizuki_response` / `evidence:Rpt2018_Mochizuki`
  `claim:mochizuki_2018_response`: the SS simplification is not harmless and destroys the inter-universal un-entangling structure; `counters` `claim:scholze_stix_2018_main`
  (status: `unresolved-as-of-2026-05`; `peer_review_status: self_published_preprint`)

  **Mochizuki counter-claim chain (all `unresolved-as-of-2026-05`):**

  | Claim | About | Mochizuki assertion (short) |
  |---|---|---|
  | `claim:mochizuki_2018_response` | `iut:Cor.3.12` | SS simplification destroys inter-universal structure |
  | `claim:mochizuki_poly_iso_not_canonical` | `iut:F_circ_theta_strip` | Full poly-iso not reducible to canonical iso; sides inhabit distinct ring structures |
  | `claim:mochizuki_alien_copies_essential` | `iut:alien_arithmetic_holomorphic_structure` | Ring structure "obliterated" across inter-universal wall (IUTchI Rem 3.9.4) |
  | `claim:mochizuki_anabelian_essential` | `iut:absolute_anabelian` | Mono-anabelian framework allows inter-HT inspection |
  | `claim:mochizuki_frobenioid_essential` | `iut:frobenioid_axioms` | Frobenioid theory essential, not decorative |
  | `claim:mochizuki_global_realified_essential` | `iut:global_realified_frobenioid` | Global realified Frobenioid essential via FrdII Thm 5.5-iii reconstructibility |
  | `claim:mochizuki_theta_gau_link_essential` | `iut:theta_gau_link` | Theta-gau-link essential (outside SS scope) |
  | `claim:mochizuki_log_theta_lattice_noncommutative` | `iut:log_theta_lattice` | Log-theta-lattice non-commutative (IUTchIII Rem 1.4.1) |
  | `claim:mochizuki_ind2_two_components` | `iut:Ind2` | Ind2 decomposes into Z-times + Oμ; Oμ insulation protects Kummer theory |
  | `claim:mochizuki_ind3_log_volume_precise` | `iut:Ind3_log_volume_absorption` | Ind3 upper-semi-compatible; log-volume compatibility is precise (Prop 3.9-iv) |
  | `claim:mochizuki_procession_essential` | `iut:procession` | Procession reduces Ind1 from (l-pm)^(l-pm) to (l-pm)! |
  | `claim:mono_theta_three_rigidities_essential` | `iut:mono_theta_cyclotomic_rigidity` | All 3 mono-theta rigidities essential; bi-theta fails discrete rigidity |
  | `claim:mochizuki_multiradial_thm_3_11_essential` | `iut:multiradial_representation_thm_3_11` | Thm 3.11 is load-bearing; SS critique targets downstream Cor.3.12 conclusion |

- **2018-09-20** — Quanta Magazine article by Hartnett.
  `event:2018_09_quanta_article` / `evidence:Quanta_2018`; cited in `claim:western_majority_skeptical`

---

## 8.5 Publication and re-exposition (2019–2024)

- **2019-04-26** — Kato Fumiharu book published (KADOKAWA, ISBN 978-4-04-400417-0).
  `event:2019_kato_book` / `evidence:Kato_book_2019`

- **2020-04-03** — PRIMS editorial board announces acceptance of IUT I–IV.
  `event:2020_prims_acceptance`

- **2021-03-05** — IUT I–IV published in PRIMS Vol.57.
  `event:2021_prims_publication` / `evidence:PRIMS_2021_publication` DOI 10.4171/PRIMS/57-1
  `claim:prims_2021_acceptance` records this as a factual publication event (status: `factual-publication-not-verdict`).

  Note: IUTch I–IV share a single publication date (2021-03-05) in PRIMS Vol.57 No.1/2. Each paper carries an individual DOI (10.4171/PRIMS/57-1-1 through 57-1-4); the journal page lists them as a special double issue. The preprint URLs at kurims.kyoto-u.ac.jp date to 2012-08-30.

- **2024-03-24** — Mochizuki posts revised "Essential Logical Structure of IUT" with comprehensive revision list.
  `event:2024_03_essential_logical_structure_update` / `evidence:Essential_Logical_Structure`
  Source: https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html (marked-up version also available)
  `claim:essential_logical_structure_reference` records this document.
  Note: the papers-english.html page marks this item "NEW!! (2024-03-24)"; earlier revision dates include 2022-05-18 per Semantic Scholar metadata.

- **2024-03-30** — Mochizuki posts report on Joshi preprint series with supplementary explanations.
  `event:2024_03_mochizuki_report_on_joshi`
  Source: https://www.kurims.kyoto-u.ac.jp/~motizuki/Report%20on%20a%20certain%20series%20of%20preprints%20(2024-03).pdf
  This document preceded the Joshi v1 arXiv upload (2025-04-29) and directly addresses the Arithmetic Teichmuller Spaces reformulation series. Relates to `claim:joshi_2025_alternative`.

- **2024-06-25** — Yamashita updates survey "A proof of abc conjecture after Mochizuki."
  `event:2024_yamashita_survey` / `evidence:Yamashita_2024`
  `claim:yamashita_2024_independent_exposition` records this (status: `survey-not-peer-reviewed`).
  Note per `claims.json` `fair_use_note`: "Yamashita is a Mochizuki-aligned proponent; this exposition is a re-presentation, not an independent verification."

  Yamashita also maintains the IU-FAQ document (`evidence:Yamashita_IUFAQ_2024`,
  https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/IUfaq_en2.pdf); the asserted_at date in evidence.json is `2024-01-01` (approximate; precise revision date not recovered from PDF metadata as of 2026-05-06 verification).

---

## 8.6 IUT Summit 2025 and continued activity

- **2025-03-17–20** — IUT Summit 2025, hybrid workshop at RIMS.
  `event:2025_03_iut_summit`
  Source: https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT_Summit_2025/program.html
  Organizers: Hoshi (RIMS), Mochizuki (RIMS).
  Key sessions:
  - Porowski: "On the essential logical structure of IUT" parts I–III (March 17)
  - Hoshi: "Galois sections of hyperbolic polycurves" I–II (March 18)
  - Minamide: "On the essential logical structure of IUT" parts IV–VI (March 19)
  - Yamashita: "On tilts and Inter-universal Teichmüller theory" (March 20)
  - Kedlaya: "Tilting and Fargues-Fontaine curves" (March 20)
  This event is the first large-scale public exposition of the Essential Logical Structure series (IUT I–VI). No claim in `claims.json` is asserted against this event specifically.

- **2025-04-27** — Mochizuki presents "Tch Dilations of Varying Hues" at ICMS Scotland workshop.
  `event:2025_04_icms_scotland_talk`
  Source: https://www.kurims.kyoto-u.ac.jp/~motizuki/news-english.html (2025-04-27 entry)
  Subject: anabelian geometry. No published preprint indexed as of 2026-05-06.

---

## 8.7 Joshi reformulation (2025–2026)

- **2025-04-29** — Joshi posts "Final Report on Mochizuki–Scholze–Stix Controversy" v1 (arXiv:2505.10568v1).
  `event:2025_joshi_v1` / `evidence:Joshi_arxiv_2505_10568`
  `claim:joshi_2025_alternative`: Arithmetic Teichmuller Spaces yield a corrected framework (stance: `reformulation`; status: `preprint-not-peer-reviewed-as-of-2026-05`); `relates_to` `claim:scholze_stix_2018_main` and `claim:mochizuki_2018_response`

- **2025-10-28** — Mochizuki posts IUT progress report.
  `event:2025_mochizuki_october_report` / `evidence:Mochizuki_IUT_report_2025_10`
  `claim:mochizuki_2025_october_report`: continued defense of original framework (status: `self-published-RIMS-preprint`)
  Peter Woit's Not Even Wrong blog carries ongoing commentary (the registered post is the 2024 entry on Joshi's earlier exposition).
  `claim:woit_blog_2024_mochizuki_on_joshi_skeptical` / `evidence:Woit_blog_2024_mochizuki_on_joshi` (status: `informal-blog-commentary`)

- **2025-11-01** — Joshi FAQ 2025-11 (arXiv:2505.10568v1 + Joshi FAQ 2025-11).
  `event:2025_11_joshi_faq` / `evidence:Joshi_FAQ_2025_11`; status: `preprint-not-peer-reviewed-as-of-2026-05`

---

## 8.8 Formalization era (2026–)

- **2026-03-31** — LANA (Lean for ANabelian geometry) project announced by ZMC.
  `event:2026_lana_announcement` / `evidence:LANA_announcement_2026`
  actors: Commelin, Kedlaya, Hoshi, Topaz, Kato Fumiharu

- **2026-04-07** — Mochizuki, Hoshi, Yamashita, Yang post "On the Formalization of IUT: a preliminary progress report."
  `event:2026_mochizuki_formalization_report` / `evidence:Mochizuki_formalization_2026_04`
  `claim:lana_formalization_in_progress` status: "mid-report-scheduled-2026-07-17; team has articulated a specific contentious point but not yet resolved it" (`peer_review_status: project_announcement`)

- **2026-04-08** — Mochizuki presents Formalization of IUT (2026-04) slides at "Workshop on AI and Theorem Provers in Mathematics."
  `event:2026_04_formalization_ai_workshop_slides`
  Source: https://www.kurims.kyoto-u.ac.jp/~motizuki/news-english.html (2026-04-08 entry)
  Immediate follow-up to the 2026-04-07 PDF; same actors.

- **2026-07-17 (SCHEDULED, PENDING)** — LANA mid-report.
  `event:2026_lana_midreport_scheduled`
  This event has not occurred as of `verified_at` 2026-05-06.

---

## 8.9 Current status (2026-05-06)

| Claim | Status |
|---|---|
| `claim:mochizuki_2012_proves_abc` | `unresolved-as-of-2026-05` |
| `claim:scholze_stix_2018_main` | `unresolved-as-of-2026-05` |
| `claim:joshi_2025_alternative` | `preprint-not-peer-reviewed-as-of-2026-05` |
| `claim:lana_formalization_in_progress` | PENDING mid-report 2026-07-17 |

No claim in `claims.json` carries status `resolved` as of 2026-05-06.

---

## 8.10 Full entity / claim cross-reference

### IUT concept nodes cited in timeline events

| Entity IRI | Label | First appears | Claimed essential by |
|---|---|---|---|
| `iut:Cor.3.12` | Corollary 3.12, IUTchIII | 2012-08-30 | `claim:mochizuki_2012_proves_abc` |
| `iut:HodgeTheater` | Hodge theater | 2012-08-30 | `claim:mochizuki_2012_proves_abc` |
| `iut:multiradial_algorithm` | multiradial algorithm | 2012-08-30 | `claim:mochizuki_multiradial_thm_3_11_essential` |
| `iut:multiradial_representation_thm_3_11` | IUTchIII Thm 3.11 | 2012-08-30 | `claim:mochizuki_multiradial_thm_3_11_essential` |
| `iut:log_theta_lattice` | log-theta-lattice | 2012-08-30 | `claim:mochizuki_log_theta_lattice_noncommutative` |
| `iut:F_circ_theta_strip` | F-circ-times-mu-prime strip | 2012-08-30 | `claim:ss_canonically_same_strips` (SS), `claim:mochizuki_poly_iso_not_canonical` (M) |
| `iut:global_realified_frobenioid` | global realified Frobenioid | 2012-08-30 | `claim:ss_global_realified_canonical_trivial` (SS), `claim:mochizuki_global_realified_essential` (M) |
| `iut:alien_arithmetic_holomorphic_structure` | alien arithmetic holomorphic structure | 2012-08-30 | `claim:mochizuki_alien_copies_essential` |
| `iut:absolute_anabelian` | absolute anabelian geometry | 2012-08-30 | `claim:mochizuki_anabelian_essential` |
| `iut:theta_gau_link` | Theta-gau-link | 2012-08-30 | `claim:mochizuki_theta_gau_link_essential` |
| `iut:mono_theta_cyclotomic_rigidity` | mono-theta 3 rigidities | 2009-01-01 | `claim:mono_theta_three_rigidities_essential` |
| `iut:procession` | procession | 2012-08-30 | `claim:mochizuki_procession_essential` |
| `iut:Ind1` | Ind1 indeterminacy | 2012-08-30 | `claim:mochizuki_ind1_two_components` |
| `iut:Ind2` | Ind2 indeterminacy | 2012-08-30 | `claim:mochizuki_ind2_two_components` |
| `iut:Ind3_log_volume_absorption` | Ind3 indeterminacy | 2012-08-30 | `claim:mochizuki_ind3_log_volume_precise` |
| `iut:abc_conjecture` | abc conjecture | 1985-01-01 | `claim:mochizuki_2012_proves_abc`, `claim:joshi_2025_alternative` |

### Person nodes cited

| Person | Role in timeline | Key events |
|---|---|---|
| Mochizuki | Author / proponent | 2012, 2018-05, 2018-09, 2024-03-24, 2024-03-30, 2025-10, 2026-04 |
| Scholze | Critic | 2018-03 (visit), 2018-07 (report) |
| Stix | Critic | 2018-03 (visit), 2018-07 (report) |
| Yamashita | Proponent / expositor | 2018-03 (visit), 2024-06-25 (survey), 2025-03-20 (Summit talk) |
| Hoshi | Proponent | 2018-03 (visit), 2025-03 (Summit), 2026-03-31 (LANA), 2026-04 |
| Joshi | Reformulator | 2025-04-29 (v1), 2025-11-01 (FAQ) |
| Commelin | Formalization | 2026-03-31 (LANA) |
| Kedlaya | Formalization | 2026-03-31 (LANA), 2025-03-20 (Summit) |
| Calegari | Skeptic | 2017-12-17 |
| Woit | Skeptic | 2025 (ongoing blog) |

### Claim stance summary

| Stance | Claims (count) | Representative |
|---|---|---|
| supportive (Mochizuki side) | ~20 | `claim:mochizuki_2012_proves_abc` |
| critical (SS side) | ~10 | `claim:scholze_stix_2018_main` |
| reformulation (Joshi) | 1 | `claim:joshi_2025_alternative` |
| neutral-observation | 5 | `claim:western_majority_skeptical`, `claim:prims_2021_acceptance` |
| factual-publication | 1 | `claim:prims_2021_acceptance` |
| investigation (LANA) | 1 | `claim:lana_formalization_in_progress` |

---

## 8.11 SS main battleground: Cor.3.12 claim chain detail

The Scholze–Stix critique (`claim:scholze_stix_2018_main`) reduces to a two-horn argument applied at IUTchIII Cor.3.12:

**Horn A (empty inequality):** If canonical identifications are accepted (`claim:ss_canonically_same_strips`), then F-circ-times-mu-prime strips on both sides of the Theta-link are the same object (SS p.9), global realified Frobenioids become canonically trivial (SS p.10: "always canonically trivial using the various gamma_can"), and the log-volume inequality reduces to 0 ≤ 0 (`claim:ss_global_realified_canonical_trivial`).

**Horn B (monodromy inconsistency):** If j-squared scalars are inserted without canonical identification, the diagram acquires "monodromy j-squared, i.e. being inconsistent" (SS p.10, `claim:ss_j_squared_monodromy_inconsistent`).

**SS blurring objection:** Mochizuki proposed (day 5 of Kyoto discussions) that Ind1/Ind2/Ind3 indeterminacies blur the diagram. SS replied that the required blurring must be of order O(l-squared), rendering the resulting inequality useless for abc (`claim:ss_o_l_squared_blurring_useless`).

**Mochizuki structural counter:** The canonical identification is illegitimate because F-circ-times-mu-prime strips on the two sides reside in distinct arithmetic holomorphic structures (IUTchI Rem 3.9.4: ring structure "obliterated"; `claim:mochizuki_alien_copies_essential`). The full poly-isomorphism of abstract topological monoids (`claim:mochizuki_poly_iso_not_canonical`) cannot be replaced by a ring-level canonical isomorphism without traversing the inter-universal wall. This structural counter is not resolved as of 2026-05-06.

**Joshi alternative path:** Joshi (arXiv:2505.10568v1 + Joshi FAQ 2025-11, `claim:joshi_2025_alternative`) proposes that both Horn A and Horn B can be avoided via Arithmetic Teichmuller Spaces (ATS): the ATS reformulation is claimed to repair the alleged gap without requiring acceptance of the SS canonical identification. This is a reformulation, not an endorsement of either the original IUT proof or the SS critique as terminal. Status: preprint-not-peer-reviewed as of 2026-05-06.

**Formalization status:** The LANA project (`claim:lana_formalization_in_progress`, `event:2026_mochizuki_formalization_report`) is formalizing anabelian geometry prerequisites in Lean 4. The 2026-04-07 preliminary progress report states a specific contentious point has been articulated but not yet resolved. LANA mid-report is scheduled for 2026-07-17.

---

## 8.12 Deliberate exclusions

- Private correspondence before the 2018 RIMS visit (no stable URL).
- Individual SNS posts without stable archival URLs.
- RIMS workshop talks for which no published transcript is indexed.
- Wikipedia / nLab edit history (only current snapshot `evidence:nLab_IUT` is linked).
- IUT Summit 2025 individual talk videos / slides not yet indexed with stable DOI or PDF URL.

---

## Cross-reference

- `data/timeline.json`: 25 dated events (`event:*`)
- `data/claims.json`: ~40 claims (`claim:*`)
- `data/evidence.json`: 27 evidence records (`evidence:*`)
- `data/entities.json`: concept / person / paper records (`iut:*`, `person:*`, `paper:*`)

*No editorial verdict expressed. All `unresolved-as-of-2026-05` claims remain open.*
