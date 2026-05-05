# [iut:height_inequality + iut:diophantine_inequality + iut:abc_conjecture] abc consequence — Mochizuki view
> 3-agent verify pending (mochizuki-side draft).

## Statement of abc conjecture

**abc conjecture (Masser–Oesterlé 1985):** for any ε > 0, there exists C(ε) such that for
all coprime triples (a, b, c) with a + b = c,

    max(|a|, |b|, |c|) ≤ C(ε) · rad(abc)^{1+ε}

where rad(n) = product of distinct prime divisors of n.

- Masser, D. (1985): unpublished letter to Oesterlé
- Oesterlé, J. (1988): Nouvelles approches du "théorème" de Fermat, Séminaire Bourbaki 694

---

## Mochizuki's IUT-derived height inequality — `iut:height_inequality`

**Source:** IUTchIV §1, Theorem 1.10 (Log-volume Estimates for Θ-Pilot Objects)
**DOI:** 10.4171/PRIMS/57-1-4
**PDF (verbatim):** https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf

**Setup (IUTchIV Def. 1.9 + Thm. 1.10 preamble, pp. 21–22):**
Fix initial Θ-data as in [IUTchI, Def. 3.1], with elliptic curve E_F / F, prime l ≥ 5, and
"tripodal" field F^{tpd} = F_mod(E_{F_mod}[2]).  Write:

- d_mod = [F_mod : Q], e_mod = max ramification index of F_mod over Q
- d*_mod = 2^{12}·3^3·5·d_mod, e*_mod = 2^{12}·3^3·5·e_mod
- log(q) = normalized degree of the q-parameter divisor of E_F at bad primes
- log(d^{F^{tpd}}), log(f^{F^{tpd}}) = normalized different / conductor of F^{tpd} / Q

**Conclusion of Thm. 1.10 (verbatim, p. 23):**

> one may take the constant "C_Θ ∈ R" of [IUTchIII], Corollary 3.12, to be
>
>     (l+1) / (4·|log(q)|) · { (1 + 12·d_mod/l)·(log(d^{F^{tpd}}) + log(f^{F^{tpd}}))
>                               + 10·(e*_mod·l + η_prm) }^{-1}
>     − 1/6·(1 − 12/l^2)·log(q)
>
> and hence, by applying the inequality "C_Θ ≥ −1" of [IUTchIII], Corollary 3.12, conclude that
>
>     1/6 · log(q)  ≤  (1 + 20·d_mod/l)·(log(d^{F^{tpd}}) + log(f^{F^{tpd}}))
>                       + 20·(e*_mod·l + η_prm)
>                    ≤  (1 + 20·d_mod/l)·(log(d^F) + log(f^F))
>                       + 20·(e*_mod·l + η_prm)

where η_prm > 0 is the positive real number from Proposition 1.6 (Prime Number Theorem estimate).

**Dependency:** The inequality "C_Θ ≥ −1" is supplied by IUTchIII, Corollary 3.12 —
the multiradial log-volume estimate for LGP-monoids derived from IUTchIII Thm. A (Thm. B in pdf).

---

## Diophantine inequality — `iut:diophantine_inequality`

**Source:** IUTchIV §2, Corollary 2.2 (Construction of Suitable Initial Θ-Data) + Corollary 2.3
**DOI:** 10.4171/PRIMS/57-1-4

### Corollary 2.2, (ii) — explicit bound (p. 42–48, verbatim conclusion p. 48)

Setup: X = P^1_Q, D = {0,1,∞}, U_X = X\D (once-punctured projective line / Legendre λ-line).
KV ⊆ U_X(Q) a compactly bounded subset (support contains the prime 2, condition (*j-inv)).
d ∈ Z_{≥1}, ε_d ∈ (0,1].  δ := 2^{12}·3^3·5·d.

For any elliptic curve E_F outside a finite exceptional set Exc_d (depending only on K_V, d, ε_d),
writing h = log(q^∀) (normalized height via q-parameters at all bad primes):

> **Condition (C2):**
>
>     1/6 · log(q)  ≤  1/6 · log(q^{∤2})  ≤  1/6 · log(q^∀)
>                    ≤  (1 + ε_E)·(log-diff_X(x_E) + log-cond_D(x_E)) + C_K
>
> where  ε_E := (60δ)^2 · (log(q^∀))^{−1/2} · log(2δ·log(q^∀)),
> and C_K is a positive constant depending only on K_V.

**Asymptotic form (Remark 2.2.1, (i), p. 48; assuming F^{tpd} = Q):**

    1/6 · h  ≤  δ  +  *· δ^{1/2} · log(δ)

where δ = log-diff + log-cond, and * denotes a fixed positive real number.
Mochizuki notes this ε-term δ^{1/2}·log(δ) is "strongly reminiscent of well-known interpretations
of the Riemann hypothesis" (arising from the archimedean/nonarchimedean balance in optimizing l).

### Corollary 2.3 (= Theorem A) — Diophantine inequalities (p. 54, verbatim)

> **Corollary 2.3.** (Diophantine Inequalities) Let X be a smooth, proper, geometrically
> connected curve over a number field; D ⊆ X a reduced divisor; U_X := X\D; d a positive
> integer; ε ∈ R_{>0} a positive real number. Write ω_X for the canonical sheaf on X.
> Suppose that U_X is a hyperbolic curve, i.e., that the degree of the line bundle ω_X(D) is
> positive. Then, relative to the notation reviewed above, one has an inequality of
> "bounded discrepancy classes"
>
>     ht_{ω_X(D)}  ≲  (1 + ε)·(log-diff_X + log-cond_D)
>
> of functions on U_X(Q)^{≤d}.

**Proof note (p. 54–55):** "One verifies immediately that the content of the statement of
Corollary 2.3 coincides precisely with the content of [GenEll], Theorem 2.1, (i)."
The proof therefore routes through Corollary 2.2, Theorem 1.10, and IUTchIII Cor. 3.12.

---

## abc conjecture as consequence — `iut:abc_conjecture`

**Source:** IUTchIV Introduction, Theorem A = Corollary 2.3 consequences (p. 3, verbatim)

> Thus, Theorem A asserts an inequality concerning the canonical height [i.e., "ht_{ω_X(D)}"],
> the logarithmic different [i.e., "log-diff_X"], and the logarithmic conductor [i.e., "log-cond_D"]
> of points of the curve U_X valued in number fields whose extension degree over Q is ≤ d.
> **In particular, the so-called Vojta Conjecture for hyperbolic curves, the ABC Conjecture,
> and the Szpiro Conjecture for elliptic curves all follow as special cases of Theorem A.**
> We refer to [Vjt] for a detailed exposition of these conjectures.

Standard specialization (implicit in IUTchIV, explicit in [GenEll, Thm. 2.1]):
Take X = P^1, D = {0,1,∞}, point (a:b:c) with a+b+c=0, gcd=1.
Then ht_{ω_X(D)} ~ log max(|a|,|b|,|c|) and log-cond_D ~ log rad(abc),
so Cor. 2.3 gives the abc inequality with explicit constant depending only on ε and d.

---

## Logical chain

```
IUTchI–III: log-theta-lattice + multiradial algorithms for LGP-monoids
    ↓
IUTchIII, Cor. 3.12: log-volume estimate for Θ-pilot objects (C_Θ ≥ −1)
    ↓
IUTchIV §1, Thm. 1.10: explicit height inequality
    1/6 · log(q) ≤ (1 + 20d_mod/l)·(log d^{F^{tpd}} + log f^{F^{tpd}}) + 20(e*_mod·l + η_prm)
    ↓
IUTchIV §2, Cor. 2.2: construction of initial Θ-data + explicit Diophantine bound
    1/6 · h ≤ (1 + ε_E)·(log-diff + log-cond) + C_K
    ↓
IUTchIV §2, Cor. 2.3 (= Thm. A): ht_{ω_X(D)} ≲ (1+ε)·(log-diff + log-cond)
    ↓
abc conjecture (Vojta / Szpiro / abc as special cases)
```

The load-bearing step is IUTchIII Cor. 3.12, which supplies the inequality C_Θ ≥ −1.
This is precisely the step disputed in the Scholze–Stix (2018) report.
Mochizuki's response is in [IUTchIV, Remark 1.10.4; IUTchIII, Remark 3.12.1–3.12.4].

---

## Why this chain is load-bearing

- abc → Szpiro conjecture (semistable elliptic curves), Vojta conjecture for hyperbolic curves,
  Fermat-type equations (via Frey–Ribet–Wiles, independent), effective Mordell.
- Mochizuki claims IUT delivers **explicit** constants C(ε) = C(ε, d) (through Cor. 2.2, (ii)),
  whereas classical proofs (if they existed) might give ineffective bounds.
- The asymptotic ε-term δ^{1/2}·log(δ) in Cor. 2.2 is noted by Mochizuki (Remark 2.2.1)
  to be consistent with a conjecture of van Frankenhuijsen (lim sup = 1/2, reminiscent of RH).

---

## Forbidden translations

The following Scholze–Stix (SS) vocabulary is not used in this draft, per project policy:

| Forbidden | IUT-native equivalent |
|---|---|
| "identification of objects in different copies" | "non-ring/scheme-theoretic horizontal arrow of the log-theta-lattice" |
| "the inequality is circular" | (SS dispute: not adopted here; see 3-agent verify) |
| "Frobenioid = scheme" | "species-theoretic formulation of Frobenioid" |

---

## Source

- **IUTchIV (primary):**
  https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf
  DOI: 10.4171/PRIMS/57-1-4
  Published: PRIMS 57-1 (2021), pp. 465–600

- **IUTchIII (Cor. 3.12 dependency):**
  https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf
  DOI: 10.4171/PRIMS/57-1-3

- **GenEll (Thm. 2.1 reduction):**
  Mochizuki, S. — "Arithmetic Elliptic Curves in General Position", RIMS preprint 2009
  https://www.kurims.kyoto-u.ac.jp/~motizuki/Arithmetic%20Elliptic%20Curves%20in%20General%20Position.pdf

- **Vojta conjecture reference:**
  Vojta, P. (1987): Diophantine Approximations and Value Distribution Theory, LNM 1239, Springer
