# Section 5: multiradial algorithm + indeterminacies (`iut:multiradial_algorithm`, `iut:Ind1`, `iut:Ind2`, `iut:Ind3`)

> 3-agent verified.
> Last verified: 2026-05-06.
> drift-zero IRIs: `iut:multiradial_algorithm`, `iut:Ind1`, `iut:Ind2`, `iut:Ind3`
> Per-side drafts: docs/concepts/multiradial.md, docs/concepts/multiradial_ss_view.md

## 5.1 multiradial algorithm (statement-level consensus)

Both sides agree on the following; only interpretation and consequences are disputed (§5.3–5.4).

- **multiradial algorithm** is introduced in IUTchIII Thm 3.11 (Multiradial Algorithms
  via LGP-Monoids/Frobenioids). It provides a representation of splitting monoids of
  LGP-monoids that is "visible" from an alien arithmetic holomorphic structure — i.e.,
  from a vertical line other than the one where the structure was originally defined.

- **Cor. 3.12 statement** (IUTchIII p.173–174):

      − |log(Θ)| ≥ − |log(q)|

  The inequality holds after subjecting the multiradial representation to
  indeterminacies (Ind1), (Ind2), (Ind3).
  Sources: IUTchIII Thm 3.11 (p.153–158), Cor. 3.12 (p.173–174).
  DOI: https://doi.org/10.4171/PRIMS/57-1-3
  PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf

- SS confirms that Thm 3.11 is **not false** and that Cor. 3.12 invokes indeterminacies
  Ind 1,2,3 "(without which the conclusion would be obviously false)".
  Source: SS 2018, p.9.
  URL: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf

- SS does **not** individually re-evaluate Ind1/Ind2/Ind3; its critique targets
  Cor. 3.12 as a whole.

## 5.2 [CLAIMED_BY: Mochizuki] Ind1, Ind2, Ind3 — technical detail

SS does not individually dispute these definitions; labelled [CLAIMED_BY: Mochizuki]
because SS's scope is Cor. 3.12's validity, not the content of each indeterminacy.

| ID   | Domain                                               | Character                           | Source                          |
|------|------------------------------------------------------|-------------------------------------|---------------------------------|
| Ind1 | Aut of procession Prc(ⁿ˒◦D⁺): label permutations of S±_{j+1} + Aut of D⁺-prime-strips | étale-like / combinatorial | IUTchIII Thm 3.11 §(i), p.154 |
| Ind2 | Independent copies of Ism acting on direct summands of I^Q(S±_{j+1}; ⁿ˒◦D⁺_{v_Q}); Z×-indeterminacy on O^{×μ} | Frobenius-like / Z×-indet | IUTchIII Thm 3.11 §(i), p.154 |
| Ind3 | "upper semi-compatibility" of log-Kummer correspondence across log-links (inclusions ⊆ at V^non, surjections ↠ at V^arc) | log-volume / upper semi-compat | IUTchIII Thm 3.11 §(ii), p.156 |

IUTchIII Introduction (p.11–12):
> "This passage to the multiradial representation is obtained by admitting the following
> three types of indeterminacy: (Ind1) … (Ind2) … (Ind3) …"

Verbatim definitions: see docs/concepts/multiradial.md §"Indeterminacies".

## 5.3 [DISPUTED] essential vs. trivial — Mochizuki ↔ SS

**Mochizuki position** (IUTchIII Thm 3.11, Cor. 3.12; "Alien Copies" survey §3):
- multiradial = framework enabling comparison across alien arithmetic holomorphic
  structures; uniradial representation cannot be referenced from a different
  vertical line, making the comparison impossible.
- (Ind1)(Ind2)(Ind3) adopted, yet the resulting inequality is non-trivial and
  connects to diophantine results in IUTchIV.
- Source: IUTchIII p.153–174; Mochizuki "Alien Copies" survey §3
  (https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf)

**SS position** (SS 2018, p.10, fn.12):
- j² monodromy: introducing scalars j² on the left side of the diagram (1.5)
  causes the whole diagram to have "monodromy j²", i.e. inconsistency.
- Removing j² yields `−|log(Θ)| ≈ −|log(Θ)|` — a tautology, hence "empty inequality".
- Thm 3.11 under this reading "does not become false, but **trivial**" (fn.12).
- Source: SS 2018, p.10; fn.12.

Neither side has retracted; dispute is live as of 2026-05-06.
Encoded as `claim:scholze_stix_2018_main` (j² monodromy → empty inequality)
and `claim:scholze_stix_2018_sub_3` (Thm 3.11 trivial).

## 5.4 [DISPUTED] indeterminacies blurring — quantitative evaluation

**SS position** (SS 2018, p.10):
- For indeterminacies to absorb j², blurring would need to contribute a factor ≥ O(ℓ²).
- At that scale the resulting inequality becomes **useless** (no non-trivial lower bound).
- Logical structure: "indeterminacies too small → diagram inconsistent; too large → inequality vacuous."

**Mochizuki position** (IUTchIII Cor. 3.12; 2018 Reply):
- Indeterminacies are absorbed within the multiradial framework; the bound remains
  meaningful because the blurring is controlled by the geometry of the prime-strips.
- Mochizuki 2018 Reply is outside the scope of these per-side drafts.

Dispute status: unresolved. No published referee adjudication as of 2026-05-06.
Encoded as `claim:scholze_stix_2018_main`.

## 5.5 Forbidden translations

The following phrasings introduce scope violations and are prohibited in this document:

| Forbidden phrase | Reason |
|---|---|
| "scheme-theoretic interpretation of Ind1/2/3" | Original text strictly distinguishes étale-like / Frobenius-like |
| "Ind2 = Galois indeterminacy" | Original text specifies Z×-indeterminacy on O^{×μ}, not Galois action |
| "Cor. 3.12 proves abc conjecture directly" | Cor. 3.12 gives log-volume inequality only; diophantine application is in IUTchIV |
| "multiradial = functorial" | Multiradial is broader than functoriality (cf. Thm 3.11 final remark) |
| "SS says Thm 3.11 is false" | SS says "trivial", not "false" (fn.12 verbatim) |

## Cross-reference

- entities.json: `iut:multiradial_algorithm`, `iut:Ind1`, `iut:Ind2`, `iut:Ind3`, `iut:Cor.3.12`
- claims.json: `claim:scholze_stix_2018_main`, `claim:scholze_stix_2018_sub_3`, `claim:mochizuki_2018_response`

## Verification log

| Item | Verdict |
|---|---|
| 5.1 multiradial algorithm statement-level | 3/3 ✅ consensus |
| 5.2 Ind1/Ind2/Ind3 technical detail | 1/3 [CLAIMED_BY: Mochizuki] — SS scope outside |
| 5.3 essential vs. trivial | 0/3 [DISPUTED] |
| 5.4 blurring quantitative evaluation | 0/3 [DISPUTED] |
| 5.5 forbidden translations | 3/3 ✅ consensus |
