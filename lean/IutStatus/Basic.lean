/-
IutStatus.Basic — top-level theorem stubs for IUT status index.

ALL theorem bodies are `sorry` and intentionally so. This file does not
prove anything about IUT. It encodes the *shape* of the claims in a
form that can be replaced by actual proofs once the LANA project
(2026-03-31, mid-report 2026-07-17) delivers formalized anabelian and
IUT machinery.

Reference:
- LANA: https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f
- Mochizuki, "On the Formalization of IUT" (2026-04):
  https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20(2026-04).pdf

Drift-zero contract:
- Theorem names match `iut:*` IRIs in `data/entities.json`.
- A consumer (LLM, human, or program) referring to `cor_3_12` here and
  to `iut:Cor.3.12` in JSON-LD refers to the same entity by construction.
-/

namespace IutStatus

/-- Anabelian geometry foundational axiom. Stub. -/
axiom anabelian_axiom : Prop

/-- Frobenioid structure. Stub. -/
structure Frobenioid : Type where
  carrier : Type

/-- Étale theta function. Stub. -/
opaque etaleTheta : Prop := True

/-- Θ±ellNF-Hodge theater. Stub. -/
structure HodgeTheater : Type where
  /-- placeholder field to be replaced by LANA. -/
  placeholder : Unit := ()

/-- θ-link (multiplicative link between Hodge theaters). Stub. -/
axiom theta_link : HodgeTheater → HodgeTheater → Prop

/-- log-link (additive link between Hodge theaters). Stub. -/
axiom log_link : HodgeTheater → HodgeTheater → Prop

/-- Multiradial algorithm. Stub. -/
axiom multiradial : Prop

/-- Indeterminacy Ind1 (étale-theoretic). Stub. -/
axiom Ind1 : Prop

/-- Indeterminacy Ind2 (Frobenius-theoretic). Stub. -/
axiom Ind2 : Prop

/-- Indeterminacy Ind3 (log-volume). Stub. -/
axiom Ind3 : Prop

/--
Corollary 3.12 (Mochizuki, IUTch-III).

This is the disputed step. Whether this Prop should be replaced by
something derivable from `multiradial`, `Ind1`, `Ind2`, `Ind3`
depends on:
  (a) the Mochizuki interpretation of un-entangling distinct copies, or
  (b) the Scholze-Stix interpretation that distinct-copy preservation
      reduces to a tautology.

Both interpretations are encoded in `data/claims.json`. The body
remains `sorry` until LANA or an equivalent project delivers a
mathlib4-formalized resolution.
-/
theorem cor_3_12 : Prop := by sorry

/-- Vojta-style height inequality. Stub. -/
theorem height_inequality : Prop := by sorry

/-- abc conjecture (Masser-Oesterlé 1985). Stub. -/
theorem abc_conjecture : Prop := by sorry

end IutStatus
