# Section 4b: log-shell I_v — Deep Properties (Mochizuki-side draft)

> status: mochizuki-side draft | 3-agent verify: pending | verified_at: 2026-05-06
> source: IUTchIII Def 1.1-i (log-shell), Prop 1.2 (iii)(iv)(v), Remark 1.2.2 (iii)(iv)(v)
> new IRIs: `iut:log_shell_containment`, `iut:log_volume_integration`, `iut:upper_semi_compatibility`
> NOT a duplicate of `iut:log_shell` (Definition) — this doc extracts its **properties layer**
> IRI flat: no sub-namespacing

---

## 4b.1 [iut:log_shell_containment] — Prop 1.2 (v): O^▷_{K_v} ⊆ I_v

### Formal statement (Prop 1.2 (v), IUTchIII p. 31–32)

At `v ∈ V^non`, the holomorphic log-shell `I_{†F_v} ⊆ log(†F_v)` satisfies:

- **(a_non)** `I_{†F_v}` is compact, hence of finite log-volume
  [AbsTopIII Cor 5.10 (i)].
- **(b_non)** `I_{†F_v}` contains the submonoid of `†Π_v`-invariants of
  `Ψ_{log(†F_v)}` (= the image of `Ψ^×_{†F_v}` under the log-map).
- **(c_non)** `I_{†F_v}` contains the image of the submonoid of
  `†Π_v`-invariants of `Ψ^×_{†F_v}`.

Concrete form (Remark 1.2.2 (i), p. 36): for `k = K_v`,

```
I_k  :=  (p*_v)^{-1} · log_k(O^×_k)  ⊆  k

O^▷_k  :=  O_k \ {0}  ⊆  O_k  ⊆  I_k        [property (b_non)]
log_k(O^×_k)  ⊆  I_k                           [property (c_non)]
```

where `p*_v = p_v` (p odd), `p*_v = p_v^2` (p = 2).

At `v ∈ V^arc` (Remark 1.2.2 (ii), p. 36):

```
I_k  :=  { a ∈ k | |a| ≤ π }
O^▷_k  ⊆  O_k  ⊆  I_k                          [property (b_arc)]
O^×_k  ⊆  exp_k(I_k)                            [property (c_arc)]
```

### Role in the proof

The two containments (b_non)/(c_non) mean that `I_v` simultaneously
contains the Kummer images from **both** domain and codomain of the
log-link: `†F` via (c_non), `‡F` via (b_non). This double-containment is
the mechanism by which the log-shell "bridges" two mutually alien
arithmetic holomorphic structures without requiring a ring-theoretic
isomorphism between them.

> Source: IUTchIII Def 1.1 (i), Prop 1.2 (v), Remark 1.2.2 (i)(ii), pp. 23–36.
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 4b.2 [iut:log_volume_integration] — Prop 1.2 (iii): log-volume compatibility

### Formal statement (Prop 1.2 (iii), IUTchIII p. 31)

At `v ∈ V^non`, the diagram

```
Ψ_{†F_v} ⊇ Ψ^×_{†F_v}  →  log(†F_v) = Ψ^{gp}_{log(†F_v)}  ~→  Ψ^{gp}_{‡F_v}
                                          (*non)
```

is compatible with the natural `p_v`-adic log-volumes
[AbsTopIII Prop 5.7 (i)(c); Cor 5.10 (ii)] on the subsets of
`†Π_v`-invariants of `Ψ^{gp}_{†F_v}` and `Ψ^{gp}_{log(†F_v)}`.

At `v ∈ V^arc`, the diagram `(*arc)` is compatible with:

- the natural **angular** log-volume on `Ψ^×_{†F_v}`, and
- the natural **radial** log-volume on `Ψ^{gp}_{log(†F_v)}`

(cf. Remark 1.2.1 (i)(ii), p. 35).

### Interpretation (Remark 1.2.2 (v), p. 37)

> "although the diagram corresponding to ⃗Γ fails to be commutative,
> it is nevertheless **commutative with respect to log-volumes**"

This "log-volume commutativity" allows log-volumes to be computed
consistently across all composites of log-link arrows in the oriented
graph ⃗Γ (the Frobenius-picture of Prop 1.2 (x)). Technically:

- The log-volume of `I_v` is preserved under iteration of log-links.
- No renormalization is needed when passing between `n`-th iterate
  log-link images of `O^×_{K_v}`.

This property is the **foundation for the log-volume estimates** at
Prop 3.9 (iv) and the global bound in Cor 3.12 (IUTchIII §3).

> Source: IUTchIII Prop 1.2 (iii), Remark 1.2.1 (i)(ii), Remark 1.2.2 (v), pp. 31–37.
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 4b.3 [iut:upper_semi_compatibility] — Remark 1.2.2 (iii)+(iv): Kummer upper semi-commutativity

### Context: Kummer non-compatibility (Prop 1.2 (iv), p. 31)

The Kummer isomorphisms

```
Ψ_cns(†F)  ~→  Ψ_cns(†D)
Ψ_cns(‡F)  ~→  Ψ_cns(‡D)
```

**fail** to be compatible with the poly-isomorphism
`Ψ_cns(†D) ~→ Ψ_cns(‡D)` induced by the log-link, relative to
the diagrams `(*non)`, `(*arc)` [AbsTopIII Cor 5.5 (iv)].

This is the central "incompatibility" fact that governs the theory of §1.

### Upper semi-commutativity (Remark 1.2.2 (iii), p. 37)

Despite Prop 1.2 (iv), Mochizuki observes:

> "the coric holomorphic log-shells of Proposition 1.2, (ix), contain not
> only the images, via the Kummer isomorphisms [...], of the various `O^▷`
> at `v ∈ V^non`, but also the images, via the **composite of the Kummer
> isomorphisms with the various iterates of the log-link** [...], of the
> portions of the various `O^▷` at `v ∈ V^non` on which these iterates
> are defined."

The formal consequence: although ⃗Γ is **not commutative**, the coric
holomorphic log-shells exhibit

> "a sort of **upper semi-commutativity** with respect to
> containing/surjecting onto the various images arising from composites
> of arrows in ⃗Γ."
> — Remark 1.2.2 (iii), IUTchIII p. 37

### Absence of lower semi-commutativity (Remark 1.2.2 (iv), p. 37)

Mochizuki explicitly notes there is **no** "lower semi-commutativity":
a lower version would require a collection of portions of `O^▷`'s mapped
isomorphically by `log_k`/`exp_k` and compatible with all Kummer
isomorphisms simultaneously — which cannot be constructed.

### Role in Cor 3.12

Upper semi-compatibility provides the containment direction needed for
the **log-volume upper bound** (not an equality) at Cor 3.12:

```
[log-shell I_v] ⊇ [Kummer images from both sides of log-link]
          ↓
log-volume(I_v) ≥ log-volume(Kummer images)
          ↓
Cor 3.12: upper bound on -|log(Θ)| in terms of |log(q)|
```

The asymmetry upper/lower is the reason the final estimate is an
inequality `−|log(Θ)| ≥ −|log(q)|` rather than an equality.

> Source: IUTchIII Prop 1.2 (iv), Remark 1.2.2 (iii)(iv), pp. 31–37.
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 4b.4 [CLAIMED_BY: Mochizuki] — Scholze-Stix scope note

The three properties documented above (§4b.1–4b.3) are **not directly
analysed** by Scholze-Stix (SS 2018). SS §2.1.3 (pp. 6–7) confirms the
log-shell definition and log-map bijectivity, but limits its critique to
the claim that the log-link endofunctor is "naturally equivalent to the
identity" (SS p. 6). SS does not:

- dispute the formal correctness of Prop 1.2 (iii)(iv)(v),
- analyse the upper semi-compatibility (Remark 1.2.2 (iii)), or
- engage with the log-volume integration foundation for Cor 3.12.

SS's silence on these properties does **not** constitute acceptance; it
reflects the scope limitation that SS explicitly acknowledges (SS p. 3:
"We focus on Corollary 3.12 and the step in its proof which we find
problematic").

Status of all three entities: **[CLAIMED_BY: Mochizuki]** — formally
stated in IUTchIII, not independently verified or disputed by SS.

---

## Cross-reference

- entities.json: `iut:log_shell` (parent Definition), `iut:log_link`,
  `iut:Cor.3.12`, `iut:Ind3`, `iut:multiradial_algorithm`
- New entities (this draft): `iut:log_shell_containment`,
  `iut:log_volume_integration`, `iut:upper_semi_compatibility`
- Related sections:
  - Section 4 overview: `docs/section_4_log_link.md` (§4.3 summarises these)
  - Section 5 (Cor 3.12): log-volume upper bound depends on §4b.2+§4b.3
  - Section 3b (`iut:theta_gau_link`): uniradial → multiradial requires log-link

## Sources

| Reference | Content |
|---|---|
| IUTchIII Def 1.1 (i)(ii) | log-shell formal construction (non-arch + arch) |
| IUTchIII Prop 1.2 (iii) | log-volume compatibility across log-link |
| IUTchIII Prop 1.2 (iv) | Kummer non-compatibility (AbsTopIII Cor 5.5 (iv)) |
| IUTchIII Prop 1.2 (v) | holomorphic log-shell containment (b_non)(c_non) |
| IUTchIII Remark 1.2.2 (i)(ii) | concrete containment O^▷ ⊆ I_k |
| IUTchIII Remark 1.2.2 (iii) | upper semi-commutativity statement |
| IUTchIII Remark 1.2.2 (iv) | absence of lower semi-commutativity |
| IUTchIII Remark 1.2.2 (v) | log-volume commutativity interpretation |
| IUTchIII Prop 3.9 (iv) | log-volume integration used in §3 |
| IUTchIII Cor 3.12 | log-volume upper bound (essential) |
| SS §2.1.3 pp. 6–7 | scope limitation: log-shell acknowledged, not disputed |

- IUTchIII PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
- IUTchIII DOI (PRIMS 2021): https://doi.org/10.4171/PRIMS/57-1-3
- SS PDF (Wayback): https://web.archive.org/web/2024/https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
