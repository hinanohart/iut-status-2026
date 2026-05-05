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
  log-volume of the Θ-pilot is bounded below by the log-volume of the q-pilot, after
  accounting for the three classes of indeterminacy arising from the multiradial algorithm.

- **Reference**: IUTchIII Cor.3.12, pp.173–174.
  DOI: [10.4171/PRIMS/57-1-3](https://doi.org/10.4171/PRIMS/57-1-3)

- **Position in IUTch**: Cor.3.12 is a direct consequence of IUTchIII Theorem 3.11
  (multiradial representation). It is the first place where a concrete numerical
  inequality is extracted from the multiradial machinery.

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

- **Horizontal axis (Θ-link)**: connects the Θ-holomorphic structure of column 0 to
  the q-holomorphic structure of column 1 via a full poly-isomorphism. The Θ-link is
  explicitly *not* a ring homomorphism (ΘNR), which Mochizuki identifies as the
  reason the two holomorphic structures must be maintained as distinct objects.

- **Vertical axis (log-link)**: within each column, the log-link applies the p-adic
  logarithm iteratively, producing a Frobenius-like structure; repeated application
  yields the log-shell I_v.

- **Source**: IUTchIII §3; EssLgc §3.10 (Stp1)–(Stp8).
  URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf

### 6.2.2 Indeterminacies and switching compatibility

- **(Ind1)**: poly-morphism indeterminacy from the Galois action in the Θ-link.
- **(Ind2)**: indeterminacy from treating O^×μ as an abstract topological monoid.
- **(Ind3)**: additive indeterminacy from the kernel of the log-Kummer-correspondence.

  Mochizuki (Rpt2018 §8): Ind1 and Ind2 are "joint flexibility" — a necessary cost to
  give the rigid structure switching symmetry between column 0 and column 1. All three
  indeterminacies must be present for the multiradial representation to be compatible
  with switching of holomorphic columns.

### 6.2.3 log-Kummer-correspondence and the closed loop

- The log-Kummer-correspondence guarantees that the étale-like structure of column 0
  is invariant (up to Ind3) under iterations of the log-link. This makes the
  log-volume of the Θ-pilot comparable with the q-pilot of column 1.

- EssLgc §3.10 (LVsQ): "log-volume を取ることで初めて formal subquotient が
  coarse/set-theoretic subquotient になる." The final step — taking log-volumes —
  collapses the distinct labels and closes the loop, yielding the set-theoretic
  inequality of Cor.3.12.

### 6.2.4 Connection to abc

- The inequality flows through IUTchIV Theorem 1.10 to give an effective height bound,
  which yields the Szpiro inequality and thus abc.
  Reference: EssLgc (vi-k); Rpt2018 (BgIUT2).

---

## 6.3 [DISPUTED] Validity of the proof argument

### 6.3.1 Mochizuki position
(`claim:mochizuki_2012_proves_abc`, `claim:mochizuki_2018_response`, `claim:mochizuki_2025_october_report`)

Core claim: the multiradial algorithm furnishes a *legitimate* comparison between
distinct alien copies, and no canonical identification of the two ring theories is
possible or permissible.

Key statements:

- **Against (SSId)** (the SS assumption that the two ring structures can be canonically
  identified): Rpt2018 (SSADFs):
  > "The assertion of (SSAD) is false. The contradiction only occurs when one identifies
  > the hol. strs./ring theories in the domain and codomain of the Θ-link."
  That is, any contradiction found by SS occurs only in a *modified* version of IUTch
  in which distinct labels are collapsed — not in IUTch itself.

- **On the illegality of label deletion** (SSDLFs, Rpt2018 §12): deleting distinct
  labels is a *stronger* operation than eliminating Ind1/Ind2; it renders the
  multiradial algorithm inapplicable.

- **Against the "loop" reading** (Cmt2018-05 (C17), (C18)):
  > "log-volume を計算する際に commute が必要な 'loop' は Cor.3.12 の proof には
  > 決して現れない."
  No canonical identification of copies of **R**, and no commutative loop in the
  displayed diagram, appear in the proof. The Θ-pilot and q-pilot are embedded into a
  *single container* (with indeterminacies admitted), so commutativity of two distinct
  mappings is not an issue.

- **IUT-report-2025-10 §2.1 (SSA2)**:
  > SS's argument is "a SS-style interpretation/simplification of the set-up of
  > Cor.3.12" that has "no logical relationship" to the actual log-theta-lattice setup
  > and the proof of Cor.3.12.

- **Existence Principle (ExPr)** (IUT2025-10): the existence of an algorithm that
  yields no nontrivial consequence (the SS simplification) does not imply the
  non-existence of an algorithm that does (Cor.3.12).

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
  This is a precise characterization of the nature of the claimed defect: Thm 3.11 is
  not wrong as stated, but its content becomes vacuous once the alien-copy framework is
  resolved via consistent identifications.

- **On the O(ℓ²) blurring** (SS 2018, p.10):
  > "it seems to us that this statement means that the **blurring must be by a factor of
  > at least O(ℓ²)**, rendering the inequality thus obtained useless."
  This is SS's evaluation of Mochizuki's day-5 reply that indeterminacies allow the
  diagram to commute: if they do, the error term swamps the inequality.

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

Under this consistent choice, the abstract Θ-pilot object does *not* encode the
arithmetic degree of the Θ-divisor:
> "we saw that with these isomorphisms, the abstract Θ-pilot object does not encode
> the arithmetic degree of the Θ-divisor." (p.10)

Introducing the j² scalars on the left side then forces a monodromy inconsistency:
> "it is clear that this will result in the whole diagram having monodromy j², i.e.
> being **inconsistent**." (p.10)

### 6.4.2 Mochizuki counter-argument

- The j² scalars arise precisely *because* one does **not** identify the two ring
  structures. The γ_can trivialization is illegitimate from the IUTch standpoint
  because it collapses the inter-universal distinction maintained by Ind1/Ind2.

- The "inconsistency" SS identifies is real — but it is an inconsistency in a
  *different* mathematical object (a version of the setup with canonical identification
  imposed), not in IUTch as formulated.

- Cmt2018-05 (C17): the "loop" that would require commutativity never appears in the
  proof; the single-container embedding with admitted indeterminacies removes the
  need for such commutativity.

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
  have provided.

- **Mochizuki position** (`claim:mochizuki_2018_response`): the core of Cor.3.12
  depends on anabelian rigidity in a way that is invisible from SS's simplified setup;
  the rigidity is precisely what prevents arbitrary identification of distinct copies.

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
  once-punctured elliptic curve that is abstractly isomorphic to X." If Hodge theaters
  are only determined up to isomorphism over X, the claim that one has access to
  "distinct," "independent" theaters is questionable from SS's viewpoint.

- **Mochizuki position**: the inter-universal framework demands that distinct copies be
  treated as set-theoretically distinct objects. Their abstract isomorphism is
  irrelevant to the comparison performed across the Θ-link; distinctness is maintained
  at the level of the underlying set-theoretic universe, not at the level of abstract
  isomorphism class.

- This sub-dispute underlies much of the broader disagreement about whether the
  "alien copies" framework introduces genuine content or only notational overhead.

---

## 6.7 What is NOT in dispute (both sides agree)

| Item | Evidence |
|---|---|
| Existence of IUTchIII Cor.3.12 as a stated corollary | factual |
| Cor.3.12 as load-bearing step for IUT→abc | SS 2018 p.1; Rpt2018 (BgIUT2) |
| Multiradial algorithm (Thm 3.11) statement-level well-definedness | SS 2018 p.9 fn.12 |
| θ-link well-definedness as full poly-isomorphism | SS 2018 p.9 |
| log-shell I_v definition (Prop 1.2) | not contested by either party |
| Mochizuki's anabelian theorems themselves | SS 2018 p.5, Remark 9 |
| Ind1/Ind2/Ind3 are necessary (without them conclusion obviously false) | SS 2018 p.9 |
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
| LANA formalization project | Announced 2026-03-31; mid-report scheduled 2026-07-17 (PENDING); Lean 4 formalization of Hodge theater and Thm 3.11 underway; expected to require several more years (`claim:lana_formalization_in_progress`) |
| Joshi 2025 (arXiv:2505.10568 v1+v2) | Proposes corrected framework; preprint, not peer-reviewed; represents a third mathematical perspective (`claim:joshi_2025_alternative`) |
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

---

## Cross-reference

- **entities.json**: `iut:Cor.3.12`, `iut:multiradial_algorithm`, `iut:Ind1`, `iut:Ind2`,
  `iut:Ind3`, `iut:HodgeTheater`, `iut:theta_link`, `iut:log_link`, `iut:log_theta_lattice`

- **claims.json**: `claim:cor_3_12_neutral_statement`, `claim:mochizuki_2012_proves_abc`,
  `claim:mochizuki_2018_response`, `claim:mochizuki_2025_october_report`,
  `claim:scholze_stix_2018_main`, `claim:scholze_stix_2018_sub_1`,
  `claim:scholze_stix_2018_sub_2`, `claim:scholze_stix_2018_sub_3`,
  `claim:joshi_2025_alternative`, `claim:lana_formalization_in_progress`

- **timeline.json**: `event:2018_07_ss_report`, `event:2018_09_mochizuki_response`,
  `event:2021_prims_publication`, `event:2025_mochizuki_october_report`,
  `event:2026_lana_announcement`, `event:2026_lana_midreport_scheduled`

- **Section links**: Section 5 (multiradial algorithm + Ind1/2/3) ← this section →
  Section 7 (abc consequence) [docs/concepts/section_7_abc_consequence.md, 未作成]

---

## Verification log

| Claim | Verdict | Note |
|---|---|---|
| 6.1 Cor.3.12 statement existence + dependency | 3/3 ✅ | IUTchIII p.173–174 DOI confirmed |
| 6.2 mathematical content (mochizuki-side detail) | 1/3 [CLAIMED_BY: Mochizuki] | SS does not individually dispute constructions |
| 6.3 validity of proof argument | 0/3 [DISPUTED] | core of the 2018 disagreement |
| 6.4 empty inequality (specific objection) | 0/3 [DISPUTED] | γ_can vs. alien-copies framework |
| 6.5 anabelian essential-ness (sub_2) | 0/3 [DISPUTED] | Remark 9 vs. Mochizuki's rigidity argument |
| 6.6 Hodge theater distinction (sub_1) | 0/3 [DISPUTED] | equivalence-of-categories vs. set-theoretic distinctness |
| 6.7 not-in-dispute items | 3/3 ✅ | confirmed from both primary sources |
| 6.8 status as of 2026-05-06 | 3/3 ✅ | factual; no verdict implied |
| 6.9 forbidden translations | 3/3 ✅ | applied throughout |

---

## Sources

| 文書 | URL / DOI |
|---|---|
| IUTchIII Cor.3.12, pp.173–174 | DOI [10.4171/PRIMS/57-1-3](https://doi.org/10.4171/PRIMS/57-1-3) |
| Rpt2018 (Report on Discussions, Feb 2019) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Rpt2018.pdf |
| Cmt2018-05 (Comments on SS manuscript, Jul 2018) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-05.pdf |
| IUT-report-2025-10 (October 2025) | https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf |
| EssLgc (Essential Logical Structure, March 2024) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf |
| SS 2018 (Why abc is still a conjecture, Jul 2018) | https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
