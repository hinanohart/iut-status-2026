# Section 4d: log-theta-lattice — Deep Properties (Mochizuki-side draft)

> Schema: v0.2
> Source: IUTchIII Def 1.4 (p. 45); Rem 1.4.1 (i)(ii)(iii) (pp. 46–47); Rem 1.4.2 (i)(ii) (pp. 47–48)
> PDF: <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf>
> PRIMS DOI: <https://doi.org/10.4171/PRIMS/57-1-3>
> Phase: 4d (section 4 layer 4), mochizuki-side only
> Entity: 1 (iut:log_theta_lattice)
> verified_at: 2026-05-06

---

## 4d.1 `iut:log_theta_lattice` — Def 1.4: the two-dimensional diagram

**IUTchIII source**: Def 1.4, p. 45; Introduction Fig. I.1, p. 2

Let `{^{n,m}HT^{Θ±ellNF}}_{n,m∈Z}` be distinct Θ±ellNF-Hodge theaters indexed
by pairs of integers. The **log-theta-lattice** is either of the following diagrams:

**Non-Gaussian variant** (horizontal = Θ×μ-links):

    ...         ...
     |log         |log
    n,m+1HT —Θ×μ→ n+1,m+1HT —Θ×μ→ ...
     |log         |log
    n,m  HT —Θ×μ→ n+1,m  HT —Θ×μ→ ...
     |log         |log
    ...         ...

**Gaussian variant**: identical with Θ×μ replaced by Θ×μ_gau throughout.

Symbolically: `... → • → • → ...` (horizontal), each "•" = one HT, vertical = log.

- **Vertical arrows**: full log-links (Def 1.1 (iii), Prop 1.3 (i)); increasing m, fixed n.
- **Horizontal arrows**: Θ×μ- or Θ×μ_gau-links (IUTchII Cor 4.10 (iii)); increasing n, fixed m.

**Coricity (Theorem 1.5, pp. 48–50)**: vertical arrows induce full poly-isos on
D-Θ±ellNF-HT (vertical coricity, 1.5-i); horizontal arrows induce full poly-isos on
F^{⊢×μ}-prime-strips (horizontal coricity, 1.5-ii); F^{⊢×μ}-prime-strips and
mono-analytic log-shells `I_{n,mD^⊢_△}` are bi-coric — invariant under both
vertical and horizontal arrows for arbitrary n,m,n′,m′ ∈ Z (1.5-iii/iv).

---

## 4d.2 Non-commutativity (Rem 1.4.1-i, p. 46)

**Direct quotation** (IUTchIII Rem 1.4.1 (i), p. 46):

> "One fundamental property of the log-theta-lattices discussed in Definition 1.4
> is the following: the various squares that appear in each of the log-theta-lattices
> discussed in Definition 1.4 are far from being [1-]commutative!"

### Mechanism

- **Vertical (log-links)**: built from p_v-adic logarithms — power series depending
  essentially on **local ring structures** at v ∈ V.
- **Horizontal (Θ×μ-, Θ×μ_gau-links)**: **incompatible** with those same local ring
  structures in an essential way (IUTchII Rem 1.11.2 (i)(ii)).

**Forcing constraint** (Rem 1.4.1 (ii), p. 46): log-shells are required for the
multiradial representation of Gaussian monoids (§3), so each HT must appear as
the codomain of a log-link:

> "each execution of a horizontal arrow of the log-theta-lattice necessarily
> obligates a subsequent execution of a vertical arrow of the log-theta-lattice."

**Rigid vs. indeterminate** (Rem 1.4.2 (i), p. 47): vertical linking data is rigid
(single fixed arithmetic holomorphic structure); horizontal linking data carries a
**Z×-indeterminacy** that obliterates the arithmetic holomorphic structure of a
vertical line. The horizontal lines are therefore universal covering spaces of
the resulting loops (Rem 1.4.2 (ii), p. 48).

**Consequence for multiradiality**: simultaneous compatibility with arithmetic
holomorphic structures on both sides of a horizontal arrow requires objects
invariant under vertical arrows — **vertical cores** (Rem 1.4.1 (ii); Prop 1.3 (iv)).

---

## 4d.3 Witt vector / Frobenius intertwining analogy (Rem 1.4.1-iii, p. 47)

**Direct quotation** (IUTchIII Rem 1.4.1 (iii), p. 47):

> "From the point of view of the analogy between the theory of the present series
> of papers and p-adic Teichmüller theory [cf. [AbsTopIII], §I5], the vertical
> arrows of the log-theta-lattice correspond to the Frobenius morphism in positive
> characteristic, whereas the horizontal arrows of the log-theta-lattice correspond
> to the 'transition from p^n Z/p^{n+1}Z to p^{n-1}Z/p^nZ', i.e., the mixed
> characteristic extension structure of a ring of Witt vectors."

Fig. 1.3 (p. 47) summary:

| log-theta-lattice | p-adic Teichmüller analogue |
|---|---|
| Horizontal arrows (Θ×μ / Θ×μ_gau) | Mixed characteristic extension of Witt ring |
| Vertical arrows (log-links) | Frobenius in positive characteristic |

The "intertwining of horizontal and vertical" (Rem 1.4.1 (ii)) corresponds to the
classical Witt-ring/Frobenius intertwining in the p-adic theory. See also
[IUTchI] Rem 3.9.3 (i) and [AbsTopIII] §I5 for the full p-adic Teichmüller analogy.

---

## 4d.4 SS-side: scope

**SS PDF**: Scholze–Stix, "Why abc is still a conjecture" (2018/2020), 10 pp.
(pymupdf full-text extraction, 2026-05-06)

"log-theta-lattice" appears **exactly once** in the SS PDF — in the bibliography
as the subtitle of [IUTT-3]:
> "[IUTT-3] Mochizuki, S., Inter-universal Teichmüller Theory III: Canonical
> Splittings of the Log-theta-lattice."

No substantive discussion of Def 1.4, Rem 1.4.1, non-commutativity, or the
Witt/Frobenius analogy appears in the SS paper. SS scope 外.

The SS objection targets the identification `^†HT ≅ ^‡HT` in Cor 3.12
(downstream of the lattice construction); see `docs/section_8_disputes_timeline.md`.

---

## 4d.5 [CLAIMED_BY: Mochizuki]

- Claimed by: Mochizuki (IUTchIII Def 1.4, Rem 1.4.1, Theorem 1.5)
- Peer review status: Published PRIMS 57 (2021), DOI 10.4171/PRIMS/57-1-3
- SS stance: SS scope 外 — Def 1.4 non-commutativity not disputed
- Verification status: mochizuki-side draft; 3-agent verify pending

---

**Sources**

- IUTchIII Def 1.4 (p. 45), Rem 1.4.1 (pp. 46–47), Rem 1.4.2 (pp. 47–48),
  Theorem 1.5 (pp. 48–50), Fig. 1.3 (p. 47):
  <https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf>
- SS PDF (bibliography only):
  <https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf>
