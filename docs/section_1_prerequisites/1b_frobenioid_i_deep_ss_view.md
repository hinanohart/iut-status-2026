# 1b — Frobenioid I — Scholze-Stix view
> 3-agent verify pending (SS-side draft).

## How SS describes Frobenioid (verbatim 全箇所)

**SS p.7, §2.1.4 "Global realiﬁed Frobenioids" — 冒頭 2文 (PDF-verified 2026-05-06):**

> "Mochizuki introduces the **difﬁcult notion of a Frobenioid** in his papers [Frd1], [Frd2].
> However, the notion of a **global realiﬁed Frobenioid is very elementary**, cf. [IUTT-1, Example 3.5]."

**SS p.7, §2.1.4 — 圏同値の結論:**

> "These considerations show that the **category of global realiﬁed Frobenioids is equivalent
> to the category of ordered 1-dimensional R-vector spaces**."

**SS p.8, §2.1.5 — trivialized Frobenioid への言及:**

> "the forgetful functor from F^{⊩×µ}-prime strips to global realiﬁed Frobenioids factors over
> the category of **trivialized global realiﬁed Frobenioids**"

**SS p.10 — Cor.3.12 proof への再言及 (footnote なし):**

> "using the natural isomorphisms R⊙,Θ ∼= R⊙,q ∼= R coming from the observation that the
> **global realiﬁed Frobenioids coming from F^{⊩×µ}-prime strips are always canonically trivial**
> using the various γ_can."

SS p.7–10 において「Frobenioid」の出現は上記 4 箇所のみ。
p.10 footnote に Frobenioid 言及なし (PDF 全文確認済み)。

---

## SS's specific Frobenioid critique

1. `iut:frobenioid_axioms` (Frd I/II の一般論): SS は "difﬁcult notion" と認め、**無効と主張しない**。
2. `iut:base_category_of_Frobenioid` / `iut:degree_function` / `iut:factorization_theorem`:
   SS は p.7–10 で一切言及せず — **definitional 内容への反論なし**。
3. SS の主張は単一: Cor.3.12 で実際に使われる **global realiﬁed Frobenioid** は
   "very elementary" であり、一般論を展開する必要はない。

---

## SS's reformulation (p.7 verbatim, §2.1.4)

global realiﬁed Frobenioid の具体的内容として SS が与える記述:

- 数体 k の place v で添字付けられた ordered 1-dim R-vector spaces R_v の族。
- codimension-1 部分空間 D₀ ⊂ ⊕_v R_v (有限 place で log N(v)、無限 place で 2π の kernel)。
- 商 R⊙ := (⊕_v R_v)/D₀ は任意の v に対し R_v と ordered isomorphic。
- **結論**: global realiﬁed Frobenioid の圏 ≅ ordered 1-dim R-vector spaces の圏。

この reformulation は `iut:degree_function` の具体化に相当するが、
SS はその名称を使わず、一般公理系 (Frd I Def.1.3) に踏み込まない。

---

## Where SS does NOT critique

| IRI | SS の態度 |
|---|---|
| `iut:frobenioid_axioms` | "difﬁcult" と認めるのみ。無効化主張なし。 |
| `iut:factorization_theorem` | p.7–10 で言及なし。批判なし。 |
| `iut:base_category_of_Frobenioid` | 言及なし。批判なし。 |
| `iut:degree_function` | 間接的に具体化するが、公理的定義には反論なし。 |

SS critique の対象は **Cor.3.12 における deployment** のみ:
global realiﬁed Frobenioid が elementary であるにもかかわらず、
scalings (j²) の inconsistency が inequality を空にする、という主張。

---

## Critical caveat

- 「SS は Frobenioid を invalid と主張した」は **誤読**。
- SS は「Frd I/II の一般論 is difﬁcult」を認めた上で、
  「Cor.3.12 で使われる部分は elementary に言い換えられる」と argue。
- Mochizuki 側の反論: global realiﬁed Frobenioid が elementary であることは争わないが、
  Θ-link の multiradial algorithm において一般 Frobenioid 理論の構造が essential との立場
  (→ 3-agent verify で要確認)。

---

## Source

- SS 2018 (Scholze–Stix, "Why abc is still a conjecture"), p.7–10.
  PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
  (PDF-verified 2026-05-06 via pymupdf full-text extraction)
- 引用 [Frd1]: Mochizuki, *The Geometry of Frobenioids I: The General Theory.*
- 引用 [Frd2]: Mochizuki, *The Geometry of Frobenioids II: Poly-Frobenioids.*
