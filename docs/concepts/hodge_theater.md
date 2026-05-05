# [iut:HodgeTheater] Θ±ellNF-Hodge theater
> 3-agent verify pending (mochizuki-side draft).
> Last verified: 2026-05-06.

## Definition (statement-level)

A **Θ±ellNF-Hodge theater** `†HT^{Θ±ellNF}` (relative to fixed initial Θ-data) is
defined as the triple: (a) a Θ±ell-Hodge theater `†HT^{Θ±ell}`; (b) a ΘNF-Hodge
theater `†HT^{ΘNF}`; (c) the necessarily unique gluing isomorphism between them.
Informally: a "miniature model of conventional scheme theory" (system of Frobenioids)
in which the additive and multiplicative dimensions of a number field are disentangled.
- Reference: Mochizuki, IUTch-I, Definition 6.13, (i), p. 182,
  DOI [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1),
  URL <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>

## Components (statement-level)

**Θ-Hodge theater.** Collection `({†F_v}_{v∈V}, †F^⊩_mod)`: at each `v ∈ V^non` a
Frobenioid `†F_v ≃ F_v`; at `v ∈ V^arc` a Kummer-structured datum; globally a
Frobenioid over `F_mod` encoding q-parameters and theta values.
- Reference: IUTch-I, Definition 3.6, pp. 87–88.

**Θ±ell-Hodge theater.** Additive component: tracks the geometric F^{⊛±}_l-symmetry
acting on labels `(-l* < ... < 0 < ... < l*) ≅ F_l`, each label represented by a
D-prime-strip; global portion = Galois category of finite étale coverings of X_K.
- Reference: IUTch-I, Definitions 6.4, (iii); 6.11, (iii); pp. 7, 14.

**ΘNF-Hodge theater.** Multiplicative component: tracks the arithmetic F^*_l-symmetry
on labels `(1 < ... < l*) ≅ F^*_l`, each a D-prime-strip; global portion = Galois
category of coverings of C_K, enabling descent K → F_mod.
- Reference: IUTch-I, Definitions 4.6, (iii); 5.5, (iii); pp. 7, 14.

**log-shell.** At nonarchimedean `v`: compact additive module
`I_v := p_v^{-1} · log_v(O^×_{K_v}) ⊆ K_v`. Satisfies `O^▷_{K_v} ⊆ I_v` and
`log_v(O^×_{K_v}) ⊆ I_v`, so it contains Kummer images from both sides of any
log-link. Archimedean analogue defined via complex logarithm [AbsTopIII, Def. 5.4, (v)].
- Reference: IUTch-III, Definition 1.1, (i)–(iii); Introduction p. 4,
  DOI [10.4171/PRIMS/57-3-1](https://doi.org/10.4171/PRIMS/57-3-1).

**log-volume integration.** Real-valued measure on log-shells. Compatibility of the
log-link with log-volumes [IUTch-III, Prop. 1.2, (iii)] converts log-Kummer
correspondences into the global bound `−|log(Θ)| ≥ −|log(q)|` (Thm B = Cor. 3.12),
from which the diophantine inequalities of IUTch-IV follow.
- Reference: IUTch-III, Corollary 3.12; IUTch-IV (title: "Log-volume Computations").

## Construction outline

- Fix **initial Θ-data** `(F/F, X_F, l, C_K, V, V^bad_mod, ε)`: elliptic curve `E_F`,
  prime `l ≥ 5`, valuation set `V`, bad-reduction locus. [IUTch-I, Def. 3.1, p. 61.]
- Build **prime-strips** (D, F, F^⊢, F^⊩) indexed by `v ∈ V`. [IUTch-I, Defs. 4.1, 5.2.]
- Assemble **Θ-Hodge theater** `†HT^Θ` carrying `Θ_v` at `v ∈ V^bad` and q-parameters.
  [IUTch-I, Def. 3.6; Cor. 3.7.]
- Separately construct **Θ±ell** (F^{⊛±}_l on X_K) and **ΘNF** (F^*_l on C_K), then
  glue via unique isomorphism of Prop. 6.7, identifying `±t ∈ F_l` with `j ∈ F^*_l`.
  [IUTch-I, Prop. 6.7; Def. 6.13; Remark 6.12.2, p. 174.]
- The **Θ-link** (full poly-iso `†F^⊩_tht →^∼ ‡F^⊩_mod`) between theaters generates
  the Frobenius-picture (chain) and étale-picture (D^⊢_>-coric hub).
  [IUTch-I, Cor. 3.7, (i); Cor. 3.8, pp. 11–15.]

## Role in IUT

Each Θ±ellNF-Hodge theater is the fundamental unit cell of IUT. The **Θ-link**
(horizontal) connects the theta-value data of one theater to the q-parameter data
of the next in a ring-structure-incompatible way, creating the "alien arithmetic
holomorphic structure" whose comparison is the core problem. The **log-link**
(vertical, IUTch-III §1) applies the p-adic logarithm within a single holomorphic
structure, producing log-shells that simultaneously house both sides of any
log-link. Iterating both yields the **log-theta-lattice** [IUTch-III, Def. 1.4],
whose noncommutativity encodes the incompatibility of ring structures across
horizontal arrows. The multiradial algorithms of IUTch-III Theorem 3.11 and the
log-volume estimate of Corollary 3.12 are stated entirely in terms of this lattice.

## Forbidden translations

Do NOT render any component in terms of: perfectoid spaces, diamonds, condensed
mathematics, prismatic cohomology. No such correspondence is established in the
primary sources.

## Source

- Mochizuki, IUTch-I, Publ. RIMS **57** (2021) 3–207, DOI [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1)
  — Defs. 3.1, 3.6, 4.6, 5.5, 6.4, 6.11, 6.13; Cors. 3.7, 3.8; Thm A.
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>
- Mochizuki, IUTch-II, Publ. RIMS **57** (2021) 209–401, DOI [10.4171/PRIMS/57-2-1](https://doi.org/10.4171/PRIMS/57-2-1)
  — Example 1.8, (ix) (log-shell multiradial version).
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf>
- Mochizuki, IUTch-III, Publ. RIMS **57** (2021) 403–626, DOI [10.4171/PRIMS/57-3-1](https://doi.org/10.4171/PRIMS/57-3-1)
  — Def. 1.1 (log-link / log-shell), Def. 1.4 (log-theta-lattice), Prop. 1.2, 1.3,
    Thm 3.11 (multiradial LGP), Cor. 3.12 (log-volume bound = Thm B).
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf>
- Mochizuki, IUTch-IV, Publ. RIMS **57** (2021) 627–723, DOI [10.4171/PRIMS/57-4-1](https://doi.org/10.4171/PRIMS/57-4-1)
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf>
