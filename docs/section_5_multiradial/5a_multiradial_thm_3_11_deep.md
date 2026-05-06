# Section 5a: Multiradial Representation — Thm 3.11 Deep (Mochizuki-side draft)

> Schema: v0.2
> Source: IUTchIII Thm 3.11 (pp. 153–158); Introduction §I3 (pp. 3, 10–16)
> PDF: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf>
> PRIMS DOI: <https://doi.org/10.4171/PRIMS/57-1-3>
> Phase: 5a (section 5 layer 1), mochizuki-side only
> Entities: 2 (iut:multiradial_representation_thm_3_11, iut:multiradiality_property)
> verified_at: 2026-05-06

---

## 5a.1 `iut:multiradiality_property` — conceptual definition (IUTchIII Intro, p. 3)

**IUTchIII Introduction, p. 3 (verbatim)**:

> "we recall that 'multiradial algorithms' [cf. the discussion of [IUTchII], Introduction]
> are algorithms that make sense from the point of view of an 'alien arithmetic
> holomorphic structure', i.e., the ring/scheme structure of a Θ±ellNF-Hodge theater
> related to a given Θ±ellNF-Hodge theater by means of a non-ring/scheme-theoretic
> Θ-/Θ×μ-/Θ×μ_gau-/Θ×μ_LGP-/Θ×μ_lgp-link."

A **uniradial** construction depends on the arithmetic holomorphic structure of one
specific vertical line `(n, ◦)` in the log-theta-lattice and cannot be referenced
from an alien vertical line `(n+1, ◦)` across a Θ×μ_LGP-link.
A **multiradial** construction is expressed in terms invariant under arbitrary
isomorphisms of the input F^{⊩▶×μ}-prime-strip (Thm 3.11-i, p. 154), making it
simultaneously valid from any vertical line.

**Introduction §I3 summary** (pp. 10–13): the "multiradialization" process involves
(1) replacing holomorphic F-/D-prime-strips by mono-analytic F^⊢-/D^⊢-prime-strips;
(2) forming tensor packets of log-shells over processions of D^⊢-prime-strips;
(3) passing to D^⊢-prime-strip data that is independent of any specific arithmetic
holomorphic structure.

**Source**: IUTchIII Introduction, pp. 3, 10–13.

---

## 5a.2 `iut:multiradial_representation_thm_3_11` — Thm 3.11 (i): formal statement

**Preamble** (IUTchIII p. 153):

> "We are now ready to discuss the main theorem of the present series of papers.
> Theorem 3.11. (Multiradial Algorithms via LGP-Monoids/Frobenioids)"

**§(i) Multiradial Representation** (IUTchIII pp. 153–154):

Consider the procession of D^⊢-prime-strips `Prc(^{n,◦}D^⊢_T)` and data (a) tensor
packets and log-shells, (b) splitting monoids `Ψ^⊥_LGP(^{n,◦}HT)_v` at `v ∈ V^bad`,
(c) number field embeddings and global Frobenioids `F^⊛_{MOD/mod}`.

Write `^{n,◦}R_LGP` for this data regarded up to indeterminacies:

**(Ind1)** verbatim (IUTchIII Thm 3.11 §(i), p. 154):

> "the indeterminacies induced by the automorphisms of the procession
> of D⊢-prime-strips Prc(^{n,◦}D^⊢_T);"

**(Ind2)** verbatim (IUTchIII Thm 3.11 §(i), p. 154):

> "for each vQ ∈ V^non_Q (respectively, vQ ∈ V^arc_Q), the indeterminacies induced
> by the action of independent copies of Ism [cf. Proposition 1.2, (vi)]
> (respectively, copies of each of the automorphisms of order 2 whose orbit
> constitutes the poly-automorphism discussed in Proposition 1.2, (vii)) on
> each of the direct summands of the j+1 factors appearing in the tensor
> product used to define IQ(S±_{j+1}; ^{n,◦}D^⊢_{vQ})"

Then `^{n,◦}R_LGP` is constructible via an algorithm functorial in isomorphisms of
`Prc(^{n,◦}D^⊢_T)`. For `n, n′ ∈ Z`, étale-picture permutation symmetries induce
compatible poly-isomorphisms `^{n,◦}R_LGP ~→ ^{n′,◦}R_LGP`.

**(Ind3)** verbatim (IUTchIII Thm 3.11 §(ii), p. 156):

> "as one varies m ∈ Z, the isomorphisms of (a) are 'upper semi-compatible',
> relative to the log-links of the n-th column of the LGP-Gaussian log-theta-lattice
> under consideration, in a sense that involves certain natural inclusions '⊆' at
> vQ ∈ V^non_Q and certain natural surjections '↠' at vQ ∈ V^arc_Q — cf.
> Proposition 3.5, (ii), (a), (b), for more details."

**Log-volume precision** (IUTchIII Thm 3.11 §(ii), p. 156): despite (Ind3),
the isomorphisms of (a) are **precisely** compatible with log-volumes as `m` varies
[cf. Prop 3.9, (iv)]. This precision is what makes Cor 3.12 yield a non-trivial bound.

**Remark 3.11.1 (i) summary** (IUTchIII p. 159):

> "Theorem 3.11 gives an algorithm for describing, up to certain relatively mild
> indeterminacies, the LGP-monoids … in terms of the a priori alien arithmetic
> holomorphic structure of another vertical line."

---

## 5a.3 SS-side: scope

SS 2018 references Thm 3.11 **twice** (p. 9, fn. 12; full-text extraction, pymupdf,
2026-05-06):

> (p. 9) "it is argued in [IUTT-3, Corollary 3.12] that the multiradial algorithm
> [IUTT-3, Theorem 3.11] implies that up to certain indeterminacies, e.g.
> (Ind 1,2,3) (without which the conclusion would be obviously false) …"

> (fn. 12, p. 9) "with the simplifications outlined above … the critical [IUTT-3,
> Theorem 3.11] does not become false, but trivial."

SS p. 3 states scope explicitly: "We focus on Corollary 3.12 and the step in its
proof which we find problematic." SS は Thm 3.11 の内部構造 (Ind1/Ind2/Ind3 の
個別技術評価、log-volume precision、étale-picture functoriality) に対する構造的
分析を行わない。SS の評価対象は Cor 3.12 の結論全体。

**Status**: [CLAIMED_BY: Mochizuki] for structural content of Thm 3.11 (i)(ii)(iii);
[DISPUTED] for non-triviality of the resulting inequality in Cor 3.12.

---

## Sources

| Reference | Content |
|---|---|
| IUTchIII Thm 3.11 §(i), pp. 153–154 | Ind1, Ind2 verbatim; multiradial representation |
| IUTchIII Thm 3.11 §(ii), pp. 155–156 | Ind3 verbatim; log-Kummer correspondence |
| IUTchIII Rem 3.11.1 (i), p. 159 | alien holomorphic structure summary |
| IUTchIII Introduction, pp. 3, 10–13 | multiradiality property definition |
| SS 2018, p. 9; fn. 12 | "trivial" claim; scope declaration |

- IUTchIII PDF: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf>
- IUTchIII PRIMS DOI: <https://doi.org/10.4171/PRIMS/57-1-3>
- SS PDF: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>
