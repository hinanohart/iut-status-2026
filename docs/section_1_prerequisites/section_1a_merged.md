# Section 1a: Anabelian Geometry (deep dive)

> 3-agent verified.
> Last verified: 2026-05-06.
> Parent: docs/section_1_prerequisites.md
> drift-zero IRIs: iut:absolute_anabelian, iut:tempered_rigidity, iut:mono_anabelian, iut:cuspidalization
> Per-side drafts: docs/section_1_prerequisites/1a_anabelian_deep.md (Mochizuki), 1a_anabelian_deep_ss_view.md (SS)
> Monitor verdict (2026-05-06): belyi_cuspidalization EXCLUDED (IUT proof body locator absent); 5→4 entities; IRI flat pattern enforced.

---

## 1a.1 Absolute anabelian framework (`iut:absolute_anabelian`)

### Consensus (statement-level)

- Mochizuki, *Topics in Absolute Anabelian Geometry I* (PRIMS 2012), Introduction pp. 2–3.
  Definition: algorithms "phrased in language that only depends on the structure of the input data as a profinite group."
  Shift from fully-faithfulness theorems to functorial group-theoretic algorithms operating on abstract profinite groups.
- SS p.5 Theorem 7 (citing [Anab3, Thm 1.9, Cor 1.10]): introduced as a **"striking result"** — definitional level accepted without objection.
  3/3 consensus on existence and correctness of the framework.

### [CLAIMED_BY: Mochizuki] essential role at Cor.3.12

- Mochizuki (IUTchI §I3, pp. 21–22): the absolute algorithmic stance is the reason IUT can "look inside" one Hodge theater from another — fundamental groups are used *as software*, not as morphism containers.
- SS (Remark 9, p.5): "we could not find the point where it is essential to work with fundamental groups — there are no additional isomorphisms of fundamental groups that do not come from isomorphisms of schemes."
  Dispute is over *deployment* at Cor.3.12, not over the framework's correctness.

**Sources**: Topics I <https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20I.pdf>; SS PDF p.5 Thm 7 + Remark 9.

---

## 1a.2 Tempered anabelian rigidity (`iut:tempered_rigidity`)

### Consensus (3/3)

- Mochizuki, *The Étale Theta Function and its Frobenioid-theoretic Manifestations* (EtTh, 2008/2022), Theorem 1.6, pp. 22–23.
  Any isomorphism γ : Π^tp_{X_α} →̃ Π^tp_{X_β} of tempered fundamental groups maps the étale theta class to a ℤ-conjugate and preserves decomposition groups and canonical integral structures of cusps.
  Companion: Theorem 1.10, pp. 27–28 (constant-multiple rigidity: values of η̈^{Θ,ℤ} preserved up to {±1}).
- SS fn.5 + p.8 §2.1.8: "Mochizuki devises an **ingenious algorithm** to recover this data very directly from the data of π₁(X) acting on a certain monoid of divisors on tempered coverings of X."
  No objection raised; described as an effective technical device.

**Source**: EtTh <https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf>; SS p.8.

---

## 1a.3 Mono-anabelian reconstruction (`iut:mono_anabelian`)

### [CLAIMED_BY: Mochizuki]

- Mochizuki, *Topics in Absolute Anabelian Geometry III* (PRIMS 2015), §I2 p.7 (definition); Theorem 1.9 pp. 36–38; Corollary 1.10 pp. 41–44; Corollary 3.6 pp. 78–79.
  Definition: reconstruction algorithm whose input is a *single* abstract arithmetic fundamental group (not a pair with isomorphism). Strictly stronger than bi-anabelian (mono ⟹ bi; converse false in the IUT context, Cor 3.7).
  "such a group-theoretic geometric framework is precisely what is furnished by the enhancement of absolute anabelian geometry — which we shall refer to as mono-anabelian geometry."
  Critical for IUT: Θ-link and log-link do not respect ring structures; mono-anabelian framework survives log-Frobenius (Cor 3.6); bi-anabelian does not (Cor 3.7).
- SS PDF: terms "mono-anabelian" and "bi-anabelian" do not appear (0 hits, 10-page PDF, keyword search confirmed).
  → No SS acknowledgment, no SS refutation.

**Source**: Topics III <https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20III.pdf>

---

## 1a.4 Cuspidalization (`iut:cuspidalization`)

### [CLAIMED_BY: Mochizuki]

- Mochizuki, *Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves* (Publ. RIMS 2007), Abstract; Theorem 1.16, p.25.
  Given ΠX →̃ ΠY (abstract group isomorphism of étale fundamental groups of proper hyperbolic curves), Thm 1.16 establishes: field type, type (g,r), decomposition groups, and compatibility with Galois quotients are preserved; induces compatible isomorphism of maximal cuspidally abelian quotients Π^{c-ab}_{UX×X} →̃ Π^{c-ab}_{UY×Y}, well-defined up to cuspidally inner automorphisms.
  Prerequisite tool for mono-anabelian Theorem 1.9 (Topics III, p. 48).
- SS PDF: term "cuspidalization" does not appear (0 hits, confirmed).
  → No SS acknowledgment, no SS refutation.

**Source**: Cuspidalizations 2007 <https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf>

---

## 1a.5 [DISPUTED] Essential role of anabelian geometry at Cor.3.12 (cross-cutting 1a.1–1a.4)

- **Mochizuki** (IUTchI §I3): anabelian methodology is the foundation enabling IUT to pass information across Θ-links and log-links — without mono-anabelian transport, the log-link would dismantle the ring structure irreversibly.
  Proponents: Mochizuki, Hoshi, Yamashita.
- **Scholze-Stix** (Remark 9, p.5, verbatim): "Anabelian geometry is supposed to be the key to Mochizuki's proof. However, here we see that in the IUTT papers, we are (for the essential part) in a situation where anabelian geometry holds true in the sense that geometry and group theory are equivalent. We could not find the point where it is essential to work with fundamental groups."
  SS fn.4: "Such isomorphisms exist for Galois groups of p-adic fields, but this did not seem to enter the discussion in a critical way."
  Encoded as `claim:scholze_stix_2018_sub_2`.
- Resolution: unresolved as of 2026-05.

---

## Forbidden translations

- Do NOT conflate `iut:mono_anabelian` with `iut:absolute_anabelian`; Topics III defines mono-anabelian as a strict *enhancement* of absolute anabelian (Topics III §I2, p.7).
- Do NOT describe `iut:cuspidalization` as a global result; Thm 1.16 is specific to proper hyperbolic curves over finite or nonarchimedean local fields.
- Do NOT translate any of these concepts into perfectoid spaces, diamonds, or condensed mathematics.
- Do NOT introduce `iut:belyi_cuspidalization` as a top-level entity — monitor agent excluded it (IUT proof body locator absent); it appears only as a technique internal to the mono-anabelian algorithm (Topics III Thm 1.9, step (a)).

---

## Cross-reference

- entities_1a_merged.json: `iut:absolute_anabelian`, `iut:tempered_rigidity`, `iut:mono_anabelian`, `iut:cuspidalization` + 3 paper records
- claims_1a_merged.json: `claim:mochizuki_anabelian_essential`, `claim:tempered_rigidity_acknowledged`, `claim:scholze_stix_2018_sub_2` (existing)
- Parent entities.json: `iut:anabelian_geometry` (top-level ancestor, introduced_by: Grothendieck 1983)

---

## Verification log

| Section | IRI | Verdict | Notes |
|---|---|---|---|
| 1a.1 | `iut:absolute_anabelian` | 3/3 consensus ✅ | SS p.5 Thm 7 "striking result" |
| 1a.2 | `iut:tempered_rigidity` | 3/3 consensus ✅ | SS p.8 "ingenious algorithm" |
| 1a.3 | `iut:mono_anabelian` | [CLAIMED_BY: Mochizuki] | SS 0 hits |
| 1a.4 | `iut:cuspidalization` | [CLAIMED_BY: Mochizuki] | SS 0 hits |
| 1a.5 | essential at Cor.3.12 | [DISPUTED] | claim:scholze_stix_2018_sub_2 |
| — | `iut:belyi_cuspidalization` | ❌ EXCLUDED by monitor agent | IUT proof body locator absent |
