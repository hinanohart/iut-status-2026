# Section 3: theta-link (`iut:theta_link`)

> 3-agent verified.
> Last verified: 2026-05-06.
> drift-zero IRI: `iut:theta_link`
> Per-side drafts: `docs/concepts/theta_link.md`, `docs/concepts/theta_link_ss_view.md`

## 3.1 Definition (statement-level consensus)

Both sides agree on the following formal statements; only their interpretation
is disputed (see 3.2 ff.).

- The Θ-link `†HT^Θ →^Θ ‡HT^Θ` is a **full poly-isomorphism** (the collection
  of all isomorphisms, no element distinguished) between prime-strips attached
  to two Θ-Hodge theaters. It is well-defined as such a poly-isomorphism on
  both readings.
  - Mochizuki formulation: `†F⊩_tht ~→ ‡F⊩_mod` between F⊩-prime-strips.
    Source: IUTchI Cor. 3.7 (i), p. 88 (DOI 10.4171/PRIMS/57-1-1).
  - SS quotation: "the (full poly-)isomorphism between the F⊩×µ-prime strip
    F⊩×µ_Θ,1 ... and the F⊩×µ-prime strip F⊩×µ_q,2." (SS §2.1.9, p. 9).
  - Source layering (non-disputed): the F⊩×µ-version is the IUTchII
    Cor. 4.10 (iii) / Def. 4.9 (vii) refinement of the F⊩-version of
    IUTchI Cor. 3.7; SS works at the F⊩×µ layer.

- The domain prime-strip is built from the theta-pilot data (Frobenioid-theoretic
  `Θ_v ~ (q^{j²}_v)_{j=1,...,ℓ*}` at `v ∈ V^bad`); the codomain from the
  q-pilot data (2ℓ-th roots of `q_v`).
  - Sources: IUTchI Def. 3.6, Cor. 3.7 (i); SS §2.1.9, p. 9 (q̃_v / Θ_v).

- **Cor. 3.7 (ii)–(iii) preserved data.** The link induces full poly-isos
  `†D⊢_v ~→ ‡D⊢_v` (base / étale-like, horizontally coric) and lifts to
  `O×_{†C⊢_v} ~→ O×_{‡C⊢_v}` (units). Value-group data is **not** preserved
  in the strict pre-link normalisation; it is dilated.
  - Source: IUTchI Cor. 3.7 (ii)–(iii), p. 88–89.
  - SS does not contest this statement; SS p. 9 explicitly notes the link
    "forgets about the concrete embeddings" of `q̃_v`, `Θ_v` into `o_{k̄_v}`.

- **F⊩×µ-prime-strip data has the form `G_v ⟲ o^{×µ}_{k̄_v} × N`** at finite
  places.
  - Source (statement only): SS §2.1.9, p. 9; consistent with IUTchII
    Def. 4.9 (vii).

## 3.2 [DISPUTED] Triviality of the Θ-link as renaming

- **Mochizuki position.** The Θ-link transports non-trivial arithmetic
  content because the two Hodge theaters carry **mutually alien** ring-theoretic
  structures; the multiplicative comparison `{q^{j²}_v} ↔ q_v` across alien
  copies is the core mechanism. "Walls / filters … separate two 'mutually
  alien' copies of conventional scheme theory."
  Source: "Mathematics of Mutually Alien Copies" §3.3 (ii), pp. 60–62;
  IUTchI §I4, pp. 26–27.

- **Scholze–Stix position** (encoded as `claim:scholze_stix_2018_main`).
  After canonical identification of the abstract F⊩×µ-prime-strip data on
  both sides, the link reduces to a renaming of the generator of `N`:
  > "the F⊩×µ-prime strips are given by data of the form `G_v ⟲ o^{×µ}_{k̄_v} × N`
  > on both sides … this data is canonically the same on both sides … It is
  > simply the name of the generator of the monoid `N` that appears that is
  > called Θ respectively q." (SS §2.1.9, p. 9)
  Footnote 12, p. 9: with these identifications, IUTT-III Theorem 3.11
  "does not become false, but trivial."

- **Neutral remark.** The disagreement is not over whether the poly-isomorphism
  exists (both agree) but over whether the abstract / concrete distinction at
  the prime-strip level carries non-trivial transport of arithmetic
  information. See `claim:mochizuki_2018_response` for Mochizuki's reply
  that the canonical identification SS uses is itself the step where the
  inter-universal content is dropped.

## 3.3 [DISPUTED] Empty inequality

- **SS position.** With the consistent canonical identifications
  `R⊙,Θ ≅ R⊙,q ≅ R` (via `γ_can`, from canonical triviality of the global
  realified Frobenioids attached to F⊩×µ-prime strips), one must "omit the
  scalars `j²` that appear, which leads to an **empty inequality**."
  Source: SS §2.2, p. 10.

- **Mochizuki position.** The deletion of the `j²` scalars is precisely the
  illegitimate identification that the "alien copies" framework forbids;
  the inequality is non-empty when the two arithmetic-holomorphic structures
  are kept distinct, which is the explicit setup of the Frobenius-picture.
  Source: IUTchI §I4, pp. 26–27; IUTchIII Rem. 1.4.1 (i); "Alien Copies"
  §3.3 (ii).

- **Neutral remark.** This is the substantive disagreement; 3.2 and 3.3 are
  the same dispute viewed first at the strip level (3.2) and then at the
  inequality level (3.3).

## 3.4 [CLAIMED_BY: Mochizuki] Inter-universal motivation

The framing of the Θ-link as the wall between mutually alien copies of
conventional scheme theory — and the identification of multiplication / addition
with the two combinatorial dimensions of a ring, hence with Θ-link / log-link —
is asserted by Mochizuki as an integral part of the construction.
SS does not deny that this is Mochizuki's stated motivation; SS denies that
the formal F⊩×µ-data records the distinction. The motivational claim itself
is therefore listed here as `[CLAIMED_BY: Mochizuki]` rather than disputed.

- Source: IUTchI §I4, pp. 26–27; "Alien Copies" §1.3 / Abstract; §3.3 (ii).

## 3.5 [CLAIMED_BY: Mochizuki] Non-commutativity with the log-link

The horizontal Θ-link and vertical log-link generate the log-theta-lattice
and **do not commute**, mirroring the Witt-vector / Frobenius intertwining
of p-adic Teichmüller theory. The Frobenius-picture chain
`... →^Θ nHT^Θ →^Θ (n+1)HT^Θ →^Θ ...` admits Z-translation symmetry but no
adjacent-index swap.

- Source: IUTchI §I4, p. 27; IUTchI Cor. 3.8, p. 89; IUTchIII Rem. 1.4.1 (i).
- SS does not address this structural claim at the prime-strip level
  (no contradicting passage was located in SS 2018); recorded here as a
  Mochizuki-side claim rather than as disputed.

## 3.6 Forbidden translations

Do NOT render the Θ-link, "alien copies," or the multiplicative comparison as:

- morphisms of perfectoid spaces or diamonds,
- maps of condensed modules,
- prismatic Frobenius lifts,
- any ring/scheme morphism (the link is multiplicative-monoid-only;
  additive structure is deliberately deactivated across it).

No such correspondence is established in IUTchI–IV, IUTchII Cor. 4.10,
"Alien Copies," or SS 2018.

## Cross-reference

- entities.json: `iut:theta_link`, `iut:HodgeTheater`,
  `iut:F_modulus_prime_strip`, `iut:log_link`
- claims.json: `claim:scholze_stix_2018_main`,
  `claim:mochizuki_2018_response`

## Verification log

- 3.1 Θ-link is a full poly-isomorphism of prime strips: 3/3 ✅
  (IUTchI Cor. 3.7-i p. 88; SS §2.1.9 p. 9)
- 3.1 F⊩ vs F⊩×µ source layering note: 3/3 ✅
  (IUTchI Cor. 3.7-i; IUTchII Cor. 4.10-iii / Def. 4.9-vii)
- 3.1 Cor. 3.7 (ii)–(iii) preserved data (D⊢, O×): 3/3 ✅
- 3.1 F⊩×µ-strip shape `G_v ⟲ o^{×µ}_{k̄_v} × N`: 3/3 ✅
  (statement only; interpretation disputed in 3.2)
- 3.2 Θ-link triviality (renaming vs essential): 0/3 [DISPUTED]
- 3.3 empty inequality after canonical identification: 0/3 [DISPUTED]
- 3.4 inter-universal motivation: 1/3 [CLAIMED_BY: Mochizuki]
- 3.5 non-commutativity with log-link: 1/3 [CLAIMED_BY: Mochizuki]
- 3.6 forbidden translations (perfectoid / condensed / prismatic): 3/3 ✅
  (no source establishes such correspondence on either side)
