# Section 7: abc consequence (`iut:height_inequality`, `iut:diophantine_inequality`, `iut:abc_conjecture`)

> 3-agent verified.
> Last verified: 2026-05-06.
> drift-zero IRIs: `iut:height_inequality`, `iut:diophantine_inequality`, `iut:abc_conjecture`
> v0.3 update: cross-ref to `iut:multiradial_representation_thm_3_11`, `iut:Ind1`/`iut:Ind2`/`iut:Ind3` internals,
>   `iut:log_Kummer_correspondence`, `iut:log_theta_lattice`, `iut:theta_gau_link`,
>   `iut:hodge_arakelov_evaluation`; new entity `iut:abc_special_case_via_iut`
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

**Dependency on upstream constructions (v0.3 cross-ref):**

The derivation of Thm. 1.10 from IUTchIII Cor. 3.12 passes through the following
chain of constructions, all of which must hold for the inequality to be non-trivial:

1. `iut:log_theta_lattice` — the two-dimensional non-commutative diagram of
   Hodge theaters (IUTchIII Def. 1.4); vertical arrows = log-links, horizontal arrows =
   Θ^×µ-links. The log-volume estimate is carried out on nodes of this lattice.

2. `iut:theta_gau_link` — the Θ^×µ_gau-link (IUTchII Cor. 4.10-iii pt 2);
   connects Θ-pilot object (`iut:theta_pilot_object`) to q-pilot object across the
   horizontal arrow of the log-theta-lattice. The Gaussian evaluation (`iut:hodge_arakelov_evaluation`)
   enters here.

3. `iut:hodge_arakelov_evaluation` — Hodge-Arakelov-theoretic evaluation isomorphism
   (IUTchII Cor. 4.10-ii); supplies the {j²}_{j=1..l^⋇} values that feed into the
   LGP-monoid estimate and ultimately into the leading term (l^⋇+3)/2 of Thm. 1.10.

4. `iut:multiradial_representation_thm_3_11` — IUTchIII Thm. 3.11-i; the multiradial
   representation of the splitting monoids of LGP-monoids. This is the output fed into
   Cor. 3.12. Its validity requires all three indeterminacies to be correctly bounded:
   - `iut:Ind1` (étale-theoretic: D'-strip Aut and label permutation)
   - `iut:Ind2` (Frobenius-theoretic: Z^×-indeterminacy from Θ-link and O^×µ-action)
   - `iut:Ind3` (log-volume: upper semi-compatibility of log-Kummer isomorphisms)

5. `iut:log_Kummer_correspondence` — IUTchIII Thm. 3.11-ii; the log-Kummer
   correspondence on log-shells underlies Ind3. The "upper semi-compatible" (not
   isomorphic) nature of the Kummer maps across the log-link is where the inequality
   direction originates.

**Dependency on Cor. 3.12:** The inequality derives from IUTchIII Cor. 3.12 supplying
C_Θ ≥ −1 (notation of Thm. 1.10 proof). Both sides acknowledge this dependency;
dispute concentrates on Cor. 3.12 (Section 6).

IUTchIV p. 31 verbatim:
> "The final portion of Theorem 1.10 follows immediately from [IUTchIII], Corollary 3.12,
> by applying the inequality of the first display of Step (ii)..."

### 7.2.2 Corollary 2.2 (ii) — Diophantine bound with explicit ε-term (`iut:diophantine_inequality`)

**Reference:** IUTchIV §2, Cor. 2.2 (pp. 42–48).

    1/6 · log(q)  ≤  (1 + ε_E)·(log-diff_X(x_E) + log-cond_D(x_E)) + C_K

where ε_E := (60δ)^2 · (log(q^∀))^{−1/2} · log(2δ·log(q^∀)) and C_K depends only on K_V.
Asymptotic form (Remark 2.2.1, assuming F^{tpd} = Q):

    1/6 · h  ≤  δ  +  *· δ^{1/2} · log(δ)

Mochizuki notes the ε-term δ^{1/2}·log(δ) is "strongly reminiscent of well-known interpretations
of the Riemann hypothesis" (IUTchIV Rem. 2.2.1).

Remark 2.2.3 (IUTchIV p. 51) notes that Cor. 2.2 (ii)/(iii) for arbitrary positive integer d
may be regarded as a "weak version" of the "uniform ABC Conjecture", restricted to points
in the compactly bounded subset K_V.

### 7.2.3 Corollary 2.3 = Theorem A — general inequality (consensus on statement)

**Reference:** IUTchIV §2, Cor. 2.3 (p. 54). Verbatim from PDF (p. 54):

> "Let X be a smooth, proper, geometrically connected curve over a number field;
> D ⊆ X a reduced divisor; U_X = X \ D; d a positive integer; ε ∈ R_{>0} a positive
> real number. Write ω_X for the canonical sheaf on X. Suppose that U_X is a hyperbolic
> curve, i.e., that the degree of the line bundle ω_X(D) is positive. Then... one has an
> inequality of 'bounded discrepancy classes'
>
>     ht_{ω_X(D)} ≲ (1 + ε)(log-diff_X + log-cond_D)
>
> of functions on U_X(Q)^{≤d}."

**Proof structure (IUTchIV p. 54-55):** Mochizuki reduces Cor. 2.3 to [GenEll] Thm. 2.1 (i).
To prove [GenEll] Thm. 2.1 (ii), he specializes to:
- X = P^1_Q (projective line over Q)
- D = {0, 1, ∞} (three-point divisor)
- K_V compactly bounded subset satisfying condition (∗j-inv) of Cor. 2.2

Then the inequality follows from Cor. 2.2 (ii) condition (C2) and (iii).

Both sides do not contest the formal statement of Cor. 2.3 / Thm A.
SS explicitly states it does not independently critique IUTchIV §2–3 steps
(SS 2018, implicit from p. 10 scope restriction).

---

## 7.3 [DISPUTED] Validity of the chain Cor. 3.12 → height inequality → abc

**Status:** DISPUTED — downstream of `claim:scholze_stix_2018_main` (Section 6).

### 7.3.1 Mochizuki position

- IUTchIV Introduction (p. 3) verbatim:
  > "the so-called Vojta Conjecture for hyperbolic curves, **the ABC Conjecture,
  > and the Szpiro Conjecture for elliptic curves all follow as special cases of Theorem A**."

- The chain is:
  ```
  iut:multiradial_representation_thm_3_11  (IUTchIII Thm. 3.11-i)
      ↓   [multiradial algorithm + Ind1/Ind2/Ind3 bounds]
  iut:log_Kummer_correspondence            (IUTchIII Thm. 3.11-ii)
      ↓   [upper semi-compatibility supplies inequality direction]
  IUTchIII Cor. 3.12  (C_Θ ≥ −1)
      ↓   [IUTchIV Thm. 1.10 proof, p. 31]
  IUTchIV Thm. 1.10   (iut:height_inequality, explicit)
      ↓
  IUTchIV Cor. 2.2    (iut:diophantine_inequality, Diophantine bound)
      ↓
  IUTchIV Cor. 2.3 = Thm. A  (iut:abc_special_case_via_iut, general inequality)
      ↓   [GenEll Thm. 2.1 reduction: X=P^1, D={0,1,∞}]
  abc / Vojta / Szpiro as special cases
  ```

- Mochizuki's position is that if Cor. 3.12 holds (as he maintains), the entire chain
  is valid with **explicit constants** C(ε, d), not merely asymptotic.

- Reduction abc ← Thm. A: X = P^1, D = {0,1,∞}, point (a:b:c) with a+b+c=0, gcd=1.
  Then ht_{ω_X(D)} ~ log max(|a|,|b|,|c|) and log-cond_D ~ log rad(abc).

- Reference for reduction: Mochizuki, *Arithmetic Elliptic Curves in General Position* (2009),
  <https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf>

- **Role of theta_gau_link and hodge_arakelov_evaluation:** The values {j²}_{j=1..l^⋇}
  computed by `iut:hodge_arakelov_evaluation` (IUTchII Cor. 4.10-ii) enter via the
  `iut:theta_gau_link` (IUTchII Cor. 4.10-iii) as the essential data crossing the
  horizontal arrow of the log-theta-lattice. Mochizuki's position is that the Gaussian
  sum structure of these values, when combined with the indeterminacy bounds Ind1–Ind3,
  yields the non-trivial inequality C_Θ ≥ −1 in Cor. 3.12.

### 7.3.2 SS position

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

- In SS's view, the issue originates at the horizontal arrow of the log-theta-lattice:
  the identification of `iut:theta_gau_link` values across non-ring-theoretic arrows
  forces the j²-scalars to be treated as indeterminate, collapsing the estimate.

- Source: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>

### 7.3.3 Neutral remark

The direct technical dispute is located in Section 6 (Cor. 3.12). Section 7 records the
consequence: if the Section 6 dispute resolves in Mochizuki's favor, the abc chain follows;
if it resolves in SS's favor, the chain does not.

Neither side disputes that the chain *would* be valid if Cor. 3.12 holds. The academic
mathematical community has not reached consensus on Cor. 3.12 as of 2026-05-06.

The indeterminacies Ind1–Ind3 (tracked via `iut:Ind1_d_prime_strip_aut`,
`iut:Ind1_label_permutation`, `iut:Ind2_z_times_indeterminacy`, `iut:Ind2_o_times_mu_action`,
`iut:Ind3_upper_semi_compat_kummer`, `iut:Ind3_log_volume_absorption`) are the precise locus
of the dispute: Mochizuki claims they are bounded sufficiently to allow C_Θ ≥ −1; SS claims
the bound is vacuous when copies of real-number structures are consistently identified.

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
| Proof of Cor. 2.3 reduces to [GenEll] Thm. 2.1 via X=P^1, D={0,1,∞} | 3/3 consensus ✅ |
| `iut:hodge_arakelov_evaluation` and `iut:theta_gau_link` are formally present in IUTchII | 3/3 consensus ✅ |
| `iut:multiradial_representation_thm_3_11` (IUTchIII Thm. 3.11-i) is formally stated | 3/3 consensus ✅ |

---

## 7.5 [CLAIMED_BY: Mochizuki] explicit constants and special cases

The following claims are present in the IUTchIV text but are accepted only by the
Mochizuki side as established results:

- **Explicit C(ε, d):** Cor. 2.2 (ii) yields an explicit constant, not merely asymptotic.
  The ε-term δ^{1/2}·log(δ) in Remark 2.2.1 is noted as consistent with van Frankenhuijsen's
  conjecture (lim sup = 1/2, RH-type bound).

- **abc as special case of Thm. A** (IUTchIV Introduction, p. 3). See §7.6 below and
  `iut:abc_special_case_via_iut`.

- **Vojta conjecture for hyperbolic curves** as special case of Thm. A.

- **Szpiro conjecture for semistable elliptic curves** as special case of Thm. A.

- **Frey–Faltings / effective Mordell** as downstream consequence (noted in [GenEll]).
  IUTchIV Remark 2.3.3 frames Cor. 2.3 as "an effective version of the Mordell Conjecture".

- **Cor. 2.3 = Thm. A (Introduction):** Mochizuki presents Cor. 2.3 as the body of the paper
  and labels it Theorem A in the Introduction for expository unity (IUTchIV p. 54 proof confirms
  the two statements "coincide precisely").

These claims are conditioned on Cor. 3.12 being valid; they are not independently
disputed at the level of IUTchIV itself (see §7.3.3 neutral remark above).

---

## 7.6 (NEW) abc as special case of Theorem A — `iut:abc_special_case_via_iut`

**Entity IRI:** `iut:abc_special_case_via_iut`
**Type:** Theorem (CLAIMED_BY: Mochizuki)
**Reference:** IUTchIV Cor. 2.3 (p. 54) + Introduction (p. 3) + [GenEll] Thm. 2.1
**Data file:** `data/entities_phase_a7_draft.json`

### Statement

Mochizuki claims that the abc conjecture (`iut:abc_conjecture`) is a special case of
Theorem A (`iut:abc_special_case_via_iut`), which is the content of Cor. 2.3 of IUTchIV.

IUTchIV Introduction (p. 3) verbatim:
> "the so-called Vojta Conjecture for hyperbolic curves, **the ABC Conjecture,
> and the Szpiro Conjecture for elliptic curves all follow as special cases of Theorem A**."

### Reduction to abc (the [GenEll] route)

Cor. 2.3 establishes the inequality on U_X(Q)^{≤d} for any hyperbolic curve U_X.
For abc, the relevant specialization (IUTchIV p. 55, citing [GenEll] Thm. 2.1) is:

    X = P^1_Q,   D = {0, 1, ∞},   U_X = P^1 \ {0,1,∞}

A rational point x ∈ U_X(Q) corresponds (via the cross-ratio parametrization) to a
coprime triple (a, b, c) with a + b + c = 0, gcd(a,b,c) = 1. Under this correspondence:

    ht_{ω_X(D)} ~ log max(|a|, |b|, |c|)
    log-diff_X  = 0   (since X = P^1 is smooth)
    log-cond_D  ~ log rad(abc)

So the Cor. 2.3 inequality:

    ht_{ω_X(D)} ≲ (1 + ε)(log-diff_X + log-cond_D)

becomes:

    log max(|a|, |b|, |c|) ≲ (1 + ε) log rad(abc)

which is precisely the abc conjecture (up to the constant C(ε)).

### Dependency chain (abbreviated)

    iut:log_theta_lattice
    iut:theta_gau_link  +  iut:hodge_arakelov_evaluation
        ↓
    iut:multiradial_representation_thm_3_11
      [iut:Ind1, iut:Ind2, iut:Ind3]
        ↓
    iut:log_Kummer_correspondence
        ↓
    iut:Cor.3.12  [DISPUTED, Section 6]
        ↓
    iut:height_inequality  (IUTchIV Thm. 1.10)
        ↓
    iut:diophantine_inequality  (IUTchIV Cor. 2.2)
        ↓
    iut:abc_special_case_via_iut  (IUTchIV Cor. 2.3 = Thm. A)
        ↓
    iut:abc_conjecture

### Status note

This entity is `CLAIMED_BY: Mochizuki`. The derivation is not independently disputed
at the level of IUTchIV §2–3 by SS (SS 2018, p. 10 scope restriction). The dispute
that blocks this claim is located entirely in Section 6 (`iut:Cor.3.12`).

---

## 7.7 Forbidden translations

The following phrasings are not used in this document, per project policy.

| Forbidden | Reason |
|---|---|
| "the inequality is circular" | SS formulation not adopted; use "empty inequality" with SS citation if attributing |
| "IUT proves abc" (unqualified) | `claim:mochizuki_2012_proves_abc` is DISPUTED; use "Mochizuki claims" |
| "abc remains open" without qualification | Accurate but must note: "as of 2026-05-06, pending resolution of Section 6 dispute" |
| "identification of objects in different copies" | Use IUT-native: "non-ring/scheme-theoretic horizontal arrow of the log-theta-lattice" |
| "Frobenioid = scheme" | Use: "species-theoretic formulation of Frobenioid" |
| "SS silent on IUTchIV §2–3" | Use: "SS does not independently analyze IUTchIV §2–3; its critique treats those sections as downstream of Cor. 3.12" |

---

## Cross-reference

### Entities (entities.json + entities_phase_a7_draft.json)

**Section 7 core:**
- `iut:height_inequality` — IUTchIV Thm. 1.10 explicit inequality
- `iut:diophantine_inequality` — IUTchIV Cor. 2.2 Diophantine bound
- `iut:abc_conjecture` — Masser–Oesterlé 1985 statement
- `iut:abc_special_case_via_iut` — NEW (entities_phase_a7_draft.json): abc as special case of Thm A

**Upstream (Section 5–6, load-bearing for §7):**
- `iut:multiradial_representation_thm_3_11` — IUTchIII Thm. 3.11-i; multiradial representation feeding Cor. 3.12
- `iut:Ind1` / `iut:Ind1_d_prime_strip_aut` / `iut:Ind1_label_permutation` — étale-theoretic indeterminacy
- `iut:Ind2` / `iut:Ind2_z_times_indeterminacy` / `iut:Ind2_o_times_mu_action` — Frobenius-theoretic indeterminacy
- `iut:Ind3` / `iut:Ind3_upper_semi_compat_kummer` / `iut:Ind3_log_volume_absorption` — log-volume indeterminacy
- `iut:log_Kummer_correspondence` — IUTchIII Thm. 3.11-ii; underlies Ind3 and inequality direction
- `iut:Cor.3.12` — IUTchIII Cor. 3.12; pivot of Section 6 dispute

**Upstream (Section 3–4, feed into multiradial):**
- `iut:log_theta_lattice` — IUTchIII Def. 1.4; the two-dimensional lattice on which log-volume is computed
- `iut:theta_gau_link` — IUTchII Cor. 4.10-iii; Gaussian link carrying j²-values
- `iut:hodge_arakelov_evaluation` — IUTchII Cor. 4.10-ii; evaluation isomorphism supplying j²-values
- `iut:log_link` / `iut:log_link_construction` / `iut:log_link_compatibility` — vertical log-theta-lattice arrows
- `iut:log_shell` / `iut:log_shell_containment` / `iut:log_volume_integration` — log-shell infrastructure

### Claims

- `claim:mochizuki_2012_proves_abc` — DISPUTED (downstream of Section 6)
- `claim:scholze_stix_2018_main` — SS 2018 main critique (see Section 6)
- `claim:joshi_2025_alternative` — alternative approach (see Section 8)

### Related sections

- Section 5 (`section_5_multiradial.md`): `iut:multiradial_representation_thm_3_11`, Ind1–Ind3 internals
- Section 6 (`section_6_cor_3_12.md`): the load-bearing upstream dispute; resolves §7 status
- Section 4 (`section_4_log_link.md`): `iut:log_theta_lattice`, `iut:log_Kummer_correspondence`
- Section 3 (`section_3_theta_link.md`): `iut:theta_gau_link`, `iut:hodge_arakelov_evaluation`

---

## Verification log

| Item | Score |
|---|---|
| 7.1 abc conjecture statement (Masser–Oesterlé 1985) | 3/3 ✅ |
| 7.2.1 Thm. 1.10 statement-level (both sides) | 3/3 ✅ |
| 7.2.1 dependency chain via log_theta_lattice / theta_gau_link / multiradial (v0.3 cross-ref) | 3/3 ✅ (statement-level) |
| 7.2.2 Cor. 2.2 (ii) Diophantine bound statement | 3/3 ✅ |
| 7.2.3 Cor. 2.3 = Thm. A general inequality statement | 3/3 ✅ |
| 7.2.3 Proof structure: reduction to [GenEll] Thm 2.1, X=P^1, D={0,1,∞} | 3/3 ✅ (IUTchIV p. 54-55 verbatim) |
| 7.3 validity of chain Cor. 3.12 → height → abc | 0/3 [DISPUTED] (downstream of Section 6) |
| 7.3.1 Mochizuki's theta_gau_link / hodge_arakelov_evaluation argument | 1/3 [CLAIMED_BY: Mochizuki] |
| 7.3.2 SS empty-inequality critique (j² blurring, Ind2 O(l²)) | 1/3 [CLAIMED_BY: SS] |
| 7.4 NOT in dispute items (extended, 11 items) | 3/3 ✅ |
| 7.5 explicit constants + special cases | 1/3 [CLAIMED_BY: Mochizuki] |
| 7.6 abc_special_case_via_iut entity (NEW) | 1/3 [CLAIMED_BY: Mochizuki] |
| 7.7 forbidden translations (extended, +SS silent) | 3/3 ✅ |
