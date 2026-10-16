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
| 3 | sum_inv_le | 41–55 | Private finite reflection bound; lambda and chained tactics review. |
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

## Phases 3–5 — completed source work

Inserted the Mathlib/project import separator. All10 original declarations and all3 added
private helpers received distinct fresh Sol Medium declaration workers. Every canonical
report has42 rule labels/11 checked steps/no unchecked steps; each report was inspected at
its checkpoint. Each source freeze explicitly revoked worker edit ownership before sequential
full/separate LeanEval gates and successful exact-path commit/push.

| Declaration / dedicated report | Original lines | Current lines |
| --- | ---: | ---: |
| [sqrt_one_sub_inv_lt](Lattice-sqrt_one_sub_inv_lt.md) | 11 | 10 |
| [inv_add_inv_le](Lattice-inv_add_inv_le.md) | 6 | 6 |
| [sum_inv_le](Lattice-sum_inv_le.md) | 15 | 15 |
| [sum_inv_lt](Lattice-sum_inv_lt.md) | 24 | 23 |
| [extend_apply_castSucc](Lattice-extend_apply_castSucc.md) | 4 | 3 |
| [extend_apply_last](Lattice-extend_apply_last.md) | 6 | 3 |
| [card_filter_box_fiber_aux](Lattice-card_filter_box_fiber_aux.md) | added | 25 |
| [card_filter_box_last](Lattice-card_filter_box_last.md) | 43 | 11 |
| [filter_weight_le_eq_empty](Lattice-filter_weight_le_eq_empty.md) | 3 | 3 |
| [card_filter_fiber_eq](Lattice-card_filter_fiber_eq.md) | 11 | 10 |
| [card_filter_weight_le_of_le_sqrt_aux](Lattice-card_filter_weight_le_of_le_sqrt_aux.md) | added | 7 |
| [card_filter_weight_le_succ_aux](Lattice-card_filter_weight_le_succ_aux.md) | added | 30 |
| [card_filter_weight_le](Lattice-card_filter_weight_le.md) | 47 | 17 |

Substantive fibre-bijection, easy-range and successor estimates were privately extracted;
original public types/docs preserved. Successor positivity localized to its used coordinate.
No data definition introduced/modified. Optional compiled square-root hm1 weakening closed
without current caller benefit. No pending Lattice API decision. Rename queue raw/deduped0,
applied0/conflicts none; project-wide drain remains scheduled at project end.

## Phase 6 cumulative gates before independent review

Frozen SHA256 `be707274cdc77d8e31a73497e8392e8a556f8d13af1e3c190e32ad9c9496a2b3`,
all source ownership revoked; no source change during gates. Original217→current214 lines,
declaration content170→163; original module/public block comments byte-identical.

| Gate | Result/evidence |
| --- | --- |
| module build | Actual final `lake build Roth.Lattice` exit0,26s; `/private/tmp/roth-succ-final-module.log`. |
| full project / separate LeanEval | Sequential owner96137 both exit0(144.68s/36.29s), stable hash; `/private/tmp/roth-lattice-helper-succ-{full,leaneval}.log`. |
| complete LSP module/caller | Native cell125 both success, partial=false/timed_out=false/no failed dependencies; Lattice0errors/1 inherited header warning, MainLemma0errors/3 inherited warnings. JSON `/private/tmp/roth-lattice-cumulative-{lattice,mainlemma}-lsp.json`. |
| public statement / independent original proofs | Fresh original entire-file independent reconstruction and all4 original public proof-function equalities38886 exit0; `/private/tmp/roth-lattice-cumulative-compatibility.log`. |
| standard axioms | Actual imported environment all13 current public/private declarations46698 exit0; `/private/tmp/roth-lattice-cumulative-axioms.log`. |
| definition protection | No original/new data definitions. Private helper premise localization authorized and original type independently recovered. |
| external breakage | Sole mathematical caller MainLemma complete diagnostics and actual full build pass; root aggregator builds. |
| packing / inequalities / comments / trust | All13 width/inequality artifacts inspected; no over100codepoint source line/reversed inequalities/banned options/sorry/newaxiom/TODO/FIXME; original block comments equal. |

New-identifier verification: all4 externally introduced proof lemmas `Finset.card_filter_le`,
`Nat.cast_nonneg`, `Nat.succ_le_succ`, `lt_of_not_ge` batch #check46698 exit0,
`/private/tmp/roth-lattice-cumulative-identifiers.log`. Native local queries first yielded
positive source hits (indexes error/warming, no absence inferred); compiler checks authoritative.
New `grind`/`gcongr` tactics validated by actual module builds; three local helper identifiers
are actual declarations and included in the all13 built-axiom scan.

Overall pre-review cumulative gates: PASS. Fresh independent simplify and actual complete-source
per-declaration profiling remain; no file completion claimed before them.

## Phase 6.5 — fresh independent simplify review and renewed gates

Outcome ISSUES-FOUND-AND-FIXED. [Fresh read-only review](Lattice-simplify.md) found
unnecessarily heavy SpecialFunctions imports. Its independent whole-file candidate with
`Mathlib.Algebra.BigOperators.Fin` and `Mathlib.Analysis.Real.Sqrt` compiled exit0; owner
applied exactly that two-line substitution. Initial Sqrt-only candidate failed missing
Fin.prod_univ_castSucc and is not successful evidence. No other substantive finding.

Final source freeze `a363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8`;
all reviewer/leaf source ownership explicitly revoked and no probes active. Actual module5997
exit0(13s); complete native module/MainLemma diagnostics cell132 success/partial=false/no
failed dependencies/zero errors, same1/3 inherited warnings. Actual independent ORIGINAL
entire-source reproof and all4 public equalities,4 introduced external #checks, all13 actual
imported public/private standard-axiom checks46950 all exit0. Logs
`/private/tmp/roth-lattice-simplify-{module,compatibility,identifiers,axioms}.log`; diagnostic
JSON `/private/tmp/roth-lattice-simplify-{lattice,mainlemma}-lsp.json`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session93589, both
exit0(82.60s/23.98s), frozen hash stable; logs
`/private/tmp/roth-lattice-simplify-{full,leaneval}.log`.
All cumulative protection/structure/width/inequality/comment/trust/identifier/caller gates
renewed PASS. Source remains214 lines, declaration content163, original block comments
identical; all13 reports remain42 rules/11 checked steps. Actual final per-declaration
profiling still required; file completion not yet claimed.
