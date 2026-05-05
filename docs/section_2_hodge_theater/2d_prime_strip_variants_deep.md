# Section 2d: Prime-Strip Variants (Deep) — Mochizuki-Side Draft

**Status**: draft (mochizuki-side only; SS-side not yet drafted)
**Sources**: IUTchI Def 4.1, Def 5.2; IUTchII Def 4.9; IUTchIII §1 (Def 1.4), §3 (Def 3.8)
**Entities covered**: `iut:D_prime_strip`, `iut:F_top_prime_strip`, `iut:F_LGP_prime_strip`, `iut:procession`

---

## 1. D-prime-strip (`iut:D_prime_strip`)

**Source**: IUTchI Def 4.1 (i), PDF p.95–96  
**Full name**: *holomorphic base-prime-strip* or *D-prime-strip*

A D-prime-strip is a collection of data
```
†D = { †D_v }_{v ∈ V}
```
satisfying:
- (a) if v ∈ V^{non}: †D_v is a category equivalent to D_v [cf. Ex. 3.2, 3.3];
- (b) if v ∈ V^{arc}: †D_v is an Aut-holomorphic orbispace isomorphic to D_v [cf. Ex. 3.4 (i)].

**D⊢-prime-strip** (mono-analytic base-prime-strip, Def 4.1 iii): The *mono-analyticization* of
a D-prime-strip; replaces holomorphic categories by their "mono-analytic" subcategories
(B(G_v)^0 type at non-archimedean places; TM⊢ object at archimedean).  
Natural functor: D-prime-strip → D⊢-prime-strip (Def 4.1 iv).

**Key property**: LabCusp(†D) carries a canonical F^⋇_l-torsor structure and canonical
element (Prop 4.2). This is the *base-category* component that underlies all Frobenioid-level
constructions.

**Relation to other entities**:
- `iut:F_prime_strip` (IUTchI Def 5.2 i) lifts †D by adding Frobenioid data at each v.
- `iut:F_top_prime_strip` (Def 5.2 ii) is the mono-analytic Frobenioid analogue.
- `iut:procession` (Prop 6.9) is a diagram of capsules of D-prime-strips.

---

## 2. F⊢-prime-strip / F-top-prime-strip (`iut:F_top_prime_strip`)

**Source**: IUTchI Def 5.2 (ii), PDF p.134  
**Full name**: *mono-analytic Frobenioid-prime-strip* or *F⊢-prime-strip*

A collection of data
```
‡F⊢ = { ‡F⊢_v }_{v ∈ V}
```
satisfying:
- (a) if v ∈ V^{non}: ‡F⊢_v is a **split Frobenioid** (underlying Frobenioid ‡C⊢_v) isomorphic to F⊢_v [Ex. 3.2 (v); 3.3 (i)];
- (b) if v ∈ V^{arc}: ‡F⊢_v is a triple (Frobenioid ‡C⊢_v, TM⊢ object, splitting) isomorphic to F⊢_v [Ex. 3.4 (ii)].

**Distinction from F-prime-strip** (Def 5.2 i):
- F-prime-strip: holomorphic, per-place Frobenioid ‡C_v equivalent to C_v.
- F⊢-prime-strip: **mono-analytic** (forgets holomorphic structure), split Frobenioid only.

**F⊩-prime-strip** (Def 5.2 iv, "globally realified mono-analytic"):
```
‡F⊩ = (‡C⊩, Prime(‡C⊩) →∼ V, ‡F⊢, {‡ρ_v}_{v∈V})
```
Adds a global realified Frobenioid ‡C⊩ (isomorphic to C⊩_mod) with local-global comparison
isomorphisms ‡ρ_v : Φ_{‡C⊩,v} →∼ Φ^{rlf}_{‡C⊢_v}.

**Note**: `iut:F_modulus_prime_strip` (F^⊩×μ in IUTchII) is a further refinement;
`iut:F_top_prime_strip` (F⊢) underlies it.

---

## 3. F⊩LGP / F⊩lgp prime-strip (`iut:F_LGP_prime_strip`)

**Source**: IUTchII Def 4.9 (vii–viii); IUTchIII Def 3.8 (ii), PDF pp.113–114  
**Full name**: *F⊩▶×μ-prime-strip* (general form defined in IUTchII Def 4.9 viii);
specialized variants F⊩_LGP, F⊩_lgp appear in IUTchIII.

**IUTchII Def 4.9 context** — introduces:
- F⊢×, F⊢×μ, F⊢▶×μ-prime-strips (Def 4.9 vii): For □ ∈ {×, ×μ, ▶×μ},
  an F⊢□-prime-strip is `{*F⊢□_v}_{v∈V}` where each local component is
  the corresponding Kummer-Frobenioid variant constructed in (iii)–(vi).
- F⊩▶×μ-prime-strip (Def 4.9 viii):
  ```
  *F⊩▶×μ = (*C⊩, Prime(*C⊩) →∼ V, *F⊢▶×μ, {*ρ_v}_{v∈V})
  ```
  same shape as F⊩ (Def 5.2 iv) with F⊢ replaced by F⊢▶×μ.
  The *pilot object* associated to this strip is defined here (IUTchII Def 4.9 viii).

**IUTchIII Def 3.8 (ii)** — defines Θ×μ_LGP- and Θ×μ_lgp-links:
- †F⊩▶×μ_LGP (resp. †F⊩▶×μ_lgp): F⊩▶×μ-prime-strip associated to †F⊩_LGP
  (resp. †F⊩_lgp), constructed via Prop 3.7 (iii),(iv) from LGP-/lgp-Gaussian monoids.
- **Θ×μ_LGP-link**: full poly-isomorphism of F⊩▶×μ-prime-strips
  `†F⊩▶×μ_LGP →∼ *F⊩▶×μ_△`.
- **Θ×μ_lgp-link**: full poly-isomorphism `†F⊩▶×μ_lgp →∼ *F⊩▶×μ_△`.

**LGP** = "Logarithmic Gaussian Procession" (splitting monoids of Gaussian monoids
rendered multiradial via procession indexing; cf. IUTchIII Theorem A title, p.19).

**Specialization relation** (informal):
```
iut:F_prime_strip
  ← specializes → iut:F_top_prime_strip (F⊢, mono-analytic)
                        ← iut:F_modulus_prime_strip (F⊩×μ, IUTchII)
                              ← F⊩▶×μ (IUTchII Def 4.9)
                                    ← iut:F_LGP_prime_strip (F⊩▶×μ_LGP/lgp, IUTchIII)
```
Each step adds structure (global realification → ×μ-Kummer → ▶×μ splitting → LGP evaluation).

---

## 4. Procession of prime-strips (`iut:procession`)

**Source**: IUTchI Prop 6.9, PDF pp.169–170; IUTchIII §3 (Ind1, Theorem A)  
**Full name**: *l±-procession of D-prime-strips* (holomorphic); *l±-procession of D⊢-prime-strips* (mono-analytic)

A procession is a diagram of capsule inclusions
```
S±_1 → S±_2 → ... → S±_{l±}
```
where S±_{j+1} = {0,1,...,j} and each S±_{j+1} indexes a capsule of D-prime-strips (resp. D⊢-prime-strips).

**Construction** (Prop 6.9 i): Given a D-Θ±-bridge †φ^{Θ±}_± : †D_T → †D_≻, the procession
`Prc(†D_T)` is the diagram of sub-capsules corresponding to S±_1 ⊆ ... ⊆ S±_{l±} = |F_l|,
via the bijection |T| →∼ |F_l| from the F±_l-group structure of T.

**Key property** (Prop 6.9 i): This reduces label-indeterminacy from (l±)^{l±} possibilities
to l±! possibilities — critical for log-volume estimates in IUTchIV.

**Role in IUTchIII**: The multiradial algorithm of Theorem A (Cor 3.12) is constructed
as a functor in `Prc(^{n,◦}D⊢_T)` (procession of D⊢-prime-strips), invariant up to
indeterminacy (Ind1) = permutation automorphisms of procession. The "procession-normalized
mono-analytic log-volume" averages over j ∈ F⋇_l indexed by the procession.

**Relation to W2 monitor**: procession is NOT a specialization of F_prime_strip or
D_prime_strip; it is a *diagram of capsules* of such strips. No overlap with
iut:F_prime_strip / iut:F_modulus_prime_strip registration.

---

## Watch notes for W2 monitor

- `iut:F_top_prime_strip` (F⊢) is the mono-analytic Frobenioid analogue of `iut:F_prime_strip`.
  The latter (holomorphic) is already registered in entities.json; this draft covers the
  mono-analytic variant. Registered `iut:F_modulus_prime_strip` (F^⊩×μ) is a further
  elaboration; `iut:F_top_prime_strip` (F⊢) is a *sub-component* of it.
- `iut:F_LGP_prime_strip` covers both F⊩_LGP and F⊩_lgp variants (they share the same
  structural template; only the monoids differ: LGP uses MOD-type, lgp uses mod-type).
  The distinction is noted in informal_md. LGP is the primary variant used in Cor 3.12.
- `iut:procession` depends on `iut:D_prime_strip` but is categorically distinct
  (it is a functor-output diagram, not a prime-strip itself).
