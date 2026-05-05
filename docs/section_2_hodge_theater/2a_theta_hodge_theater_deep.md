# Section 2a: Theta-Hodge Theater — Deep Dive (Mochizuki-side draft)

> v0.2 schema — mochizuki-side draft — 2026-05-06  
> Source: IUTchI §3 (PRIMS 57, 2021); IUTchII §4 (PRIMS 57, 2021)  
> PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf  
> PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf

---

## 2a.1 `iut:theta_hodge_theater` — Θ-Hodge theater

**Definition source**: IUTchI Def 3.6, p. 87  
**IRI**: `iut:theta_hodge_theater`  
**Notation**: `†HT^Θ`

**Verbatim definition (IUTchI Def 3.6, p. 87)**:
> "a Θ-Hodge theater [relative to the given initial Θ-data] to be a collection of data
> `†HT^Θ = ({†F_v}_{v∈V}, †F^⊩_mod)`
> that satisfies the following conditions:
> (a) If v ∈ V^non, then †F_v is a category which admits an equivalence of categories
> †F_v ~→ F_v [where F_v is as in Examples 3.2, (i); 3.3, (i)].
> (b) If v ∈ V^arc, then †F_v is a collection of data (†C_v, †D_v, †κ_v) …
> (c) †F^⊩_mod is a collection of data (†C^⊩_mod, Prime(†C^⊩_mod) ~→ V, {†F^⊢_v}_{v∈V}, {†ρ_v}_{v∈V})"

**Role in IUTchI**: The Θ-Hodge theater is the basic unit of the Frobenius-picture
(Cor 3.8). A Z-indexed chain `{^n HT^Θ}_{n∈Z}` connected by Θ-links (Cor 3.7)
forms the oriented graph `⃗Γ` that is the starting point of the IUT construction.
The theater encodes, at each place v ∈ V, a Frobenioid-theoretic copy of
the arithmetic geometry surrounding the theta function.

**Depends on**: `iut:HodgeTheater` (enhanced version),
`iut:F_prime_strip`, `iut:Frobenioid`, initial Θ-data (IUTchI Def 3.1).

**Note**: The full Θ^±ellNF-Hodge theater (IUTchI Def 6.13) is the enhanced version
used in IUTchII–III; the Θ-Hodge theater of §3 is its simpler precursor.

---

## 2a.2 `iut:F_circ_theta_strip` — F^⊩_tht strip (Theta-side global Frobenioid)

**Definition source**: IUTchI Example 3.5 (ii), p. 85  
**IRI**: `iut:F_circ_theta_strip`  
**Notation**: `F^⊩_tht`  
**Alt labels**: theta-strip, F-⊩-tht-prime-strip

**Verbatim definition (IUTchI Example 3.5 ii, p. 85)**:
> "F^⊩_tht =^def (C^⊩_tht, Prime(C^⊩_tht) ~→ V, {F^Θ_v}_{v∈V}, {ρ^Θ_v}_{v∈V})"
>
> where `ρ^Θ_v : Φ_{C^⊩_tht,v} ~→ Φ^rlf_{C^Θ_v}` is the isomorphism of topological monoids
> determined by the restriction functor `C^{ρΘ}_v : C^⊩_tht → (C^Θ_v)^rlf`.
> At v ∈ V^bad: `ρ^Θ_v` is given by
> `log^⊢_mod(p_v)·log(Θ) ↦ logΦ(p_v)/[K_v:(F_mod)_v] · logΦ(Θ_v)/logΦ(q_v)`

**Structural twin**: There is a natural isomorphism `F^⊩_mod ~→ F^⊩_tht` (IUTchI Ex 3.5 ii).
The two strips differ only in which Frobenioid sits at each v: `F^⊢_v` (mod-side)
vs `F^Θ_v` (theta-side).

**Role in IUTchI/II**:
- Source domain of the Θ-link: `†F^⊩_tht ~→ ‡F^⊩_mod` (Cor 3.7 i).
- The lack of a "distinguished" isomorphism (Rmk 3.7.1) is essential — no canonical
  identification exists between `†F^⊩_tht` and `‡F^⊩_mod`; only a full poly-isomorphism.
- In IUTchII, upgraded to `F^⊩▶×μ`-prime-strip (Def 4.9 viii) for the Θ^×μ-link.

---

## 2a.3 `iut:F_circ_q_strip` — F^⊩_q strip (q-parameter / mod-side global Frobenioid)

**Definition source**: IUTchI Example 3.5 (i), p. 84; also used as target of Θ-link  
**IRI**: `iut:F_circ_q_strip`  
**Notation**: `F^⊩_mod`  
**Alt labels**: mod-strip, F-⊩-mod-prime-strip, q-strip

**Verbatim definition (IUTchI Example 3.5 i, p. 84)**:
> "F^⊩_mod =^def (C^⊩_mod, Prime(C^⊩_mod) ~→ V, {F^⊢_v}_{v∈V}, {ρ_v}_{v∈V})"
>
> where `ρ_v : Φ_{C^⊩_mod,v} ~→ Φ^rlf_{C^⊢_v}` is given by
> `log^⊢_mod(p_v) ↦ 1/[K_v:(F_mod)_v] · logΦ(p_v)`.

**Relationship to q-parameter**: At v ∈ V^bad, the divisor monoid of `C^⊩_mod` tracks
the q-parameter `q_v` (Tate parameter of the elliptic curve at v). The Θ-link
sends theta values {Θ_v}_{v∈V^bad} to the q-parameters {q_v}_{v∈V^bad} via
`ρ^Θ_v / ρ_v`, effecting the central "Teichmuller deformation" (IUTchII Rmk 4.10.3 ii).

**Role in proof**: The target side `‡F^⊩_mod` of the Θ-link carries the
q-pilot object (see §2a.4). Comparison of volumes on mod-side vs theta-side
yields the Diophantine inequality.

---

## 2a.4 `iut:theta_pilot_object` — Theta-pilot / q-pilot object

**Definition source**: IUTchII Def 4.9 (viii), p. 158  
**IRI**: `iut:theta_pilot_object`  
**Notation**: pilot object of `∗F^⊩▶×μ`

**Verbatim definition (IUTchII Def 4.9 viii, p. 158)**:
> "the generators of the monoids 'O^▶(−)' [each of which is abstractly isomorphic to N]
> of the data at v ∈ V^bad of ∗F^⊢▶×μ = {∗F^⊢▶×μ_w}_{w∈V}, together with the {∗ρ_w}_{w∈V},
> determine a well-defined object, up to isomorphism, of the global realified Frobenioid
> ∗C^⊩ of negative 'arithmetic degree' … which we refer to as the **pilot object**
> associated to the F^⊩▶×μ-prime-strip ∗F^⊩▶×μ."

**Two flavors**:
- **Θ-pilot** (theta-pilot): pilot object of `†F^⊩▶×μ_env` (theta-side);
  encodes the theta values `{Θ_v}_{v∈V^bad}` as an arithmetic degree in `C^⊩`.
- **q-pilot**: pilot object of `‡F^⊩▶×μ_△` (mod/q-side);
  encodes the q-parameters `{q_v}_{v∈V^bad}` as an arithmetic degree in `C^⊩`.

**Role in proof**: The Θ^×μ_gau-link sends the Θ-pilot to the q-pilot (full poly-isomorphism).
IUTchIII Cor 3.12 derives the Diophantine inequality by bounding the log-volumes of
these pilot objects after applying the three indeterminacies (Ind1, Ind2, Ind3).
The pilot objects are the "test objects" on which the entire volume comparison rests.

---

## 2a.5 [DISPUTED] Role at Cor 3.12 — connection to sub_1

The pilot objects are essential to IUTchIII Cor 3.12.

### Mochizuki position
The theta-pilot and q-pilot exist in separate, "alien" arithmetic holomorphic
structures (Frobenius-picture). The Θ^×μ_gau-link identifies them only up to
the indeterminacies Ind1/Ind2/Ind3. The multiradial algorithm (IUTchIII Thm 3.11)
allows a simultaneous description of the theta-pilot across copies, yielding
the log-volume inequality. See `claim:mochizuki_2012_proves_abc`.

### Scholze-Stix position (sub_1)
The "alien copies" argument — that `†F^⊩_tht` and `‡F^⊩_mod` are genuinely
distinct as ring-theoretic objects — is questioned in `claim:scholze_stix_2018_sub_1`.
The objection is that if one identifies the two copies via a ring isomorphism,
the theta/q-pilot comparison collapses to a tautology with no arithmetic content.
Source: Scholze-Stix report §3, https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf

### Status
Unresolved as of `verified_at: 2026-05-06`. See `claim:scholze_stix_2018_sub_1`,
`claim:mochizuki_2018_response`, `claim:lana_formalization_in_progress`.

---

## Sources

| Reference | URL |
|---|---|
| IUTchI (PRIMS 2021) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf |
| IUTchII (PRIMS 2021) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf |
| Scholze-Stix report (2018) | https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
