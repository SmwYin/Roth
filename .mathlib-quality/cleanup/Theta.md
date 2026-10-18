# Theta cleanup: preparation and declaration ledger

Baseline: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`; 981 lines, 35 original declarations
(29 public,6 private). Original contracts and documentation protected; named public API changes
require explicit fresh approval. Scope: all declaration audits, new-helper audits and final phases.
Dialect: classic Lean (no module-system header).

## Phase 0 baseline

- Optional cache get skipped: warm pinned dependency cache already available.
- Owner full `lake build`: exit0, `/private/tmp/roth-theta-baseline-full.log` (2465 jobs).
- Complete unfiltered native LSP: success=true,partial=false,timed_out=false,zero errors,28 warnings; `/private/tmp/roth-theta-baseline-lsp.json`. Separate baseline `lake build Roth.LeanEval`:exit0,`/private/tmp/roth-theta-baseline-leaneval.log` (2464 jobs).
- Optional runLinter not separately available; Lean native linters supply findings.

## Phase 2 file-level punch-list (before edits)

A.1 Header metadata absent; explicitly user-preserved, no invented copyright/license.
A.2 Module docstring present immediately after imports, source references included; preserve.
A.3 Initial project imports preceded Mathlib imports. Phase3 applied alphabetic groups separated
by a blank line; all six original imports retained.
Check redundant imports at final independent review.
A.4 No contentless section header; three nonempty named sections retained.
A.5 981 initial lines; extraction may cross1000, file restructuring would need concrete proposal.
A.6 No resource-limit/debug/linter suppression option in source.
A.7 Many ordinary lambda `=>` arrows require per-declaration normalization; no λ,$,push_neg.
B. Baseline28 warnings confirmed by fresh complete diagnostic; no warnings suppressed.
Five unused-contract warnings exposed by approved Index changes reserved for scoped proposals;
public hypotheses not removed without fresh approval.
C. Long proofs: Θ_unique_le headline29;min_le_sum_max46;index_det_le94;index_le_lem6 89;
lem6M_lt53;Θ_lt headline198.
Exact inventory below records physical body spans; dedicated leaves decide extraction against
≤15 headline/≤30 other targets. Correlated existential conjunctions retain their witnesses.
Check all effective binders, casts, declarations, proof branches and mathlib alternatives separately.
Known profiled linarith failure in index_le_lem6 and slow index_det_le remain unresolved;
ordinary baseline builds passing does not imply any all-file profile pass.

## Original declaration inventory

| # | Declaration | Initial line | Physical body lines | State |
|---|---|---:|---:|---|
| 1 | `RSet` | 49 | 1 | Complete;[audit](Theta-RSet.md) |
| 2 | `indexSet` | 55 | 2 | Complete;[audit](Theta-indexSet.md) |
| 3 | `Θ` | 61 | 0 | Complete;[audit](Theta-Theta.md) |
| 4 | `map_intCast_real_ne_zero` | 63 | 1 | Complete; deleted Mathlib wrapper;[audit](Theta-map_intCast_real_ne_zero.md) |
| 5 | `degreeOf_map_intCast_real` | 67 | 1 | Pending dedicated audit |
| 6 | `one_mem_RSet` | 73 | 3 | Pending dedicated audit |
| 7 | `indexSet_nonempty` | 80 | 1 | Pending dedicated audit |
| 8 | `indexSet_bddAbove` | 86 | 4 | Pending dedicated audit |
| 9 | `index_le_Θ` | 96 | 1 | Pending dedicated audit |
| 10 | `Θ_nonneg` | 103 | 2 | Pending dedicated audit |
| 11 | `Θ_le_card` | 109 | 4 | Pending dedicated audit |
| 12 | `Θ_le_of_forall_index_le` | 118 | 3 | Pending dedicated audit |
| 13 | `Θ_mono` | 128 | 3 | Pending dedicated audit |
| 14 | `indexSet_comp_subset` | 134 | 16 | Pending dedicated audit |
| 15 | `Θ_equiv` | 155 | 4 | Pending dedicated audit |
| 16 | `isPrimitive_linear` | 164 | 9 | Pending dedicated audit |
| 17 | `isPrimitive_pow` | 176 | 3 | Pending dedicated audit |
| 18 | `exists_eq_pow_mul_of_rootMultiplicity` | 187 | 14 | Pending dedicated audit |
| 19 | `pow_rootMultiplicity_le` | 210 | 13 | Pending dedicated audit |
| 20 | `Θ_unique_le` | 230 | 29 | Pending dedicated audit |
| 21 | `lem6M` | 270 | 1 | Pending dedicated audit |
| 22 | `lem6Φ` | 275 | 1 | Pending dedicated audit |
| 23 | `one_le_lem6M` | 279 | 8 | Pending dedicated audit |
| 24 | `floor_sq_div_two_le_sum` | 291 | 11 | Pending dedicated audit |
| 25 | `sq_div_three_lt_floor_sq_div_two` | 307 | 5 | Pending dedicated audit |
| 26 | `min_le_sum_max` | 319 | 46 | Pending dedicated audit |
| 27 | `sum_max_sub_le_index_det` | 371 | 25 | Pending dedicated audit |
| 28 | `index_det_le` | 410 | 94 | Pending dedicated audit |
| 29 | `index_le_lem6` | 521 | 89 | Pending dedicated audit |
| 30 | `Θ_option_le` | 623 | 6 | Pending dedicated audit |
| 31 | `one_lt_of_log_pos` | 640 | 5 | Pending dedicated audit |
| 32 | `lem6M_lt` | 650 | 53 | Pending dedicated audit |
| 33 | `lem7_Φ_bound` | 711 | 22 | Pending dedicated audit |
| 34 | `lem7_numeric` | 741 | 25 | Pending dedicated audit |
| 35 | `Θ_lt` | 774 | 198 | Pending dedicated audit |

## Published checkpoint1 — RSet

Dedicated fresh leaf audit complete; retained two-line definition. Owner Phase3 import grouping
applied. Fresh module,complete unfilteredLSP,original exacttype/value/actualstandardaxioms and
uncontended actual prefixprofile61.649ms(conservative async/lint charge) passed. Frozen sequential full+separateLeanEval exit0.
After successful publication:1/35Theta originals;overall182/264,9/14filescomplete.
No helpers/newpublicAPI;all29publicTheta contracts unchanged. Next:indexSet.

## Published checkpoint2 — indexSet

Dedicated fresh audit complete;one lambda arrow normalized,public exact type/value protected.
Module,complete unfilteredLSP,independent originalvalue/actualstandardaxioms and uncontended
exactsource-prefix profile33.915ms passed. Owner frozen full94.839s then separateLeanEval31.755s
both exit0. After successful publication:2/35Theta originals;overall183/264,9/14filescomplete.
The separate [contract menu](Theta-contract-proposal.md) is unapplied: whole independent candidate
proofs compile,explicit all29 originaltype adapters/actualcandidateaxioms/ASTchecks and exactexternalcall probe also pass.
No candidate preview is counted as a declaration audit. Next:Θ.

## Published checkpoint3 — Θ

Dedicated fresh audit retained original one-line named supremum. Module,complete unfilteredLSP,
independent original type/value rfl,actualstandardaxioms,sevenparameter probes and uncontended
prefix traceprofile6.478ms passed. Frozen owner full4.975s then separateLeanEval2.850s both0.
After successful publication:3/35Theta originals;overall184/264,9/14filescomplete.
No helpers/newAPI. [Scoped contract menu](Theta-contract-proposal.md) now has all29kernel-checked
old-type adapters,actualcandidateaxiom/AST and exactexternalcaller checks,stillUNAPPLIED.
Next:private map_intCast_real_ne_zero.

## Published checkpoint4 — map_intCast_real_ne_zero

Fresh dedicated audit deleted the private wrapper and specialized Mathlib directly at seven uses
across five public proofs. No new declaration or public amendment. Actual module, complete
unfiltered LSP (0 errors/28 preserved warnings), independent original proof/type, five exact actual
consumer-type comparisons after universe alpha-renaming, actual standard axioms and private-suffix
absence checks pass. Original-only trace profile42.625ms; edited early consumer-prefix samples
61.011/52.708ms pass. These samples do not certify the still-pending wholeTheta profile.
Owner sequential full/separateLeanEval gates and exact publication recorded in the dedicated report.
After successful publication:4/35Theta originals;overall185/264,9/14filescomplete.
RSet's original accepted raw trace was re-accounted conservatively at61.649ms including async/lint;
no source or timing sample changed. Contract menu remains UNAPPLIED. Next:degreeOf_map_intCast_real.
