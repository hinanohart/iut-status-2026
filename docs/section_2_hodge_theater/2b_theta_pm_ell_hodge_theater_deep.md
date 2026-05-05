# Section 2b: Θ±ell-Hodge Theater (deep) — mochizuki-side draft

> Status: mochizuki-side DRAFT (not yet 3-agent merged).
> Source extraction: pymupdf from IUTchI RIMS PDF (1.2 MB), 2026-05-06.
> Primary references: IUTchI Defs 6.1, 6.4, 6.11, 6.13; Cor. 6.12; Props. 6.5, 6.6.
> IRI flat: `iut:theta_pm_ell_hodge_theater`, `iut:F_pm_ell_symmetry`, `iut:cusp_label_class`
> DOI: [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1)
> PDF: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>

---

## 2b.1 Notation: F^{⊛±}_l (= F^{⋊±}_l) symmetry group

**Definition 6.1, (i), p. 155.**

```
F^{⋊±}_l  :=  F_l ⋊ {±1}
```

where the semi-direct product is with respect to the natural inclusion `{±1} → F^×_l`.

- An element that maps to `+1` (resp. `−1`) via the surjection `F^{⋊±}_l ↠ {±1}` is called **positive** (resp. **negative**).
- An **F^±_l-group** is a set `E` equipped with a `{±1}`-orbit of bijections `E →∼ F_l`; it carries a natural `F_l`-module structure.
- An **F^±_l-torsor** is a set `T` equipped with an `F^{⋊±}_l`-orbit of bijections `T →∼ F_l`, relative to the action `F_l ∋ z ↦ ±z + λ`.

**Role in the theater:** The F^{⋊±}_l-symmetry is the *additive* symmetry of the Θ±ell-Hodge theater, acting on the label set `(-l* < ... < 0 < ... < l*)  ≅ F_l`. This contrasts with the **F^⋇_l-symmetry** (multiplicative, `≅ F^×_l`) of the ΘNF-Hodge theater acting on `(1 < ... < l*)  ≅ F^⋇_l`. (IUTchI Remark 6.12.3, p. 175.)

---

## 2b.2 LabCusp±(D) — ±-label classes of cusps

**Definition 6.1, (iii), pp. 156–157.**

For a D-prime-strip `†D = {†D_v}_{v∈V}`:

- A **±-label class of cusps** of `†D_v` is the set of cusps lying over a single cusp of `†D^±_v` (= `B(X_v)^0`, the "overcover" corresponding to `X_K → C_K`).
- Write `LabCusp±(†D_v)` for the set of ±-label classes.

**Key structure:**
- `LabCusp±(†D_v)` admits a natural `F^×_l`-action plus a **zero element** `†η^0_v` and a **±-canonical element** `†η^±_v` (well-defined up to `±1`).
- The bijection `(LabCusp±(†D_v) \ {†η^0_v})/{±1} →∼ LabCusp(†D_v)` sends `†η^±_v ↦ †ηv` (cf. Def. 4.1, (ii) for `LabCusp` without `±`).
- In particular, `LabCusp±(†D_v) →∼ F_l` (well-defined up to `±1`): it carries a natural **F^±_l-group structure**. (p. 157.)

**For D^{⊚±} = B(X_K)^0 (Definition 6.1, (v)–(vi), pp. 158–159):**

- `LabCusp±(†D^{⊚±})` = set of cusps of `†D^{⊚±}`.
- Equipped with a natural **F^±_l-torsor structure** coming from the cusp `ϵ` of `C_K` (Def. 3.1, (f)).
- The natural outer isomorphism `Aut±(D^{⊚±})/Autcsp(D^{⊚±}) →∼ F^{⋊±}_l` depends essentially on the choice of `ϵ`.

**Contrast with LabCusp(D^⊚) (without ±, §4):** `LabCusp(†D^⊚)` has an F^⋇_l-torsor structure and tracks non-zero cusps only. `LabCusp±` includes the zero element `†η^0_v`, enabling the additive symmetry to relate zero-labeled and non-zero-labeled prime-strips. (IUTchI Remark 6.12.5, p. 179.)

---

## 2b.3 D-Θ±-bridge and D-Θell-bridge (base-Θ± structures)

**Definition 6.4, (i)–(ii), pp. 162–163.**

### D-Θ±-bridge

A poly-morphism `†D_T →^{†φ^{Θ±}_±} †D_≻` where:
- `†D_≻` is a D-prime-strip; `T` is an **F^±_l-group**; `†D_T = {†D_t}_{t∈T}` is a capsule of D-prime-strips indexed by `T`.
- Compatible up to isomorphisms `D_≻ →∼ †D_≻`, `D_± →∼ †D_T` (with the bijection `F_l →∼ T` being an isomorphism of F^±_l-groups).
- Write `†D_{|T|}`: the `l±`-capsule (= `l* + 1 = (l+1)/2` components) obtained by collapsing via the `{±1}`-quotient `T ↠ |T|`.
- Write `†D_{T^⋇}`: the `l*`-capsule on `T^⋇ := |T| \ {0}` (nonzero labels).

### D-Θell-bridge

A poly-morphism `†D_T →^{†φ^{Θell}_±} †D^{⊚±}` where:
- `†D^{⊚±} ≃ D^{⊚±}`; `T` is an **F^±_l-torsor**; `†D_T` a capsule of D-prime-strips.
- The bijection `F_l →∼ T` is an isomorphism of F^±_l-torsors.

### D-Θ±ell-Hodge theater (base version)

**Definition 6.4, (iii), p. 163.**

```
†HT^{D-Θ±ell} = (†D_≻ ←^{†φ^{Θ±}_±} †D_T →^{†φ^{Θell}_±} †D^{⊚±})
```

where `T` is an F^±_l-group, `†φ^{Θ±}_±` is a D-Θ±-bridge, `†φ^{Θell}_±` is a D-Θell-bridge.

The label set of `†D_T` simultaneously carries:
- an F^±_l-**group** structure (from the Θ±-bridge side, tracking `(-l* < ... < l*)`)
- an F^±_l-**torsor** structure (from the Θell-bridge side, via `LabCusp±(D^{⊚±})`)

---

## 2b.4 Transport of ±-label classes (Proposition 6.5)

**Proposition 6.5, pp. 163–165.**

Given `†HT^{D-Θ±ell}`:

(i) For each `v ∈ V`, `t ∈ T`, the D-Θell-bridge induces a well-defined bijection
```
†ζ^{Θell}_{vt} : LabCusp±(†D_{vt}) →∼ LabCusp±(†D^{⊚±})
```
compatible with the F^±_l-torsor structures; cross-comparisons `†ξ^{Θell}_{vt,wt}` are compatible with the F^±_l-group structure.

(ii) The D-Θ±-bridge induces `†ζ^{Θ±}_{vt} : LabCusp±(†D_{vt}) →∼ LabCusp±(†D_{≻,v})` compatible with F^±_l-group structures.

(iii) The assignment `T ∋ t ↦ †ζ^{Θell}_t(0)` determines a well-defined bijection
```
(†ζ^±)^{-1} : T →∼ LabCusp±(†D^{⊚±})
```
compatible with the F^±_l-torsor structures.

**Significance:** These bijections realize the *synchronization of ±-labels* across all valuations `v ∈ V` — essential for the functorial algorithm that constructs `†HT^{D-Θ±ell}` from `D^{⊚±}`.

---

## 2b.5 First properties of D-Θ±ell-Hodge theaters (Proposition 6.6)

**Proposition 6.6, (i)–(v), pp. 165–166.**

| Object | Isomorphism group |
|---|---|
| Two D-Θ±-bridges | `{±1} ×_∏ {±1}^V`-torsor |
| Two D-Θell-bridges | `F^{⋊±}_l`-torsor (outer iso to F^{⋊±}_l) |
| Two D-Θ±ell-Hodge theaters | `{±1}`-torsor |
| Gluing D-Θ±-bridge + D-Θell-bridge | `F^{⋊±}_l ×_∏ {±1}^V`-torsor |

From a given D-Θell-bridge, a D-Θ±ell-Hodge theater exists (functorially, up to `F^{⋊±}_l`-indeterminacy). (Prop. 6.6, (v).)

---

## 2b.6 Θ±ell-Hodge theater (Frobenius-level) — Definition 6.11

**Definition 6.11, (i)–(iii), pp. 172–173.**

### Θ±-bridge (Frobenius level)

A poly-morphism `†F_T →^{†ψ^{Θ±}_±} †F_≻` of F-prime-strip capsules that lifts a D-Θ±-bridge.

### Θell-bridge (Frobenius level)

A D-Θell-bridge `†φ^{Θell}_± : †D_T → †D^{⊚±}` lifted to F-prime-strip level:
```
†F_T →^{†ψ^{Θell}_±} †D^{⊚±}
```
(The Θell-bridge at Frobenius level maps into `†D^{⊚±}`, not an F-prime-strip, since `D^{⊚±}` does not carry Frobenius-like data in the same sense.)

### Θ±ell-Hodge theater (`iut:theta_pm_ell_hodge_theater`)

```
†HT^{Θ±ell} = (†F_≻ ←^{†ψ^{Θ±}_±} †F_T →^{†ψ^{Θell}_±} †D^{⊚±})
```

such that `{†φ^{Θ±}_±, †φ^{Θell}_±}` (the associated D-bridges) form a D-Θ±ell-Hodge theater.

**Corollary 6.12, p. 173:**
- The map from isomorphisms of Θ±ell-Hodge theaters to isomorphisms of associated D-Θ±ell-Hodge theaters is **bijective**.
- The gluing indeterminacy is a torsor over `F^{⋊±}_l ×_∏ {±1}^V` (same as base level).

---

## 2b.7 Θ±ellNF-Hodge theater — Definition 6.13 (`iut:theta_pm_ell_hodge_theater`)

**Definition 6.13, (i)–(ii), p. 182.**

```
†HT^{Θ±ellNF}
```

is a **triple** consisting of:
- (a) a Θ±ell-Hodge theater `†HT^{Θ±ell}` (Definition 6.11, (iii))
- (b) a ΘNF-Hodge theater `†HT^{ΘNF}` (Definition 5.5, (iii))
- (c) the [**necessarily unique!**] gluing isomorphism between them (uniqueness from Prop. 4.8 (ii) + Cor. 5.6 (ii))

The gluing is effected via the functorial algorithm of Proposition 6.7 (which constructs a D-Θ-bridge from a D-Θ±-bridge), and the uniqueness of the gluing isomorphism follows from Propositions 4.8, 6.6 and Corollaries 5.6, 6.12. (Remark 6.12.2, (ii), p. 174.)

**D-Θ±ellNF-Hodge theater (base version):** same triple structure with D-Θ±ell + D-ΘNF + unique gluing isomorphism. (Definition 6.13, (ii), p. 183.)

---

## 2b.8 Conceptual role: relay between geometric and arithmetic basepoints

**Remark 6.12.6, (v), p. 181; Remark 6.12.3, p. 175.**

A Θ±ellNF-Hodge theater is an "intricate relay between geometric and arithmetic basepoints":
- The **F^{⋊±}_l-symmetry** (additive, Θ±ell side) uses a *single geometric basepoint* = single connected component `D_v` at each `v ∈ V`; it is suited to the Hodge-Arakelov-theoretic evaluation of the étale theta function in IUTchII.
- The **F^⋇_l-symmetry** (multiplicative, ΘNF side) uses *arithmetic basepoints* `V^{Bor} = F^⋇_l · V^{±}_{un}`; it is suited to the explicit construction of the number field `F_{mod}`.
- Together they resolve, in a "global combinatorial" sense, the additive and multiplicative dimensions of the ring Z (Remark 6.12.3, (i), p. 175; Remark 6.12.6, (v), p. 181).

The **coric symmetries** common to both are `{±1}` only (cf. Fig. 6.4, p. 178; the upper half-plane analogy).

---

## Forbidden translations

Per `LLM_CONTEXT.md §4`: do NOT render `F^{⋊±}_l`, `LabCusp±`, the Θ±ell-Hodge theater, or the gluing isomorphism of Def. 6.13 in terms of perfectoid spaces, diamonds, condensed mathematics, or prismatic cohomology. No such correspondence is established in IUTchI or Scholze-Stix 2018.

---

## Source citations

| Item | Source | Page |
|---|---|---|
| Definition 6.1 (F^{⋊±}_l, LabCusp±, D^{⊚±}) | IUTchI §6, pp. 155–159 | DOI 10.4171/PRIMS/57-1-1 |
| Definition 6.4 (D-Θ±ell-HT, base bridges) | IUTchI §6, pp. 162–163 | DOI 10.4171/PRIMS/57-1-1 |
| Proposition 6.5 (transport of ±-label classes) | IUTchI §6, pp. 163–165 | DOI 10.4171/PRIMS/57-1-1 |
| Proposition 6.6 (first properties) | IUTchI §6, pp. 165–166 | DOI 10.4171/PRIMS/57-1-1 |
| Definition 6.11 (Θ±ell-HT, Frobenius level) | IUTchI §6, pp. 172–173 | DOI 10.4171/PRIMS/57-1-1 |
| Corollary 6.12 (iso bijection) | IUTchI §6, p. 173 | DOI 10.4171/PRIMS/57-1-1 |
| Definition 6.13 (Θ±ellNF-HT triple) | IUTchI §6, p. 182 | DOI 10.4171/PRIMS/57-1-1 |

---

## Verification status (mochizuki-side only — not yet 3-agent)

- 2b.1 F^{⋊±}_l group definition: **text-extracted from PDF p. 155** ✅
- 2b.2 LabCusp±(D) definition: **text-extracted from PDF pp. 156–159** ✅
- 2b.3 D-Θ±ell-Hodge theater (base): **text-extracted from PDF pp. 162–163** ✅
- 2b.4 Proposition 6.5 transport bijections: **text-extracted from PDF pp. 163–165** ✅
- 2b.5 Proposition 6.6 torsor structure: **text-extracted from PDF pp. 165–166** ✅
- 2b.6 Definition 6.11 Frobenius level: **text-extracted from PDF pp. 172–173** ✅
- 2b.7 Definition 6.13 triple: **text-extracted from PDF p. 182** ✅
- SS-side / neutral: NOT YET DRAFTED — pending phase B2b completion.
