/-
IutStatus.Basic — orchestrator that imports every per-section module.

Per v0.7.5 split, each per-section module owns its own stubs and
documents the IRI it maps to. This file exists solely so that
`lake build` reaches every stub via a single entry point and so that
external consumers can `import IutStatus` to pull in the entire stub
surface in one statement.

Drift-zero contract:
- Every identifier matches an `iut:*` IRI in `data/entities.json`.
- The split layout (one file per `lean_module` value) is enforced by
  `tools/validate.py` v0.7.5 rule, which checks that
  `lean/<lean_module>.lean` exists for every entity carrying a
  `lean_module` field.

LANA tracking:
- LANA project: https://zen.ac.jp/en/zmc/topics/jwz-o8xr3v6f
- Mochizuki Formalization (2026-04):
  https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20(2026-04).pdf
- mid-report scheduled 2026-07-17.
-/

import IutStatus.Anabelian
import IutStatus.AbsoluteAnabelian
import IutStatus.MonoAnabelian
import IutStatus.Frobenioid
import IutStatus.EtaleTheta
import IutStatus.MonoTheta
import IutStatus.TemperedRigidity
import IutStatus.Cuspidalization
import IutStatus.HodgeTheater
import IutStatus.ThetaLink
import IutStatus.LogLink
import IutStatus.Multiradial
import IutStatus.Cor312
import IutStatus.HeightInequality
import IutStatus.Diophantine
import IutStatus.ABC
