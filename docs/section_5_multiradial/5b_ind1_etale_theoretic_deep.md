# Section 5b: Ind1 étale-theoretic deep — Mochizuki-side draft

> status: mochizuki-side draft | 3-agent verify: pending | verified_at: 2026-05-06
> source: IUTchIII Thm 3.11-i; Introduction pp. 11–12
> new IRIs: `iut:Ind1_d_prime_strip_aut`, `iut:Ind1_label_permutation`
> IRI flat; v0.2 schema; depends_on: [iut:Ind1, iut:D_prime_strip] / [iut:Ind1, iut:cusp_label_class]
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 5b.1 Ind1 two-component structure

Thm 3.11 (i), p. 154 — formal statement (verbatim):

> "(Ind1) the indeterminacies induced by the automorphisms of the procession
> of D⊢-prime-strips Prc(n,◦D⊢_T);"

Introduction p. 12 — explicit decomposition (verbatim):

> "(Ind1): This is the indeterminacy that arises from the automorphisms of
> processions of D⊢-prime-strips … i.e., more concretely, **from permutation
> automorphisms of the label sets S±_{j+1}** … **as well as from the
> automorphisms of the D⊢-prime-strips** that appear in these processions."

Two sub-indeterminacies:

| Sub-indeterminacy | Acts on | Type |
|---|---|---|
| D⊢-prime-strip Aut | individual slots n,◦D⊢_j (j = 0,…,l⋇) | étale-like / structural |
| label permutation | index sets S±_{j+1} (|S±_{j+1}| = j+1) | combinatorial |

The theorem body presents both as a single group action on the procession;
the Introduction separates them for conceptual clarity. A full automorphism
of Prc(n,◦D⊢_T) combines: permuting label slots *and* applying slot-wise
D⊢-prime-strip automorphisms.

---

## 5b.2 [iut:Ind1_d_prime_strip_aut] — D⊢-prime-strip Aut

**Domain**: individual D⊢-prime-strips n,◦D⊢_j within Prc(n,◦D⊢_T).

**Role**: the multiradial algorithm for `n,◦R^LGP` is required to be
*functorial with respect to isomorphisms of processions of D⊢-prime-strips*
(Thm 3.11-i, final clause, p. 154). Admitting D⊢-prime-strip Aut
indeterminacy is what enables this functoriality.

**Why D⊢, not D?** Passing from holomorphic D-prime-strips to
mono-analytic D⊢-prime-strips forgets the arithmetic holomorphic
structure of a specific vertical line (Introduction p. 12), making the
representation legible from an alien arithmetic holomorphic structure.
The Aut group of D⊢ is larger than that of D; this larger indeterminacy
is the structural price of multiradiality.

> Source: IUTchIII Thm 3.11 (i), p. 154; Introduction pp. 11–12.

---

## 5b.3 [iut:Ind1_label_permutation] — label permutation

**Domain**: label sets S±_{j+1} that parametrize procession slots.

**Relation to LabCusp±**: S±_{j+1} arises via IUTchI Prop 6.9 (ii) from
the cusp-label classification LabCusp± (IUTchI Def 6.1-iii).
Permuting S±_{j+1} corresponds to permuting the label slots of Prc(n,◦D⊢_T).

**Role**: the étale-picture permutation symmetries (IUTchI Cor 6.10-iii;
IUTchII Cor 4.11-ii,iii) induce compatible poly-isomorphisms
```
Prc(n,◦D⊢_T) ~→ Prc(n′,◦D⊢_T);   n,◦R^LGP ~→ n′,◦R^LGP
```
Admitting label permutation indeterminacy is what allows `n,◦R^LGP` to
be "visible" from any vertical line n′ without a preferred label bijection.

> Source: IUTchIII Introduction p. 12; IUTchI Prop 6.9 (ii); Cor 6.10 (iii).

---

## 5b.4 [CLAIMED_BY: Mochizuki] Role at Cor 3.12

At Cor 3.12 Step (xi), the multiradial representation `n,◦R^LGP` — subject
to (Ind1),(Ind2),(Ind3) — is used to compare log-volumes of Θ-pilot and
q-pilot objects. (Ind1) contributes to the holomorphic hull: the log-volume
estimate is taken over the union of possible images of the Θ-pilot object
under the (Ind1) action (IUTchIII Introduction p. 16; Fig. I.8 p. 18).

Mochizuki's claim: (Ind1) is mild; blurring from D⊢-prime-strip Aut and
label permutation is controlled by the procession geometry, and does not
destroy `−|log(Θ)| ≥ −|log(q)|`.

Status: **[CLAIMED_BY: Mochizuki]**

---

## 5b.5 SS-side scope

pymupdf search of SS 2018 PDF (10 pages):

| Term | Hits | Location |
|---|---|---|
| "Ind 1" (space) | 1 | p. 9 — collective mention only |
| "D-prime-strip" / "procession" / "S±" / "label permut" | 0 | — |

SS p. 9 (verbatim):
> "up to certain indeterminacies, e.g. (Ind 1,2,3) (without which the
> conclusion would be obviously false)"

SS lists Ind1–3 collectively; the internal structure of Ind1 (D⊢-prime-strip
Aut or label permutation components) is not mentioned. SS's critique
targets Cor 3.12 as a whole via the j² monodromy argument (p. 10), not
the Ind1 mechanism.

Status: **[CLAIMED_BY: Mochizuki]**, **[OUT_OF_SCOPE: Scholze-Stix]**

---

## Sources

| Reference | Content |
|---|---|
| IUTchIII Thm 3.11 (i), p. 154 | Ind1 formal statement |
| IUTchIII Introduction p. 12 | two-component expansion |
| IUTchIII Introduction pp. 16–18 | role in Cor 3.12 log-volume estimate |
| IUTchI Prop 6.9 (ii) | procession construction |
| IUTchI Def 6.1 (iii) | LabCusp± definition |
| IUTchI Cor 6.10 (iii); IUTchII Cor 4.11 (ii),(iii) | étale-picture permutation symmetries |
| SS 2018 pp. 3, 9 | scope declaration; "(Ind 1,2,3)" mention |

- IUTchIII PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
- SS 2018 PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
