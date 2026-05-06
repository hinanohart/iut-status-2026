# Section 4a: log-link deep (IUTchIII §1) — Mochizuki-side draft

> Schema: v0.2  
> Source: IUTchIII §1 (Def 1.1, Prop 1.2, Prop 1.3, Def 1.4) — PDF direct read via pymupdf  
> IUTchIII PDF: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf>  
> IUTchIII PRIMS DOI: <https://doi.org/10.4171/PRIMS/57-1-3>  
> Phase: 4a (section 4 layer 2), mochizuki-side only  
> Entities: 3 (iut:log_link_construction, iut:log_link_compatibility, iut:log_volume)  
> verified_at: 2026-05-06  

---

## 4a.1 `iut:log_link_construction` — log-link as poly-isomorphism

**IUTchIII source**: Def 1.1 (i)(ii)(iii), pp. 23–27; Prop 1.3 (i), p. 42

### Construction (Def 1.1 (iii))

The **tautological log-link** at v ∈ V^non is the diagram

    †F_v  --log-->  log(†F_v)

where `log(†F_v)` is the Frobenioid determined by the pair `{†Π_v ↷ Ψ_log(†F_v)}`,
and `Ψ_log(†F_v) ⊆ Ψ~_†F_v` is the multiplicative monoid of nonzero integers
inside the ind-topological field `Ψ~_†F_v = Ψ^gp_log(†F_v)` defined via the
p_v-adic logarithm on `Ψ~_†F_v = (Ψ^×_†F_v)^pf` (the perfection of the units).

A **log-link from †F_v to ‡F_v** is any diagram obtained by post-composing the
tautological log-link with a [poly-]isomorphism `log(†F_v) ~→ ‡F_v`.  
When that poly-isomorphism is the **full** poly-isomorphism, the result is
called the **full log-link**.

At v ∈ V^arc the construction is analogous using the complex archimedean logarithm
(Def 1.1 (ii), p. 25): the log-shell in this case is the Ψ^×_log(†F_v)-orbit of
the closed segment `{a ∈ k | |a| ≤ π} ⊆ k` (Def 1.1 (ii), Remark 1.2.2 (ii)).

The **log-link between Θ^±ellNF-Hodge theaters** (Prop 1.3 (i), p. 42) is:
given an isomorphism `Ξ : †HT^D-Θ^±ellNF ~→ ‡HT^D-Θ^±ellNF`, the poly-isomorphism
induced by Ξ on associated D-prime-strips uniquely determines
`log(†F^□) ~→ ‡F^□` for each constituent F-prime-strip `†F^□`, hence a
log-link `†F^□ --log--> ‡F^□`.  The **full log-link** `†HT --log--> ‡HT`
is the collection of these constituent log-links when Ξ is the full poly-isomorphism.

### Key structural point

The full log-link is employed in preference to the tautological log-link because
it expresses the relationship between the etale-like `(-)Π_v`'s in domain and
codomain **in purely etale-like terms**, free of any dependence on the
Frobenius-like monoids (Remark 1.1.2, p. 29; Prop 1.3 context, p. 42).

### Relation to existing entity `iut:log_link`

`iut:log_link` (Construction, entities.json) records the top-level existence
of the log-link arrow.  The present entity `iut:log_link_construction`
specialises to the **layer-2 construction detail**: tautological vs. full
poly-iso, the v-by-v structure, and the Hodge-theater-level assembly in Prop 1.3 (i).
No duplication: `iut:log_link` `depends_on` → `iut:log_shell`; the present
entity `depends_on` → `iut:log_link`, `iut:log_shell`.

---

## 4a.2 `iut:log_link_compatibility` — compatibility with HT structure

**IUTchIII source**: Prop 1.2 (i)(ii)(iii)(iv)(v)(viii)(ix)(x), pp. 30–34;
Prop 1.3 (ii)(iii), p. 42

### Prop 1.2 — log-links between F-prime-strips

Let `†F --log--> ‡F`.  Key compatibility properties:

| Sub | Statement | page |
|-----|-----------|------|
| (i) Coricity | `†D ~→ ‡D` and `†D^⊢ ~→ ‡D^⊢` (poly-iso on D-prime-strips) | 31 |
| (ii) Ring struct. | Π_v-actions on `Ψ^gp_†F_v` and `Ψ^gp_log(†F_v)` compatible with ind-topological ring structures (v ∈ V^non); co-holomorphicizations compatible (v ∈ V^arc) | 31 |
| (iii) Log-volumes | diagram (∗non) compatible with p_v-adic log-volumes on Π_v-invariants; diagram (∗arc) compatible with angular (domain) and radial (codomain) log-volumes | 31 |
| (iv) Kummer FAIL | Kummer isos `Ψ_cns(†F) ~→ Ψ_cns(†D)` and `Ψ_cns(‡F) ~→ Ψ_cns(‡D)` are **NOT compatible** with the log-link-induced `Ψ_cns(†D) ~→ Ψ_cns(‡D)` | 31 |
| (v) HoloLogShells | I_{†F_v} compact, of finite log-volume; contains `O^▷`-invariants of `Ψ_log(†F_v)` and image of `Ψ^×`-invariants of `†F_v` | 31–32 |
| (viii) MA log-shells | collections of poly-isos `log(†D^⊢) ~→ log(†F^⊢×µ) ~→ log(†F)` | 33 |
| (ix) Coric HLS | functorial algorithm in D-prime-strip `∗D` constructing coric holomorphic log-shells `I_{∗D} = I_{†F}` ⊆ `Ψ^gp_cns(∗D)` | 34 |
| (x) Frobenius-picture | infinite chain `... --log--> ^{n-1}F --log--> ^nF --log--> ...` inducing poly-isos on D-prime-strips; oriented graph ⃗Γ with Z-translation symmetry fixing the coric core ◦ | 34 |

Prop 1.2 proof: "follow immediately from the definitions and the references
quoted" (p. 35; no independent argument needed beyond [AbsTopIII] citations).

### Prop 1.3 (ii)(iii) — Hodge-theater level

- **(ii) Coricity**: any log-link `†HT --log--> ‡HT` induces a poly-iso
  `†HT^D-Θ^±ellNF ~→ ‡HT^D-Θ^±ellNF` (p. 42).
- **(iii) Further properties**: simultaneous compatibility with ring structures,
  log-volumes, Kummer theory, and log-shells (inherit Prop 1.2 (ii)–(ix)).

### Structural significance

Prop 1.2 (iv) (Kummer non-compatibility) is not a defect; it is the central
mechanism: the log-link is **incompatible** with conventional ring-structure
transport ("log-wall", Remark 1.2.4, p. 39).  Only D-prime-strip data is
manifestly coric.  This forces the IUT framework to work with log-shells as
containers rather than with exact ring-theoretic equalities.

---

## 4a.3 `iut:log_volume` — log-volume on log-shells

**IUTchIII source**: Prop 1.2 (iii)(v), pp. 31–32; Remark 1.2.1, p. 35;
Remark 1.2.2 (v), p. 37; [AbsTopIII] Prop 5.7, Cor 5.10

### Definition

The **log-volume** is the measure on the log-shell `I_v` (and related modules)
derived from:
- **v ∈ V^non**: the natural p_v-adic log-volume on the submodule
  `I_v = (p*_v)^{-1} · log_v(O^×_{K_v}) ⊆ K_v`,
  where `p*_v = p_v` (p_v odd) or `p^2_v` (p_v = 2).
  Source: [AbsTopIII] Prop 5.7 (i)(c), Cor 5.10 (i)(ii).
- **v ∈ V^arc**: the angular log-volume on `Ψ^×_†F_v` (domain of log-link)
  and the radial log-volume on `Ψ^gp_log(†F_v)` (codomain).
  Source: [AbsTopIII] Prop 5.7 (ii), Cor 5.10 (ii); Remark 1.2.1.

### Log-volume compatibility (Prop 1.2 (iii))

The diagram (∗non)/(∗arc) is **compatible** with these log-volumes.
Concretely: the log-link does not change log-volumes even though it fails
to be a ring homomorphism.

Remark 1.2.2 (v) clarifies: although ⃗Γ is far from commutative, it is
**"commutative with respect to log-volumes"**.  This permits consistent
log-volume computation across all composites of ⃗Γ-arrows.

### Role in Cor 3.12 / Theorem B

Log-volume is the quantitative measurement applied in IUTchIII §3.
Upper semi-compatibility (Remark 1.2.2 (iii)) — the log-shells contain
Kummer images from **both** domain and codomain of the log-link:

    O^▷_{K_v} ⊆ I_v  and  log_v(O^×_{K_v}) ⊆ I_v   (Prop 1.2 (v)(bnon)(cnon))

— gives an **upper bound** on log-volume (not an equality), which is the
form used in Cor 3.12.  Prop 3.9 (iv) extends this compatibility to the
full multiradial setting.

### Archimedean weight convention (Remark 1.2.1 (i))

At v ∈ V^arc, `Ψ^gp_†F_v / Ψ^µN_†F_v` is assigned "weight N" so that its
log-volume equals that of `Ψ^×_†F_v`.  This weight convention is purely
book-keeping; it does not affect computations.

---

## 4a.4 [DISPUTED] log-link: essential non-triviality vs. identity-equivalence

This dispute is recorded in `docs/section_4_log_link.md §4.2` (sub_2) and
in `docs/disputes.md`.  Cross-reference only; no new claims added here.

**Mochizuki** (IUTchIII Def 1.1, Prop 1.3 (i)): the full log-link employs the
**full poly-isomorphism** `log(†F) ~→ ‡F`, which is specifically chosen
to be "free of any dependence on the Frobenius-like monoids involved"
(Remark 1.1.2 (i), p. 29).  The tautological log-link has a rigid "rigidifying
path"; the full log-link replaces this with a "tautologically indeterminate
isomorphism".  This indeterminacy is not a flaw; it is what permits the
etale-like Π_v to serve as the invariant (coric) core.

**Scholze–Stix** (SS §2.1.3, p. 6; fn. 8, p. 7): "the endofunctor log is
naturally equivalent to the identity."  SS argues that if all Hodge theaters
arise from a fixed curve X, then `K_1 ≅ K_2 = k̄` and there is a natural
`Π_1 ≅ Π_2`-equivariant isomorphism `log(K_1) ≅ K_2` — making the
indeterminacy unnecessary.

**Status**: [DISPUTED] — no third-party resolution as of 2026-05-06.  
Connection to `sub_2` of section_4_log_link.md §4.2: same dispute,
now with Prop 1.3 (i) construction detail attached.

---

## Forbidden translations

- "log-shell" — do not render as 「対数殻」 or any coined term; use log-shell.
- "full poly-isomorphism" — do not simplify to "isomorphism"; the poly prefix
  (= orbit of isomorphisms) carries content.
- "upper semi-compatibility" — not "approximate commutativity" or "weak equality";
  it is a containment statement (`I_v ⊇ both Kummer images`), not an equation.
- "coric" — do not translate as "invariant"; coricity is a specific technical
  notion (independence from the arithmetic holomorphic structure on either side).
- "tautological log-link" vs "full log-link" — distinct; do not conflate.
- log-volume "commutativity" (Rem 1.2.2 (v)) refers only to log-volume
  consistency across ⃗Γ-composites, not commutativity of ⃗Γ as a diagram.

---

## Cross-reference

| IRI | Link |
|-----|------|
| `iut:log_link` | parent entity (Construction); depends_on iut:log_shell |
| `iut:log_shell` | existing entity; IUTchIII Def 1.1 (i)(ii), Prop 1.2 (v) |
| `iut:HodgeTheater` | `iut:log_link_construction` depends_on this |
| `iut:F_prime_strip` | fundamental object for Prop 1.2 |
| `iut:multiradial_algorithm` | consumes `iut:log_volume` in §3 |
| `iut:Ind3` | log-volume indeterminacy; depends_on iut:log_shell |
| `iut:Cor.3.12` | uses log-volume upper bound from Prop 1.2 (iii)(v) |

---

## Verification log

| Claim | Source | Status |
|-------|--------|--------|
| Tautological log-link definition (Def 1.1 (i)) | IUTchIII p. 23–24 direct read | ✅ text confirmed |
| Full log-link = post-compose with full poly-iso | IUTchIII p. 24 direct read | ✅ text confirmed |
| Prop 1.2 (i) coricity | IUTchIII p. 31 direct read | ✅ text confirmed |
| Prop 1.2 (ii) ring struct. compat. | IUTchIII p. 31 direct read | ✅ text confirmed |
| Prop 1.2 (iii) log-volume compat. | IUTchIII p. 31 direct read | ✅ text confirmed |
| Prop 1.2 (iv) Kummer non-compat. | IUTchIII p. 31 direct read | ✅ text confirmed |
| Prop 1.2 (v) containment O^▷ ⊆ I_v | IUTchIII p. 31–32 + Rem 1.2.2 (i) | ✅ text confirmed |
| Log-shell I_v = (p*_v)^{-1} log_v(O^×) | IUTchIII p. 24, Rem 1.2.2 (i) p. 36 | ✅ explicit formula |
| I_v (archimedean) = {a | |a| ≤ π} | IUTchIII Rem 1.2.2 (ii) p. 36 | ✅ text confirmed |
| Prop 1.3 (i) HT-level log-link | IUTchIII p. 42 direct read | ✅ text confirmed |
| Def 1.4 log-theta-lattice | IUTchIII p. 45 direct read | ✅ text confirmed |
| SS "naturally equivalent to identity" | SS §2.1.3 p. 6 (not re-fetched; recorded from section_4_log_link.md §4.2) | [DISPUTED] carry-over |

---

## Sources

| Reference | URL / Locator |
|-----------|---------------|
| IUTchIII PDF (RIMS) | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf> |
| IUTchIII PRIMS 2021 | <https://doi.org/10.4171/PRIMS/57-1-3> |
| SS "Why abc is still a conjecture" | <https://web.archive.org/web/2024/https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf> |
| [AbsTopIII] (log-volume) | IUTchIII citations: [AbsTopIII] Prop 5.7, Cor 5.10 |
| Alien Copies survey | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf> |
