# Theta — completed file cleanup

Baseline 2b64544bf9f77a8ff957bf1bcaf693ac72217ff6; current frozen source SHA256
ff85b7f132cf83c980323449b38558699e7e39d5a1b8bd895ac3374d78310207.
Original 981 → final 991 lines (+10); 35 originals audited (29 public, 6 private).
The 50 current declarations comprise 32 retained originals plus 18 new private helpers.
Three original private Mathlib wrappers were removed. All 22 introduced helper histories
received separate fresh audits; 18 remain and 4 were subsequently removed. Original counts
remain 216/264; final publication completes 10/14 files, with MainLemma next.

## Phases 0–5 and audit coverage

Warm-cache baseline full and separate LeanEval builds passed. Complete baseline native
Theta diagnostics had 0 errors and 28 warnings. Every original received its own fresh declaration
worker and all 24 audit items, 42 golf rules, five actual search methods, effective-binder/generalisation
and public-literature work, signature packing, inequality scan and 11 verification steps.
Each source checkpoint was frozen, independently validated, committed and pushed before
proceeding. Revisit and helper reports preserve actual failed probes and unavailable search
results; no original count is added for revisits or helpers.

The full [declaration ledger](Theta.md), [contract ledger](Theta-contract-proposal.md) and
[fresh independent final review](Theta-final-simplify-final.md) link all 35 original audits,
22 introduced-helper audits and performance repairs. Source references and descriptions remain.
All seven module Main results satisfy their 15-line target; other bodies are at most 30 lines and branches at most 10.

| Main result | Noncomment proof body lines |
|---|---:|
| `Θ_nonneg` | 3 |
| `Θ_le_card` | 5 |
| `Θ_mono` | 3 |
| `Θ_equiv` | 3 |
| `Θ_unique_le` | 3 |
| `Θ_option_le` | 5 |
| `Θ_lt` | 15 |

Three named sections retained; file length 991 < 1,000. Width is at most 100 codepoints. The independent
review records 183 signature-packing rows and 11 proof comments with every removed/reanchored comment
accounted for, 176 new lexical identifiers classified, and 97 external positive #checks (exit 0, no warnings).
The removed antitone comment restated the immediately following typed assertion; a small-index
comment explains the new case. Imports were checked against actual identifier use. No
unsupported new import, unverified identifier, resource-limit raise or diagnostic suppression.

## Contracts and cumulative semantics

Public definitions RSet,indexSet,Θ,lem6M,lem6Φ retain their exact original values/types.
Every public statement amendment has a dedicated supported/authorized ledger entry and exact
full original-type adapter. Actual telescope metadata, opaque bodies and standard axioms are
checked separately from historical compatibility contexts. Strict conclusions/domains remain;
supported redundant hypotheses and numerical premises were removed or weakened. The user’s
explicit retained global Θ hB/hr, index_le_lem6/Θ_option_le hq, header metadata, wrappers and
previously declined domains remain protected.

Both technical hr findings from the first filewide review were separately audited, validated
and published: index_le_Θ at 34102b2/73e2604 and Θ_unique_le at 367508c/164e33b. The second fresh
filewide review returns PASS-THROUGH with no further recommendation. Original documentation
and the historical first review remain preserved. All 25 final-review artifacts, 17 source pins,
3 configuration pins, 23 combined FIRST paths plus 9 older supplements rehash exactly. Four complete
original Index/Theta/originalMainLemma/preceding-currentMainLemma source blocks rehash exactly.
Inverse migrations recover every byte of the 692,893/806,170-byte preceding scaffolds; historical markers are
explicitly labelled. No unproved whole-prefix identity claim is used.

Whole original and updated MainLemma proofs retain the entire 26-binder caller contract.
External Theta uses are RSet,Θ_lt,index_le_Θ in MainLemma; Main/LeanEval/root remain downstream
consumers. The necessary MainLemma edits are routine argument/certificate repairs; Main source
is unchanged. The full 1,223-check cumulative replay includes all 29 original public contracts,
five definition values, independent actual type/body/standard-axiom checks and whole old/current
caller proofs; fresh final owner replay passed all 1,223 marker categories in 354.517 s.

## Final owner gates

All final commands ran sequentially against the exact frozen source and all 17 source/configuration pins.

| Gate | Actual command / result |
|---|---|
| Original/public/caller semantics | `lake env lean /private/tmp/theta-unique-technical-hr/ActualSemanticsAugmented.lean`:exit0,354.517s,1223positive checks; no PANIC, error or sorryAx |
| Actual retained opaque bodies/types/axioms | `lake env lean /private/tmp/ThetaFinalOwnerAllActual.lean`:exit0,30.338s,50 bodies and 50 standard-axiom sets |
| Complete unfiltered diagnostics | Native requests for Theta/MainLemma/Main/LeanEval/root:success=true,partial=false,timed_out=false,failed_dependencies=[]; errors0; warnings6/3/4/0/0 |
| Affected module build | `lake build Roth.Theta Roth.MainLemma`:exit0,4.802s |
| Full project build | `lake build`:exit0,6.695s |
| Separate LeanEval | `lake build Roth.LeanEval`:exit0,3.353s,started only after full build completed |
| definition_protected | All 5 original definition types/values independently compared and unchanged |
| theorem_statement_protected | Every accepted change traced through dedicated report/authorization and exact old-contract adapter |
| cumulative_no_unintended_breakage | Complete affected/downstream diagnostics,all 29 original contracts and entire old/current caller proofs pass |

Actual standard axioms are limited to propext/Classical.choice/Quot.sound. No new axiom,
sorry,native_decide,resource-limit raise,warning suppression or debug/profile scaffolding
is added to source. Final commands/process groups are drained and no native request remains.

The six Theta warnings are user-preserved header metadata and the protected Θ_nonneg.hB/hr,
Θ_le_card.hB,Θ_mono.hr,index_le_lem6.hq. MainLemma's header,hδ0/hr₁ and Main's header,hδ/hQ/hc
are existing next-file findings, not hidden or waived by this Theta cleanup. LeanEval/root have
no warnings. Raw unfiltered messages are in `/private/tmp/theta-final-owner/native-*.json`.
All normal raw logs use strict UTF8 and were fully inspected for errors/PANIC/sorryAx; module/full/Eval
logs retain imported-module metadata and unused-instance warning context.


## Performance and historical evidence

All failed threshold traces and raw logs remain preserved. Dedicated performance revisions
repair index_le_lem6/index_det_le/separated/numeric/summax/phi/numeric/prefix/mapped proofs.
A lower repeat never erases a failed sample. In particular summax 1004.335 and 1131.027/1065.136
remain historical failures preceding p10’s 900.517/748.233, and mapped 1049.976 remains preceding
p11’s 837.283/861.675. Prior scoped captures do not substitute for the final owner sweep.
Final owner actual whole-file profile: first capture and one required repeat on identical final source; every sample is below 1,000 ms.

Actual command for each capture: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`; exit 0, no external timeout, all 17 pins immutable and own process/group drained.

| Declaration | First ms | Repeat ms |
|---|---:|---:|
| `RSet` | 127.141 | 85.788 |
| `indexSet` | 55.009 | 37.312 |
| `Θ` | 8.440 | 10.465 |
| `one_mem_RSet` | 442.518 | 381.626 |
| `indexSet_nonempty` | 43.065 | 26.927 |
| `indexSet_bddAbove` | 308.659 | 291.027 |
| `index_le_Θ` | 37.763 | 36.104 |
| `Θ_nonneg` | 32.512 | 23.145 |
| `Θ_le_card` | 271.763 | 317.348 |
| `Θ_le_of_forall_index_le` | 43.380 | 49.225 |
| `Θ_mono` | 41.732 | 37.188 |
| `indexSet_comp_subset` | 269.692 | 275.789 |
| `Θ_equiv` | 79.697 | 64.980 |
| `isPrimitive_linear` | 314.167 | 240.803 |
| `isPrimitive_pow` | 58.498 | 60.660 |
| `exists_eq_pow_mul_of_rootMultiplicity` | 537.107 | 533.921 |
| `pow_rootMultiplicity_le` | 459.741 | 471.098 |
| `index_unique_le_log_div` | 660.093 | 764.736 |
| `Θ_unique_le` | 64.175 | 76.161 |
| `lem6M` | 46.627 | 33.292 |
| `lem6Φ` | 13.991 | 13.375 |
| `one_le_lem6M` | 165.830 | 172.571 |
| `floor_sq_div_two_le_sum` | 558.264 | 582.482 |
| `sq_div_three_lt_floor_sq_div_two` | 541.071 | 572.671 |
| `mul_div_two_le_sum_max_aux` | 547.276 | 567.380 |
| `mul_sq_div_three_le_sum_max_of_pos_aux` | 588.694 | 658.614 |
| `mul_sq_div_three_le_sum_max_aux` | 418.266 | 449.406 |
| `min_le_sum_max` | 178.633 | 197.346 |
| `sum_max_sub_le_index_det` | 698.746 | 805.424 |
| `index_separated_mul_le_aux` | 657.717 | 735.960 |
| `index_det_le` | 718.317 | 870.082 |
| `weight_le_delta_aux` | 395.614 | 466.307 |
| `mapped_det_ne_zero_aux` | 778.325 | 907.046 |
| `index_numeric_bound_aux` | 594.187 | 638.257 |
| `index_le_lem6` | 573.004 | 617.219 |
| `Θ_option_le` | 186.351 | 172.637 |
| `factorial_coefficient_le_two_pow_aux` | 217.804 | 297.323 |
| `two_pow_lt_rpow_aux` | 511.405 | 582.536 |
| `lem6M_lt` | 572.026 | 672.281 |
| `lem7_Φ_bound` | 652.621 | 739.678 |
| `lem7_numeric` | 684.075 | 736.036 |
| `theta_scaled_unique_le_aux` | 582.090 | 633.855 |
| `theta_delta_succ_lt_aux` | 685.847 | 703.845 |
| `theta_prefix_lt_aux` | 656.545 | 744.509 |
| `theta_lt_base_aux` | 503.856 | 529.938 |
| `theta_denominators_one_lt_aux` | 102.474 | 106.938 |
| `theta_phi_lt_aux` | 571.950 | 677.839 |
| `theta_lt_succ_aux` | 557.306 | 680.291 |
| `theta_lt_of_large_delta_aux` | 515.119 | 611.354 |
| `Θ_lt` | 341.366 | 365.409 |

Maxima: 778.325ms, 907.046ms. No third capture or discarded failed capture.

The threshold is 1,000 ms; a measurement at least 750 ms requires a repeat. Conservative totals use disjoint enclosing
command+async proof/addDecl/linter/compiler rows; nested kernel/macro rows are not double-counted.
Raw logs remain strict UTF8 with exact source hashes/byte slices; limits unchanged.

MainLemma main_lemma actual timing remains unavailable after the earlier bounded 60 s cutoff
before target (5/27). It is the next file’s performance task; no whole-project performance pass.

## Remaining preferences and release

User-preserved metadata warnings remain. The authorized index_hasseDeriv_ge rename is queued
for the project-end global pass by the coordinator. Earlier optional domain/wrapper enhancements
remain unapplied per recorded decisions; no pending Theta recommendation requires user input.
Final verification is complete. Final audit publication and actual commit hash are recorded in central cleanup-progress.md; ownership releases only after successful push and clean HEAD=origin verification.

## Exact final artifact records

- `/private/tmp/theta-final-owner/semantics-checked.json`:SHA256`2001712b70dd8147f84e0d4d63a6336894a5c44650695aa917efef0015ee6547`.
- `/private/tmp/theta-final-owner/allactual-checked.json`:SHA256`5d6d9948761aa504577da9ba8cdbeab65eab8e156daac0c2e25e813e03c1b7a1`.
- `/private/tmp/theta-final-owner/native-checked.json`:SHA256`5c787831c862cf4d18e4a0fb08b6bddb1bfea3bc54fcbf0041fd02af36b774d7`.
- `/private/tmp/theta-final-owner/affected-modules-checked.json`:SHA256`43e3c1f332a2e2c2af1be75b5e54d5e00115a39f4580ab922966a4d1ae6c4d8b`.
- `/private/tmp/theta-final-owner/profile-first-checked.json`:SHA256`34771b03ba97a9ce3c91a4a7d86d8c15f5d897c5d4e6a100549c203d54139e63`.
- `/private/tmp/roth-theta-final-builds.json`:SHA256`5439493c36d7f669222a3d2b89262ab8fda2df3de3ec4451797d77cba1462c74`.
- `/private/tmp/theta-final-review-after-hr/owner-final-review-checked.json`:SHA256`dc91ba9223d9730a010e93c232a8b768e89f1c33eb49c11b4c4d2193ddffcd45`.
- `/private/tmp/theta-final-owner/profile-repeat-checked.json`:SHA256`3a76560b78669452a72d4919307267ef3ac5498a3cb59c2d93459b3817873564`.
