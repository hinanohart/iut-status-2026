# Section 4a: log-link IUTchIII Def 1.1 — SS-side deep view

> SS-side draft / 2026-05-06.  
> Scope: `iut:log_link_construction`, `iut:log_link_compatibility`, `iut:log_volume`.  
> Extends: `docs/concepts/log_link_ss_view.md` (general SS view, 119 lines).

## `iut:log_link_construction` — [ACCEPT] construction-level

SS §2.1.3 p.6, citing IUTchIII Def 1.1 (i):

> "The logarithm map defines a well-defined surjective map `log : o×_K → K` that
> turns multiplication into addition. […] the logarithm induces a bijection
> `log : o×µ_K →~ K`."

> "Mochizuki defines an endofunctor log […] the multiplication on log(K) is
> defined via transport of structure along the bijection `log : log(K) = o×µ_K →~ K`."

> "It follows that the endofunctor log is **naturally equivalent to the identity**,
> with the natural equivalence to the identity given by `log : log(K) ≅ K`."
> — SS p.6

Bijection and endofunctor construction accepted without qualification.
Non-triviality is the disputed point: see `section_4_log_link.md` §4.2 [DISPUTED].

## `iut:log_link_compatibility` — [CLAIMED_BY: Mochizuki]

SS §2.1.3 p.7 states morphism data only:

> "the log-link consists of an isomorphism Π₁ ≅ Π₂ and an isomorphism
> `o_{log(K₁)} ≅ o_{K₂}` of topological monoids equivariant for the Π₁ ≅ Π₂-actions."

Footnote 8 (p.7) on poly-isomorphism:

> "there is a completely natural isomorphism Π₁ = π₁(X) = Π₂ and K₁ ≅ K₂ as
> K₁ = k̄ = K₂ […]. Choosing these 'obvious' isomorphisms did not result in any
> problem that would be solved by allowing some other (possibly indeterminate)
> isomorphism."

SS does **not** address: HT-structure preservation (Prop 1.3 (i)),
Kummer non-compatibility (Prop 1.2 (iv)), upper semi-compatibility (Rem 1.2.2 (iii)).
All three remain [CLAIMED_BY: Mochizuki].

## `iut:log_volume` — [CLAIMED_BY: Mochizuki]

No dedicated SS analysis. [IUTT-4] title ("Log-volume Computations…") appears in
p.10 references only. Log-shell appears once (p.9) as encoding medium for pilot
objects; not independently analysed.

Closest SS engagement is §2.2 p.10 "empty inequality" argument:

> "with consistent identifications of copies of real numbers, one must in (1.5)
> omit the scalars j² that appear, which leads to an **empty inequality**."
> — SS p.10

This targets R-vector space identification at Cor. 3.12 step (xi), not the
log-volume measure as defined in IUTchIII Prop 1.2 (iii) / Prop 3.9 (iv).

## Summary

| Entity | SS stance | Status |
|---|---|---|
| `iut:log_link_construction` | bijection + endofunctor confirmed (p.6) | [ACCEPT] construction-level |
| `iut:log_link_compatibility` | morphism data only; HT-preservation not analysed (p.7, fn.8) | [CLAIMED_BY: Mochizuki] |
| `iut:log_volume` | title-only in refs; "empty inequality" indirect (p.9–10) | [CLAIMED_BY: Mochizuki] |

**Forbidden**: "SS accepts log-link" ≠ accepts non-triviality.
"empty inequality" ≠ log-volume definition error.

## Sources

- SS §2.1.3 p.6 — `log_link_construction` verbatim
- SS §2.1.3 p.7 + fn.8 — `log_link_compatibility` morphism data
- SS §2.2 p.9–10; p.10 refs — `log_volume` indirect / title-only
- SS PDF: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- IUTchIII: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
