# Section 5c: Ind2 Frobenius-theoretic deep — Mochizuki-side draft

> status: mochizuki-side draft | 3-agent verify: pending | verified_at: 2026-05-06
> source: IUTchIII Thm 3.11-i (p. 154); Introduction pp. 9, 12; Prop 1.2 (vi)(vii) (pp. 32–33)
> new IRIs: `iut:Ind2_z_times_indeterminacy`, `iut:Ind2_o_times_mu_action`
> IRI flat; v0.2 schema; DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 5c.1 Ind2 two-component structure

Thm 3.11 (i), p. 154 — formal statement (verbatim):

> "(Ind2) for each vQ ∈ V^non_Q (respectively, vQ ∈ V^arc_Q), the indeterminacies
> induced by the action of independent copies of Ism [cf. Proposition 1.2, (vi)]
> (respectively, copies of each of the automorphisms of order 2 whose orbit
> constitutes the poly-automorphism discussed in Proposition 1.2, (vii)) on
> each of the direct summands of the j+1 factors appearing in the tensor product
> used to define IQ(S±_{j+1}; ^{n,◦}D^⊢_{vQ}) — where we recall that the
> cardinality of the collection of direct summands is equal to the cardinality
> of the set of v ∈ V that lie over vQ."

Introduction p. 12 — informal expansion (verbatim):

> "(Ind2): This is the ['non-(Ind1) portion' of the] indeterminacy that arises from
> the automorphisms of the F^{⊢×μ}-prime-strips that appear in the
> Θ-/Θ×μ-/Θ×μ_{gau}-/Θ×μ_{LGP}-/Θ×μ_{lgp}-link — i.e., in particular, at
> [for simplicity] v ∈ V^non, the Z×-indeterminacies acting on local copies of 'O×μ'."

| Sub-component | Acts on | Prop 1.2 ref |
|---|---|---|
| Z×-indeterminacy (v^non) | Ism-orbit on log(†D^⊢_v) → log(†F^{⊢×μ}_v) | (vi), p. 32 |
| {±1}-indeterminacy (v^arc) | poly-iso orbit on log(†D^⊢_v) | (vii), p. 33 |

---

## 5c.2 [iut:Ind2_z_times_indeterminacy] — Z×-indeterminacy from the Theta-link

**Domain**: local O×μ-components at v ∈ V^non in the F^{⊢×μ}-prime-strips
constituting the Θ×μ_{LGP}-link.

**Origin**: the horizontal arrows of the log-theta-lattice identify the respective
O×μ's on both sides "up to a residual Z×-indeterminacy" (Remark 1.4.1 (ii), p. 46).
Each nontrivial Z× element "obliterates the arithmetic holomorphic structure
currently under consideration" (Remark 1.4.2 (i), p. 48).

**Mechanism (Prop 1.2 (vi), p. 32)**: a "functorial algorithm in †F^{⊢×μ}_v for
constructing an **Ism-orbit** of isomorphisms log(†D^⊢_v) ~→ log(†F^{⊢×μ}_v)
of ind-topological modules." Ism = the Z×-automorphism group of O×μ.

**Insulation of Oμ**: the composite Oμ_{F_v} → O× ↠ O×μ is trivial (Introduction
p. 9), so Kummer theory of the étale theta function is insulated from Z×.
Consequently splitting monoids of LGP-monoids are compatible with (Ind2):
"the identity automorphism … is compatible … with the Θ×μ_{LGP}-link
[cf. the indeterminacy '(Ind2)']" (Theorem A §(ii), p. 21).

**At Cor 3.12**: (Ind2) requires a union over Ism-orbits in the holomorphic hull;
the Oμ insulation bounds the resulting log-volume contribution.

> Sources: Thm 3.11 (i) p. 154; Introduction pp. 9, 12, 21; Rem 1.4.1–2 pp. 46, 48; Prop 1.2 (vi) p. 32.

Status: **[CLAIMED_BY: Mochizuki]**

---

## 5c.3 [iut:Ind2_o_times_mu_action] — O×μ group action component

**Group**: O×μ := O× / Oμ. The Z×-action via Ism constitutes the
indeterminacy. At v^arc, {±1}-independent actions per direct factor (Prop 1.2 (vii), p. 33)
play the analogous role.

**Per-summand independence**: "independent copies of Ism" act on *each* direct
summand of the j+1-factor tensor product separately (Thm 3.11 (i), p. 154).
This independence requires a union (not average) over orbits in the global
log-volume computation.

**Role of F^{⊢×μ}**: O×μ is the unit-group component of the F^{⊢×μ}-prime-strip
that is preserved across the Theta-link (IUTchI Cor. 3.7 (ii)–(iii)). Its
Aut group = Z×-indeterminacy, making `iut:Ind2_o_times_mu_action` the
Frobenius-theoretic counterpart to étale-theoretic `iut:Ind1_d_prime_strip_aut`.

> Sources: Thm 3.11 (i) p. 154; Prop 1.2 (vi)(vii) pp. 32–33; IUTchI Cor. 3.7 (ii)–(iii).

Status: **[CLAIMED_BY: Mochizuki]**

---

## 5c.4 SS-side: analytical scope

SS 2018 p. 9: "(Ind 1,2,3)" — collective listing only. The Ism-orbit mechanism,
Prop 1.2 (vi)/(vii) distinction, per-summand independence, and Oμ insulation
argument are not addressed. SS's critique targets Cor 3.12 as a whole via the
j² monodromy argument (SS p. 10); the Frobenius-theoretic Ind2 components
are not within SS 2018's stated analytical scope.

Status: **[CLAIMED_BY: Mochizuki]**, **[OUT_OF_SCOPE: Scholze-Stix 2018]**

---

## Sources

| Reference | Content |
|---|---|
| IUTchIII Thm 3.11 (i), p. 154 | Ind2 verbatim; Ism-orbit; direct summands |
| IUTchIII Introduction p. 12 | Z×-indeterminacy on O×μ |
| IUTchIII Introduction p. 9 | Oμ insulation; horizontal-arrow origin |
| IUTchIII Introduction p. 21 | Ind2 compatibility with mono-theta environments |
| IUTchIII Prop 1.2 (vi)(vii), pp. 32–33 | Ism-orbit (v^non); {±1}-poly-iso (v^arc) |
| IUTchIII Rem 1.4.1 (ii), p. 46; Rem 1.4.2 (i), p. 48 | Z×-indeterminacy structural source |
| SS 2018 p. 9 | collective "(Ind 1,2,3)" |

- IUTchIII PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
- SS 2018 PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
