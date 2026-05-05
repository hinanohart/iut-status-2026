<!-- 3-agent verify pending -->

# [iut:anabelian_geometry] Anabelian Geometry (Mochizuki-side draft)

> ⚠️ This document is the **mochizuki-side draft**. The neutral merge in `docs/section_1_prerequisites.md` is the consumer-facing view.
> Last verified: 2026-05-06

## Definition (Mochizuki / RIMS)

- **Anabelian geometry** studies the extent to which algebraic varieties (especially hyperbolic curves) are determined by their étale fundamental groups, viewed as abstract topological groups devoid of auxiliary basepoint data.
- In the IUT context, the relevant discipline is **absolute anabelian geometry** (`iut:anabelian_geometry`): reconstruction of ring/scheme structure from the underlying abstract topological group of an étale fundamental group, with no reference to a fixed algebraic closure or geometric point.
- Reference: Mochizuki, "Inter-universal Teichmüller Theory I" (IUTchI), §I3, p. 21. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>

## Key properties (statement-level)

- **Tempered Anabelian Rigidity** (étale theta function version): Let γ : Π^tp_{X_α} →̃ Π^tp_{X_β} be an isomorphism of tempered fundamental groups of Tate curves over p-adic fields. Then γ maps the étale theta class O×_{K̈_α} · η̈^Θ_α to a Z-conjugate of O×_{K̈_β} · η̈^Θ_β, and preserves decomposition groups and canonical integral structures of cusps.
  - Reference: Mochizuki, "The Étale Theta Function and its Frobenioid-theoretic Manifestations" (EtTh), Theorem 1.6, pp. 22–23. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>

- **Constant Multiple Rigidity**: Under the hypotheses of Theorem 1.6, any γ preserves the property that η̈^{Θ,Z} is of standard type, up to a {±1}-indeterminacy; and γ preserves the standard sets of values of η̈^{Θ,Z}.
  - Reference: EtTh, Theorem 1.10, pp. 27–28.

- **Inter-universal aspect**: Because the Θ-link and log-link are not compatible with ring structure, étale fundamental groups on either side of such filters can only be related as abstract topological groups; the scheme-theoretic reconstruction possible from those abstract groups is precisely the content of absolute anabelian geometry.
  - Reference: IUTchI, §I3, pp. 21–22.

- **Reconstruction of number field from fundamental group**: The reconstruction of the number field F_mod from the étale fundamental group of C_K is cited as one of the key applications of the F^⋇_l-symmetry in IUTchI §5 (Example 5.1) and [IUTchII].
  - Reference: IUTchI, p. 8 (discussion of §I1 reconstruction remark); §I3, p. 21.

## Why this is a prerequisite for IUT

The `iut:anabelian_geometry` machinery provides the mechanism by which IUT "looks inside" one Hodge theater from another: by applying absolute anabelian geometry to the tempered and étale fundamental groups constituting a D-Θ^{±ell}NF-Hodge theater in the étale-picture, one obtains algorithmic descriptions of the conventional scheme theory of one theater in terms of another (IUTchI, §I3, p. 21; Theorem A). Without mono-anabelian reconstruction, the Θ-link and log-link would carry no geometric information across the ring-theoretic boundary they traverse.

## Forbidden translations

- Do NOT translate to: perfectoid spaces, diamonds, condensed mathematics.
- Why: Mochizuki's framework operates on abstract topological groups and categories, not on the ring-based or site-theoretic structures of Scholze–Stix geometry; conflating the two obscures the "inter-universal" (basepoint-varying) character that is definitional to IUT. (Cf. Mochizuki, "Mathematics of Mutually Alien Copies", Introduction, §1.)

## Source

- 主に: Mochizuki, "Inter-universal Teichmüller Theory I" (May 2020), §I3 (pp. 21–22), §I1. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>
- 補助: Mochizuki, "The Étale Theta Function and its Frobenioid-theoretic Manifestations" (Dec 2008, updated 2022), §1. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>
- survey: Yamashita, "A proof of the abc conjecture after Mochizuki" (2024), §§relating anabelian geometry. URL: <https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2024Jun25.pdf>
- Paper list: <https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html>
