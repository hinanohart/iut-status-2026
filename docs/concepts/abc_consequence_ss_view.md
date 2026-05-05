# [iut:height_inequality + iut:abc_conjecture] abc consequence — SS view
> 3-agent verify pending (SS-side draft).
> Source: SS 2018 PDF verbatim. Knowledge cutoff: July 16, 2018 (paper date).

---

## SS's reading of the IUT-to-abc chain

SS において abc 帰結は Cor.3.12 の downstream consequence として扱われる。
chain: Cor.3.12 → inequality (1.4) → Claim 6 ([IUTT-4, Thm. 1.10]) → Vojta 不等式 → abc。

一貫した実数同一視のもとで (1.5) の j² が消えると (1.6) になり、

> "Starting from the corrected inequality we obtain **0 ⪅ d(P)**
> which is essentially **free of content**." (SS 2018, p.4)

高さ上界が出ない以上、後続 steps も `iut:diophantine_inequality` を導けない。

> "with consistent identifications of copies of real numbers, one must in (1.5) omit the
> scalars j² that appear, which leads to an **empty inequality**." (SS 2018, p.10)

Mochizuki の day-5 reply (indeterminacy blurring) についても:

> "the blurring must be by a factor of at least O(ℓ²) rendering the inequality
> thus obtained **useless**." (SS 2018, p.10)

---

## Where SS agrees

- `iut:abc_conjecture` の statement (Masser-Oesterlé 1985) は valid な open conjecture。(p.1–2)
- Claim 6 / [IUTT-4, Thm. 1.10] の statement 形式は valid; 前段 Cor.3.12 が成立するなら
  Vojta 不等式に繋がる。SS は IUTchIV 内部の証明 steps を独立評価しない。

---

## Where SS disagrees

- Cor.3.12 が "empty inequality" → `iut:height_inequality` は実質的内容なし。(p.4, p.10)
- indeterminacy blurring で diagram を commute させるには O(ℓ²) 誤差が必要 → useless。(p.10)

---

## SS does NOT claim

- abc conjecture が偽であるとは主張しない (依然 open conjecture として扱う)。
- IUTchIV §2–3 の technical steps が独立に誤っているとは主張しない。
- Mochizuki の `iut:diophantine_inequality` の statement が wrong であるとは主張しない。

---

## Source

- https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- p.4: (1.5) vs (1.6), "free of content"
- p.10 final paragraph: "empty inequality", O(ℓ²) blurring
