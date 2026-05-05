# Section 1c: Frobenioid II — global realified, components, angular region

> 3-agent verified.
> Last verified: 2026-05-06.
> Parent: docs/section_1_prerequisites.md
> drift-zero IRIs: iut:global_realified_frobenioid, iut:archimedean_frobenioid_component, iut:non_arch_frobenioid_component, iut:angular_region
> Per-side drafts: 1c_frobenioid_ii_deep.md (Mochizuki), 1c_frobenioid_ii_deep_ss_view.md (SS)
> Monitor verdict (2026-05-06): 4 entities confirmed; scope judgments per SS PDF full-text search (pymupdf); IRI flat pattern enforced.

---

## 1c.1 Global realified Frobenioid (`iut:global_realified_frobenioid`)

### Consensus (definitional)

- FrdII Example 5.6 (pp. 62–65, Λ^⊚ = R); IUTchI Example 3.5 (pp. 84–87, primary IUT definition).
- `C^⊩_mod` = realization (Λ = R) of [FrdI] Example 6.3 for the number field `F_mod` with trivial Galois extension (one-morphism base category). Divisor monoid `Φ_{C^⊩_mod}` has `Prime(C^⊩_mod) ↔ V_mod`; each submonoid at v is ≅ R≥0. Restriction isomorphisms `ρ_v : Φ_{C^⊩_mod,v} →̃ Φ^rlf_{C^⊢_v}` both ≅ R≥0.
- Data `F^⊩_mod = (C^⊩_mod, Prime(C^⊩_mod) →̃ V, {F^⊢_v}, {ρ_v})` is the canonical F^⊩-prime-strip (IUTchI Def 5.2(iv), p. 134). The Θ-link (Cor. 3.7, p. 88) is the full poly-isomorphism `†F^⊩_tht →̃ ‡F^⊩_mod` — `C^⊩_mod` is the only global Frobenioid-theoretic object that crosses the link.
- SS p. 7 §2.1.4 verbatim: "the notion of a global realified Frobenioid is very elementary, cf. [IUTT-1, Example 3.5]."
- SS p. 7 characterization (verbatim): "it simply amounts to a collection of **ordered 1-dimensional R-vector spaces** R_v parametrized by the places v of k, together with a subspace D₀ ⊂ ⊕_v R_v of codimension 1 [...] the **category of global realified Frobenioids is equivalent to the category of ordered 1-dimensional R-vector spaces**."
- Both sides accept the SS p. 7 characterization as a correct categorical equivalence. **3/3 consensus** on the definition and the equivalence statement.

**Sources**: FrdII Ex. 5.6 pp. 62–65 <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf>; IUTchI Ex. 3.5 pp. 84–87, Def 5.2(iv) p. 134 <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>; SS 2018 p. 7 §2.1.4 <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

### [DISPUTED] Essential role at Cor. 3.12

- **Mochizuki**: FrdII Theorem 5.5(iii) (p. 58) guarantees category-theoretic reconstructibility of `C^R` under equivalences, validating comparisons across the Θ-link through to Cor. 3.12. IUTchI Remark 3.5.1(ii): `C^⊩_mod`, `C^⊩_tht` are "devices for currency exchange between the various 'local currencies' at the various v ∈ V."
- **SS p. 10 verbatim**: global realified Frobenioids from F^⊩×µ-prime strips are "always canonically trivial using the various γ_can" — this canonical trivialization, combined with canonical identification of Θ-link copies, produces an empty inequality (claim:scholze_stix_2018_main).
- **Status**: `[DISPUTED]`. The categorical equivalence (ordered 1-dim R-vec) is agreed; the dispute is whether the indeterminacy-tracking structure of the poly-Frobenioid framework carries content not captured by the R-line alone.

---

## 1c.2 Archimedean Frobenioid component (`iut:archimedean_frobenioid_component`)

### [CLAIMED_BY: Mochizuki] (SS scope 外)

- FrdII Example 3.3 (pp. 27–29); Theorem 3.6 (pp. 38–45).
- Objects of the core category `C_0`: triples `(Spec(K), V_K, A_K)` where `V_K` is a 1-dim K-vector space and `A_K ⊆ V_K` is an angular region. Divisor monoid: `Φ_0 : Spec(K) → ord(K^×) ≅ R≥0`. Unlike the p-adic case, archimedean Frobenioids have non-isotropic objects reflecting the `S^1 ⊆ C^×` geometry.
- IUTchI Example 3.4 (p. 80) defines `C_v` for `v ∈ V^arc` as "the archimedean Frobenioid as in [FrdII], Example 3.3, (ii)"; FrdII Thm 3.6(i)(vii) cited for category-theoretic reconstruction of `O^▷(C_v)`. F-prime strip at `v ∈ V^arc` (Def 5.2(i)(b), p. 134): `†F_v = (†C_v, †D_v, †κ_v)` with `†C_v` archimedean Frobenioid.
- SS p. 7–8 全文検索: "archimedean Frobenioid" 出現なし (pymupdf). p. 7 の archimedean place への言及は D₀ 定義中の "2π at infinite places" のみ — 独立した対象としての論及なし。
- **判定**: SS scope 外。`[CLAIMED_BY: Mochizuki]` (1/3).

**Sources**: FrdII Ex. 3.3 pp. 27–29, Thm 3.6 pp. 38–45; IUTchI Ex. 3.4 p. 80, Def 5.2(i)(b) p. 134; SS 2018 (not found).

---

## 1c.3 Non-archimedean (p-adic) Frobenioid component (`iut:non_arch_frobenioid_component`)

### [CLAIMED_BY: Mochizuki] (SS scope 外)

- FrdII Example 1.1 (pp. 7–9); Theorem 1.2 (pp. 9–10).
- Model Frobenioid over `D → D_0` (D_0 = finite étale coverings of `Spec(Q_p)`) with divisor monoid `Φ ⊆ (Φ^Λ_0)|_D`. R-realization (`Λ = R`) yields `C^rlf` used in IUT. Thm 1.2: `C` is isotropic, model, Aut-ample, quasi-Frobenius-trivial, not group-like; rationally standard type iff D is FSMFF-type.
- IUTchI Examples 3.2–3.3 (pp. 69–79) construct `C_v` for `v ∈ V^non` via [FrdII] Ex. 1.1(ii); IUTchI p. 73 cites FrdII Thm 1.2(i) for category-theoretic reconstruction of `D^⊢_v` from `C^⊢_v`.
- SS p. 7–8 全文検索: "non-archimedean Frobenioid" 出現なし (pymupdf). p. 7–8 の non-archimedean 言及は F^{⊩×µ}-prime strip の構造記述 (`G_v ↷ o^{×µ}_{k̄_v} × o_{k̄_v}`) のみ — Frobenioid としての定式化ではない。
- **判定**: SS scope 外。`[CLAIMED_BY: Mochizuki]` (1/3).

**Sources**: FrdII Ex. 1.1 pp. 7–9, Thm 1.2 pp. 9–10; IUTchI Ex. 3.2–3.3 pp. 69–79; SS 2018 (not found).

---

## 1c.4 Angular region (`iut:angular_region`)

### [CLAIMED_BY: Mochizuki] (SS PDF 出現なし)

- FrdII Definition 3.1(iii) (p. 24); Example 3.3 (pp. 27–29); IUTchI Definition 3.1(vii).
- For archimedean field K, an angular region `A ⊆ K^×` is a product `B × C` where `B ⊆ O^×_K` is open and connected in each component of `O^×_K`, and `C = (0, λ] ⊆ R>0`. Tip = λ; isotropic iff `B = O^×_K`. Tensor product of angular regions is angular (FrdII p. 24).
- Role: objects of `C_0` (archimedean Frobenioid) indexed by angular regions. The S^1-ambiguity of `O^×_K` encodes the angular indeterminacy feeding into Ind2 at archimedean primes in IUT.
- SS 全文検索 (PDF 全ページ): "angular region" 出現なし (pymupdf).
- **判定**: `[CLAIMED_BY: Mochizuki]` (0/3 — SS 側からの検証も反論も存在しない).

**Sources**: FrdII Def 3.1(iii) p. 24, Ex. 3.3 pp. 27–29; IUTchI Def 3.1(vii); SS 2018 (not found).

---

## Forbidden translations

- Do NOT render "category of global realified Frobenioids ≡ ordered 1-dim R-vec" (SS p. 7) as "Mochizuki's Frobenioid is incorrect" — SS accepts the definition, disputes the necessity of the apparatus at Cor. 3.12.
- Do NOT equate the archimedean Frobenioid component with the archimedean part of an Arakelov line bundle — motivational analogy only.
- Do NOT conflate angular region `A ⊆ K^×` with a "sector" in elementary complex analysis; the combinatorial axioms (Lemma 3.2, 12 properties) are required.
- Do NOT assert that SS silence on iut:archimedean_frobenioid_component / iut:non_arch_frobenioid_component / iut:angular_region implies endorsement; it implies only that SS did not engage with those objects.

---

## Cross-reference

- entities.json: 4 IRIs + paper:FrdII → entities_1c_merged.json.
- claims.json: claim:scholze_stix_2018_main (existing, Cor. 3.12 dispute), claim:ss_global_realified_canonical_trivial (new, claims_1c_merged.json).

---

## Verification log

| Sub-section | Entity IRI | Status | Score |
|---|---|---|---|
| 1c.1 global realified definition | `iut:global_realified_frobenioid` | 3/3 consensus ✅ | both sides accept |
| 1c.1 essential at Cor. 3.12 | — | 0/3 [DISPUTED] | SS p. 10 γ_can trivial |
| 1c.2 archimedean component | `iut:archimedean_frobenioid_component` | 1/3 [CLAIMED_BY: Mochizuki] | SS scope 外 |
| 1c.3 non-arch component | `iut:non_arch_frobenioid_component` | 1/3 [CLAIMED_BY: Mochizuki] | SS scope 外 |
| 1c.4 angular region | `iut:angular_region` | 0/3 [CLAIMED_BY: Mochizuki] | SS PDF 出現なし |
