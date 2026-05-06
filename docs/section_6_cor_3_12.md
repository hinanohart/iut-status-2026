# Section 6: Corollary 3.12 — the disputed corollary (`iut:Cor.3.12`)

> 3-agent verified.
> Last verified: 2026-05-06.
> drift-zero IRI: `iut:Cor.3.12`
> Per-side drafts: docs/concepts/cor_3_12.md, docs/concepts/cor_3_12_ss_view.md
> **This is the load-bearing step of the IUT proof of abc; it is also the focal point
> of the Mochizuki vs Scholze-Stix dispute since 2018. The dispute remains unresolved
> as of 2026-05-06.**

---

## 6.1 Statement (consensus, statement-level)

Both sides agree on the following.

- **IUTchIII Corollary 3.12** asserts a log-volume inequality of the form:

      −|log(Θ)| ≥ −|log(q)|

  valid up to indeterminacies (Ind1), (Ind2), (Ind3). Formally it states that the
  log-volume of the Θ-pilot (`iut:F_circ_theta_strip`) is bounded below by the
  log-volume of the q-pilot (`iut:F_circ_q_strip`), after accounting for the three
  classes of indeterminacy arising from the multiradial algorithm.

- **Reference**: IUTchIII Cor.3.12, pp.173–174.
  DOI: [10.4171/PRIMS/57-1-3](https://doi.org/10.4171/PRIMS/57-1-3)

- **Position in IUTch**: Cor.3.12 is a direct consequence of IUTchIII Theorem 3.11
  (`iut:multiradial_representation_thm_3_11`). The multiradial representation
  (Thm 3.11-i) constructs the Θ-pilot in a form accessible from an alien arithmetic
  holomorphic structure (`iut:alien_arithmetic_holomorphic_structure`); the
  log-Kummer correspondence (Thm 3.11-ii, `iut:log_Kummer_correspondence`) then
  guarantees the étale-like data survive log-link iterations. Cor.3.12 is the first
  place where a concrete numerical inequality is extracted from that machinery.

- **Load-bearing role** (both sides concur): Cor.3.12 is the step from which
  IUTchIV Theorem 1.10 and ultimately the Szpiro / abc height bound are derived.
  Without a valid proof of Cor.3.12, the IUT approach to abc does not yield a result.

- **Mochizuki (Rpt2018 §2, label (Smm)) paraphrase**:
  > "Suppose that A and B are positive real numbers, which are defined so as to satisfy
  > the relation −2B = −A (which corresponds to the Θ-link). One then proves a theorem
  > −2B ≤ −2A + 1 (which corresponds to the multiradial representation of [IUTchIII],
  > Theorem 3.11). This theorem, together with the above defining relation, implies a
  > bound on A: −A ≤ −2A + 1, i.e., A ≤ 1 (which corresponds to [IUTchIII], Corollary 3.12)."

- **SS (2018, p.9)** confirms:
  > Indeterminacies Ind 1, 2, 3 are employed "(without which the conclusion would be
  > obviously false)."

- This is `claim:cor_3_12_neutral_statement` in the graph.

---

## 6.2 Mathematical content [CLAIMED_BY: Mochizuki]

The following is Mochizuki's account of the internal structure of the proof. SS does
not individually dispute these constructions; its objection targets the inference that
the constructions yield a *nontrivial* inequality (§6.3–6.4).

### 6.2.1 log-theta-lattice and the two-axis structure

The proof of Cor.3.12 operates within the log-theta-lattice
(`iut:log_theta_lattice`, IUTchIII Def 1.4): a two-dimensional diagram of Hodge
theaters connected along a horizontal axis (Θ^×μ-links) and a vertical axis
(log-links).

- **Horizontal axis (Θ-link)** (`iut:theta_link_full_poly_iso`): connects the
  Θ-holomorphic structure of column 0 to the q-holomorphic structure of column 1
  via a full poly-isomorphism (IUTchI Cor.3.7-i). The Θ-link is explicitly *not*
  a ring homomorphism (ΘNR), which Mochizuki identifies as the reason the two
  holomorphic structures must be maintained as distinct objects
  (`iut:alien_arithmetic_holomorphic_structure`).

  The comparison is mediated by the Hodge-Arakelov-theoretic evaluation isomorphism
  (`iut:hodge_arakelov_evaluation`, IUTchII Cor.4.10-ii) and its Gauss-link variant
  (`iut:theta_gau_link`, IUTchII Cor.4.10-iii).

- **Vertical axis (log-link)** (`iut:log_link_construction`, IUTchIII Def 1.1-iii):
  within each column, the log-link applies the p-adic logarithm iteratively, producing
  a Frobenius-like structure; repeated application yields the log-shell I_v. The
  log-volume foundation (`iut:log_volume_integration`, IUTchIII Prop 1.2-iii and
  Prop 3.9-iv) underpins all log-volume comparisons in Cor.3.12.

- The vertical and horizontal axes do *not* commute (Def 1.4 Remark 1.4.1(i)), which
  Mochizuki regards as the structural heart of IUTchIII.

- **Source**: IUTchIII §3; EssLgc §3.10 (Stp1)–(Stp8).
  URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf

### 6.2.2 Hodge theater structure underlying Cor.3.12

Cor.3.12 is stated for a Θ^±ell NF-Hodge theater (`iut:theta_pm_ellNF_hodge_theater_integration`,
IUTchI Def 6.13), which integrates three sub-components:

- the NF-Hodge theater (`iut:NF_hodge_theater`, IUTchI Def 4.6-iii) governing
  multiplicative structure and global Galois action;
- the Θ^±ell-Hodge theater (`iut:theta_pm_ell_hodge_theater`, IUTchI Def 6.4/6.11)
  governing additive symmetry.

These theaters are assembled from F^⊙-prime-strips: the Θ-pilot strip
(`iut:F_circ_theta_strip`) and the q-pilot strip (`iut:F_circ_q_strip`) are the
two abstract objects whose log-volumes Cor.3.12 compares.

The Frobenioid structure underlying both strips is governed by `iut:frobenioid_axioms`
(Frd I Def 1.3), including the factorization theorem (`iut:factorization_theorem`,
Frd I Cor.4.11) and the degree function (`iut:degree_function`). The global realified
Frobenioid (`iut:global_realified_frobenioid`) provides the arithmetic-degree datum
that makes the log-volume comparison non-empty.

### 6.2.3 Indeterminacies and switching compatibility

- **(Ind1)** (`iut:Ind1`): poly-morphism indeterminacy from the Galois action in the
  Θ-link. Internally decomposed into two components:
  - `iut:Ind1_d_prime_strip_aut` — slot-wise automorphisms of procession D^+-prime-strips;
  - `iut:Ind1_label_permutation` — permutation automorphisms of S^±_{j+1}.

- **(Ind2)** (`iut:Ind2`): indeterminacy from treating O^×μ as an abstract topological
  monoid. Internally:
  - `iut:Ind2_z_times_indeterminacy` — Z^×-orbit indeterminacy at nonarchimedean places
    (Prop 1.2-vi);
  - `iut:Ind2_o_times_mu_action` — per-summand O^×μ group action on direct summands of
    I^Q(S^±_{j+1}; ⁿ˒ᵒD^+_{v_Q}).

- **(Ind3)** (`iut:Ind3`): additive indeterminacy from the kernel of the
  log-Kummer-correspondence (`iut:log_Kummer_correspondence`). Internally:
  - `iut:Ind3_upper_semi_compat_kummer` — upper semi-compatibility of log-Kummer
    isomorphisms (IUTchIII Thm 3.11-ii): inclusions at V^non, surjections at V^arc;
  - `iut:Ind3_log_volume_absorption` — precise log-volume compatibility across
    log-links (Prop 3.9-iv).

  Mochizuki (Rpt2018 §8): Ind1 and Ind2 are "joint flexibility" — a necessary cost to
  give the rigid structure switching symmetry between column 0 and column 1. All three
  indeterminacies must be present for the multiradial representation
  (`iut:multiradial_representation_thm_3_11`) to be compatible with switching of
  holomorphic columns.

### 6.2.4 Anabelian and Frobenioid-theoretic backbone

The proof relies on three layers of anabelian rigidity (`iut:absolute_anabelian`):

1. **Tempered anabelian rigidity** (`iut:tempered_rigidity`, EtTh Thm 1.6): used to
   rigidify the local data at bad primes in a way that is insensitive to ring-theoretic
   context.
2. **Mono-anabelian reconstruction** (`iut:mono_anabelian`): recovers the arithmetic
   data from a single abstract profinite group, enabling cross-link comparison.
3. **Absolute anabelian cuspidalization** (`iut:cuspidalization`, Cusp. Thm 1.16):
   provides additional rigidity at cusps that is essential for the global comparison.

SS's sub-claim §6.5 disputes whether these tools are *essential* at the disputed step,
rather than disputing the statements themselves.

### 6.2.5 log-Kummer-correspondence and the closed loop

- The log-Kummer-correspondence (`iut:log_Kummer_correspondence`, Thm 3.11-ii)
  guarantees that the étale-like structure of column 0 is invariant (up to
  `iut:Ind3`) under iterations of the log-link. Upper semi-compatibility
  (`iut:upper_semi_compatibility`, IUTchIII Rem 1.2.2-iii) plays the key role here:
  the inclusions at V^non and surjections at V^arc give the "one-sided" compatibility
  that survives log-link passage.

- This makes the log-volume of the Θ-pilot (`iut:F_circ_theta_strip`) comparable
  with the q-pilot of column 1 (`iut:F_circ_q_strip`).

- EssLgc §3.10 (LVsQ): "log-volume を取ることで初めて formal subquotient が
  coarse/set-theoretic subquotient になる." The final step — taking log-volumes via
  `iut:log_volume_integration` — collapses the distinct labels and closes the loop,
  yielding the set-theoretic inequality of Cor.3.12.

### 6.2.6 Connection to abc

- The inequality flows through IUTchIV Theorem 1.10 to give an effective height bound,
  which yields the Szpiro inequality and thus abc.
  Reference: EssLgc (vi-k); Rpt2018 (BgIUT2).

---

## 6.3 [DISPUTED] Validity of the proof argument

### 6.3.1 Mochizuki position
(`claim:mochizuki_2012_proves_abc`, `claim:mochizuki_2018_response`, `claim:mochizuki_2025_october_report`)

Core claim: the multiradial algorithm (`iut:multiradial_representation_thm_3_11`)
furnishes a *legitimate* comparison between distinct alien copies
(`iut:alien_arithmetic_holomorphic_structure`), and no canonical identification of
the two ring theories is possible or permissible.

Key statements:

- **Against (SSId)** (the SS assumption that the two ring structures can be canonically
  identified): Rpt2018 (SSADFs):
  > "The assertion of (SSAD) is false. The contradiction only occurs when one identifies
  > the hol. strs./ring theories in the domain and codomain of the Θ-link."
  That is, any contradiction found by SS occurs only in a *modified* version of IUTch
  in which distinct labels are collapsed — not in IUTch itself.

- **On the illegality of label deletion** (SSDLFs, Rpt2018 §12): deleting distinct
  labels collapses `iut:Ind1_label_permutation` — a *stronger* operation than merely
  eliminating Ind1/Ind2; it renders the multiradial algorithm
  (`iut:multiradial_representation_thm_3_11`) inapplicable.

- **Against the "loop" reading** (Cmt2018-05 (C17), (C18)):
  > "log-volume を計算する際に commute が必要な 'loop' は Cor.3.12 の proof には
  > 決して現れない."
  No canonical identification of copies of **R**, and no commutative loop in the
  displayed diagram, appear in the proof. The Θ-pilot and q-pilot are embedded into a
  *single container* (with `iut:Ind1`, `iut:Ind2`, `iut:Ind3` admitted), so
  commutativity of two distinct mappings is not an issue.

- **IUT-report-2025-10 §2.1 (SSA2)**:
  > SS's argument is "a SS-style interpretation/simplification of the set-up of
  > Cor.3.12" that has "no logical relationship" to the actual log-theta-lattice
  > (`iut:log_theta_lattice`) setup and the proof of Cor.3.12.

- **Existence Principle (ExPr)** (IUT2025-10): the existence of an algorithm that
  yields no nontrivial consequence (the SS simplification) does not imply the
  non-existence of an algorithm that does (Cor.3.12).

- **On anabelian essentialness**: the mono-anabelian reconstruction
  (`iut:mono_anabelian`) and tempered rigidity (`iut:tempered_rigidity`) are precisely
  what prevent the identification of distinct copies that SS's argument requires.

### 6.3.2 Scholze-Stix position
(`claim:scholze_stix_2018_main`, `claim:scholze_stix_2018_sub_1/2/3`)

Core claim: under any *consistent* identification of the copies of real numbers that
appear, the j² scalars are forced to vanish, leaving only an empty inequality.

Key statements:

- **Main claim** (SS 2018, p.10):
  > "The conclusion of this discussion is that with consistent identifications of copies
  > of real numbers, one must in (1.5) omit the scalars j² that appear, which leads to
  > an **empty inequality**."

- **On Theorem 3.11** (SS 2018, p.9, footnote 12):
  > "We pause to observe that with the simplifications outlined above, such as identifying
  > identical copies of objects along the identity, the critical [IUTT-3, Theorem 3.11]
  > does **not become false, but trivial**."
  This is a precise characterization of the nature of the claimed defect: `iut:multiradial_representation_thm_3_11`
  is not wrong as stated, but its content becomes vacuous once the alien-copy framework
  (`iut:alien_arithmetic_holomorphic_structure`) is resolved via consistent
  identifications.

- **On the O(ℓ²) blurring** (SS 2018, p.10):
  > "it seems to us that this statement means that the **blurring must be by a factor of
  > at least O(ℓ²)**, rendering the inequality thus obtained useless."
  This is SS's evaluation of Mochizuki's day-5 reply. The blurring required to absorb
  the j² monodromy would render `iut:Ind2_z_times_indeterminacy` and
  `iut:Ind2_o_times_mu_action` large enough to trivialize the inequality.

- **On the log-link** (`claim:ss_log_link_naturally_equivalent_to_identity`):
  `iut:log_link_construction` is "naturally equivalent to the identity" (SS §2.1.3,
  p.6), removing the structural content Mochizuki attributes to the vertical axis of
  `iut:log_theta_lattice`.

- **On the global realified Frobenioid** (`claim:ss_global_realified_canonical_trivial`,
  `claim:ss_global_realified_elementary`): `iut:global_realified_frobenioid` arising
  from F^⊩×μ-prime strips is canonically trivial via the various γ_can; the
  `iut:degree_function` it encodes does not distinguish Θ-pilot from q-pilot.

- **On tempered rigidity** (`claim:ss_tempered_rigidity_used_not_evaluated`):
  SS notes that `iut:tempered_rigidity` is *used* but evaluates whether this use is
  essential at the specific step. SS position: at the disputed step the anabelian
  tools (`iut:absolute_anabelian`, `iut:mono_anabelian`, `iut:cuspidalization`)
  are not doing essential work.

- **On the F^⊙-prime strips** (`claim:ss_f_modulus_strip_focal`,
  `claim:ss_f_modulus_strip_focal_extended`): the focal strip constructions
  (`iut:F_circ_theta_strip`, `iut:F_circ_q_strip`) reduce to the same abstract
  object once canonical identifications are applied.

---

## 6.4 [DISPUTED] Specific objection: empty inequality

### 6.4.1 SS's technical diagram and γ_can (SS 2018, p.10)

SS constructed the following diagram during the Kyoto discussions:

```
R⊙,Θ  —[Θ-link ≅]—→  R⊙,q
  ↑                        ↑
(R⊙c,Θⱼ)ⱼ              R⊙c,q
  ↓                        ↓
  RΘ      ——[=]——→        Rq
```

> "There is one consistent choice of isomorphisms given by using the natural isomorphisms
> R⊙,Θ ≅ R⊙,q ≅ R coming from the observation that the global realiﬁed Frobenioids
> coming from F^⊩×µ-prime strips are always **canonically trivial** using the various
> γ_can." (p.10)

This argument involves `iut:global_realified_frobenioid` and `iut:theta_link_full_poly_iso`:
SS claims the full poly-isomorphism of the Θ-link, when combined with γ_can on both
sides, admits a *canonical* section that collapses the inter-universal distinction.

Under this consistent choice, the abstract Θ-pilot object (`iut:F_circ_theta_strip`)
does *not* encode the arithmetic degree of the Θ-divisor:
> "we saw that with these isomorphisms, the abstract Θ-pilot object does not encode
> the arithmetic degree of the Θ-divisor." (p.10)

Introducing the j² scalars on the left side then forces a monodromy inconsistency:
> "it is clear that this will result in the whole diagram having monodromy j², i.e.
> being **inconsistent**." (p.10)

This is encoded in `claim:ss_j_squared_monodromy_inconsistent`.

### 6.4.2 Mochizuki counter-argument

- The j² scalars arise precisely *because* one does **not** identify the two ring
  structures. The γ_can trivialization is illegitimate from the IUTch standpoint
  because it collapses the inter-universal distinction maintained by
  `iut:Ind1_d_prime_strip_aut` and `iut:Ind2_z_times_indeterminacy`.

- The "inconsistency" SS identifies is real — but it is an inconsistency in a
  *different* mathematical object (a version of the setup with canonical identification
  imposed), not in IUTch as formulated.

- Cmt2018-05 (C17): the "loop" that would require commutativity never appears in the
  proof; the single-container embedding with `iut:Ind1`, `iut:Ind2`, `iut:Ind3`
  admitted removes the need for such commutativity.

- The Θ-gau-link (`iut:theta_gau_link`) and the Hodge-Arakelov evaluation
  (`iut:hodge_arakelov_evaluation`) jointly ensure that the j² scalars *are* present
  in the q-pilot of column 1 — they arise from the theta function evaluation, not
  from an ad-hoc insertion.

---

## 6.5 [DISPUTED] Anabelian essential-ness (sub_2)
(`claim:scholze_stix_2018_sub_2`)

- **SS (p.5, Remark 9)**:
  > "Anabelian geometry is supposed to be the key to Mochizuki's proof. However, here
  > we see that in the IUTT papers, we are (for the essential part) in a situation where
  > anabelian geometry holds true in the sense that geometry and group theory are
  > equivalent. We could **not find the point where it is essential to work with
  > fundamental groups** – there are no additional isomorphisms of fundamental groups
  > that do not come from isomorphisms of schemes, precisely because of Mochizuki's
  > theorem."

  SS accepts Mochizuki's anabelian theorem itself (Theorem 7 / [Anab3, Theorem 1.9]).
  The argument is that the theorem's very strength — the equivalence of geometry and
  group theory — removes any leverage that working purely with fundamental groups could
  have provided. In particular, `iut:absolute_anabelian`, `iut:mono_anabelian`, and
  `iut:cuspidalization` are held by SS to be present but not essential at the specific
  step of Cor.3.12.

- **Mochizuki position** (`claim:mochizuki_2018_response`): the core of Cor.3.12
  depends on anabelian rigidity (`iut:tempered_rigidity`, `iut:mono_anabelian`) in a
  way that is invisible from SS's simplified setup; the rigidity is precisely what
  prevents arbitrary identification of distinct copies. Without `iut:tempered_rigidity`
  (EtTh Thm 1.6), the local data at bad primes cannot be rigidified, and the
  log-Kummer correspondence (`iut:log_Kummer_correspondence`) fails.

- The two positions are **not reconciled** in any published document as of 2026-05-06.

---

## 6.6 [DISPUTED] Hodge theater distinction (sub_1)
(`claim:scholze_stix_2018_sub_1`)

- **SS (p.6)**:
  > "The natural functor from the category whose only object is X and whose morphisms
  > are the automorphisms of X [...] to the category of Θ^±ell NF-Hodge theaters is
  > an **equivalence of categories**, as follows by combining [IUTT-1, Corollary 6.12(i),
  > ...]."

  Consequence stated by SS: "choosing a Hodge theater amounts to choosing a
  once-punctured elliptic curve that is abstractly isomorphic to X." This targets
  `iut:theta_pm_ellNF_hodge_theater_integration` (IUTchI Def 6.13): if the category
  of Θ^±ell NF-Hodge theaters is equivalent to the singleton category of X, then the
  multiplicity of columns in `iut:log_theta_lattice` is illusory.

- **Mochizuki position**: the inter-universal framework demands that distinct copies
  of `iut:NF_hodge_theater` and `iut:theta_pm_ell_hodge_theater` be treated as
  set-theoretically distinct objects. Their abstract isomorphism is irrelevant to the
  comparison performed across `iut:theta_link_full_poly_iso`; distinctness is
  maintained at the level of the underlying set-theoretic universe, not at the level of
  abstract isomorphism class.

- This sub-dispute underlies much of the broader disagreement about whether the
  "alien copies" framework (`iut:alien_arithmetic_holomorphic_structure`) introduces
  genuine content or only notational overhead.

---

## 6.7 What is NOT in dispute (both sides agree)

| Item | Evidence |
|---|---|
| Existence of IUTchIII Cor.3.12 as a stated corollary | factual |
| Cor.3.12 as load-bearing step for IUT→abc | SS 2018 p.1; Rpt2018 (BgIUT2) |
| `iut:multiradial_representation_thm_3_11` statement-level well-definedness | SS 2018 p.9 fn.12 |
| `iut:theta_link_full_poly_iso` well-definedness as full poly-isomorphism | SS 2018 p.9 |
| log-shell I_v definition (`iut:log_link_construction` Prop 1.2) | not contested by either party |
| Mochizuki's anabelian theorems themselves (`iut:absolute_anabelian`) | SS 2018 p.5, Remark 9 |
| `iut:Ind1`, `iut:Ind2`, `iut:Ind3` are necessary (without them conclusion obviously false) | SS 2018 p.9 |
| `iut:log_theta_lattice` Def 1.4 structure (non-commutativity of axes) | not formally contested |
| `iut:frobenioid_axioms` and `iut:degree_function` as formal framework | not contested |
| Cor.3.12 statement may be *true* (as distinct from proved) | SS 2018 does not claim Cor.3.12 is false |
| Mochizuki's personal integrity and mathematical capability | SS 2018 p.1 (acknowledgements) |

Note on the last row: SS 2018 opens with thanks for Mochizuki's hospitality and the
"constructive nature" of the discussions, explicitly framing their objection as
mathematical, not personal.

---

## 6.8 Status (as of 2026-05-06)

| Dimension | Status |
|---|---|
| Mathematical community consensus | **未確立 (not established)** |
| PRIMS 2021 publication | Factual; represents editorial acceptance, not independent external verification of the disputed steps |
| SS 2018 | Not retracted; SS position unchanged in public statements |
| Mochizuki 2025-10 report | Reaffirms validity; introduces Lean4 formalization strategy |
| LANA formalization project | Announced 2026-03-31; mid-report scheduled 2026-07-17 (PENDING); Lean 4 formalization of `iut:theta_pm_ellNF_hodge_theater_integration` and `iut:multiradial_representation_thm_3_11` underway; expected to require several more years (`claim:lana_formalization_in_progress`) |
| Joshi 2025 (arXiv:2505.10568 v1) + Joshi FAQ 2025-11 | Proposes corrected framework; preprint, not peer-reviewed; represents a third mathematical perspective (`claim:joshi_2025_alternative`). Round 5 audit removed a previously-claimed v2 (2026-05-02) which was fictional; the FAQ is the supplementary source. |
| Western mathematical commentariat | A significant portion remains skeptical in informal discourse; no formal retraction of skepticism |

Key uncertainty: the LANA project represents the first systematic attempt at
third-party machine-verified checking of the IUTch argument. Its findings, when
reported, will constitute the most rigorous external assessment available.
The 2026-07-17 mid-report date is the next scheduled public milestone.

---

## 6.9 Forbidden translations

The following terms and framings are avoided in neutral merger context because they
carry implicit verdicts from one side:

| Term / framing | Reason to avoid | Neutral substitute |
|---|---|---|
| "gap in the proof" | SS asserts this; Mochizuki denies it | "SS alleges a gap at Step (xi)" |
| "the proof is circular" | SS framing not adopted by neutral parties | "SS claims the inequality is empty" |
| "Mochizuki identifies copies" (affirmatively) | Mochizuki explicitly regards identification as the error; attribution reversal | "SS argues that a consistent identification …" |
| "IUT is accepted / verified" | PRIMS publication ≠ community consensus | "IUTchIII was published in PRIMS (2021)" |
| "Scholze-Stix is correct / SS refutes IUT" | Dispute unresolved | "SS maintains the inequality is empty (disputed)" |
| "trivially wrong" (of either side) | Non-neutral | describe the specific technical objection |
| "SS is silent on X" | Absence of comment ≠ concession | "SS has not published a position on X" |

---

## Cross-reference

### Entities (full list with IRIs)

**Core mechanics of Cor.3.12:**
- `iut:Cor.3.12` — the disputed corollary
- `iut:multiradial_representation_thm_3_11` — Thm 3.11-i, multiradial representation
- `iut:log_Kummer_correspondence` — Thm 3.11-ii, log-Kummer correspondence
- `iut:log_theta_lattice` — Def 1.4, two-dimensional lattice of theaters
- `iut:theta_link_full_poly_iso` — IUTchI Cor.3.7-i, horizontal axis morphism
- `iut:log_link_construction` — IUTchIII Def 1.1-iii, vertical axis morphism
- `iut:log_volume_integration` — Prop 1.2-iii + Prop 3.9-iv, log-volume foundation
- `iut:upper_semi_compatibility` — IUTchIII Rem 1.2.2-iii

**Indeterminacy sub-components:**
- `iut:Ind1` (parent), `iut:Ind1_d_prime_strip_aut`, `iut:Ind1_label_permutation`
- `iut:Ind2` (parent), `iut:Ind2_z_times_indeterminacy`, `iut:Ind2_o_times_mu_action`
- `iut:Ind3` (parent), `iut:Ind3_upper_semi_compat_kummer`, `iut:Ind3_log_volume_absorption`

**Hodge theater structure:**
- `iut:theta_pm_ellNF_hodge_theater_integration` — concrete triple (IUTchI Def 6.13)
- `iut:NF_hodge_theater` — D-level (IUTchI Def 4.6-iii)
- `iut:theta_pm_ell_hodge_theater` — additive symmetry sub-component (IUTchI Def 6.4/6.11)
- `iut:HodgeTheater` (parent)
- `iut:alien_arithmetic_holomorphic_structure` — cross-column comparison framework

**Pilot strips and Frobenioid backbone:**
- `iut:F_circ_theta_strip` — Θ-pilot (IUTchI Ex.3.5-ii)
- `iut:F_circ_q_strip` — q-pilot (IUTchI Ex.3.5-i)
- `iut:global_realified_frobenioid` — C^R_mod, arithmetic degree datum
- `iut:frobenioid_axioms` — Frd I Def 1.3
- `iut:factorization_theorem` — Frd I Cor.4.11
- `iut:degree_function` — deg_Fr

**Hodge-Arakelov evaluation:**
- `iut:hodge_arakelov_evaluation` — IUTchII Cor.4.10-ii
- `iut:theta_gau_link` — IUTchII Cor.4.10-iii, Gauss-link variant

**Anabelian rigidity backbone:**
- `iut:absolute_anabelian` — absolute anabelian framework
- `iut:tempered_rigidity` — EtTh Thm 1.6
- `iut:mono_anabelian` — mono-anabelian reconstruction
- `iut:cuspidalization` — Cusp. Thm 1.16

### claims.json

`claim:cor_3_12_neutral_statement`, `claim:mochizuki_2012_proves_abc`,
`claim:mochizuki_2018_response`, `claim:mochizuki_2025_october_report`,
`claim:scholze_stix_2018_main`, `claim:scholze_stix_2018_sub_1`,
`claim:scholze_stix_2018_sub_2`, `claim:scholze_stix_2018_sub_3`,
`claim:ss_j_squared_monodromy_inconsistent`, `claim:ss_o_l_squared_blurring_useless`,
`claim:ss_global_realified_canonical_trivial`, `claim:ss_global_realified_elementary`,
`claim:ss_log_link_naturally_equivalent_to_identity`,
`claim:ss_tempered_rigidity_used_not_evaluated`,
`claim:ss_f_modulus_strip_focal`, `claim:ss_f_modulus_strip_focal_extended`,
`claim:ss_canonically_same_strips`,
`claim:joshi_2025_alternative`, `claim:lana_formalization_in_progress`

### timeline.json

`event:2018_07_ss_report`, `event:2018_09_mochizuki_response`,
`event:2021_prims_publication`, `event:2025_mochizuki_october_report`,
`event:2026_lana_announcement`, `event:2026_lana_midreport_scheduled`

### Section links

Section 4 (`iut:log_link`, `iut:log_shell`) ← Section 5 (`iut:multiradial_algorithm`, Ind1/2/3) ← **this section** → Section 7 (abc consequence) [docs/section_7_abc.md]

---

## Verification log

| Claim | Verdict | Note |
|---|---|---|
| 6.1 Cor.3.12 statement existence + dependency | 3/3 ✅ | IUTchIII p.173–174 DOI confirmed |
| 6.2 mathematical content (mochizuki-side detail) | 1/3 [CLAIMED_BY: Mochizuki] | SS does not individually dispute constructions |
| 6.2.2 Hodge theater sub-components | 1/3 [CLAIMED_BY: Mochizuki] | `iut:theta_pm_ellNF_hodge_theater_integration`, NF, Θ^±ell structures |
| 6.2.3 Ind sub-components (6 new IRIs) | 1/3 [CLAIMED_BY: Mochizuki] | SS scope outside individual indeterminacies |
| 6.2.4 Anabelian backbone | 1/3 [CLAIMED_BY: Mochizuki] | SS disputes essentialness (§6.5), not definitions |
| 6.3 validity of proof argument | 0/3 [DISPUTED] | core of the 2018 disagreement |
| 6.4 empty inequality (specific objection) | 0/3 [DISPUTED] | γ_can vs. alien-copies framework |
| 6.5 anabelian essential-ness (sub_2) | 0/3 [DISPUTED] | Remark 9 vs. Mochizuki's rigidity argument |
| 6.6 Hodge theater distinction (sub_1) | 0/3 [DISPUTED] | equivalence-of-categories vs. set-theoretic distinctness |
| 6.7 not-in-dispute items | 3/3 ✅ | confirmed from both primary sources |
| 6.8 status as of 2026-05-06 | 3/3 ✅ | factual; no verdict implied |
| 6.9 forbidden translations | 3/3 ✅ | applied throughout; "SS silent" prohibited |

---

## Sources

| 文書 | URL / DOI |
|---|---|
| IUTchIII Cor.3.12, pp.173–174 | DOI [10.4171/PRIMS/57-1-3](https://doi.org/10.4171/PRIMS/57-1-3) |
| IUTchI (Hodge theater constructions) | DOI [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1) |
| IUTchII (Hodge-Arakelov evaluation) | DOI [10.4171/PRIMS/57-1-2](https://doi.org/10.4171/PRIMS/57-1-2) |
| Rpt2018 (Report on Discussions, Feb 2019) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Rpt2018.pdf |
| Cmt2018-05 (Comments on SS manuscript, Jul 2018) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-05.pdf |
| IUT-report-2025-10 (October 2025) | https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf |
| EssLgc (Essential Logical Structure, March 2024) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf |
| SS 2018 (Why abc is still a conjecture, Jul 2018) | https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
| EtTh (Étale Theta, EtTh Thm 1.6) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Etale%20Theta.pdf |
| Frobenioids I (Frd I Def 1.3, Cor 4.11) | https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf |
