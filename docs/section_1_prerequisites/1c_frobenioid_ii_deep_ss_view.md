# 1c — Frobenioid II (deep) — Scholze-Stix view
> SS-side draft. PDF-verified 2026-05-06 via pymupdf full-text extraction.

## Source
- SS 2018 (Scholze–Stix, "Why abc is still a conjecture"), p.7–8.
  PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- 検索対象: [Frd2] / "Frobenioid II" / "poly-Frobenioid" / "archimedean Frobenioid" /
  "non-archimedean Frobenioid" / "angular region" — 全文 PDF (pymupdf) で確認。

---

## SS p.7 verbatim — [Frd2] の言及 (全 occurrence)

SS p.7, §2.1.4 冒頭:

> "Mochizuki introduces the **difficult notion of a Frobenioid** in his papers [Frd1], **[Frd2]**.
> However, the notion of a global realified Frobenioid is very elementary,
> cf. [IUTT-1, Example 3.5]."

これが SS 全文における [Frd2] の **実質的な言及箇所**。
続く §2.1.4 本文は [Frd2] (Poly-Frobenioids) の内容には一切踏み込まず、
global realified Frobenioid の elementary な reformulation のみを展開する。

参考文献リストでの出現 (p.最終ページ):

> "[Frd2] Mochizuki, S., The Geometry of Frobenioids II: Poly-Frobenioids."

---

## `iut:global_realified_frobenioid` — SS の扱い

SS p.7, §2.1.4 — reformulation (verbatim):

> "In this case, it simply amounts to a collection of **ordered 1-dimensional R-vector spaces
> R_v** parametrized by the places v of k, together with a subspace D₀ ⊂ ⊕_v R_v
> of codimension 1 such that there is an ordered isomorphism R_v ≅ R under which D₀
> is the kernel of the map ⊕_v R_v ≅ ⊕_v R → R given by sending 1 to log(N(v))
> at finite places, and 2π at infinite places."

> "These considerations show that the **category of global realified Frobenioids is equivalent
> to the category of ordered 1-dimensional R-vector spaces**."

SS の立場: `iut:global_realified_frobenioid` は Frd II の poly-Frobenioid 一般論を
経由せずに elementary に記述できる。批判は定義の無効化ではなく
「Cor.3.12 の文脈では過剰装備」という主張。

---

## `iut:archimedean_frobenioid_component` — SS の扱い

**SS p.7 全文に "archimedean Frobenioid" の出現なし (pymupdf 全文検索で NOT FOUND)。**

p.7 §2.1.4 で archimedean place への言及は以下のみ:

> "...given by sending 1 to log(N(v)) at finite places, and **2π at infinite places**."

これは global realified Frobenioid の D₀ 定義の一部であり、
archimedean component を独立した Frobenioid 対象として論じるものではない。

**判定: SS の scope 外。** archimedean Frobenioid component への批判・言及なし。

---

## `iut:non_arch_frobenioid_component` — SS の扱い

**SS p.7–p.8 全文に "non-archimedean Frobenioid" の出現なし (pymupdf 全文検索で NOT FOUND)。**

p.7–8 で non-archimedean place の扱いは F^{⊩×µ}-prime strip の文脈のみ:

> "at nonarchimedean places, given by the pair G_v ↷ o^{×µ}_{k̄_v} × o_{k̄_v}
> where o_{k̄_v} ≃ N with trivial G_v-action."

これは F^{⊩×µ}-prime strip の構造記述であり、
non-archimedean Frobenioid component としての定式化ではない。

**判定: SS の scope 外。** non-arch Frobenioid component への批判・言及なし。

---

## `iut:angular_region` — SS での出現

**SS 全文 (PDF 全ページ) に "angular region" の出現なし (pymupdf 全文検索で NOT FOUND)。**

**判定: [CLAIMED_BY: Mochizuki]。** angular region は Mochizuki 側の概念であり、
SS はこの概念に触れない。SS の反論対象ではなく、SS 側からの検証も存在しない。

---

## まとめ: SS p.7 における Frobenioid II 関連の全 occurrence

| 検索語 | p.7 出現 | 全文出現 | 備考 |
|---|---|---|---|
| `[Frd2]` | 1 回 | 2 回 (本文 + 参考文献) | "difficult notion" の括弧内のみ |
| "Frobenioid II" | 0 | 0 | 文字列としては出現しない |
| "poly-Frobenioid" | 0 | 1 回 | 参考文献リストのみ |
| "archimedean Frobenioid" | 0 | 0 | scope 外 |
| "non-archimedean Frobenioid" | 0 | 0 | scope 外 |
| "angular region" | 0 | 0 | [CLAIMED_BY: Mochizuki] |
| "global realified Frobenioid" | 複数 | 複数 | SS 批判の中心概念 |

SS の Frobenioid II への態度は単一:
[Frd2] を "difficult notion" の引用元として挙げるが内容に踏み込まず、
global realified Frobenioid の elementary 等価性 (ordered 1-dim R-vec) に議論を集中させる。
Poly-Frobenioid / archimedean component / non-arch component / angular region は
**いずれも SS の批判対象外**。
