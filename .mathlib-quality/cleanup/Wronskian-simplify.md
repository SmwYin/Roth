# Independent holistic simplify review — Roth/Wronskian.lean

## Simplify pass — Roth/Wronskian.lean

Outcome: ISSUES-FOUND-AND-FIXED

Issues identified by the independent simplify equivalent:
- Five explicit imports are transitively redundant; the exact cumulative file compiles with all five removed together (details below).

Fixes applied by this reviewer:
- No source fixes by this reviewer. The coordinator confirmed applying exactly the five verified import removals after receiving this finding; source is now frozen at 219 lines. Coordinator post-change checks are pending (module build session 76381, followed by full build, separate LeanEval, and diagnostics).

Files modified:
- By this reviewer: `.mathlib-quality/cleanup/Wronskian-simplify.md` only.
- By the coordinator implementing this finding: `Roth/Wronskian.lean` (five imports removed).

## Scope and workflow

Fresh independent review of the complete 224-line file and cumulative diff against `d259f95` (271 original lines), after the coordinator's cumulative gates. Read the installed Lean 4 and mathlib-quality skills and the actual Phase 6.5 workflow at `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`. The built-in `/simplify` skill is not exposed here; this is its explicitly requested independent holistic review equivalent, not a claim that the unavailable skill ran.

Source and Git were not edited. No subdelegation. Prior individual audits were consulted only after the first complete source/diff reading, to avoid duplicating already tested proof alternatives. Existing public signatures and definitions, documentation, and the user-preserved header policy remain authoritative.

## Compiled finding: redundant imports

Remove these five import lines as a single optional hygiene change:

```lean
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.RingTheory.Polynomial.Pochhammer
```

Retained import roots:

```lean
import Mathlib.Algebra.Order.Group.Int.Sum
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.LinearAlgebra.Dimension.OrzechProperty
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.LinearAlgebra.Vandermonde
```

Evidence: a recursive read-only traversal of actual mathlib import declarations established each removed module is already imported by a retained root. Direct examples: HasseDeriv publicly imports BigOperators; ToLinearEquiv publicly imports NonsingularInverse; Vandermonde publicly imports Pochhammer, which publicly imports Degree.Lemmas. Dimension.Finite is in the OrzechProperty import closure. The retained roots supply the actual API: `Finset.sum_range_le_sum`, Hasse derivatives, `linearIndependent_iff_card_eq_finrank_span`, `Matrix.exists_mulVec_eq_zero_iff`, and polynomial-evaluation/Vandermonde determinants.

Native `lean_run_code` received the exact current source with only those five import lines deleted. It returned `success: true`, `timed_out: false`, `isError: false` within the 45-second bound. Diagnostics contained only the existing unused `hφ` and `hd` warnings (probe lines 116–117). No header-linter result is inferred from an isolated snippet. No local fallback or repeated equivalent probe was needed.

This removes redundant source declarations only; it does not reduce the transitive dependency closure or establish a performance improvement. The reviewer did not run downstream builds on this edit. The coordinator is rerunning Phase 6 as the workflow requires; final results belong in the coordinator's report.

## Holistic assessment

- **Definitions and API:** The matrix/determinant definitions remain direct and transparent. Mathlib's `RingTheory/Polynomial/Wronskian.lean` defines the two-polynomial Wronskian, so it does not replace this arbitrary finite family construction. No new wrapper definition is warranted.
- **Reuse:** The final replacement of private sum and span helpers with `Finset.sum_range_le_sum` and `Submodule.span_range_update_sub_smul` removes actual duplicated library arguments. The new total-degree decrease proof correctly reuses updated-family independence for its nonvanishing fact. No duplicated remaining proof skeleton merits another helper.
- **Remaining private helper:** `coeff_prod_of_natDegree_le'` handles an arbitrary degree bound `n i` per factor and the coefficient at their sum. Mathlib `Polynomial.coeff_prod_of_natDegree_le` in BigOperators instead has one common bound `n` and coefficient index `s.card * n`; inspection confirms it is not a direct replacement. Its eight-line finite induction is justified and structurally clear.
- **Coefficient/determinant argument:** The permutation-local `key` cleanly separates the degree-bound case from a zero derivative/binomial factor. Keeping this fact local avoids a new single-use public or private API. The determinant sum assembly is now a short direct simplification.
- **Column operation and descent:** The matrix update identity is handled once by extensionality, then the determinant theorem applies. Span preservation supplies independence; cancellation lowers total degree; strong induction assembles these facts. The proof architecture is coherent and contains no circular dependency.
- **Public results:** `sum_range_le_sum_of_injective` is now a library specialization and is not used by the current coefficient proof, but it is existing public API and must not be deleted as dead code. The coefficient theorem's `hφ`/`hd` remain pending the user's decision; this review neither recommends applying their removal without that decision nor suppresses their warnings.
- **Clarity and scale:** Proofs are compact with mathematical intermediate facts where useful. No additional extraction is justified by the final file's size. Existing comments and module explanations still describe the implemented mathematical argument.

## Limits and disposition

No additional robust proof simplification was found beyond the concrete import hygiene change. This is not an exhaustive global theorem search or a replacement for the separate performance pass. Prior full-module, full-project, LeanEval, and public-type/definition compatibility gates are coordinator-reported evidence, not rerun or newly claimed by this reviewer. Missing header metadata is deliberately unchanged. The coordinator applied the finding, and the required post-change validation is pending at this artifact's completion. This reviewer made no source changes.


## Coordinator post-review validation

The exact five import removals passed module build76381, full build10167 (2587 jobs), separate LeanEval82516 (2586 jobs), repeated original-public-type/definition compatibility compile62603, and complete native LSP with zero errors and the unchanged three warnings. All sessions exited0. The final source remained frozen during validation and profiling. These are coordinator-run results, distinct from the reviewer's isolated experiment. Actual profiling also passed all 13 declarations under 1000ms (maximum647.20ms); see the final report.
