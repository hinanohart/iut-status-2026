# Section 7: abc consequence (`iut:height_inequality`, `iut:diophantine_inequality`, `iut:abc_conjecture`)

> 3-agent verified.
> Last verified: 2026-05-06.
> drift-zero IRIs: `iut:height_inequality`, `iut:diophantine_inequality`, `iut:abc_conjecture`
> Per-side drafts: docs/concepts/abc_consequence.md, docs/concepts/abc_consequence_ss_view.md

---

## 7.1 abc conjecture statement (consensus)

Both sides agree on the following.

- **abc conjecture (Masser–Oesterlé 1985):** for any ε > 0, there exists C(ε) such that for
  all coprime triples (a, b, c) with a + b = c,

      max(|a|, |b|, |c|) ≤ C(ε) · rad(abc)^{1+ε}

  where rad(n) = product of distinct prime divisors of n.

- **Historical note**: the conjecture was formulated in unpublished correspondence by Masser
  (1985) and published by Oesterlé (1988): *Nouvelles approches du "théorème" de Fermat*,
  Séminaire Bourbaki 694.

- Both sides treat abc as an **open conjecture** as of 2026-05-06; neither side claims it is
  false or trivially true.

- `iut:abc_conjecture` IRI = the conjecture statement only. Its validity / proof status is
  tracked via `claim:mochizuki_2012_proves_abc` (disputed, see §7.3).

---

## 7.2 IUTchIV height inequality (statement-level)

Both sides agree that the following *statements* are formally present in the IUTchIV paper.
Validity of the proof chain is the subject of §7.3.

### 7.2.1 Theorem 1.10 — explicit height inequality (`iut:height_inequality`)

**Reference:** IUTchIV §1, Theorem 1.10 (pp. 22–23).
DOI: [10.4171/PRIMS/57-1-4](https://doi.org/10.4171/PRIMS/57-1-4)
PDF: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf>

Given initial Θ-data (IUTchI Def. 3.1) with elliptic curve E_F / F, prime l ≥ 5:

    1/6 · log(q)  ≤  (1 + 20·d_mod/l)·(log d^{F^{tpd}} + log f^{F^{tpd}})
                      + 20·(e*_mod·l + η_prm)

where d_mod = [F_mod : Q], e*_mod = 2^{12}·3^3·5·e_mod, η_prm > 0 from Prop. 1.6
(Prime Number Theorem estimate).

**Dependency:** The inequality derives from IUTchIII Cor. 3.12 supplying C_Θ ≥ −1.
Both sides acknowledge this dependency; dispute concentrates on Cor. 3.12 (Section 6).

### 7.2.2 Corollary 2.2 (ii) — Diophantine bound with explicit ε-term (`iut:diophantine_inequality`)

**Reference:** IUTchIV §2, Cor. 2.2 (pp. 42–48).

    1/6 · log(q)  ≤  (1 + ε_E)·(log-diff_X(x_E) + log-cond_D(x_E)) + C_K

where ε_E := (60δ)^2 · (log(q^∀))^{−1/2} · log(2δ·log(q^∀)) and C_K depends only on K_V.
Asymptotic form (Remark 2.2.1, assuming F^{tpd} = Q):

    1/6 · h  ≤  δ  +  *· δ^{1/2} · log(δ)

Mochizuki notes the ε-term δ^{1/2}·log(δ) is "strongly reminiscent of well-known interpretations
of the Riemann hypothesis" (IUTchIV Rem. 2.2.1).

### 7.2.3 Corollary 2.3 = Theorem A — general inequality (consensus on statement)

**Reference:** IUTchIV §2, Cor. 2.3 (p. 54). Verbatim:

> ht_{ω_X(D)}  ≲  (1 + ε)·(log-diff_X + log-cond_D)

on U_X(Q)^{≤d}, for any hyperbolic curve U_X = X \ D over a number field (deg ω_X(D) > 0).

Both sides do not contest the formal statement of Cor. 2.3 / Thm A.
SS explicitly states it does not independently critique IUTchIV §2–3 steps
(SS 2018, implicit from p.10 scope restriction).

---

## 7.3 [DISPUTED] Validity of the chain Cor. 3.12 → height inequality → abc

**Status:** DISPUTED — downstream of `claim:scholze_stix_2018_main` (Section 6).

### Mochizuki position

- IUTchIV Introduction (p. 3) verbatim:
  > "the so-called Vojta Conjecture for hyperbolic curves, **the ABC Conjecture,
  > and the Szpiro Conjecture for elliptic curves all follow as special cases of Theorem A**."

- The chain is:
  ```
  IUTchIII Cor. 3.12  (C_Θ ≥ −1)
      ↓
  IUTchIV Thm. 1.10   (explicit height inequality)
      ↓
  IUTchIV Cor. 2.2    (Diophantine bound, explicit ε-term)
      ↓
  IUTchIV Cor. 2.3 = Thm. A  (general inequality)
      ↓
  abc / Vojta / Szpiro as special cases
  ```

- Mochizuki's position is that if Cor. 3.12 holds (as he maintains), the entire chain
  is valid with **explicit constants** C(ε, d), not merely asymptotic.

- Reduction abc ← Thm. A routed through [GenEll, Thm. 2.1]:
  X = P^1, D = {0,1,∞}, point (a:b:c) with a+b+c=0, gcd=1.
  Then ht_{ω_X(D)} ~ log max(|a|,|b|,|c|) and log-cond_D ~ log rad(abc).

- Reference for reduction: Mochizuki, *Arithmetic Elliptic Curves in General Position* (2009),
  <https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf>

### SS position

- SS (2018, p. 4) on the chain with "consistent identifications of copies of real numbers":
  > "Starting from the corrected inequality we obtain **0 ⪅ d(P)** which is essentially
  > **free of content**."

- SS (2018, p. 10) on indeterminacy blurring:
  > "with consistent identifications of copies of real numbers, one must in (1.5) omit the
  > scalars j² that appear, which leads to an **empty inequality**."

- SS (2018, p. 10) on Mochizuki's day-5 reply (O(ℓ²) blurring):
  > "the blurring must be by a factor of at least O(ℓ²) rendering the inequality
  > thus obtained **useless**."

- SS's critique is **not** an independent analysis of IUTchIV §2–3; it treats the height
  inequality chain as a downstream consequence of Cor. 3.12. If Cor. 3.12 yields an empty
  inequality (SS claim), then IUTchIV Thm. 1.10 → Cor. 2.2 → Cor. 2.3 → abc cannot be
  derived.

- Source: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>

### Neutral remark

The direct technical dispute is located in Section 6 (Cor. 3.12). Section 7 records the
consequence: if the Section 6 dispute resolves in Mochizuki's favor, the abc chain follows;
if it resolves in SS's favor, the chain does not. Neither side disputes that the chain
*would* be valid if Cor. 3.12 holds. The academic mathematical community has not reached
consensus on Cor. 3.12 as of 2026-05-06.

---

## 7.4 What both sides agree is NOT in dispute

| Claim | Status |
|---|---|
| abc conjecture statement (Masser–Oesterlé 1985) | 3/3 consensus ✅ |
| abc conjecture is currently **open** in the academic community as of 2026-05-06 | 3/3 consensus ✅ |
| Formal existence of IUTchIV Thm. 1.10 / Cor. 2.2 / Cor. 2.3 statements | 3/3 consensus ✅ |
| abc chain *would* follow if Cor. 3.12 is valid | 3/3 consensus ✅ |
| Vojta conjecture for hyperbolic curves is equivalent to abc (in this context) | 3/3 consensus ✅ |
| Szpiro conjecture for elliptic curves follows from Thm. A | 3/3 consensus ✅ |
| IUTchIV §2–3 internal steps are NOT independently criticized by SS | 3/3 consensus ✅ |
| SS does not claim abc is false | 3/3 consensus ✅ |

---

## 7.5 [CLAIMED_BY: Mochizuki] explicit constants and special cases

The following claims are present in the IUTchIV text but are accepted only by the
Mochizuki side as established results:

- **Explicit C(ε, d):** Cor. 2.2 (ii) yields an explicit constant, not merely asymptotic.
  The ε-term δ^{1/2}·log(δ) in Remark 2.2.1 is noted as consistent with van Frankenhuijsen's
  conjecture (lim sup = 1/2, RH-type bound).

- **abc as special case of Thm. A** (IUTchIV Introduction, p. 3).

- **Vojta conjecture for hyperbolic curves** as special case of Thm. A.

- **Szpiro conjecture for semistable elliptic curves** as special case of Thm. A.

- **Frey–Faltings / effective Mordell** as downstream consequence (noted in [GenEll]).

These claims are conditioned on Cor. 3.12 being valid; they are not independently
disputed at the level of IUTchIV itself (see §7.3 neutral remark above).

---

## 7.6 Forbidden translations

The following phrasings are not used in this document, per project policy.

| Forbidden | Reason |
|---|---|
| "the inequality is circular" | SS formulation not adopted; use "empty inequality" with SS citation if attributing |
| "IUT proves abc" (unqualified) | `claim:mochizuki_2012_proves_abc` is DISPUTED; use "Mochizuki claims" |
| "abc remains open" without qualification | Accurate but must note: "as of 2026-05-06, pending resolution of Section 6 dispute" |
| "identification of objects in different copies" | Use IUT-native: "non-ring/scheme-theoretic horizontal arrow of the log-theta-lattice" |
| "Frobenioid = scheme" | Use: "species-theoretic formulation of Frobenioid" |

---

## Cross-reference

- entities.json: `iut:abc_conjecture`, `iut:height_inequality`, `iut:diophantine_inequality`,
  `iut:Cor.3.12`, `iut:Thm_A`
- claims.json: `claim:mochizuki_2012_proves_abc` (DISPUTED), `claim:scholze_stix_2018_main`
  (see Section 6), `claim:joshi_2025_alternative`
- Section 6 (`section_6_cor_3_12.md`): load-bearing upstream dispute
- Section 5 (`section_5_multiradial.md`): multiradial algorithm feeding into Cor. 3.12

---

## Verification log

| Item | Score |
|---|---|
| 7.1 abc conjecture statement (Masser–Oesterlé 1985) | 3/3 ✅ |
| 7.2.1 Thm. 1.10 statement-level (both sides) | 3/3 ✅ |
| 7.2.2 Cor. 2.2 (ii) Diophantine bound statement | 3/3 ✅ |
| 7.2.3 Cor. 2.3 = Thm. A general inequality statement | 3/3 ✅ |
| 7.3 validity of chain Cor. 3.12 → height → abc | 0/3 [DISPUTED] (downstream of Section 6) |
| 7.4 NOT in dispute items | 3/3 ✅ |
| 7.5 explicit constants + special cases | 1/3 [CLAIMED_BY: Mochizuki] |
| 7.6 forbidden translations | 3/3 ✅ |
