/-
IutStatus.ThetaLink — θ-link multiplicative connection stub.

Drift-zero: maps to `iut:theta_link` in `data/entities.json`.
Multiplicative link between distinct Hodge theaters (IUTchII Def 4.10).
-/

import IutStatus.HodgeTheater

namespace IutStatus

/-- θ-link (multiplicative link between Hodge theaters). Stub. -/
axiom theta_link : HodgeTheater → HodgeTheater → Prop

end IutStatus
