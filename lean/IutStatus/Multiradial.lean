/-
IutStatus.Multiradial — multiradial algorithm + indeterminacies stub.

Drift-zero: maps to `iut:multiradial_algorithm` in `data/entities.json`.
The structural heart of IUTchIII §3, including the three
indeterminacies Ind1 / Ind2 / Ind3 that bound the resulting volume
estimate.
-/

import IutStatus.ThetaLink
import IutStatus.LogLink
import IutStatus.EtaleTheta

namespace IutStatus

/-- Multiradial algorithm. Stub. -/
axiom multiradial : Prop

/-- Indeterminacy Ind1 (étale-theoretic). Stub. -/
axiom Ind1 : Prop

/-- Indeterminacy Ind2 (Frobenius-theoretic). Stub. -/
axiom Ind2 : Prop

/-- Indeterminacy Ind3 (log-volume). Stub. -/
axiom Ind3 : Prop

end IutStatus
