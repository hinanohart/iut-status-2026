# 3b: IUTchII Cor. 4.10 + Θ×µ — SS-side deep view

> Source primary: Scholze–Stix 2018, "Why abc is still a conjecture"
> URL: https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
> Version: July 16, 2018 (10 pp.)
> Extracted via pymupdf from cached PDF.
> Last updated: 2026-05-06.

---

## 1. MOCHIZUKI POSITION

IUTchII Cor. 4.10 (iii) constructs the **F⊩×µ-prime-strip** version of the
Θ-link as a full poly-isomorphism `F⊩×µ_Θ ~→ F⊩×µ_q` between the Θ-pilot
strip (source) and q-pilot strip (target).  The F⊩×µ-layer (Def. 4.9 (vii))
records `G_v ⟲ o^{×µ}_{k̄_v} × N` together with a global realified Frobenioid;
the F⊩-layer of IUTchI Cor. 3.7 is the coarser predecessor.

Mochizuki's position is that the transport across the Θ-link is non-trivial
because the two Hodge theaters carry **mutually alien** copies of ring-theoretic
structure; the j²-scaling of the Θ-pilot's arithmetic degree relative to the
q-pilot is the operative content.  The concrete embeddings
`Θ_v ~ (q^{j²}_v)_{j=1,...,ℓ*}` and `q_v` into `o_{k̄_v}` are **remembered
inside each Hodge theater** and are the source of the non-trivial comparison.

- Sources: IUTchII Def. 4.9 (vii), Cor. 4.10 (iii); IUTchI Cor. 3.7 (i);
  "Mathematics of Mutually Alien Copies" §3.3 (ii), pp. 60–62.

## 2. SCHOLZE–STIX POSITION

### 2a. Scope: what SS directly analyzes in their 2018 report

SS work **entirely at the F⊩×µ-prime-strip level** throughout §2.  They
explicitly describe (§2.1.5, p. 7) the F⊩×µ-prime strip data as:

> "at nonarchimedean places, given by the pair G_v ⟲ o^{×µ}_{k̄_v} × o_{k̄_v}"
> (where o_{k̄_v} ≅ N with trivial G_v-action)

and note (§2.1.5, p. 8):

> "the category of F⊩×µ-prime strips is equivalent to the product of the
> categories of pairs … abstractly isomorphic to G_v ⟲ o^{×µ}_{k̄_v} × N,
> over all places v."

**SS p. 4 "Mochizuki agreed F⊩×µ simplification OK"** — verbatim:

> "(1) During our discussion in Kyoto, Mochizuki agreed that some of these
> simplifications are OK, for example regarding the critical notion of
> F⊩×µ-prime strips below."  (SS §2, p. 4)

This is explicitly limited to F⊩×µ **simplifications** — i.e., that the
description `G_v ⟲ o^{×µ}_{k̄_v} × N` correctly captures the local data of
the strip.  It does **not** constitute Mochizuki's agreement on the SS
conclusion (canonical triviality of the link).

### 2b. IUTchII Cor. 4.10 — direct engagement status

SS **cite IUTchII** only in the reference list as "[IUTT-2] Mochizuki, S.,
Inter-universal Teichmuller Theory II: Hodge-Arakelov-theoretic Evaluation"
(SS p. 10).  The body of the SS report does **not** discuss or quote any
specific result internal to IUTchII beyond the F⊩×µ-strip definition (Def. 4.9)
that underlies the Θ-link construction.  Cor. 4.10 is not cited by number in the
SS body text.

**Implication:** SS's argument operates at the F⊩×µ-strip layer, which is
the output layer of IUTchII Cor. 4.10 (iii).  SS implicitly accept the
strip construction (they agree on its shape) and dispute the interpretation
of the Θ-link built from it, not the internal mechanism of Cor. 4.10 itself.

### 2c. Θ-times-µ (Θ×µ / F⊩×µ) occurrences in SS

| Location | Content |
|----------|---------|
| SS p. 4 §2 intro | "Mochizuki agreed … regarding the critical notion of F⊩×µ-prime strips" |
| SS §2.1.5 pp. 7–8 | Full definition: `G_v ⟲ o^{×µ}_{k̄_v} × N`; global realified Frobenioid with canonical γ_can |
| SS §2.1.7 p. 8 | Concrete q-pilot strip: `G_v ⟲ o^{×µ}_{k̄_v} × q^N_v` |
| SS §2.1.8 pp. 8–9 | Concrete Θ-pilot strip: `G_v ⟲ o^{×µ}_{k̄_v} × ((q^{j²}_v)_{j=1,…,ℓ*})^N` |
| SS §2.1.9 p. 9 | Θ-link as full poly-iso between F⊩×µ-strips; canonical identification claim |
| SS §2.2 pp. 9–10 | R⊙,Θ ≅ R⊙,q ≅ R via γ_can → j²-scalars must be omitted → empty inequality |

### 2d. Θ-gau

The term "Θ-gau" (theta-gauge / ΘNF-Hodge theater) does **not appear** in
SS 2018.  SS reduce to the F⊩×µ-strip layer and do not engage with the
ΘNF-Hodge theater or Θ-gau normalization present in IUTchI §4 / IUTchII.

### 2e. Hodge-Arakelov evaluation map

The Hodge-Arakelov evaluation map (IUTchII Cor. 4.10 (i)–(ii); evaluation of
the theta-function at 2ℓ-torsion) is **not discussed in SS 2018**.  SS note
in §2.1.8, fn. 11 (p. 8) that Mochizuki "encodes the Θ-function" via
"divisors on tempered coverings of X", acknowledging the mechanism exists, but
they state it "plays no role for us" at the strip level they analyze.

> "There is one notable more interesting case related to the monoid of divisors
> on tempered coverings of X at places of bad reduction, by means of which
> Mochizuki encodes the Θ-function."  (SS §2.1.2 fn. 5, p. 5)

**Implication:** Hodge-Arakelov evaluation is acknowledged as a pre-existing
construction but is treated as **outside SS scope**: they analyze only the
coarse F⊩×µ-strip output, not the evaluation map that produces it.

### 2f. λ (lambda)

The symbol λ appears in SS p. 5 fn. 3 solely in the geometric context
`P¹ \ {0,1,λ,∞}` (Belyi / Legendre parameter for the elliptic curve E).
It does **not** appear as an IUTchII-internal lambda (e.g., log-volume
normalisation factor or Hodge-Arakelov lambda).

## 3. ALTERNATIVE / THIRD-PARTY VIEW

Not applicable for this sub-section (Joshi 2021–2024 addresses Cor. 4.10
separately; outside SS-side scope here).

## 4. PENDING

- Mochizuki's point-by-point response (RIMS, 2018) addresses the "agreed on
  simplifications" claim: Mochizuki contests that his agreement was limited to
  the description of the strip data, **not** to the legitimacy of SS's
  subsequent canonical identification step (`R⊙,Θ ≅ R⊙,q via γ_can`).
  Source status: Mochizuki 2018 response PDF (RIMS); to be extracted
  separately as `3b_iutchII_cor_4_10_deep_mochizuki_response.md`.

## 5. UNRESOLVED

Whether the canonical identification `R⊙,Θ ≅ R⊙,q ≅ R` (SS §2.2, p. 10)
is or is not legitimate in the IUTchII Cor. 4.10 framework remains the core
unresolved dispute.  Neither the PRIMS publication (2021) nor any independent
verifier has adjudicated this as of 2026-05-06.

---

## Source table

| Claim | Source | Page | DOI / URL |
|-------|--------|------|-----------|
| F⊩×µ simplification agreed | SS 2018 | 4 | https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf |
| F⊩×µ strip shape `G_v ⟲ o^{×µ} × N` | SS 2018 §2.1.5 | 7–8 | ibid. |
| Θ-link canonical identification | SS 2018 §2.1.9 | 9 | ibid. |
| Empty inequality from j²-omission | SS 2018 §2.2 | 9–10 | ibid. |
| IUTchII Cor. 4.10 (iii) F⊩×µ construction | IUTchII | — | DOI 10.4171/PRIMS/57-1-2 |
| IUTchI Cor. 3.7 F⊩-version | IUTchI | 88 | DOI 10.4171/PRIMS/57-1-1 |
| Mutually alien copies motivation | Alien Copies §3.3 (ii) | 60–62 | https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf |

---

## Verification log

- SS scope at F⊩×µ-layer (not deeper into Cor. 4.10): confirmed from PDF full text
- "Mochizuki agreed" passage (SS p. 4): verbatim extracted
- Θ-gau absent from SS 2018: confirmed (no occurrence in 10-page PDF)
- Hodge-Arakelov evaluation map: acknowledged in SS fn. 5 but stated out of scope
- λ in SS: only Legendre parameter, not IUTchII-internal (confirmed)
- IUTchII Cor. 4.10 number-cited in SS body: absent (reference list only)
