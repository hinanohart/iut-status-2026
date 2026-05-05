# Section 2c: NF-Hodge Theater and ΘellNF Integration (Deep)

**Source**: IUTchI §4/§5/§6
**PDF**: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf
**DOI**: 10.4171/PRIMS/57-1-1 | Extracted: 2026-05-06 (pymupdf, 186 pages)

---

## W1/W2 整合

`iut:HodgeTheater` (entities.json) = Θ±ellNF-HT の概念 entity (Def 6.13 triple 全体)。
本 2c は **sub-component** 4 件: NF_hodge_theater (D-level) / theta_NF_hodge_theater (F-level) / F_l_star_symmetry / theta_pm_ellNF_integration (Def 6.13 具体形)。

---

## 1. D-NF-bridge と D-ΘNF-Hodge theater (§4)

**Def 4.6 (i) p.111** — D-NF-bridge: poly-morphism `†D_J --†φ^NF_⋇--> †D^⊚`
where `†D^⊚ = B(C_K)^0`, `†D_J = {†D_j}_{j∈J}` capsule of D-prime-strips.
Morphism = pair (capsule-full on J, Aut_ε(D^⊚)-orbit on D^⊚ side).

**Prop 4.7 (iii) p.112** — bijection `†ζ^⋇ : LabCusp(†D^⊚) →∼ J →∼ F^⋇_l` ("combinatorial Kodaira-Spencer", Remark 4.7.2 iii).

**Def 4.6 (iii) p.112** — D-ΘNF-HT:
```
†HT^{D-ΘNF} = ( †D^⊚ <--†φ^NF_⋇-- †D_J --†φ^Θ_⋇--> †D_> )
```

**Prop 4.8 (i/ii/iii) p.115**:
- (i) isos between two D-NF-bridges = F^⋇_l-torsor
- (ii) isos between two D-Θ-bridges (or D-ΘNF-HTs) = cardinality **one**
- (iii) gluing D-NF-bridge + D-Θ-bridge → F^⋇_l-torsor of gluings

---

## 2. ΘNF-Hodge theater — Frobenius level (§5)

**Def 5.5 (i) p.151** — NF-bridge:
```
‡F_J --‡ψ^NF_⋇--> ‡F^⊚ ↪ ‡F^⊛
```
Components: (a) capsule of F-prime-strips `‡F_J`; (b) Frobenioids `‡F^⊚`, `‡F^⊛` with base `‡D^⊚ → ‡D^⊛`; (d) `‡ψ^NF_⋇` lifts `‡φ^NF_⋇` **uniquely** (Cor 5.3 ii).

**Def 5.5 (iii) p.153** — ΘNF-HT:
```
‡HT^{ΘNF} = ( ‡F^⊛ ↩ ‡F^⊚ <--NF-- ‡F_J --Θ--> ‡F_> ↪ ‡HT^Θ )
```
Condition: `{‡φ^NF_⋇, ‡φ^Θ_⋇}` forms a D-ΘNF-HT.

**Cor 5.6 (ii/iii) p.153-154**:
- (ii) isos of ΘNF-HTs biject with isos of associated D-ΘNF-HTs
- (iii) gluing NF-bridge + Θ-bridge → F^⋇_l-torsor

---

## 3. F^⋇_l-symmetry (§4)

`F^⋇_l def= F^×_l / {±1}`, cardinality `l^⋇ = (l-1)/2` (§4 intro, p.95).

| property | locus | content |
|---|---|---|
| Simple transitivity | Prop 4.9 (i), p.115 | F^⋇_l acts simply transitively on J →∼ F^⋇_l |
| Arithmetic basepoint | Remark 6.12.6 (i), p.180 | permutes V^Bor = F^⋇_l · V^±un; multiple connected components at v |
| Holomorphic label bijection | Prop 4.7 (iii), p.112 | †ζ^⋇ : LabCusp(†D^⊚) →∼ J, "combinatorially holomorphic" |
| Nonarchimedean/multiplicative | Remark 4.7.2 (ii), p.114 | primes of number field, cyclic permutation |
| Coric symmetry | Fig. 6.4, p.178 | only {±1} shared with F^{⋊±}_l |
| UHP analogy | Fig. 6.4, p.178 | toral rotation; "functions" = elements of F_mod; prototype = nodes |

Key contrast with F^{⋊±}_l (iut:F_pm_ell_symmetry, a2b draft): excludes zero ∈ F_l; arithmetic vs geometric basepoint; no global ±-synchronization.

---

## 4. Θ±ellNF-HT integration — Def 6.13

**Def 6.13 (i) p.182** — a **triple**:
```
†HT^{Θ±ellNF} = ( †HT^{Θ±ell},  †HT^{ΘNF},  [necessarily unique] gluing iso )
```
- (a) Θ±ell-HT (Def 6.11 iii): additive/geometric F^{⋊±}_l side
- (b) ΘNF-HT (Def 5.5 iii): multiplicative/arithmetic F^⋇_l side
- (c) gluing iso — **necessarily unique** (Prop 4.8 ii + Cor 5.6 ii; Remark 6.12.2 i-ii p.174)

**Gluing construction** (Remark 6.12.2 i, p.174): Prop 6.7 gives functorial algorithm constructing D-Θ-bridge from Θ±-bridge; Θ-bridge portion ‡F_J → ‡F_> is then uniquely determined.

**Structural meaning** (Remark 6.12.6 v, p.181):
> "intricate relay between geometric and arithmetic basepoints" — enabling both (a) Hodge-Arakelov theta evaluation (F^{⋊±}_l geometric side) and (b) explicit F_mod construction (F^⋇_l arithmetic side).

Equivalently: "global combinatorial resolution of the two combinatorial dimensions (additive + multiplicative) of the ring Z" — treating F_l as finite approximation of Z.

**Def 6.13 (ii) p.183** — D-Θ±ellNF-HT: analogous base-level triple.

**Fig. 6.5 p.182** shows combined diagram with D_T (F^±_l-torsor, additive side) and D_J (F^⋇_l, multiplicative side) joined by the gluing.

---

## Source table

| locus | PDF p. | content |
|---|---|---|
| Def 4.6 (i)/(iii) | 111-112 | D-NF-bridge, D-ΘNF-HT |
| Prop 4.7 (iii) | 112 | †ζ^⋇ label bijection |
| Prop 4.8 | 115 | F^⋇_l-torsor / cardinality-1 |
| Prop 4.9 (i) | 115 | simple transitivity |
| Def 5.5 (i)/(iii) | 151-153 | NF-bridge, ΘNF-HT |
| Cor 5.6 (ii)/(iii) | 153-154 | iso bijection, gluing torsor |
| Remark 6.12.2 (i)-(ii) | 174 | gluing construction, uniqueness |
| Remark 6.12.6 (i)/(v) | 180-181 | arithmetic basepoint, Z resolution |
| Def 6.13 (i)/(ii) | 182-183 | Θ±ellNF-HT triple |
| Fig. 6.4 | 178 | UHP analogy table |
| Fig. 6.5 | 182 | combined diagram |
