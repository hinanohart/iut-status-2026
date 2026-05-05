# Section 3a — Θ-link deep dive: SS-side view
> IRI: `iut:theta_link`
> Source-locked: SS 2018 §2.1.9 p.9 (pymupdf verbatim 2026-05-06)
> 3-agent verify: pending

## IRIs flat
`iut:theta_link` · `iut:HodgeTheater` · `iut:F_modulus_prime_strip` · `claim:scholze_stix_2018_main`

---

## SS 2018 p.9 verbatim — all occurrences

**Q1** definition (§2.1.9 s.1):
> "The Θ-link between two Hodge theaters HT1 and HT2 is the **(full poly-)isomorphism**
> between the F⊩×µ-prime strip F⊩×µ_{Θ,1} constructed from the Θ-pilot object in HT1 and
> the F⊩×µ-prime strip F⊩×µ_{q,2} constructed from the q-pilot object in HT2."

**Q2** identifies abstract / forgets concrete (§2.1.9 s.2–3):
> "the choice of such an isomorphism **identifies the corresponding abstract pilot objects**.
> However, the Θ-link **forgets** about the concrete embeddings of q̃_v into o_{k̄_v} and
> Θ_v ~ (q^{j²}_v)_{j=1,...,ℓ⋇} into o_{k̄_v}."

**Q3** canonical choice — the core claim (§2.1.9 s.4–6):
> "The F⊩×µ-prime strips are given by data of the form **G_v ⟲ o^{×µ}_{k̄_v} × N** on both
> sides (at finite places), and **this data is canonically the same on both sides**. It is
> simply the name of the generator of the monoid N that appears that is called Θ respectively q."

**Q4** footnote 12, p.9 (on IUTT-3 Theorem 3.11):
> "with the simplifications outlined above, such as identifying identical copies of objects
> along the identity, the critical [IUTT-3, Theorem 3.11] **does not become false, but trivial**."

Source: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>

---

## SS argument structure (p.9)

```
[Q1] Θ-link = full poly-iso of F⊩×µ-prime strips       ← both sides agree
[Q2] link: abstract pilots identified; concrete forgot   ← both sides agree
[Q3] strip data G_v ⟲ o^{×µ} × N canonically same
     → only generator NAME differs (Θ vs q)              ← SS claim
[Q4] ∴ canonical id applied → Thm 3.11 trivial           ← SS conclusion
[p.10 §2.2] ∴ j² must be omitted → empty inequality     ← downstream
```

**核心批判:** 両側の F⊩×µ-prime strip データは "canonically the same" であり、Θ-link は
N の生成元の名前替えに過ぎない。これを一貫適用すると Cor.3.12 の核不等式が空になる。

**Frobenius-picture / alien copies:** SS p.9 では直接議論なし。Mochizuki の反論
(`claim:mochizuki_2018_response`) は、Q3 の canonical identification ステップ自体が
inter-universal 内容を落とす illegitimate 同一視だという立場を取る。

---

## Cross-reference

- Agreed structure: IUTchI Cor. 3.7 (i) p.88 (DOI 10.4171/PRIMS/57-1-1) — F⊩版定義;
  IUTchII Cor. 4.10 (iii) / Def. 4.9 (vii) — F⊩×µ 精緻化 (SS はこの層で議論).
- Existing file: `docs/concepts/theta_link_ss_view.md` (概要); `docs/section_3_theta_link.md` §3.2–3.3 (disputed encoding).
