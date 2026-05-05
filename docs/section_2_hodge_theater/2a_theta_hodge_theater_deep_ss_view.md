# Section 2a: Theta-Hodge Theater (deep) — SS-side draft

> Status: SS-side draft only. NOT 3-agent merged. Do NOT cite as neutral.
> IRIs: `iut:theta_hodge_theater`, `iut:theta_pilot_object`, `iut:F_circ_theta_strip`, `iut:F_circ_q_strip`
> Source: Scholze-Stix 2018, pp. 6–9. <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>

## sub_1 — `iut:theta_hodge_theater` ≃ {X}: 圏同値 (SS p.6)

SS は [IUTT-1, Cor 6.12(i), Prop 6.6(iii), Cor 5.6(ii), Prop 4.8(ii), Def 6.13] を組み合わせて次を導く (verbatim):

> "The natural functor from the category whose only object is X … to the category of
> Θ±ellNF-Hodge theaters is an equivalence of categories … up to equivalence of categories,
> choosing a Hodge theater is equivalent to choosing a once-punctured elliptic curve abstractly
> isomorphic to X, and this equivalence of categories is constructive." (SS p.6)

- **[CLAIMED_BY: SS]** Mochizuki 自身の定理から圏同値を constructive に導出。
  「この simplification が allowed でない理由を Kyoto で説明できなかった」(SS p.4, excuse (3))。
- **[DISPUTED]** Mochizuki 側: distinct copies は alien arithmetic holomorphic structure の座席 (IUTchI §I1)。

## sub_2 — `iut:F_circ_theta_strip` / `iut:F_circ_q_strip` の共通構造 (SS §2.1.5, p.7–8)

F⊩×µ-prime strip [IUTT-2, Def 4.9] の非アルキメデス的 datum:

```
Gv ↷ o×µ_{k̄v} × N    (N ≃ o_{k̄v}, trivial Gv-action)
```

F⊩×µ-prime strips の圏 ≃「`Gv ↷ o×µ_{k̄v} × N` に abstractly isomorphic な対の圏」の積 (SS p.8)。
- **SS態度**: `iut:F_circ_theta_strip` も `iut:F_circ_q_strip` も同一抽象圏の object。

## sub_3 — `iut:theta_pilot_object`: 抽象 pilot element (SS §2.1.6–2.1.8, p.8–9)

> "Abstract pilot objects … essentially consist of generators of the o_{k̄v}-portions of a
> F⊩×µ-prime strip." (SS p.8, [IUTT-3, Def 3.8])

- Abstract pilot element: `γ_pilot = image of (v(q_v)·γ_v)_v ∈ R⊙`, normalized → `1/(2l)·deg(q_E) ∈ R`.
- **sub-claim**: 具体的 Θ-pilot は `q_v^{j²}` (j=1,…,ℓ*); F⊩×µ_Θ = `Gv ↷ o×µ × ((q_v^{j²}))^N`。
  abstract pilot が arithmetic degree を正しくエンコードするには R⊙,Θ ≅ R を **j² 倍スケール** 必要。
  > "the necessity of this scaling is critical and will play a key role below." (SS p.9)
- **[CLAIMED_BY: SS]** Mochizuki の abstract/concrete 区別の不備が「our main concern の一部」(SS p.8, fn.10)。

## sub_4 — §2.1.9: F⊩×µ-prime strip は両側で canonically the same (SS p.9)

> "The F⊩×µ-prime strips are given by data of the form Gv ↷ o×µ_{k̄v} × N on both sides (at
> finite places), and this data is canonically the same on both sides. It is simply the name of
> the generator of the monoid N that appears that is called Θ respectively q." (SS p.9)

- `iut:F_circ_theta_strip` (HT₁) と `iut:F_circ_q_strip` (HT₂) の差異は生成元の名前のみ。
- **SS態度**: canonical identification が存在 → full poly-isomorphism は不要、obvious isomorphism で十分 (SS p.7, fn.8)。
- **[DISPUTED]** Mochizuki 側: 両側は異なる ring structure 下にあり canonical 同一視は環構造を破壊 (IUTchI Cor.3.7–3.8; 本 repo §2.4)。

## 4 IRI への SS 態度判定

| IRI | SS 箇所 | 態度 |
|---|---|---|
| `iut:theta_hodge_theater` | p.6 sub_1 | 圏同値 ≃ {X}、distinct copies は余剰。`[DISPUTED]` |
| `iut:theta_pilot_object` | §2.1.6–2.1.8 sub_3 | 定義受容、abstract/concrete 区別欠如を批判、j² scaling critical。`[CLAIMED_BY: SS]` |
| `iut:F_circ_theta_strip` | §2.1.5, §2.1.9 sub_2,4 | `Gv ↷ o×µ × N`、両側 canonically same。`[DISPUTED]` |
| `iut:F_circ_q_strip` | §2.1.7, §2.1.9 sub_2,4 | 同上、名前のみ異なる同一構造。`[DISPUTED]` |

- `[DISPUTED]` は `data/claims.json` → `claim:scholze_stix_2018_sub_1` (圏同値・Θ-link)。
- j² scaling 問題 → `claim:scholze_stix_2018_sub_2`。
- 禁止翻訳: perfectoid / prismatic / condensed math 変換不可 (`LLM_CONTEXT.md` §4)。
