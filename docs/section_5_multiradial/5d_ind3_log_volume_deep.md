# Section 5d: Ind3 log-volume deep — Mochizuki-side draft

> status: mochizuki-side draft | 3-agent verify: pending | verified_at: 2026-05-06
> source: IUTchIII Thm 3.11 §(ii) (PDF pp. 155–156); Prop 3.5 §(ii)(a)(b) (PDF pp. 103–104); Prop 3.9 §(iv) (PDF pp. 116–117)
> new IRIs: `iut:Ind3_upper_semi_compat_kummer`, `iut:Ind3_log_volume_absorption`
> IRI flat; v0.2 schema
> DOI: https://doi.org/10.4171/PRIMS/57-1-3

---

## 5d.1 Background: Ind3 and the log-Kummer correspondence

Thm 3.11 §(ii) establishes a system of Kummer isomorphisms connecting holomorphic data
`(n,m)` to vertically coric data `(n,◦)`. Their behaviour as `m ∈ Z` varies is controlled
by two complementary properties: upper semi-compatibility at the set level (Ind3), and
*precise* log-volume compatibility ([precisely!], PDF p. 155).

**Key tension**: a single Kummer isomorphism at fixed `m` *fails* to be log-link-compatible
(Prop 3.5, proof note, PDF p. 105). The log-Kummer correspondence resolves this by replacing
the single iso with the totality of pre-composites of Kummer isomorphisms with iterates of
log-links, as described in detail in Prop 3.5 §(ii)(a)(b).

> Source: IUTchIII Thm 3.11 §(ii), PDF p. 154–156; Prop 3.5 §(ii) intro, PDF p. 103.

---

## 5d.2 `iut:Ind3_upper_semi_compat_kummer` — Definition

**IUTchIII Thm 3.11 §(ii), (Ind3) verbatim** (PDF p. 155–156):

> "(Ind3) as one varies m ∈ Z, the isomorphisms of (a) are 'upper semi-compatible',
> relative to the log-links of the n-th column of the LGP-Gaussian log-theta-lattice
> under consideration, in a sense that involves certain natural inclusions '⊆' at
> vQ ∈ V^non_Q and certain natural surjections '↠' at vQ ∈ V^arc_Q — cf.
> Proposition 3.5, (ii), (a), (b), for more details."

The isomorphisms of "(a)" are the local mono-analytic tensor packet isos
`IQ(S±_{j+1}; n,m F_{vQ}) ∼→ IQ(S±_{j+1}; n,◦ D^⊢_{vQ})` [Prop 3.2, 3.4, 3.5].

**Prop 3.5 §(ii)(a) — nonarchimedean** (PDF p. 103): `I(S±_{j+1} F(n,◦ D≻)_{vQ})` *contains*
the images of Galois-invariant unit subgroups under Kummer + log-link iterates → **inclusion ⊆**.

**Prop 3.5 §(ii)(b) — archimedean** (PDF p. 104): the closed unit ball contains images of
(1) unit groups `(Ψ_cns(n,m F≻)_{|t|})^×_v` and (2) closed balls of radius π via tensor
Kummer isos → **surjection ↠**.

The one-sided nature arises because `log: O^× → k` (Rem 1.2.2-iii) compresses units strictly
into the coric log-shell; no equality can hold for individual `m`.

> Sources: IUTchIII Thm 3.11 §(ii)(Ind3), PDF p. 155–156; Prop 3.5 §(ii)(a)(b), PDF pp. 103–104.

---

## 5d.3 `iut:Ind3_log_volume_absorption` — Theorem

**IUTchIII Thm 3.11 §(ii) final clause, verbatim** (PDF p. 155):

> "Finally, as one varies m ∈ Z, the isomorphisms of (a) are [precisely!] compatible,
> relative to the log-links of the n-th column of the LGP-Gaussian log-theta-lattice
> under consideration, with the respective log-volumes [cf. Proposition 3.9, (iv)]."

**Prop 3.9 §(iv)(b) verbatim** (PDF p. 116):

> "(b) At the level of the Q-spans of log-shells 'IQ((−))' … the log-volumes of (a)
> indexed by (n, m) are compatible — in the sense discussed in Propositions 1.2, (iii);
> 1.3, (iii) — with the corresponding log-volumes indexed by (n, m−1), relative to
> the log-link n,m−1 HT Θ±ellNF → n,m HT Θ±ellNF."

The exclamation mark "[precisely!]" is Mochizuki's own emphasis. Despite the set-level
upper semi-compatibility of (Ind3), the log-volume measure on Q-spans of log-shells is
*exactly* preserved across log-links. This is the absorption property: Ind3 does not
distort the log-volume used in Cor 3.12.

**Role at Cor 3.12 Step (xi)**: comparison `−|log(Θ)| ≥ −|log(q)|` applies log-volumes to
`n,◦R^LGP`. The absorption property ensures the Ind3 set-theoretic containment does not
enlarge the log-volume estimate. Rem 3.9.4 (PDF p. 119) provides a measure-theoretic
formulation.

> Sources: IUTchIII Thm 3.11 §(ii) final clause, PDF p. 155; Prop 3.9 §(iv)(b), PDF pp. 116–117.

---

## 5d.4 Comparative summary

| Property | `Ind3_upper_semi_compat_kummer` | `Ind3_log_volume_absorption` |
|---|---|---|
| Level | Set-theoretic (Kummer iso images) | Measure-theoretic (log-volume on Q-spans) |
| Behaviour | One-sided: ⊆ at non-arch, ↠ at arch | Precise equality across log-links |
| Key prop | Prop 3.5 §(ii)(a)(b) | Prop 3.9 §(iv)(b) |
| Keyword | "upper semi-compatible" | "[precisely!] compatible" |

---

## 5d.5 SS-side: scope

pymupdf search SS 2018 (10 pages, 2026-05-06):

| Term | Hits | Location |
|---|---|---|
| "blurring" | 1 | SS p. 10 |
| "upper semi" / "semi-compat" / Prop 3.5 / Prop 3.9 | 0 | — |
| "(Ind 1,2,3)" | 1 | SS p. 9 (collective) |

SS p. 10 (verbatim): "he claimed that up to the 'blurring' given by certain indeterminacies
the diagram does commute; it seems to us that this statement means that the blurring must
be by a factor of at least O(ℓ²) rendering the inequality thus obtained useless."

SS treats Ind1–3 collectively and does not analyze the internal structure of Ind3.
The `O(ℓ²)` blurring argument functions as an *indirect* challenge to
`iut:Ind3_log_volume_absorption`: if the log-volume were enlarged by `O(ℓ²)` due to the
set-level containment, Cor 3.12 yields a trivial bound. Mochizuki's position is that Prop 3.9
§(iv) prevents this enlargement. The existing entity `claim:ss_o_l_squared_blurring_useless`
records the SS p. 10 claim; both new entities connect to it indirectly.

Status: **[CLAIMED_BY: Mochizuki]**; **[OUT_OF_SCOPE: Scholze-Stix]** (internal Ind3 structure);
**[DISPUTED]** via `O(ℓ²)` at Cor 3.12 level.

---

## Sources

| Reference | Content |
|---|---|
| IUTchIII Thm 3.11 §(ii) (Ind3), PDF p. 155–156 | Ind3 verbatim; isomorphisms of (a) |
| IUTchIII Prop 3.5 §(ii)(a)(b), PDF pp. 103–104 | ⊆ at non-arch; ↠ at arch |
| IUTchIII Thm 3.11 §(ii) final clause, PDF p. 155 | "[precisely!]" log-volume compat |
| IUTchIII Prop 3.9 §(iv)(b), PDF pp. 116–117 | log-link compatibility of log-volumes |
| SS 2018 pp. 9–10 | "(Ind 1,2,3)" collective; "blurring" O(ℓ²) |

- IUTchIII PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
- IUTchIII PRIMS DOI: https://doi.org/10.4171/PRIMS/57-1-3
- SS 2018 PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
