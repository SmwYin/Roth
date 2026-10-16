# CoeffNorm final file-level cleanup report

Current status — approved amendment, 2026-10-16: the four unused public DecidableEq
parameters and `normOne_det_le.hC` have been removed with explicit user approval.
Names, conclusions, other arguments, definitions and documentation remain unchanged.
Current source SHA256 `ee0b23cfee16cf674512a5c8f912a8030242e736db6e79fc1270be71675e67a9`.
Complete LSP has zero errors and one preserved metadata warning (previously six).
Actual current-source profiling checks all26 declarations: maximum625.993ms, all below750ms.
Independent reproofs verify all four stronger statements; all25 historical public types and
both definition values are recovered, with standard axioms only.
See [approved amendment audit](CoeffNorm-api-amendment.md) for current verification and
publication evidence. The whole-file cleanup report below is historical evidence for its
original checkpoint; its pending-proposal, warning-count and old-profile statements are
superseded by this amendment. Original project tally remains130/264;7/14 files complete.

Status: all26 original declarations, one new private helper and every final file-level phase complete. Source checkpoint `72871a7`, SHA256 `7165f8d8bacbd22a337d00a95133d3b1264c5e2a972e7e2ee6ec9ddcc6517d5c`. Public mathematical API, original definition values, documentation and pinned toolchain preserved. Header metadata and the compiled public-hypothesis proposal remain explicit limitations, not a clean-lint claim.

## Phases 0–3 — baseline and preparation

[Initial file audit](CoeffNorm.md) records baseline `e63b156a9d2faabc1bf569f0e86eb8fe82569b96`,320 source lines,26 originals (25 public,1 private), full baseline build14707 exit0 and complete native diagnostics. Both skills and full cleanup/cleanup-all workflows were read. The retained Mathlib determinant import precedes alphabetized project imports; independent review removed the redundant polynomial bridge import. Classic module dialect/docs/sections preserved. No standalone runLinter configured; ordinary mathlib linters run during compilation. Missing authoritative copyright/license metadata is explicitly user-preserved; no invented metadata or warning suppression.

## Phase 4 — declaration artifacts

Every original declaration received a fresh dedicated worker; the extracted private geometric-box helper subsequently received a separate fresh dedicated audit. All workers used the explicit user preference Sol Medium with fresh contexts. Each report contains all24 audit items, all42 golfing rules, five actual search methods, per-parameter generalisation probes, public literature/top-three comparisons (private exemption explicit), signature packing and occurrence-based inequality artifacts, actual proof alternatives, module/complete-LSP/original-type/nonself-reproof/standard-axiom gates and all11 required checklist steps. Search outages, failed probes and profiling-tool limitations are disclosed, not counted as successful proof evidence.

Each checkpoint froze source and explicitly revoked leaf source ownership before fileowner validation. Full `lake build` then separate `lake build Roth.LeanEval` passed before exact-path staging, commit and successful branch push, followed by the next declaration. Root Roth omits LeanEval, so it is a separate required target. Declaration26's packing correction invalidated its previous source hash; module/full/separate/type/LSP checks were rerun on the corrected frozen source before publication.

Machine inventory `/private/tmp/roth-coeffnorm-final-analysis.json` confirms27 complete individual reports (26 originals plus1 new helper), all42 rule labels each,11 checked steps each and no unchecked item. Actual report contents were inspected at their checkpoints. All local structure/naming/packing/inequality gates pass.

| Declaration / audit | Original lines | Final lines |
|---|---:|---:|
| [normOne](CoeffNorm-normOne.md) | 1 | 1 |
| [normOne_nonneg](CoeffNorm-normOne_nonneg.md) | 2 | 2 |
| [normOne_eq_sum_of_support_subset](CoeffNorm-normOne_eq_sum_of_support_subset.md) | 3 | 3 |
| [normOne_monomial](CoeffNorm-normOne_monomial.md) | 4 | 4 |
| [normOne_zero](CoeffNorm-normOne_zero.md) | 2 | 2 |
| [abs_coeff_le_normOne](CoeffNorm-abs_coeff_le_normOne.md) | 6 | 3 |
| [normOne_add_le](CoeffNorm-normOne_add_le.md) | 7 | 7 |
| [normOne_neg](CoeffNorm-normOne_neg.md) | 2 | 2 |
| [normOne_sum_le](CoeffNorm-normOne_sum_le.md) | 3 | 3 |
| [normOne_mul_le](CoeffNorm-normOne_mul_le.md) | 12 | 7 |
| [normOne_prod_le](CoeffNorm-normOne_prod_le.md) | 8 | 4 |
| [normOne_le_card_mul](CoeffNorm-normOne_le_card_mul.md) | 4 | 3 |
| [normOne_det_le](CoeffNorm-normOne_det_le.md) | 11 | 10 |
| [abs_coeff_hasseDeriv_le](CoeffNorm-abs_coeff_hasseDeriv_le.md) | 12 | 10 |
| [normOne_hasseDeriv_le](CoeffNorm-normOne_hasseDeriv_le.md) | 23 | 10 |
| [diag](CoeffNorm-diag.md) | 1 | 1 |
| [diag_eq_sum](CoeffNorm-diag_eq_sum.md) | 7 | 5 |
| [abs_coeff_diag_le](CoeffNorm-abs_coeff_diag_le.md) | 8 | 6 |
| [natDegree_diag_le](CoeffNorm-natDegree_diag_le.md) | 7 | 7 |
| [eval_diag](CoeffNorm-eval_diag.md) | 4 | 4 |
| [diag_sub](CoeffNorm-diag_sub.md) | 2 | 2 |
| [geom_sum_le_one_add_pow](CoeffNorm-geom_sum_le_one_add_pow.md) | 7 | 7 |
| [sum_box_prod_pow](CoeffNorm-sum_box_prod_pow.md) | 4 | removed |
| [abs_eval_le](CoeffNorm-abs_eval_le.md) | 28 | 17 |
| [degreeOf_det_hasseDeriv_le](CoeffNorm-degreeOf_det_hasseDeriv_le.md) | 14 | 9 |
| [abs_coeff_det_hasseDeriv_le](CoeffNorm-abs_coeff_det_hasseDeriv_le.md) | 20 | 15 |
| [sum_box_prod_pow_le_aux](CoeffNorm-sum_box_prod_pow_le_aux.md) | added | 5 |

Counts exclude documentation and scope commands:202→149 declaration lines (−53);26 declarations retained after removing one original private wrapper and adding one substantial private bound. Source320→268 lines (−52,16.25%). The retained public API has25 constants, including the two original definitions. Main proof bodies: normOne_hasseDeriv_le21→8, abs_eval_le25→14, determinant coefficient bound14→10. The initial light-scan prose overstated abs_eval_le body length; these figures use the actual declaration boundary and final source.

## Phase 5a — non-rename refactoring

Direct Finsupp coefficient bounds, MvPolynomial multiplication/derivative/evaluation expansions and generic finite-product submultiplicativity replace support bookkeeping and redundant induction. The original private Cartesian-sum wrapper was deleted in favor of direct Mathlib calls. The geometric-box inequality is a distinct mathematical bound needed to keep the main value estimate short; its new private helper was subsequently audited and shortened8→4 proof lines; independent final review removed one redundant setup line, yielding3. Its private unused DecidableEq argument was removed with declaration-local Classical scope; the old statement for arbitrary supplied instances was independently recovered by subsingleton transport. Public signatures remain untouched.

[Compiled public-hypothesis proposal](CoeffNorm-api-proposal.md) remains unapplied pending a scoped user decision: four public DecidableEq parameters and normOne_det_le.hC. Earlier Box/Wronskian approvals were scoped and do not authorize this amendment. Other speculative generic-coefficient, point-local, wrapper-deletion and redundant-hB0 restatements were closed under public API preservation without new approval requests. No required private refactor remains.

## Phase 5b — rename pass

| Raw queue | Deduplicated queue | Applied | Conflicts | Caller files changed |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |

All27 reports queue no rename; no rename sidecar exists or was mutated. The global cleanup-all rename pass remains scheduled for project end.

## Phase 6 — cumulative preservation and verification

Complete native diagnostics succeeded for CoeffNorm and all direct caller files: `success=true`, `partial=false`, `timed_out=false`, no failed dependencies and zero errors. First bounded requests were partial; subsequent complete requests are the evidence. CoeffNorm retains six inherited warnings: missing header metadata, four public DecidableEq parameters and hC. Separation/Theta/MainLemma retain32/23/3 preexisting warnings respectively, for their own file audits. Initial final evidence `/private/tmp/roth-coeffnorm-final-lsp.json`; after reviewer fixes, `/private/tmp/roth-coeffnorm-simplify-lsp.json` confirms CoeffNorm complete and `/private/tmp/roth-coeffnorm-simplify-callers-lsp.json` confirms all three callers complete; no future file was edited. Full builds cover the downstream closure.

The entire original module was compiled under `Roth.CoeffNormBaseline` alongside the final module. All25 original public constants compare by rfl, checking exact elaborated types and both definition values; theorem equality uses proof irrelevance. Initial compatibility80821, packed-source compatibility62691 and post-review compatibility76428 all exit0. File `/private/tmp/roth-coeffnorm-final-compatibility.lean`, final log `/private/tmp/roth-coeffnorm-simplify-compatibility.log`. Every printed axiom set contains only propext, Classical.choice and Quot.sound (definitions may use fewer). Private original/new statements and independent reproofs were checked in dedicated audits.

Block comments/docstrings are byte-identical to baseline; narrative proof comments0→0. No source line exceeds100 codepoints. No sorry/admit, new axiom, native_decide, FIXME/TODO, option/limit override, λ, dollar application or push_neg; no profiler scaffolding. `git diff --check` passes. Temporary probes remain outside the repository.

Introduced external identifiers have positive local source/search evidence and a successful compiled11-name batch (session35946 and post-review41147 exit0), `/private/tmp/roth-coeffnorm-final-identifiers.lean` and matching log. Existing APIs moved between proof blocks remain checked by actual module and isolated compilations; local projections are elaborated rather than guessed.

| Identifier | Verification | Result |
|---|---|---|
| `Finsupp.single_eval_le_sum` | positive source/search and compiled #check | pass |
| `MvPolynomial.mul_def` | positive source/search and compiled #check | pass |
| `Finset.le_prod_of_submultiplicative_of_nonneg` | positive source/search and compiled #check | pass |
| `Int.cast_mul` | positive source/search and compiled #check | pass |
| `Int.cast_natCast` | positive source/search and compiled #check | pass |
| `MvPolynomial.aeval_def` | positive source/search and compiled #check | pass |
| `MvPolynomial.eval₂_eq` | positive source/search and compiled #check | pass |
| `MvPolynomial.eval₂_eq'` | positive source/search and compiled #check | pass |
| `MvPolynomial.eval_map` | positive source/search and compiled #check | pass |
| `Finset.mem_range_succ_iff` | positive source/search and compiled #check | pass |
| `MvPolynomial.degreeOf_C_mul_le` | positive source/search and compiled #check | pass |

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | pass | final cached74265, reviewer-fix96881 and post-profile37614 exit0 |
| lake_build | pass | packed-source2725 and reviewer-fix94127 exit0 |
| separate LeanEval | pass | packed-source2725 and reviewer-fix94127 exit0, each sequential after full |
| definition_protected | pass | both original definitions compare by rfl |
| theorem_statement_protected | pass | all25 original public constants compare by rfl; private weakening explicitly audited |
| cumulative_no_unintended_breakage | pass | complete three-caller diagnostics, full and separate builds; no caller edits |
| structure/naming/packing/inequality | pass | all27 dedicated audits and machine source sweep |

Logs `/private/tmp/roth-coeffnorm-final-module.log`, `/private/tmp/roth-coeffnorm-d26-packed-{full,leaneval}.log`, `/private/tmp/roth-coeffnorm-simplify-{module,full,leaneval}.log` and `/private/tmp/roth-coeffnorm-post-profile-module.log`. Overall pass with the explicit preserved metadata/pending-public-hypothesis limitations.

## Phase 6.5 — independent simplify

Outcome: ISSUES-FOUND-AND-FIXED. A fresh independent Sol Medium reviewer examined the entire file and cumulative diff for reuse, quality, efficiency, imports and cross-declaration structure. Built-in /simplify is unavailable, so the required fresh independent fallback supplied the review. [Review](CoeffNorm-simplify.md) documents two compiled findings: redundant polynomial bridge import and helper classical tactic under declaration-local Classical scope. Fileowner applied both, reran complete module/caller diagnostics, original type/value comparisons, identifier batch, module/full/separate builds and protection gates, then published72871a7. The reviewer's report explicitly distinguishes its read-only handoff from fileowner implementation. No outstanding finding, new helper or public API change resulted.

## Phase 6.6 — actual performance sweep

Outcome: FAST-BOARD. Budget1000ms; all26 retained declarations below750ms, so none meets the ±25% borderline re-sweep criterion. No slow declaration diagnosis/fix/propagation, heartbeat optimization probe, deferral or approval-dependent performance change was necessary. No limit raises removed/added (0/0).

Actual command, session70638 exit0:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/CoeffNorm.lean`.

Pinned Lean4.34 trace mode supplies declaration anchors; aggregate profiling alone does not. Parsed every Elab.command and associated asynchronous proof/type-checking/compiler task, excluding separately tagged linter tasks. Nested trace nodes are not summed twice. For the declaration-local Classical wrapper, the larger outer/inner command time is used once, and its private proof is associated through the explicit full-name async anchor. This corrected an initial parser undercount before reporting. Conservative total is command plus associated asynchronous tasks; representative nested tactic timing is separate. All26 current source declarations match anchors. No other build/profile ran concurrently. A premature parse while the trace was still being written failed at an incomplete UTF-8 byte; only the finished exit0 trace was parsed successfully. Raw trace `/private/tmp/roth-coeffnorm-final-profile-trace.log`; parser `/private/tmp/roth-coeffnorm-final-profile-parse.py`; timing table `/private/tmp/roth-coeffnorm-final-profile-table.json`.

| Declaration | Line | Command ms | Proof ms | Conservative total ms | Representative dominant step | Over budget |
|---|---:|---:|---:|---:|---|---|
| `normOne` | 41 | 47.62 | 0.00 | 48.14 | term elaboration | no |
| `normOne_nonneg` | 44 | 5.18 | 16.44 | 22.22 | term elaboration | no |
| `normOne_eq_sum_of_support_subset` | 48 | 17.90 | 31.29 | 51.14 | simp [notMem_support_iff.1 hd] | no |
| `normOne_monomial` | 53 | 8.30 | 47.92 | 59.07 | simp | no |
| `normOne_zero` | 60 | 2.85 | 25.62 | 29.84 | simp [normOne] | no |
| `abs_coeff_le_normOne` | 65 | 3.24 | 35.37 | 39.79 | simp | no |
| `normOne_add_le` | 71 | 4.74 | 101.63 | 111.17 | exact | no |
| `normOne_neg` | 80 | 3.05 | 45.91 | 52.61 | simp [normOne] | no |
| `normOne_sum_le` | 84 | 4.88 | 19.11 | 24.68 | term elaboration | no |
| `normOne_mul_le` | 90 | 6.05 | 129.81 | 143.74 | exact | no |
| `normOne_prod_le` | 99 | 9.04 | 98.67 | 115.76 | simpa using (normOne_monomial (0 : σ →₀ ℕ) 1).le | no |
| `normOne_le_card_mul` | 107 | 11.57 | 50.95 | 63.86 | simpa [normOne] using P.support.sum_le_card_nsmul _ _ (fun d _ ↦ hB d) | no |
| `normOne_det_le` | 113 | 12.56 | 625.43 | 656.95 | rcases Int.units_eq_one_or (Equiv.Perm.sign τ) with h &#124; h <;> | no |
| `abs_coeff_hasseDeriv_le` | 128 | 19.42 | 469.52 | 495.81 | simpa using | no |
| `normOne_hasseDeriv_le` | 142 | 20.41 | 134.59 | 161.78 | exact_mod_cast | no |
| `diag` | 155 | 25.88 | 0.00 | 26.30 | term elaboration | no |
| `diag_eq_sum` | 158 | 15.86 | 99.73 | 137.42 | simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq, | no |
| `abs_coeff_diag_le` | 168 | 16.06 | 410.81 | 442.27 | split_ifs <;> grind [abs_nonneg] | no |
| `natDegree_diag_le` | 177 | 17.03 | 17.00 | 35.33 | exact Finset.sum_le_sum fun j _ ↦ (monomial_le_degreeOf j hk).trans (hP j) | no |
| `eval_diag` | 187 | 16.58 | 527.25 | 564.50 | induction P using MvPolynomial.induction_on <;> simp_all [diag] | no |
| `diag_sub` | 193 | 11.66 | 46.22 | 75.05 | term elaboration | no |
| `geom_sum_le_one_add_pow` | 199 | 13.01 | 61.04 | 75.98 | exact_mod_cast Nat.choose_pos (Finset.mem_range_succ_iff.1 hm) | no |
| `sum_box_prod_pow_le_aux` | 208 | 26.36 | 530.17 | 561.31 | simpa [← Finset.mul_sum, box, Finset.prod_univ_sum] using | no |
| `abs_eval_le` | 217 | 29.36 | 238.07 | 273.38 | calc | no |
| `degreeOf_det_hasseDeriv_le` | 239 | 26.38 | 345.73 | 376.64 | simpa using | no |
| `abs_coeff_det_hasseDeriv_le` | 252 | 50.78 | 283.39 | 345.15 | calc | no |

Maximum656.95ms (`normOne_det_le`); source hash unchanged throughout profiling. Post-profile module37614 exit0 and diff/hygiene gates pass. No benchmark-derived source edit or temporary instrumentation entered the repository.

## Completion and remaining project work

CoeffNorm is complete:26/26 original declarations plus1 added private helper;26 declarations retained. Overall original-project tally101/264. Three nontrivial Mathlib discoveries are recorded in `.mathlib-quality/learnings.jsonl` as required. Missing authoritative header metadata remains user-preserved. The compiled public-hypothesis proposal remains unapplied and awaiting the parent/user's scoped decision; current published API is fully preserved and all six inherited warnings remain explicit. No other CoeffNorm finding or unfinished mandatory gate remains.

Next file GenWronskian requires a fresh file owner; this worker does not start it. The global rename pass and remaining project files are not claimed complete. File/source/shared-progress/Git ownership is released after the final report checkpoint is successfully pushed.

