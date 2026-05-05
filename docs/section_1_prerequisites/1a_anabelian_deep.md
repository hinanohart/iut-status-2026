# 1a — Anabelian Geometry (Mochizuki framework, deep dive)

> 3-agent verify pending (mochizuki-side draft).
> Last verified: 2026-05-06.
> Parent: docs/section_1_prerequisites/README.md (created later)
> drift-zero IRIs: iut:anabelian.absolute_anabelian, iut:anabelian.tempered_rigidity,
>   iut:anabelian.cuspidalization, iut:anabelian.mono_anabelian,
>   iut:anabelian.belyi_cuspidalization
> PDF-verified sources: RIMS kurims.kyoto-u.ac.jp, pymupdf direct extraction 2026-05-06.

---

## 1a.1 Absolute anabelian framework (`iut:anabelian.absolute_anabelian`)

### Statement

- **Paper**: Mochizuki, *Topics in Absolute Anabelian Geometry I: Generalities* (March 2012).
- **URL**: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20I.pdf>
- **Location**: Introduction pp. 2–3.
- **Verbatim short statement** (≤200 chars):
  > "algorithms which are 'group-theoretic' in the sense that they are phrased in language that only depends on the structure of the input data as a profinite group"
- `verbatim_sha256_prefix`: `9f215511bee84cb7`

### Key content (paraphrase, not synthesis)

Mochizuki distinguishes three stages of anabelian geometry: (1) *relative* — using the augmentation `ΠX ↠ Gk`; (2) *semi-absolute* — using only `Ker(ΠX ↠ Gk)`; (3) *absolute* — using only `ΠX` as an abstract profinite group. The "Topics in Absolute Anabelian" series shifts focus from fully-faithfulness results of the form "X ↦ π₁(X) is fully faithful" to algorithmic results of the form "some scheme-theoretic construction may be expressed as a group-theoretic algorithm." The input is an abstract profinite group that "just happens to arise" as an étale fundamental group; the algorithm reconstructs objects reminiscent of scheme theory without ever returning to scheme-theoretic morphisms.

### Key theorems cited

- **Theorem 2.6** (Field types and group-theoreticity): for an extension `1 → Δ → Π → G → 1` of AFG-type with `k` a FF, MLF, or NF, the natural surjection `Π ↠ G` (hence the kernel `Δ`) can be characterised group-theoretically by `θ¹`, `θ²`, `ζ` invariants (Topics I, Theorem 2.6, pp. 21–22).
- **Theorem 4.7** (Semi-absoluteness of chains of elementary operations): under rel-isom-DGC, the functor Chain(X̃/X) → Chain(Πi) is an equivalence of categories (Topics I, Theorem 4.7, p. 56).

---

## 1a.2 Tempered anabelian rigidity (`iut:anabelian.tempered_rigidity`)

### Statement (EtTh Theorem 1.6)

- **Paper**: Mochizuki, *The Étale Theta Function and its Frobenioid-theoretic Manifestations* (Dec 2008, updated 2022).
- **URL**: <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>
- **Location**: Theorem 1.6, pp. 22–23.
- **Verbatim short statement** (≤200 chars):
  > "γ maps the étale theta class O×_{K̈_α}·η̈^Θ_α to a Z-conjugate of O×_{K̈_β}·η̈^Θ_β, and preserves decomposition groups and canonical integral structures of cusps"
- `verbatim_sha256_prefix`: `6f16c30429a19aaf`

### Key content (paraphrase)

Let `γ : Π^tp_{X_α} →̃ Π^tp_{X_β}` be an isomorphism of tempered fundamental groups of Tate curves over p-adic fields. Then `γ` maps the étale theta class to a `ℤ`-conjugate, and preserves decomposition groups of cusps and canonical integral structures. The companion result **Theorem 1.10** asserts constant-multiple rigidity: under the same hypotheses, `γ` preserves the standard sets of values of `η̈^{Θ,ℤ}` up to `{±1}`-indeterminacy (EtTh Theorem 1.10, pp. 27–28).

### Note

This theorem is recorded in `docs/section_1_prerequisites.md` §1.1 as `[CLAIMED_BY: Mochizuki]` because SS neither quote nor refute it; their critique is downstream of theta-value extraction.

---

## 1a.3 Absolute anabelian cuspidalization (`iut:anabelian.cuspidalization`)

### Statement (Cusp. Theorem 1.16)

- **Paper**: Mochizuki, *Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves* (June 2007).
- **URL**: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf>
- **Location**: Abstract; Theorem 1.16 (Reconstruction of Maximal Cuspidally Abelian Quotients), p. 25.
- **Verbatim short statement** (≤200 chars):
  > "the ultimate goal of this theory is the group-theoretic reconstruction of the etale fundamental group of an arbitrary open subscheme of the curve from the etale fundamental"
  > [truncated at 172 chars; full abstract: "…group of the full proper curve"]
- `verbatim_sha256_prefix`: `46c6bfdf983a8074`

### Key content (paraphrase)

Given a proper hyperbolic curve `X` over a finite or nonarchimedean local field with étale fundamental group `ΠX`, and an isomorphism `α : ΠX →̃ ΠY`, Theorem 1.16 establishes: (i) `α` preserves field type, type `(g,r)`, decomposition groups of cusps; (ii) `α` is compatible with the natural quotients to absolute Galois groups; (iii) when `X, Y` are proper, `α` induces a compatible isomorphism of the maximal cuspidally abelian quotients `Π^{c-ab}_{UX×X} →̃ Π^{c-ab}_{UY×Y}`, well-defined up to cuspidally inner automorphisms. This provides the tool for passing from the abstract fundamental group of the proper curve to the fundamental groups of open sub-curves.

---

## 1a.4 Mono-anabelian reconstruction (`iut:anabelian.mono_anabelian`)

### Statement (Topics III §I2 definition + Theorem 1.9)

- **Paper**: Mochizuki, *Topics in Absolute Anabelian Geometry III: Global Reconstruction Algorithms* (November 2015).
- **URL**: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20III.pdf>
- **Location**: Introduction §I1 p. 2; §I2 p. 7 (definition); Theorem 1.9, pp. 36–38.
- **Verbatim short statement** (≤200 chars):
  > "such a group-theoretic geometric framework is precisely what is furnished by the enhancement of absolute anabelian geometry — which we shall refer to as mono-anabelian geometry"
- `verbatim_sha256_prefix`: `ae1407a2aabf3a00`

### Key content (paraphrase)

Mochizuki defines **mono-anabelian** reconstruction as an algorithm whose input is a single abstract arithmetic fundamental group (not a pair of groups equipped with an isomorphism). This is strictly stronger than **bi-anabelian** (= "preserved by an isomorphism of fundamental groups"): mono-anabelian ⟹ bi-anabelian, but the converse is asserted to be false in the context relevant to IUT (Topics III, §I2, p. 7; Corollaries 3.6, 3.7).

**Theorem 1.9** (Topics III, pp. 36–38) gives the central mono-anabelian result: for a hyperbolic orbicurve `X` of strictly Belyi type over a sub-p-adic field, there exists a functorial group-theoretic algorithm — using only `1 → ΔX → ΠX → Gk → 1` as a profinite group extension — that reconstructs the NF-portion of the function field of `X`. Steps: (a) Belyi cuspidalization to construct `ΠU`; (b–d) cyclotomic isomorphisms and Kummer classes; (e) reconstruction of `k^×_NF` and the NF-rational functions. **Corollary 1.10** extends this to MLFs by adding reconstruction of the natural isomorphism `H²(Gk, μℤ(Gk)) →̃ ℤ`.

The **mono-anabelian** framework is critical for IUT because the Θ-link and log-link do not respect ring structures. A framework that remains "neutral" with respect to taking logarithms — i.e., immune to dismantling the `⊞/⊠` two-dimensional ring structure — is required to make the multiradial algorithm (`iut:multiradial_algorithm`) functorial. The bi-anabelian approach fails log-Frobenius compatibility (Topics III, Corollary 3.7); the mono-anabelian approach succeeds (Corollary 3.6).

---

## 1a.5 Belyi-style cuspidalization (`iut:anabelian.belyi_cuspidalization`)

### Statement (Cusp. Corollary 2.13)

- **Paper**: Mochizuki, *Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves* (June 2007).
- **URL**: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf>
- **Location**: Definition 2.9 (Belyi type, p. 43); Corollary 2.13 (Absoluteness of Curves of Belyi Type, p. 49).
- **Verbatim short statement** (≤200 chars):
  > "every hyperbolic curve of Belyi type over a nonarchimedean local field is absolute"
- `verbatim_sha256_prefix`: `a01944bedb7c5ca5`

### Key content (paraphrase)

A hyperbolic curve `U` over a nonarchimedean local field is **of Belyi type** if it is defined over a number field and admits a finite étale cover by a genus-zero curve (Definition 2.9). The **absolute p-adic Grothendieck Conjecture for Belyi-type curves** (Corollary 2.12, p. 48–49) states: for `U, V` hyperbolic curves over nonarchimedean local fields, any isomorphism `ΠU →̃ ΠV` satisfying conditions (a) quasi-Belyi and (b) one of the two is Belyi arises from a unique isomorphism of schemes. Corollary 2.13 draws the "absoluteness" consequence.

The technique underlying this result is Belyi cuspidalization: the existence of a Belyi map (defined over a number field, mapping to a tripod) allows propagation of the pro-l cuspidalization (`ΠUX→ Π_US^{≤∞}`) constructed in Theorem 3.10. This Belyi cuspidalization technique is also the "non-elementary ingredient" of the mono-anabelian algorithm of Topics III, Theorem 1.9 (Topics III, p. 48).

---

## How these support `iut:Cor.3.12`

Mochizuki's position (IUTchI §I3, pp. 21–22) is that anabelian geometry provides the mechanism by which IUT "looks inside" one Hodge theater from another. The specific chain is: (1) mono-anabelian reconstruction (`iut:anabelian.mono_anabelian`) furnishes a ring/field structure from an abstract fundamental group; (2) tempered rigidity (`iut:anabelian.tempered_rigidity`) rigidifies the étale theta class across the Θ-link; (3) cuspidalization (`iut:anabelian.cuspidalization`) and Belyi cuspidalization (`iut:anabelian.belyi_cuspidalization`) are prerequisite techniques for Theorem 1.9 and for encoding the Θ-values in the mono-theta environment. Without the mono-anabelian framework, the log-link and Θ-link would have no geometric content: applying logarithms would dismantle the ring structure with no way to reconstruct it group-theoretically. The absolute anabelian framework (`iut:anabelian.absolute_anabelian`) is the foundational algorithmic stance that makes all five concepts coherent as "software" rather than "fully-faithfulness theorems." All five concepts are `[CLAIMED_BY: Mochizuki]` in `docs/section_1_prerequisites.md` §1.1 (not refuted by SS; SS's critique operates downstream at `iut:Cor.3.12`).

---

## Forbidden translations

- Do NOT translate these concepts into perfectoid spaces, diamonds, or condensed mathematics.
- Do NOT assert that "mono-anabelian = absolute anabelian"; they are distinct (the latter is a sub-concept of the former: Topics III defines "mono-anabelian" explicitly as an enhancement of absolute anabelian geometry).
- Do NOT describe `iut:anabelian.belyi_cuspidalization` as a global result; it concerns nonarchimedean local fields specifically.

---

## Source

| Concept IRI | Primary paper | Section / Theorem | URL |
|---|---|---|---|
| `iut:anabelian.absolute_anabelian` | Topics in Absolute Anabelian I | Intro pp. 2–3; Thm 2.6 | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20I.pdf> |
| `iut:anabelian.tempered_rigidity` | EtTh | Thm 1.6, pp. 22–23; Thm 1.10, pp. 27–28 | <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf> |
| `iut:anabelian.cuspidalization` | Cuspidalizations 2007 | Abstract; Thm 1.16, p. 25 | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf> |
| `iut:anabelian.mono_anabelian` | Topics in Absolute Anabelian III | §I1–I2 pp. 2, 7; Thm 1.9 pp. 36–38; Cor 1.10 pp. 41–44; Cor 3.6 pp. 78–79 | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20III.pdf> |
| `iut:anabelian.belyi_cuspidalization` | Cuspidalizations 2007 | Def 2.9 p. 43; Cor 2.12–2.13 pp. 48–49; Thm 3.10 pp. 73–74 | <https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf> |
| background (mono-anabelian enhancement) | Topics in Absolute Anabelian III | Intro §I4, §I5 | same as above |
