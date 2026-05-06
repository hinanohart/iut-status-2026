# Section 4a: log-link IUTchIII Def 1.1 — merged (v0.2)

> Schema: v0.2
> Phase: 4a merged (REVISE applied: log_volume entity removed → 4b)
> Entities: 2 — iut:log_link_construction, iut:log_link_compatibility
> Claims added: 1 — claim:ss_log_link_naturally_equivalent_to_identity
> verified_at: 2026-05-06
> Sources: IUTchIII §1 (RIMS PDF direct read); SS §2.1.3 p.6 + fn.8

---

## REVISE note

`iut:log_volume` is **not** registered in this section.
`iut:Ind3` (entities.json) already records log-volume indeterminacy.
`4b_log_volume_integration` will carry the full log-volume entity and
Prop 1.2 (iii) / Prop 3.9 (iv) / Cor 3.12 pipeline.
Cross-references from the two entities below point to `iut:Ind3` and
`section_4b` accordingly.

---

## Entity 1: `iut:log_link_construction`

**Type**: Construction
**IUTchIII source**: Def 1.1 (i)(ii)(iii) pp. 23–27; Prop 1.3 (i) p. 42

### Construction (Def 1.1 (iii))

The **tautological log-link** at v ∈ V^non is the diagram

    †F_v  --log-->  log(†F_v)

where `log(†F_v)` is the Frobenioid determined by `{†Π_v ↷ Ψ_log(†F_v)}`,
and `Ψ_log(†F_v) ⊆ Ψ~_†F_v` is the multiplicative monoid of nonzero
integers inside the ind-topological field defined via the p_v-adic
logarithm on `(Ψ^×_†F_v)^pf` (the perfection of the units).

A **log-link from †F_v to ‡F_v** is any diagram obtained by
post-composing the tautological log-link with a [poly-]isomorphism
`log(†F_v) ~→ ‡F_v`. When that poly-isomorphism is the **full**
poly-isomorphism, the result is the **full log-link**.

At v ∈ V^arc the construction uses the complex archimedean logarithm
(Def 1.1 (ii) p. 25); the log-shell is the Ψ^×_log(†F_v)-orbit of
`{a ∈ k | |a| ≤ π}` (Rem 1.2.2 (ii) p. 36).

The **log-link between Θ^±ellNF-Hodge theaters** (Prop 1.3 (i) p. 42):
a fixed poly-iso `Ξ : †HT^D-Θ^±ellNF ~→ ‡HT^D-Θ^±ellNF` uniquely
determines constituent log-links `†F^□ --log--> ‡F^□`; the **full
log-link** `†HT --log--> ‡HT` uses the full poly-isomorphism for Ξ.

### SS view — [ALLEGED_GAP] at this entity

SS §2.1.3 p. 6: "the endofunctor log is **naturally equivalent to the
identity**" — construction accepted; non-triviality disputed.
See `claim:ss_log_link_naturally_equivalent_to_identity` (claims_4a_merged.json).

---

## Entity 2: `iut:log_link_compatibility`

**Type**: Definition
**IUTchIII source**: Prop 1.2 (i)–(x) pp. 30–34; Prop 1.3 (ii)(iii) p. 42

### Key compatibility properties (Prop 1.2)

| Sub | Statement | page | SS stance |
|-----|-----------|------|-----------|
| (i) Coricity | log-link induces poly-iso on D-prime-strips and D^⊢-prime-strips | 31 | [not analysed] |
| (ii) Ring struct. | Π_v-actions compatible with ind-topological ring structures (V^non); co-holomorphicizations compatible (V^arc) | 31 | [not analysed] |
| (iii) Log-volumes | compatible with p_v-adic / angular / radial log-volumes — detail in 4b | 31 | [not analysed] |
| (iv) Kummer FAIL | Kummer isos **not** compatible with log-link-induced D-iso ("log-wall") | 31 | morphism data only (p.7 fn.8) |
| (v) HoloLogShells | I_{†F_v} compact, finite log-volume; O^▷ ⊆ I_v and log(O^×) ⊆ I_v | 31–32 | [not analysed] |
| (viii) MA log-shells | poly-isos `log(†D^⊢) ~→ log(†F^⊢×µ) ~→ log(†F)` | 33 | [not analysed] |
| (ix) Coric HLS | functorial D-prime-strip algorithm for coric holomorphic log-shells | 34 | [not analysed] |
| (x) Frobenius-picture | infinite chain `... --log--> ^nF --log--> ...`; oriented graph ⃗Γ with Z-translation symmetry | 34 | [not analysed] |

Prop 1.2 proof: "follow immediately from the definitions and the
references quoted" (p. 35; relies on [AbsTopIII] citations).

### Hodge-theater level (Prop 1.3 (ii)(iii) p. 42)

- **(ii) Coricity**: log-link induces poly-iso `†HT^D-Θ^±ellNF ~→ ‡HT^D-Θ^±ellNF`.
- **(iii)**: simultaneous compatibility with ring structures, log-volumes,
  Kummer theory, log-shells (inherits Prop 1.2 (ii)–(ix)).

### Structural significance

Prop 1.2 (iv) ("log-wall", Remark 1.2.4 pp. 39–40) is not a defect.
Incompatibility with conventional ring-structure transport forces the
framework to work with log-shells as containers rather than ring-theoretic
equalities. Only D-prime-strip data is manifestly coric.

### SS view — [CLAIMED_BY: Mochizuki]

SS §2.1.3 p. 7 + fn. 8 states morphism data only (Π₁ ≅ Π₂,
`o_{log(K₁)} ≅ o_{K₂}`); HT-structure preservation (Prop 1.3 (i)),
Kummer non-compatibility (Prop 1.2 (iv)), and upper semi-compatibility
(Rem 1.2.2 (iii)) are not independently analysed by SS.

---

## Forbidden translations (carry-forward)

- "log-shell" — not 「対数殻」; use log-shell.
- "full poly-isomorphism" — not "isomorphism"; poly prefix carries content.
- "upper semi-compatibility" — a containment statement, not weak equality.
- "coric" — not "invariant"; coricity is independence from arithmetic
  holomorphic structure on either side.
- "tautological log-link" vs "full log-link" — distinct; do not conflate.

---

## Cross-reference

| IRI | Link |
|-----|------|
| `iut:log_link` | parent entity (Construction) |
| `iut:log_shell` | IUTchIII Def 1.1 (i)(ii), Prop 1.2 (v) |
| `iut:HodgeTheater` | `iut:log_link_construction` depends_on |
| `iut:F_prime_strip` | fundamental object for Prop 1.2 |
| `iut:Ind3` | log-volume indeterminacy (entities.json) |
| `iut:Cor.3.12` | uses log-volume upper bound (→ section 4b) |
| `claim:ss_log_link_naturally_equivalent_to_identity` | SS §2.1.3 p.6 gap claim |

---

## Sources

| Reference | URL |
|-----------|-----|
| IUTchIII PDF (RIMS) | https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf |
| IUTchIII PRIMS 2021 | https://doi.org/10.4171/PRIMS/57-1-3 |
| SS "Why abc is still a conjecture" | https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
| Wayback archive (SS) | https://web.archive.org/web/2024/https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
