# Section 2: Hodge Theater (`iut:HodgeTheater`)

> 3-agent verified (mochizuki-side / SS-side / neutral merger).
> Last verified: 2026-05-06.
> drift-zero IRI: `iut:HodgeTheater`
> Source-of-truth contract: see `LLM_CONTEXT.md` §3 (4-block template).
> Per-side drafts (NOT consumer-facing): `docs/concepts/hodge_theater.md`, `docs/concepts/hodge_theater_ss_view.md`.

This document records the 3-agent merge of mochizuki-side and SS-side drafts of the entity `iut:HodgeTheater`. **Definitional / theorem-statement consensus** is recorded as plain bullets. **Interpretive disputes** (whether distinct Hodge theaters carry essential extra information, whether the Θ-link is non-trivial, whether the `j²` monodromy objection holds) are recorded as `[DISPUTED]` with both positions quoted. Single-side claims are flagged `[CLAIMED_BY: …]`. Empty bullets are not invented.

---

## 2.1 Definition (`iut:HodgeTheater`) — statement-level consensus

- A **Θ±ellNF-Hodge theater** `†HT^{Θ±ellNF}` (relative to fixed initial Θ-data) is a triple consisting of:
  (a) a Θ±ell-Hodge theater `†HT^{Θ±ell}`,
  (b) a ΘNF-Hodge theater `†HT^{ΘNF}`,
  (c) the (necessarily unique) gluing isomorphism between them.
  - Mochizuki side: IUTchI, Definition 6.13, (i), p. 182. DOI [10.4171/PRIMS/57-1-1](https://doi.org/10.4171/PRIMS/57-1-1). URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>
  - SS side: refers to "(Θ±ellNF-)Hodge theater" as the data-bundle of [IUTT-1, Cor 6.12(i), Prop 6.6(iii), Cor 5.6(ii), Prop 4.8(ii), Def 6.13]. (Scholze-Stix 2018, p. 6.)
- The Θ±ellNF-Hodge theater is constructed from initial Θ-data `(F/F, X_F, l, C_K, V, V^{bad}_{mod}, ε)` (elliptic curve `E_F`, prime `l ≥ 5`, valuation set `V`, bad-reduction locus): IUTchI Def 3.1, p. 61.
- Components (statement-level, both sides quote or rely on the same Mochizuki definitions):
  - **Θ-Hodge theater** (additive + multiplicative gluing absent): collection `({†F_v}_{v∈V}, †F^⊩_{mod})`, with a Frobenioid `†F_v ≃ F_v` at `v ∈ V^{non}`, a Kummer-structured datum at `v ∈ V^{arc}`, and a global Frobenioid over `F_{mod}` encoding `q`-parameters and theta values. (IUTchI Def 3.6, pp. 87–88.)
  - **Θ±ell-Hodge theater** (additive component): tracks the geometric `F^{⊛±}_l`-symmetry on labels `(-l* < … < 0 < … < l*) ≅ F_l`, each label a D-prime-strip; global portion = Galois category of finite étale coverings of `X_K`. (IUTchI Defs. 6.4, (iii); 6.11, (iii).)
  - **ΘNF-Hodge theater** (multiplicative component): tracks the arithmetic `F^*_l`-symmetry on labels `(1 < … < l*) ≅ F^*_l`, each a D-prime-strip; global portion = Galois category of coverings of `C_K`. (IUTchI Defs. 4.6, (iii); 5.5, (iii).)
- **Étale-like data inside a Hodge theater** is the abstract topological group `π₁(X)` up to inner automorphism (= abstract Galois category of finite étale covers of `X`).
  - Mochizuki side: consistent with IUTchI §I3, p. 21.
  - SS side: explicit at Scholze-Stix 2018, p. 5.
- **Frobenius-like data** is `π₁(X)` acting on a monoid (e.g. `O^×_{k̄_v}`); often categorically equivalent to a hyperbolic-curves category.
  - SS side: Scholze-Stix 2018, pp. 5–6 ("but not always").
  - Mochizuki side: not contradicted; the étale-like / Frobenius-like dichotomy is intrinsic at the categorical level (FrdI §I4; cf. Section 1.2 of this repository).

## 2.2 Log-shell and log-volume (statement-level consensus, mochizuki-side draft only — SS not quoting these definitions)

- **Log-shell**: at non-archimedean `v`, the compact additive module `I_v := p_v^{-1} · log_v(O^×_{K_v}) ⊆ K_v`. It satisfies `O^▷_{K_v} ⊆ I_v` and `log_v(O^×_{K_v}) ⊆ I_v`, so it contains Kummer images from both sides of any log-link. Archimedean analogue defined via the complex logarithm. (IUTchIII Def. 1.1, (i)–(iii); AbsTopIII Def 5.4, (v); IUTchIII Introduction p. 4. DOI [10.4171/PRIMS/57-3-1](https://doi.org/10.4171/PRIMS/57-3-1).)
- **Log-volume integration**: real-valued measure on log-shells; compatibility of the log-link with log-volumes (IUTchIII Prop. 1.2, (iii)) is what converts the log-Kummer correspondences into the global bound `−|log(Θ)| ≥ −|log(q)|` of Cor. 3.12.
- **[CLAIMED_BY: Mochizuki]** at the level of textual quotation: SS do not separately quote the log-shell / log-volume definitions; their critique addresses the diagram in IUTchIII Cor 3.12 directly via ordered 1-D `ℝ`-vector spaces (Scholze-Stix 2018, p. 10) without invoking the `I_v` machinery by name. The constructions themselves are not contested; they are simply outside the scope SS chose to quote.

## 2.3 [DISPUTED] Are distinct Hodge theaters genuinely distinct?

- **Mochizuki position** (`claim:mochizuki_2012_proves_abc`, `claim:mochizuki_2018_response`):
  - Each Θ±ellNF-Hodge theater is the fundamental "unit cell" of IUT; the Θ-link (horizontal) connects the theta-value data of one theater to the `q`-parameter data of the next *in a ring-structure-incompatible way*, creating an "alien arithmetic holomorphic structure" whose comparison is the core problem (IUTchI §I1; Cor 3.7, (i); Cor 3.8). The distinct copies are not redundant: they are precisely what makes the Θ-link carry non-trivial information.
  - Source: Mochizuki, IUTchI, Cors. 3.7–3.8; Theorem A.
- **Scholze-Stix position** (`claim:scholze_stix_2018_sub_1`):
  - Deriving from Mochizuki's own results [IUTT-1, Cor 6.12(i), Prop 6.6(iii), Cor 5.6(ii), Prop 4.8(ii), Def 6.13], SS argue that the functor from the single-object category `{X}` to Θ±ellNF-Hodge theaters is an *equivalence of categories*. (Scholze-Stix 2018, p. 6.)
  - Consequence: "choosing a Hodge theater is equivalent to choosing a once-punctured elliptic curve abstractly isomorphic to `X`." The equivalence is constructive. (Scholze-Stix 2018, p. 6.)
  - "Mochizuki was not able to convince us during the week why such a simplification was not allowed." (Scholze-Stix 2018, p. 4, excuse (3).)
- **Neutral remark**: SS do **not** redefine the Hodge theater; they derive a categorical equivalence from Mochizuki's own cited results and conclude that the distinct copies carry no information not already in `X`. Mochizuki maintains that the distinct copies are the seat of an *alien* ring structure not visible from the abstract single-object category `{X}`. The dispute is scoped strictly to whether the distinct copies generate extra degrees of freedom needed at `iut:Cor.3.12`. Encoded as `claim:scholze_stix_2018_sub_1`.

## 2.4 [DISPUTED] Θ-link triviality between two Hodge theaters

- **Mochizuki position** (`claim:mochizuki_2012_proves_abc`):
  - The Θ-link is a full poly-isomorphism `†F^⊩_{tht} →^∼ ‡F^⊩_{mod}` between the relevant Frobenioid-theoretic portions of two distinct Hodge theaters; its non-compatibility with ring structures is what generates the Frobenius-picture (chain) and the étale-picture (`D^⊢_>`-coric hub). (IUTchI Cor. 3.7, (i); Cor. 3.8, pp. 11–15.)
  - The "inter-universal" character is essential: the comparison cannot be reduced to a single ambient ring/scheme.
- **Scholze-Stix position** (`claim:scholze_stix_2018_sub_1`):
  - Under SS's analysis of the Θ-link between `HT₁` and `HT₂`, the `F^⊩×µ`-prime strips on both sides are "data of the form `Gv ↷ o^×µ_{k̄_v} × N` … canonically the same on both sides. It is simply the name of the generator … that is called `Θ` respectively `q`." (Scholze-Stix 2018, p. 9.)
  - On full poly-isomorphisms specifically: SS spent "a lot of time" on this point; "Mochizuki was not able to explain this convincingly in our opinion." (Scholze-Stix 2018, p. 7, fn. 8.)
- **Neutral remark**: SS do not deny the Θ-link is *defined*; their claim is that with consistent identifications the two sides are canonically the same datum with a renamed generator. Mochizuki maintains the renaming is not innocuous because the two sides are housed in incompatible ring structures. The two positions describe the same construction (the Θ-link) but disagree on whether identifying the two copies introduces or destroys content. Encoded as `claim:scholze_stix_2018_sub_1`.

## 2.5 [DISPUTED] Monodromy `j²` inconsistency at `iut:Cor.3.12`

- **Mochizuki position** (`claim:mochizuki_2018_response`):
  - The `j²` factors are intrinsic to the theta-pilot data and are preserved across the Θ-link by the rigidity properties of the étale theta function and mono-theta environment (cyclotomic, discrete, constant-multiple rigidity; EtTh §1, Cors. 2.18–2.19). Apparent ambiguities are absorbed by the prescribed `(Ind1)–(Ind3)` indeterminacies of IUTchIII §3, not by collapsing the `j²` structure.
  - Source: Mochizuki, IUTchIII, §3; EtTh, Introduction.
- **Scholze-Stix position** (`claim:scholze_stix_2018_sub_2`, `claim:scholze_stix_2018_sub_3`):
  - Tracing all ordered 1-dimensional `ℝ`-vector spaces in [IUTT-3, Cor. 3.12], SS conclude that introducing `j²` scalars on the Θ-side makes the commutative diagram exhibit "monodromy `j²`, i.e. being inconsistent." With consistent identifications the `j²` factors must be dropped, yielding an empty inequality (effectively `0 ≤ d(P)`). (Scholze-Stix 2018, pp. 4, 10.)
- **Neutral remark**: This is the central technical dispute of the entire IUT controversy as recorded in the SS document. Both sides agree on the *diagram* and on the *theta values* `q_v^{j²}` (cf. Section 1.3 of this repository, 3/3 consensus). They disagree on whether consistent identifications across the Θ-link force the `j²` to be dropped (SS) or whether the rigidity / indeterminacy framework legitimately keeps the `j²` (Mochizuki). Encoded as `claim:scholze_stix_2018_sub_2` and `claim:scholze_stix_2018_sub_3`.

## 2.6 Where SS explicitly agree (consensus on what is *not* contested)

- Mochizuki's anabelian theorem ([Anab3] Thm 1.9 / Cor 1.10) is accepted as valid. (Scholze-Stix 2018, p. 5; cf. Section 1.1 of this repository.)
- The categorical structure of Hodge theaters in IUTT-1 is not contested — SS work *within* it.
- Some simplifications applied by SS were confirmed by Mochizuki in Kyoto as "OK." (Scholze-Stix 2018, p. 4, excuse (1).)
- The log-link and Θ-link constructions, *as categorical operations*, are not themselves disputed (Scholze-Stix 2018, §2.1.9). The disagreement is about what the Θ-link *transports*, not whether it is well-defined.

## Forbidden translations (per `LLM_CONTEXT.md` §4)

- Do NOT render the Θ±ellNF-Hodge theater, its components (Θ-Hodge / Θ±ell- / ΘNF-), the log-shell, or the Θ-link in terms of: perfectoid spaces, diamonds, condensed mathematics, prismatic cohomology. No such correspondence is established in either Mochizuki's RIMS papers or in Scholze-Stix 2018; the translatability is itself part of the unresolved dispute (cf. `LLM_CONTEXT.md` §4).
- Do NOT paraphrase "Θ-link" as "ring isomorphism" or "scheme-theoretic comparison map" — both sides explicitly note the Θ-link is *not* compatible with ring/scheme structure (IUTchI Cor 3.7; Scholze-Stix 2018 p. 9 implicitly accepts the non-ring-compatibility while disputing its content).

## Cross-reference

- IRI / Lean stub mapping: `data/entities.json` (`iut:HodgeTheater`, `iut:theta_link`, `iut:log_link`).
- Dispute claim graph: `data/claims.json` — relevant nodes: `claim:scholze_stix_2018_sub_1`, `claim:scholze_stix_2018_sub_2`, `claim:scholze_stix_2018_sub_3`, `claim:scholze_stix_2018_main`, `claim:mochizuki_2012_proves_abc`, `claim:mochizuki_2018_response`.
- Per-side drafts (do NOT cite as source of truth): `docs/concepts/hodge_theater.md`, `docs/concepts/hodge_theater_ss_view.md`.
- Section 1 (prerequisites): `docs/section_1_prerequisites.md` — anabelian / Frobenioid / étale theta consensus and disputes feeding into this section.

## Verification log

- 2.1 definition (Θ±ellNF triple = Θ±ell + ΘNF + unique gluing): **3/3 consensus** ✅ (IUTchI Def 6.13 cited by both sides; SS p. 6 explicitly references the same Mochizuki definitions).
- 2.1 components (Θ-Hodge theater, Θ±ell-Hodge theater, ΘNF-Hodge theater, initial Θ-data): **3/3 consensus** ✅ (IUTchI Defs 3.1, 3.6, 4.6, 5.5, 6.4, 6.11; SS works within these definitions).
- 2.1 étale-like data = `π₁(X)` up to inner auto; Frobenius-like = `π₁` ↷ monoid: **3/3 consensus** ✅ (IUTchI §I3 + Scholze-Stix 2018 pp. 5–6).
- 2.2 log-shell `I_v` and log-volume integration: **1/3 [CLAIMED_BY: Mochizuki]** at the textual-quotation level (IUTchIII Def 1.1; SS does not quote these definitions but does not refute them; SS critique is downstream at the Cor 3.12 diagram).
- 2.3 distinct Hodge theaters genuinely distinct vs. equivalent to choosing `X`: **0/3 → [DISPUTED]** (Mochizuki: alien arithmetic holomorphic structure / SS p. 6: equivalence of categories with `{X}`). Encoded as `claim:scholze_stix_2018_sub_1`.
- 2.4 Θ-link triviality: **0/3 → [DISPUTED]** (Mochizuki: full poly-iso ring-incompatible / SS p. 9: canonically the same datum with renamed generator). Encoded as `claim:scholze_stix_2018_sub_1`.
- 2.5 monodromy `j²` inconsistency: **0/3 → [DISPUTED]** (Mochizuki: rigidity intact, indeterminacies absorb / SS p. 10: monodromy `j²` forces dropping the factor → empty inequality). Encoded as `claim:scholze_stix_2018_sub_2`, `claim:scholze_stix_2018_sub_3`.
- 2.6 Mochizuki anabelian theorem accepted; categorical structure of Hodge theaters not contested; Θ-link / log-link well-defined as categorical operations: **3/3 consensus** ✅ (Scholze-Stix 2018 pp. 4–5, §2.1.9).

### Aggregate

- **3/3 consensus**: 4 entries (definition of Θ±ellNF-Hodge theater and its three components; étale-like / Frobenius-like dichotomy; SS's explicit non-contestations).
- **1/3 [CLAIMED_BY: Mochizuki]**: 1 entry (log-shell / log-volume definitions — SS does not separately quote them; not refuted).
- **0/3 [DISPUTED]**: 3 entries — distinct copies / Θ-link triviality / `j²` monodromy — encoded as `claim:scholze_stix_2018_sub_1`, `sub_2`, `sub_3`.
- **0/3 absent (no entry created)**: none in this section.

The dispute structure is consistent with `LLM_CONTEXT.md` §3 UNRESOLVED FLAG: both sides agree on the named definitions of the Hodge theater and its components; they disagree on whether distinct Hodge theaters carry non-trivial information across the Θ-link, and on whether `j²` monodromy in IUTchIII Cor 3.12 is consistent or empty.
