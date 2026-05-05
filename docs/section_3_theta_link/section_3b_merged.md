# Section 3b (merged): IUTchII Cor. 4.10 — Θ×µ-link & Θ×µ_gau-link

> status: merged | sources: mochizuki-side (3b_iutchII_cor_4_10_deep.md) + SS-side (3b_iutchII_cor_4_10_deep_ss_view.md)
> verified_at: 2026-05-06
> entity IRIs: `iut:F_vdash_times_mu_prime_strip`, `iut:hodge_arakelov_evaluation`,
>   `iut:theta_times_mu_link`, `iut:theta_gau_link`
> claim IRIs: `claim:ss_f_modulus_strip_focal_extended`, `claim:mochizuki_theta_gau_link_essential`

---

## 1. MOCHIZUKI POSITION

### 1.1 F⊩▶×µ-prime-strip — `iut:F_vdash_times_mu_prime_strip` (Def. 4.9(vi)–(viii))

The **F⊩▶×µ-prime-strip** is:
```
*F⊩▶×µ = (*C⊩, Prime(*C⊩) ~→ V, *F⊢▶×µ, {*ρ_v}_{v∈V})
```
The local O× of the IUTchI F⊩-strip is replaced by O^{×µ} = O×/torsion.
At `v ∈ V^bad` the generators of `O▶(−) ≅ ℕ` together with `{*ρ_w}` determine
a **pilot object** in `*C⊩` (negative arithmetic degree, well-defined up to
isomorphism).

Source: IUTchII Def. 4.9(vi)–(viii), pp. 157–158.
DOI [10.4171/PRIMS/57-2-1](https://doi.org/10.4171/PRIMS/57-2-1).

### 1.2 Hodge-Arakelov evaluation — `iut:hodge_arakelov_evaluation` (Cor. 4.10(ii))

Evaluation isomorphism `†F⊩_env ~→ †F⊩_gau` effecting at `v ∈ V^bad`:
```
O×_{F_v} · Θ^N_v  ⇝  O×_{F_v} · {q^{j²}_v}^N_{j=1,...,l*}
```
(theta monoids → Gaussian monoids via restriction to l-torsion points).
**Uniradial in isolation**; multiradiality requires combination with the
IUTchIII log-link (Rmk. 2.9.1, 3.4.1, 3.7.1).

Source: IUTchII Cor. 4.10(ii); Introduction pp. 11–12.

### 1.3 Θ×µ-link — `iut:theta_times_mu_link` (Cor. 4.10(iii) part 1)

Full poly-isomorphism of F⊩▶×µ-prime-strips:
```
†F⊩▶×µ_env  ~→  ‡F⊩▶×µ_△
```
Strictly finer than `iut:theta_link` (IUTchI Cor. 3.7-i):

| | `iut:theta_link` | `iut:theta_times_mu_link` |
|---|---|---|
| Strip level | F⊩ | F⊩▶×µ |
| Units | O× | O^{×µ} = O×/torsion |
| Coric piece | D⊢-strip | F⊢×µ-strip |

Coric invariant (Cor. 4.10-iv): the induced full poly-iso
`†F⊢×µ_△ ~→ ‡F⊢×µ_△` defines the D-Θ±ellNF-link at base level.

Source: IUTchII Cor. 4.10(iii)(iv), pp. 159–160.

### 1.4 Θ×µ_gau-link — `iut:theta_gau_link` (Cor. 4.10(iii) part 2)

> "We shall refer to the full poly-isomorphism `†F⊩▶×µ_gau ~→ ‡F⊩▶×µ_△`
> as the Θ×µ_gau-link … which may be regarded as being obtained from the
> full poly-isomorphism `†F⊩▶×µ_env ~→ ‡F⊩▶×µ_△` by composition with the
> inverse of the evaluation isomorphism of (ii)."
> — IUTchII Cor. 4.10(iii), p. 160

Value-group transformation (Rmk. 4.11.1):
```
q_v  →  {q^{j²}_v}_{1 ≤ j ≤ l*}
```
Units O^{×µ} are coric; value groups are not.

**Significance for multiradiality** (Rmk. 4.10.2-i, p. 162):
> "it is precisely by thinking of [a further enhanced version of] the Θ×µ_gau-link
> as an object that is constructed as the composite of the Θ×µ-link with the
> operation of Galois evaluation that one may establish the crucial multiradiality
> properties discussed in [IUTchIII], Theorem 3.11."

Source: IUTchII Cor. 4.10(iii); Rmk. 4.10.2-3, 4.11.1, pp. 160–164.

---

## 2. SCHOLZE–STIX POSITION

SS 2018 (10 pp.) operates **entirely at the F⊩×µ-prime-strip level** (§2).

**Scope of SS engagement with IUTchII Cor. 4.10:**

| IUTchII construct | SS engagement |
|---|---|
| F⊩▶×µ-prime-strip (Def. 4.9(vi)–(viii)) | Analyzed in §2.1.5–2.1.9 |
| Θ×µ-link (Cor. 4.10(iii) part 1) | Analyzed as full poly-iso (§2.1.9) |
| Hodge-Arakelov evaluation (Cor. 4.10(ii)) | Acknowledged in fn. 5 as out of scope: "plays no role for us" |
| Θ×µ_gau-link (Cor. 4.10(iii) part 2) | **Absent** from SS 2018 (0 occurrences of "Θ-gau", verified) |

**SS p. 4 "agreement" — exact scope:**
> "(1) During our discussion in Kyoto, Mochizuki agreed that some of these
> simplifications are OK, for example regarding the critical notion of
> F⊩×µ-prime strips below." (SS §2, p. 4)

This agreement covers only that the description `G_v ⟲ o^{×µ}_{k̄_v} × N`
correctly captures the local strip data. It does **not** constitute agreement
on SS's subsequent canonical identification step (`R⊙,Θ ≅ R⊙,q via γ_can`).
Mochizuki contests this scope interpretation (RIMS 2018 response, to be
extracted as `3b_iutchII_cor_4_10_deep_mochizuki_response.md`).

See `claim:ss_f_modulus_strip_focal_extended`.

---

## 3. ALTERNATIVE / REFORMULATION

Joshi 2021–2024 addresses Cor. 4.10 separately; not within current SS-side
scope. No alternative reformulation indexed for this sub-section.

---

## 4. PENDING

- Mochizuki 2018 RIMS response to SS (re: exact scope of Kyoto agreement)
  to be extracted separately.
- `claim:mochizuki_theta_gau_link_essential` — IUTchIII Theorem 3.11
  multiradiality via Θ×µ_gau-link: full evidence chain pending IUTchIII
  deep section.

---

## 5. UNRESOLVED

Whether SS's canonical identification `R⊙,Θ ≅ R⊙,q ≅ R` (§2.2, p. 10)
is or is not legitimate within the IUTchII Cor. 4.10 framework remains the
core unresolved dispute. Neither the PRIMS publication (2021) nor any
independent verifier has adjudicated this as of 2026-05-06.

---

## Forbidden translations (inherited)

- Do NOT equate `iut:theta_times_mu_link` with `iut:theta_link`.
- Do NOT claim Θ×µ_gau-link is multiradial alone (requires IUTchIII log-link).
- Do NOT treat the evaluation isomorphism as a ring morphism.
- Do NOT render Gaussian monoids as perfectoid / condensed / prismatic objects.

---

## Sources

| Item | Source | Page | DOI / URL |
|---|---|---|---|
| Def. 4.9(vi)–(viii) | IUTchII | 157–158 | https://doi.org/10.4171/PRIMS/57-2-1 |
| Cor. 4.10(ii)–(iv) | IUTchII | 159–160 | ibid. |
| Rmk. 4.10.2-3, 4.11.1 | IUTchII | 161–164 | ibid. |
| Introduction | IUTchII | 11–15 | ibid. |
| F⊩×µ strip scope + agreement | SS 2018 | 4, 7–8 | https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
| Θ-link canonical identification | SS 2018 | 9 | ibid. |
| Empty inequality | SS 2018 | 9–10 | ibid. |
| Mutually alien copies | Alien Copies §3.3(ii) | 60–62 | https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf |
