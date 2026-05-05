# Section 3b: IUTchII Cor. 4.10 Deep — Θ×µ-link & Θ×µ_gau-link

> status: mochizuki-side draft | 3-agent verify: pending | verified_at: 2026-05-06  
> new IRIs: `iut:theta_times_mu_link`, `iut:theta_gau_link`,
> `iut:hodge_arakelov_evaluation`, `iut:F_vdash_times_mu_prime_strip`  
> NOT a duplicate of `iut:theta_link` (IUTchI) — distinct prime-strip level

---

## 3b.1 Conceptual position

`iut:theta_link` (IUTchI Cor. 3.7-i) operates at the **F⊩-prime-strip** level.
IUTchII Cor. 4.10 introduces two **strictly finer** variants by replacing
F⊩-prime-strips with F⊩▶×µ-prime-strips (local O× → O^{×µ} = O×/torsion):

> "The Θ×µ-link is essentially the same as the Θ-link of [IUTchI], Theorem A,
> except that F⊩-prime-strips are replaced by F⊩▶×µ-prime-strips."
> — IUTchII Introduction, p. 14

---

## 3b.2 [iut:F_vdash_times_mu_prime_strip] — Def. 4.9(vi)–(viii), pp. 157–158

An **F⊩▶×µ-prime-strip** is the global object:
```
*F⊩▶×µ = (*C⊩, Prime(*C⊩) ~→ V, *F⊢▶×µ, {*ρ_v}_{v∈V})
```
satisfying IUTchI Def. 5.2(iv) conditions, with the F⊢ component replaced by
F⊢▶×µ (units = O^{×µ}, not O×). The generators of `O▶(−) ≅ ℕ` at `v ∈ V^bad`,
together with `{*ρ_w}`, determine a **pilot object** in `*C⊩`
(negative arithmetic degree, well-defined up to isomorphism).

Locally:
- `v ∈ V^bad`: split-Kummer Frobenioid (Def. 4.9-iii)
- `v ∈ V^good ∩ V^non`: split-Kummer Frobenioid (Def. 4.9-iv)
- `v ∈ V^arc`: inductive system `… ↠ O^{×µ_N}(A) ↠ …` of N-torsion quotients

Source: IUTchII Def. 4.9, pp. 157–158.
DOI [10.4171/PRIMS/57-2-1](https://doi.org/10.4171/PRIMS/57-2-1).

---

## 3b.3 [iut:hodge_arakelov_evaluation] — Cor. 4.10(ii), p. 159

The **evaluation isomorphism** `†F⊩_env ~→ †F⊩_gau` effects (at `v ∈ V^bad`):
```
O×_{F_v} · Θ^N_v  ⇝  O×_{F_v} · {q^{j²}_v}^N_{j=1,...,l*}
```
(theta monoids → Gaussian monoids, by evaluation at l-torsion points).

From IUTchII p. 12:
> "this requirement of compatibility with Kummer theory forces any sort of
> 'evaluation operation' to arise from restriction to Galois sections of the
> [arithmetic] tempered fundamental groups involved."

This isomorphism is **uniradial** in isolation (Rmk. 2.9.1, 3.4.1, 3.7.1);
multiradiality requires combination with the IUTchIII log-link.

Source: IUTchII Cor. 4.10(ii); Introduction pp. 11–12.

---

## 3b.4 [iut:theta_times_mu_link] — Cor. 4.10(iii) part 1, p. 159–160

> "We shall refer to the full poly-isomorphism `†F⊩▶×µ_env ~→ ‡F⊩▶×µ_△`
> as the Θ×µ-link … [cf. the 'Θ-link' of [IUTchI], Corollary 3.7, (i)]."

The **Θ×µ-link** `†HT^{Θ±ellNF} —Θ×µ→ ‡HT^{Θ±ellNF}` is the full
poly-isomorphism:
```
†F⊩▶×µ_env  ~→  ‡F⊩▶×µ_△
```
Functoriality of Def. 4.9(vi) induces the map on Isom-sets:
```
Isom_{F⊩}(†F⊩_env, ‡F⊩_△) → Isom_{F⊩▶×µ}(†F⊩▶×µ_env, ‡F⊩▶×µ_△)
```

**Coric invariant** (Cor. 4.10-iv): `(−)F⊢×µ_△` is preserved by both
Θ×µ- and Θ×µ_gau-links; the induced full poly-iso `†F⊢×µ_△ ~→ ‡F⊢×µ_△`
defines the D-Θ±ellNF-link at base level.

Distinction from `iut:theta_link`:

| | `iut:theta_link` | `iut:theta_times_mu_link` |
|---|---|---|
| Strip level | F⊩ | F⊩▶×µ |
| Units | O× | O^{×µ} = O×/torsion |
| Coric piece | D⊢-strip | F⊢×µ-strip |

Source: IUTchII Cor. 4.10(iii), (iv), pp. 159–160.

---

## 3b.5 [iut:theta_gau_link] — Cor. 4.10(iii) part 2, p. 160

> "We shall refer to the full poly-isomorphism `†F⊩▶×µ_gau ~→ ‡F⊩▶×µ_△`
> as the Θ×µ_gau-link … which may be regarded as being obtained from the
> full poly-isomorphism `†F⊩▶×µ_env ~→ ‡F⊩▶×µ_△` by composition with the
> inverse of the evaluation isomorphism of (ii)."

Value-group transformation effected (Rmk. 4.11.1):
```
q_v  →  {q^{j²}_v}_{1 ≤ j ≤ l*}   (Gaussian distribution / Teichmüller deformation)
```
Units O^{×µ} are coric (preserved); value groups are not.

**Significance for multiradiality** (Rmk. 4.10.2-i, p. 162):
> "it is precisely by thinking of [a further enhanced version of] the Θ×µ_gau-link
> as an object that is constructed as the composite of the Θ×µ-link with the
> operation of Galois evaluation that one may establish the crucial multiradiality
> properties discussed in [IUTchIII], Theorem 3.11."

p-adic Teichmüller analogy (Fig. I.7):
- Θ×µ-link ↔ canonicality via MF∇-objects
- Θ×µ_gau-link ↔ canonicality via crystalline Galois representations

Source: IUTchII Cor. 4.10(iii); Rmk. 4.10.2, 4.10.3, 4.11.1, pp. 160–164.

---

## 3b.6 Frobenius-picture (Cor. 4.10-vi)

Both links yield Frobenius-pictures (oriented graph `⃗Γ` with Z-translation):
```
… →^{Θ×µ}     nHT →^{Θ×µ}     (n+1)HT → …
… →^{Θ×µ_gau} nHT →^{Θ×µ_gau} (n+1)HT → …
```
No adjacent-swap automorphism (same structure as IUTchI Cor. 3.8,
but at finer F⊩▶×µ level).

---

## 3b.7 Forbidden translations

- Do NOT equate `iut:theta_times_mu_link` with `iut:theta_link` (different
  prime-strip levels; F⊩ vs F⊩▶×µ).
- Do NOT claim Θ×µ_gau-link is multiradial alone — requires IUTchIII log-link.
- Do NOT treat the evaluation isomorphism as a ring morphism.
- Do NOT render Gaussian monoids as perfectoid / condensed / prismatic objects.

---

## 3b.8 Sources

- IUTchII, Publ. RIMS **57** (2021) 209–401,
  DOI [10.4171/PRIMS/57-2-1](https://doi.org/10.4171/PRIMS/57-2-1)
  URL: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf>
  — Def. 4.9(vi–viii) pp. 157–158; Cor. 4.10(ii–iv) pp. 159–160;
    Rmk. 4.10.2-3 pp. 161–162; Introduction pp. 11–15.
