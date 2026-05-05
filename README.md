# iut-status-2026

> A vendor-neutral, drift-resistant, dispute-preserving status index for
> Inter-universal Teichmüller theory (IUT) by Shinichi Mochizuki, the
> Scholze-Stix counter-claim (2018-), the Mochizuki response (2018-),
> and the Joshi reformulation (2025-).
>
> **This repository is NOT a tutorial, NOT a popularization, and NOT a
> verdict.** It is a machine-readable index designed to prevent
> interpretation drift across LLMs (Claude / GPT / Gemini / Llama) and
> across human readers, by encoding entities, claims, and evidence as
> JSON-LD with stable IRIs and Lean 4 theorem stubs.

## Why this repository exists

When asked about IUT, contemporary LLMs frequently:
1. assert "abc is proved" without mentioning Scholze-Stix, OR
2. assert "IUT is broken" without mentioning Mochizuki's response, OR
3. silently fuse the two positions into a fictional consensus.

All three are factually wrong as of 2026-05. The dispute is unresolved.
This repository encodes the unresolved status in a format that does not
collapse under summarization.

## Drift-resistance strategy (3 layers)

| Layer | Mechanism | Drift guarantee |
|---|---|---|
| **JSON-LD core** (`data/*.json`) | Stable IRIs (`iut:Cor.3.12`), claim graph with `counters` edges | Entity identity ✓ |
| **Lean 4 stubs** (`lean/IutStatus/`) | `theorem cor_3_12 : Prop := sorry` placeholders, mathlib4-compatible | Semantic identity (when `sorry` is replaced) — currently stub-only |
| **Markdown view** (`docs/`) | Auto-generated from JSON-LD via `tools/render_md.py` | Human-readable; not the source of truth |

**Honest scope:** Drift is eliminated at the IRI/structure level. Full
semantic drift-zero requires Lean 4 formalization, which is being
attempted by the [LANA project](https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f)
(Commelin, Kedlaya, Hoshi, Topaz, Kato, et al.; founded 2026-03-31; mid-report
scheduled 2026-07-17). When LANA produces formal `theorem` bodies, the
`sorry` stubs in this repository will be replaced.

## Multi-consumer design

| Consumer | Entry point |
|---|---|
| Any LLM (Claude / GPT / Gemini / Llama / ...) | `LLM_CONTEXT.md` |
| Claude Code specifically | `CLAUDE.md` (thin shim → `LLM_CONTEXT.md`) |
| Human researcher | `README.md` → `docs/overview.md` |
| Program (Python) | `loaders/python_minimal.py` (stdlib-only, no deps) |
| Program (jq / shell) | `data/*.json` directly |
| Lean 4 | `lean/lakefile.lean` |
| Validator (CI) | `schemas/*.json` (JSON Schema 2020-12) |

## Repository layout

```
iut-status-2026/
├── LLM_CONTEXT.md         # Vendor-neutral system prompt for any LLM
├── CLAUDE.md              # Claude Code shim → LLM_CONTEXT.md
├── data/                  # JSON-LD source of truth
│   ├── context.jsonld     # @context for all data files
│   ├── entities.json      # IUT concepts (anabelian, Frobenioid, ...)
│   ├── claims.json        # Mochizuki / Scholze-Stix / Joshi claim graph
│   └── timeline.json      # 2012-2026 dispute timeline
├── schemas/               # JSON Schema validators
│   ├── entity.json
│   ├── claim.json
│   └── timeline.json
├── lean/                  # Lean 4 theorem stubs (mathlib4-compatible)
│   ├── lakefile.lean
│   └── IutStatus/
│       └── Basic.lean
├── loaders/               # Reference parsers
│   └── python_minimal.py  # Python 3.10+, stdlib only
├── tools/                 # Maintenance utilities
│   └── render_md.py       # JSON-LD → Markdown view generator
├── docs/                  # Human-readable, auto-generated
│   ├── overview.md
│   └── disputes.md
├── tests/                 # CI validation
│   └── test_validation.py
├── LICENSE                # Apache-2.0
├── NOTICE                 # Citation policy + neutrality statement
├── CONTRIBUTING.md        # PR rules (evidence-only label gate)
└── CODE_OF_CONDUCT.md     # Contributor Covenant 2.1
```

## Citation policy

- We quote **statements** (theorems, corollaries, definitions) which are
  not subject to copyright. Each quotation carries DOI + paper +
  section + page number + URL.
- We do **not** redistribute original PDFs, figures, or prose passages
  from copyrighted sources.
- We treat this as fair use under US 17 U.S.C. §107 and Japanese
  Copyright Act Article 32.
- Take-down requests: open a GitHub Issue.

## Versioning

Semantic Versioning. v0.x is unstable; the JSON-LD `@context` may break.
v1.0 is gated on either (a) LANA mid-report (2026-07-17) confirming or
refuting the dispute, OR (b) one full year of stable claim graph.

## License

- Code, schemas, JSON-LD structure, Lean stubs: **Apache-2.0**
- Quoted mathematical statements: not copyrighted (academic convention)
- Quoted prose passages from copyrighted papers: fair-use educational excerpt

## Acknowledgements

The repository owes its premise (drift-zero across LLM consumers) to the
observation that LLMs trained on Quanta-2018-era reporting drift toward
the Scholze-Stix consensus, while Japanese-language LLMs drift toward
Mochizuki support, and neither captures the unresolved status. The
3-layer hybrid encoding addresses this by making the structure
machine-checkable rather than narrative.

## See also

- [LANA project](https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f) — Lean 4 formalization (2026-03-31, ongoing)
- [Mochizuki, "Formalization of IUT" (2026-04)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20(2026-04).pdf)
- [Joshi, arXiv:2505.10568 (2025-05)](https://arxiv.org/abs/2505.10568)
- [Scholze-Stix, "Why abc is still a conjecture"](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [nLab: inter-universal Teichmüller theory](https://ncatlab.org/nlab/show/inter-universal+Teichm%C3%BCller+theory)
