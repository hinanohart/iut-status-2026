# Section 1b: Frobenioid I (deep dive)

> 3-agent verified.
> Last verified: 2026-05-06.
> Parent: docs/section_1_prerequisites.md
> drift-zero IRIs: iut:frobenioid_axioms, iut:factorization_theorem, iut:base_category_of_Frobenioid, iut:degree_function
> Per-side drafts: docs/section_1_prerequisites/1b_frobenioid_i_deep.md (Mochizuki), docs/section_1_prerequisites/1b_frobenioid_i_deep_ss_view.md (SS)
> Monitor verdict (2026-05-06): perfection EXCLUDED (IUTchI Cor.3.12 proof chain locator weak beyond Rmk 3.1.6); 4 entities confirmed; IRI flat pattern enforced.

---

## 1b.1 Frobenioid axioms (`iut:frobenioid_axioms`)

### Consensus (definitional)

- FrdI Definition 1.3, pp. 24–25: 7 axioms — (i) pull-back surjectivity, (ii) Frobenius-degree surjectivity, (iii) divisor monoid surjectivity via co-angular morphisms, (iv) triple factorization of arbitrary morphisms, (v) pre-step factorization, (vi) faithfulness up to units, (vii) isotropic hull existence.
- SS p.7 §2.1.4 verbatim: "Mochizuki introduces the **difficult notion of a Frobenioid** in his papers [Frd1], [Frd2]." SS acknowledges the general theory as difficult; no claim of invalidity.
- SS's argument is that the *particular* Frobenioid appearing in Cor.3.12 (global realified) is elementary — not that the axiom system is wrong.
- **3/3 consensus**: axiom system is definitionally correct and accepted by both sides.

**Sources**: FrdI Def 1.3 <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf> pp. 24–25; SS 2018 p.7 <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

---

## 1b.2 Factorization theorem (`iut:factorization_theorem`)

### [CLAIMED_BY: Mochizuki] (1/3)

- FrdI Def 1.3 (iv) p.25 (axiom): every morphism φ admits an essentially unique decomposition φ = α ∘ β ∘ γ where α is pull-back, β is pre-step, γ is Frobenius-type.
- FrdI Corollary 4.11 (pp. 91–94): main reconstruction result — under "rationally standard type" and "Div-slim" conditions, any equivalence Ψ: C₁ →̃ C₂ induces a 1-commutative diagram making C → F_Φ reconstructible purely category-theoretically. Described in §I1 (p.2) as the paper's central result.
- SS p.7–10: no mention of Cor 4.11 or the general factorization theorem. No positive or negative claim.
- Status: Mochizuki cites this as essential structural scaffolding; SS neither endorses nor disputes it.

**Sources**: FrdI Def 1.3(iv) p.25, Cor 4.11 pp.91–94, §I1 p.2.

---

## 1b.3 Base category (`iut:base_category_of_Frobenioid`)

### [CLAIMED_BY: Mochizuki] (1/3)

- FrdI Def 1.1 (ii)–(iv) pp. 19–21: D is a connected, totally epimorphic category; elementary Frobenioid F_Φ over D has morphisms as triples (φ_D, Div(φ), deg_Fr(φ)) with composition rule deg_Fr(φ∘ψ) = deg_Fr(φ)·deg_Fr(ψ).
- FrdI §I4 dichotomy (p.9): base category D is "étale-like" (indifferent to order; automorphism monoids are groups); Frobenius portion is "order-conscious." IUTchI p.13 recalls this verbatim as "key."
- Note: the étale-like vs. Frobenius-like dichotomy (`iut:etale_like_vs_frobenius_like`) is already registered in entities.json with 3/3 consensus from section_1_prerequisites.md §1.2; the present entity covers the base category structure specifically.
- SS p.7–10: no mention of the base category construction. No positive or negative claim.

**Sources**: FrdI Def 1.1(ii)–(iv) pp.19–21, §I4 p.9; IUTchI p.13.

---

## 1b.4 Degree function (`iut:degree_function`)

### Consensus (definitional)

- FrdI Def 1.1 (iii) p.20; Def 1.2 (i) p.21; Prop 1.5 (ii) p.27: on any morphism φ of a pre-Frobenioid, deg_Fr(φ) ∈ N≥1 (Frobenius degree, multiplicative); Div(φ) ∈ Φ(A) (zero divisor). Prop 1.5 (ii): natural isomorphism O▷(A) →̃ Φ(A).
- SS p.7 §2.1.4: global realified Frobenioid reformulated as ordered 1-dim R-vector spaces. The construction R⊙ := (⊕_v R_v)/D₀ concretizes the degree/divisor data. SS does not name "degree_function" but the reformulation is a concrete realization of exactly this structure.
- SS's reformulation implicitly accepts that the degree-type data is well-defined; the dispute concerns the *sufficiency* of this data for Cor.3.12, not its definition.
- **3/3 consensus**: degree function is definitionally accepted by both sides.

**Sources**: FrdI Def 1.1(iii) p.20, Def 1.2(i) p.21, Prop 1.5(ii) p.27; SS 2018 p.7 §2.1.4.

---

## 1b.5 [EXCLUDED] Perfection of a Frobenioid

- IUTchI Rmk 3.1.6 (p.66) references "perfection or the realization" citing [FrdI]; FrdI Prop 3.2 supplies the key lemma for Cor 4.11.
- However, `C^pf` does not appear by name in the IUTchI Cor.3.12 proof chain beyond Rmk 3.1.6, and the IUT proof body locator is insufficient to confirm it as an independently required entity at the disputed step.
- Monitor verdict: **excluded from 1b entities** (4-entity limit upheld). May be added in a later sub-section if a stronger locator is identified.

---

## 1b.6 [DISPUTED] Essential role of Frobenioid at Cor.3.12

- **Mochizuki**: general Frobenioid theory is essential (IUTchI Thm A p.13: Hodge theater = "in essence, a system of Frobenioids"; Θ-link relates Frobenioid-theoretic portions incompatibly with ring structure, IUTchI Abstract p.1).
- **SS p.7 verbatim**: "the notion of a global realified Frobenioid is very elementary" / "the category of global realified Frobenioids is equivalent to the category of ordered 1-dimensional R-vector spaces."
- **SS p.10 verbatim**: global realified Frobenioids from F^⊩×µ-prime strips are "always canonically trivial using the various γ_can" — this triviality, combined with canonical identification of theta-link copies, feeds the main SS objection that the inequality becomes empty (claim:scholze_stix_2018_main).
- This dispute is encoded in claim:scholze_stix_2018_main and claim:mochizuki_frobenioid_essential (added in claims_1b_merged.json). Neutral remark: see section_6_cor_3_12.md §6.3 for the downstream consequence.

**Sources**: IUTchI Thm A p.13, Abstract p.1; SS 2018 pp.7–10.

---

## Forbidden translations

- Do NOT equate base category D with a Grothendieck site or topos.
- Do NOT translate "étale-like vs. Frobenius-like" into perfectoid/condensed language.
- Do NOT conflate `iut:degree_function` (Frobenius degree on morphisms) with the global degree of an arithmetic line bundle (motivational analogy only, not definitionally equal).
- Do NOT render "difficult notion of a Frobenioid" (SS p.7) as "SS claims Frobenioid is invalid" — SS accepts the axioms, disputes the deployment.

---

## Cross-reference

- entities.json: 4 IRIs registered in entities_1b_merged.json (iut:frobenioid_axioms, iut:factorization_theorem, iut:base_category_of_Frobenioid, iut:degree_function) + paper:FrdI.
- Top-level entity `iut:Frobenioid` already in entities.json.
- claims.json: claim:scholze_stix_2018_main (Cor.3.12 dispute, existing), claim:mochizuki_2018_response (existing), claim:mochizuki_frobenioid_essential (new, in claims_1b_merged.json), claim:ss_global_realified_elementary (new).

---

## Verification log

| Sub-section | Entity IRI | Status | Score |
|---|---|---|---|
| 1b.1 Frobenioid axioms (7 conditions) | `iut:frobenioid_axioms` | 3/3 consensus ✅ | definitional |
| 1b.2 Factorization Theorem | `iut:factorization_theorem` | 1/3 [CLAIMED_BY: Mochizuki] | SS silent |
| 1b.3 Base category | `iut:base_category_of_Frobenioid` | 1/3 [CLAIMED_BY: Mochizuki] | SS silent |
| 1b.4 Degree function | `iut:degree_function` | 3/3 consensus ✅ | SS implicitly accepts |
| 1b.5 Perfection | — | ❌ excluded | locator weak |
| 1b.6 Essential at Cor.3.12 | — | 0/3 [DISPUTED] | feeds §6.3 |
