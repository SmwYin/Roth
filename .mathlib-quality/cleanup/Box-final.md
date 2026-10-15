# Box final file-level cleanup report

Status: all 14 declaration checkpoints completed and pushed; final file-level refactoring, cumulative gates, independent review, and actual profiling complete. Original baseline: `62e7b29`; final-phase starting checkpoint: `b84f3ab`. Header metadata remains unchanged under the user's explicit decision. No license or attribution has been invented or warning suppressed.

## Phases 0–3 — baseline, preparation, punch-list, file-level fixes

The [file audit](Box.md) preserves the original 128-line/14-declaration inventory, successful full baseline build (2586 jobs), complete native LSP baseline (21 warnings, zero errors), seven file-level categories, and declaration punch-list. The complete cleanup/cleanup-all workflows and Lean/mathlib-quality skills were read. Imports were alphabetically ordered; module/public documentation already existed; no option override or inline proof comment was present. No Phase-3 source edit was needed.

The user's explicit “Follow your recommendation” decision authorized verified unused Box positivity and DecidableEq removals, preserving conclusions, together with minimal Index caller repairs. The user supplied no authoritative copyright/license facts and chose to leave metadata unchanged; the line-1 header warning remains a stated limitation.

## Phase 4 — full declaration artifact sweep

Every original declaration had its own fresh worker, its own 24-item audit, all 42 golfing-rule statuses, five-method search, parameter/generalisation and public-literature checks, measured signature and inequality tables, live proof alternatives, isolated proof/type/axiom checks, module build, complete LSP, and completed checklist. The file owner then ran full `lake build` plus separate `lake build Roth.LeanEval`, staged exact paths, and committed/pushed successfully before the next declaration edit. Each report records actual session IDs and logs. Unavailable LeanSearch/index results are recorded as unavailable, never mathematical absence.

The post-Phase-4 sweep verifies 14 distinct reports, 42 rule statuses each, all four required structure/naming/packing/inequality gate labels, and no unchecked checklist item. All individual gate contents were inspected. Machine-readable tally: `/private/tmp/roth-box-artifact-sweep.json`. No declaration was batched or skipped.

Counts below include complete declaration lines, excluding docstrings and scope commands. Checklists sometimes include one additional final handoff item.

| Declaration / audit | Before | Final | Delta | Checklist | Pushed checkpoint |
|---|---:|---:|---:|---:|---|
| [box](Box-box.md) | 3 | 2 | -1 | 11/11 | `13b99bb` |
| [mem_box](Box-mem_box.md) | 2 | 2 | +0 | 11/11 | `5bed172` |
| [card_box](Box-card_box.md) | 2 | 2 | +0 | 12/12 | `9e3462f` |
| [card_le_card_box](Box-card_le_card_box.md) | 3 | 4 | +1 | 11/11 | `20d4254` |
| [weight](Box-weight.md) | 1 | 1 | +0 | 11/11 | `5c8697e` |
| [weight_nonneg](Box-weight_nonneg.md) | 2 | 2 | +0 | 11/11 | `c9979b7` |
| [weight_zero](Box-weight_zero.md) | 2 | 2 | +0 | 11/11 | `502a98c` |
| [weight_add](Box-weight_add.md) | 2 | 2 | +0 | 11/11 | `5c86638` |
| [weight_eq_zero_iff](Box-weight_eq_zero_iff.md) | 3 | 3 | +0 | 12/12 | `d51137b` |
| [weight_single](Box-weight_single.md) | 3 | 3 | +0 | 12/12 | `d196a3f` |
| [weight_le_card](Box-weight_le_card.md) | 4 | 4 | +0 | 12/12 | `c486b4d` |
| [weight_mul_left](Box-weight_mul_left.md) | 3 | 3 | +0 | 11/11 | `43f44a1` |
| [weight_le_degree_div](Box-weight_le_degree_div.md) | 5 | 5 | +0 | 11/11 | `8268ad8` |
| [weight_mapDomain](Box-weight_mapDomain.md) | 6 | 4 | -2 | 12/12 | `b84f3ab` |

Total declaration lines: 41 → 39 (−2). Source file: 128 → 126 lines (−2) after the new shared scope command, local classical proof steps, and two redundant import removals. No declaration was added or removed. Both definitions retain their original mathematical meaning, and every original docstring/comment remains byte-identical.

## Phase 5a — non-rename refactoring

Collected every worker refactoring item. The only required external repairs were the two obsolete positivity arguments in Index; both were completed and built within their own sequential checkpoints. No definition replacement, junk definition, single-use existential helper, proof decomposition, or file split was warranted. The generic Finsupp weight representation was inspected and compiled in several audits, but migrating this established quotient-sum API offers no required caller benefit. No broad generalisation or new companion API is proposed.

After all declaration checkpoints, consolidated ten `omit [DecidableEq σ] in` commands into one `omit [DecidableEq σ]` before `card_le_card_box`, covering all later declarations. This removes eight net lines of repeated scope scaffolding and changes no theorem text or proof. All 14 `#check` types and `#print axioms` outputs before and after are byte-identical (`cmp` exit 0); the scope consolidation therefore introduces no further API change. Type dump command: `lake env lean /private/tmp/roth-box-types.lean`; before session9635 exit0, after session72760 exit0. Logs: `/private/tmp/roth-box-types-before-scope.log` and `...-after-scope.log`.

## Phase 5b — rename pass scope

Project-wide Phase 5b remains scheduled after all project files, per cleanup-all. All 14 declaration reports queue no rename; `.mathlib-quality/renames.jsonl` is absent. This file worker did not mutate a shared rename queue.

| Deduped queue | Disposition |
|---|---|
| (empty) | No Box rename action |

- Raw / deduped queue depth: 0 / 0.
- Applied / skipped / conflicting renames: 0 / 0 / 0.
- Callsite files changed by rename pass: 0.
- Compatibility callsite edits under approved generalisation: exactly two lines in `Roth/Index.lean`, removing `hr` from `weight_le_card` and `hl` from `weight_mul_left`.

## Phase 6a — diagnostics, preservation, identifiers

Final complete native Box diagnostics after scope consolidation: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, exactly one unchanged `Copyright too short!` warning. The file is not warning-free; the user chose unchanged metadata without authoritative replacement facts.

Cumulative source analysis against `62e7b29`: all 14 declarations retained; all block comments/docstrings byte-identical; narrative proof comments 0 → 0; zero lines over 100 codepoints; no FIXME/TODO, sorry/admit, custom axiom, native_decide, option/limit override, tracing/profiling scaffolding, λ, `$`, or push_neg. `git diff --check` passes. Analysis and parser: `/private/tmp/roth-box-final-analysis.json`, `/private/tmp/roth-box-final-analyze.py`.

Approved elaborated signature changes: remove DecidableEq σ from `card_le_card_box` and all nine weight theorems; additionally remove DecidableEq τ from `weight_mapDomain`; remove positivity `hr` from `weight_le_card` and `hl` from `weight_mul_left`. Necessary positivity/injectivity hypotheses elsewhere remain. The textual signatures differ only for these two positivity removals, the explicit τ instance removal, and whitespace/lambda normalization. Definitions and all other public arguments/conclusions are preserved. Independent fresh `rfl` examples against both original definitions compile successfully.

Every new external proof identifier was searched through native local search first. The semantic index returned error/empty, which was not treated as absence. Source lookup and an actual batched native `#check` confirmed each name. Generated additive declarations were confirmed directly by the compiler. A scratch out-of-date-import notice while the concurrent build ran did not affect source diagnostics or actual build gates.

| New identifier | Verification | Result |
|---|---|---|
| `LE.le.trans_eq` | local search → source fallback → native `#check` | pass |
| `Fintype.sum_nonneg` | local search → additive-source fallback → native `#check` | pass |
| `Finsupp.sum_fintype` | local search → source uses → native `#check` | pass |
| `Finsupp.sum_mapDomain_index_inj` | local search → source fallback → native `#check` | pass |
| `gcongr` | existing imported tactic syntax; actual module and isolated proof compilation | pass |

Direct Box uses were inspected in CoeffNorm, Taylor, Index, Lattice, Theta, MainLemma, and Main. Separation and aggregate Roth lie in the dependent closure. The broad textual search also matched a HasseDeriv docstring's word “box”; that is not a dependency on `Roth.box`. All closure modules are covered by actual full build; LeanEval is separately built because aggregate Roth does not import it.

The two minimal Index edits passed complete native LSP (success=true, partial=false, zero errors), and the actual closure build. Index retains its own existing declaration audit work; the `index_le_card` call repair exposes an unused `hr` warning in its preserved signature. This is explicitly recorded for the future Index worker, without suppression or unrelated cleanup.

## Phase 6b — cumulative gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Final post-review `lake build Roth.Box`, session91862 exit0, 1154 jobs; `/private/tmp/roth-box-final-review-module.log` |
| additional touched module | pass | `lake build Roth.Index`, session57455 exit0, 1501 jobs; `/private/tmp/roth-box-final-index-module.log` |
| lake_build | pass | Final post-review `lake build`, session88871 exit0, 2586 jobs; `/private/tmp/roth-box-final-review-full.log` |
| separate LeanEval | pass | Final post-review `lake build Roth.LeanEval`, session70480 exit0, 2585 jobs; `/private/tmp/roth-box-final-review-leaneval.log` |
| definition_protected | pass | signatures unchanged; fresh independent rfl proofs against original definitions |
| theorem_statement_protected | pass under explicit user authorization | exact unused-assumption removals listed above, all other mathematical content preserved |
| scope consolidation | pass | all 14 types/axiom outputs byte-identical before/after |
| cumulative_no_unintended_breakage | pass | actual full + separate LeanEval closure gates, all affected modules compiled |
| no-sorry/no-limit/no-scaffolding | pass | cumulative source scan, module compilation, standard axioms for all declarations |

Cumulative gates: PASS. Final review and profiling outcomes are recorded below.


## Phase 6.5 — independent holistic simplify review

Outcome after owner remediation: **ISSUES-FOUND-FIXED**; fresh cumulative gates pass. The read-only reviewer reported **ISSUES-FOUND-NOT-FIXED** because it was explicitly not allowed to edit; the file owner applied its entire actionable finding.

The built-in simplify command is not exposed on this host. A fresh independent child `simplify_review`, created without inherited conversation history, read the entire source, cumulative baseline Box/Index diff, report draft, relevant skills, and Phase-6.5 workflow after cumulative gates passed. It reviewed reuse, quality, efficiency, abstraction, and import structure without repeating the declaration audits.

One actionable finding covered two redundant direct imports:
- `Mathlib.Algebra.BigOperators.Ring.Finset` is publicly imported by `Mathlib.Algebra.BigOperators.Field:8`.
- `Mathlib.Data.Fintype.Pi` is publicly re-exported via Field → Ring.Finset → Group.Finset.Pi (each link at source line8).

The owner verified these dependency sources and removed both direct imports. This shortens the import list without changing the transitive closure; no compilation-speed gain is claimed. Other apparent paths through private imports were correctly excluded, and removing Finsupp.Interval was not established. No other actionable finding or follow-up remained.

Reviewer observations: shared omission cleanly scopes instance-independent declarations; local classical proofs are appropriate; no substantial duplicate argument warrants helpers; the generic mapDomain sum theorem is appropriate; retained positive-denominator hypotheses have mathematical purpose; the two Index repairs are exact; neither mathematical definition needs replacement.

Reviewer edits/builds: none. Owner edits: two import lines. Fresh complete Box LSP after the fix passes with exactly the preserved header warning. Fresh module `lake build Roth.Box` session91862 exited 0, 1154 jobs, `/private/tmp/roth-box-final-review-module.log`. The earlier cumulative full36784/LeanEval92988 gates were successful before this fix; they are superseded for final-source coverage by the following mandatory reruns, rather than being presented as post-fix evidence.

Post-review `lake build` session88871 exited 0 (2586 jobs; `/private/tmp/roth-box-final-review-full.log`). Post-review `lake build Roth.LeanEval` session70480 exited 0 (2585 jobs; `/private/tmp/roth-box-final-review-leaneval.log`). These are the final-source cumulative gates. No remaining simplify finding or deferred follow-up. Actual profiling follows these successful gates.


## Phase 6.6 — actual performance sweep

Outcome: **FAST-BOARD**, all 14 declarations below the 1000ms elaboration budget.

Actual command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Box.lean`, session3955, actual exit0. Trace: `/private/tmp/roth-box-final-profile-trace.log`. Parser: `/private/tmp/roth-box-profile-parse.py`; complete parsed table: `/private/tmp/roth-box-final-profile-table.json`. The supported Lean4.34 profiler trace was used directly because earlier project profiling established that aggregate flags alone do not supply declaration anchors. No aggregate timing is substituted for per-declaration evidence.

All timings below are milliseconds. Conservative total adds the command and its async proof/kernel/compiler durations, excluding imports and linter work; nested duplicate command nodes use their maximum once. The proof column records the named async proof node. Dominant operation names the measured largest relevant tactic node (or term elaboration), not an inferred cause. Profiling was entirely command-line instrumentation; no source scaffold was added.

| Declaration | Source line | Command ms | Proof ms | Conservative total ms | Dominant operation | Budget |
|---|---:|---:|---:|---:|---|---|
| `box` | 41 | 21.41 | 0.00 | 21.58 | term elaboration | pass |
| `mem_box` | 45 | 6.89 | 77.06 | 85.62 | simp | pass |
| `card_box` | 51 | 11.91 | 47.47 | 60.56 | simp | pass |
| `card_le_card_box` | 59 | 6.02 | 8.17 | 15.07 | exact cardinality composition | pass |
| `weight` | 65 | 6.84 | 0.00 | 6.96 | term elaboration | pass |
| `weight_nonneg` | 69 | 1.88 | 73.93 | 78.20 | positivity | pass |
| `weight_zero` | 74 | 2.29 | 55.38 | 58.85 | simp | pass |
| `weight_add` | 79 | 5.15 | 128.99 | 137.66 | simp | pass |
| `weight_eq_zero_iff` | 85 | 4.76 | 184.99 | 196.39 | simp | pass |
| `weight_single` | 90 | 9.75 | 96.83 | 107.89 | simp | pass |
| `weight_le_card` | 97 | 7.86 | 136.15 | 146.73 | simp | pass |
| `weight_mul_left` | 104 | 11.19 | 135.45 | 147.85 | simp | pass |
| `weight_le_degree_div` | 112 | 22.57 | 123.61 | 149.03 | gcongr with j | pass |
| `weight_mapDomain` | 121 | 8.57 | 171.67 | 188.78 | simpa using generic sum theorem | pass |

Maximum: `weight_eq_zero_iff`, **196.39ms**. All 14 are below budget and below the 750ms borderline-resweep threshold. No slow declaration was found; performance diagnosis, optimization, issue propagation, and before/after heartbeat measurements are therefore inapplicable. No performance deferral or unmeasured optimization is claimed. No resweep is required because no declaration is borderline and no source changed after this measurement.

- Existing / removed / added heartbeat overrides: 0 / 0 / 0.
- Other limit raises: 0.
- Performance fixes / outstanding flags: 0 / 0.
- All final source and comment/scaffolding checks pass after the sweep.

## Phase 7 — completed result and remaining project scope

Box cleanup is complete: 14/14 original declarations reviewed; 14 retained. Together with HasseDeriv this brings the project to 40/264 original declarations reviewed. Next file is Wronskian, to be assigned a fresh file worker. This report does not claim the other project files have been cleaned.

Known limitations are explicit: the unchanged header warning reflects missing authoritative metadata and the user's decision to leave it; remote LeanSearch failure and local-index errors used bounded honest fallbacks; Index retains its separate future declaration cleanup, including its newly exposed unused hr warning. No required Box task, actionable simplify finding, performance issue, rename, or approval request remains outstanding.

- [x] Phase0 baseline doctor/build.
- [x] Phase1 full preparation and 14-declaration inventory.
- [x] Phase2 file/declaration punch-list.
- [x] Phase3 file-level audit; no initial edit needed.
- [x] Phase4 14 distinct workers, all required artifacts/gates/checklists, each sequentially built/committed/pushed.
- [x] Post-Phase4 artifact sweep and rename reconciliation.
- [x] Phase 5a non-rename refactoring; scope consolidation and completed caller repairs.
- [x] Phase5b empty Box queue accounted for; project-wide pass reserved for orchestrator after all files.
- [x] Phase6 final post-review module, complete LSP, cumulative full/LeanEval, signature/definition/comment/identifier/trust gates.
- [x] Phase6.5 fresh independent review, both redundant imports removed, all cumulative gates rerun.
- [x] Phase6.6 actual trace-backed complete performance sweep, all 14 under budget.
- [x] Phase7 final report and accurate shared progress.
