# Wronskian final file-level cleanup report

Current status: the user-approved removal of both unused hypotheses is applied and fully validated. See the amendment section below; earlier pending references describe the historical checkpoint.

Status: all 15 declaration checkpoints and all final file-level phases complete; final publication checkpoint prepared. Baseline `d259f95`; all 15 original declaration checkpoints published through `ed342ce`. Header metadata remains unchanged under the explicit user decision. The coefficient theorem now omits the two unused arguments under explicit user approval; the original final-phase evidence below is historical, supplemented by the amendment verification.

## Phases 0–3 — baseline and preparation

The [file audit](Wronskian.md) records the original 271-line/15-declaration inventory, baseline full build session9164 exit0, complete LSP with no errors and three warnings, all seven file-level audit categories, and the declaration punch-list. Both Lean/mathlib-quality skills and full cleanup/cleanup-all workflows were read. Existing module/public documentation and import order were sound. No Phase-3 source edit was required. The missing copyright metadata is explicitly retained; no author/license was invented and no linter was suppressed.

## Phase 4 — declaration artifact sweep

All 15 original declarations received fresh dedicated workers and individual reports with the 24-item audit, all 42 golfing rules, five-method search, per-hypothesis generalisation audit, public literature checks (private-helper exemption stated), width and inequality tables, tested proof alternatives, isolation/type/axiom checks, module and complete LSP gates, and 11 completed checklist items. The file owner validated affected dependents with full `lake build` plus separate `lake build Roth.LeanEval`, then staged exact paths, committed, and pushed before allowing the next declaration edit. Reports cite actual sessions and logs. A premature source-freeze violation in declaration9 was repaired by rerunning the full closure on the final frozen source; the earlier changed-source build is not counted.

Machine sweep `/private/tmp/roth-wronskian-artifact-sweep.json` confirms 15 reports, 42 rules and 11 checked items each, all required gate labels, and no unfinished checkbox. Full gate content was inspected individually. LeanSearch HTTP500 and unavailable/warming/error local indices were recorded honestly; source and compiler fallback supplied positive evidence.

| Declaration / audit | Original lines | Final lines | Checkpoint |
|---|---:|---:|---|
| [wronskianMatrix](Wronskian-wronskianMatrix.md) | 2 | 2 | `046dfdf` |
| [wronskian](Wronskian-wronskian.md) | 1 | 1 | `d36d1f5` |
| [wronskian_eq_zero_of_not_linearIndependent](Wronskian-wronskian_eq_zero_of_not_linearIndependent.md) | 8 | 8 | `e5a6285` |
| [det_choose_eq](Wronskian-det_choose_eq.md) | 16 | 13 | `a6ab470` |
| [sum_range_card_le_sum](Wronskian-sum_range_card_le_sum.md) | 11 | 0 | `c30f58c` |
| [coeff_prod_of_natDegree_le'](Wronskian-coeff_prod_of_natDegree_le.md) | 12 | 11 | `1c983b5` |
| [sum_range_le_sum_of_injective](Wronskian-sum_range_le_sum_of_injective.md) | 6 | 8 | `ab65b1b` |
| [coeff_wronskian_of_natDegree_injective](Wronskian-coeff_wronskian_of_natDegree_injective.md) | 29 | 22 | `edaf9aa` |
| [wronskian_ne_zero_of_natDegree_injective](Wronskian-wronskian_ne_zero_of_natDegree_injective.md) | 8 | 5 | `a860965` |
| [wronskian_update_sub_smul](Wronskian-wronskian_update_sub_smul.md) | 10 | 7 | `64872e6` |
| [span_range_update_sub_le](Wronskian-span_range_update_sub_le.md) | 10 | 0 | `8520ced` |
| [linearIndependent_update_sub_smul](Wronskian-linearIndependent_update_sub_smul.md) | 11 | 6 | `0182ccd` |
| [sum_natDegree_update_lt](Wronskian-sum_natDegree_update_lt.md) | 23 | 19 | `ab266cd` |
| [wronskian_ne_zero_of_linearIndependent](Wronskian-wronskian_ne_zero_of_linearIndependent.md) | 11 | 10 | `7f3fa5a` |
| [wronskian_eq_zero_iff](Wronskian-wronskian_eq_zero_iff.md) | 4 | 4 | `ed342ce` |

Final counts include whole declarations, excluding documentation and scope commands: 162 → 116 declaration lines (−46). Two original private helpers are removed after their completed audits; all 12 public declarations and the private coefficient-product lemma remain. Source: 271 → 219 lines (−52, 19.2%).

## Phase 5a — non-rename refactoring

1. Removed private `sum_range_card_le_sum`, following declaration5/7 search findings. Its sole public caller now specializes Mathlib `Finset.sum_range_le_sum` to the image of the injective natural-valued function, embedded into integers with lower bound zero. Added the narrow `Mathlib.Algebra.Order.Group.Int.Sum` import. The standalone replacement compiled with no diagnostics before editing; complete source LSP passed after editing. Public signature and conclusion are unchanged.
2. Removed private `span_range_update_sub_le`, following declaration11/12 findings. Its sole caller already uses Mathlib `Submodule.span_range_update_sub_smul`; a source search verified no remaining use. Complete source LSP passed after deletion.

These are routine internal Mathlib replacements, not public theorem generalisations. No project split or new definition was needed. The coefficient identity proposal is deliberately unapplied: its existing documentation already states that the two hypotheses are unnecessary, but public removal still awaits the user's decision. No rename was inferred from that pending proposal.

## Phase 5b — rename pass

All 15 reports queue no rename; `.mathlib-quality/renames.jsonl` is absent. Raw/deduped depth 0/0; applied/skipped/conflicting renames 0/0/0; caller files modified 0. The cleanup-all project-wide rename pass remains scheduled after all files. No shared queue mutation occurred here.

## Phase 6a — diagnostics, preservation, and identifiers

Complete final native LSP: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, exactly three warnings: unchanged missing copyright metadata at line1 and unused `hφ`/`hd` at lines116–117. This is not a warning-free result. Neither warning category has been hidden.

Analysis against `d259f95` (`/private/tmp/roth-wronskian-final-analysis.json`) confirms every block comment/docstring byte-identical, narrative proof comments 0 → 0, and no line over 100 codepoints. Hygiene scan finds no sorry/admit, custom axiom, unsafe/native_decide, FIXME/TODO, option/limit override, profiling scaffolding, λ, `$`, or push_neg. `git diff --check` passes.

The original baseline source was compiled under `RothBaseline` alongside the final module; `rfl` examples compare all 12 original public declarations, checking exact elaborated types and both definition values (theorems use proof irrelevance). Command `lake env lean /private/tmp/roth-wronskian-final-compatibility.lean`, session16695, exit0; repeated after simplify as session62603, exit0 (`/private/tmp/roth-wronskian-post-simplify-compatibility.log`). All printed public axioms are exactly `[propext, Classical.choice, Quot.sound]`; no sorryAx. The remaining private theorem was independently isolated/type/axiom-checked in its declaration report. Baseline warning output in that probe is expected.

Every introduced external name was positively verified. Local search was called first; index error/warming is not absence. Positive source results and compiled native `#check` supply the evidence. Local projections `h.1`, `h.2`, `hd.injOn` and `.mp` resolve through their verified types.

| Introduced external identifier | Evidence | Result |
|---|---|---|
| `Finset.forall_mem_insert` | local source result + native `#check` | pass |
| `Finset.sum_range_le_sum` | local source result + native `#check` | pass |
| `Function.update_apply` | local source result + native `#check` | pass |
| `Matrix.det` | local source result + native `#check` | pass |
| `Matrix.updateCol_apply` | local source result + native `#check` | pass |
| `Nat.castEmbedding` | local source result + native `#check` | pass |
| `Nat.cast_sum` | local source result + native `#check` | pass |
| `Submodule.span_range_update_sub_smul` | local source result + native `#check` | pass |
| `Function.Injective.injOn` | native `#check`; local proof projection | pass |
| `imp_not_comm` / `Iff.mp` | local search / native `#check` | pass |
| `linearIndependent_iff_card_eq_finrank_span` | existing identifier; new `.mp` use compiled | pass |
| `apply_ite` | local index warming, source search inconclusive; native `#check` succeeds | pass |
| `exact_mod_cast` | imported tactic syntax; standalone and module compilation | pass |

Direct external uses occur in GenWronskian and Separation; the full build validates their entire downstream closure. LeanEval is separately built because root Roth does not import it. No external caller needed modification.

## Phase 6b — cumulative gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.Wronskian`, session91443, exit0; `/private/tmp/roth-wronskian-final-module.log` |
| lake_build | pass | `lake build`, session2376, exit0, 2587 jobs; `/private/tmp/roth-wronskian-final-full.log` |
| definition_protected | pass | Original public definitions compared by compiled `rfl`; only lambda/ascription syntax changed |
| theorem_statement_protected | pass | All original public types compare; two private deletions trace to Phase5a; pending generalisation not applied |
| cumulative_no_unintended_breakage | pass | Full closure plus `lake build Roth.LeanEval`, session44062, exit0; `/private/tmp/roth-wronskian-final-leaneval.log` |

Overall before simplify: pass. Source remained frozen throughout these builds. Post-simplify module session76381, full session10167 (2587 jobs), and separate LeanEval session82516 (2586 jobs) all exited0 on the final frozen source. Overall after simplify: pass. Logs use `/private/tmp/roth-wronskian-post-simplify-{module,full,leaneval}.log`.

## Phase 6.5 — independent simplify pass

Fresh independent reviewer `final_simplify` inspected the cumulative source/diff and Mathlib helper reuse, then compiled exact source with five redundant import lines removed. The owner applied this concrete finding: removed BigOperators, Degree.Lemmas, Dimension.Finite, Matrix.NonsingularInverse, and Polynomial.Pochhammer imports. Five direct roots remain; their transitive dependencies supply the needed declarations. No dependency-closure or speed improvement is claimed. Status: ISSUES-FOUND-AND-FIXED. Post-change module session76381 and original-type compatibility session62603 exited0; complete native LSP again reports zero errors and the same three warnings. Full dependent build session10167 and separate LeanEval session82516 both exited0. All cumulative gates therefore pass after the review fix. See [independent review](Wronskian-simplify.md). The built-in `/simplify` tool was not exposed; this fresh independent holistic review implements the required review purpose without falsely claiming a tool invocation.

## Phase 6.6 — actual performance pass

Actual pinned Lean4.34 invocation: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Wronskian.lean`, session16927, exit0. Imports came from the warm cache. Raw trace: `/private/tmp/roth-wronskian-final-profile-trace.log`; parser: `/private/tmp/roth-wronskian-profile-parse.py`; machine table: `/private/tmp/roth-wronskian-final-profile-table.json`. The parser anchors command headers to all 13 retained declarations, including the private apostrophe name, and sums command elaboration plus associated async proof/typechecking/compiler work, excluding separately identified linter execution. Proof time is shown separately; the conservative total is the budget measure. This is measured trace evidence, not an aggregate-category estimate. The first sweep overlapped the separately running LeanEval build, so wall-clock contention was possible; every measured total is nevertheless below the 750ms lower boundary of the required ±25% recheck band.

| Declaration | Source line | Command ms | Proof ms | Total ms | Dominant step | Over 1000ms? |
|---|---:|---:|---:|---:|---|---|
| `coeff_wronskian_of_natDegree_injective` | 116 | 29.56 | 600.11 | 647.20 | `simp [coeff_intCast_mul, key, Finset.prod_mul_distrib, mul_comm, mul_assoc]` | no |
| `sum_range_le_sum_of_injective` | 101 | 7.54 | 564.07 | 588.89 | `exact_mod_cast` | no |
| `wronskian_eq_zero_of_not_linearIndependent` | 59 | 7.94 | 539.87 | 565.22 | `simpa [wronskianMatrix, Matrix.mulVec, dotProduct, ← smul_eq_C_mul,` | no |
| `wronskian_ne_zero_of_natDegree_injective` | 143 | 5.93 | 511.78 | 521.94 | `simpa [h0, det_choose_eq, eq_comm (a := 0), Finset.prod_eq_zero_iff, sub_eq_zero, hφ,` | no |
| `wronskian_update_sub_smul` | 153 | 16.33 | 292.84 | 318.67 | `simp [wronskianMatrix, Matrix.updateCol_apply, Function.update_apply, apply_ite,` | no |
| `sum_natDegree_update_lt` | 177 | 30.83 | 262.62 | 297.71 | `have hdeg' : degree (φ ν') = degree (C a * φ ν) := by` | no |
| `det_choose_eq` | 73 | 45.43 | 206.77 | 254.76 | `have h1 :` | no |
| `coeff_prod_of_natDegree_le'` | 87 | 15.30 | 94.10 | 119.81 | `induction s using Finset.induction_on with` | no |
| `linearIndependent_update_sub_smul` | 165 | 21.17 | 86.17 | 114.36 | `rw [linearIndependent_iff_card_eq_finrank_span, Set.finrank, ← smul_eq_C_mul,` | no |
| `wronskian_ne_zero_of_linearIndependent` | 200 | 9.42 | 55.70 | 66.59 | `induction hN : ∑ ρ, (φ ρ).natDegree using Nat.strong_induction_on generalizing` | no |
| `wronskianMatrix` | 50 | 39.21 | 0.00 | 40.02 | `term elaboration` | no |
| `wronskian_eq_zero_iff` | 214 | 7.71 | 5.77 | 13.85 | `term elaboration` | no |
| `wronskian` | 54 | 9.81 | 0.00 | 10.12 | `term elaboration` | no |

FAST BOARD — all 13 declarations below 1000ms; maximum 647.20ms. No declaration lies in the 750–1250ms remeasurement band. No optimization, limit increase, source instrumentation, or `/decompose-proof` deferral was required. No proof changed after profiling; no extra build is needed for report-only edits. Profiling and final LeanEval both exited0; no orphan probe remains.


## Phase 7 — final disposition

All authorized source work and required checks are complete. Known limitations: unchanged header metadata by user decision; the approved coefficient-hypothesis removal is implemented and verified. The overall project is incomplete: 61/264 original declarations audited; Taylor is active.


## Required phase checklist

- [x] Phase 0: successful baseline build and complete LSP.
- [x] Phase 1: complete file/reference reading and declaration inventory.
- [x] Phase 2: file, linter, and declaration audit punch-list.
- [x] Phase 3: file-level style/doc/header policy handled.
- [x] Phase 4: 15 fresh dedicated audits, full artifacts/gates, individually pushed checkpoints.
- [x] Phase 5a: two verified private helper replacements/removals.
- [x] Phase 5b: empty file rename queue; global pass remains scheduled project-wide.
- [x] Phase 6: cumulative module/full/separate LeanEval, LSP, type/definition/axiom, hygiene gates.
- [x] Phase 6.5: fresh independent holistic simplify finding applied and all gates rerun.
- [x] Phase 6.6: actual anchored per-declaration profiling; all 13 below budget.
- [x] Phase 7: complete final report, with explicit unchanged header limitation and resolved API decision.

## User-approved hypothesis amendment (2026-10-15)

The user approved removal of both unused `hφ`/`hd` arguments from
`coeff_wronskian_of_natDegree_injective`, preserving its name and conclusion,
and the minimal sole-caller update to `(φ := φ)`. A fresh narrow worker applied exactly
those two replacements. All other source, definitions, proof, documentation and the
nonvanishing caller's hypotheses remain byte-identical. Earlier pending-proposal
statements in historical checkpoints are superseded by this approval and implementation.

Wronskian source is now271→218lines,13retained declarations; the original audit count
remains15. Module28780 exit0, complete LSP zeroerrors and only the user-preserved header
warning, independent pre-target theorem/caller compilation and standard-axiom checks pass.
Actual profiling5470 exit0: all13 below750ms, maximum586.13ms; caller457.33ms.
Full `lake build` session30588 exit0 (2587jobs), followed by separate
`lake build Roth.LeanEval` session6721 exit0 (2586jobs). The full result was recovered
successfully after a usage interruption; both source hashes stayed unchanged.
Logs `/private/tmp/roth-wronskian-approved-{full,leaneval}.log`.
Frozen Wronskian SHA256 `b4f0c0db36bcbd81983f5a38c137dcefdf57bce18e12445e8241689a8abf888e`.
[Full amendment evidence](Wronskian-approved-hypotheses.md). No API proposal remains pending.
This amendment does not increment the264original-declaration tally; Taylor remains6/20,
overall61/264. Taylor7 resumes after this separate publication checkpoint.
