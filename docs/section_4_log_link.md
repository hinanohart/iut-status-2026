# Section 4: log-link (`iut:log_link`)

> 3-agent verified.
> Last verified: 2026-05-06.
> drift-zero IRIs: `iut:log_link`, `iut:log_shell`
> Per-side drafts: docs/concepts/log_link.md, docs/concepts/log_link_ss_view.md

## 4.1 Definition (statement-level consensus)

Both sides agree on the following; only interpretation is disputed (§4.2).

- **log-link** is the additive link between Hodge theaters induced by applying
  the p-adic logarithm map at each nonarchimedean place v ∈ V^non:

      log_v : O^×_{F_v} → F_v

  Sources: IUTchIII Def 1.1 (i), Prop 1.3 (i);
  SS §2.1.3, p.6: "The logarithm map defines a well-defined surjective map
  log : o×_K → K that turns multiplication into addition."

- **log : o^×µ_K → K bijectivity** (full consensus): both sides affirmatively
  confirm that this map is well-defined and bijective (surjective, with trivial
  kernel on the torsion-free part after passing to the pro-p completion).
  Sources: IUTchIII Def 1.1 (i); SS p.6 explicit confirmation.

- **log-shell definition** I_v (v ∈ V^bad):

      I_v  :=  p_v^{-1} · log_v(O^×_{K_v})  ⊆  K_v

  The definition is formally uncontested; its role in the proof is outside SS
  scope (§4.5 below).
  Sources: IUTchIII Def 1.1 (i), Intro p.4; SS p.9 passing mention.

- **log-link as endofunctor**: both sides describe log-link as an endofunctor on
  (a suitable category of) Hodge theaters. The name, construction procedure,
  and constituent maps are not in dispute.

## 4.2 [DISPUTED] essential non-triviality vs. identity-equivalence

The core interpretive dispute concerns whether log-link carries genuine
arithmetic content or is trivially equivalent to the identity.

**Mochizuki position** (IUTchIII §1, Intro pp.3–8):
- log-link transports between "mutually alien copies" of arithmetic structures;
  the two Hodge theaters connected by a log-link are not canonically
  identified and must be treated as distinct objects.
- The non-triviality of log-link is precisely what permits the
  log-Kummer correspondence (Thm 3.11 (ii)) and the log-volume upper bound
  at Cor. 3.12 to be non-vacuous.
- The log-theta-lattice (vertical log-links + horizontal Θ^×µ-links) is
  fundamentally non-commutative; this non-commutativity is not an artifact
  but the structural heart of IUTchIII (Def 1.4, Remark 1.4.1 (i)).

**Scholze–Stix position** (SS §2.1.3, p.6; footnote 8, p.7):
- "It follows that the endofunctor log is **naturally equivalent to the
  identity**, with the natural equivalence to the identity given by
  log : log(K) ≅ K." (SS p.6)
- In footnote 8: "if one remembers that all Hodge theaters really come from
  our fixed curve X, there is a completely natural isomorphism Π₁ = π₁(X) = Π₂
  and K₁ ≅ K₂ as K₁ = k̄ = K₂, and thus a natural Π₁ ≅ Π₂-equivariant
  isomorphism log(K₁) ≅ K₁ ≅ K₂. Choosing these 'obvious' isomorphisms did
  not result in any problem that would be solved by allowing some other
  (possibly indeterminate) isomorphism." (SS fn.8, p.7)
- SS does not assert that the log-link construction is incorrect, only that
  its claimed non-triviality is not established.

**Status**: No third-party consensus resolution documented as of 2026-05-06.

## 4.3 [CLAIMED_BY: Mochizuki] log-shell containment and log-volume

These properties appear in IUTchIII Prop 1.2; SS does not analyse them.

- **Containment**: O^▷_{K_v} ⊆ I_v and log_v(O^×_{K_v}) ⊆ I_v (Prop 1.2 (v)).
  I_v contains the Kummer images from both domain and codomain of log-link.

- **Kummer non-compatibility** (Prop 1.2 (iv), [AbsTopIII] Cor 5.5 (iv)):
  the Kummer isomorphisms Ψ_cns(†F) →~ Ψ_cns(†D) and Ψ_cns(‡F) →~ Ψ_cns(‡D)
  are not compatible at element level with the log-link-induced map
  Ψ_cns(†D) →~ Ψ_cns(‡D).

- **Upper semi-compatibility** (Remark 1.2.2 (iii)):
  although element-level equality fails, the containment I_v ⊇ (both Kummer
  images) permits a log-volume upper bound rather than an equality, which
  suffices for Cor. 3.12.

- **Log-volume integration**: Prop 1.2 (iii), Prop 3.9 (iv) establish that
  log-link is compatible with the natural p_v-adic log-volume.

Caveat: SS's critique centres on the Θ-link / degree comparison (§2.2, p.9–10);
it does not directly address whether the above properties are stated correctly.

## 4.4 [CLAIMED_BY: Mochizuki] log-theta-lattice non-commutativity

SS mentions log-theta-lattice only as a paper title (p.10 references); no
structural analysis is given. The following is Mochizuki's uncontested
characterisation (contested only in significance):

- **Vertical arrows** = iterated log-links (F-prime-strip → F-prime-strip).
- **Horizontal arrows** = Θ^×µ- / Θ^×µ_gau- / Θ^×µ_LGP-links.
- The two families of arrows do **not** commute: theta-link depends only on the
  multiplicative monoid structure, while log-link uses both additive and
  multiplicative structure (Remark 1.4.1 (i)).
- Analogy invoked: non-commutativity of Witt vector / Frobenius operations in
  p-adic Hodge theory (IUTchIII Intro p.7).
- Formal definition: IUTchIII Def 1.4.

## 4.5 Forbidden translations

- "log-shell" must not be rendered as 「対数殻」 or any ad hoc coinage; use
  the term log-shell (原語そのまま).
- log-theta-lattice ≠ theta-link: vertical (log-link) and horizontal
  (theta-link) are distinct arrows in the lattice.
- "upper semi-compatibility" must not be read as "commutativity" or
  "approximate equality"; it is a containment statement, not an equation.
- "naturally equivalent to the identity" (SS claim, §4.2) and
  "non-trivial link between alien copies" (Mochizuki claim, §4.2) must be
  tagged [DISPUTED] and never merged into a single neutral statement.

## Cross-reference

- entities.json: `iut:log_link`, `iut:log_shell`, `iut:HodgeTheater`,
  `iut:log_theta_lattice`
- claims.json: `claim:scholze_stix_2018_main`, `claim:mochizuki_2018_response`
- Related sections: Section 3 (theta-link, horizontal arrows of the lattice);
  Section 5 (Cor. 3.12, log-volume upper bound computation)

## Verification log

| Item | Votes | Status |
|---|---|---|
| log : o^×µ_K → K bijectivity | 3/3 | consensus ✅ |
| log-shell definition I_v = p_v^{-1} log_v(O^×) | 3/3 | consensus ✅ |
| log-link as endofunctor (construction) | 3/3 | consensus ✅ |
| essential non-triviality vs. identity-equivalence | 0/3 | [DISPUTED] |
| log-shell containment O^▷ ⊆ I_v | 1/3 | [CLAIMED_BY: Mochizuki] |
| Kummer non-compatibility (Prop 1.2 (iv)) | 1/3 | [CLAIMED_BY: Mochizuki] |
| upper semi-compatibility (Rem 1.2.2 (iii)) | 1/3 | [CLAIMED_BY: Mochizuki] |
| log-theta-lattice non-commutativity | 1/3 | [CLAIMED_BY: Mochizuki] |
| Forbidden translations | 3/3 | consensus ✅ |

## Sources

| Reference | Content |
|---|---|
| IUTchIII Def 1.1 (i)(ii) | log-link, log-shell formal definition |
| IUTchIII Prop 1.2 (i)(iii)(iv)(v) | coricity / log-volume / Kummer non-compat / containment |
| IUTchIII Prop 1.3 (i) | log-link between Hodge theaters |
| IUTchIII Def 1.4 | log-theta-lattice |
| IUTchIII Cor 3.12; Thm 3.11 (ii) | log-volume upper bound; log-Kummer correspondence |
| SS §2.1.3 pp.6–7; fn.8 p.7 | log-link construction + "naturally equivalent to identity" claim |
| SS p.9 | log-shell passing mention (pilot object encoding) |
| SS p.10 refs | log-theta-lattice title only |

- IUTchIII PDF: https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
- IUTchIII DOI (PRIMS 2021): https://doi.org/10.4171/PRIMS/57-1-3
- SS PDF (Wayback): https://web.archive.org/web/2024/https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
- Alien Copies survey: https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf
