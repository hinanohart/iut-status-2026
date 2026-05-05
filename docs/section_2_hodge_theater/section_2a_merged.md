# Section 2a: Theta-Hodge Theater — Merged (v0.2)

> Merged from mochizuki-side draft + SS-side draft  
> Schema: v0.2 — 2026-05-06  
> Sources:  
> - IUTchI (PRIMS 2021): https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf  
> - IUTchII (PRIMS 2021): https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf  
> - Scholze-Stix 2018: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf

---

## 2a.1 `iut:theta_hodge_theater` — Θ-Hodge theater

**Definition source**: IUTchI Def 3.6, p. 87  
**Notation**: `†HT^Θ`

> **[W1]** Distinct from generic `iut:HodgeTheater`: this is the Θ-component projection of
> Θ±ellNF-HT. The full Θ±ellNF-Hodge theater (IUTchI Def 6.13) is the enhanced version used
> in IUTchII–III; the Θ-Hodge theater of §3 is its simpler precursor encoding only the
> Frobenioid-theoretic theta data at each v ∈ V.

**Verbatim definition (IUTchI Def 3.6, p. 87)**:
> "a Θ-Hodge theater [relative to the given initial Θ-data] to be a collection of data
> `†HT^Θ = ({†F_v}_{v∈V}, †F^⊩_mod)`
> (a) If v ∈ V^non, then †F_v is a category which admits an equivalence of categories
> †F_v ~→ F_v.
> (b) If v ∈ V^arc, then †F_v is a collection of data (†C_v, †D_v, †κ_v) …
> (c) †F^⊩_mod is a collection of data (†C^⊩_mod, Prime(†C^⊩_mod) ~→ V, {†F^⊢_v}_{v∈V}, {†ρ_v}_{v∈V})"

**Mochizuki position**: A Z-indexed chain `{^n HT^Θ}_{n∈Z}` connected by Θ-links (Cor 3.7)
forms the oriented graph `⃗Γ` underlying the Frobenius-picture (Cor 3.8). Each copy is
an "alien" arithmetic holomorphic structure; distinctness is essential (IUTchI §I1).

**SS position (sub_1, p.6)**: Mochizuki's own theorems [IUTT-1, Cor 6.12(i) etc.] yield
a constructive equivalence of categories `{X} ≃ {Θ±ellNF-HT}`. The necessity of
"distinct" copies is therefore not established at the formal level. `[DISPUTED]`

**Status**: Unresolved as of 2026-05-06. See `claim:scholze_stix_2018_sub_1`.

---

## 2a.2 `iut:F_circ_theta_strip` — F^⊩_tht-strip (theta-side)

**Definition source**: IUTchI Example 3.5 (ii), p. 85

> **[W2]** Specialization of `iut:F_prime_strip` with Θ-pilot constraint: the local
> Frobenioid at each v ∈ V^bad is `F^Θ_v` (theta-Frobenioid) rather than `F^⊢_v`
> (mod-Frobenioid); at v ∈ V^bad the divisor monoid tracks `Θ_v`-values, not `q_v`.

**Verbatim definition (IUTchI Ex 3.5 ii, p. 85)**:
> "F^⊩_tht =^def (C^⊩_tht, Prime(C^⊩_tht) ~→ V, {F^Θ_v}_{v∈V}, {ρ^Θ_v}_{v∈V})"
> where `ρ^Θ_v : Φ_{C^⊩_tht,v} ~→ Φ^rlf_{C^Θ_v}` is given at v ∈ V^bad by
> `log^⊢_mod(p_v)·log(Θ) ↦ logΦ(p_v)/[K_v:(F_mod)_v] · logΦ(Θ_v)/logΦ(q_v)`

**Mochizuki position**: Source domain of the Θ-link `†F^⊩_tht ~→ ‡F^⊩_mod` (Cor 3.7 i).
Only a full poly-isomorphism exists; no canonical ring-theoretic identification (Rmk 3.7.1).

**SS position (sub_4, p.9 verbatim)**:
> "The F⊩×µ-prime strips are given by data of the form `Gv ↷ o×µ_{k̄v} × N` on both sides
> (at finite places), and this data is canonically the same on both sides. It is simply the
> name of the generator of the monoid N that appears that is called Θ respectively q."

→ See `claim:ss_canonically_same_strips`. `[DISPUTED]`

---

## 2a.3 `iut:F_circ_q_strip` — F^⊩_mod-strip (q-side)

**Definition source**: IUTchI Example 3.5 (i), p. 84

> **[W2]** Specialization of `iut:F_prime_strip` with q-pilot constraint: the local
> Frobenioid at each v ∈ V^bad is `F^⊢_v` (mod-Frobenioid); the divisor monoid tracks
> `q_v`-parameters (Tate parameters of the elliptic curve at v).

**Verbatim definition (IUTchI Ex 3.5 i, p. 84)**:
> "F^⊩_mod =^def (C^⊩_mod, Prime(C^⊩_mod) ~→ V, {F^⊢_v}_{v∈V}, {ρ_v}_{v∈V})"
> where `ρ_v : Φ_{C^⊩_mod,v} ~→ Φ^rlf_{C^⊢_v}` is given by
> `log^⊢_mod(p_v) ↦ 1/[K_v:(F_mod)_v] · logΦ(p_v)`

**Mochizuki position**: Target side of the Θ-link; carries the q-pilot object.
Volume comparison (mod-side vs theta-side) yields the Diophantine inequality (IUTchIII Cor 3.12).

**SS position**: Abstractly isomorphic to `iut:F_circ_theta_strip` (same `Gv ↷ o×µ × N`
structure); the "canonical" identification makes the theta-vs-q comparison a tautology
(SS p.9, fn.12). `[DISPUTED]`

---

## 2a.4 `iut:theta_pilot_object` — Theta-pilot / q-pilot

**Definition source**: IUTchII Def 4.9 (viii), p. 158

**Verbatim definition (IUTchII Def 4.9 viii, p. 158)**:
> "the generators of the monoids 'O^▶(−)' [each of which is abstractly isomorphic to N]
> of the data at v ∈ V^bad of ∗F^⊢▶×μ … determine a well-defined object, up to isomorphism,
> of the global realified Frobenioid ∗C^⊩ of negative 'arithmetic degree' … which we refer
> to as the **pilot object** associated to the F^⊩▶×μ-prime-strip ∗F^⊩▶×μ."

**Two flavors**:
- **Θ-pilot**: pilot of `†F^⊩▶×μ_env`; arithmetic degree encodes `{Θ_v^{j²}}_{j=1,…,ℓ*}`.
- **q-pilot**: pilot of `‡F^⊩▶×μ_△`; arithmetic degree encodes `{q_v}_{v∈V^bad}`.

**Mochizuki position**: Θ^×μ_gau-link sends Θ-pilot to q-pilot via full poly-isomorphism.
IUTchIII Cor 3.12 bounds log-volumes after Ind1/Ind2/Ind3, yielding the height inequality.

**SS position (sub_3, p.8–9)**: Abstract pilot element reduces to
`γ_pilot = 1/(2l)·deg(q_E) ∈ R`. The j²-scaling (`R⊙,Θ ≅ R` via j² factor) is critical
(SS p.9: "the necessity of this scaling is critical"); the abstract/concrete distinction
in Mochizuki is alleged to be insufficiently rigorous. `[CLAIMED_BY: SS, DISPUTED]`

---

## 2a.5 Dispute map

| Sub-claim | About | SS source | Status |
|---|---|---|---|
| sub_1: copies not distinct | `theta_hodge_theater` | SS p.6 | unresolved |
| sub_2 (canonical same) | `F_circ_theta_strip`, `F_circ_q_strip` | SS p.9 | unresolved |
| sub_3 (abstract/concrete) | `theta_pilot_object` | SS p.8–9 | unresolved |
| `claim:ss_canonically_same_strips` | `F_circ_theta_strip` | SS p.9 verbatim | new — see claims_2a_merged.json |

All disputes unresolved as of `verified_at: 2026-05-06`.
