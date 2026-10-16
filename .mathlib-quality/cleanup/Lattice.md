# Lattice cleanup

Baseline: branch `ramin-cleanup`, commit `45cdf4f`; source 217 lines, ten original declarations.
`lake build` session 69299 exited 0; log `/private/tmp/roth-lattice-baseline.log`.
Complete native LSP: zero errors, one inherited header warning, no partial/timed-out diagnostics.
Cache fetch skipped: existing dependency cache. No separate runLinter executable configured.
Dialect: classic imports. Original snapshot: `/private/tmp/roth-lattice-original.lean`.

## Phase 2 punch-list

| Item | Finding/action |
| --- | --- |
| A.1 copyright | Missing authoritative metadata; preserve unchanged by existing user decision. |
| A.2 module documentation | Present, preserve original source citation. |
| A.3 imports | Alphabetical groups; insert blank between Mathlib and project imports. |
| A.4 headers | No contentless section headers. |
| A.5 length | 217 lines, below split threshold. |
| A.6 options | No raised limits or debug options. |
| A.7 mechanical | No λ binders, dollar applications, deprecated push_neg; mathematical lambda arrows need review. |
| B.1 L1 | Existing copyright header warning; user chose preservation, no suppression. |

| Original | Declaration | Initial lines | Light scan |
| ---: | --- | --- | --- |
| 1 | sqrt_one_sub_inv_lt | 22–32 | Descriptive theorem name; public docs preserved; short algebraic proof. |
| 2 | inv_add_inv_le | 34–39 | Private descriptive bound; no docstring; arithmetic hypotheses audit. |
| 3 | sum_inv_le | 41–54 | Private finite reflection bound; lambda and chained tactics review. |
| 4 | sum_inv_lt | 62–85 | Public docs preserved; signature/auxiliary aliases audit. |
| 5 | extend_apply_castSucc | 87–90 | Private Finsupp extension coordinate identity; library replacement review. |
| 6 | extend_apply_last | 92–98 | Private last-coordinate identity; library replacement review. |
| 7 | card_filter_box_last | 104–146 | Public docs preserved; long bijection proof requires structure review. |
| 8 | filter_weight_le_eq_empty | 148–150 | Private empty-cutoff identity; direct arithmetic proof. |
| 9 | card_filter_fiber_eq | 152–162 | Private fibre-weight transport; signature and cast audit. |
| 10 | card_filter_weight_le | 169–215 | Headline theorem: induction branches/finite-sum estimate require decomposition review. |

Public statements/definitions and existing documentation are protected. Any substantive API
proposal will be compiled separately and referred to the project owner before application.
Each original receives a fresh dedicated worker, complete audit/golf/search/generalisation
artifacts, followed by module/LSP/independent proof/axiom and full/separate LeanEval gates,
then its own commit and successful push before the next source edit.
