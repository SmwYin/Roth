# HasseDeriv final file-level cleanup report

Status: Phase 5a refactor and Phase 6 cumulative gates passed, including separate LeanEval. Independent simplify review and profiling remain in progress. Original baseline: `d2eb5e9a1806e12e66db25d15d8954ade4be9874`; final-phase starting checkpoint: `eb1710d`.

## Baseline, audit and file-level fixes (Phases 0–3)

The preserved [file audit](HasseDeriv.md) records the clean full baseline build (2586 jobs), responsive complete LSP, seven file-level audit categories, all 26 declaration inventory items, and the single baseline header warning. No file-level replacement was needed: imports were ordered, module documentation present, and no option override existed. Copyright/license metadata is still unconfirmed. No attribution or license was invented.

## Post-Phase-4 artifact sweep and declaration results

All 26 original declarations have their own preserved audit, including 24 audit items, 42 golfing rules, five-method search status, signature/inequality checks and an 11-step completed checklist. Searches that failed (notably LeanSearch HTTP 500) remain explicitly recorded as unavailable, not evidence of absence. Each declaration has an actual module build, complete LSP, type/axiom checks, full project build, and separate LeanEval checkpoint already recorded by its worker and file owner. These workflows were not repeated or replaced by a batch audit.

Counts below are complete declaration lines, excluding following blank lines and docstrings. The removed private helper remains a row in the original inventory.

| Original declaration / audit | Before | Final | Delta | Phase-4 checklist |
|---|---:|---:|---:|---|
| [hasseCoeff](HasseDeriv-hasseCoeff.md) | 1 | 1 | +0 | 11/11 complete |
| [hasseDeriv](HasseDeriv-hasseDeriv.md) | 4 | 4 | +0 | 11/11 complete |
| [hasseDeriv_monomial](HasseDeriv-hasseDeriv_monomial.md) | 3 | 3 | +0 | 11/11 complete |
| [hasseDeriv_apply](HasseDeriv-hasseDeriv_apply.md) | 4 | 3 | -1 | 11/11 complete |
| [hasseCoeff_eq_zero_iff](HasseDeriv-hasseCoeff_eq_zero_iff.md) | 3 | 3 | +0 | 11/11 complete |
| [coeff_hasseDeriv](HasseDeriv-coeff_hasseDeriv.md) | 12 | 12 | +0 | 11/11 complete |
| [hasseCoeff_eq_prod](HasseDeriv-hasseCoeff_eq_prod.md) | 3 | 2 | -1 | 11/11 complete |
| [hasseDeriv_zero_apply](HasseDeriv-hasseDeriv_zero_apply.md) | 3 | 3 | +0 | 11/11 complete |
| [hasseDeriv_zero](HasseDeriv-hasseDeriv_zero.md) | 2 | 2 | +0 | 11/11 complete |
| [hasseDeriv_C](HasseDeriv-hasseDeriv_C.md) | 3 | 3 | +0 | 11/11 complete |
| [hasseDeriv_map](HasseDeriv-hasseDeriv_map.md) | 4 | 4 | +0 | 11/11 complete |
| [hasseDeriv_rename](HasseDeriv-hasseDeriv_rename.md) | 11 | 9 | -2 | 11/11 complete |
| [choose_mul_choose_eq](HasseDeriv-choose_mul_choose_eq.md) | 6 | 0 | -6 | 11/11 complete |
| [hasseCoeff_mul_hasseCoeff](HasseDeriv-hasseCoeff_mul_hasseCoeff.md) | 14 | 16 | +2 | 11/11 complete |
| [hasseDeriv_hasseDeriv](HasseDeriv-hasseDeriv_hasseDeriv.md) | 5 | 5 | +0 | 11/11 complete |
| [hasseDeriv_hasseDeriv_of_disjoint](HasseDeriv-hasseDeriv_hasseDeriv_of_disjoint.md) | 5 | 5 | +0 | 11/11 complete |
| [hasseCoeff_mul_succ](HasseDeriv-hasseCoeff_mul_succ.md) | 25 | 5 | -20 | 11/11 complete |
| [pderiv_hasseDeriv](HasseDeriv-pderiv_hasseDeriv.md) | 9 | 6 | -3 | 11/11 complete |
| [degreeOf_hasseDeriv_le](HasseDeriv-degreeOf_hasseDeriv_le.md) | 5 | 5 | +0 | 11/11 complete |
| [hasseDeriv_eq_zero_of_degreeOf_lt](HasseDeriv-hasseDeriv_eq_zero_of_degreeOf_lt.md) | 6 | 5 | -1 | 11/11 complete |
| [hasseDeriv_monomial_mul](HasseDeriv-hasseDeriv_monomial_mul.md) | 15 | 13 | -2 | 11/11 complete |
| [hasseDeriv_mul_of_degreeOf_eq_zero](HasseDeriv-hasseDeriv_mul_of_degreeOf_eq_zero.md) | 6 | 5 | -1 | 11/11 complete |
| [hasseDeriv_single_aeval_X](HasseDeriv-hasseDeriv_single_aeval_X.md) | 10 | 8 | -2 | 11/11 complete |
| [uniqueAlgEquiv_hasseDeriv](HasseDeriv-uniqueAlgEquiv_hasseDeriv.md) | 7 | 6 | -1 | 11/11 complete |
| [hasseCoeff_le_two_pow](HasseDeriv-hasseCoeff_le_two_pow.md) | 5 | 5 | +0 | 11/11 complete |
| [factorial_smul_hasseDeriv_single](HasseDeriv-factorial_smul_hasseDeriv_single.md) | 9 | 7 | -2 | 11/11 complete |

## Phase 5a — Non-rename refactoring

- Removed the single-use private scalar helper `choose_mul_choose_eq`. Its sole caller now specializes `Nat.choose_mul` directly, retaining explicit binomial symmetry and the standard bound `Nat.le_add_left`. Source search found exactly the declaration and this one call. The scalar specialization compiled independently through native `lean_run_code`; the real file subsequently passed module build and complete diagnostics. This is routine internal proof refactoring; no public declaration was removed or restated. Net change in this phase: 3 additions, 6 deletions (−3 lines).
- Kept `hasseCoeff` and `hasseDeriv`: both are substantive definitions with repeated downstream uses. Kept the remaining private coefficient and monomial helpers because they separate genuinely reusable mathematical steps; `hasseCoeff_mul_hasseCoeff` serves both composition and successor coefficient identities.
- Closed the arbitrary-function upper coefficient argument proposal as unwarranted for current callers: polynomial exponents are finitely supported throughout this development. Generalizing would change a useful existing interface without an identified caller needing the extra scope.
- Closed the noncommutative-semiring/module-valued derivative and additive-only coefficient map proposals as speculative API projects: the current multivariate-polynomial construction and all callers use commutative coefficient semirings; no current proof needs the alternate construction.
- Closed support-specific renaming and public monomial-vanishing companions as unnecessary current API expansion. Existing injective renaming is used by Separation, and vanishing is already composed from the coefficient criterion and monomial computation.
- Closed the abstract iterative Hasse–Schmidt framework and bundled composition counterpart proposals as unwarranted for this concrete polynomial development; the current pointwise composition/partial-derivative API serves downstream proofs.
- The stronger degree-bound and sum-bound coefficient companions were explicitly declined by the user (keep current API). Neither was added; neither is an outstanding approval request.
- No required decomposition or file-splitting item remains.

## Phase 5b — Rename pass scope

Project-wide Phase 5b is deliberately deferred until every file has completed cleanup. This worker did not drain or mutate the shared queue. The queue file `.mathlib-quality/renames.jsonl` is absent, and all 26 declaration reports queue no rename.

| Deduped queue | Disposition |
|---|---|
| (empty) | No HasseDeriv rename action |

- Queue depth (raw): 0
- Queue depth (deduped): 0
- Renames applied: 0
- Renames skipped/conflicts: none
- Call sites updated: 0
- Files touched by rename pass: 0

## Verification (Phase 6a)

Complete native `lean_diagnostic_messages` after the Phase-5a edit: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors. Exactly one unchanged line-1 warning: `Copyright too short!`. Thus compilation is clean; the file is not warning-free.

Cumulative source analysis against the original baseline found 26→25 declarations (only the private scalar helper removed), all retained signatures identical modulo whitespace, and exact preservation of every block comment/docstring. Narrative proof comments: 0→0. No line exceeds 100 Unicode codepoints. No FIXME/TODO, sorry/admit, axioms, native_decide, limit override, trace/profiler/diagnostics scaffolding, λ, `$`, or push_neg appears. `git diff --check` passes.

The two definition-body edits from Phase 4 are explicitly tracked in their own audits: lambda eta-reduction in `hasseCoeff` and arrow normalization in `hasseDeriv`. Fresh independent `rfl` examples against their original definitions passed through native `lean_run_code`, so no mathematical definition changed. This scratch probe also printed only `propext`, `Classical.choice`, `Quot.sound` for the two public results depending on the inlined helper. Scratch-only line-length warnings and an informational out-of-date-import notice during the concurrent build did not occur in the source file; final actual build gates remain mandatory.

### New identifier verification

Lexical set difference of cumulative source additions identified the following new references. Local search was attempted first for every declaration; positive source-backed matches are valid even when the semantic index reports warming/error. No empty/incomplete index result was interpreted as absence. Generated additive names and the global `map_natCast` were confirmed with actual batched `#check` after source search.

| New source identifier | Verified via | Result |
|---|---|---|
| `Nat.cast_add_one` | native local search, concrete source match | pass |
| `Nat.choose_symm_add` | native local search, concrete source match | pass |
| `Nat.le_add_left` | native local search, concrete source match | pass |
| `Polynomial.hasseDeriv_coeff` | native local search, concrete source match | pass |
| `MvPolynomial.coeff_uniqueAlgEquiv` | native local search, concrete source match | pass |
| `Finsupp.prod_fintype (d.prod_fintype)` | native local search, concrete source match | pass |
| `MvPolynomial.notMem_support_of_degreeOf_lt` | native local search, concrete source match | pass |
| `MvPolynomial.sum_def` | native local search, concrete source match | pass |
| `LE.le.trans'` | native local search, concrete source match | pass |
| `tsub_eq_iff_eq_add_of_le` | native local search, concrete source match | pass |
| `add_comm` | local search → source search → native `#check` | pass |
| `add_left_comm` | local search → source search → native `#check` | pass |
| `add_right_comm` | local search → source search → native `#check` | pass |
| `mul_left_comm` | local search → source search → native `#check` | pass |
| `map_natCast` | local search → source search → native `#check` | pass |
| `simp_all` | Lean tactic syntax; actual module compilation | pass |

## Phase 6 cumulative gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | `lake build Roth.HasseDeriv`, exec session 71016, exit 0; 1430 jobs, target 15s; `/private/tmp/roth-hasse-final-module.log` |
| lake_build | pass | `lake build`, exec session 68721, exit 0; 2586 jobs; `/private/tmp/roth-hasse-final-build.log`; completed by 2026-10-15 20:39:55 UTC |
| separate LeanEval | pass | `lake build Roth.LeanEval`, exec session 13076, exit 0; 2585 jobs; `/private/tmp/roth-hasse-final-leaneval.log` |
| definition_protected | pass | Same signatures; two audited syntax-only body edits freshly confirmed definitionally equal by `rfl` |
| theorem_statement_protected | pass | All retained theorem/lemma signatures identical modulo whitespace; removal of private scalar wrapper traced to Phase 5a |
| cumulative_no_unintended_breakage | pass | All direct/transitive caller modules built successfully in actual full project build; no external source edit |
| no-sorry/no-limit/no-scaffolding | pass | Complete source scan and actual compilation |

Overall cumulative code/build gates: PASS. Known baseline header warning remains a documented metadata limitation, not a warning-free claim.

Source search inspected direct uses in `Roth.CoeffNorm`, `Roth.GenWronskian`, `Roth.Taylor`, `Roth.Index`, `Roth.Separation`, `Roth.Theta`, `Roth.MainLemma`, and `Roth.Main`; aggregate `Roth` imports the closure. The broad search also matched `Roth.Wronskian`'s univariate `Polynomial.hasseDeriv` names; it was covered by full build. Full-build logs retain unrelated baseline linter warnings in later project files for their own cleanup.

## Phase 6.5 — Independent holistic simplify review

Pending gates and fresh reviewer.

## Phase 6.6 — Buzz performance sweep

Pending independent simplify review.

## Metadata evidence and remaining limitation

The tracked tree has no LICENSE/COPYING/NOTICE/AUTHORS file. README.md contains only `# Roth`. The original HasseDeriv source in commit `3cab03b` already lacks a copyright header. History identifies contributors SmwYin and Ramin Takloo-Bighash, which is not authoritative evidence of copyright ownership or a license grant. Missing confirmed metadata: holder(s), year(s), author credit, and license. The parent has been informed; no warning suppression was inserted.

## Total line delta

329 → 288 lines: −41 lines (−12.5%). Phase 5a alone: 291 → 288. Public API, mathematical meaning, documentation, imports and toolchain preserved.
