/-
IutStatus.LogLink — log-link additive connection stub.

Drift-zero: maps to `iut:log_link` in `data/entities.json`.
Additive link between Hodge theaters (IUTchIII Def 1.1-iii); the
vertical axis of the log-theta-lattice (Def 1.4).
-/

import IutStatus.HodgeTheater

namespace IutStatus

/-- log-link (additive link between Hodge theaters). Stub. -/
axiom log_link : HodgeTheater → HodgeTheater → Prop

end IutStatus
