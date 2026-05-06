# Section 4b: log-shell I_v — Deep Properties (merged v0.2)

> status: merged | sources: mochizuki-side (4b_log_shell_deep.md) + SS-side (4b_log_shell_deep_ss_view.md)
> verified_at: 2026-05-06
> IRIs: `iut:log_shell_containment` (Definition), `iut:log_volume_integration` (Theorem), `iut:upper_semi_compatibility` (Theorem)
> depends_on: `iut:log_shell` (parent Definition), `iut:log_link_construction`
> NOT a duplicate of `iut:log_shell` — this file documents the **properties layer** built on it

---

## 4b.1 [iut:log_shell_containment] — Definition

**Prop 1.2-v + Rem 1.2.2-i/ii (IUTchIII pp. 31–36)**

At `v ∈ V^non`, the holomorphic log-shell `I_{†F_v} ⊆ log(†F_v)` satisfies two containments:

```
O^▷_k  :=  O_k \ {0}  ⊆  I_k  :=  (p*_v)^{-1} · log_k(O^×_k)   [b_non]
log_k(O^×_k)  ⊆  I_k                                               [c_non]
```

where `p*_v = p_v` (p odd), `p*_v = p_v^2` (p = 2) (Rem 1.2.2-i).

At `v ∈ V^arc` (Rem 1.2.2-ii): `I_k := { a ∈ k | |a| ≤ π }`,
`O^▷_k ⊆ O_k ⊆ I_k` and `O^×_k ⊆ exp_k(I_k)`.

The double containment (b_non)/(c_non) means `I_v` simultaneously contains Kummer images
from **both** domain and codomain of the log-link (`†F` via c_non, `‡F` via b_non).
This is the mechanism by which log-shells bridge mutually alien arithmetic holomorphic
structures without requiring a ring-theoretic isomorphism.

**SS scope note:** SS §2.1.3 (pp. 6–7) confirms the log-shell definition and log-map
bijectivity. SS does not perform structural analysis of Prop 1.2-v or Rem 1.2.2-i/ii;
these propositions are outside the scope of SS's argument, which focuses on the
theta-link identification step (SS p.3: "We focus on Corollary 3.12 and the step in
its proof which we find problematic").

**Claim:** `claim:mochizuki_log_shell_containment_essential` — IUTchIII Prop 1.2-v
O^▷_K ⊆ I_v is the foundation for the Cor.3.12 log-volume estimate. [CLAIMED_BY: Mochizuki]

> Source: IUTchIII Def 1.1-i, Prop 1.2-v, Rem 1.2.2-i/ii, pp. 23–36.
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 4b.2 [iut:log_volume_integration] — Theorem

**Prop 1.2-iii + Rem 1.2.2-v + Prop 3.9-iv (IUTchIII)**

At `v ∈ V^non`, the diagram

```
Ψ_{†F_v} ⊇ Ψ^×_{†F_v}  →  log(†F_v)  ~→  Ψ^{gp}_{‡F_v}
```

is compatible with the natural `p_v`-adic log-volumes [AbsTopIII Prop 5.7-i-c; Cor 5.10-ii].
At `v ∈ V^arc`, the same diagram is compatible with angular and radial log-volumes
(Rem 1.2.1-i/ii).

Rem 1.2.2-v: although the diagram corresponding to ⃗Γ fails to be commutative,
it is **commutative with respect to log-volumes**. Concretely:

- The log-volume of `I_v` is preserved under iteration of log-links.
- No renormalization is needed when passing between nth-iterate log-link images of `O^×_{K_v}`.

This log-volume commutativity is the **foundation for the log-volume estimates**
at Prop 3.9-iv and the global bound in Cor 3.12 (IUTchIII §3).

**SS scope note:** SS §2.1.7 (p.8, "Concrete q-pilot object") and §2.2 (p.9) together
contain the single occurrence of "log-shell" in the SS PDF (pymupdf-verified, 10 pages).
The §2.2 occurrence treats log-shells as an encoding vehicle; SS does not analyse
log-volume compatibility or the ⃗Γ commutativity property. Prop 3.9-iv is outside SS scope.

> Source: IUTchIII Prop 1.2-iii, Rem 1.2.1-i/ii, Rem 1.2.2-v, Prop 3.9-iv, pp. 31–37.
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 4b.3 [iut:upper_semi_compatibility] — Theorem

**Prop 1.2-iv + Rem 1.2.2-iii/iv (IUTchIII pp. 31–37)**

The Kummer isomorphisms `Ψ_cns(†F) ~→ Ψ_cns(†D)`, `Ψ_cns(‡F) ~→ Ψ_cns(‡D)`
**fail** to be compatible with the poly-isomorphism `Ψ_cns(†D) ~→ Ψ_cns(‡D)`
induced by the log-link (Prop 1.2-iv; AbsTopIII Cor 5.5-iv). This Kummer
non-compatibility is the central incompatibility fact governing IUTchIII §1.

Despite this, Rem 1.2.2-iii establishes:

> "the coric holomorphic log-shells [...] contain not only the images,
> via the Kummer isomorphisms [...], of the various O^▷ at v ∈ V^non,
> but also the images, via the **composite of the Kummer isomorphisms with
> the various iterates of the log-link** [...], of the portions of the
> various O^▷ at v ∈ V^non on which these iterates are defined."

This gives a **upper semi-commutativity** of coric log-shells with respect to
containing/surjecting onto images arising from composites of arrows in ⃗Γ.

Rem 1.2.2-iv explicitly excludes lower semi-commutativity: a lower version
would require portions of O^▷ mapped isomorphically by `log_k`/`exp_k` and
simultaneously compatible with all Kummer isomorphisms — which cannot be constructed.

**Role in Cor.3.12:** Upper semi-compatibility provides the containment direction
for the log-volume upper bound (not equality):

```
I_v ⊇ Kummer images from both sides of log-link
  → log-volume(I_v) ≥ log-volume(Kummer images)
  → Cor.3.12: upper bound on -|log(Θ)| in terms of |log(q)|
```

The upper/lower asymmetry is why the final estimate is an inequality rather
than an equality.

**SS scope note:** Rem 1.2.2-iii/iv and Prop 1.2-iv are outside SS scope.
SS §2.2 (p.9) references log-shells as encoding vehicles; SS performs no
structural analysis of upper semi-compatibility or its role in Cor.3.12.

> Source: IUTchIII Prop 1.2-iv, Rem 1.2.2-iii/iv, pp. 31–37.
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 4b.4 Claim summary — [CLAIMED_BY: Mochizuki]

All three entities (§4b.1–4b.3) are formally stated in IUTchIII (published PRIMS 2021).
SS 2018 does not dispute the formal correctness of Prop 1.2-iii/iv/v or Rem 1.2.2-iii/iv.
These propositions are outside SS scope; SS's lack of structural analysis does not
constitute acceptance or rejection.

Active claim: `claim:mochizuki_log_shell_containment_essential`
- Prop 1.2-v O^▷_K ⊆ I_v + Rem 1.2.2-iii upper semi-compatibility jointly constitute
  the foundation for the Cor.3.12 log-volume estimate.
- SS PDF (10pp pymupdf-verified): 1 log-shell occurrence (§2.2 p.9 only).
  SS performs no independent analysis of Prop 1.2/Rem 1.2.2. These are outside SS scope.

---

## Sources

| Reference | Content |
|---|---|
| IUTchIII Def 1.1-i/ii | log-shell construction (non-arch + arch) |
| IUTchIII Prop 1.2-iii | log-volume compatibility across log-link |
| IUTchIII Prop 1.2-iv | Kummer non-compatibility |
| IUTchIII Prop 1.2-v | holomorphic log-shell containment b_non/c_non |
| IUTchIII Rem 1.2.2-i/ii | concrete containment O^▷ ⊆ I_k |
| IUTchIII Rem 1.2.2-iii | upper semi-commutativity |
| IUTchIII Rem 1.2.2-iv | absence of lower semi-commutativity |
| IUTchIII Rem 1.2.2-v | log-volume commutativity interpretation |
| IUTchIII Prop 3.9-iv | log-volume integration (§3) |
| IUTchIII Cor 3.12 | log-volume upper bound |
| SS §2.1.3 pp. 6–7 | log-shell acknowledged; no structural analysis of Prop 1.2-v |
| SS §2.2 p.9 | single log-shell occurrence (1/10 pages) |

- IUTchIII DOI: https://doi.org/10.4171/PRIMS/57-1-3
- SS PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
