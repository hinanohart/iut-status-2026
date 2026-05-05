# [iut:log_link] — SS view
> 3-agent verify pending (SS-side draft).
> Source: Wayback Machine キャッシュ経由取得 (uni-bonn.de 直接到達不可)。
> PDF: 10 pages, 2018, Peter Scholze & Jakob Stix.

---

## How SS describes log-link

SS は §2.1.3「log-links」節 (p.6–7) で `iut:log_link` を明示的に定義・紹介している。
出現ページ: **p.6 (×2), p.7 (×2)** — 計4回。

### p.6 — §2.1.3 の冒頭定義

> "The log-link introduced in [IUTT-3] is based on the following construction for an
> algebraic closure K of a nonarchimedean local field of characteristic 0,
> cf. [IUTT-3, Definition 1.1 (i)]. The logarithm map defines a well-defined surjective map
> log : o×_K → K that turns multiplication into addition."

SS はここで log : o^×µ_K → K の全単射を確認し、これにより Mochizuki が
「乗法を加法に変換する endofunctor `log`」を定義することを説明する。
そして次の結論を付記する:

> "It follows that the endofunctor log is **naturally equivalent to the identity**,
> with the natural equivalence to the identity given by log : log(K) ≅ K."

これが SS の批判の出発点となる重要な観察。

### p.7 — log-link の構造的定義

> "In the case of the log-link, the data is essentially that of π₁(X) acting on k_v
> (for v ranging over the finite places). […] the log-link consists of an isomorphism
> Π₁ ≅ Π₂ and an isomorphism o_{log(K₁)} ≅ o_{K₂} of topological monoids
> that is equivariant for the Π₁ ≅ Π₂-actions."

脚注8でさらに:

> "if one remembers that all Hodge theaters really come from our fixed curve X,
> there is a completely **natural** isomorphism Π₁ = π₁(X) = Π₂ and K₁ ≅ K₂ as
> K₁ = k̄ = K₂, and thus a natural Π₁ ≅ Π₂-equivariant isomorphism log(K₁) ≅ K₁ ≅ K₂.
> Choosing these 'obvious' isomorphisms did **not** result in any problem that would be
> solved by allowing some other (possibly indeterminate) isomorphism."

---

## SS's view on log-shell

`log-shell` は **p.9 に1回のみ**出現。定義節は設けられず、
Cor.3.12 の証明解析の文脈で通過的に言及される:

> "this becomes an identification of concrete Θ-pilot objects and concrete q-pilot objects
> (encoded via their action on **processions of tensor packets of log-shells**),
> and then the inequality follows directly."

SS は log-shell を独立した概念として掘り下げない。
Cor.3.12 Step (xi) の「パイロット対象のエンコード媒体」として名前が出るのみ。

---

## SS's view on log-theta-lattice

`log-theta` は **p.10 参考文献リストに1回**のみ:

> "[IUTT-3] Mochizuki, S., Inter-universal Teichmuller Theory III:
> Canonical Splittings of the **Log-theta-lattice**."

論文タイトルとして言及されるのみ。SS は log-theta-lattice の構造・役割を
本文中で一切議論しない。

---

## Where SS agrees

SS は log-link の構成手順 (対数写像による endofunctor、局所体の代数閉包への適用) を
IUTT-3 に忠実に再現しており、構成の記述自体に異議を唱えていない。
well-definedness (log : o^×µ_K → K が全単射) は肯定的に確認している (p.6)。

---

## Where SS sees no essential content / silently passes over

SS の批判は log-link 自体の定義の誤りではなく、**その「使われ方」**にある。

1. **log-link は恒等と自然同値** — p.6 で明示。Mochizuki が log-link を
   「異なる宇宙を繋ぐ非自明なリンク」として使う根拠が SS には見えない。

2. **log-theta-lattice の深い議論なし** — SS は lattice 構造・
   log-Frobenius 的性質・無限列の収束性について一切言及しない。
   これは SS が「そこに証明の本質がある」と見ていないことを示すが、
   「log-theta-lattice が無意味」と主張しているわけではない。

3. **log-shell の役割未解析** — SS は log-shell が indeterminacy (Ind 1,2,3)
   の文脈でどう機能するかを展開せず、批判はより上流の「R-vector space の
   isomorphism の一貫性」問題に集中する (p.9–10)。

結論: **SS は log-link を Cor.3.12 における核心とは扱わない。**
核心は「Θ-link を越えた pilot object の degree の同一視が
diagram の monodromy j² を生む」点であり、log-link はその前段の記述的整理にとどまる。

---

## Critical caveat

- SS は `iut:log_link` を再定義しない。記述は IUTT-3 の定義に従う。
- SS の批判が log-link 節に集中しないことは、log-link が「正しい」ことを
  含意しない。SS の批判焦点は Θ-link 後の degree 比較 (§2.2, p.9–10) にある。
- Mochizuki 側の反論 (log-theta-lattice の本質的役割) は本ドラフトの scope 外。

---

## Source

- **Primary**: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
  (Wayback Machine 経由取得: https://web.archive.org/web/2024/https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- PDF: 10 pages, 2018
- `iut:log_link` 出現: p.6 (×2), p.7 (×2)
- `iut:log_shell` 出現: p.9 (×1)
- `log-theta-lattice` 出現: p.10 参考文献 (×1)
- `log-volume` 出現: p.10 参考文献 (×1, IUTT-4 タイトルのみ)
