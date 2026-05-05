# [iut:multiradial_algorithm + iut:Ind1/2/3] multiradial algorithm + indeterminacies
> 3-agent verify pending (mochizuki-side draft).

## Definition (statement-level)

- **multiradial algorithm**: 「alien arithmetic holomorphic structure」の視点から意味をなすアルゴリズム。
  具体的には Theorem 3.11 (Multiradial Algorithms via LGP-Monoids/Frobenioids) が
  splitting monoids of LGP-monoids の構成を multiradial に与え、その帰結として
  Corollary 3.12 が Θ-pilot object の log-volume estimate (不等式) を導出する。
  - **Cor. 3.12 statement** (PDF p.173–174, 内部 p.173–174):
    > *"− |log(Θ)| ≥ − |log(q)|"*
    すなわち、(Ind1), (Ind2), (Ind3) に服した multiradial representation における
    Θ-pilot log-volume は q-pilot log-volume 以上である。

- **Reference**: IUTchIII Cor. 3.12, p.173–174; Thm. 3.11, p.153–158
- **DOI**: [10.4171/PRIMS/57-1-3](https://doi.org/10.4171/PRIMS/57-1-3)
- **PDF**: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf

## Indeterminacies (Ind1, Ind2, Ind3) — Mochizuki verbatim (Thm. 3.11)

原文 (PDF p.154–156, Theorem 3.11 §(i)–(ii)):

> **(Ind1)** "the indeterminacies induced by the automorphisms of the procession
> of D⁺-prime-strips Prc(ⁿ˒◦D⁺); [i.e.,] from permutation automorphisms of the
> label sets S±_{j+1} that appear in the processions … as well as from the
> automorphisms of the D⁺-prime-strips that appear in these processions."
>
> **(Ind2)** "for each v ∈ V^non_Q (resp. v ∈ V^arc_Q), the indeterminacies induced
> by the action of independent copies of Ism [cf. Proposition 1.2, (vi)]
> (resp. copies of each of the automorphisms of order 2 …) on each of the
> direct summands of the j+1 factors appearing in the tensor product used
> to define I^Q(S±_{j+1}; ⁿ˒◦D⁺_{v_Q})"
>
> **(Ind3)** "as one varies m ∈ Z, the isomorphisms of (a) are 'upper semi-
> compatible', relative to the log-links of the n-th column … in a sense that
> involves certain natural inclusions '⊆' at v ∈ V^non_Q and certain natural
> surjections '↠' at v ∈ V^arc_Q — cf. Proposition 3.5, (ii), (a), (b), for more
> details."

### 簡略説明

| ID | 作用対象 | 性質 |
|---|---|---|
| **Ind1** | D⁺-prime-strip の procession 自己同型 (ラベル集合 S±_{j+1} の置換 + D⁺-prime-strip の Aut) | étale-like / combinatorial |
| **Ind2** | F^{×μ}-prime-strip の Aut (Θ-link から生じる Z^×-不定性、局所 O^{×μ} への作用) | Frobenius-like / Z^×-indeterminacy |
| **Ind3** | log-Kummer 対応の「upper semi-compatibility」(精確な等式でなく一方向的な包含関係) | log-volume / 上半相容性 |

Introduction (PDF p.11–12) では:
> "This passage to the multiradial representation is obtained by admitting the following
> three types of indeterminacy: (Ind1) … (Ind2) … (Ind3) …"

## Why multiradial essential

- **「多輻的」** = 複数の arithmetic holomorphic structure (異なる vertical line) の観点から
  同時に意味をなす記述形式。"uniradial" (単輻的) では alien structure の側から参照できない。
- Cor. 3.12 の不等式は、Θ-pilot object を multiradial representation に写した「可能像の
  holomorphic hull の log-volume」と q-pilot の log-volume を比較することで成立する。
- (Ind1), (Ind2), (Ind3) に服した上でなお不等式が成立することが、IUTchIV における
  diophantine 結果 (Vojta 予想の特殊形など) の根拠となる。

## Forbidden translations (SS 系語彙)

以下の用語は Mochizuki 原文に存在しない解釈を導入するため使用禁止:

- "scheme-theoretic interpretation of Ind1/2/3" → 原文は étale/Frobenius-like の区別を厳守
- "Ind2 = Galois indeterminacy" → 原文は Z^×-indeterminacy (on O^{×μ}) と明記
- "Cor. 3.12 proves abc conjecture directly" → 原文は log-volume inequality のみ; IUTchIV で適用
- "multiradial = functorial" → 多輻性は functoriality より広い概念 (cf. Thm. 3.11 final remark)

## Source

- **IUTchIII §1, §3, Thm. 3.11, Cor. 3.12**
  - Thm. 3.11 (Multiradial Representation): PDF p.153–158 (内部 p.153–158)
  - Cor. 3.12 (Log-volume Estimates): PDF p.173–174 (内部 p.173–174)
  - Ind1/Ind2 定義: Thm. 3.11 §(i), PDF p.154
  - Ind3 定義: Thm. 3.11 §(ii), PDF p.156
  - Introduction の三不定性一覧: PDF p.11–12 (内部 p.11–12)
- **"Alien Copies" survey**: Mochizuki, "The Mathematics of Mutually Alien Copies", §3
  (https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf)
- **PRIMS 掲載版 DOI**: https://doi.org/10.4171/PRIMS/57-1-3
- **kurims PDF**: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
