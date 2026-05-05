# 1d — Etale Theta (deep) — Scholze-Stix view
> SS-side draft. PDF-verified 2026-05-06 via pymupdf full-text extraction (pages 7–10).

## Source
- SS 2018 (Scholze–Stix, "Why abc is still a conjecture"), p.8 §2.1.6–§2.1.9.
  PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- 検索対象: "theta" / "Θ" / "tempered" / "ingenious" / "etale" / "étale" / "EtTh"
  — pymupdf 全文検索 (全 10 ページ) で確認済み。

---

## "theta" / "Θ" 全出現 (p.8–10)

| 場所 | 文字列 | 文脈 |
|---|---|---|
| p.8 §2.1.8 冒頭 | "values of a Θ-function" | Θ-function の θ 値 = q_v^{j²} の出典説明 |
| p.8 §2.1.8 | "Θ-pilot object" (×複数) | Concrete Θ-pilot object の定義 |
| p.8 §2.1.8 | "F^{⊩×µ}_Θ" | Θ-pilot を格納する F^{⊩×µ}-prime strip |
| p.9 §2.1.9 | "Θ-link" (×複数) | Θ-link の定義と批判の中心 |
| p.9–10 §2.2 | "abstract Θ-pilot" / "concrete Θ-pilot" | 批判図の operand |

**"étale theta" / "etale theta" / "EtTh" の出現: 全文 0 件。**
[EtTh] は SS 2018 参考文献リストに存在しない。

---

## "tempered" 出現 (p.8 §2.1.8)

SS p.8 §2.1.8 — verbatim:

> "Mochizuki devises an **ingenious algorithm** to recover this data very directly from
> the data of π₁(X) acting on a certain monoid of divisors on **tempered coverings** of X."

**"tempered" の全文出現: この 1 箇所のみ。**
"tempered fundamental group" / "tempered group" としての出現は 0 件。

---

## "ingenious" 出現 (p.8 §2.1.8)

SS p.8 §2.1.8 — verbatim (fn.11 含む):

> "Mochizuki devises an **ingenious algorithm** to recover this data very directly from
> the data of π₁(X) acting on a certain monoid of divisors on tempered coverings of X.¹¹"

fn.11:
> "There is an issue here that this is not one object but ℓ⋇ many. This can be resolved
> in a number of ways, e.g. by passing to a 'diagonal' copy; or more concretely by forming
> averages when one extracts numbers such as arithmetic degrees."

**"ingenious" の全文出現: この 1 箇所のみ (§2.1.8)。**

---

## 3 IRI への SS 態度判定

### `iut:etale_theta_class`

**[CLAIMED_BY: Mochizuki]**

"étale theta" という文字列は SS 2018 全文に出現しない。[EtTh] 論文も参照されない。
SS は θ 関数の値 q_v^{j²} を受け入れるが、その値を生成する étale theta 理論の
定式化 (EtTh Thm 1.10, §1 の rigid-analytic theta function の étale-theoretic 解釈) には
一切触れない。

判定根拠: SS は Θ-function values の存在を前提として受け入れた上で
Θ-pilot を構成するため、`iut:etale_theta_class` の否定も肯定も行っていない。

---

### `iut:absolute_anabelian_theta`

**態度: ACKNOWLEDGED (ingenious) — 批判対象外**

EtTh Thm 1.10 は「π₁(X) の tempered coverings 上の約数モノイドへの作用から
q_v^{j²} を group-theoretically recover する」アルゴリズムに相当する。

SS p.8 §2.1.8 はこのアルゴリズムを "ingenious" と明示的に評価し、
fn.11 でその技術的問題点 (ℓ⋇ 個の対象の対角化) に言及しつつも、
アルゴリズムの正当性を争わない。

SS の批判は「π₁(X) から q_v^{j²} を recover できるか」ではなく、
「recover した値を abstract F^{⊩×µ}-prime strip に置いた後の
ℝ-copies の identification が consistent か」に集中する。

---

### `iut:frobenioid_theoretic_theta`

**態度: ACKNOWLEDGED (construction accepted) — 批判対象外**

EtTh Thm 5.10 は theta 値を Frobenioid 的構造 (モノイド・Kummer 理論) と
結びつける。SS はこの部分を black box として扱い内容に踏み込まない。

SS p.8 §2.1.8 verbatim:

> "Up to some 2ℓ-th roots of unity, these arise naturally as the values of a
> Θ-function at certain 2ℓ-torsion points"

この記述は Θ-function 値の起源を認める。続いて F^{⊩×µ}-prime strip
F^{⊩×µ}_Θ = (G_v ↷ o^{×µ}_{k̄_v} × ((q_v^{j²})_{j=1,…,ℓ⋇})^ℕ) を構成するが、
これは EtTh Thm 5.10 の Frobenioid 的側面の反映とみなせる。

批判はこの構成後の段階 — abstract pilot object が R⊙,Θ に encode される際に
j²-scaling が必要となり、Θ-link 全体図に monodromy j² が生じること — に向けられる。

---

## SS が認める範囲 vs. 批判対象

| 事項 | SS の態度 |
|---|---|
| q_v^{j²} が Θ-function の 2ℓ-torsion 値であること | 受け入れ (p.8) |
| π₁(X) からの group-theoretic recovery アルゴリズム | "ingenious" と称賛 (p.8 §2.1.8) |
| tempered coverings 上の約数モノイドの役割 | 認識あり (1 箇所のみ言及) |
| F^{⊩×µ}_Θ prime strip の構成 | 受け入れ (p.8 §2.1.8) |
| Θ-link の well-definedness | 受け入れ (p.9 §2.1.9) |
| Θ-link 後の ℝ-copies identification | **批判の中心** (p.9–10 §2.2) |
| j²-scaling による diagram の monodromy | "inconsistent" と断定 (p.10) |

---

## 誤解防止注記

**「SS は étale theta を否定した」は誤り。**

- SS は étale theta の構成を論じていない (全文に "étale theta" 0 件)。
- 批判点は θ 値が abstract strips に入った後の downstream の identification。
- EtTh 全体が否定されたわけではなく、Cor.3.12 の proof step で使われる
  ℝ-copies の一貫性が争点。
- `claim:tempered_rigidity_acknowledged` (§2.1.8 の "ingenious" 言及) は
  既存 claim として記録済み。

## Version
PDF-verified: 2026-05-06, pymupdf full-text extraction, pages 7–10.
