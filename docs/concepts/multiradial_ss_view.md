# [iut:multiradial_algorithm + iut:Ind1/2/3] — SS view
> 3-agent verify pending (SS-side draft).

## How SS describes multiradial / indeterminacies

SS 2018 では "multiradial" という語は **1箇所のみ** 出現する。

> "it is argued in [IUTT-3, Corollary 3.12] that the **multiradial algorithm**
> [IUTT-3, Theorem 3.11] implies that up to certain indeterminacies,
> e.g. **(Ind 1,2,3)** (without which the conclusion would be obviously false),
> this becomes an identification of concrete Θ-pilot objects and concrete
> q-pilot objects …"
>
> — SS 2018, p.9 (char offset ~28367)

"indeterminacies" は **2箇所**出現:
1. 上記 p.9 — Ind 1,2,3 の列挙箇所
2. p.10 末尾 — 「最終日、望月はある indeterminacies による "blurring" で図式が可換になると主張した」箇所

"Ind1/Ind2/Ind3" の個別技術評価: **出現しない**。
SS は Ind 1, Ind 2, Ind 3 それぞれの内容に立ち入らず、Cor.3.12 全体の有効性を問う。

- Reference: SS 2018, p.9–10

## SS's central objection

SS の核心的反論は **j² モノドロミー** に帰着する。

> "Thus, Mochizuki wanted to introduce scalars of j² somewhere on the left
> part of this diagram (which strictly speaking leads to inconsistencies,
> i.e. **monodromy**, on the left part of the diagram alone …). However,
> it is clear that this will result in the whole diagram having
> **monodromy j²**, i.e. being inconsistent."
>
> — SS 2018, p.10

> "with consistent identifications of copies of real numbers, one must in
> (1.5) omit the scalars j² that appear, which **leads to an empty
> inequality**."
>
> — SS 2018, p.10

論理構造:
- (1.5) に j² を残すと図式全体がモノドロミーを持ち矛盾
- j² を除くと (1.5) は `−|log(Θ)| ≈ −|log(Θ)|` という同義反復になり、非自明な下界を与えない

Theorem 3.11 (multiradial algorithm の主文) については脚注 12 で言及:

> "with the simplifications outlined above … the critical [IUTT-3,
> Theorem 3.11] does not become false, but **trivial**."
>
> — SS 2018, p.10 fn.12

## Where SS agrees

- multiradial algorithm の **statement レベルの well-definedness** は否定していない。
- Theorem 3.11 の主張が **偽** だとは言わない — "trivial" と評する。

## Where SS sees no essential content

- Ind 1,2,3 の "blurring" が j² を吸収できると望月が主張した点に対し、
  SS は「そのためには blurring が O(ℓ²) 以上の factor を持つ必要があり、
  得られる不等式は **useless** になる」と反論する (p.10)。
- すなわち: indeterminacies が十分小さければ矛盾、十分大きければ無意味 — という二律背反を SS は主張する。

## Critical caveat

- SS は Ind1/Ind2/Ind3 を **独立に再定義・再評価しない**。
- SS の立場: 「multiradial algorithm および indeterminacies の役割が
  Cor.3.12 において非自明な不等式を導くために **不十分**」。
- Mochizuki 側の応答 (Mochizuki 2018 Reply 等) はこの draft の scope 外。

## Source

- SS 2018, p.9–10 主
- URL: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- 取得日: 2026-05-06、全文 33,389 chars (pdfminer 抽出)
