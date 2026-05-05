# Section 1e: Mono-Theta Environment — 3 Rigidities

> 3-agent verify pending.
> Last updated: 2026-05-06.
> Parent: docs/section_1_prerequisites.md
> drift-zero IRIs: iut:mono_theta_cyclotomic_rigidity, iut:mono_theta_discrete_rigidity, iut:mono_theta_constant_multiple_rigidity
> Per-side drafts: 1e_mono_theta_env_deep.md (Mochizuki), 1e_mono_theta_env_deep_ss_view.md (SS)
> Monitor verdict (2026-05-06): 3 entities confirmed; all [CLAIMED_BY: Mochizuki] — SS 2018 全文 (pymupdf) に "mono-theta" / "cyclotomic" / "discrete" / "constant multiple" の出現 0 件。

---

## Background: Mono-Theta Environment

A **[mod N] mono-theta environment** is an ordered triple
`M = (Π, D_Π, s^Θ_Π)` where `Π ≅ Π^tp_Y[μ_N]`, `D_Π` encodes `D_Y`, and
`s^Θ_Π` is the `μ_N`-conjugacy class determined by the theta section `s^Θ_Ÿ`.
Def. 2.13 (EtTh, pp. 43–44). All three rigidities are established in Cor. 2.19
(EtTh, pp. 58–59).

---

## 1e.1 Cyclotomic rigidity (`iut:mono_theta_cyclotomic_rigidity`)

### [CLAIMED_BY: Mochizuki]

- **Source**: EtTh Cor. 2.19 (i) (p. 58); EtTh Thm. 1.10.
- **Statement**: Given any abstract mono-theta environment `M•` isomorphic to
  `M_N`, there exists a *functorial group-theoretic algorithm* — using only the
  abstract structure of `M•`, devoid of any fixed identification `M• ≅ M_N` —
  that produces two splittings of
  `Π•|(l·Δ•_Θ) ↠ (l·Δ•_Θ)`,
  whose difference yields a canonical isomorphism of cyclotomes
  `(l·Δ•_Θ) ⊗ (Z/NZ) ≅ Π•_μ`.
- **Role in IUT**: The cyclotome `μ_N` is identified intrinsically from `M•`
  alone, making the theta Kummer class self-contained across the θ-link
  (IUTchII §2). Without this, cyclotomic comparison across distinct Hodge
  theaters is ambiguous.
- **SS**: "cyclotomic" 全文 NOT FOUND。EtTh Cor. 2.19 への言及なし。
  SS が §2.1.8 で "ingenious" と呼ぶアルゴリズム (q^{j²}_v の復元) の
  formalism を支える層だが、SS はその正否を評価しない。
- **判定**: `[CLAIMED_BY: Mochizuki]` — SS scope 外。

**Sources**: EtTh Cor. 2.19 (i) pp. 58–59; Thm. 1.10 pp. 27–28
<https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>;
SS 2018 (not found) <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

---

## 1e.2 Discrete rigidity (`iut:mono_theta_discrete_rigidity`)

### [CLAIMED_BY: Mochizuki]

- **Source**: EtTh Cor. 2.19 (ii) (p. 59).
- **Statement**: Let `E ⊆ N≥1` be cofinal and totally ordered with `1 ∈ E`.
  Any projective system `{M•_M}_{M∈E}` of abstract mono-theta environments
  is isomorphic to the natural projective system `{M_M}_{M∈E}`.
- **Key point**: The theta-torsor in the projective limit lives over the
  *discrete* group `l·Z`, not over its profinite completion `l·Ẑ`. Bi-theta
  environments fail this property (EtTh Cor. 2.16 / Rem. 2.16.1): their extra
  symmetry introduces `l·Ẑ`-indeterminacy.
- **Role in IUT**: Without discrete rigidity, projective-limit theta values
  drift over `l·Ẑ`, contaminating the Cor. 3.12 multiradial output
  (IUTchIII).
- **SS**: "discrete" 全文 NOT FOUND。評価対象外。
- **判定**: `[CLAIMED_BY: Mochizuki]` — SS scope 外。

**Sources**: EtTh Cor. 2.19 (ii) p. 59; Cor. 2.16, Rem. 2.16.1
<https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>;
SS 2018 (not found) <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

---

## 1e.3 Constant multiple rigidity (`iut:mono_theta_constant_multiple_rigidity`)

### [CLAIMED_BY: Mochizuki]

- **Source**: EtTh Cor. 2.19 (iii) (p. 59); EtTh Thm. 1.10.
- **Statement**: Assuming `η̈^{Θ,l·Z×μ_2}` is of standard type, there exists
  a *functorial group-theoretic algorithm* on any `Π•_X ≅ Π^tp_X` — devoid
  of any fixed identification — constructing a collection of classes in
  `H¹(Π•_Ÿ, (l·Δ•_Θ))` that maps, under any `Π•_X ≅ Π^tp_X`, to the
  étale theta classes `η̈^{Θ,l·Z×μ_2}` **up to multiplication by an
  l-th root of unity** (EtTh Cor. 2.8 (i)).
- **Residual ambiguity**: The `±1` ambiguity is not an error; it corresponds
  to the canonical `{±1}`-structure at the cusp (Thm. 1.10 (iii)).
- **Role in IUT**: Pins the theta value from `Π^tp_X` alone, up to
  `{±1}` × l-th root ambiguity. Without this, the theta value is only an
  `l·Ẑ`-orbit and cannot seed the Cor. 3.12 inequality.
- **Relationship to 1d**: Thm. 1.10 (registered as `iut:absolute_anabelian_theta`
  in 1d) is the scheme-theoretic precursor; Cor. 2.19 (iii) is the
  abstract group-theoretic (mono-theta-environment-level) generalization.
- **SS**: "constant multiple" 全文 NOT FOUND。評価対象外。
  注意: SS が §2.1.8 で "ingenious" と呼ぶ算法は Thm. 1.10 系の成果を
  事実上承認しているが、Cor. 2.19 の formalism には明示的に触れない。
- **判定**: `[CLAIMED_BY: Mochizuki]` — SS scope 外。

**Sources**: EtTh Cor. 2.19 (iii) p. 59; Thm. 1.10 pp. 27–28; Cor. 2.8 (i)
<https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>;
SS 2018 (not found) <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.

---

## 1e.4 All 3 rigidities essential to IUT mono-theta environment

### [CLAIMED_BY: Mochizuki] — SS 沈黙

- Mochizuki の主張: 3 rigidities は同時に mono-theta 環境においてのみ成立し、
  IUTchII θ-link と IUTchIII Cor. 3.12 multiradial algorithm に essential。
  (IUTchII §2 pp. 47–58; IUTchIII Cor. 3.12)
- **Mono vs. bi-theta**: Bi-theta 環境は discrete rigidity を失う
  (EtTh Cor. 2.16)。"Naïve use both sections" approach は非離散不定性を
  導入し Cor. 3.12 出力を汚染する、と Mochizuki は主張する。
- **SS の態度**: SS 2018 全文に "mono-theta" / "EtTh" / "Cor. 2.19" の出現なし。
  SS の批判 chain は「q^{j²}_v の復元 (Step 1) → F^{⊩×µ}-prime strip
  抽象化 (Step 2) → ℝ-copies identification の inconsistency (Step 3-4)」に
  集中する。Step 1 の formalism (= 3 rigidities の apparatus) を invalid と
  する主張は SS 2018 全文に存在しない。
- **判定**: `[CLAIMED_BY: Mochizuki]` — SS scope 外 (否定も肯定もなし)。

**Sources**: IUTchII §2; IUTchIII Cor. 3.12; EtTh Cor. 2.16, 2.19
<https://www.kurims.kyoto-u.ac.jp/~motizuki/inter-universal-teichmuller-theory-ii.pdf>;
<https://www.kurims.kyoto-u.ac.jp/~motizuki/inter-universal-teichmuller-theory-iii.pdf>;
SS 2018 (not found) <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>.
