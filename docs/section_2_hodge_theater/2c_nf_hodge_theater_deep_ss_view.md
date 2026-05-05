# Section 2c: NF-Hodge Theater (deep) — SS-side draft

> Status: SS-side draft only. NOT 3-agent merged. Do NOT cite as neutral.
> IRIs: `iut:nf_hodge_theater`, `iut:F_l_star_symmetry`, `iut:theta_ell_NF_hodge_theater`, `iut:global_frobenioid`
> Source: Scholze-Stix 2018 (SS), July 16, 2018.
> URL: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>
> PDF-verified 2026-05-06 via pymupdf full-text extraction (all 10 pages).

---

## 検索結果サマリー (PDF 全文照合)

| 検索語 | 全文出現数 | 備考 |
|---|---|---|
| `ΘNF` / `ΘNF-` / `NF-Hodge` (スタンドアロン) | 0 / 0 / 1 | `NF-Hodge` の 1 件は `Θ±ellNF-Hodge` の内部 |
| `NF-` (全形) | 2 | いずれも `Θ±ellNF-)` / `Θ±ellNF-Hodge` の一部 |
| `F_l^*` / `F^*` / `F_l ` (乗法的対称群) | 0 | 全文 0 件 |
| `symmetry` | 0 | 全文 0 件 |
| `multiplicative symmetry` | 0 | 全文 0 件 |
| `number field` | 0 | 全文 0 件 |
| `multiplicative` (文中) | 2 | p.2, p.3 のみ。Tate 曲線の「multiplicative bad reduction」の意味。対称群とは無関係。 |

**結論**: SS 2018 は `ΘNF`-Hodge theater・`F_l^*`-symmetry・number field symmetry のいずれにも
独立した形で立ち入らない。`NF` という文字列は `Θ±ellNF` という複合型名の一部としてのみ 2 回現れる。

---

## sub_1 — `Θ±ellNF` 型名としての唯一の言及 (SS §2.1.2, p.6)

SS が `Θ±ellNF` (= `ΘellNF`) に触れる文脈は §2.1.2 "Hodge theater" 圏同値の叙述のみ。verbatim:

> "In any case, a (Θ±ellNF-)Hodge theater is a certain amount of data that abstractly comes
> from the fixed once-punctured elliptic curve X. The natural functor from the category whose
> only object is X and whose morphisms are the automorphisms of X (which has one object with
> two automorphisms, the 'identity' and 'negation') to the category of Θ±ellNF-Hodge theaters is
> an equivalence of categories, as follows by combining [IUTT-1, Corollary 6.12 (i), Proposition 6.6
> (iii), Corollary 5.6 (ii), Proposition 4.8 (ii), Definition 6.13]." (SS p.6)

- SS は `Θ±ellNF` を **分解しない**。`Θ±ell` 成分 (加法的 `F_l^±`-symmetry) と
  `ΘNF` 成分 (乗法的 `F_l^*`-symmetry) の内部構造を個別に議論しない。
- 上記引用が SS 全文中で `ΘNF` / `NF-Hodge` に関連する唯一の箇所である。
- **[CLAIMED_BY: Mochizuki]**: `ΘNF`-Hodge theater は `F_l^*`-symmetry (= `F_l^×`; 乗法的)
  が label set `(1 < 2 < … < l*)  ≅ F_l^×` に作用する global arithmetic symmetry 構造を担う
  (IUTchI Def 5.4, 6.4(iii), Remark 6.12.3, pp. 155–175)。SS はこの構造に言及しない。

---

## sub_2 — `F_l^*`-symmetry への SS 態度: 不言及

Mochizuki の文脈では `F_l^*`-symmetry (= `F_l^×`-symmetry; 乗法的 global symmetry) は
`ΘNF`-Hodge theater の基幹構造であり、`Θ±ell`-Hodge theater の加法的 `F_l^±`-symmetry と
対をなす (IUTchI Remark 6.12.3, p. 175)。

SS 2018 全文 (10 pp.) に `F_l^*` / `F^*` / `symmetry` の出現は **0 件**。

- **[CLAIMED_BY: Mochizuki]**: `F_l^*`-symmetry は `1 < … < l*` という非対称 label set 上に
  作用し、theta 値 `q_v^{j²}` の `j ∈ {1,…,l*}` による収集 (= "étale theta function の
  global multiplicative structure") を可能にする。この非対称性が `F_l^±`-symmetry の
  対称 label set `(-l* < … < 0 < … < l*)` と補完関係にある
  (IUTchI Def 6.4(i)(ii)(iii); §I1 pp. 9–11)。
- SS の Cor 3.12 批判 (j² monodromy 問題) は `F_l^*`-symmetry の構造を前提せず、
  abstract/concrete pilot objects の同一性のみを問題にする (SS §2.2, pp. 9–10)。

---

## sub_3 — global realiﬁed Frobenioid と `iut:global_frobenioid` (SS §2.1.4, p.7)

SS は global realiﬁed Frobenioid について例外的に詳しく述べる。verbatim (p.7):

> "However, the notion of a global realified Frobenioid is very elementary, cf. [IUTT-1, Example 3.5].
> In this case, it simply amounts to a collection of ordered 1-dimensional R-vector spaces Rv
> parametrized by the places v of k, together with a subspace D0 ⊂ ⊕_v Rv of codimension 1 …
> the category of global realified Frobenioids is equivalent to the category of ordered
> 1-dimensional R-vector spaces." (SS p.7)

- **[CLAIMED_BY: SS]**: global realiﬁed Frobenioid は ordered 1-dim R-vector space と圏同値。
  Mochizuki が用いる NF 側の "global arithmetic" 構造は、SS の見方ではこの初等的対象に収まる。
- SS 引用先 [IUTT-1, Example 3.5] は `ΘNF`-Hodge theater の NF-Frobenioid ではなく、
  IUTchI §3 の一般的 global Frobenioid の例である。SS は NF 側固有の Galois 作用を明示しない。
- **[CLAIMED_BY: Mochizuki]**: global realiﬁed Frobenioid の「初等性」は Mochizuki も認めるが、
  その上に乗る `F_l^*`-Galois 作用 (= NF-symmetry) が IUTchII の multiradial algorithm で
  本質的役割を果たすとされる (IUTchII §1, Prop. 1.4; Mochizuki 2018 response §3)。

---

## sub_4 — `Θ±ellNF` の NF 成分: SS の沈黙の構造的理由

SS p.4 には批判の "scope" について次の注釈がある (excuses (3)(4)):

> "(3) When it comes to the more drastic simplifications indicated below, such as merely identifying
> the choice of a Hodge theater with the choice of a curve abstractly isomorphic to X …
> Mochizuki was not able to explain [why this simplification is not allowed]." (SS p.4)

- SS の戦略は `Θ±ellNF`-Hodge theater 全体を `{X}` 圏同値に還元することで、
  内部の `ΘNF` / `Θ±ell` 分解を検討する必要を回避している (SS §2.1.2, p.6)。
- この戦略により `ΘNF` 成分の `F_l^*`-symmetry・global multiplicative structure は
  SS の批判の俎上に乗らない: SS は「内部構造がどう定義されていても、全体が `{X}` と
  圏同値なら自明」という立場を取る。
- **[CLAIMED_BY: Mochizuki]**: この「drastic simplification」こそが IUT の
  inter-universality を破壊する誤りである (Mochizuki response 2018, §1–§3)。
  `ΘNF` の NF 側 global structure は異なる universe 間の算術的情報の輸送に不可欠であり、
  `{X}` への還元はその輸送を不可能にする。
- **[DISPUTED]** — `claim:scholze_stix_2018_sub_1` (圏同値・Θ-link 問題) と連動。

---

## 4 IRI への SS 態度判定

| IRI | SS の記述箇所 | SS の態度 |
|---|---|---|
| `iut:nf_hodge_theater` | 全文 0 件 (独立言及なし) | 不言及。全体を `{X}` 圏同値に包含。**[CLAIMED_BY: Mochizuki]** (内部 `F_l^*` 構造) |
| `iut:F_l_star_symmetry` | 全文 0 件 | 不言及。Mochizuki 側定義 (IUTchI Def 6.4, Remark 6.12.3) のみ。**[CLAIMED_BY: Mochizuki]** |
| `iut:theta_ell_NF_hodge_theater` | p.6 型ラベルとして 2 回 (`Θ±ellNF`) | 内部分解なし。`{X}` 圏同値の主語として。**[CLAIMED_BY: Mochizuki]** (分解構造) |
| `iut:global_frobenioid` | SS §2.1.4, p.7 (詳述) | 初等的 (ordered 1-dim R-vector space 圏同値) と記述。**[CLAIMED_BY: SS]** (初等性) / **[CLAIMED_BY: Mochizuki]** (その上の F_l^*-Galois 作用) |

---

## 注意事項

- 本ドキュメントは SS-side draft。3-agent merge は未実施。
- SS の沈黙 (0 件) は否定ではない。SS は §2.1.2 の圏同値論証が `Θ±ellNF` 全体に
  適用されると主張しており、NF 成分の個別反論を要しない立場。
- `[CLAIMED_BY: Mochizuki]` は「SS が検証も否定もしなかった」を意味する。
- 禁止翻訳: perfectoid / prismatic / condensed math への変換は行わない (`LLM_CONTEXT.md` §4)。
- IRIs `iut:nf_hodge_theater` / `iut:F_l_star_symmetry` は `data/entities.json` 未収録の
  可能性あり。収録済みの場合は当該 `@id` を参照のこと。
- 2b SS ビュー (`2b_theta_pm_ell_hodge_theater_deep_ss_view.md`) との関係:
  2b は `Θ±ell` 加法成分の沈黙を記録; 本ドキュメントは `ΘNF` 乗法成分の沈黙を記録。
  両者は SS の「`Θ±ellNF` 全体を型名として使うが内部分解しない」戦略の両面。
