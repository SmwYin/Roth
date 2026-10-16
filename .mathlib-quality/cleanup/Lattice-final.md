# Lattice final cleanup report

Status: all10 original declarations, all3 added private helpers, and every final file phase complete.
Final source SHA256 `a363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8`.
All4 original public types, existing documentation, mathematical conclusions and pinned versions
preserved. Source217→214 lines; declaration content170→163. Headline proof43→14 body lines.

## Phases 0–3 — baseline, preparation and audit

[Initial audit and cumulative evidence](Lattice.md): clean branch `ramin-cleanup`, baseline
`45cdf4f`,217 lines/10 declarations, classic imports. Actual baseline `lake build`69299 exit0,
`/private/tmp/roth-lattice-baseline.log`; complete native LSP success, no errors, one existing
header warning. Cache fetch skipped because dependencies populated; standalone runLinter absent,
ordinary Mathlib linters enabled during module builds. Both skills, full cleanup/cleanup-all
commands and relevant file-owner references read; buzz command and profiling reference read.

Full A.1–A.7 file audit, linter finding and all10 light declaration scans recorded before edits.
Inserted Mathlib/project import separator. No section headers removed or resource options found.
Missing authoritative copyright/license metadata remains explicitly preserved by user decision;
no metadata invented or linter suppressed. Module and all4 public block docstrings are byte-identical.

## Phase 4 — one fresh worker per declaration

Each original and each added private helper received its own fresh Sol Medium worker with no
inherited context. Each canonical report contains all24 audit items, all42 golfing rules, five
actual Mathlib search attempts, per-parameter mechanical probes, public literature/private
exemptions, width100 #check and codepoint packing arithmetic, inequality scan, actual independent
proof/standard-axiom checks, scoped diff gates, and all11 checked steps. Owner inspected every
report; final inventory parser verified42 rule labels/11 checked steps/zero unchecked entries
in all13 reports. Tool timeouts, partial/warming/error indexes and rejected probes are explicit;
no absence or success inferred from unavailable services. Native diagnostics used normally,
persistent direct MCP/fresh CLI used for bounded stale-import/stall recovery.

| Declaration / dedicated audit | Initial lines | Final lines |
|---|---:|---:|
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

All10 originals retained and3 substantive private helpers added (13 current declarations).
Declaration counts exclude docs/scope commands. Headline14 body lines, largest branch9;
fibre cardinality theorem7 body lines, bijection helper20, successor helper24. No long
conjunction result or unresolved decomposition flag remains.

Each declaration checkpoint explicitly froze a source hash and revoked leaf source ownership
before owner full `lake build` followed by separate `lake build Roth.LeanEval` (root omits it).
Exact paths staged, staged set printed, commit and successful cleanup-branch push confirmed
before the next edit. A report-detected headline binder packing defect was corrected by owner;
all affected gates renewed on corrected hash before publication, earlier gates marked historical.

## Phase 5a — non-rename refactoring

Private fibre-bijection, easy-range and successor estimates replace long branches with a clear
induction outline. The repeated extension reconstruction is proved once; private successor
positivity is localized to its used last coordinate. Existing Mathlib filter/cardinality,
reflection, mapDomain and arithmetic API used directly. Single-use aliases and omega removed;
cast/iff bookkeeping simplified with gcongr/grind. No data definition, instance or trust change.

The separately compiled optional square-root hm1 weakening was closed without current caller
benefit, preserving the existing paper/API. No Lattice public proposal remains pending.

## Phase 5b — rename queue

Raw queue0, deduplicated0, applied0, conflicts none; no caller rename or source-name change.
Project-wide rename drain remains scheduled at project end; queue is empty.

## Phase 6 — cumulative verification

All source ownership explicitly revoked at final hash above; source remained unchanged through
post-review gates, all profiling sweeps, final builds and report generation.

| Gate | Result and actual evidence |
|---|---|
| lake_build_file | `lake build Roth.Lattice`5997 exit0(13s), `/private/tmp/roth-lattice-simplify-module.log`. |
| lake_build | Final `lake build`6730 exit0(6.36s), `/private/tmp/roth-lattice-final-full.log`. |
| separate LeanEval | After full build in6730, `lake build Roth.LeanEval` exit0(3.23s), `/private/tmp/roth-lattice-final-leaneval.log`. |
| definition_protected | No original/new data definitions; authorized proof-only helpers and private premise localization. |
| public statements/original proofs | Fresh ORIGINAL whole-file independent reconstruction and all4 original public proof-function equalities46950 exit0, `/private/tmp/roth-lattice-simplify-compatibility.log`. |
| actual standard axioms | All13 actual imported public/private constants enumerated and checked46950 exit0; only propext/Classical.choice/Quot.sound, `/private/tmp/roth-lattice-simplify-axioms.log`. |
| new identifiers | All4 external names batch #check46950 exit0, `/private/tmp/roth-lattice-simplify-identifiers.log`; local source hits checked first, indexes error/warming not absence. |
| complete module/caller LSP | Native132 both success,partial=false,timed_out=false,no failed dependencies; zero errors. Lattice1 inherited header warning; MainLemma3 inherited warnings (header, hδ0/hr₁ at149). JSON `/private/tmp/roth-lattice-simplify-{lattice,mainlemma}-lsp.json`. |
| external breakage | Sole mathematical caller MainLemma complete diagnostics and actual full build pass; root aggregator builds. |
| style/trust/comments | All13 packing/inequality tables inspected; no source line over100 codepoints, reversed inequality, sorry/newaxiom/native_decide/limits/traces/TODO/FIXME; block comments identical, diff --check pass. |

New external declarations: Finset.card_filter_le, Nat.cast_nonneg, Nat.succ_le_succ,
lt_of_not_ge. New grind/gcongr tactics validated by compilation; all3 local helper names are
actual declarations included in the imported-constant scan. No hallucinated identifier.
Post-review full/separate93589 also passed82.60s/23.98s at the same hash; final6730 above is
fresh publication verification. Every build row cites an actual command/session, not LSP alone.
Overall cumulative gates PASS.

## Phase 6.5 — fresh independent simplify

Outcome **ISSUES-FOUND-AND-FIXED**. Built-in Claude /simplify unavailable; adapted to a fresh,
independent read-only reuse/quality/efficiency review, [report](Lattice-simplify.md).
It found unnecessarily heavy real/complex power and sqrt-smoothness imports. Its whole-file
candidate with Mathlib.Algebra.BigOperators.Fin + Mathlib.Analysis.Real.Sqrt compiled exit0;
owner applied exactly that import substitution. Initial Sqrt-only candidate failed at
Fin.prod_univ_castSucc and was correctly rejected. No other substantive issue or follow-up.
All Phase6 gates rerun after application; public statements/docs unchanged. Import fix published
as b34d56d before profiling. No other compiler/profiler probes remained active during final sweeps.

## Phase 6.6 — actual complete-source profiling

Outcome **FAST-BOARD after required borderline remeasurements**, budget1000ms.
Actual command for all three isolated full-source sweeps:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Lattice.lean`.
Sessions3913/82130/19793 all exit0 on identical final source hash. Initial square-root sample
1034.98ms was marginally over budget; required isolated repeats measured959.56ms and994.79ms.
Both consecutive final complete sweeps have all13 declarations below1000ms. The other borderline
result, sum_inv_lt, measured774.15/790.97ms; all remaining declarations are below750ms.
No source performance patch, claimed speedup, limit raise, deferral or profiling scaffold.

Traces and per-declaration tables archived as `/private/tmp/roth-lattice-profile-passN-{trace.log,table.json}`
for N=1,2,3. Final trace/table also `/private/tmp/roth-lattice-final-profile-{trace.log,table.json}`.
Parser `/private/tmp/roth-lattice-final-profile-parse.py` asserts all13 source declarations are
covered. Totals add command elaboration and associated top-level async proof/kernel/compiler tasks;
separately tagged linter work excluded, nested nodes never counted twice. Aggregate --profile
category totals alone were not used as per-declaration timing. One early parser call on an
unfinished third trace was rejected by its coverage assertion; only completed exit0 sweeps below
supply final evidence.

| Declaration | First ms | Repeat1 ms | Repeat2 ms | Final dominant source step |
|---|---:|---:|---:|---|
| `sqrt_one_sub_inv_lt` | 1034.98 | 959.56 | 994.79 | have hsq : 4 * (m : ℝ) < lam ^ 2 := by |
| `inv_add_inv_le` | 637.90 | 587.21 | 614.57 | nlinarith [mul_nonneg hx0 (sub_nonneg.2 hx2)] |
| `sum_inv_le` | 664.35 | 620.12 | 643.12 | have h := |
| `sum_inv_lt` | 798.68 | 774.15 | 790.97 | have hlam2 : 2 < lam := by |
| `extend_apply_castSucc` | 35.10 | 29.87 | 33.78 | simp [Finsupp.mapDomain_apply_of_injective (Fin.castSucc_injective m)] |
| `extend_apply_last` | 26.73 | 27.30 | 26.51 | simp [Finsupp.mapDomain_of_notMem_range] |
| `card_filter_box_fiber_aux` | 172.74 | 145.60 | 162.71 | have hext : |
| `card_filter_box_last` | 68.64 | 69.66 | 70.78 | rw [Finset.card_eq_sum_card_fiberwise (f := fun d ↦ d (Fin.last m)) (t := |
| `filter_weight_le_eq_empty` | 201.46 | 201.38 | 176.22 | linarith [weight_nonneg r d] |
| `card_filter_fiber_eq` | 320.67 | 276.77 | 300.28 | grind |
| `card_filter_weight_le_of_le_sqrt_aux` | 310.08 | 271.18 | 325.30 | calc |
| `card_filter_weight_le_succ_aux` | 663.56 | 641.17 | 648.15 | calc |
| `card_filter_weight_le` | 259.97 | 243.95 | 252.08 | induction m generalizing lam with |

Final maximum994.79ms; both required consecutive borderline confirmations pass. Raised limits
removed0/added0. No over-budget declaration in either final sweep; no deferred performance work.

## Phase 7 — publication and handoff

All13 canonical declaration artifacts, baseline/punch list, scoped proposal disposition,
fresh independent review, cumulative gates and actual full profiling tables present. Three
schema-conforming meaningful learnings recorded. No routine Lattice follow-up, decomposition,
rename, public decision or file split remains. Header metadata limitation remains user-preserved.
Original project tally130/264;7/14 files complete after this final report publication. Next file
work and newly approved prior-file API amendments belong to the project orchestrator after
successful final push and explicit ownership release; this file owner changes no prior files.
