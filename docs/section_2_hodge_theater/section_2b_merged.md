# Section 2b: Θ±ell-Hodge Theater — 3-agent merged

> Status: MERGED (mochizuki-side + SS-side). 2026-05-06.
> IRIs: `iut:theta_pm_ell_hodge_theater`, `iut:F_pm_ell_symmetry`, `iut:cusp_label_class`
> Primary source: IUTchI §6 (DOI 10.4171/PRIMS/57-1-1), pp. 155–183.
> SS source: Scholze-Stix 2018 (SS), 10 pp., full-text PDF-verified.

---

## 2b.1 F^{⋊±}_l-symmetry group (`iut:F_pm_ell_symmetry`)

**IUTchI Definition 6.1 (i), p. 155.**

```
F^{⋊±}_l  :=  F_l ⋊ {±1}
```

semi-direct product via the natural inclusion `{±1} → F^×_l`.

- **Positive** element: maps to `+1` via `F^{⋊±}_l ↠ {±1}`.
- **F^±_l-group**: set `E` with a `{±1}`-orbit of bijections `E →∼ F_l` (natural F_l-module structure).
- **F^±_l-torsor**: set `T` with an `F^{⋊±}_l`-orbit of bijections `T →∼ F_l`, action `z ↦ ±z + λ`.

**Role:** additive symmetry of the Θ±ell-Hodge theater, acting on label set
`(-l* < ... < 0 < ... < l*) ≅ F_l`. Contrast with F^⋇_l-symmetry (multiplicative,
ΘNF-Hodge theater, acting on `(1 < ... < l*) ≅ F^⋇_l`). (IUTchI Remark 6.12.3.)

**SS attitude:** full-text 0 occurrences of `F_l^±`, `additive symmetry`, or `F^{⋊±}_l`.
SS uses `Θ±ellNF` only as a type label (§2.1.2, p. 6). The `{±1}` automorphisms of
`X` are mentioned (SS p. 6: "identity and negation"), but the lift to `F^{⋊±}_l`-symmetry
on label indices is neither verified nor denied — SS scope excludes it.

---

## 2b.2 LabCusp±(D) — ±-label classes of cusps (`iut:cusp_label_class`)

**IUTchI Definition 6.1 (iii), pp. 156–157; Def 6.1 (v)–(vi), pp. 158–159.**

For a D-prime-strip `†D`:

- `LabCusp±(†D_v)` = ±-label classes of cusps at `v`; carries a natural **F^±_l-group
  structure** (`→∼ F_l`, well-defined up to `±1`).
- Includes a **zero element** `†η^0_v` and a **±-canonical element** `†η^±_v` (up to `±1`).
- Relation to non-pm version: `(LabCusp±(†D_v) \ {†η^0_v})/{±1} →∼ LabCusp(†D_v)`.

For the global object `D^{⊚±} = B(X_K)^0`:
`LabCusp±(†D^{⊚±})` carries an **F^±_l-torsor structure** determined by cusp `ε` (Def. 3.1 (f)).
Natural outer iso: `Aut±(D^{⊚±})/Autcsp(D^{⊚±}) →∼ F^{⋊±}_l` depends essentially on `ε`.

**SS attitude:** "cusp" 0 occurrences in SS 2018. The LabCusp± label structure is entirely
Mochizuki-side; SS's Cor. 3.12 critique (j² monodromy) does not invoke cusp labels.

---

## 2b.3 D-Θ±ell-Hodge theater (base level)

**IUTchI Definition 6.4 (i)–(iii), pp. 162–163.**

```
†HT^{D-Θ±ell} = (†D_≻ ←^{†φ^{Θ±}_±} †D_T →^{†φ^{Θell}_±} †D^{⊚±})
```

where:
- `†φ^{Θ±}_±`: D-Θ±-bridge — `†D_T` (capsule indexed by F^±_l-group `T`) → `†D_≻`.
- `†φ^{Θell}_±`: D-Θell-bridge — `†D_T` (T = F^±_l-torsor) → `†D^{⊚±}`.
- The label set of `†D_T` simultaneously carries F^±_l-group (Θ±-bridge side)
  and F^±_l-torsor (Θell-bridge side) structures, compatible via Prop. 6.5 (iii).

---

## 2b.4 Θ±ell-Hodge theater, Frobenius level (`iut:theta_pm_ell_hodge_theater`)

**IUTchI Definition 6.11 (i)–(iii), pp. 172–173.**

```
†HT^{Θ±ell} = (†F_≻ ←^{†ψ^{Θ±}_±} †F_T →^{†ψ^{Θell}_±} †D^{⊚±})
```

- `†ψ^{Θ±}_±`: Θ±-bridge (F-prime-strip capsule lifting the D-Θ±-bridge).
- `†ψ^{Θell}_±`: Θell-bridge (F-prime-strip capsule mapping into `†D^{⊚±}`,
  since `D^{⊚±}` does not carry Frobenius-like data in the same sense).
- The associated D-bridges must form a D-Θ±ell-Hodge theater.

**Corollary 6.12, p. 173:**
- Isomorphisms of Θ±ell-HT biject with isomorphisms of associated D-Θ±ell-HT.
- Gluing indeterminacy: torsor over `F^{⋊±}_l ×_∏ {±1}^V`.

**Definition 6.13 (Θ±ellNF-HT), p. 182:** triple of (Θ±ell-HT, ΘNF-HT,
necessarily unique gluing iso). The uniqueness follows from Prop. 4.8 (ii) + Cor. 5.6 (ii).

---

## 2b.5 Additive vs. multiplicative basepoints — conceptual role

**IUTchI Remark 6.12.6 (v), p. 181; Remark 6.12.3, p. 175.**

| Symmetry | Group | Basepoint | Role |
|---|---|---|---|
| Additive (Θ±ell side) | F^{⋊±}_l | single geometric basepoint (single `D_v`) | Hodge-Arakelov evaluation of étale theta in IUTchII |
| Multiplicative (ΘNF side) | F^⋇_l | arithmetic basepoints `V^{Bor}` | explicit construction of number field F_{mod} |

Coric symmetry common to both: `{±1}` only (Fig. 6.4, upper half-plane analogy).
Together they resolve, combinatorially, the additive and multiplicative dimensions of Z.

---

## 2b.6 SS attitude — scope summary

SS 2018 (10 pp., full-text verified):

| Term | SS occurrences | SS stance |
|---|---|---|
| `±ell` / `pm-ell` | 2 (type label `Θ±ellNF-` only) | Scope: categorical equivalence; internal structure not addressed |
| `F_l^±`, `additive symmetry`, `sigma-symmetry` | 0 | Not addressed |
| `cusp`, `cusp label`, `LabCusp±` | 0 | Not addressed |
| `{±1}` automorphisms | 1 mention ("identity and negation", SS p. 6) | Used only to state the `{X}` ↔ HT equivalence |

SS's sole direct use of `Θ±ellNF` (SS §2.1.2, p. 6):
> "…the natural functor from the category whose only object is X and whose morphisms
> are the automorphisms of X … to the category of Θ±ellNF-Hodge theaters is an equivalence
> of categories, as follows by combining [IUTT-1, Corollary 6.12 (i), Proposition 6.6 (iii),
> Corollary 5.6 (ii), Proposition 4.8 (ii), Definition 6.13]."

SS uses Cor. 6.12 (i) / Prop. 6.6 (iii) to assert the categorical equivalence, but does
not enter the internal `±ell`-bridge structure. The internal `F^{⋊±}_l`-symmetry and
`LabCusp±` mechanism are **[CLAIMED_BY: Mochizuki]**; SS is silent — not contradictory.

---

## Forbidden translations

Per `LLM_CONTEXT.md §4`: do NOT render `F^{⋊±}_l`, `LabCusp±`, or the Θ±ell-Hodge theater
in terms of perfectoid spaces, diamonds, condensed mathematics, or prismatic cohomology.
No such correspondence is established in IUTchI or SS 2018.

---

## Source citations

| Item | Source | Pages |
|---|---|---|
| Def. 6.1 (F^{⋊±}_l, LabCusp±) | IUTchI §6 (DOI 10.4171/PRIMS/57-1-1) | 155–159 |
| Def. 6.4 (D-Θ±ell-HT base bridges) | IUTchI §6 | 162–163 |
| Prop. 6.5 (label transport) | IUTchI §6 | 163–165 |
| Prop. 6.6 (first properties / torsors) | IUTchI §6 | 165–166 |
| Def. 6.11 (Θ±ell-HT Frobenius) | IUTchI §6 | 172–173 |
| Cor. 6.12 (iso bijection) | IUTchI §6 | 173 |
| Def. 6.13 (Θ±ellNF triple) | IUTchI §6 | 182 |
| SS §2.1.2 (sole Θ±ellNF mention) | Scholze-Stix 2018 | 6 |

---

## Verification status

- Mochizuki-side (§§2b.1–2b.5): text-extracted from IUTchI RIMS PDF (1.2 MB), 2026-05-06. ✅
- SS-side (§2b.6): pymupdf full-text extraction of SS 2018 (10 pp.), 0-occurrence counts verified, 2026-05-06. ✅
- 3-agent merge: completed 2026-05-06. ✅
