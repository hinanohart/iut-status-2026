# [iut:anabelian_geometry] — Scholze-Stix view

> ⚠️ This document is the **SS-side draft** (3-agent verify pending).
> Documents how the concept is *received* and *deployed* by Scholze-Stix in their 2018 critique. Does NOT translate the concept itself.

## How SS uses this concept

- SS cite Mochizuki's own theorem (Anab3, Theorem 1.9 / Corollary 1.10) as a starting point: the
  functor X ↦ π₁(X) is **fully faithful** on connected curves of strictly Belyi type over number
  fields and p-adic fields, with an explicit quasi-inverse.
  Reference: Scholze-Stix 2018, p. 5 (citing [Anab3])

- SS acknowledge étale-like data in the Hodge theater is "the abstract topological group π₁(X),
  considered as a group up to inner automorphism", or equivalently the abstract Galois category
  of finite étale covers.
  Reference: Scholze-Stix 2018, p. 5

- SS invoke Remark 8 to note the fully-faithful statement extends to morphisms Xₖᵥ → X when X
  lives over a number field k and kᵥ is a nonarchimedean localization.
  Reference: Scholze-Stix 2018, p. 5

- SS's central observation (Remark 9): in IUTT, the machinery operates in a regime where
  anabelian geometry *already holds* — i.e., geometry and group theory are provably equivalent
  by Mochizuki's own theorem — so working with fundamental groups adds no new isomorphisms
  beyond what comes from isomorphisms of schemes.
  Reference: Scholze-Stix 2018, p. 5

## Where SS agrees with Mochizuki

- Mochizuki's anabelian theorem itself (Theorem 7 in SS's note) is stated and accepted as correct.
- The theorem is "striking" (SS's word) and is the basis on which the IUTT structure is built.
- SS acknowledge that extra π₁-isomorphisms exist for Galois groups of p-adic fields (footnote 4),
  though they found this did not enter the discussion in a critical way.

## Where SS disagrees / sees no essential content

- "Anabelian geometry is supposed to be the key to Mochizuki's proof. However, here we see that
  in the IUTT papers, we are (for the essential part) in a situation where anabelian geometry holds
  true in the sense that geometry and group theory are equivalent."
  — Remark 9, p. 5

- "We could not find the point where it is essential to work with fundamental groups – there are
  no additional isomorphisms of fundamental groups that do not come from isomorphisms of schemes,
  precisely because of Mochizuki's theorem."
  — Remark 9, p. 5

- The Frobenius-like picture (π₁(X) acting on a monoid) is also shown to often reduce, via Kummer
  theory, to an equivalence of categories on the essential image of X ↦ (π₁(X) ↷ k×), leaving
  no room for extra group-theoretic freedom at the disputed step.
  Reference: Scholze-Stix 2018, pp. 5–6

- A Hodge theater reduces (up to equivalence of categories) to the choice of a once-punctured
  elliptic curve abstractly isomorphic to X: "choosing a Hodge theater is equivalent to choosing
  a once-punctured elliptic curve abstractly isomorphic to X."
  Reference: Scholze-Stix 2018, p. 6

## Critical caveat

- SS do **not** claim anabelian geometry is invalid or unimportant as a research field.
  Their claim is strictly scoped: *at the disputed step in Corollary 3.12*, the anabelian
  framework does not generate the extra degrees of freedom that the proof requires.
  The distinction is between "anabelian geometry is valid" (agreed) and "anabelian geometry
  plays an essential role at Cor. 3.12" (disputed by SS).

## Source

- Scholze-Stix 2018 PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
