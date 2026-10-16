# Taylor final file-level cleanup report

Status: all 20 original declarations, both added private helpers, and all final file phases complete. Source checkpoint `6f039c2`; source SHA256 `31af75afd28f840ddee51978509ba63b28536aa84bba56dc047df2aa4b23fbdc`. Public mathematical API, original definition value, documentation and toolchain preserved. Missing copyright metadata remains an explicit user-preserved warning, not a clean-lint claim.

## Phases 0–3 — baseline and preparation

[Initial file audit](Taylor.md) records baseline `6c4df1d1a6644e6bbaeedad9fc50fb2ebaba5e6a`,239 source lines,20 declarations (17 public,3 private), baseline full build session9844 exit0, complete native diagnostics and the complete file-level punch-list. Both skills and full cleanup/cleanup-all workflows were read. Classic imports retained; project imports alphabetized. Module/docs/sections preserved; no invented metadata or linter suppression. No standalone runLinter configured; normal mathlib linters run during compilation.

## Phase 4 — declaration artifact sweep

Every original declaration received its own fresh dedicated worker and separate audit; both extracted helpers subsequently received fresh independent dedicated audits. The reports contain all24 audit items, all42 golfing rules, five search methods, per-parameter generalisation analyses, public literature checks (private exemption explicit), measured signature/inequality artifacts, actual proof experiments, local module/complete-LSP/isolation/type/axiom gates and all11 required checklist steps. Optional negative-probe limitations in declarations13/15 are disclosed rather than counted as successful weakenings. No successful necessary generalisation remains unimplemented.

Each declaration was frozen before parent validation, with source ownership explicitly revoked. Full `lake build` then separate `lake build Roth.LeanEval` passed before exact-path stage/commit/push and the next source edit. LeanEval is separate because root Roth does not import it. All20 originals remain; two private helpers were added. Model changes followed user instruction: later workers switched first to Astra Medium, then new workers from declaration14 onward to Sol Medium; existing workers finished without a claimed model switch.

Machine sweep `/private/tmp/roth-taylor-final-analysis.json` confirms22 individual reports,42 rule labels each, at least11 checked steps each and no unchecked item. The extra checkbox in the coefficient-product report is supplemental. Actual report content was inspected individually. All local structural/naming/packing/inequality gates pass.

| Declaration / dedicated audit | Original lines | Final lines | Original checkpoint |
|---|---:|---:|---|
| [taylor](Taylor-taylor.md) | 2 | 2 | `3ed5784` |
| [taylor_apply](Taylor-taylor_apply.md) | 2 | 2 | `8c39c00` |
| [taylor_X](Taylor-taylor_X.md) | 2 | 1 | `ef61039` |
| [taylor_C](Taylor-taylor_C.md) | 2 | 1 | `49abee2` |
| [taylor_monomial](Taylor-taylor_monomial.md) | 3 | 3 | `0d5433c` |
| [coeff_aeval_X_mul](Taylor-coeff_aeval_X_mul.md) | 24 | 18 | `d0e7999` |
| [hasseCoeff_single_add_eq](Taylor-hasseCoeff_single_add_eq.md) | 16 | 9 | `258cfa4` |
| [prod_pow_single_add_tsub](Taylor-prod_pow_single_add_tsub.md) | 11 | 8 | `4239ed6` |
| [coeff_taylor](Taylor-coeff_taylor.md) | 35 | 5 | `5496d75` |
| [eval_taylor](Taylor-eval_taylor.md) | 3 | 3 | `dbac1c0` |
| [taylor_taylor](Taylor-taylor_taylor.md) | 3 | 3 | `771528e` |
| [taylor_zero](Taylor-taylor_zero.md) | 2 | 2 | `3002adc` |
| [taylor_map](Taylor-taylor_map.md) | 3 | 3 | `7472875` |
| [taylor_rename](Taylor-taylor_rename.md) | 3 | 3 | `e3400a8` |
| [degreeOf_taylor_le](Taylor-degreeOf_taylor_le.md) | 5 | 4 | `ae051f3` |
| [taylor_neg_taylor](Taylor-taylor_neg_taylor.md) | 3 | 3 | `59c59a0` |
| [taylor_injective](Taylor-taylor_injective.md) | 2 | 2 | `8585448` |
| [taylor_eq_zero_iff](Taylor-taylor_eq_zero_iff.md) | 2 | 2 | `32473ad` |
| [eq_sum_box_hasseDeriv](Taylor-eq_sum_box_hasseDeriv.md) | 18 | 17 | `8994327` |
| [eval_eq_sum_box](Taylor-eval_eq_sum_box.md) | 5 | 4 | `93fb44e` |
| [coeff_taylor_monomial_single_add_aux](Taylor-coeff_taylor_monomial_single_add_aux.md) | added | 18 | `2c552b3` |
| [coeff_taylor_monomial_aux](Taylor-coeff_taylor_monomial_aux.md) | added | 10 | `53f4983` |

Final counts include whole declarations, excluding documentation/scope commands:146→123 declaration lines (−23), including both new helpers. Source239→218 lines (−21,8.8%). The coefficient theorem body shrank33→3 lines; evaluated expansion2→1. The polynomial expansion now has14 tactic lines (15 including its `:= by` line). The independent final review further shortened the variable-degree proof3→2 body lines after its original checkpoint.

## Phase 5a — non-rename refactoring

The coefficient proof was separated into the monomial induction and its substantial single-add step, with two private helpers; both required follow-up audits are complete. Direct library evaluation/composition and Finsupp lemmas replace redundant inductions/manual support manipulations. No outstanding cross-declaration refactor remains. The speculative CommMonoid helper generalisation and public-wrapper deletion ideas were closed without implementation: no needed caller benefit, and explicit public API preservation governs. No public signature, mathematical definition or project structure change was applied in Taylor. No user decision is pending for this file.

## Phase 5b — rename pass

| Raw queue | Deduplicated queue | Applied | Conflicts | Caller files changed |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |

All reports queue no rename; `.mathlib-quality/renames.jsonl` is absent. No queue mutation. The cleanup-all global rename pass remains scheduled for project end.

## Phase 6a — cumulative preservation, diagnostics and identifiers

Final complete native whole-file Taylor diagnostics: success=true,partial=false,timed_out=false,failed_dependencies=[],zero errors,one preserved line1 copyright warning. No target warning or sorry. Direct external callers are `Roth/Index.lean` and `Roth/Main.lean`; both complete native diagnostics succeeded with partial=false and no errors. Their existing header/unused-hypothesis warnings remain for their own future file audits, including previously recorded Index.index_le_card `hr`; they were not suppressed or changed here. Full builds validate the whole downstream closure.

Baseline source was compiled in namespace `TaylorBaseline` alongside the final module. All17 public constants compare by `rfl`, checking exact elaborated types and the original taylor definition value; theorem equality uses proof irrelevance. Initial compatibility session75242 exit0; post-review after module completion session7752 exit0. File `/private/tmp/roth-taylor-final-compatibility.lean`, final log `/private/tmp/roth-taylor-post-simplify-compatibility-final.log`. All public printed axioms are standard `[propext, Classical.choice, Quot.sound]`; private declarations were individually isolated/type/axiom checked in their audits.

Block comments/docstrings are byte-identical to baseline; narrative proof comments0→0. No line exceeds100 codepoints. No sorry/admit, custom axiom, native_decide, FIXME/TODO, option/limit override, λ, dollar application or push_neg; no profiling scaffolding. `git diff --check` passes. Temporary probes live outside the repository.

Introduced external identifiers were checked through local search, positive source evidence and a successful native compiled batch of20 `#check`s. Index errors did not establish absence. Detailed tool evidence: `/private/tmp/roth-taylor-final-tool-evidence.json`.

| Identifier | Verification | Result |
|---|---|---|
| `MvPolynomial.aeval_X` | source/local lookup and native `#check` | pass |
| `MvPolynomial.algHom_C` | source/local lookup and native `#check` | pass |
| `Polynomial.aeval_def` | source/local lookup and native `#check` | pass |
| `Polynomial.eval₂_eq_sum` | source/local lookup and native `#check` | pass |
| `Polynomial.sum_def` | source/local lookup and native `#check` | pass |
| `tsub_eq_of_eq_add` | source/local lookup and native `#check` | pass |
| `Finsupp.erase_add_single` | source/local lookup and native `#check` | pass |
| `Finsupp.mul_prod_erase'` | source/local lookup and native `#check` | pass |
| `Finsupp.support_erase` | source/local lookup and native `#check` | pass |
| `Finset.ne_of_mem_erase` | source/local lookup and native `#check` | pass |
| `MvPolynomial.eval_assoc` | source/local lookup and native `#check` | pass |
| `MvPolynomial.comp_aeval_apply` | source/local lookup and native `#check` | pass |
| `MvPolynomial.aeval_X_left_apply` | source/local lookup and native `#check` | pass |
| `MvPolynomial.map_eval₂` | source/local lookup and native `#check` | pass |
| `Function.comp_def` | source/local lookup and native `#check` | pass |
| `MvPolynomial.rename_eq_aeval` | source/local lookup and native `#check` | pass |
| `congrArg` | source/local lookup and native `#check` | pass |
| `MvPolynomial.aeval_def` | source/local lookup and native `#check` | pass |
| `Finsupp.single_tsub` | source/local lookup and native `#check` | pass |
| `MvPolynomial.hasseDeriv_C` | source/local lookup and native `#check` | pass |

Existing APIs moved into helpers (`aeval_monomial`, `coeff_X_add_C_pow`, `hasseCoeff` and related lemmas) retain their verified imports; local variables and projection methods are checked by the actual module/isolated compilation. No unverified external name remains.

## Phase 6b — cumulative gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | Final module60520 exit0; after reviewer fix module87739 exit0; after profiling module42517 exit0 |
| lake_build | pass | Initial final81114 exit0; after reviewer fix91300 exit0 (2587 jobs) |
| separate LeanEval | pass | Initial final70103 exit0; after reviewer fix69418 exit0 (2586 jobs), sequential after full build |
| definition_protected | pass | Only synonymous lambda notation in original definition; baseline value `rfl` comparison passes |
| theorem_statement_protected | pass | All17 public original constants compare by rfl; original private signatures preserved, new helpers independently audited |
| cumulative_no_unintended_breakage | pass | Complete Index/Main diagnostics no errors; full build and separate LeanEval pass, no caller changes |
| structure/naming/packing/inequality | pass | All22 audits and independent holistic review; no outstanding failure |

Logs: `/private/tmp/roth-taylor-final-{module,full,leaneval}.log`, `/private/tmp/roth-taylor-simplify-{module,full,leaneval}.log`, `/private/tmp/roth-taylor-post-profile-module.log`. Overall: pass, with explicit header-metadata limitation.

## Phase 6.5 — independent simplify pass

Outcome: ISSUES-FOUND-AND-FIXED. Fresh independent Sol Medium reviewer examined the complete file and cumulative diff for reuse, quality, structure and efficiency; see [review](Taylor-simplify.md). Built-in `/simplify` is unavailable on this host, so the required fresh independent reviewer supplied the holistic fallback. It found one compiled improvement: replace the degree proof's final rewrite/contradiction with terminal simp. Parent applied exactly that proof-only fix and reran the module, complete diagnostics, baseline compatibility, full build and separate LeanEval. Published `6f039c2`. No further actionable issue or pending suggestion. No new public API/helper was introduced by review.

## Phase 6.6 — actual performance sweep

Outcome: FAST-BOARD. Budget1000ms; all22 retained declarations below750ms, so none meets the ±25% borderline re-sweep criterion. No slow-declaration diagnosis/fix/propagation was needed. No limit raises removed or added (0/0), no deferrals or approval-dependent changes.

Actual command, session24788 exit0:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Taylor.lean`.
Pinned Lean4.34 trace mode supplies command/declaration anchors; the aggregate profiler alone lacks them. Parsed every `Elab.command` and associated asynchronous proof/type-checking/compiler task, excluding separately tagged linter tasks. Parent and child trace nodes are not summed twice. Conservative total is command plus associated asynchronous tasks; nested tactic time identifies a representative dominant step. All22 source declarations matched parser anchors. No other build/profile ran concurrently. Raw trace `/private/tmp/roth-taylor-final-profile-trace.log`; parser `/private/tmp/roth-taylor-final-profile-parse.py`; table `/private/tmp/roth-taylor-final-profile-table.json`.

| Declaration | Line | Command ms | Proof ms | Conservative total ms | Representative dominant step | Over budget |
|---|---:|---:|---:|---:|---|---|
| `taylor` | 36 | 48.70 | 0.00 | 49.65 | term elaboration | no |
| `taylor_apply` | 40 | 20.30 | 6.21 | 27.48 | term elaboration | no |
| `taylor_X` | 45 | 9.01 | 3.80 | 13.73 | term elaboration | no |
| `taylor_C` | 49 | 9.41 | 16.83 | 28.25 | term elaboration | no |
| `taylor_monomial` | 53 | 22.27 | 14.11 | 40.67 | term elaboration | no |
| `coeff_aeval_X_mul` | 57 | 24.34 | 362.21 | 408.51 | simp [tsub_eq_of_eq_add (Finsupp.erase_add_single i d).symm] | no |
| `hasseCoeff_single_add_eq` | 76 | 8.51 | 95.32 | 106.67 | simp [Finsupp.single_eq_of_ne (Finset.ne_of_mem_erase hj)] | no |
| `prod_pow_single_add_tsub` | 86 | 15.63 | 515.78 | 546.32 | have h : | no |
| `coeff_taylor_monomial_single_add_aux` | 95 | 54.46 | 601.59 | 672.30 | simp [mul_assoc, mul_comm, mul_left_comm] | no |
| `coeff_taylor_monomial_aux` | 114 | 47.73 | 158.06 | 225.63 | induction k using Finsupp.induction generalizing d with | no |
| `coeff_taylor` | 128 | 23.30 | 191.41 | 222.90 | induction P using MvPolynomial.induction_on' with | no |
| `eval_taylor` | 135 | 8.51 | 147.32 | 172.31 | simp [taylor, aeval_def, ← eval_assoc, Function.comp_def] | no |
| `taylor_taylor` | 140 | 9.51 | 108.82 | 124.47 | simp [taylor, comp_aeval_apply, add_assoc] | no |
| `taylor_zero` | 146 | 8.07 | 25.62 | 35.96 | simp [taylor, aeval_X_left_apply] | no |
| `taylor_map` | 151 | 27.40 | 236.35 | 274.28 | simp [taylor, aeval_def, map_eval₂, Function.comp_def] | no |
| `taylor_rename` | 158 | 30.00 | 168.81 | 208.93 | simp [taylor, rename_eq_aeval, comp_aeval_apply] | no |
| `degreeOf_taylor_le` | 164 | 5.85 | 57.00 | 65.48 | simp [mem_support_iff, coeff_taylor, hasseDeriv_eq_zero_of_degreeOf_lt h] at he | no |
| `taylor_neg_taylor` | 176 | 9.39 | 33.58 | 46.57 | simp [taylor_taylor] | no |
| `taylor_injective` | 181 | 7.40 | 2.04 | 10.08 | term elaboration | no |
| `taylor_eq_zero_iff` | 186 | 17.89 | 62.32 | 82.98 | term elaboration | no |
| `eq_sum_box_hasseDeriv` | 191 | 98.57 | 314.84 | 424.68 | have h1 : taylor α P = ∑ d ∈ Roth.box r, monomial d (eval α (hasseDeriv d P)) := | no |
| `eval_eq_sum_box` | 211 | 42.21 | 297.52 | 344.82 | simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP) | no |

Maximum672.30ms (`coeff_taylor_monomial_single_add_aux`); unchanged source hash after profiling. Post-profile module42517 exit0 and diff/hygiene gates pass. No benchmark-derived proof edit or temporary instrumentation entered the repository.

## Completion and remaining project work

Taylor is complete:20/20 original declarations plus2 added private helpers; overall original-project tally75/264. Existing missing header metadata remains explicit under user instruction. No other Taylor limitation or pending mathematical proposal. Next file is CoeffNorm under a fresh file owner; this worker does not start it. Project-wide rename and remaining file cleanup phases are not claimed complete.
