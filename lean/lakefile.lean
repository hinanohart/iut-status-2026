import Lake
open Lake DSL

package iutStatus where
  -- Lean 4 stub package for iut-status-2026.
  -- All theorems are `sorry` placeholders.
  -- When the LANA project (https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f)
  -- delivers actual formalizations, the `sorry` bodies in this package
  -- can be replaced with mathlib4-compatible imports.

-- mathlib4 pinned to a specific tag for reproducibility. Bump deliberately
-- when LANA delivers IUT-relevant formalisations.
require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.10.0"

@[default_target]
lean_lib IutStatus where
  roots := #[`IutStatus.Basic]
