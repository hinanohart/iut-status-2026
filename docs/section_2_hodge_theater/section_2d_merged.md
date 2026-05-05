# Section 2d: Prime-Strip Variants — 3-agent merged

> Status: MERGED (mochizuki-side + SS-side). 2026-05-06.
> IRIs: `iut:D_prime_strip`, `iut:F_top_prime_strip`, `iut:F_LGP_prime_strip`, `iut:procession`
> Primary sources: IUTchI Def 4.1/5.2/Prop 6.9; IUTchII Def 4.9; IUTchIII Def 3.8/Cor 3.12.
> SS source: Scholze-Stix 2018 (SS), 10 pp., full-text PDF-verified 2026-05-06.

---

## 2d.1 D-prime-strip (`iut:D_prime_strip`)

**IUTchI Definition 4.1 (i)/(iii), pp. 95–96.**

A **D-prime-strip** is a collection indexed over all places:
```
†D = { †D_v }_{v ∈ V}
```
- v ∈ V^{non}: †D_v is a category equivalent to D_v (holomorphic Galois-category type).
- v ∈ V^{arc}: †D_v is an Aut-holomorphic orbispace isomorphic to D_v.

The **D⊢-prime-strip** (Def 4.1 iii, *mono-analytic base-prime-strip*) is its mono-analyticization:
replaces holomorphic categories by `B(G_v)^0` type at non-archimedean places and the `TM⊢`
object at archimedean places. Natural functor: D-prime-strip → D⊢-prime-strip (Def 4.1 iv).

**LabCusp(†D)** carries a canonical F^⋇_l-torsor structure and canonical element (Prop 4.2).

**W1 note:** D-prime-strip is the base-category (D-level) component underlying all
Frobenioid-level constructions. Every F-prime-strip, F⊢-strip, F⊩×μ-strip, and
F⊩▶×μ-strip has a D-prime-strip as its underlying base-category data.

**SS attitude:** SS 2018 full-text — `D-prime` (ハイフン区切り): 0 occurrences.
SS does not independently discuss D-prime-strips; it works directly at the `F^⊩×μ` level
(SS §2.1.5, p. 7). The D-level base-category structure is subsumed under SS's
equivalence-of-categories argument without decomposition.

---

## 2d.2 F⊢-prime-strip (mono-analytic Frobenioid-prime-strip) (`iut:F_top_prime_strip`)

**IUTchI Definition 5.2 (ii)/(iv), pp. 134–136.**

An **F⊢-prime-strip** is a collection:
```
‡F⊢ = { ‡F⊢_v }_{v ∈ V}
```
- v ∈ V^{non}: ‡F⊢_v is a split Frobenioid (underlying Frobenioid ‡C⊢_v) isomorphic to F⊢_v.
- v ∈ V^{arc}: ‡F⊢_v is a triple (Frobenioid ‡C⊢_v, TM⊢ object, splitting) isomorphic to F⊢_v.

Distinction from F-prime-strip (Def 5.2 i): F-prime-strip is holomorphic (per-place Frobenioid
‡C_v ≃ C_v); F⊢-prime-strip is **mono-analytic** (forgets holomorphic structure).

**F⊩-prime-strip** (Def 5.2 iv, "globally realified mono-analytic"):
```
‡F⊩ = (‡C⊩, Prime(‡C⊩) →∼ V, ‡F⊢, {‡ρ_v}_{v∈V})
```
Adds a global realified Frobenioid ‡C⊩ ≃ C⊩_mod with local-global comparison maps
‡ρ_v : Φ_{‡C⊩,v} →∼ Φ^{rlf}_{‡C⊢_v}.

**Specialization chain** (informal):
```
iut:F_prime_strip  →  iut:F_top_prime_strip (F⊢, mono-analytic)
                          →  iut:F_modulus_prime_strip (F⊩×μ, adds ×μ-Kummer)
                                 →  F⊩▶×μ (adds ▶×μ splitting)
                                        →  iut:F_LGP_prime_strip (LGP/lgp evaluation)
```

**W2 note:** `iut:F_top_prime_strip` (F⊢) is a *sub-component* of `iut:F_modulus_prime_strip`
(F⊩×μ, already in entities.json). The F⊩ step (global realification) intervenes between them.

**SS attitude:** `F^⊢` (vdash): 0 occurrences in SS 2018 full-text.
SS bypasses the F⊢ level and works directly with `F^⊩×μ` (§2.1.5 onwards). The mono-analytic
structure of F⊢ is implicitly encoded in SS's description of local components as pairs
`G_v ⟲ o×μ_{k̄_v} × N` — but the intermediate F⊢ layer is not analyzed.

---

## 2d.3 F⊩▶×μ_LGP-prime-strip (Logarithmic Gaussian Procession strip) (`iut:F_LGP_prime_strip`)

**IUTchII Definition 4.9 (vii)/(viii) + IUTchIII Definition 3.8 (ii), pp. 113–114.**

**IUTchII Def 4.9 context** — For □ ∈ {×, ×μ, ▶×μ}, an F⊢□-prime-strip is
`{*F⊢□_v}_{v∈V}` where each local component is the corresponding Kummer-Frobenioid variant.

The **F⊩▶×μ-prime-strip** (Def 4.9 viii) takes the shape:
```
*F⊩▶×μ = (*C⊩, Prime(*C⊩) →∼ V, *F⊢▶×μ, {*ρ_v}_{v∈V})
```
The *pilot object* is defined here and governs the Θ×μ_LGP-link.

**IUTchIII Def 3.8 (ii)** specializes this to:
- †F⊩▶×μ_LGP: built from LGP-Gaussian monoids (MOD-type, global realified).
- †F⊩▶×μ_lgp: built from lgp-Gaussian monoids (mod-type, local, secondary variant).
- **Θ×μ_LGP-link**: full poly-isomorphism `†F⊩▶×μ_LGP →∼ *F⊩▶×μ_△`.
- **Θ×μ_lgp-link**: full poly-isomorphism `†F⊩▶×μ_lgp →∼ *F⊩▶×μ_△`.

**LGP** = "Logarithmic Gaussian Procession": the j-indexed splitting monoids of Gaussian monoids
rendered multiradial via procession indexing (IUTchIII Theorem A title, p. 19). LGP is the
primary variant in Cor 3.12; lgp is the auxiliary (lgp-normalized) variant.

**W3 note:** LGP and lgp share the same structural template; only the global Frobenioid
type differs (MOD vs. mod). The LGP-link carries the essential j² arithmetic (q_v^{j²},
j = 1,…,l*) that Mochizuki considers irreducible to a generator name swap.

**SS attitude:** `LGP` / `F^⊩LGP`: 0 occurrences in SS 2018 full-text (SS does not use this
notation). SS reaches `F^⊩×μ` as the deepest prime-strip variant it discusses. The ▶×μ and LGP
elaboration layers are outside SS's stated scope (SS §2.2 p. 9 treats Cor 3.12 in summary form).

---

## 2d.4 Procession of prime-strips (`iut:procession`)

**IUTchI Proposition 6.9 (i), pp. 169–170 + IUTchIII §3 (Ind1, Theorem A).**

A **procession** (l±-procession of D-prime-strips) is a diagram of capsule inclusions:
```
S±_1 → S±_2 → ... → S±_{l±}
```
where S±_{j+1} = {0, 1, …, j} and each S±_{j+1} indexes a capsule of D-prime-strips
(holomorphic variant) or D⊢-prime-strips (mono-analytic variant).

**Construction (Prop 6.9 i):** Given a D-Θ±-bridge †φ^{Θ±}_± : †D_T → †D_≻, the procession
`Prc(†D_T)` corresponds to sub-capsules indexed by S±_1 ⊆ … ⊆ S±_{l±} = |F_l| via
the bijection |T| →∼ |F_l|.

**Label-indeterminacy reduction:** This diagram reduces the indeterminacy from (l±)^{l±}
to l±! — critical for log-volume estimates in IUTchIV (cf. IUTchIII Ind1 = permutation
automorphisms of procession).

**Role in IUTchIII Theorem A (Cor 3.12):** The multiradial algorithm is a functor in
`Prc(^{n,◦}D⊢_T)` (procession of D⊢-prime-strips). The "procession-normalized mono-analytic
log-volume" averages over j ∈ F⋇_l indexed by the procession, yielding a finite bound.

**W4 note:** procession is a *functor-output diagram of capsules*, NOT a prime-strip itself.
It depends on `iut:D_prime_strip` but is categorically distinct from any prime-strip variant.

**SS attitude (claim:ss_f_modulus_strip_focal):** SS 2018 — `procession`: exactly 1 occurrence
(§2.2, p. 9), in the summary phrase "processions of tensor packets of log-shells".
SS does not define or decompose the procession structure; it appears as part of Cor 3.12
quoted in passing. SS §2.2 treats the procession as outside its analytical scope,
framing the entire Cor 3.12 through the lens of Θ-link triviality.

SS p. 4 (Excuse 1): "During our discussion in Kyoto, Mochizuki agreed that some of these
simplifications are OK, **for example regarding the critical notion of F⊩×μ-prime strips below**."
This situates `F^⊩×μ` as the focal point of SS's prime-strip analysis; all other variants
(D, F⊢, LGP, procession) fall outside SS's stated simplification scope.

---

## Cross-entity stance summary

| IRI | Mochizuki | SS | Status |
|---|---|---|---|
| `iut:D_prime_strip` | base-category D-level, essential for all F-level constructions | 0 occurrences, implicitly subsumed | Mochizuki-side only |
| `iut:F_top_prime_strip` | mono-analytic Frobenioid layer; essential bridge F→F⊩ | 0 occurrences (F⊢ skipped) | Mochizuki-side only |
| `iut:F_LGP_prime_strip` | j²-scaling essential; irreducible to name swap | 0 occurrences (LGP outside scope) | Mochizuki-side only |
| `iut:procession` | Ind1-reduction essential for multiradial bound | 1 occurrence, summary-only, not analyzed | Mochizuki-essential / SS-scope-outside |
| `iut:F_modulus_prime_strip` (prev. registered) | ×μ-Kummer structure carries log-link cyclotomic rigidity | SS's sole deep focus (§2.1.5–2.1.9); canonical-triviality claim | **DISPUTED** |
