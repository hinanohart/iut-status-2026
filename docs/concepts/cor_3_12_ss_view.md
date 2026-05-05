# [iut:Cor.3.12] Corollary 3.12 — Scholze-Stix view
> 3-agent verify pending (SS-side draft).
> Source: SS 2018 PDF verbatim. Knowledge cutoff: July 16, 2018 (paper date).

---

## SS's reading of Cor.3.12

SS の批判は [IUTT-3, Corollary 3.12] の証明 Step (xi) の最終部分に集中する。

> "If one interprets the above discussion in terms of the notation introduced in the statement of
> Corollary 3.12, then one concludes [...] that −|log(q)| ≤ −|log(Θ)| ∈ R."

この不等式を導く論証が SS の objection の対象。SS が問題とするのは「一貫した実数同一視を施すと
j² スカラーが消え、空の不等式しか残らない」という主張である。(SS 2018, p.9–10)

---

## Core SS objection (1 main + 3 sub-claims)

### 1. Main claim (claim:scholze_stix_2018_main)
**一貫した同一視のもとで不等式は空になる。**

> "The conclusion of this discussion is that with consistent identifications of copies of real
> numbers, one must in (1.5) omit the scalars j² that appear, which leads to an **empty
> inequality**." (p.10)

すなわち (1.5) の j² が消えると、式は 0 ≤ d(P) という自明な不等式に帰着し、高さ不等式を導く
情報を持たない。SS は "empty inequality" と呼ぶ。

---

### 2. Sub-claim 1 (claim:scholze_stix_2018_sub_1): Hodge theater の圏同値

Hodge theater を選ぶことは、X に abstractly isomorphic な once-punctured 楕円曲線を選ぶことと
圏同値である。

> "The natural functor from the category whose only object is X and whose morphisms are the
> automorphisms of X [...] to the category of Θ±ellNF-Hodge theaters is an **equivalence of
> categories**, as follows by combining [IUTT-1, Corollary 6.12 (i), ...]." (p.6)

この帰結として、「異なる Hodge theaters」は本質的に X の同一コピーに過ぎず、θ-link が要求する
形での「真に独立した」Hodge theaters の存在は自明でない。(p.6)

---

### 3. Sub-claim 2 (claim:scholze_stix_2018_sub_2): anabelian 幾何は Cor.3.12 で本質的でない

> "Remark 9. Anabelian geometry is supposed to be the key to Mochizuki's proof. However,
> here we see that in the IUTT papers, we are (for the essential part) in a situation where
> anabelian geometry holds true in the sense that geometry and group theory are equivalent.
> We could **not find the point where it is essential to work with fundamental groups** –
> there are no additional isomorphisms of fundamental groups that do not come from
> isomorphisms of schemes, precisely because of Mochizuki's theorem." (p.5, Remark 9)

SS は Mochizuki 自身の anabelian 定理 (Theorem 7 / [Anab3, Theorem 1.9]) によって、幾何と
群論が等価であるゆえに、基本群のみで作業する必然性を証明の核心部で見出せなかった、と述べる。
SS は anabelian 定理そのものは肯定している点に注意。

---

### 4. Sub-claim 3 (claim:scholze_stix_2018_sub_3): π₁ と geometry が equivalent → IUT 操作が自明化

Global realiﬁed Frobenioid が「ordered 1-dimensional R-vector spaces の圏」と同値であること、
および F^⊩×µ-prime strip が各 v での標準的な対象と同値であることから、

> "The category of global realiﬁed Frobenioids is equivalent to the category of ordered
> 1-dimensional R-vector spaces." (p.7)

かつ canonical trivialization γ_can によって R⊙ が常に自然に自明化される。この自明性が
θ-link を「同じ対象の別名付け」に還元し、j² スカラーの導入を inconsistency として顕在化させる。

---

## SS's specific technical objection (p.9–10)

### γ_can による canonical trivialization と j² omission

SS は以下のダイアグラムを Kyoto での議論中に描いた:

```
R⊙,Θ  —[Θ-link ≅]—→  R⊙,q
  ↑                        ↑
(R⊙c,Θⱼ)ⱼ              R⊙c,q
  ↓                        ↓
  RΘ      ——[=]——→        Rq
```

> "There is one consistent choice of isomorphisms given by using the natural isomorphisms
> R⊙,Θ ≅ R⊙,q ≅ R coming from the observation that the global realiﬁed Frobenioids coming
> from F^⊩×µ-prime strips are always **canonically trivial** using the various γ_can." (p.10)

しかしこの consistent な選択のもとでは、abstract Θ-pilot object は Θ-divisor の arithmetic
degree を encode しない。

> "However, we saw that with these isomorphisms, the abstract Θ-pilot object does not encode
> the arithmetic degree of the Θ-divisor." (p.10)

望月はダイアグラムの左辺に j² スカラーを導入しようとするが、

> "it is clear that this will result in the whole diagram having monodromy j², i.e. being
> **inconsistent**." (p.10)

### Footnote 12: Theorem 3.11 は trivial になる

> "We pause to observe that with the simpliﬁcations outlined above, such as identifying
> identical copies of objects along the identity, the critical [IUTT-3, Theorem 3.11] does
> **not become false, but trivial**." (p.9, footnote 12)

Theorem 3.11 (multiradial algorithm) は false でなく trivial になる、という指摘。
これは証明の誤りの性質を characterize する重要な言明である。

---

## SS's response to Mochizuki's day-5 reply

5日目に望月は「indeterminacy による blurring でダイアグラムが commute する」と説明した。
SS の評価:

> "it seems to us that this statement means that the **blurring must be by a factor of at
> least O(ℓ²)** rendering the inequality thus obtained useless." (p.10)

すなわち、indeterminacy を用いてダイアグラムを commute させようとすれば、誤差が O(ℓ²) 以上に
なり、元の高さ不等式が意味を失う。

---

## What SS does NOT claim

これらは SS が **否定していない** 点であり、SS の批判の射程を正確に理解するために重要である。

- **anabelian 定理 (Theorem 7) 自体は肯定する。** SS は Mochizuki の anabelian 定理を
  証明の前提として正しく受け入れ、むしろその定理を根拠として「anabelian 幾何が essential
  でない」と論じる。(p.5)
- **θ-link の well-definedness 自体は否定しない。** SS は θ-link が定義されること、
  abstract pilot object の同一視が行われることを認める。問題は「その同一視が j² スカラーと
  両立しない」点にある。(p.9)
- **Frobenioid 一般論を否定しない。** Global realiﬁed Frobenioid が elementary であると
  論じるが (p.7)、それは Frobenioid 理論の一般的誤りを主張するものでない。
- **望月の数学的能力や誠実性を疑わない。** SS はむしろ議論の constructive な性格と
  望月の hospitality に謝辞を述べている。(p.1)
- **Cor.3.12 の statement (主張命題) を否定しない。** SS の批判は **証明の Step (xi) の
  論証** に限定される。命題が真か偽かは SS 2018 では明言されていない。

---

## Source

- **URL**: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- **Date**: July 16, 2018
- **Page reference map**:
  - p.1: 結論宣言 ("there is no proof")
  - p.3–4: (1.5) vs (1.6) — j² あり/なしの対比、高さ不等式への帰結
  - p.5, Remark 9: anabelian geometry の非本質性 (verbatim 引用)
  - p.6: Hodge theater 圏同値 ([IUTT-1, Cor.6.12(i)] 他)
  - p.7: Global realiﬁed Frobenioid の elementary 性、γ_can の定義
  - p.8: F^⊩×µ-prime strip、concrete pilot objects (q, Θ)
  - p.9: θ-link、Section 2.2 開始、footnote 12 (Theorem 3.11 trivial)
  - p.10: ダイアグラム、canonical trivialization、j² inconsistency、O(ℓ²) blurring
