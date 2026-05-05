# Section 2d: Prime-Strip Variants (deep) — SS-side draft

> Status: SS-side draft only. NOT 3-agent merged. Do NOT cite as neutral.
> IRIs: `iut:F_prime_strip`, `iut:F_modulus_prime_strip`, `iut:F_circ_theta_strip`, `iut:F_circ_q_strip`
> Source: Scholze-Stix 2018 (SS), July 16, 2018.
> URL: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>
> PDF-verified 2026-05-06 via pymupdf full-text extraction (all 10 pages).

---

## 検索結果サマリー (PDF 全文照合)

| 検索語 | 全文出現数 | 備考 |
|---|---|---|
| `prime strip` (スペース区切り) | 15 | §2.1.5 (p.7) から §2.2 (p.9) にかけて集中 |
| `prime-strip` (ハイフン) | 0 | PDF 文字コード上ハイフンが半角スペースに変換されている |
| `⊩` (= `F^⊩×µ` の `⊩` 部分) | 21 | 全て `F ⊩×µ` 形式で出現 |
| `×µ` / `×μ` | 35 | `F ⊩×µ` 構造およびローカルの `o×µ_K` 定義の両方 |
| `procession` | 1 | §2.2 p.9 のみ (`processions of tensor packets of log-shells`) |
| `log-shell` / `log-shells` | 1 | §2.2 p.9 のみ (上記と同箇所) |
| `log-link` | 4 | §2.1.3 (p.6-7) で定義; p.7 で IUTT link の一般形として登場 |
| `Θ-link` | 6 | §2.1.9 (p.9) で定義 |
| `multiradial` | 1 | §2.2 p.9: IUTT-3 Cor 3.12 の文脈 |
| `D-prime` / `D'-prime` / `F-prime-strip` (ハイフン) | 0 | 全文 0 件 |
| `LGP` / `F^⊩LGP` | 0 | 全文 0 件 (SS は LGP 記法を使わない) |
| `F^⊢` (vdash) | 0 | 全文 0 件 |

**結論**: SS 2018 において prime-strip variants の中で **`F^⊩×µ`-prime strip のみが深く論じられる**。
`F^⊢`-prime strip・D-prime-strip・LGP-strip 等の他 variants は全文 0 件。
`procession` は §2.2 の IUTT-3 Cor 3.12 批判の文脈で 1 回登場するが、SS 自身が定義せず引用するのみ。

---

## sub_1 — `F^⊩×µ`-prime strip: SS §2.1.5 (p.7) の定義的記述

SS §2.1.5 "F ⊩×µ-prime strips" は本文書中で prime-strip variants の唯一の詳述箇所。verbatim:

> "Another kind of coarse data that can be extracted from Hodge theaters is the data of a
> F ⊩×µ-prime strip, cf. [IUTT-2, Definition 4.9]. In general, prime strips denote data that is
> parametrized by all places of the number field k. In the case of a F ⊩×µ-prime strip, this
> data is, at nonarchimedean places, given by the pair
> G_v ⟲ o×µ_{k̄_v} × o_{k̄_v}
> where o_{k̄_v} ≃ N with trivial G_v = Gal(k_v)-action." (SS p.7)

- SS は `F^⊩×µ`-prime strip を **coarse data** として捉える: Hodge theater から抽出された「粗い」データ。
- 局所成分は `G_v ⟲ o×µ_{k̄_v} × N` という対 (topological group 作用 on topological monoid)。
- **[CLAIMED_BY: Mochizuki]**: `F^⊩×µ`-prime strip は IUTchII Def 4.9 で定義。
  `⊩` は Frobenioid 由来の "Frobenius-like" 構造、`×µ` は `o×µ_K = o×_K / oµ_K`
  (roots of unity の商) を意味し、log-link 下での "×µ-Kummer structure" を保持する
  (IUTchII §2, §4; IUTchIII §3)。SS はこの Kummer structure に脚注で触れるが捨象する。

---

## sub_2 — `F^⊩×µ`-prime strips の圏論的性質: SS §2.1.5 後半 (p.8)

SS は `F^⊩×µ`-prime strip の圏を具体的に characterize する。verbatim:

> "the forgetful functor from F ⊩×µ-prime strips to global realified Frobenioids factors over
> the category of trivialized global realified Frobenioids, and the category of F ⊩×µ-prime
> strips is equivalent to the product of the categories of pairs of topological groups acting
> on topological monoids abstractly isomorphic to G_v ⟲ o×µ_{k̄_v} × N,
> over all places v." (SS p.8)

- **[CLAIMED_BY: SS]**: `F^⊩×µ`-prime strips のカテゴリは
  `∏_v (G_v ⟲ o×µ_{k̄_v} × N)` 型の対の積カテゴリに圏同値。
  global 成分 (global realified Frobenioid) は trivialized (= ordered 1-dim R-vector space) に
  因子分解される。すなわち `F^⊩×µ`-prime strip は本質的に局所データの積である。
- SS 脚注 9: "×µ-Kummer structure" (`(o×_{k̄_v})^H → o×µ_{k̄_v}` の像) は
  SS の議論では "play no role" として捨象される。
- **[CLAIMED_BY: Mochizuki]**: この捨象こそが IUT の核心を失わせる。
  ×µ-Kummer structure は log-link の "cyclotomic rigidity" を担い、
  inter-universal な算術情報の輸送を可能にする (IUTchIII §3; Mochizuki 2018 response §2)。

---

## sub_3 — `F^⊩×µ`-prime strip と Θ-link の関係: SS §2.1.9 (p.9)

SS §2.1.9 "Θ-link" は prime-strip が Θ-link の主体であることを明示する。verbatim:

> "The Θ-link between two Hodge theaters HT_1 and HT_2 is the (full poly-)isomorphism
> between the F ⊩×µ-prime strip F ⊩×µ_{Θ,1} constructed from the Θ-pilot object in HT_1
> and the F ⊩×µ-prime strip F ⊩×µ_{q,2} constructed from the q-pilot object in HT_2." (SS p.9)

- Θ-link は `F^⊩×µ_{Θ,1} ≅ F^⊩×µ_{q,2}` という prime-strip 間の同型として定式化される。
- SS の核心的指摘: "the F ⊩×µ-prime strips are given by data of the form G_v ⟲ o×µ_{k̄_v} × N
  on both sides …this data is canonically the same on both sides. It is simply the name of
  the generator of the monoid N that appears that is called Θ respectively q." (SS p.9)
- **[CLAIMED_BY: SS]**: Θ-link は自明な同型 (両辺が標準的に同じデータ) であり、
  abstract pilot object の対応は単に generator の「名前」の付け替えに過ぎない。
  これが SS の main objection: abstract ≠ concrete の区別が失われる。
- **[CLAIMED_BY: Mochizuki]**: `F^⊩×µ` prime-strip の「canonical な同型」は
  異なる universe に属する 2 つの Hodge theater 間でのみ意味を持つ。
  同一 universe 内では canonical だが、inter-universal 輸送では indeterminacy (Ind 1,2,3)
  を通じてのみ比較可能 (IUTchIII Cor 3.12; Mochizuki 2018 response §2)。
- **[DISPUTED]** — `claim:scholze_stix_2018_sub_1` (Θ-link 問題の核心) と直結。

---

## sub_4 — `F^⊩×µ` 以外の prime-strip variants: SS の沈黙

### `iut:F_prime_strip` (F-prime-strip, IUTchI §3)
SS 全文に独立した `F-prime-strip` の言及は 0 件。
`F^⊩×µ`-prime strip は `F-prime-strip` の派生型 (depends_on: `iut:F_prime_strip`) だが、
SS は `F-prime-strip` の一般定義には立ち入らず `F^⊩×µ` 特化の記述のみを行う。
- **[CLAIMED_BY: Mochizuki]**: F-prime-strip は IUTchI Def 3.7 で定義される
  Frobenioid-theoretic data bundle。`F^⊩×µ` はその "×µ-version" (IUTchII §4)。

### `iut:F_circ_theta_strip` / `iut:F_circ_q_strip`
SS 全文に `F-circ-theta-strip`・`F-circ-q-strip` の名称は 0 件。
ただし §2.1.7-2.1.8 で "concrete q-pilot object" / "concrete Θ-pilot object" を
`F^⊩×µ`-prime strip として記述しており (`F^⊩×µ_q`, `F^⊩×µ_Θ`)、
entities.json の `iut:F_circ_q_strip` / `iut:F_circ_theta_strip` に実質対応する。
- **[CLAIMED_BY: SS]**: `F^⊩×µ_q` と `F^⊩×µ_Θ` は両側で "canonically the same data"
  (SS p.9); 区別は generator の名前のみ。
- **[CLAIMED_BY: Mochizuki]**: `F^⊩×µ_Θ` には `q_v^{j²}` (`j = 1,…,l*`) の
  j-indexed 構造が埋め込まれており (IUTchII §2, Def 4.9)、
  単純な名前の付け替えに還元できない (IUTchIII Cor 3.12 の j² scaling が本質的)。

### `procession` (IUTchIII §3)
SS §2.2 (p.9) に唯一の出現: "encoded via their action on **processions of tensor packets
of log-shells**". verbatim:

> "it is argued in [IUTT-3, Corollary 3.12] that the multiradial algorithm [IUTT-3, Theorem 3.11]
> implies that up to certain indeterminacies, e.g. (Ind 1,2,3) (without which the conclusion
> would be obviously false), this becomes an identification of concrete Θ-pilot objects and
> concrete q-pilot objects (encoded via their action on processions of tensor packets of
> log-shells), and then the inequality follows directly." (SS p.9)

- SS は "processions of tensor packets of log-shells" を Mochizuki の主張の**要約として引用**する。
  SS 自身はその構造を定義・分解しない。
- **[CLAIMED_BY: Mochizuki]**: procession (= ordered sequence of prime-strips) は
  IUTchIII §3 で定義され、multiradial algorithm の入力として
  log-shell の tensor packet 構造を組織化する (IUTchIII Def 3.1, Thm 3.11)。
- SS はその構造を "(Ind 1,2,3) without which the conclusion would be obviously false" という
  indeterminacy の問題として再記述する。procession 自体の validity は問わない。

---

## sub_5 — SS §2.1.5 先頭: Mochizuki が「簡略化を認めた」という記述 (SS p.4)

SS p.4 (Section 2 導入部) に重要な記述がある。verbatim:

> "During our discussion in Kyoto, Mochizuki agreed that some of these simplifications are OK,
> **for example regarding the critical notion of F ⊩×µ-prime strips below**." (SS p.4, excuse (1))

- Mochizuki は `F^⊩×µ`-prime strip に関する SS の簡略化を「OK と認めた」と SS は述べる。
- **[CLAIMED_BY: SS]**: この「合意」は `F^⊩×µ`-prime strip の圏論的記述の妥当性を
  Mochizuki 本人が承認したことを意味し、SS の批判の出発点として正当化される。
- **[CLAIMED_BY: Mochizuki]** (推定): Mochizuki 2018 response (§2) では、
  SS が simplification を正しく理解したとは述べておらず、
  inter-universal な文脈での ×µ-Kummer structure の役割が捨象されたことを問題視する。
  この「合意」の範囲は文書上 disputed のまま。
- **[DISPUTED]** — Kyoto 会議の「合意内容」は公開議事録が存在せず、
  両者の解釈が異なる可能性が高い。

---

## 4 IRI への SS 態度判定

| IRI | SS の記述箇所 | SS の態度 |
|---|---|---|
| `iut:F_prime_strip` | 全文 0 件 (独立言及なし) | 不言及。`F^⊩×µ` を通じて間接的に使用。**[CLAIMED_BY: Mochizuki]** (IUTchI Def 3.7) |
| `iut:F_modulus_prime_strip` (= `F^⊩×µ`) | SS §2.1.5-2.1.9 で深く論じる (15 occurrence) | **[CLAIMED_BY: SS]**: 局所積カテゴリ同値 + canonical trivial。批判の主舞台。 **[CLAIMED_BY: Mochizuki]**: ×µ-Kummer structure が inter-universal 輸送の要 |
| `iut:F_circ_theta_strip` | `F^⊩×µ_Θ` として §2.1.8-2.1.9 に登場 | **[CLAIMED_BY: SS]**: `F^⊩×µ_q` と canonical 同一。**[CLAIMED_BY: Mochizuki]**: j² 構造が非自明。 |
| `iut:F_circ_q_strip` | `F^⊩×µ_q` として §2.1.7-2.1.9 に登場 | **[CLAIMED_BY: SS]**: Θ-side と canonical 同一。Θ-link は trivial。**[CLAIMED_BY: Mochizuki]**: 別 universe の対象として本質的に異なる。 |

---

## 注意事項

- 本ドキュメントは SS-side draft。3-agent merge は未実施。
- `procession` / `iut:F_prime_strip` は SS では不言及。**[CLAIMED_BY: Mochizuki]** のみ。
- `iut:log_shell` (`section: 04_log_link`) は §2.2 で 1 回言及されるが、
  Section 2d の主要 IRI ではなく、参照のみ。詳細は `docs/section_4_log_link.md`。
- SS の §2.1.5 Footnote 9: "×µ-Kummer structure … plays no role for us" という明示的な
  捨象宣言が存在する。Mochizuki 側の反論の中心点の 1 つ。
- SS p.4 の "Mochizuki agreed" は dispute 中であり中立的事実として扱わないこと。
- 禁止翻訳: perfectoid / prismatic / condensed math への変換は行わない (`LLM_CONTEXT.md` §4)。
- 2c SS ビュー (`2c_nf_hodge_theater_deep_ss_view.md`) との関係:
  2c は `ΘNF`-Hodge theater の NF 成分の沈黙を記録;
  本ドキュメントは prime-strip variants の中で `F^⊩×µ` のみが SS に深く論じられ
  (`F^⊢`・D-prime-strip・LGP 等は 0 件)、それが Θ-link 批判の核心であることを記録する。
