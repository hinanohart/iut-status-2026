# Section 3a — Theta-link / IUTchI Cor. 3.7–3.8: Merged View

> schema: v0.2 | merged_at: 2026-05-06
> sources: IUTchI Cor. 3.7–3.8 (pp. 88–90), Rem. 3.9.4 (p. 94);
>   Alien Copies §3.3 (ii)(vi)(vii) (pp. 59–73);
>   SS 2018 §2.1.9 p.9 (verbatim)
> entities: 4 (iut:theta_link_full_poly_iso, iut:theta_link_preserved_data,
>   iut:Frobenius_picture, iut:alien_arithmetic_holomorphic_structure)
> claims recorded: claim:mochizuki_alien_copies_essential (new, this file)
>   claim:ss_canonically_same_strips (pre-existing, cross-ref only)

---

## 5-block answer template

### Mochizuki
IUTchI Cor. 3.7 (i) p.88: the Theta-link `†HT^Θ —Θ→ ‡HT^Θ` is a **full
poly-isomorphism** `†F⊩_tht ~→ ‡F⊩_mod`.  Rem. 3.7.1: the isomorphism set
is nonempty and **no element is distinguished** — the poly-iso is the entire set,
not a canonical choice.  Cor. 3.7 (ii)–(iii): D⊢ and O× data are preserved via
composite full poly-isos; value groups are **dilated** (j² average), not preserved.
Cor. 3.8: iterating yields the **Frobenius-picture** (Z-indexed chain of Hodge
theaters) with Z-translation symmetry and **no adjacent-swap automorphism**.
Rem. 3.9.4 p.94: each `nHT^Θ` carries a distinct "arithmetic holomorphic
structure"; the Theta-link **obliterates** ring structure across the inter-universal
wall, making the alien copies non-identifiable.

### Scholze-Stix
SS 2018 §2.1.9 p.9 (verbatim):
> "The F⊩×µ-prime strips are given by data of the form **G_v ⟲ o^{×µ}_{k̄_v} × N**
> on both sides (at finite places), and **this data is canonically the same on both
> sides**. It is simply the name of the generator of the monoid N that appears that
> is called Θ respectively q."

Under this reading, the full poly-isomorphism is **trivially resolved** by the
canonical identity; no arithmetic content (j² dilation) survives the identification.
SS footnote 12 p.9: Theorem 3.11 "does not become false, but trivial."
SS does not engage Alien Copies §3.3 (vi)–(vii) or the Frobenius-picture structure
in the 10-page report (0 occurrences of "alien", "Frobenius-picture", "Rem 3.9.4").

### Alternative / Third-party
Joshi (arXiv:2505.10568v2): Arithmetic Teichmüller Spaces reframe the
separation of arithmetic holomorphic structures; claims the gap identified by SS
can be repaired within ATS. Neither accepts SS canonical identification nor
reproduces original IUT as-is. Status: preprint, not peer-reviewed as of 2026-05.

### Pending
- LANA formalization project (mid-report 2026-07-17): formalizing anabelian geometry
  and IUT in Lean 4. Specific contentious point articulated but not resolved
  (Mochizuki 2026-04 PDF).
- Whether Rem. 3.9.4 "obliterates ring structure" constitutes a proof of
  non-canonicality (vs. SS "canonically the same") is the central unresolved point.

### Unresolved
The dispute over `claim:ss_canonically_same_strips` vs.
`claim:mochizuki_alien_copies_essential` is **not resolved as of 2026-05**.
Both sides agree on: (a) full poly-iso is nonempty; (b) D⊢ and O× isos exist;
(c) value groups are dilated by j².  Disagreement is over whether the two sides
of the Theta-link inhabit structurally distinct "scheme theories" (Mochizuki) or
whether a canonical identification collapses that distinction (SS).

---

## Entity summary

| IRI | type | source |
|-----|------|--------|
| `iut:theta_link_full_poly_iso` | Construction | IUTchI Cor. 3.7-i |
| `iut:theta_link_preserved_data` | Theorem | IUTchI Cor. 3.7 ii–iii |
| `iut:Frobenius_picture` | Construction | IUTchI Cor. 3.8 + §I4 |
| `iut:alien_arithmetic_holomorphic_structure` | Concept | Alien Copies §3.3 |

depends_on chains (flat IRI):
- `iut:theta_link_full_poly_iso` → `iut:theta_link`, `iut:F_circ_theta_strip`, `iut:F_circ_q_strip`
- `iut:theta_link_preserved_data` → `iut:theta_link_full_poly_iso`, `iut:D_prime_strip`
- `iut:Frobenius_picture` → `iut:theta_hodge_theater`, `iut:theta_link`
- `iut:alien_arithmetic_holomorphic_structure` → `iut:theta_link`

---

## Claim summary

| claim IRI | position | status |
|-----------|----------|--------|
| `claim:mochizuki_alien_copies_essential` (new) | valid / supportive | unresolved-as-of-2026-05 |
| `claim:ss_canonically_same_strips` (pre-existing) | alleged_gap / critical | unresolved-as-of-2026-05 |

`claim:mochizuki_alien_copies_essential` is recorded as the structural counter
to `claim:ss_canonically_same_strips`: the alien copies framework (Rem. 3.9.4 +
Alien Copies §3.3 vii) asserts the ring structure is obliterated across the
inter-universal wall, making SS canonical identification illegitimate at that step.

---

## Verification log

| item | source | status |
|------|--------|--------|
| full poly-iso nonempty, no distinguished element | IUTchI Cor. 3.7-i + Rem. 3.7.1 p.88–89 | ✅ verbatim |
| D⊢ / O× preservation | IUTchI Cor. 3.7 ii–iii p.88–89 | ✅ verbatim |
| value-group dilation j² | Alien Copies §3.3(vii) p.73 | ✅ verbatim |
| Frobenius-picture Z-symmetry, no adjacent-swap | IUTchI Cor. 3.8 p.89 | ✅ verbatim |
| core arrow nΘ_v → (n+1)q_v | IUTchI Rem. 3.8.1(i) p.90 | ✅ verbatim |
| arithmetic hol. structure / obliterates ring | IUTchI Rem. 3.9.4 p.94 | ✅ verbatim |
| SS "canonically the same on both sides" | SS 2018 §2.1.9 p.9 | ✅ verbatim |
| SS footnote 12 "trivial" | SS 2018 p.9 fn.12 | ✅ verbatim |
| SS: 0 occurrences alien/Frobenius-picture | SS 2018 full-text pymupdf | ✅ verified |
| 4-entity cap; no duplicate with `iut:theta_link` | entities_3a_merged.json | ✅ |
