# 1e — Mono-Theta Environment (deep) — Scholze-Stix view
> SS-side draft. PDF full-text extraction via pymupdf (2026-05-06).
> IRI flat: `iut:mono_theta_cyclotomic_rigidity` / `iut:mono_theta_discrete_rigidity` /
> `iut:mono_theta_constant_multiple_rigidity`

---

## 検索対象 occurrence 表 (SS 2018 全文)

| 検索語 | 出現数 | 箇所 |
|---|---|---|
| "mono-theta" / "mono theta" | 0 | NOT FOUND |
| "EtTh" | 0 | NOT FOUND |
| "cyclotomic" | 0 | NOT FOUND |
| "discrete" | 0 | NOT FOUND |
| "constant multiple" | 0 | NOT FOUND |
| "rigidity" | 2 | p.6 §2.1.2 のみ ("non-rigidity of the unit group portion") |
| "tempered" | 2 | fn.5 (p.5) + §2.1.8 (p.8) |
| "ingenious" | 1 | §2.1.8 (p.8) |
| "Cor. 2.19" / "Corollary 2.19" | 0 | NOT FOUND |

---

## "rigidity" の実際の用法 — p.6 §2.1.2

SS が "rigidity" という語を使う唯一の箇所は、mono-theta 環境の 3 rigidities
(cyclotomic / discrete / constant_multiple) とは **無関係**。

**SS p.6, §2.1.2 verbatim:**

> "We note that the monoid o×_{k̄v} does not have this rigidity property: In this case,
> the pair (π₁(X) ↷ o×_{k̄v}) admits extra automorphisms given by the action of Ẑ× on
> o×_{k̄v}. This is the 'non-rigidity of the unit group portion'."

文脈: SS は「k̄× に作用する Ẑ× のうち ±1 以外は k̄× を保たない → k̄× は rigidity を持つ
(up to sign)」と説明した直後に、o×_{k̄v} にはその rigidity がない、と述べている。
これは EtTh の 3 rigidities とは別概念であり、**SS は EtTh の rigidity 体系
(Mochizuki [EtTh] Cor.2.19 / Thm.1.10 系) を用語レベルで一切参照しない**。

---

## "tempered" の実際の用法

**fn.5 (p.5 §2.1.2, footnote):**

> "There is one notable more interesting case related to the monoid of divisors on
> **tempered** coverings of X at places of bad reduction, by means of which Mochizuki
> encodes the Θ-function."

**§2.1.8 (p.8):**

> "Mochizuki devises an **ingenious** algorithm to recover this data very directly from
> the data of π₁(X) acting on a certain monoid of divisors on **tempered** coverings
> of X."

両箇所とも "tempered" は「tempered coverings of X」という位相的対象への言及に
とどまり、mono-theta 環境の理論的 apparatus (tempered fundamental group・
log-meromorphic continuation 等) には踏み込まない。

---

## "ingenious" が指す内容の特定

"ingenious" は §2.1.8 でただ 1 箇所出現し、以下を指す:

> q^{j²}_v (j = 1, …, ℓ⋇) を、tempered coverings 上の divisors の monoid に
> π₁(X) が作用するデータから **直接** 復元する Mochizuki のアルゴリズム。

これは EtTh Thm.1.10 が証明する「étale theta function の group-theoretic
reconstruction」に対応すると解釈できる。ただし SS は [EtTh] を引用せず、
アルゴリズムの correctness を "ingenious" と認めた上で、**その結果物 (q^{j²}_v
の値) を F⊩×µ-prime strip に抽象化した後の操作** に批判を向ける。

fn.11 (§2.1.8 直後):
> "There is an issue here that this is not one object but ℓ⋇ many. This can be
> resolved in a number of ways, e.g. by passing to a 'diagonal' copy; or more
> concretely by forming averages when one extracts numbers such as arithmetic degrees."

fn.11 は multiplicity (ℓ⋇ 個の j) の技術的問題を認知し、averaging による解決を
SS 自身が示唆している。mono-theta 環境の rigidities への反論ではない。

---

## 3 rigidities への SS の態度 (個別判定)

### `iut:mono_theta_cyclotomic_rigidity`

- **SS 直接言及**: なし ("cyclotomic" 全文 NOT FOUND)
- **間接的関連**: なし。
- **判定**: SS の scope 外。cyclotomic rigidity (EtTh Thm.1.10 の核心) は
  SS が "ingenious" と呼ぶアルゴリズムを支える formalism だが、SS はその
  正否を評価しない。[CLAIMED_BY: Mochizuki]

### `iut:mono_theta_discrete_rigidity`

- **SS 直接言及**: なし ("discrete" 全文 NOT FOUND)
- **判定**: SS の scope 外。[CLAIMED_BY: Mochizuki]

### `iut:mono_theta_constant_multiple_rigidity`

- **SS 直接言及**: なし ("constant multiple" 全文 NOT FOUND)
- **判定**: SS の scope 外。[CLAIMED_BY: Mochizuki]

---

## "striking" が指す定理 (誤読防止)

p.5 §2.1.2 に "striking result" の出現があるが、これは Mochizuki [Anab3,
Thm.1.9 / Cor.1.10] の anabelian 定理 (Belyi 型曲線の π₁ による復元) を指す。
mono-theta 環境・EtTh とは別の文脈である。

---

## SS の批判構造と mono-theta env の関係

SS の批判は単一の chain で完結する:

1. q^{j²}_v の値は "ingenious" な算法で得られる (= EtTh の成果を事実上承認)。
2. それらを F⊩×µ-prime strip に抽象化すると abstract pilot object は
   R⊙,Θ の元になる。
3. Θ-pilot の arithmetic degree を正しく encode するには R⊙,Θ ≅ R の
   識別を j² でスケールする必要がある。
4. このスケールを diagram 全体に通すと monodromy j² が生じ inconsistent
   になる (SS p.10)。

**Step 1 で mono-theta 環境の 3 rigidities が利用されると仮定しても、
SS の批判は Step 3-4 (deployment) に集中しており、Step 1 の formalism を
invalid とする主張は SS 2018 全文に存在しない。**

---

## Critical caveats

1. "mono-theta" という用語の不在は否定ではない。SS は [EtTh] を引用しないが、
   §2.1.8 で EtTh の成果 (tempered coverings → q^{j²}_v 復元) を事実上
   認めている。
2. SS が "rigidity" を使うのは o×_{k̄v} の non-rigidity (§2.1.2) のみであり、
   EtTh の rigidity 体系とは別概念。混同禁止。
3. SS が cyclotomic / discrete / constant_multiple rigidity を valid と
   認めた、とも言えない。単に評価対象外として沈黙している。
4. Mochizuki 側は 3 rigidities が Cor.3.12 の multiradial algorithm に
   essential と主張する (→ 3-agent verify で要確認)。

---

## Source

- Scholze–Stix 2018, "Why abc is still a conjecture", p.5–10.
  PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
  (pymupdf 全文テキスト抽出 + 全 occurrence 手動確認, 2026-05-06)
- 参照 IRI: `iut:mono_theta_cyclotomic_rigidity` / `iut:mono_theta_discrete_rigidity` /
  `iut:mono_theta_constant_multiple_rigidity` (flat, no prefix expansion)
