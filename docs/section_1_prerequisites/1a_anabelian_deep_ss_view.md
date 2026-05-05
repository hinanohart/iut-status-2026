# 1a — Anabelian Geometry — Scholze-Stix view
> 3-agent verify pending (SS-side draft).

## How SS describes anabelian (verbatim 全箇所)

**p.5 Theorem 7 導入文 — "striking result":**
> "At this point, it is useful to recall the following striking result of Mochizuki."
Theorem 7 ([Anab3, Theorem 1.9, Corollary 1.10]): strictly Belyi type 曲線 X に対し X ↦ π₁(X) が fully faithful、quasi-inverse explicit に構成可。Once-punctured elliptic curves も strictly Belyi type に該当 (p.5 fn.3)。

**p.5 Remark 9 verbatim (全文):**
> "Anabelian geometry is supposed to be the key to Mochizuki's proof. However, here we see that in the IUTT papers, we are (for the essential part) in a situation where anabelian geometry holds true in the sense that geometry and group theory are equivalent. We could not find the point where it is essential to work with fundamental groups – there are no additional isomorphisms of fundamental groups that do not come from isomorphisms of schemes, precisely because of Mochizuki's theorem."

**p.5 footnote 4 (Remark 9 付随):**
> "Such isomorphisms exist for Galois groups of p-adic fields, but this did not seem to enter the discussion in a critical way."

**p.5 footnote 5 / p.8 §2.1.8 — tempered 言及:**
> fn.5: "…monoid of divisors on tempered coverings of X at places of bad reduction, by means of which Mochizuki encodes the Θ-function."
> p.8: "Mochizuki devises an ingenious algorithm to recover this data very directly from the data of π₁(X) acting on a certain monoid of divisors on tempered coverings of X."

---

## SS's specific anabelian critique

- Mochizuki の anabelian 定理 (Theorem 7) 自体は **valid と認める** ("striking result", p.5)
- しかし Cor.3.12 の essential part では anabelian geometry が成立済 (geometry = group theory 等価) のため、fundamental groups を使うことが **追加等価性を生まない** と主張 (Remark 9)
- p-adic Galois 群の余分な同型は存在するが Cor.3.12 議論に **critical な役割を果たさなかった** (fn.4)

---

## Where SS does NOT critique

- Theorem 7 ([Anab3]) の正しさ: SS PDF で直接批判なし
- tempered coverings による Θ-function encoding: "ingenious algorithm" と評価 (p.8)
- Belyi maps による reduction: §1.2 で SS 自身が採用
- `cuspidalization`, `mono-anabelian` の語: SS PDF **全文に出現なし** (10p, keyword search 確認)

---

## IRI mapping (SS PDF evidence)

| IRI | SS 内記述 | 批判有無 |
|---|---|---|
| `iut:anabelian.absolute_anabelian` | Theorem 7 を "striking result" として引用 (p.5) | なし |
| `iut:anabelian.tempered_rigidity` | fn.5 + p.8 §2.1.8 で "tempered coverings" 言及 | なし ("ingenious") |
| `iut:anabelian.cuspidalization` | 語なし (0 hit) | 言及なし |
| `iut:anabelian.mono_anabelian` | 語なし (0 hit) | 言及なし |
| `iut:anabelian.belyi_cuspidalization` | Belyi maps を reduction tool として使用 (p.2, p.5) | なし |

---

## Critical caveat

SS は anabelian methodology を否定しない。批判対象は Cor.3.12 における **deployment** のみ: 「IUTT の essential part では anabelian が成立済なので fundamental groups の余分な同型が存在しない → anabelian が本質的貢献をしていない」という argument。"anabelian = invalid" の単純化は SS PDF の記述と矛盾する。

---

## Source

- Scholze, P. and Stix, J., *Why abc is still a conjecture* (July 16, 2018).
  `https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf`
  PDF-verified 2026-05-06, pymupdf, 10 pages.
  Local cache: `.../webfetch-1778015625413-l1jnga.pdf`
- 引用: p.5 Theorem 7, Remark 8, Remark 9, fn.3–5; p.8 §2.1.8; p.10 References [Anab3][Belyi]
