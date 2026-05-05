# [iut:Frobenioid] — Scholze-Stix view

> ⚠️ This document is the **SS-side draft** (3-agent verify pending).
> Documents how the concept is *received* and *deployed* by Scholze-Stix in their 2018 critique. Does NOT translate the concept itself.

## How SS uses this concept

- SS acknowledge the general Frobenioid as "the difficult notion" introduced in [Frd1], [Frd2], but
  focus exclusively on the **global realified Frobenioid**, which they show is elementary.
  Reference: Scholze-Stix 2018, p. 7

- A global realified Frobenioid (in the sense relevant to the proof) is: a collection of ordered
  1-dimensional ℝ-vector spaces Rᵥ parametrized by the places v of k, together with a codimension-1
  subspace D₀ ⊂ ⊕ᵥRᵥ defined by the kernel of the map sending 1 ↦ log(N(v)) at finite places
  and ↦ 2 at infinite places.
  Reference: Scholze-Stix 2018, p. 7

- SS derive: "the category of global realified Frobenioids is equivalent to the category of ordered
  1-dimensional ℝ-vector spaces."
  Reference: Scholze-Stix 2018, p. 7

- The global realified Frobenioid of an F♯-prime strip is always **canonically trivialized** via
  the normalization that maps log(N(v)) to the canonical element. Under this trivialization the
  pilot element maps to (1/2ℓ)·deg(q_E).
  Reference: Scholze-Stix 2018, pp. 8, 10

- In the key diagram drawn in Kyoto (p. 10), both the Θ-side and the q-side produce global
  realified Frobenioids that are "always canonically trivial using the various θ_can". SS use
  this canonical trivialization to anchor the comparison of arithmetic degrees.
  Reference: Scholze-Stix 2018, p. 10

## Where SS agrees with Mochizuki

- The construction of global realified Frobenioids from F♯-prime strips is accepted as correct
  and is used directly in SS's own reformulation (§2.1.4–§2.1.5).
- The forgetful functor from F♯-prime strips to global realified Frobenioids is accepted as
  well-defined and the category equivalence is not disputed.
- The canonical element θ_can ∈ ℝ and the normalization map are accepted as correct.

## Where SS disagrees / sees no essential content

- "Mochizuki introduces the difficult notion of a Frobenioid in his papers [Frd1], [Frd2].
  However, the notion of a global realified Frobenioid is very elementary."
  — p. 7

- The full generality of Frobenioid theory ([Frd1], [Frd2]) does not appear to contribute
  additional content at the disputed step: the only Frobenioid structure that matters reduces
  to an ordered 1-dimensional ℝ-vector space.

- The core problem SS identify concerns the **identification of copies of ℝ** across the
  Θ-link. With consistent identifications (using canonical triviality of both global realified
  Frobenioids), the j²-scalars necessary for the non-trivial inequality disappear, yielding
  0 ≤ d(P), which is vacuous.
  Reference: Scholze-Stix 2018, p. 10

- "The conclusion of this discussion is that with consistent identifications of copies of real
  numbers, one must in (1.5) omit the scalars j² that appear, which leads to an empty inequality."
  — p. 10

- Mochizuki's response (that "blurring" from indeterminacies rescues the inequality) is assessed
  by SS as implying a blurring of at least O(ℓ²), which renders the resulting inequality useless
  for the intended application.
  Reference: Scholze-Stix 2018, p. 10

## Critical caveat

- SS do **not** dispute Frobenioid theory as a mathematical framework. Their objection is that
  at the specific step of Corollary 3.12, the global realified Frobenioid collapses to a trivial
  ordered ℝ-vector space, so the elaborate machinery of [Frd1]/[Frd2] is not doing work at the
  disputed inequality.

## Source

- Scholze-Stix 2018 PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
