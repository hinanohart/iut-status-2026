# Section 2c: NF-Hodge Theater and Θ±ellNF Integration — 3-agent merged

> Status: MERGED (mochizuki-side + SS-side). 2026-05-06.
> IRIs: `iut:NF_hodge_theater`, `iut:theta_NF_hodge_theater`, `iut:F_l_star_symmetry`, `iut:theta_pm_ellNF_hodge_theater_integration`
> Primary source: IUTchI §4/§5/§6 (DOI 10.4171/PRIMS/57-1-1), pp. 95–183.
> SS source: Scholze-Stix 2018 (SS), 10 pp., full-text PDF-verified 2026-05-06.

---

## 2c.1 D-NF-bridge and D-ΘNF-Hodge theater (`iut:NF_hodge_theater`)

**IUTchI Definition 4.6 (i)/(iii), pp. 111–112.**

A **D-NF-bridge** is a poly-morphism of base-prime-strip data:
```
†φ^NF_⋇ : †D_J --poly--> †D^⊚
```
where `†D^⊚ = B(C_K)^0` and `†D_J = {†D_j}_{j∈J}` is a capsule of D-prime-strips.
The morphism consists of a capsule-full poly-automorphism on the J-side and an
`Aut_ε(D^⊚)`-orbit on the `D^⊚`-side.

A **D-ΘNF-Hodge theater** is the resulting triple:
```
†HT^{D-ΘNF}  =  ( †D^⊚  <--†φ^NF_⋇--  †D_J  --†φ^Θ_⋇-->  †D_> )
```
where `†φ^Θ_⋇` is a D-Θ-bridge (Def 4.6 ii).

**Prop 4.7 (iii), p. 112** — canonical bijection (combinatorial Kodaira-Spencer):
```
†ζ^⋇ : LabCusp(†D^⊚)  →∼  J  →∼  F^⋇_l
```
This is "combinatorially holomorphic" in the sense of Remark 4.9.2 iv.

**W1 note:** `iut:NF_hodge_theater` is a sub-component of `iut:HodgeTheater` (entities.json),
which records the full Θ±ellNF-HT triple at the conceptual level (Def 6.13). The D-ΘNF-HT
is the multiplicative/arithmetic (F^⋇_l) half of that triple at the base-category (D-) level.

**SS attitude:** SS 2018 full-text — `ΘNF` as standalone: 0 occurrences; `NF-Hodge` as standalone: 0
occurrences (the 2 occurrences of `NF` in SS are both within the compound label `Θ±ellNF`).
SS subsumes the entire Θ±ellNF-HT under the equivalence of categories `{X}` (SS §2.1.2, p. 6)
without decomposing the NF component individually.

---

## 2c.2 ΘNF-Hodge theater — Frobenius level (`iut:theta_NF_hodge_theater`)

**IUTchI Definition 5.5 (i)/(iii), pp. 151–153.**

An **NF-bridge** (Def 5.5 i) is:
```
‡ψ^NF_⋇ : ‡F_J  --poly-->  ‡F^⊚  ↪  ‡F^⊛
```
Uniqueness: the morphism `‡ψ^NF_⋇` lifts `‡φ^NF_⋇` uniquely (Cor 5.3 ii, p. 148).

A **ΘNF-Hodge theater** (Def 5.5 iii) is the Frobenius-level collection:
```
‡HT^{ΘNF}  =  ( ‡F^⊛  ↩  ‡F^⊚  <--NF--  ‡F_J  --Θ-->  ‡F_>  ↪  ‡HT^Θ )
```
such that `{‡φ^NF_⋇, ‡φ^Θ_⋇}` forms a D-ΘNF-HT (from 2c.1).

**Cor 5.6 (ii)/(iii), pp. 153–154:**
- (ii) Isos of ΘNF-HTs biject with isos of associated D-ΘNF-HTs.
- (iii) Gluing NF-bridge + Θ-bridge into a ΘNF-HT yields an F^⋇_l-torsor of gluings.

**W2 note:** `iut:theta_NF_hodge_theater` IS `iut:NF_hodge_theater` lifted to the Frobenius
(F-level) category; both entity IRIs are needed because the D-level / F-level distinction is
structurally essential in IUT (cf. `iut:etale_like_vs_frobenius_like`).

**SS attitude:** as in 2c.1 — 0 independent occurrences. Cor 5.6 (ii) is cited by SS in the
category-equivalence argument (SS p. 6, citing "[IUTT-1, Corollary 5.6 (ii)]"), but only as
one step in establishing the `{X}` equivalence, not as analysis of the ΘNF component itself.

---

## 2c.3 F^⋇_l-symmetry (`iut:F_l_star_symmetry`)

**IUTchI §4 intro, p. 95 (definition) + Prop 4.8–4.9, p. 115.**

```
F^⋇_l  :=  F^×_l / {±1}     |F^⋇_l|  =  l^⋇  :=  (l-1)/2
```

| Property | Locus | Content |
|---|---|---|
| Simple transitivity | Prop 4.9 (i), p. 115 | F^⋇_l acts simply transitively on J →∼ F^⋇_l |
| F^⋇_l-torsor of isos | Prop 4.8 (i), p. 115 | Isos between two D-NF-bridges = F^⋇_l-torsor |
| Gluing torsor | Prop 4.8 (iii), p. 115 | Gluing D-NF + D-Θ → F^⋇_l-torsor |
| Arithmetic basepoint | Remark 6.12.6 (i), p. 180 | Permutes V^Bor = F^⋇_l · V^±un (multiple connected components) |
| Label bijection | Prop 4.7 (iii), p. 112 | †ζ^⋇ : LabCusp(†D^⊚) →∼ J →∼ F^⋇_l |
| Nonarchimedean/multiplicative | Remark 4.7.2 (ii), p. 114 | Cusps = primes of number field; cyclic permutation |
| Coric symmetry | Fig. 6.4, p. 178 | Only {±1} shared with F^{⋊±}_l |

**Contrast with F^{⋊±}_l** (`iut:F_pm_ell_symmetry`, section 2b): F^⋇_l excludes zero
(no zero-labeled prime-strip), uses arithmetic basepoint (vs geometric), needs no global
±-synchronization. IUTchI Remark 6.12.3, p. 175 makes this contrast explicit.

**SS attitude:** `F_l^*` / `F^*` / `symmetry` — 0 occurrences in SS 2018 full text.
The two occurrences of `multiplicative` in SS (pp. 2–3) refer to Tate-curve bad reduction,
not to this symmetry group. This is the structural silence documented in
`claim:mochizuki_nf_symmetry_essential` below.

---

## 2c.4 Θ±ellNF-Hodge theater integration (`iut:theta_pm_ellNF_hodge_theater_integration`)

**IUTchI Definition 6.13 (i)/(ii), pp. 182–183.**

A **Θ±ellNF-Hodge theater** is the triple:
```
†HT^{Θ±ellNF}  =  ( †HT^{Θ±ell},   †HT^{ΘNF},   [necessarily unique gluing iso] )
```
- (a) `†HT^{Θ±ell}` (Def 6.11 iii): additive / geometric F^{⋊±}_l side.
- (b) `†HT^{ΘNF}` (Def 5.5 iii): multiplicative / arithmetic F^⋇_l side.
- (c) The gluing isomorphism is **necessarily unique** (Prop 4.8 ii + Cor 5.6 ii;
  Remark 6.12.2 i–ii, p. 174).

**Gluing construction** (Remark 6.12.2 i, p. 174): given a Θ±-bridge `†F_T → †F_≻`,
Prop 6.7 provides a functorial algorithm constructing the D-Θ-bridge; the Θ-bridge portion
`‡F_J → ‡F_>` is then uniquely determined.

**Structural meaning** (Remark 6.12.6 v, p. 181):
> "intricate relay between geometric and arithmetic basepoints"

enabling both (a) Hodge-Arakelov theta evaluation via F^{⋊±}_l and (b) explicit F_mod
construction via F^⋇_l. Equivalently: "global combinatorial resolution of the two
combinatorial dimensions (additive + multiplicative) of the ring Z".

**W1 note:** `iut:HodgeTheater` in entities.json is the conceptual entity for this triple;
`iut:theta_pm_ellNF_hodge_theater_integration` records the concrete Def 6.13 triple
with its uniqueness proof and structural role.

**SS attitude:** SS cites Definition 6.13 once, as part of the category-equivalence
argument (SS p. 6). The internal triple structure — and in particular the uniqueness of the
gluing and its structural meaning — is not analyzed individually. SS treats the full
Θ±ellNF-HT as the unit equivalent to `{X}`.
---
## Source table
| Locus | PDF p. | Content |
|---|---|---|
| Def 4.6 (i)/(iii) | 111–112 | D-NF-bridge, D-ΘNF-HT |
| Prop 4.7 (iii) | 112 | †ζ^⋇ label bijection |
| Prop 4.8 (i)/(ii)/(iii) | 115 | F^⋇_l-torsor / cardinality-1 / gluing torsor |
| Prop 4.9 (i) | 115 | Simple transitivity |
| Def 5.5 (i)/(iii) | 151–153 | NF-bridge, ΘNF-HT |
| Cor 5.6 (ii)/(iii) | 153–154 | Iso bijection, gluing torsor |
| Remark 6.12.2 (i)–(ii) | 174 | Gluing construction and uniqueness |
| Remark 6.12.3 | 175 | F^⋇_l vs F^{⋊±}_l contrast |
| Remark 6.12.6 (i)/(v) | 180–181 | Arithmetic basepoint, Z resolution |
| Def 6.13 (i)/(ii) | 182–183 | Θ±ellNF-HT triple |
| Fig. 6.4/6.5; SS §2.1.2 p.6, §2.1.4 p.7 | 178/182/6/7 | UHP analogy, combined diagram; SS sole NF/Frobenioid refs |
