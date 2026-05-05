# 1d — etale theta function (deep dive, mochizuki-side)
> 3-agent verify pending (mochizuki-side draft).
> PDF-verified 2026-05-06 via pymupdf full-text extraction (EtTh, 112 pp.).

---

## 1d.1 etale theta class (`iut:etale_theta_class`)

- **Reference**: EtTh §1, Prop. 1.3 (PDF p.18–19); "standard type" defined at Def. 1.9 (PDF p.27).
  Def. 2.7 (PDF p.38) defines "standard type" for *l-th roots* of the etale theta class — distinct from Prop. 1.3.

**Prop. 1.3 statement (paraphrase)**:
Let `X^log` be a smooth log curve of type (1,1) over a nonarchimedean mixed-characteristic local field `K`.
The difference between two natural actions of `Π^tp_Y` — one from Prop. 1.1(ii), one from the theta trivialization of Lem. 1.2 — on constant multiples of `τ_N` determines a cohomology class

```
η^Θ_N ∈ H¹(Π^tp_Y, (½·ℤ/Nℤ)(1)) ≅ H¹(Π^tp_Y, Δ_Θ ⊗ (½·ℤ/Nℤ))
```

Taking `N → ∞` yields a class `O^×_{K/K̈} · η^Θ ∈ H¹(Π^tp_Y, ½Δ_Θ)`,
whose restriction to `Ȳ` arises from classes `O^×_{K̈} · η̈^Θ ∈ H¹(Π^tp_{Ȳ}, Δ_Θ)` "without denominators".
Mochizuki refers to any element of these sets as **"the etale theta class"**.

**Def. 1.9 / Def. 2.7 distinction** (PDF p.27, p.38):
- Def. 1.9: "standard type" for `η̈^Θ_ℤ` — the unique `O^×_K`-value of maximal order among standard values `{η̈^Θ_ℤ|_τ, η̈^Θ_ℤ|_{τ−1}}` equals `±1`.
- Def. 2.7: extends "standard type" terminology to *l-th root* orbits `η̈^Θ_{l·ℤ}`, `η̈^Θ_{l·ℤ×μ₂}`, etc., after the degree-`l` covering `Ȳ^log → Ȳ^log` is introduced in §2.
  **These are distinct definitions**: Def. 2.7 presupposes Def. 1.9 and the §2 covering setup.

**Definition locator**: Prop. 1.3 = PDF p.18–19; Def. 1.9 = PDF p.27; Def. 2.7 = PDF p.38.

---

## 1d.2 absolute anabelian theta (`iut:absolute_anabelian_theta`)

- **Reference**: EtTh Thm. 1.10 (PDF p.27–28), title: "Constant Multiple Rigidity of the Étale Theta Function".

**Thm. 1.10 statement (paraphrase)**:
For `□ = α, β`, let `Ċ^log_□` be a smooth log curve of type `(1, μ₂)^±` over a finite extension `K_□` of `ℚ_p` containing `√−1`.
Let `γ : Π^tp_{Ċ_α} →̃ Π^tp_{Ċ_β}` be an isomorphism of topological groups such that the induced isomorphism on `Π^tp_X` maps `η̈^Θ_ℤ_α → η̈^Θ_ℤ_β`. Then:

1. `γ` preserves the property that `η̈^Θ_ℤ_□` be of standard type — a property that determines this collection of classes **up to multiplication by ±1**.
2. The isomorphism `K^×_α →̃ K^×_β` induced by (any) `γ` preserves the standard sets of values of `η̈^Θ_ℤ_□`.
3. If `η̈^Θ_ℤ_□` is of standard type and the residue characteristic of `K_□` is odd, then `η̈^Θ_ℤ_□` determines a `{±1}`-structure on the `(K^×_□)^∧`-torsor at the unique cusp of `Ċ^log_□`, compatible with the canonical integral structure and preserved by (arbitrary) `γ`.

**Key feature**: rigidity holds for the *full* tempered fundamental group `Π^tp_Ċ`, not merely for the theta quotient `(Π^tp_C)^Θ` — see Rem. 1.10.3 (PDF p.28–29).

**Definition locator**: Thm. 1.10 = PDF p.27–28.

---

## 1d.3 Frobenioid-theoretic theta (`iut:frobenioid_theoretic_theta`)

- **Reference**: EtTh Thm. 5.10 (PDF p.97–98), title: "Category-theoreticity of Frobenioid-theoretic Theta Environments".

**Thm. 5.10 statement (paraphrase)**:
In the notation of Thm. 5.6, suppose `A` arises from `X^log`; let `Ψ : C →̃ C` be a self-equivalence of the tempered Frobenioid. Write:
- `s^⊓_N, s^⊔_N : A_N → B_N` = pair of base-equivalent morphisms (N-th root of a right fraction-pair of an l-th root of `Θ̈`);
- `E_N ⊆ Aut_C(B_N)` = subgroup as defined preceding Lem. 5.8;
- `E^Π_N = E_N ×_{Im(Π^tp_Y)} Π^tp_Y`.

Then (selecting assertion (iii), the main categorical rigidity claim):
> The operation of applying `Ψ` followed by conjugation by `β` preserves the `Aut_C(B_N)`-orbit of `ε : E^Π_N → Aut_C(B_N)`, **in a fashion compatible with the mono-theta environment structure** on `E^Π_N` involving `s^⊔-Π_N`. More precisely, there exists a commutative diagram
>
> ```
> E^Π_N  —γ→  E^Π_N
>   |ε            |κ∘ε
> Aut_C(B_N) —Ψ_Aut→ Aut_C(B_N)
> ```
>
> where `κ` is an inner automorphism and `γ` is an automorphism of **mono-theta environments**.

Rem. 5.10.1 (PDF p.100) interprets this: "a mono-theta environment may be 'extracted' from the tempered Frobenioids in a purely category-theoretic fashion."

**Definition locator**: Thm. 5.10 = PDF p.97–98; Lem. 5.9 setup = PDF p.96.

---

## How these support IUT

- `iut:etale_theta_class` (Prop. 1.3) supplies the Kummer class `η̈^Θ` as the fundamental cohomological object encoding the theta function of a Tate curve.
- `iut:absolute_anabelian_theta` (Thm. 1.10) establishes that `η̈^Θ` is **rigidly determined** (up to `±1`) by the topological group `Π^tp_Ċ` alone — a prerequisite for treating it as a "group-theoretic" object in IUTchI–II.
- `iut:frobenioid_theoretic_theta` (Thm. 5.10) establishes that the **mono-theta environment** (Def. 2.13) — the common core of the etale-theoretic and Frobenioid-theoretic approaches — can be extracted category-theoretically from a tempered Frobenioid.
- In **IUTchII §1**, the theta-pilot object is constructed via this mono-theta environment; the three rigidity properties (cyclotomic, discrete, constant-multiple — Cor. 2.19) are essential for the Θ-link to carry well-defined arithmetic data.
- In **IUTchIII Cor. 3.12**, multiradiality of the theta monoids relies on constant-multiple rigidity (Cor. 2.19(iii) + Thm. 5.10(iii)) to ensure independence under `Aut(Π^tp)` indeterminacies.

---

## Forbidden translations

- "Def. 2.7 = definition of etale theta class" — **wrong**: Def. 2.7 defines "standard type" for l-th root orbits in §2; the etale theta class itself is Prop. 1.3.
- "Thm. 1.10 = anabelian reconstruction of theta" — more precisely, it establishes *constant multiple rigidity*, not full reconstruction (which is Thm. 1.6).
- "mono-theta environment = bi-theta environment" — the mono-theta environment (Def. 2.13(ii)) omits the algebraic section `s^alg`; the bi-theta environment (Def. 2.13(iii)) includes it. Discrete rigidity holds for mono- but **fails** for bi- (cf. Cor. 2.16, Rem. 2.16.1).

---

## Source

- **EtTh**: Mochizuki, "The Étale Theta Function and its Frobenioid-theoretic Manifestations" (Dec. 2008, 112 pp.).
  URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf
- **IUTchII §1**: Mochizuki, "Inter-universal Teichmüller Theory II" — theta-pilot construction.
  URL: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf
