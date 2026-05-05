# 1b — Frobenioid I (Mochizuki framework, deep dive)

> 3-agent verify pending (mochizuki-side draft).
> Source: FrdI = "The Geometry of Frobenioids I", Mochizuki, June 2008.
> URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf
> IUTchI cross-ref: §I1 p.2, p.13, Thm A p.13, Rmk 3.1.6 p.66.
> PDF verified 2026-05-06 via pymupdf (126 pp.).

---

## 1b.1 Frobenioid axioms (`iut:frobenioid_axioms`)

**Locator**: FrdI Definition 1.3, pp. 24–25.

A pre-Frobenioid `C → F_Φ` is a **Frobenioid** iff all seven conditions hold:

| # | Label (verbatim) | Core requirement |
|---|---|---|
| (i) | Surjectivity to base via pull-back morphisms | Pull-back subcategory `C^{pl-bk}_A →̃ D_{A_D}` is an equivalence; every isomorphism class of `D` lifts to a Frobenius-trivial object. |
| (ii) | Surjectivity to N≥1 via Frobenius-type morphisms | For every `A`, `n ∈ N≥1`, a morphism of Frobenius degree `n` exists and is essentially unique. |
| (iii) | Surjectivity to divisor monoid via co-angular morphisms | Co-angular pre-step subcategories are equivalent to `Order(Φ(A))`; bijection `O▷(A) →̃ O▷(B)` depending only on `Base(φ)`. |
| (iv) | Factorization of arbitrary morphisms | `φ = α ∘ β ∘ γ` (pull-back ∘ pre-step ∘ Frobenius type), essentially unique. |
| (v) | Factorization of pre-steps | Pre-step factors as isometric ∘ co-angular and co-angular ∘ isometric, each essentially unique; pre-step is a monomorphism. |
| (vi) | Faithfulness up to units | Base-equivalent, metrically equivalent co-angular pre-steps `A → B` differ by a unique `α ∈ O×(B)`. |
| (vii) | Isotropic objects | Every `A` has an essentially unique isotropic hull; any morphism from an isotropic object has isotropic codomain. |

---

## 1b.2 Factorization theorem (`iut:factorization_theorem`)

**Locator**: FrdI Def 1.3 (iv), p. 25 (axiom); Corollary 4.11 (pp. 91–94) for the main result.

**Axiom (iv)(a)** verbatim:
> "φ admits a factorization φ = α ∘ β ∘ γ where α is a pull-back morphism, β is a pre-step, and γ is a morphism of Frobenius type; this factorization is unique, up to replacing (α, β, γ) by (α ∘ δ, δ⁻¹ ∘ β ∘ ε, ε⁻¹ ∘ γ), where δ, ε are isomorphisms."

**Main reconstruction result (Cor 4.11)**: Under conditions "rationally standard type" and "Div-slim", any equivalence `Ψ: C₁ →̃ C₂` induces a 1-commutative diagram making `C → F_Φ` reconstructible purely category-theoretically. Stated in §I1 (p. 2) as the paper's central result.

---

## 1b.3 Base category (`iut:base_category_of_Frobenioid`)

**Locator**: FrdI Def 1.1 (ii)–(iv), pp. 19–21; §I4, pp. 8–9.

`D` is a connected, totally epimorphic category. The elementary Frobenioid `F_Φ`
over `D` has morphisms `φ: A → B` = triples `(φ_D, Div(φ), deg_Fr(φ))` where
`φ_D ∈ Arr(D)`, `Div(φ) ∈ Φ(A_D)`, `deg_Fr(φ) ∈ N≥1`. Composition rule
(Rmk 1.1.1, p. 21):
```
deg_Fr(φ ∘ ψ) = deg_Fr(φ) · deg_Fr(ψ)
Div(φ ∘ ψ)    = Base(ψ)*(Div(φ)) + deg_Fr(φ) · Div(ψ)
```

**FrdI §I4 dichotomy** (p. 9):
> "the structure of a ['permissible'] base category D [...] is fundamentally combinatorially different — indeed, different in a category-theoretically distinguishable fashion — from the structure of the 'Frobenius portion' F."

`D` is **étale-like** (indifferent to order; automorphism monoids are groups).
`N≥1`, `Z≥0` are **Frobenius-like** (order-conscious). IUTchI p. 13 recalls this
dichotomy verbatim as "key" to the whole theory.

---

## 1b.4 Degree function (`iut:degree_function`)

**Locator**: FrdI Def 1.1 (iii) p. 20; Def 1.2 (i) p. 21; Prop 1.5 (ii) p. 27.

On any morphism `φ` of a pre-Frobenioid:
- `deg_Fr(φ) ∈ N≥1`: Frobenius degree (multiplicative under composition).
- `Div(φ) ∈ Φ(A)`: zero divisor.
- **Linear**: `deg_Fr = 1`; **isometric**: `Div = 0`.
- `O▷(A)`: base-identity linear endomorphisms; `O×(A)`: units.

Prop 1.5 (ii): natural isomorphism `O▷(A) →̃ Φ(A)` for objects of `F_Φ`.

In IUT: the Frobenius-degree/zero-divisor data is the "Frobenius-like" arithmetic
content transported by the Θ-link. IUTchI Thm A (p. 13) calls a Hodge theater
"in essence, a system of Frobenioids."

---

## 1b.5 Perfection of a Frobenioid (conditional — included)

**Decision basis**: IUTchI Rmk 3.1.6 (p. 66) cites "perfection or the realization"
in direct connection with [FrdI] Frobenioids. FrdI Prop 3.2 is a key lemma for
Cor 4.11. Included per IUT proof-body locator requirement.

**Locator**: FrdI Def 3.1 (iii) pp. 56–57; Prop 3.2 (iii) p. 59.

For `C` of Frobenius-isotropic type, `C^pf` has objects = pairs `(A, n)` with
`n ∈ N≥1` ("n-th root of A"); morphisms = perfected morphisms (inductive limit
over Frobenius-type morphisms). Prop 3.2 (iii):

> "The category C^pf, equipped with the functor C^pf → F_{Φ^pf}, is a Frobenioid of perfect and isotropic type. Moreover, there is a natural equivalence C^pf →̃ (C^pf)^pf."

Effect on divisor monoid: `Z≥0 ⇝ Q≥0` (FrdI §I1, p. 4). The **realization**
(`Z≥0 ⇝ R≥0`) yields the global realified Frobenioid, which both sides treat in
the IUT dispute (SS 2018 p. 7: "equivalent to ordered 1-D R-vector spaces").

**Caution**: `C^pf` does not appear by name in the IUTchI Cor 3.12 proof chain
beyond Rmk 3.1.6; this entity is **[CLAIMED_BY: Mochizuki]** based on FrdI.

---

## How these entities support IUT

IUTchI p. 13 (before Thm A):
> "we recall the 'heuristic' notions of Frobenius-like — i.e., 'order-conscious' — and étale-like — i.e., 'indifferent to order' — mathematical structures discussed in [FrdI], §I4. These notions will play a key role in the theory developed in the present series of papers."

Thm A (p. 13): Hodge theater = "in essence, a system of Frobenioids." Θ-link
relates Frobenioid-theoretic portions incompatibly with ring structure (IUTchI
Abstract p. 1). Whether the full `[FrdI]` machinery does nontrivial work at
Cor 3.12 is **[DISPUTED]** — see `section_1_prerequisites.md` §1.2.

---

## Forbidden translations

- Do NOT equate base category `D` with a Grothendieck site or topos.
- Do NOT translate "étale-like vs. Frobenius-like" into perfectoid/condensed language.
- Do NOT conflate `iut:degree_function` (Frobenius degree on morphisms) with the
  global degree of an arithmetic line bundle (motivational, not definitionally equal).

## Sources

- FrdI: Mochizuki 2008, Kyushu J. Math. 63 (2009) no. 2.
  URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf
- IUTchI: URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf
- SS 2018: URL: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
