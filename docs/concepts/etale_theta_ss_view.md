# [iut:etale_theta] — Scholze-Stix view

> ⚠️ This document is the **SS-side draft** (3-agent verify pending).
> Documents how the concept is *received* and *deployed* by Scholze-Stix in their 2018 critique. Does NOT translate the concept itself.

## How SS uses this concept

- SS do **not** use the term "étale theta function" or "étale theta" explicitly in the 2018
  document. The étale theta paper [EtTh] does not appear in their reference list.
  Reference: Scholze-Stix 2018, full text (absence confirmed by search)

- The theta-function values *do* appear, but through the lens of the concrete Θ-pilot object.
  SS describe the Θ-pilot object as "the collection of q_v^{j²} ∈ O_kv for j = 1,…,ℓ>
  (at bad places). Up to some 2ℓ-th roots of unity, these arise naturally as the values of a
  Θ-function at certain 2ℓ-torsion points."
  Reference: Scholze-Stix 2018, p. 8 (§2.1.8)

- The "ingenious algorithm" by which Mochizuki recovers q_v^{j²} from π₁(X) acting on a monoid
  of divisors on tempered coverings of X is acknowledged in a footnote (fn. 11): "There is an
  issue here that this is not one object but ℓ> many. This can be resolved in a number of ways,
  e.g. by passing to a 'diagonal' copy; or more concretely by forming averages."
  Reference: Scholze-Stix 2018, p. 8, footnote 11

- At p. 5, footnote 5, SS note: "There is one notable more interesting case related to the monoid
  of divisors on tempered coverings of X at places of bad reduction, by means of which Mochizuki
  encodes the Θ-function." This is the only explicit acknowledgment of the Θ-function mechanism.

- The q-pilot and Θ-pilot objects, once extracted as abstract F♯-prime strips, are the operands
  of the Θ-link. SS's critique focuses on what the Θ-link *does* to these objects, not on the
  Θ-function construction that produces them.
  Reference: Scholze-Stix 2018, §2.1.9, pp. 8–9

## Where SS agrees with Mochizuki

- The values q_v^{j²} as theta-function values at 2ℓ-torsion points are accepted as a correct
  construction within the Hodge theater.
- Mochizuki's algorithm to recover these values from group-theoretic data is called "ingenious"
  and is not challenged.
- The Θ-link definition (full poly-isomorphism between F♯_{Θ,1} and F♯_{q,2}) is accepted
  as a well-defined construction.

## Where SS disagrees / sees no essential content

- The étale theta machinery (in the sense of [EtTh]) is treated as a **black box** for producing
  the concrete Θ-pilot values. SS's disagreement concerns what happens *after* these values
  have been extracted and placed in abstract F♯-prime strips.

- Once placed in abstract strips, the q_v^{j²} are encoded as an element of ℝ = (⊕ᵥRᵥ)/D₀
  via the global realified Frobenioid. At this point, the full étale theta construction collapses
  to a real number: pilot_Θ ↦ (1/2ℓ)·(average of j²·deg(q_E)) when the j²-scaling is applied.

- The j²-scaling required to make the Θ-pilot encode the correct arithmetic degree introduces
  monodromy O(ℓ²) into the identification diagram. SS argue: "it is clear that this will result
  in the whole diagram having monodromy j², i.e. being inconsistent."
  Reference: Scholze-Stix 2018, p. 10

- In SS's framing, the non-trivial content of the étale theta function (the algorithmic recovery
  of q_v^{j²} from tempered fundamental group data) is not the locus of the claimed error. The
  error is downstream, in the identification of distinct copies of ℝ.

## Critical caveat

- The absence of "étale theta" as an explicit term in SS 2018 is **not** equivalent to dismissal.
  SS accept the theta-value construction and target the step *after* the values have been
  abstracted into F♯-prime strips. Their critique does not address whether the étale theta
  construction itself is correct or essential to the proof strategy in principle — only that
  once the values are in hand, the subsequent identification of real-number copies is inconsistent.

## Source

- Scholze-Stix 2018 PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
