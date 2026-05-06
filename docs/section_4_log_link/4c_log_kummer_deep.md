# Section 4c: log-Kummer correspondence — Deep Analysis (Mochizuki-side draft)

> status: mochizuki-side draft | 3-agent verify: pending | verified_at: 2026-05-06
> source: IUTchIII Thm 3.11-ii; Prop 1.2-iv (log-wall)
> new IRI: `iut:log_Kummer_correspondence` (1 entity; phase_a4c budget exhausted)
> IRI flat; v0.2 schema (no `definition_locus`, no `informal_description`)
> depends_on: `iut:log_link_compatibility`, `iut:log_shell`

---

## 4c.1 [iut:log_Kummer_correspondence] — Thm 3.11 (ii)

**Title in paper**: "(log-Kummer Correspondence)" (IUTchIII p. 155)

For `n, m ∈ Z`, the Kummer isomorphisms of labeled data
```
Ψ_cns(^{n,m}F≻)_t  ~→  Ψ_cns(^{n,◦}D≻)_t          [IUTchII Cor 4.6-iii]
{π^{κ-sol}_1(^{n,m}D⊛) ↷ ^{n,m}M⊛_∞κ}_j  ~→  {…(^{n,◦}D⊚)…}_j
(^{n,m}M⊛_mod)_j  ~→  M⊛_mod(^{n,◦}D⊚)_j
```
induce isomorphisms between the vertically coric data of Thm 3.11 (i) and
corresponding data from each `^{n,m}HT^{Θ±ellNF}`, as follows.

**(a) Tensor packets of log-shells** — subject to **(Ind3)**:
as `m` varies in `Z`, upper semi-compatible relative to log-links of the n-th column
(inclusions `⊆` at `v_Q ∈ V^non_Q`; surjections `↠` at `v_Q ∈ V^arc_Q`).
[Prop 3.5-ii-a,b]

**(b) Splitting monoids** (`v ∈ V^bad`) — **precisely compatible** with log-links
as `m` varies; inter-`m` relations involve only roots of unity (= no indeterminacy).
[Props 3.5-i,ii-c; Prop 3.10-ii]

**(c) Number fields and global Frobenioids** — "MOD"-versions precisely compatible
across `m`; "mod"-versions are not. [Prop 3.10-iii; Rem 3.10.1]

**Log-volume precision** (Prop 3.9-iv): despite (Ind3) in (a), the isomorphisms of
(a) are **precisely compatible with log-volumes** as `m` varies. This is the datum
that makes the final bound in Cor 3.12 non-trivial.

> Source: IUTchIII Thm 3.11 (ii), pp. 155–156.

---

## 4c.2 Relation to log-wall (Prop 1.2-iv)

### Prop 1.2-iv: Kummer non-compatibility (log-wall)

The Kummer isomorphisms `Ψ_cns(†F) ~→ Ψ_cns(†D)`, `Ψ_cns(‡F) ~→ Ψ_cns(‡D)`
[IUTchII Cor 4.6-i] **fail** to be compatible with `Ψ_cns(†D) ~→ Ψ_cns(‡D)`
induced by the log-link, relative to `(*non)`,`(*arc)`. [AbsTopIII Cor 5.5-iv]

The oriented graph `⃗Γ` (Prop 1.2-x) encodes this as:
```
  ···  →  •  →  •  →  •  →  ···    (• = ^nF, horizontal = log-links)
           ↓  /diagonal              (↓ = Kummer isos, ◦ = ^nD coric)
           ◦
```
Vertical/diagonal arrows (Kummer) are not compatible with horizontal arrows
(log-links). This is the log-wall.

### How log-Kummer correspondence navigates the log-wall

Thm 3.11-ii does **not** eliminate Prop 1.2-iv incompatibility. Instead it works
with the **totality** of Kummer isomorphisms as `m` varies over `Z` as a system,
using `I_v` as a container (upper semi-compatibility, §4b.3) that absorbs (Ind3).
This is why:

1. The final bound is an **inequality** `−|log(Θ)| ≥ −|log(q)|` (not equality).
2. (Ind3) is unavoidable and explicitly listed in Thm 3.11 (ii).

Rem 3.11.4 (p. 168): "such 'Kummer isomorphisms' fail to give rise to a
'log-Kummer correspondence', i.e., they fail to satisfy mutual compatibility
properties of the sort discussed in the final portion of Theorem 3.11, (ii)."

---

## 4c.3 [DISPUTED] Essential role at Cor 3.12

**Mochizuki's claim**: Cor 3.12 Step (xi) applies Thm 3.11-ii to access
Frobenius-like objects `^{n,m}F` from the coric `^{n,◦}D` world via the system of
Kummer isomorphisms. Combined with (a)'s log-volume precision (Prop 3.9-iv),
this yields `−|log(Θ)| ≥ −|log(q)|`. Status: **[CLAIMED_BY: Mochizuki]**

Rem 3.12.2-iv (p. 170): "The log-Kummer correspondences … This is precisely
what is achieved by the log-Kummer correspondences."

**SS connection**: SS §2.2 p. 9 targets the abstract-to-concrete pilot object
transition at Cor 3.12 Step (xi), claiming Thm 3.11 becomes "trivial" under
their identification framework. SS does not analyse Thm 3.11-ii construction
internally; the dispute is at the level of the Cor 3.12 conclusion.
This connects to `claim:ss_log_link_naturally_equivalent_to_identity` (section 4a).

---

## 4c.4 SS-side scope

**pymupdf search** (`ss2018_ia.pdf`, 10 pages):

| Term | Hits |
|---|---|
| "log-Kummer" or "log-Kummer correspondence" | 0 |
| "Kummer" | 3 (pp. 5, 6, 7 — Kummer theory prerequisites; footnote fn.9) |
| "Thm 3.11" / "Theorem 3.11" | 2 (p. 9 — "trivial" claim at global level) |

SS's two references to Thm 3.11 (p. 9) concern the alleged triviality of the
multiradial algorithm as a whole. SS does **not** engage with the internal structure
of Thm 3.11-ii: the Kummer isomorphism system across `m ∈ Z`, the (Ind3)
mechanism, or the log-volume compatibility of Prop 3.9-iv.

**Scope**: log-Kummer correspondence (Thm 3.11-ii) is **out of scope** for SS's
explicit critique. SS p. 3: "We focus on Corollary 3.12 and the step in its proof
which we find problematic."

Status: **[CLAIMED_BY: Mochizuki]**, **[OUT_OF_SCOPE: Scholze-Stix]**

---

## Sources

| Reference | Content |
|---|---|
| IUTchIII Thm 3.11 (ii), pp. 155–156 | log-Kummer correspondence formal statement |
| IUTchIII Prop 1.2 (iv), p. 31 | Kummer non-compatibility (log-wall) |
| IUTchIII Prop 3.5 (ii) | splitting monoid Kummer compatibility |
| IUTchIII Prop 3.9 (iv) | log-volume precision across m ∈ Z |
| IUTchIII Rem 3.11.4, p. 168 | failure without full system |
| IUTchIII Rem 3.12.2 (iv), pp. 170–171 | role in Cor 3.12 |
| IUTchIII Cor 3.12 Step (xi) | application in final inequality |
| SS §2.2, p. 9; p. 3 (ss2018_ia.pdf) | scope declaration + "trivial" claim |

- IUTchIII DOI (PRIMS 2021): https://doi.org/10.4171/PRIMS/57-1-3
- IUTchIII PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
