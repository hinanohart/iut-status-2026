# Section 1: Prerequisites for IUT

> 3-agent verified (mochizuki-side / SS-side / neutral merger).
> Last verified: 2026-05-06.
> drift-zero IRIs: `iut:anabelian_geometry` / `iut:Frobenioid` / `iut:etale_theta`
> Source-of-truth contract: see `LLM_CONTEXT.md` §3 (4-block template).
> Per-side drafts (NOT consumer-facing): `docs/concepts/{anabelian,frobenioid,etale_theta}{,_ss_view}.md`.

This document records the 3-agent merge of mochizuki-side and SS-side drafts. **Definitional consensus** is recorded as plain bullets. **Interpretive disputes** (whether a concept is *essential* at the disputed step `iut:Cor.3.12`) are recorded as `[DISPUTED]` with both positions quoted. Single-side claims are flagged `[CLAIMED_BY: …]`. Empty bullets are not invented.

---

## 1.1 Anabelian geometry (`iut:anabelian_geometry`)

### Consensus (definitional / theorem-level)

- The basic anabelian theorem invoked in IUT is Mochizuki's: the functor `X ↦ π₁(X)` is fully faithful on a class of curves over number fields and p-adic fields, with an explicit quasi-inverse.
  - Mochizuki side: cited via the absolute anabelian framework reconstructing ring/scheme structure from abstract topological groups (IUTchI §I3, p. 21).
  - SS side: cited as [Anab3] Theorem 1.9 / Corollary 1.10 (Scholze-Stix 2018, p. 5).
- Étale-like data inside a Hodge theater is the abstract topological group `π₁(X)` up to inner automorphism, equivalently the abstract Galois category of finite étale covers (Scholze-Stix 2018, p. 5; consistent with IUTchI §I3).
- Mochizuki's anabelian theorem itself is accepted as correct by SS ("striking", Scholze-Stix 2018, p. 5).

### [CLAIMED_BY: Mochizuki] Specific anabelian rigidity statements used in IUT

- **Tempered anabelian rigidity (étale theta version)**: any isomorphism `γ : Π^tp_{X_α} →̃ Π^tp_{X_β}` of tempered fundamental groups of Tate curves over p-adic fields maps the étale theta class `O×_{K̈_α}·η̈^Θ_α` to a `ℤ`-conjugate of `O×_{K̈_β}·η̈^Θ_β`, and preserves decomposition groups and canonical integral structures of cusps.
  - Source: Mochizuki, EtTh, Theorem 1.6, pp. 22–23.
- **Constant multiple rigidity** up to `{±1}`-indeterminacy.
  - Source: Mochizuki, EtTh, Theorem 1.10, pp. 27–28.
- **Reconstruction of `F_mod` from `π₁(C_K)`** as one of the key applications of `F^⋇_l`-symmetry.
  - Source: IUTchI §I1, p. 8 (discussion); §I3, p. 21.
- These statements are not contradicted by SS but are not separately quoted in Scholze-Stix 2018.

### [DISPUTED] Essential role of anabelian geometry at `iut:Cor.3.12`

- **Mochizuki position** (`claim:mochizuki_2012_proves_abc`, `claim:mochizuki_2018_response`):
  - Anabelian geometry is the mechanism by which IUT "looks inside" one Hodge theater from another; without mono-anabelian reconstruction the Θ-link and log-link carry no geometric information across the ring-theoretic boundary (IUTchI §I3, pp. 21–22; Theorem A).
  - Source: Mochizuki, IUTchI, §I3, pp. 21–22. URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf>
- **Scholze–Stix position** (`claim:scholze_stix_2018_sub_2`):
  - "Anabelian geometry is supposed to be the key to Mochizuki's proof. However, here we see that in the IUTT papers, we are (for the essential part) in a situation where anabelian geometry holds true in the sense that geometry and group theory are equivalent." — Remark 9, p. 5.
  - "We could not find the point where it is essential to work with fundamental groups – there are no additional isomorphisms of fundamental groups that do not come from isomorphisms of schemes, precisely because of Mochizuki's theorem." — Remark 9, p. 5.
  - Source: Scholze-Stix 2018, p. 5. URL: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>
- **Neutral remark**: SS explicitly do NOT claim the field of anabelian geometry is invalid (Scholze-Stix 2018, "Critical caveat" of internal SS view, p. 5). The dispute is strictly scoped to whether anabelian machinery generates *extra degrees of freedom* needed at `iut:Cor.3.12`. The unresolved disagreement is encoded in the claim graph as `claim:scholze_stix_2018_sub_2`.

---

## 1.2 Frobenioid (`iut:Frobenioid`)

### Consensus (definitional / theorem-level)

- A **global realified Frobenioid** (the specific instance both sides discuss in connection with `iut:Cor.3.12`) corresponds, up to equivalence, to ordered 1-dimensional `ℝ`-vector spaces with an arithmetic-degree structure.
  - Mochizuki side: simple structure of Frobenioids — "essentially monoids isomorphic to `ℕ` or `ℝ_{≥0}`" — is what makes cross-theater gluings possible (IUTchI, p. 17).
  - SS side: "the category of global realified Frobenioids is equivalent to the category of ordered 1-dimensional `ℝ`-vector spaces" (Scholze-Stix 2018, p. 7).
- The construction of global realified Frobenioids from `F^♯`-prime strips, the canonical element `θ_can`, and the canonical trivialization (mapping `1 ↦ log(N(v))` finite / `↦ 2` infinite) are accepted by both sides (Scholze-Stix 2018, pp. 7–8, 10; consistent with FrdI Proposition 1.5).
- The **étale-like vs. Frobenius-like dichotomy** (base category `D` vs. `ℕ_{≥1}` Frobenius portion) is intrinsic at the categorical level (FrdI §I4, p. 9). SS do not contest this dichotomy at the level of the global realified Frobenioid.

### [CLAIMED_BY: Mochizuki] Full general theory of Frobenioids

- **General Frobenioid definition** (FrdI Definition 1.3): a category `C` with a functor `C → F_Φ` to an elementary Frobenioid satisfying seven conditions on factorization, surjectivity to base / `ℕ_{≥1}` / divisor monoid, faithfulness up to units, and isotropic objects.
  - Source: Mochizuki, FrdI, Definition 1.1(iii) and Definition 1.3, pp. 19–24.
- **Factorization theorem** (FrdI Definition 1.3(iv)): every morphism `φ` in a Frobenioid factors essentially uniquely as `α∘β∘γ` (pull-back / pre-step / Frobenius type).
- **Frobenius endomorphism of a number field** as a Frobenioid-theoretic object with no scheme-theoretic counterpart (FrdI Abstract; §I3, pp. 1, 7–8).
- **Category-theoretic reconstruction of `C → F_Φ`** from the abstract category `C` (FrdI §I1, pp. 2–3; §§3–4).
- SS do not quote or refute these statements; they restrict their analysis to the global realified case.

### [DISPUTED] Essential role of full Frobenioid theory at `iut:Cor.3.12`

- **Mochizuki position** (`claim:mochizuki_2012_proves_abc`):
  - "A `Θ^{±ell}NF`-Hodge theater is, in essence, a system of Frobenioids" (IUTchI Theorem A, p. 13). The Θ-link relates "certain Frobenioid-theoretic portions" of one Hodge theater to another in a way not compatible with ring/scheme structures (IUTchI Abstract, p. 1).
  - Source: Mochizuki, IUTchI, Abstract and §I1–I3.
- **Scholze–Stix position** (`claim:scholze_stix_2018_sub_2`):
  - "Mochizuki introduces the difficult notion of a Frobenioid in his papers [Frd1], [Frd2]. However, the notion of a global realified Frobenioid is very elementary." — Scholze-Stix 2018, p. 7.
  - The full generality of [Frd1], [Frd2] does not, in SS's reading, contribute additional content at the disputed step; the only Frobenioid structure that matters there reduces to an ordered 1-dimensional `ℝ`-vector space.
  - "The conclusion of this discussion is that with consistent identifications of copies of real numbers, one must in (1.5) omit the scalars `j²` that appear, which leads to an empty inequality." — Scholze-Stix 2018, p. 10.
  - Source: Scholze-Stix 2018, pp. 7, 10.
- **Neutral remark**: SS do not claim Frobenioid theory is mathematically invalid. The disagreement concerns whether the elaborate `[Frd1]/[Frd2]` machinery is doing nontrivial work at `iut:Cor.3.12`, and whether the identification of distinct `ℝ`-copies across the Θ-link is consistent. Encoded as `claim:scholze_stix_2018_sub_2`.

---

## 1.3 Étale theta function (`iut:etale_theta`)

### Consensus (theta-value construction only)

- The **theta-function values** `q_v^{j²} ∈ O_{k_v}` for `j = 1,…,ℓ▷` at bad places, arising up to `2ℓ`-th roots of unity as values of a Θ-function at certain `2ℓ`-torsion points, are accepted by both sides as a correct construction within a Hodge theater.
  - Mochizuki side: encoded as the Frobenioid-theoretic data at bad primes that the Θ-link transports (IUTchI p. 17; EtTh §§1–2).
  - SS side: "Up to some `2ℓ`-th roots of unity, these arise naturally as the values of a Θ-function at certain `2ℓ`-torsion points." (Scholze-Stix 2018, p. 8, §2.1.8.)
- Mochizuki's algorithm to recover `q_v^{j²}` from `π₁(X)` acting on a monoid of divisors on tempered coverings is acknowledged by SS as "ingenious" and is **not challenged** (Scholze-Stix 2018, p. 8, footnote 11; p. 5, footnote 5).
- The Θ-link, as a full poly-isomorphism between `F^♯_{Θ,1}` and `F^♯_{q,2}`, is accepted by SS as a well-defined construction (Scholze-Stix 2018, §2.1.9, pp. 8–9).

### [CLAIMED_BY: Mochizuki] Étale theta function and mono-theta environment (definitional)

- **Étale theta function** as the Kummer class `η̈^Θ ∈ H^1(Π^tp_{Ÿ}, Δ_Θ)` of the classical formal algebraic theta function on a tempered cover of a Tate curve.
  - Source: Mochizuki, EtTh, §1.
- **Mono-theta environment [mod N]**: triple `(Π^tp_Y[μ_N], D_Y ⊆ Out(…), μ_N`-conjugacy class from `s^Θ_{Ÿ}`).
  - Source: Mochizuki, EtTh, Definition 2.13(ii), p. 43 (approx.).
- **Three rigidity properties** of the mono-theta environment: cyclotomic, discrete, constant-multiple rigidity (EtTh Introduction pp. 3–5; Corollaries 2.18–2.19).
- **Theorem 5.10** identifying the Frobenioid-theoretic and group-theoretic mono-theta environments (EtTh Theorem 5.10, pp. 96–97 approx.).
- **`iut:etale_theta` is not redefined or independently invoked under that label by SS.** The phrase "étale theta function" does **not** appear in Scholze-Stix 2018, and `[EtTh]` is not in their reference list (Scholze-Stix 2018, full-text search; per-side draft `etale_theta_ss_view.md` p. 9–10 of §"How SS uses this concept").

### [DISPUTED] Locus of the alleged error relative to the étale theta machinery

- **Mochizuki position** (`claim:mochizuki_2012_proves_abc`, `claim:mochizuki_2018_response`):
  - The three rigidity properties of the mono-theta environment — particularly cyclotomic and constant-multiple rigidity — are what allow the Θ-link to carry controlled arithmetic information without collapsing to an indeterminate unit multiple. The mono-theta environment serves as a "translation apparatus" between `ℤ` and `ℤ̂` and the local extension structure of the tempered Frobenioid (EtTh, p. 6).
  - Source: Mochizuki, EtTh, Introduction pp. 3–6; IUTchI §I3.
- **Scholze–Stix position** (`claim:scholze_stix_2018_sub_2`):
  - Treats the étale theta construction as a "black box" producing the concrete `Θ`-pilot values; the disagreement is downstream, in the identification of distinct `ℝ`-copies after the values are placed in abstract `F^♯`-prime strips.
  - "It is clear that this will result in the whole diagram having monodromy `j²`, i.e. being inconsistent." — Scholze-Stix 2018, p. 10.
  - Source: Scholze-Stix 2018, p. 10; per-side draft `etale_theta_ss_view.md`.
- **Neutral remark**: The two positions describe *different loci* of the alleged failure (Mochizuki: rigidity is essential and intact; SS: the issue is the post-extraction identification of `ℝ`-copies). The two are not directly contradictory at the level of the étale theta construction itself; they are contradictory at the level of whether `iut:Cor.3.12` succeeds. Encoded as `claim:scholze_stix_2018_sub_2`.

---

## Cross-reference

- IRI / Lean stub mapping: `data/entities.json`.
- Dispute claim graph: `data/claims.json`.
- Per-side drafts (do NOT cite as source of truth): `docs/concepts/anabelian.md`, `docs/concepts/anabelian_ss_view.md`, `docs/concepts/frobenioid.md`, `docs/concepts/frobenioid_ss_view.md`, `docs/concepts/etale_theta.md`, `docs/concepts/etale_theta_ss_view.md`.

## Forbidden translations (per `LLM_CONTEXT.md` §4)

- Do NOT translate `iut:anabelian_geometry`, `iut:Frobenioid`, or `iut:etale_theta` into perfectoid spaces, diamonds, or condensed mathematics. The translatability is itself disputed; both sides above are quoted in their original framing precisely because the cross-vocabulary mapping is not consensus.

## Verification log

- 1.1 anabelian — basic theorem (fully faithful `X ↦ π₁(X)` on the relevant class): **3/3 consensus** ✅ (Mochizuki IUTchI §I3 + SS via Anab3 Thm 1.9 / Cor 1.10).
- 1.1 anabelian — étale-like data = `π₁(X)` up to inner automorphism: **3/3 consensus** ✅.
- 1.1 anabelian — specific rigidity statements (EtTh Thm 1.6, Thm 1.10, `F_mod` reconstruction): **1/3 [CLAIMED_BY: Mochizuki]** (not refuted by SS, not separately quoted).
- 1.1 anabelian — essential role at `iut:Cor.3.12`: **0/3 → [DISPUTED]** (Mochizuki: essential / SS Remark 9: "could not find the point where it is essential").
- 1.2 Frobenioid — global realified Frobenioid ≅ ordered 1-D `ℝ`-vector spaces (with degree structure): **3/3 consensus** ✅ (IUTchI p. 17 "essentially monoids" + SS p. 7 explicit equivalence).
- 1.2 Frobenioid — `θ_can` and canonical trivialization: **3/3 consensus** ✅.
- 1.2 Frobenioid — étale-like vs. Frobenius-like dichotomy at the categorical level: **3/3 consensus** ✅ (FrdI §I4 + SS not contesting at the global realified level).
- 1.2 Frobenioid — full FrdI Definition 1.3, factorization theorem, number-field Frobenius endomorphism, category-theoretic reconstruction: **1/3 [CLAIMED_BY: Mochizuki]** (SS focus exclusively on the global realified case; do not quote or refute the general theory).
- 1.2 Frobenioid — full `[Frd1]/[Frd2]` machinery essential at `iut:Cor.3.12`: **0/3 → [DISPUTED]** (Mochizuki IUTchI Thm A: "in essence, a system of Frobenioids" / SS p. 7: "very elementary"; SS p. 10: empty inequality after consistent identification).
- 1.3 étale theta — concrete theta values `q_v^{j²}` at `2ℓ`-torsion points: **3/3 consensus** ✅.
- 1.3 étale theta — Mochizuki's group-theoretic recovery algorithm "ingenious" (not challenged): **3/3 consensus** ✅ (SS p. 8 fn. 11).
- 1.3 étale theta — Θ-link as full poly-isomorphism well-defined: **3/3 consensus** ✅ (SS §2.1.9).
- 1.3 étale theta — definition of `η̈^Θ`, mono-theta environment, three rigidities, EtTh Thm 5.10: **1/3 [CLAIMED_BY: Mochizuki]** (the term "étale theta function" does not appear in Scholze-Stix 2018; `[EtTh]` not in their reference list).
- 1.3 étale theta — locus of the alleged error: **0/3 → [DISPUTED]** (Mochizuki: rigidity is essential and intact / SS: error is downstream of theta-value extraction, in identification of `ℝ`-copies, monodromy `j²`).

### Aggregate

- **3/3 consensus**: 9 entries (definitional / theorem-level statements both sides agree on).
- **1/3 `[CLAIMED_BY: Mochizuki]`**: 3 entries (full anabelian rigidity statements; full Frobenioid theory; full étale theta + mono-theta theory). SS neither quote nor refute; their critique is scope-restricted.
- **0/3 `[DISPUTED]`**: 3 entries — all of the form *"essential at `iut:Cor.3.12`"* — encoded as `claim:scholze_stix_2018_sub_2`.
- **0/3 absent (no entry created)**: none in this section.

The dispute structure is consistent with the `LLM_CONTEXT.md` UNRESOLVED FLAG: both sides agree on the named theorems and their statements; they disagree on whether the theorems do nontrivial work at the disputed step `iut:Cor.3.12`.
