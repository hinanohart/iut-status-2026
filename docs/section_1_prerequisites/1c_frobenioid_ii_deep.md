# 1c — Frobenioid II (Mochizuki framework, deep dive)

> 3-agent verify pending (mochizuki-side draft).
> Source: FrdII = "The Geometry of Frobenioids II: Poly-Frobenioids", Mochizuki, June 2008.
> URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf
> Published: Kyushu J. Math. 62 (2008), pp. 401–460 (72 pp. preprint).
> IUTchI cross-ref: p.2, Example 3.4 p.80, Example 3.5 pp.84–87, Def 5.2 (iv) p.134.
> PDF verified 2026-05-06 via pymupdf (72 pp.).

---

## 1c.1 Non-archimedean (p-adic) Frobenioid component (`iut:non_arch_frobenioid_component`)

**Locator**: FrdII Example 1.1, pp. 7–9; Theorem 1.2, pp. 9–10.

A **p-adic Frobenioid** `C` is the model Frobenioid over `D → D_0` (D_0 = finite étale
coverings of `Spec(Q_p)`) with divisor monoid `Φ ⊆ (Φ^Λ_0)|_D`. Monoid types:

| `Λ` | Divisor monoid | Notation |
|---|---|---|
| Z | `ord(O^▷_K)` ≅ Z≥0 | `C^Z = C` |
| Q | perfection, ≅ Q≥0 | `C^Q = C^pf` |
| R | realization, ≅ R≥0 | `C^R = C^rlf` (used in IUT) |

Thm 1.2: For arbitrary Λ, `C` is of isotropic, model, Aut-ample, quasi-Frobenius-trivial
type, not group-like; rationally standard type iff `D` is FSMFF-type.

**IUTchI usage**: Examples 3.2–3.3 (pp.69–79) construct `C_v` for `v ∈ V^non` as p-adic
Frobenioids via [FrdII] Ex.1.1(ii); IUTchI p.73 cites [FrdII] Thm 1.2(i) for
category-theoretic reconstruction of `D^⊢_v` from `C^⊢_v`.

---

## 1c.2 Archimedean Frobenioid component (`iut:archimedean_frobenioid_component`)

**Locator**: FrdII Example 3.3, pp. 27–29; Theorem 3.6, pp. 38–45.

Objects of the core category `C_0`: triples `(Spec(K), V_K, A_K)` where `V_K` is a
1-dim K-vector space and `A_K ⊆ V_K` is an **angular region**. Morphisms carry
Frobenius degree `d ∈ N≥1` and an isomorphism `V_L^⊗d →̃ V_K|_L` mapping `A_L^⊗d`
into `A_K|_L` (FrdII p.27–28). Divisor monoid: `Φ_0 : Spec(K) → ord(K^×) ≅ R≥0`.

Unlike the p-adic case, archimedean Frobenioids have non-isotropic objects and
non-co-angular morphisms, reflecting the geometry of `S^1 ⊆ C^×`. Lemma 3.2
(12 properties of connected open subsets of `S^1`) verifies the [FrdI] Def 1.3 axioms.

**IUTchI usage**: Example 3.4 (p.80) defines `C_v` for `v ∈ V^arc` as "the archimedean
Frobenioid as in [FrdII], Example 3.3, (ii)"; [FrdII] Thm 3.6(i)(vii) cited for
category-theoretic reconstruction of `O^▷(C_v)`. F-prime strip at `v ∈ V^arc`
(Def 5.2(i)(b), p.134) is `†F_v = (†C_v, †D_v, †κ_v)` with `†C_v` archimedean Frobenioid.

---

## 1c.3 Angular region (`iut:angular_region`)

**Locator**: FrdII Def 3.1(iii), p.24; Example 3.3, pp. 27–29.

For archimedean field `K`, an **angular region** `A ⊆ K^×` is a product `B × C` where
`B ⊆ O^×_K` is open and connected in each component of `O^×_K`, and `C = (0, λ] ⊆ R>0`.
Tip = λ; boundary `∂A = {a ∈ A | |a| = λ}`; **isotropic** iff `B = O^×_K`.

Role: objects of `C_0` are indexed by angular regions; isotropic objects of `C` coincide
with naively isotropic objects (FrdII p.28 via Lemma 3.2(i)). Tensor product of angular
regions is angular (FrdII p.24). The `S^1`-ambiguity of `O^×_K` encodes the angular
indeterminacy that feeds into Ind2 at archimedean primes in IUT.

---

## 1c.4 Global realified Frobenioid (`iut:global_realified_frobenioid`)

**Locator**: FrdII Example 5.6 (poly-Frobenioid, pp.62–65, Λ^⊚ = R);
IUTchI Example 3.5, pp.84–87 (primary IUT definition).

`C^⊩_mod` = realization (`Λ = R`) of [FrdI] Example 6.3 for the number field `F_mod`
with trivial Galois extension (one-morphism base category). Divisor monoid `Φ_{C^⊩_mod}`
is a single monoid with `Prime(C^⊩_mod) ↔ V_mod`; each submonoid at `v` is `≅ R≥0`.
Restriction isomorphisms: `ρ_v : Φ_{C^⊩_mod,v} →̃ Φ^rlf_{C^⊢_v}` both `≅ R≥0`
given by `log^⊢_mod(p_v) → [K_v:(F_mod)_v]^{-1} log^Φ(p_v)`.

Data `F^⊩_mod = (C^⊩_mod, Prime(C^⊩_mod) →̃ V, {F^⊢_v}, {ρ_v})` is the canonical
**F^⊩-prime-strip** (Def 5.2(iv), p.134). The **Θ-link** (Cor 3.7, p.88) is the
full poly-isomorphism `†F^⊩_tht →̃ ‡F^⊩_mod` — `C^⊩_mod` is the only global
Frobenioid-theoretic object that crosses the link.

IUTchI Remark 3.5.1(ii): "`C^⊩_mod`, `C^⊩_tht` may be thought of as 'devices for
currency exchange' between the various 'local currencies' [...] at the various `v ∈ V`."

---

## 1c.5 [DISPUTED] Essential role at Cor. 3.12

**Mochizuki position**: `C^⊩_mod` and the poly-Frobenioid framework of [FrdII] §5 are
essential: Theorem 5.5(iii) (FrdII p.58) guarantees category-theoretic reconstructibility
of `C^R` under equivalences, validating comparisons across the Θ-link through to Cor.3.12.

**Scholze-Stix critique (SS 2018, p.7)**: `C^⊩_mod` "simply amounts to a collection of
ordered 1-dimensional R-vector spaces `R_v` parametrized by the places `v`, together with
a subspace `D_0 ⊂ ⊕_v R_v` of codimension 1 [...] the category of global realified
Frobenioids is equivalent to the category of ordered 1-dimensional R-vector spaces."
If correct, the FrdII §5 apparatus is **dispensable** — the arithmetic content reduces to
a product formula on R≥0, adding no constraint beyond standard Arakelov geometry.

**Status**: `[DISPUTED]`. Both sides accept SS p.7's characterization of the category;
the dispute is whether the **identification process** across the Θ-link (using the
full Frobenioid-theoretic indeterminacies) carries nontrivial content not captured by
working directly with the R-line.

---

## Sources

- FrdII: Mochizuki 2008, Kyushu J. Math. 62 (2008), pp. 401–460.
  URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf
- IUTchI: URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf
- SS 2018: URL: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
