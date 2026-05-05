# Section 1d: Étale Theta Function — etale class, absolute anabelian rigidity, Frobenioid-theoretic theta

> 3-agent verified.
> Last verified: 2026-05-06.
> Parent: docs/section_1_prerequisites.md
> drift-zero IRIs: iut:etale_theta_class, iut:absolute_anabelian_theta, iut:frobenioid_theoretic_theta
> Per-side drafts: 1d_etale_theta_deep.md (Mochizuki), 1d_etale_theta_deep_ss_view.md (SS)
> Monitor verdict (2026-05-06): 3 entities confirmed; scope judgments per SS PDF full-text search (pymupdf, pp. 7–10); IRI flat pattern enforced.

---

## 1d.1 Étale theta class (`iut:etale_theta_class`)

### [CLAIMED_BY: Mochizuki]

- EtTh §1, Prop. 1.3 (PDF pp. 18–19); "standard type" for the class at Def. 1.9 (PDF p. 27).
  Def. 2.7 (PDF p. 38) separately defines "standard type" for *l-th root* orbits — presupposes Def. 1.9 and the §2 degree-l covering; the two definitions are distinct.
- **Prop. 1.3 (paraphrase)**: Let `X^log` be a smooth log curve of type (1,1) over a nonarchimedean mixed-characteristic local field `K`. The discrepancy between two natural `Π^tp_Y`-actions — one from Prop. 1.1(ii), one from the theta trivialization of Lem. 1.2 — on constant multiples of `τ_N` determines a cohomology class
  ```
  η^Θ_N ∈ H¹(Π^tp_Y, (½·ℤ/Nℤ)(1)) ≅ H¹(Π^tp_Y, Δ_Θ ⊗ (½·ℤ/Nℤ))
  ```
  Taking `N → ∞` yields `O^×_{K/K̈} · η^Θ ∈ H¹(Π^tp_Y, ½Δ_Θ)`. Any element of the resulting set is called **the étale theta class**.
- SS 2018 全文 (pymupdf, 全 10 ページ): "étale theta" / "etale theta" / "EtTh" の出現 0 件。[EtTh] は SS 参考文献リストに存在しない。SS は `q_v^{j²}` の存在を前提として受け入れるが、その値を生成する EtTh §1 の定式化には触れない。否定も肯定も行っていない。
- **判定**: `[CLAIMED_BY: Mochizuki]` (1/3 — SS scope 外).

**Sources**: EtTh Prop. 1.3 pp. 18–19, Def. 1.9 p. 27, Def. 2.7 p. 38 <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>; SS 2018 (not found) <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

---

## 1d.2 Absolute anabelian theta (`iut:absolute_anabelian_theta`)

### 3/3 consensus (construction acknowledged, not disputed)

- EtTh Thm. 1.10 (PDF pp. 27–28), title: "Constant Multiple Rigidity of the Étale Theta Function".
- **Thm. 1.10 (paraphrase)**: For `□ = α, β`, let `Ċ^log_□` be a smooth log curve of type `(1, μ₂)^±` over a finite extension `K_□/ℚ_p` containing `√−1`. Let `γ : Π^tp_{Ċ_α} →̃ Π^tp_{Ċ_β}` be an isomorphism mapping `η̈^Θ_ℤ_α → η̈^Θ_ℤ_β`. Then: (i) `γ` preserves the standard-type property, which determines `η̈^Θ_ℤ_□` **up to multiplication by ±1**; (ii) the induced `K^×_α →̃ K^×_β` preserves the standard value sets; (iii) if residue characteristic is odd, `η̈^Θ_ℤ_□` of standard type determines a `{±1}`-structure on the `(K^×_□)^∧`-torsor at the cusp, compatible with the canonical integral structure and preserved by arbitrary `γ`.
- Key feature: rigidity holds for the full `Π^tp_Ċ`, not only the theta quotient `(Π^tp_C)^Θ` (Rem. 1.10.3).
- SS p. 8 §2.1.8 verbatim: "Mochizuki devises an **ingenious algorithm** to recover this data very directly from the data of π₁(X) acting on a certain monoid of divisors on **tempered coverings** of X." SS fn. 11 notes the `ℓ⋇`-multiplicity issue (diagonal copy / averaging) but does not dispute the algorithm's validity.
- SS 批判の焦点は「π₁(X) から `q_v^{j²}` を recover できるか」ではなく、「recover した値を abstract F^{⊩×µ}-prime strip に置いた後の ℝ-copies identification が consistent か」。
- **判定**: 3/3 consensus ✅ (construction accepted by both sides).

**Sources**: EtTh Thm. 1.10 pp. 27–28, Rem. 1.10.3 pp. 28–29; SS 2018 p. 8 §2.1.8 <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

---

## 1d.3 Frobenioid-theoretic theta (`iut:frobenioid_theoretic_theta`)

### 3/3 consensus (construction level) + [DISPUTED] (essential role at Cor. 3.12)

- EtTh Thm. 5.10 (PDF pp. 97–98), title: "Category-theoreticity of Frobenioid-theoretic Theta Environments".
- **Thm. 5.10(iii) (paraphrase)**: Let `Ψ : C →̃ C` be a self-equivalence of the tempered Frobenioid arising from `X^log`. The operation of applying `Ψ` followed by conjugation by `β` preserves the `Aut_C(B_N)`-orbit of `ε : E^Π_N → Aut_C(B_N)`, in a fashion compatible with the mono-theta environment structure. More precisely, there exists a commutative diagram with `γ` an automorphism of mono-theta environments and `κ` an inner automorphism. Rem. 5.10.1: "a mono-theta environment may be 'extracted' from the tempered Frobenioids in a purely category-theoretic fashion."
- SS p. 8 §2.1.8 verbatim: "Up to some 2ℓ-th roots of unity, these arise naturally as the values of a Θ-function at certain 2ℓ-torsion points" — SS accepts the existence and origin of Θ-function values; constructs `F^{⊩×µ}_Θ = (G_v ↷ o^{×µ}_{k̄_v} × ((q_v^{j²})_{j=1,…,ℓ⋇})^ℕ)`, which reflects the Frobenioid-theoretic side of Thm. 5.10.
- SS 批判は構成後の段階 — abstract pilot object が R⊙,Θ に encode される際に j²-scaling が生じ、Θ-link 全体図に monodromy が生じること — に向けられる (SS p. 9–10 §2.2)。Thm. 5.10 の category-theoretic extraction 自体は争点外。
- **判定**: 3/3 consensus ✅ (construction level) + `[DISPUTED]` (Cor. 3.12 での essential 性)。

**Sources**: EtTh Thm. 5.10 pp. 97–98, Lem. 5.9 p. 96, Rem. 5.10.1 p. 100; IUTchII §1 theta-pilot <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf>; SS 2018 pp. 8–10 §2.1.8–§2.2.

---

## How these support IUT

- `iut:etale_theta_class` (Prop. 1.3) supplies the Kummer class `η̈^Θ` as the fundamental cohomological object encoding the theta function of a Tate curve — the raw material for all downstream constructions.
- `iut:absolute_anabelian_theta` (Thm. 1.10) establishes constant multiple rigidity: `η̈^Θ` is determined up to `±1` by the topological group `Π^tp_Ċ` alone. This is a prerequisite for treating the theta class as a "group-theoretic" object in IUTchI–II.
- `iut:frobenioid_theoretic_theta` (Thm. 5.10) establishes that the mono-theta environment (Def. 2.13) — the common core of the étale-theoretic and Frobenioid-theoretic approaches — can be extracted category-theoretically from a tempered Frobenioid.
- In IUTchII §1, the theta-pilot object is constructed via this mono-theta environment; the three rigidity properties of Cor. 2.19 (cyclotomic, discrete, constant-multiple) are essential for the Θ-link to carry well-defined arithmetic data.
- In IUTchIII Cor. 3.12, multiradiality of the theta monoids relies on constant-multiple rigidity (Cor. 2.19(iii) + Thm. 5.10(iii)) to ensure independence under `Aut(Π^tp)` indeterminacies.

---

## Forbidden translations

- "Def. 2.7 = definition of étale theta class" — wrong: Def. 2.7 defines "standard type" for l-th root orbits in §2; the étale theta class itself is Prop. 1.3.
- "Thm. 1.10 = anabelian reconstruction of theta" — more precisely, it establishes *constant multiple rigidity*; full reconstruction is Thm. 1.6.
- "mono-theta environment = bi-theta environment" — mono-theta (Def. 2.13(ii)) omits the algebraic section `s^alg`; bi-theta (Def. 2.13(iii)) includes it. Discrete rigidity holds for mono- but fails for bi- (Cor. 2.16, Rem. 2.16.1).
- "SS denied the étale theta function" — SS 全文に "étale theta" 0 件。SS は construction を論じておらず、批判は downstream の ℝ-copies identification に集中する。

---

## Cross-reference

- entities.json: 3 IRIs → entities_1d_merged.json (新規 standalone ファイル).
- claims.json: claim:tempered_rigidity_acknowledged (新規), claim:frobenioid_theta_construction_accepted (新規) → claims_1d_merged.json.

---

## Verification log

| Sub-section | Entity IRI | Status | Score |
|---|---|---|---|
| 1d.1 étale theta class | `iut:etale_theta_class` | [CLAIMED_BY: Mochizuki] | SS scope 外 (1/3) |
| 1d.2 absolute anabelian theta | `iut:absolute_anabelian_theta` | 3/3 consensus ✅ | SS §2.1.8 "ingenious" |
| 1d.3 Frobenioid-theoretic theta (construction) | `iut:frobenioid_theoretic_theta` | 3/3 consensus ✅ | SS construction accepted |
| 1d.3 essential role at Cor. 3.12 | — | [DISPUTED] | SS p. 9–10 j²-scaling |
