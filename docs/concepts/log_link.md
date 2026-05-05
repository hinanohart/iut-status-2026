# [iut:log_link] log-link (additive)
> 3-agent verify pending (mochizuki-side draft).

## Definition

**log-link** は 2 つの F-prime-strip (または Θ±ellNF-Hodge theater) 間の射であり、
各 nonarchimedean 付値 v ∈ V^non において局所 p_v-adic 対数写像

    log_v : O^×_{F_v} → F_v

を適用することで定義される (IUTchIII Def 1.1 (i); Prop 1.3 (i))。

具体的には、F-prime-strip の v 成分における対応として

    { Π_v ↷ O^▷_{F_v} }  —log→  { Π_v ↷ O^▷_{F_v} }

を与え、右辺の O^▷_{F_v} は左辺の単数部分 O^×_{F_v} ⊆ O^▷_{F_v} の
テンソル積 O^×_{F_v} ⊗ Q に p_v-adic 対数が誘導する体構造から得る。

**log-shell** I_v は (v ∈ V^bad の場合)

    I_v  :=  p_v^{-1} · log_v(O^×_{K_v})  ⊆  K_v  ⊆  F_v

と定義される加法的コンパクト加群 (IUTchIII Def 1.1 (i); Intro p.4)。
archimedean 側 (v ∈ V^arc) の log-shell は [AbsTopIII] Def 5.4 (v) 準拠の類似定義を持つ
(IUTchIII Def 1.1 (ii))。

## Key properties

- **coricity of D-prime-strips**: log-link は下敷きの D-prime-strip に
  poly-isomorphism †D →~ ‡D を誘導する (Prop 1.2 (i))。
  Π_v は log-link に対して "coric"、すなわち中立的。

- **additive vs multiplicative の対称性**: log-link (vertical arrow) は局所環の
  加法・乗法両構造を用いて定義される。対して theta-link / Θ^×μ-link (horizontal arrow)
  は乗法モノイド構造のみに依存し、局所環構造と非整合 (Remark 1.4.1 (i))。
  この非整合性が log-theta-lattice の高度な非可換性の源泉。

- **log-shell 包含**: O^▷_{K_v} ⊆ I_v かつ log_v(O^×_{K_v}) ⊆ I_v (Prop 1.2 (v))。
  すなわち I_v は log-link の domain・codomain 双方の Kummer 像を包含する。

- **log-volume との整合性**: log-link は自然な p_v-adic log-volume と整合する
  (Prop 1.2 (iii); Prop 3.9 (iv))。

- **log-Kummer correspondence**: Kummer 同型
  Ψ_cns(†F) →~ Ψ_cns(†D) と Ψ_cns(‡F) →~ Ψ_cns(‡D) は、
  log-link が誘導する Ψ_cns(†D) →~ Ψ_cns(‡D) と element レベルでは非整合
  (Prop 1.2 (iv); [AbsTopIII] Cor 5.5 (iv))。
  この非整合性を包む全体的な図式を **log-Kummer correspondence** と呼ぶ
  (Thm 3.11 (ii); Thm A (ii))。

- **log-theta-lattice**: vertical arrow = log-link の反復、horizontal arrow =
  Θ^×μ-/Θ^×μ_gau-/Θ^×μ_LGP-link とからなる高度に非可換な 2 次元図式
  (Def 1.4)。

## Why log-link is essential at Cor. 3.12

Cor. 3.12 (= Theorem B) の核心は LGP-monoid の log-volume 上界の計算である。
log-link が log-volume と整合する (Prop 1.2 (iii)) 一方、Kummer 同型との整合性は
element レベルでは成り立たない。しかし log-shell I_v が domain・codomain 双方の
Kummer 像を包含するという "upper semi-compatibility" (Remark 1.2.2 (iii)) により、
log-volume 積分は「等式」ではなく「上界」として評価できる。
この上界推定が [IUTchIV] における Diophantine 結果 (ABC 予想型不等式) の基礎をなす。

## Forbidden translations

- "log-shell" → 「対数殻」等の造語: 原語 log-shell をそのまま使用。
- "log-theta-lattice" を theta-link と混同しないこと (vertical ≠ horizontal)。
- "upper semi-compatibility" を「可換性」と読み替えないこと。

## Source

| 参照箇所 | 内容 |
|---|---|
| IUTchIII Def 1.1 (i)(ii), §1 p.23– | log-link・log-shell の形式定義 |
| IUTchIII Prop 1.2 (i)(iii)(iv)(v)(x) | coricity / log-volume / Kummer 非整合 / log-Kummer |
| IUTchIII Prop 1.3 (i) | Hodge theater 間 log-link |
| IUTchIII Def 1.4 | log-theta-lattice |
| IUTchIII Cor 3.12; Thm 3.11 (ii) | log-volume 上界・log-Kummer correspondence |
| IUTchIII Intro pp.3–8 | 概念的動機の要約 |

- **IUTchIII PDF**: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
- **DOI (PRIMS 2021)**: https://doi.org/10.4171/PRIMS/57-1-3
- **Alien Copies survey**: https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf
