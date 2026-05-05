# Section 3a: Theta-link IUTchI Deep (Mochizuki-side draft)

> schema: v0.2 | source: IUTchI Cor. 3.7–3.8 (pp. 88–90), Rem. 3.9.4 (p. 94);
> Alien Copies §3.3 (ii)(vi)(vii) (pp. 59–73) | verified_at: 2026-05-06
> 4 entities; specialization note: `iut:theta_link` (existing) = concept-level;
> these 4 entities = construction/consequence layer; no duplication.

---

## `iut:theta_link_full_poly_iso` — Construction

**label**: full poly-isomorphism constituting the Theta-link (IUTchI Cor. 3.7-i)
**definedIn**: paper:IUTchI | **introduced_year**: 2012
**depends_on**: `iut:theta_link`, `iut:F_modulus_prime_strip`, `iut:theta_pilot_object`
**lean_module**: IutStatus.ThetaLinkFullPolyIso

IUTchI Cor. 3.7 (i) p. 88 (verbatim):
> "The full poly-isomorphism [cf. §0] between collections of data
> `†F⊩_tht ~→ ‡F⊩_mod` is nonempty. We shall refer to this full poly-isomorphism
> as the Θ-link `†HT^Θ —Θ→ ‡HT^Θ`."

Remark 3.7.1: many distinct isomorphisms exist; **none is distinguished**.
Domain = `†F⊩_tht` (reciprocal of l-th root of Frobenioid-theoretic Θ_v, v ∈ V^bad).
Codomain = `‡F⊩_mod` (2l-th roots of q-parameters). No ring structure crosses.

```lean
axiom theta_link_full_poly_iso (HT1 HT2 : HodgeTheater) :
    Set (F_vdash_prime_strip HT1 ≅ F_vdash_prime_strip HT2)
```

---

## `iut:theta_link_preserved_data` — Theorem

**label**: preserved data across the Theta-link: D⊢ and O× (IUTchI Cor. 3.7 ii–iii)
**definedIn**: paper:IUTchI | **introduced_year**: 2012
**depends_on**: `iut:theta_link_full_poly_iso`, `iut:D_prime_strip`
**lean_module**: IutStatus.ThetaLinkPreservedData

Cor. 3.7 (ii) p. 88: composite full poly-iso `†D⊢_v ~→ †D^Θ_v ~→ ‡D⊢_v`.
Cor. 3.7 (iii) p. 89: composite full poly-iso `O×_{†C⊢_v} ~→ O×_{†C^Θ_v} ~→ O×_{‡C⊢_v}`.
Alien Copies §3.3 (vii) p. 73: "Θ-link induces an isomorphism of the unit group
portion data … and a dilation … of the value group data."
Rem. 3.9.3 (ii): O× = dimension held fixed; value groups = dimension dilated.
Dispute note: SS does not contest existence of these isos; dispute is over whether
abstract-monoid identification makes the comparison trivial (see `iut:theta_link`).

```lean
axiom theta_link_preserves_D_vdash (v : Place) (HT1 HT2 : HodgeTheater) :
    D_vdash v HT1 ≅ D_vdash v HT2
axiom theta_link_preserves_O_times (v : Place) (HT1 HT2 : HodgeTheater) :
    O_times v HT1 ≅ O_times v HT2
```

---

## `iut:Frobenius_picture` — Construction

**label**: Frobenius-picture (infinite chain of Theta-linked Hodge theaters, IUTchI Cor. 3.8)
**alt_labels**: ["oriented graph Γ", "log-theta-lattice horizontal slice"]
**definedIn**: paper:IUTchI | **introduced_year**: 2012
**depends_on**: `iut:theta_link_full_poly_iso`, `iut:HodgeTheater`
**lean_module**: IutStatus.FrobeniusPicture

IUTchI Cor. 3.8 p. 89: infinite chain `… —Θ→ nHT^Θ —Θ→ (n+1)HT^Θ —Θ→ …`,
oriented graph Γ with **Z-translation symmetry** but **no adjacent-swap automorphism**.
Core arrow (Rem. 3.8.1 i): `nΘ_v → (n+1)q_v` for v ∈ V^bad.
Alien Copies §3.3 (ii) pp. 60–62: two lattice dimensions = addition (log-link) +
multiplication (Θ-link). Lattice is **highly noncommutative**: Θ-link requires
deactivating the log-link's add/multiply rotation, hence Θ∘log ≠ log∘Θ.

```lean
axiom Frobenius_picture : ℤ → HodgeTheater
axiom Frobenius_picture_link (n : ℤ) :
    theta_link_full_poly_iso (Frobenius_picture n) (Frobenius_picture (n + 1))
axiom Frobenius_picture_no_adjacent_swap :
    ¬∃ σ : ℤ ≃ ℤ, σ 0 = 1 ∧ σ 1 = 0 ∧ ∀ n, n ≠ 0 → n ≠ 1 → σ n = n
```

---

## `iut:alien_arithmetic_holomorphic_structure` — Concept

**label**: alien arithmetic holomorphic structure (Alien Copies §3.3 ii, vi, vii)
**alt_labels**: ["mutually alien copies", "inter-universal wall", "互いに異質なスキーム理論のコピー"]
**definedIn**: paper:AlienCopies | **introduced_year**: 2019
**depends_on**: `iut:Frobenius_picture`, `iut:theta_link`
**lean_module**: IutStatus.AlienArithHolStructure

Alien Copies §3.3 (vi) p. 68: each abstract Π_X determines an "arithmetic holomorphic
structure" on the quotient Π_X ↠ G_k. Distinct HT^Θ carry *distinct* such structures.
IUTchI Rem. 3.9.4 p. 94: "(n+1)q_v belongs to a distinct scheme theory … from
the base nq_v … The distinctness may be seen in the indeterminacy of the isomorphism
between the associated isomorphs of D⊢_v, which obliterates the ring structure —
the 'arithmetic holomorphic structure' — associated to nD_v for distinct n."
Alien Copies §3.3 (vii) p. 73: Θ-link is "fundamentally incompatible with the ring
structures in its domain and codomain"; G_k is only well-defined up to indeterminate iso.
**Mochizuki vs. SS**: The canonical identification SS applies is exactly the step that
discards this inter-universal separation and makes the theory trivial, per Mochizuki.

```lean
axiom alien_arith_hol_structure (n m : ℤ) (h : n ≠ m) :
    ¬ RingEquiv (arith_hol_structure (Frobenius_picture n))
               (arith_hol_structure (Frobenius_picture m))
```

---

## Verification log

| claim | source | status |
|-------|--------|--------|
| full poly-iso is nonempty, no element distinguished | IUTchI Cor. 3.7-i p. 88; Rem. 3.7.1 p. 89 | ✅ verbatim |
| D⊢ full poly-iso via Cor. 3.7-ii | IUTchI p. 88 | ✅ verbatim |
| O× full poly-iso via Cor. 3.7-iii | IUTchI p. 89 | ✅ verbatim |
| value-group dilation (j² average) | Alien Copies §3.3(vii) p. 73 | ✅ verbatim |
| Frobenius-picture: Z-symmetry, no adjacent-swap | IUTchI Cor. 3.8 p. 89 | ✅ verbatim |
| core arrow nΘ_v → (n+1)q_v | IUTchI Rem. 3.8.1(i) p. 90 | ✅ verbatim |
| log-theta-lattice noncommutativity | Alien Copies §3.3(ii) pp. 60–62 | ✅ |
| arithmetic holomorphic structure definition | Alien Copies §3.3(vi) p. 68 | ✅ verbatim |
| "distinct scheme theory" obliterates ring structure | IUTchI Rem. 3.9.4 p. 94 | ✅ verbatim |
| 4-entity cap satisfied; no duplicate with `iut:theta_link` | entities.json cross-check | ✅ |
