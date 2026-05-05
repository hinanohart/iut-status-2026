<!-- 3-agent verify pending -->

# [iut:Frobenioid] Frobenioid (Mochizuki-side draft)

> ⚠️ This document is the **mochizuki-side draft**. The neutral merge in `docs/section_1_prerequisites.md` is the consumer-facing view.
> Last verified: 2026-05-06

## Definition (Mochizuki / RIMS)

- A **Frobenioid** (`iut:Frobenioid`) is a category C equipped with a functor C → F_Φ to an elementary Frobenioid F_Φ (built from a divisorial monoid Φ on a base category D and the multiplicative monoid N_{≥1} of positive integers) satisfying seven conditions (Definition 1.3) concerning: surjectivity to the base category via pull-back morphisms; surjectivity to N_{≥1} via Frobenius-type morphisms; surjectivity to the divisor monoid via co-angular morphisms; factorization of arbitrary morphisms; factorization of pre-steps; faithfulness up to units; and isotropic objects.
- The **elementary Frobenioid** F_Φ has objects = objects of D; a morphism φ : A → B is a triple (φ_D, Z_φ, n_φ) where φ_D is a morphism of D, Z_φ ∈ Φ(A_D) is the zero divisor, and n_φ ∈ N_{≥1} is the **Frobenius degree**. Composition: (ψ∘φ) = (ψ_D∘φ_D, φ_D*(Z_ψ) + n_ψ·Z_φ, n_ψ·n_φ).
- Reference: Mochizuki, "The Geometry of Frobenioids I: The General Theory" (FrdI), Definition 1.1 (iii) and Definition 1.3, pp. 19–24. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf>

## Key properties (statement-level)

- **Elementary Frobenioids are Frobenioids** (Proposition 1.5): F_Φ equipped with F_Φ → F_{Φ^{char}} is a Frobenioid of Aut-ample, End-ample, base-trivial, Frobenius-trivial, Frobenius-normalized, and isotropic type; there is a natural functorial isomorphism O^▷(A) →̃ Φ(A) for A ∈ Ob(F_Φ).
  - Reference: FrdI, Proposition 1.5, p. 27.

- **Factorization Theorem** (Definition 1.3, (iv)): Every morphism φ : A → B in a Frobenioid admits an essentially unique factorization φ = α∘β∘γ where α is a pull-back morphism, β is a pre-step, and γ is a morphism of Frobenius type.
  - Reference: FrdI, Definition 1.3(iv), p. 24.

- **Étale-like vs. Frobenius-like dichotomy**: The base category D (analogous to a Galois category; "order-indifferent") is fundamentally and category-theoretically distinguishable from the Frobenius portion F (built on N_{≥1}; "order-conscious"). This dichotomy is intrinsic, not an artifact of labeling.
  - Reference: FrdI, §I4, p. 9.

- **Frobenius endomorphism of a number field**: The category-theoretic framework of Frobenioids admits a "Frobenius endomorphism" for the Frobenioid associated to a number field — an object that has no counterpart in conventional scheme theory.
  - Reference: FrdI, Abstract and §I3, pp. 1, 7–8.

- **Category-theoretic reconstruction of C → F_Φ** (main theorem of §§3–4): Under suitable conditions, the functor C → F_Φ (projecting to the base and recording Frobenius degree and divisor) is reconstructible intrinsically from the abstract category C.
  - Reference: FrdI, §I1, pp. 2–3 (summary); §§3–4 (proofs).

## Why this is a prerequisite for IUT

The `iut:Frobenioid` structure constitutes the "Frobenius-like" backbone of every Hodge theater in IUT. In IUTchI, Theorem A states that a Θ^{±ell}NF-Hodge theater is "in essence, a system of Frobenioids" (p. 13). The Θ-link relates "certain Frobenioid-theoretic portions" of one Hodge theater to another in a way that is not compatible with ring/scheme structures (IUTchI, p. 1 abstract). The simple structure of Frobenioids — essentially monoids isomorphic to N or R_{≥0} — is precisely what makes these cross-theater gluings possible (IUTchI, p. 17).

## Forbidden translations

- Do NOT translate to: perfectoid spaces, diamonds, condensed mathematics.
- Why: Frobenioids are non-ring-based category-theoretic structures; translating them into perfectoid or condensed language would re-introduce the ring/scheme framework that IUT deliberately dismantles to enable the Θ-link. (Cf. Mochizuki, "Mathematics of Mutually Alien Copies", §1.)

## Source

- 主に: Mochizuki, "The Geometry of Frobenioids I: The General Theory" (June 2008, updated 2024-01-21), §I1–I4, §1 (Definitions 1.1–1.3), §3–4. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf>
- 補助: Mochizuki, "The Geometry of Frobenioids II: Poly-Frobenioids" (June 2008, updated 2019-02-10). URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf>
- IUT application: Mochizuki, IUTchI, Abstract and §I1–I3. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>
- survey: Yamashita, "A proof of the abc conjecture after Mochizuki" (2024). URL: <https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2024Jun25.pdf>
