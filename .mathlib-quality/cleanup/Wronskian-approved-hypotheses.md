# Approved Wronskian hypothesis amendment

This is a narrow amendment to the completed Wronskian audit, not an additional original declaration audit. The user explicitly approved removing both unused arguments `hφ` and `hd` from `Roth.coeff_wronskian_of_natDegree_injective`, preserving the theorem name and conclusion. The sole code caller is repaired by supplying `(φ := φ)`. The earlier proposal in [the declaration audit](Wronskian-coeff_wronskian_of_natDegree_injective.md) is now applied; its historical pending status is superseded by this amendment.

## Exact scope and protections

Baseline: `d0e7999`. Only two textual replacements were made in `Roth/Wronskian.lean`: remove the two unused binders, and replace the caller's `hφ hd` arguments with `(φ := φ)`. A scripted exact comparison against the baseline confirms the final source equals precisely those replacements. Thus all definitions, comments/docstrings, the target conclusion and proof, the caller's statement, imports, other declarations, and all remaining source are byte-identical. No rename, new API, proof refactor, option, or profiling instrumentation was added.

Repository-wide Lean source search finds the target declaration, a documentation reference, and exactly one code caller at line 146 in `wronskian_ne_zero_of_natDegree_injective`. No external code caller needs repair. The coefficient identity now applies to every polynomial family, as its existing proof and documentation already explain. Nonvanishing and degree injectivity remain necessary arguments of the subsequent nonvanishing theorem and are preserved there.

Final target signature is three lines, at lines 116–118, with Unicode codepoint widths 67, 99, and 76. No file line exceeds 100 codepoints. The file retains all 13 post-cleanup declarations; its original audit count remains 15.

## Verification

- `lake build Roth.Wronskian`: exit 0, session 28780, 1828 jobs; log `/private/tmp/roth-wronskian-approved-module.log`.
- Complete native `lean_diagnostic_messages`: `success: true`, `partial: false`, `timed_out: false`, no failed dependencies and no errors. The sole warning is the existing copyright/header warning retained by user decision. Both unused-hypothesis warnings are gone.
- Native `lean_run_code` independently compiled the complete source prefix through the repaired caller, importing only the file's five Mathlib roots, without importing `Roth.Wronskian`. This reconstructs the target and caller from their predecessors and rules out accidental reliance on their compiled original declarations. Result: `success: true`, `timed_out: false`, no errors or warnings.
- Actual `#check @Roth.coeff_wronskian_of_natDegree_injective` confirms the parameters are now `{K} [Field K] {l} {φ}` followed by the unchanged coefficient equality. The caller's `#check` retains `[CharZero K]`, nonvanishing and degree injectivity.
- Actual `#print axioms` for both target and caller reports only `propext`, `Classical.choice`, and `Quot.sound`.

## Actual profiling

Actual command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Wronskian.lean`; session 5470, exit 0. The module build and isolated/LSP checks had finished before profiling; the parent full builds begin only after this profile completed. Warm imports were available.

Raw trace: `/private/tmp/roth-wronskian-approved-profile-trace.log`. Adapted parser: `/private/tmp/roth-wronskian-approved-profile-parse.py`; current source anchors: `/private/tmp/roth-wronskian-approved-analysis.json`; machine table: `/private/tmp/roth-wronskian-approved-profile-table.json`. The existing parser was reused with new paths and current line anchors, including both noncomputable definitions and the private apostrophe name. Its assertion confirms all 13 retained declarations are represented. Total timing adds command elaboration and associated asynchronous proof/typechecking/compiler work, excluding separately identified linter execution.

| Declaration | Line | Command ms | Proof ms | Total ms |
|---|---:|---:|---:|---:|
| `wronskianMatrix` | 50 | 36.36 | 0.00 | 37.06 |
| `wronskian` | 54 | 9.46 | 0.00 | 9.63 |
| `wronskian_eq_zero_of_not_linearIndependent` | 59 | 7.14 | 453.78 | 478.43 |
| `det_choose_eq` | 73 | 40.01 | 170.20 | 213.84 |
| `coeff_prod_of_natDegree_le'` | 87 | 9.44 | 80.60 | 98.38 |
| `sum_range_le_sum_of_injective` | 101 | 5.06 | 487.89 | 509.12 |
| `coeff_wronskian_of_natDegree_injective` | 116 | 20.09 | 547.25 | 586.13 |
| `wronskian_ne_zero_of_natDegree_injective` | 142 | 6.53 | 446.56 | 457.33 |
| `wronskian_update_sub_smul` | 152 | 12.23 | 264.17 | 285.82 |
| `linearIndependent_update_sub_smul` | 164 | 18.95 | 74.30 | 97.84 |
| `sum_natDegree_update_lt` | 176 | 30.46 | 235.89 | 270.29 |
| `wronskian_ne_zero_of_linearIndependent` | 199 | 8.46 | 43.52 | 53.65 |
| `wronskian_eq_zero_iff` | 213 | 5.97 | 4.29 | 10.64 |

All 13 totals are below the 1000 ms budget and below the 750 ms lower edge of the remeasurement band. Maximum: 586.13 ms for the amended coefficient theorem; its dominant step is terminal `simp [coeff_intCast_mul, key, Finset.prod_mul_distrib, mul_comm, mul_assoc]` (292.707 ms). The repaired caller totals 457.33 ms, dominated by its terminal `simpa` (443.483 ms). No performance source change or remeasurement was required. No speedup claim is made from cross-run timing differences.

## Handoff

Final source SHA-256: `b4f0c0db36bcbd81983f5a38c137dcefdf57bce18e12445e8241689a8abf888e`.
The parent performs the full project and separate LeanEval builds after the source is frozen, then owns the shared reports and Git checkpoint. This worker has not modified shared logs, historical reports, Taylor source, or Git state.

## Parent publication validation

Final frozen-source full `lake build` session30588 exited0 (2587jobs), then separate
`lake build Roth.LeanEval` session6721 exited0 (2586jobs). Logs:
`/private/tmp/roth-wronskian-approved-full.log` and
`/private/tmp/roth-wronskian-approved-leaneval.log`. Both Wronskian and Taylor hashes
were verified unchanged. Exact-path staging and dedicated publication follow these gates.
