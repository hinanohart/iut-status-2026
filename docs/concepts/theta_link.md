# [iut:theta_link] Θ-link (multiplicative)
> 3-agent verify pending (mochizuki-side draft).
> Last verified: 2026-05-06.

## Definition

A **Θ-link** `†HT^Θ →^Θ ‡HT^Θ` between two Θ-Hodge theaters is the
**full poly-isomorphism** (collection of all isomorphisms) of F⊩-prime-strips:

```
†F⊩_tht  ~→  ‡F⊩_mod
```

`†F⊩_tht` is built from the Frobenioid-theoretic theta function `Θ_v` (reciprocal
of the l-th root at `v ∈ V^bad`); `‡F⊩_mod` from the 2l-th roots of the
q-parameters `q_v`, each extended via the product formula.  No single isomorphism
is distinguished; the indeterminacy is intentional.

- Reference: IUTch-I, Corollary 3.7 (i), p. 88; Remark 3.7.1, p. 89;
  DOI [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1),
  URL <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>

## Key properties

- **(Cor. 3.7 (ii)–(iii)) Preserved data.** The link induces full poly-isos
  `†D⊢_v ~→ ‡D⊢_v` (base/étale-like, horizontally coric) and lifts to
  `O×_{†C⊢_v} ~→ O×_{‡C⊢_v}` (units). Value-group data is not preserved —
  the link dilates it by a symmetrized average of `j²` for `j = 1, …, l*`.
  [IUTch-I, Cor. 3.7 (ii)–(iii), p. 88–89.]
- **Multiplicative only.** The Θ-link involves only Frobenioid/monoid
  (multiplicative) structure.  It does not arise from a ring or scheme morphism;
  additive structure is deliberately "deactivated" across it.
  [IUTch-I, §I4, p. 26–27; "Alien Copies" §3.3 (ii), p. 60–61.]
- **Non-commutativity with log-link.** The two arrows of the log-theta-lattice
  — Θ-link (horizontal, multiplicative) and log-link (vertical, additive) —
  do not commute, mirroring the intertwining of Witt-vector extension structure
  with Frobenius in p-adic Teichmüller theory.
  [IUTch-I, §I4, p. 27; IUTch-III, Remark 1.4.1 (i).]
- **Frobenius-picture.** The infinite chain `... →^Θ nHT^Θ →^Θ (n+1)HT^Θ →^Θ ...`
  admits Z-translation symmetry but no permutation swapping adjacent indices.
  [IUTch-I, Cor. 3.8, p. 89.]

## Why Θ-link is "inter-universal"

The Θ-link separates two Hodge theaters whose ring-theoretic arithmetic holomorphic
structures are treated as **mutually alien** — abstract, tautologically distinct
copies of conventional scheme theory.  [The intended sense of "alien" is the Latin
root: abstract otherness.]  To compare `{q^{j²}_v}` (domain) with `q_v` (codomain),
one works with Frobenius-like monoid data stripped of its ambient ring structure,
which is only coherent if the two "universes" are regarded as genuinely distinct.
The two dimensions of the log-theta-lattice correspond to the two combinatorial
dimensions of a ring (addition ↔ log-links; multiplication ↔ Θ-links); the
Θ-link deactivates addition to make the multiplicative comparison well-defined
across alien copies.

> "A key aspect of inter-universal Teichmüller theory is the study of certain
> 'walls' or 'filters' … that separate two 'mutually alien' copies of conventional
> scheme theory." — Mochizuki, "Alien Copies" §1.3 / Abstract.

- Reference: "Mathematics of Mutually Alien Copies" §3.3 (ii), pp. 60–62,
  URL <https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf>

## Forbidden translations

Do NOT render the Θ-link or its "alien copies" as morphisms of perfectoid
spaces/diamonds, condensed modules, or prismatic Frobenius lifts.  No such
correspondence is established in the primary sources.

## Source

- Mochizuki, IUTch-I, Publ. RIMS **57** (2021) 3–207,
  DOI [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1) —
  Def. 3.6 (c); Def. 3.8 (i); Cors. 3.7, 3.8, 3.9; §I1, §I4.
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>
- Mochizuki, IUTch-II, Publ. RIMS **57** (2021) 209–401,
  DOI [10.4171/PRIMS/57-2-1](https://doi.org/10.4171/PRIMS/57-2-1) —
  Cor. 4.10 (iii); Def. 4.9 (vii) (F⊩×µ-prime-strip definition).
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf>
- Mochizuki, "Mathematics of Mutually Alien Copies," RIMS Kôkyûroku Bessatsu
  **B88** (2022) — §3.3 (ii), (vii), pp. 59–73.
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf>
