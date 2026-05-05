# Section 2b: Theta-pm-ell Hodge Theater (deep) — SS-side draft

> Status: SS-side draft only. NOT 3-agent merged. Do NOT cite as neutral.
> IRIs: `iut:theta_pm_ell_hodge_theater`, `iut:F_l_pm_symmetry`, `iut:cusp_label`
> Source: Scholze-Stix 2018 (SS), July 16, 2018.
> URL: <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>
> PDF-verified 2026-05-06 via pymupdf full-text extraction (all 10 pages).

---

## 検索結果サマリー (PDF 全文照合)

下記の用語を SS 2018 全 10 ページで pymupdf 検索した結果を記録する。

| 検索語 | 全文出現数 | 備考 |
|---|---|---|
| `±ell` / `pm-ell` / `ell-symmetry` | 2 | いずれも型ラベル `Θ±ellNF-` の一部 (§2.1.2, p.6) のみ |
| `sigma-symmetry` / `sigma symmetry` | 0 | 全文 0 件 |
| `cusp` / `cusp label` | 0 | 全文 0 件 |
| `F_l^±` / `F_ell^±` / `additive symmetry` | 0 | 全文 0 件 |
| `multiplicative symmetry` | 0 | 全文 0 件 |
| `label` (数論的 label の意味で) | 0 | 全文 0 件 (`label` は IRI ラベル用語として不出現) |
| `symmetry` | 0 | 全文 0 件 |

**結論**: SS 2018 は `±ell`-symmetry・`F_l^±`-symmetry・cusp label・
sigma-symmetry のいずれにも立ち入らない。`Θ±ellNF` は Hodge theater の
型名 (type label) として 2 回使われるのみ。

---

## sub_1 — `Θ±ellNF` の唯一の言及 (SS §2.1.2, p.6)

SS が `Θ±ellNF` に触れる唯一の箇所は §2.1.2 "Hodge theater" の冒頭。verbatim:

> "In any case, a (Θ±ellNF-)Hodge theater is a certain amount of data that abstractly comes
> from the fixed once-punctured elliptic curve X. The natural functor from the category whose
> only object is X and whose morphisms are the automorphisms of X (which has one object with
> two automorphisms, the 'identity' and 'negation') to the category of Θ±ellNF-Hodge theaters is
> an equivalence of categories, as follows by combining [IUTT-1, Corollary 6.12 (i), Proposition
> 6.6 (iii), Corollary 5.6 (ii), Proposition 4.8 (ii), Definition 6.13]." (SS p.6)

- `Θ±ellNF` はここで Hodge theater 全体の圏同値命題の主語として登場する。
- SS は `Θ±ell` 成分と `ΘNF` 成分の内部構造を個別に議論しない。
- 「±ell」が担う加法的 `F_l^±`-symmetry と「NF」が担う乗法的 `F_l^*`-symmetry の
  区別は SS の記述に現れない。
- **[CLAIMED_BY: Mochizuki]**: `Θ±ell`-Hodge theater の additive symmetry (`F_l^±`-symmetry,
  label set `(-l* < … < 0 < … < l*) ≅ F_l`) は IUTchI Def 6.4(iii), Def 6.11(iii) で
  定義され、label に付随する D-prime-strip が distinct information を担うとされる
  (IUTchI §I1, pp. 9–10)。SS はこの構造に言及しない。

---

## sub_2 — "negation" 言及 (SS p.6) — ±1 構造の唯一の痕跡

SS は Hodge theater の automorphisms を次のように述べる:

> "…the automorphisms of X (which has one object with **two automorphisms, the 'identity'
> and 'negation'**) to the category of Θ±ellNF-Hodge theaters…" (SS p.6)

- この "negation" は `X = E \ {0}` の automorphism group `{±1}` (楕円曲線上の
  点の符号反転) を指す。
- Mochizuki の `Θ±ell`-Hodge theater における `F_l^±`-symmetry の「±」は、
  この `{±1}` 作用に由来するが、SS はその構造を ±1 automorphism の言及のみで
  処理し、label 集合 `(-l*, …, 0, …, l*)` や cusp label には立ち入らない。
- **[CLAIMED_BY: Mochizuki]**: ±1 作用が label set 上の `F_l^±`-symmetry に昇格し、
  各 label に D-prime-strip が張られることで `Θ±ell`-Hodge theater の additive 成分が
  構成される (IUTchI Def 6.4(iii); EtTh §1 との整合)。
  SS はこの昇格ステップを検証も否定もしない — 単に言及しない。

---

## sub_3 — sigma-symmetry への SS 態度: 不言及

Mochizuki の文脈では "sigma-symmetry"(または `Aut(CK)`-symmetry) は
`ΘNF`-Hodge theater の global arithmetic symmetry (`F_l^*`-symmetry) と対比される
additive symmetry の呼称として IUTchI §I1 で紹介される。

SS 2018 全文 (10 pp.) に "sigma" / "sigma-symmetry" の出現は 0 件。

- **[CLAIMED_BY: Mochizuki]**: sigma-symmetry は `Θ±ell`-Hodge theater の加法的
  global structure を担い、cusp 上の Galois 圏的対称性 (`π₁(X_K)` の ±1 作用)
  として実現される (IUTchI Def 6.11(iii); Cor 6.12(i))。
  IUTchI Cor 5.6(ii) と Prop 6.6(iii) はその functor の full faithfulness を与える。
- SS は同じ Cor 5.6(ii) / Prop 6.6(iii) を引用するが、これらを `{X}`-equivalence の
  証拠として用いるのみで、sigma-symmetry の内容には触れない。

---

## sub_4 — cusp label への SS 態度: 不言及

cusp label は `Θ±ell`-Hodge theater において label 集合
`T ≅ F_l = (-l*, …, 0, …, l*)` を cusp の組み合わせ的インデックスとして
識別する概念 (IUTchI Def 6.1; Def 6.4(i))。

SS 2018 全文に "cusp" の出現は 0 件。

- **[CLAIMED_BY: Mochizuki]**: cusp label は 2l-torsion 点のスペシャリゼーションで
  theta 値 `q_v^{j²}` の j-index を cusp に対応付ける構造を与え、
  `Θ±ell`-Hodge theater の additive symmetry group `F_l^±` が label 集合上に
  transitive に作用することを確保する (IUTchI Def 6.4(iii); §I1 pp. 9–11)。
- SS はこの label 構造に言及しない。SS の Cor 3.12 批判 (j² monodromy) は
  cusp label の存在を前提せず、単に j² という scalar の整合性のみを問題にする。

---

## 4 IRI への SS 態度判定

| IRI | SS の記述箇所 | SS の態度 |
|---|---|---|
| `iut:theta_pm_ell_hodge_theater` | SS p.6 型ラベルとして 2 回 | 内部構造に立ち入らず。全体を `{X}` 圏同値に包含。**[CLAIMED_BY: Mochizuki]** (内部 ±ell 構造) |
| `iut:F_l_pm_symmetry` | 全文 0 件 | 不言及。Mochizuki 側定義 (IUTchI Def 6.4) のみ。**[CLAIMED_BY: Mochizuki]** |
| `iut:cusp_label` | 全文 0 件 | 不言及。Mochizuki 側定義 (IUTchI Def 6.1) のみ。**[CLAIMED_BY: Mochizuki]** |

---

## 注意事項

- 本ドキュメントは SS-side draft。Mochizuki 側の `Θ±ell`-Hodge theater 構造の詳細は
  対応する mochizuki-side draft および `docs/section_2_hodge_theater.md` §2.1 に記録。
- SS の沈黙 (0 件) は否定ではない。SS は「我々が指摘する issue は subtleties を
  全て復元しても prevail する」と述べており (SS p.4, excuse (4))、
  `Θ±ell` 内部構造を捨象しても論点が成立すると判断している。
- `[CLAIMED_BY: Mochizuki]` は「SS が検証も否定もしなかった」を意味する。
- 禁止翻訳: perfectoid / prismatic / condensed math への変換は行わない
  (`LLM_CONTEXT.md` §4)。
- IRIs `iut:F_l_pm_symmetry` / `iut:cusp_label` は `data/entities.json` 未収録の
  可能性がある。収録済みの場合は当該 `@id` を参照のこと。
