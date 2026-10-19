# Theta cleanup: preparation and declaration ledger

Baseline: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`; 981 lines, 35 original declarations
(29 public,6 private). Original contracts are recovered independently and documentation is preserved.
The user's standing authorization permits well-supported recommended API cleanup with compiled
evidence and all validation gates; prior explicit preservation choices remain in force.
Scope: all declaration audits, new-helper audits and final phases.
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
| 5 | `degreeOf_map_intCast_real` | 67 | 1 | Complete; deleted Mathlib wrapper;[audit](Theta-degreeOf_map_intCast_real.md) |
| 6 | `one_mem_RSet` | 73 | 3 | Complete;[audit](Theta-one_mem_RSet.md) |
| 7 | `indexSet_nonempty` | 80 | 1 | Complete;[audit](Theta-indexSet_nonempty.md) |
| 8 | `indexSet_bddAbove` | 86 | 4 | Complete;[audit](Theta-indexSet_bddAbove.md) |
| 9 | `index_le_Θ` | 96 | 1 | Complete;[audit](Theta-index_le_Theta.md) |
| 10 | `Θ_nonneg` | 103 | 2 | Complete;[audit](Theta-Theta_nonneg.md) |
| 11 | `Θ_le_card` | 109 | 4 | Complete;[audit](Theta-Theta_le_card.md) |
| 12 | `Θ_le_of_forall_index_le` | 118 | 3 | Complete;[audit](Theta-Theta_le_of_forall_index_le.md) |
| 13 | `Θ_mono` | 128 | 3 | Complete;[audit](Theta-Theta_mono.md) |
| 14 | `indexSet_comp_subset` | 134 | 16 | Complete;[audit](Theta-indexSet_comp_subset.md) |
| 15 | `Θ_equiv` | 155 | 4 | Complete;[audit](Theta-Theta_equiv.md) |
| 16 | `isPrimitive_linear` | 164 | 9 | Complete;[audit](Theta-isPrimitive_linear.md) |
| 17 | `isPrimitive_pow` | 176 | 3 | Complete;[audit](Theta-isPrimitive_pow.md) |
| 18 | `exists_eq_pow_mul_of_rootMultiplicity` | 187 | 14 | Complete;[audit](Theta-exists_eq_pow_mul_of_rootMultiplicity.md) |
| 19 | `pow_rootMultiplicity_le` | 210 | 13 | Complete;[audit](Theta-pow_rootMultiplicity_le.md) |
| 20 | `Θ_unique_le` | 230 | 29 | Complete;[audit](Theta-Theta_unique_le.md) |
| 21 | `lem6M` | 270 | 1 | Complete;[audit](Theta-lem6M.md) |
| 22 | `lem6Φ` | 275 | 1 | Complete;[audit](Theta-lem6Phi.md) |
| 23 | `one_le_lem6M` | 279 | 8 | Complete;[audit](Theta-one_le_lem6M.md) |
| 24 | `floor_sq_div_two_le_sum` | 291 | 11 | Complete;[audit](Theta-floor_sq_div_two_le_sum.md) |
| 25 | `sq_div_three_lt_floor_sq_div_two` | 307 | 5 | Complete;[audit](Theta-sq_div_three_lt_floor_sq_div_two.md) |
| 26 | `min_le_sum_max` | 319 | 46 | Complete;[audit](Theta-min_le_sum_max.md) |
| 27 | `sum_max_sub_le_index_det` | 371 | 25 | Complete;[audit](Theta-sum_max_sub_le_index_det.md) |
| 28 | `index_det_le` | 410 | 94 | Complete;[audit](Theta-index_det_le.md) |
| 29 | `index_le_lem6` | 521 | 89 | Complete;[audit](Theta-index_le_lem6.md) |
| 30 | `Θ_option_le` | 623 | 6 | Complete;[audit](Theta-Theta_option_le.md) |
| 31 | `one_lt_of_log_pos` | 640 | 5 | Complete;[audit](Theta-one_lt_of_log_pos.md) |
| 32 | `lem6M_lt` | 650 | 53 | Complete;[audit](Theta-lem6M_lt.md) |
| 33 | `lem7_Φ_bound` | 711 | 22 | Complete;[audit](Theta-lem7_Phi_bound.md) |
| 34 | `lem7_numeric` | 741 | 25 | Complete;[audit](Theta-lem7_numeric.md) |
| 35 | `Θ_lt` | 774 | 198 | Complete;[audit](Theta-Theta_lt.md) |

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

## Published checkpoint5 — degreeOf_map_intCast_real

Fresh dedicated audit deleted the private degree wrapper and rewrote both coordinate-bound
families directly using Mathlib degreeOf_def/degrees_map_of_injective. No helper/public amendment.
Module, complete unfiltered LSP0errors/27warnings, independent original proof/value/type and binder
probes, independent original caller proofs, direct actual caller-type comparisons, actual standard
axioms and deleted private-suffix scan pass. One unused-section-instance warning disappears because
the new proof consumes the retained DecidableEq; no argument was removed or warning suppressed.
Uncontended exact-prefix traces: original31.035ms; edited callers188.193/178.634ms (<750ms).
The deliberate direct specialization is slower than the wrapper applications but comfortably
within budget; no whole-file performance success inferred. Owner sequential full/separateLeanEval
and publication are recorded in the dedicated report. After successful publication:Theta5/35,
overall186/264,9/14files complete. Contract menu remains UNAPPLIED. Next:one_mem_RSet.

## Published checkpoint6 — one_mem_RSet

Fresh dedicated audit simplified the original3-line proof to one terminal simp. Every public
parameter/instance and all docs/callers retained; no helper. Full24/42/five actual searches,
compiled parameter tests and threshold/counterexample/literature/inversion checks complete.
Module51.177s, complete unfiltered native LSP0errors/27preservedwarnings, independent original
proof, direct actual constant-type equality modulo universe renaming and actual standard axioms
pass. Exact-prefix actual trace211.489→173.030ms including async/lint charge; no whole-file
profile claim. Owner sequential full/separateLeanEval and publication recorded in dedicated
report. After successful publication:Theta6/35,overall187/264,9/14files complete.
No public contract proposal applied. Next:indexSet_nonempty.

## Published checkpoint7 — indexSet_nonempty

Fresh full dedicated audit retained the shared existential witness and changed only two lambda
arrows. Original public type/instances/docs/callers unchanged; no helper. Every parameter probed,
including compiled zero-bound emptiness counterexample and unapplied DecidableEq candidate.
Module41.172s, independent original nonself proof/direct actual-type check/standard axioms24.008s,
complete unfiltered native LSP0errors/27identicalwarnings and uncontended exact-prefix actual
trace14.238→13.303ms pass. No speedup claim for syntax-only change or whole-file profile claim.
Owner sequential full/separateLeanEval/publication recorded in dedicated report. After successful
publication:Theta7/35,overall188/264,9/14files complete. Contract menu still UNAPPLIED.
Next:indexSet_bddAbove.

## Published checkpoint8 — indexSet_bddAbove

Fresh full dedicated audit compacted direct degreeOf specialization: live-start6→5body lines
(initial-original4→final5 after the earlier wrapper replacements). All public binders/docs/callers
retained; no helper. All24/42/five searches/effective-binder/literature/inversion/width/inequality
and11leaf gates complete. Module, independent copied original nonself proof, direct actual old-type
comparison and built/original standard axioms pass. Complete unfiltered native LSP0errors/28warnings:
exactly one target unused-section-DecEq warning restored by the proof, no suppression/removal.
Uncontended exact-prefix trace148.516→160.621ms (<750ms); no speedup or whole-file profile claim.
Owner frozen sequential full/separateLeanEval/publication recorded in dedicated report. After
successful publication:Theta8/35,overall189/264,9/14files complete. Menu remains UNAPPLIED.
Next:index_le_Θ.

## Published checkpoint9 — index_le_Θ

Fresh full dedicated audit retained the one-line domain corollary of le_csSup and normalized
only a lambda arrow in its conclusion. All effective public parameters/types/docs/proof retained;
no helper. All24/42/five actual searches/every-binder probes/literature/inversion/packing/inequality
and11gates complete. Module, independent original nonself proof/direct actual-type comparison,
original+actual standard axioms and fresh complete native LSP0errors/28identicalwarnings pass.
Sequential uncontended actual exact-prefix traces24.066→26.208ms; ordinary noise, no speedup or
whole-file profile claim. Owner frozen full/separateLeanEval/publication recorded in dedicated
report. After successful publication:Theta9/35,overall190/264,9/14files complete.
No contract menu amendment applied. Next:Θ_nonneg.

## Published checkpoint10 — Θ_nonneg

Fresh full dedicated audit replaced witness-specific transitivity with canonical Real.sSup_nonneg
and direct nonnegativity of every index (body2→3clear lines). All original public binders/types/
docs/callers preserved; no helper. Full24/42/five searches/every-binder/literature/inversion/width/
inequality/11leaf gates complete. Module, independent original proof/direct actual exact type,
actual standard axioms and fresh complete unfiltered LSP0errors/31warnings pass. Three protected
unused warnings newly exposed: hB,hr,DecEq section instance; none removed/suppressed.
Real exact-prefix aggregate14.181→13.669ms (corrected baseline includes async/kernel/linter);
no speedup or whole-file claim. Owner frozen full/separateLeanEval/publication recorded in audit.
After successful publication:Theta10/35,overall191/264,9/14files complete.
New [proposalD](Theta-contract-proposal.md) independently proves no-hB/no-hr/no-DecEq target,
with ACTUAL imported definitions, full original lambda adapter/kernel equality/direct type+
binderInfo/order/AST/standardaxioms/four internalcaller trials; still UNAPPLIED awaiting decision.
Next:Θ_le_card.

## Published checkpoint11 — Θ_le_card

Fresh full dedicated audit uses canonical Real.sSup_le and direct degreeOf unfolding. Live-start
body6→5 (initial-original4→final5 after prior wrapper replacements). All original public binders/
type/docs retained; no callers/helper. Full24/42/five searches/eightbinder probes/literature/
inversion/width/inequality/11leaf gates complete. Module, independent original proof, actual
old-type/BinderInfo and original+actual standard axioms pass. Fresh complete unfiltered native
LSP0errors/33warnings: new protected hB-unused and DecEq-section-unused; none suppressed.
Uncontended actual exact-prefix153.288→155.638ms (<750/1000), ordinary noise, no speedup/filewide
claim. Owner frozen full/separateLeanEval/publication recorded in dedicated audit. After
publication:Theta11/35,overall192/264,9/14files complete. New [proposalE](Theta-contract-proposal.md)
removes this target's hB alongside prior proposedhr/DecEq, actual-import original lambda adapter/
BinderInfo/AST/standardaxioms/inference trials verified, ZERO actual callers. Still UNAPPLIED.
Next:Θ_le_of_forall_index_le.

## Published checkpoint12 — Θ_le_of_forall_index_le

Fresh full dedicated audit normalized one lambda arrow and packed the short conclusion;
body3→3, declaration7→6. All nine original actual binders/types/docs preserved. Full24/42/
five searches/every-binder/literature/inversion/packing/inequality/11gates complete. The hB
requirement is certified: B0 gives empty indexSet and Θ0=0, so universal c−1 bound is vacuous
while conclusion fails; dropping hc also has a compiled counterexample. Nonempty-set criterion
is only an optional generic csSup_le restatement, retained current parameter API recommended.
Module, independent original proof/direct actual old-type+BinderInfo/standard axioms and fresh
complete native LSP0errors/33unchangedwarnings pass. Uncontended exact-prefix26.433→27.993ms,
no speedup/filewideclaim. Owner frozen full/separateLeanEval/publication recorded in audit.
After publication:Theta12/35,overall193/264,9/14files complete. AllA/B/C/D/E menus UNAPPLIED.
Next:Θ_mono.


## Published checkpoint13 — Θ_mono

Fresh full dedicated audit unpacks RSet's three properties in the witness pattern, normalizes
one lambda and packs hr; body3unchanged, original public telescope/type/docs retained, no callers
or helpers changed. Full24/42/five actual searches/every-binder/literature/inversion/packing/
inequality/11gates complete. Module, independent original/direct actual type+universe+BinderInfo,
actual standard axioms and fresh complete unfiltered LSP0errors33unchangedwarnings pass.
Uncontended exact-prefix23.483→23.606ms, no speedup/filewideclaim. Frozen owner full58.864s THEN
separateLeanEval21.222s both0, identical finalSHA. [ProposalF](Theta-contract-proposal.md) adds
fully verified actual-import no-hB/no-hr monotonicity alongside this target's prior proposedDecEq;
explicit original λadapter/kernel/BinderInfo/AST/standardaxioms and full independent actual Θ_lt
caller reproof with exactly two prospective substitutions pass. Still UNAPPLIED pending decision.
After publication:Theta13/35,overall194/264,9/14files complete. AllA–F menus remain UNAPPLIED.
Next:private indexSet_comp_subset.


## Published checkpoint 14 — private indexSet_comp_subset

Fresh dedicated audit replaces manual nonzero transport, inverse exponent reindexing and final
function congruence with existing mathlib APIs. Proof body: 16 → 12 lines; declaration: 18 → 14,
plus one local omit command; file: 977 → 974. Both private decidability instances are removed.
All public source and comments remain byte-identical; actual Θ_equiv retains all ten original
binders, with exact type/universe/BinderInfo verified. No helper is added. Full 24-item audit,
42 golf rules, five actual searches, ten binder probes, private literature exemption, inversion,
packing, inequality scan and 11-step checklist are complete. Module and complete unfiltered native
LSP pass with 0 errors and 32 warnings (one obsolete private warning removed). Independent original
proof, explicit old ten-binder adapter to actual new eight-binder private constant, direct public
caller contract and actual standard axioms pass. Uncontended prefix profiles: 178.731 → 181.401 ms;
no speedup or whole-file claim. Frozen owner full build (60.885 s), then separate LeanEval (22.704 s),
both pass with identical SHA. After publication: Theta 14/35, overall 195/264, 9/14 files complete.
All public menus A–F remain unapplied. Next: Θ_equiv.


## Published checkpoint 15 — Θ_equiv and approved instance removals

Fresh dedicated audit applies `congrArg sSup` directly (proof 4 → 3 lines) and the user's newly
approved A row: remove both DecEq instances, with a scoped omit before the preserved docstring.
All other parameters, definitions, conclusions and caller source remain intact. No helper added.
Full 24/42/five actual searches/every-binder/literature/inversion/packing/inequality/11 gates pass.
Immutable independent original proof and explicit full-old-ten-binder adapter recover the original
contract from actual new eight-binder theorem; exact retained types/order/BinderInfo/user names,
AST absence and actual standard axioms pass. Anonymous synthetic instance renumbering is documented,
with no artificial production names. Sole theorem caller Θ_lt retains its immutable original
contract. Module and complete unfiltered LSP pass (0 errors, 30 warnings). Accepted post-LSP
uncontended exact-prefix aggregate: 44.400 → 37.638 ms. No whole-file performance claim.
Frozen owner full build (45.642 s), then separate LeanEval (14.442 s), both pass on identical SHA.
After publication: Theta 15/35, overall 196/264, 9/14 files. The exact user decision is recorded
in [the contract menu](Theta-contract-proposal.md): A/B plus first five C rows approved; hq and
D/E/F's extra hB/hr widenings declined. Next: fresh approved revisit of one_mem_RSet, then completed
targets 7–13 in source/dependency order, with no original-count inflation; original 16 follows.


## Approved revisit of original 6 — one_mem_RSet

Applied exactly approved A+B: scoped omission of Fintype σ and DecidableEq σ before the preserved docstring, with proof-local classical decidability. The simp proof remains; body 1 → 2 lines and source +2 lines. No helper, caller edit, definition or other public change. The actual theorem has four binders; its full old six-binder form is recovered by the explicit adapter.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. The sole caller, indexSet_nonempty, has an independent original proof and exact old type/BinderInfo recovery; no caller edit. Its now-unused DecEq is preserved until its separate approved revisit. Module and complete unfiltered final LSP pass with
0 errors and 28 warnings. Accepted uncontended exact-prefix aggregate:
195.926 → 185.150 ms; no whole-file performance claim.
Frozen owner full build (45.375 s), then separate LeanEval (15.075 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-one_mem_RSet-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 7, indexSet_nonempty (DecidableEq σ only).


## Historical CI notification clarified

The coordinator relayed root's verification of [run 39123476667](https://github.com/SmwYin/Roth/actions/runs/39123476667)
at commit 692d63c: its Lean action passed; Pages deployment returned HTTP 400 while deployment
for a4d22a3 overlapped. Newer 132df63 and following workflows completed successfully. This was
not a Lean regression; no workflow change is required or applied. This CI note is independent
of the local checkpoint gates documented above.


## Approved revisit of original 7 — indexSet_nonempty

Applied only a scoped omission of DecidableEq σ before the byte-preserved docstring. Fintype σ, B, hB, q and r, the original proof, all definitions and callers are unchanged. The actual theorem has six retained binders; an explicit full old seven-binder adapter recovers its immutable original contract.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. Both actual callers have independent original proofs and exact original type/BinderInfo/standard-axiom checks. The newly unused DecEq in Θ_le_of_forall_index_le remains until its own approved revisit. Module and complete unfiltered final LSP pass with
0 errors and 27 warnings. Accepted uncontended exact-prefix aggregate:
15.137 → 14.645 ms; no whole-file performance claim.
Frozen owner full build (53.182 s), then separate LeanEval (12.704 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-indexSet_nonempty-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 8, indexSet_bddAbove (DecidableEq σ and hr only, plus necessary caller proof fixes).


## Approved revisit of original 8 — indexSet_bddAbove

Applied approved A+C: scoped omission of DecidableEq σ and removal of hr, retaining Fintype σ, B, q and implicit r. The proof uses local classical decidability. Exactly two obsolete helper hr arguments are removed inside index_le_Θ and Θ_mono proofs; both callers retain ALL original public hypotheses, including hr and their not-yet-revisited DecEq. The actual target has five binders; its full old seven-binder form is recovered by an explicit adapter. No new helper, definition, domain or conclusion change.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. Both actual callers have independent immutable original proofs and exact actual old public type/order/BinderInfo/standard-axiom recovery. Their accepted final aggregates are 32.608 ms and 23.794 ms (baseline 26.474/24.818 ms), extracted with the target from the same two shared exact-prefix logs. Newly unused caller assumptions remain protected. Module and complete unfiltered final LSP pass with
0 errors and 28 warnings. Accepted uncontended exact-prefix aggregate:
165.828 → 215.404 ms; no whole-file performance claim.
Frozen owner full build (80.493 s), then separate LeanEval (22.939 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-indexSet_bddAbove-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 9, index_le_Θ (DecidableEq σ only; hr retained).


## Approved revisit of original 9 — index_le_Θ

Applied exactly one scoped omit before the preserved docstring. Fintype σ, positivity hr and every ordinary argument remain; the existing le_csSup proof and all caller source are unchanged. The full immutable original contract is recovered by an explicit adapter to the actual new theorem, with only its approved class argument removed. No helper, definition, domain or conclusion change.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. The internal index_det_le caller retains its complete immutable original public type, including its not-yet-revisited DecEq, with actual standard axioms. External main_lemma actual original type/names/order/BinderInfo/axioms are separately owner-verified after the full rebuild; its visible hr0 argument remains. Module and complete unfiltered final LSP pass with
0 errors and 27 warnings. Accepted uncontended exact-prefix aggregate:
25.452 → 26.385 ms; no whole-file performance claim.
Frozen owner full build (57.757 s), then separate LeanEval (12.932 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-index_le_Theta-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 10, Θ_nonneg (DecidableEq σ only; hB and hr retained).


## Approved revisit of original 10 — Θ_nonneg

Applied exactly one scoped omit before the preserved docstring. The canonical three-line proof and all four actual caller expressions are unchanged. The user-retained hB/hr assumptions and Fintype remain; the stronger D proposal is not applied. Immutable old proof and explicit full old adapter recover the original type from the actual DecEq-only amended theorem, including retained names/order/BinderInfo and selected-drop AST. No helper, definition, domain or conclusion change.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. All four actual calls in index_le_lem6 and Θ_lt remain unchanged and module-checked. Both actual lem6Φ caller shapes independently compile with standard axioms; no claim is made here to independently reprove either complete long caller. Module and complete unfiltered final LSP pass with
0 errors and 25 warnings. Accepted uncontended exact-prefix aggregate:
15.233 → 14.808 ms; no whole-file performance claim.
Frozen owner full build (54.394 s), then separate LeanEval (17.121 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-Theta_nonneg-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 11, Θ_le_card (DecidableEq σ and hr only; hB retained).


## Approved revisit of original 11 — Θ_le_card

Applied approved A+C: scoped omit for DecidableEq σ, hr deletion and signature packing to one 95-codepoint line. The five-line canonical proof and complete docstring are unchanged. The user-retained hB assumption and Fintype σ remain; the extra E bound widening is not applied. The full immutable original eight-binder type is recovered by an explicit adapter to the actual six-binder theorem, with precise selected AST and retained metadata. No helper, definition, domain or conclusion change.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. Fresh project-wide Lean inventory finds no actual caller, only the declaration and module documentation. Named/inferred compatibility examples are not represented as existing calls. Module and complete unfiltered final LSP pass with
0 errors and 22 warnings. Accepted uncontended exact-prefix aggregate:
147.521 → 148.013 ms; no whole-file performance claim.
Frozen owner full build (65.268 s), then separate LeanEval (23.107 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-Theta_le_card-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 12, Θ_le_of_forall_index_le (DecidableEq σ only).


## Approved revisit of original 12 — Θ_le_of_forall_index_le

Applied approved A only: one scoped omit for DecidableEq σ before the preserved docstring. The canonical three-line proof is unchanged. The immutable original nine-binder type is recovered by an explicit adapter to the actual eight-binder theorem, with precise selected AST and retained metadata. No helper, definition, domain or conclusion change.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. Both unchanged actual internal callers compile in the module gate; a separate no-DecEq call example also passes. No external caller or caller edit. Module and complete unfiltered final LSP pass with
0 errors and 21 warnings. Accepted uncontended exact-prefix aggregate:
27.675 → 28.845 ms; no whole-file performance claim.
Frozen owner full build (102.795 s), then separate LeanEval (31.734 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-Theta_le_of_forall_index_le-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: approved revisit of original 13, Θ_mono (DecidableEq σ only; hB/hr retained).


## Approved revisit of original 13 — Θ_mono

Applied approved A only: one scoped omit before the byte-preserved docstring. The canonical three-line proof, hB/hr hypotheses, Fintype σ and both Θ_lt callers are unchanged; the user-declined extra F widening remains unapplied. The immutable original ten-binder contract is recovered by an explicit adapter to the actual nine-binder theorem, with exact retained metadata and selected-drop AST. No helper, definition, domain or conclusion change.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. Both unchanged actual Θ_lt callers are module checked; actual caller axioms and a separate no-DecEq call example pass. No external direct caller or caller edit. Module and complete unfiltered final LSP pass with
0 errors and 19 warnings. Accepted uncontended exact-prefix aggregate:
25.133 → 23.713 ms; no whole-file performance claim.
Frozen owner full build (68.560 s), then separate LeanEval (31.179 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-Theta_mono-approved.md).
Original counts unchanged: Theta 15/35, overall 196/264, 9/14 files. Next: original 16, private isPrimitive_linear.


## Published checkpoint16 — isPrimitive_linear

Shortened the private coefficient-divisibility argument from nine proof lines to five by inlining the two once-used coefficient facts and removing a definitional rewrite. Its statement, sole public caller, documentation and all definitions remain unchanged.

Fresh full24/42 audit, five actual searches and every-binder probes pass. Immutable independent original proofs, the actual private constant exact type/binder metadata/standard axioms and the sole caller’s complete original hR contract are verified. Module and complete unfiltered final LSP pass with0errors/19warnings.
Accepted uncontended exact-prefix profile: 96.215 → 164.688 ms; no whole-file performance claim.
Frozen owner full (62.585 s) then separate LeanEval (23.065 s) pass.
[Dedicated audit](Theta-isPrimitive_linear.md). Theta 16/35, overall 197/264 originals;9/14 files complete.
No new production helper. Next: original 17, private isPrimitive_pow.


## Published checkpoint17 — isPrimitive_pow

Replaced the private three-line induction with a one-line Nat.rec term using the same primitive-one and primitive-product lemmas. The private type and sole public caller, including its approved but not-yet-removed hR, remain unchanged. No definition, documentation or helper change.

Fresh 24-item/42-rule audit, five actual searches and every-binder probes pass. Immutable independent helper/caller proofs, actual private/public type and binder metadata, and all actual standard axiom sets are verified. Module and complete unfiltered final LSP pass with 0 errors / 19 warnings.
Accepted uncontended exact-prefix profile: 36.297 → 49.696 ms; no whole-file performance claim.
Frozen owner full (64.388 s) then separate LeanEval (24.164 s) pass.
[Dedicated audit](Theta-isPrimitive_pow.md). Theta 17/35, overall 198/264 originals;9/14 files complete.
No new production helper. Next: original 18, exists_eq_pow_mul_of_rootMultiplicity, applying approved hR removal.


## Published checkpoint18 — exists_eq_pow_mul_of_rootMultiplicity

Applied the approved removal of unused hR from the integer root-multiplicity factorization. Inlined the single-use primitive-power fact and applied Gauss’s lemma directly, shortening the proof from fourteen lines to twelve. The sole caller deletes the obsolete argument and retains its own hR and complete original contract. Definitions, remaining domains/arguments, conclusion and documentation are unchanged.

Fresh 24-item/42-rule audit, five actual searches, every-binder probes and public literature pass. Independent immutable original target/caller proofs, explicit full-old adapter, exact retained binder metadata and selected-drop AST, and actual standard axioms pass. The edited caller also profiles at 279.948 → 259.915 ms. Module and complete unfiltered final LSP pass with 0 errors / 18 warnings.
Accepted uncontended exact-prefix profile: 395.202 → 361.739 ms; no whole-file performance claim.
Frozen owner full (58.997 s) then separate LeanEval (23.527 s) pass.
[Dedicated audit](Theta-exists_eq_pow_mul_of_rootMultiplicity.md). Theta 18/35, overall 199/264 originals;9/14 files complete.
No new production helper. Next: original 19, pow_rootMultiplicity_le.


## Published checkpoint19 — pow_rootMultiplicity_le

Localized hB from a bound on every coefficient to the bound on the absolute leading coefficient used by the proof. This strengthens the theorem while retaining every other binder, its domains and conclusion. The original uniform premise recovers the new one at R.natDegree. The sole Θ_unique_le caller specializes hcoef there and keeps its complete original public contract. Proof thirteen → twelve lines; existing documentation and source quote preserved with one clarification.

Fresh 24-item/42-rule audit, five actual searches, every-binder probes and public literature pass. Concrete preapply candidate/old adapter/caller compiled before the authorized edit. Definitive actual-built checks establish the exact localized premise, full-old adapter, other retained metadata, immutable independent proofs, and actual standard axioms. Required borderline caller repeats pass: 820.803 and 829.009 ms, with no speedup claim. Module and complete unfiltered final LSP pass with 0 errors / 18 warnings.
Accepted uncontended exact-prefix profile: 295.693 → 366.074 ms; no whole-file performance claim.
Frozen owner full (77.364 s) then separate LeanEval (24.504 s) pass.
[Dedicated audit](Theta-pow_rootMultiplicity_le.md). Theta 19/35, overall 200/264 originals;9/14 files complete.
No new production helper. Next: original 20, headline Θ_unique_le (approved DecidableEq σ removal and proof shortening).


## Published checkpoint20 — Θ_unique_le

Shortened the headline proof from twenty-nine lines to three by extracting the per-polynomial index/log bound. Applied only the approved public DecidableEq σ removal; hB/hr/Fintype and every other original public parameter/domain/conclusion remain. The one new private helper received a separate fresh audit: its positive-weight hypothesis was removed and coefficient hypothesis localized to the equivalent univariate leading coefficient, shortening its body from twenty-six to twenty-three lines.

Both original and fresh helper audits complete all 24 items/42 rules/five actual searches/binder probes and their literature requirements. Final-source actual checks independently replay the immutable original public proof and INITIAL helper proof, recover both original contracts through explicit adapters, verify exact selected AST/retained metadata and actual standard axioms. Final helper/public timings are 481.521/73.124 ms (combined 554.645), after every normal request drained. The public hr warning remains unsuppressed under this audit’s preserved public-API scope. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: public 829.009 → 73.124; new helper 481.521 ms; no whole-file performance claim.
Frozen owner full (39.883 s) then separate LeanEval (15.025 s) pass.
[Dedicated audit](Theta-Theta_unique_le.md). Theta 20/35, overall 201/264 originals;9/14 files complete.
One new private helper independently audited and retained; helper audits do not increase original counts. Next: original 21, public definition lem6M.


## Published checkpoint21 — lem6M

Retained the one-line real coefficient-bound constant unchanged: it matches the paper’s equation (16), is reused by the main statements, and needs no extra abstraction or naming/API change. No source, caller, definition-value or documentation edits.

Fresh 24-item/42-rule audit, five actual searches, all four compiled binder deletions/value-sensitivity certificates, semiring assessment and public literature pass. Independently elaborated immutable type/value, kernel definitional equality and both rfl comparisons protect the exact definition; actual built axioms are standard only. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: 37.516 ms; no whole-file performance claim.
Frozen owner full (5.980 s) then separate LeanEval (3.018 s) pass.
[Dedicated audit](Theta-lem6M.md). Theta 21/35, overall 202/264 originals;9/14 files complete.
No new production helper; the previously added helper remains separately audited. Next: original 22, public definition lem6Φ.


## Published checkpoint22 — lem6Φ

Normalized three ordinary lambda arrows to ↦ in the one-line Φ definition. Its complete original telescope, mathematical value, public API, paper documentation and all callers remain unchanged; no helper introduced.

Fresh 24-item/42-rule audit, five actual searches, all six effective binder probes, literature/inversion and measured tables pass. Independently elaborated immutable RSet/indexSet/Θ/Φ definitions, exact telescope metadata, type/value definitional equality and kernel rfl checks pass against the rebuilt actual constant; actual axioms remain standard only. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: 19.752 ms; no whole-file performance claim.
Frozen owner full (65.683 s) then separate LeanEval (26.314 s) pass.
[Dedicated audit](Theta-lem6Phi.md). Theta 22/35, overall 203/264 originals;9/14 files complete.
No new production helper; the prior helper remains separately audited. Next: original 23, one_le_lem6M.


## Published checkpoint23 — one_le_lem6M

Shortened the M lower-bound proof from eight to six body lines, replacing linarith with ordered-add nonnegativity and direct existing product/power lemmas. All public arguments, conclusion, name, documentation and callers remain unchanged.

Dedicated 24-item/42-rule audit, five actual searches, all five effective binder probes with independent counterexamples, literature/inversion and measured tables pass. Immutable independent original nonself proof, exact complete original type AST/binder metadata and actual built standard-axiom checks pass. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: 131.343 (conservative including tiny lazy definition-equation tasks <133; baseline 284.544, conservatively <286) ms; no whole-file performance claim.
Frozen owner full (73.770 s) then separate LeanEval (26.327 s) pass.
[Dedicated audit](Theta-one_le_lem6M.md). Theta 23/35, overall 204/264 originals;9/14 files complete.
No new production helper; the prior helper remains separately audited. Next: original 24, floor_sq_div_two_le_sum.


## Published checkpoint24 — floor_sq_div_two_le_sum

Shortened the floor-sum proof from eleven to six body lines using the directly cast Gauss sum identity and the floor bound. Removed the local floor name and nested cast-equality boilerplate; the exact public real-number statement, documentation and sole caller remain unchanged.

Dedicated 24-item/42-rule audit, five actual searches, both effective binder probes, a certified negative-input counterexample, literature/inversion and measured tables pass. The compiled ordered-floor-field candidate was assessed and not recommended for public API churn. Immutable independent original nonself proof, complete original type recovery and actual built standard axioms pass. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: 414.955 (baseline 503.277) ms; no whole-file performance claim.
Frozen owner full (83.621 s) then separate LeanEval (29.992 s) pass.
[Dedicated audit](Theta-floor_sq_div_two_le_sum.md). Theta 24/35, overall 205/264 originals;9/14 files complete.
No new production helper; the prior helper remains separately audited. Next: original 25, sq_div_three_lt_floor_sq_div_two.


## Published checkpoint25 — sq_div_three_lt_floor_sq_div_two

Reduced the floor-square comparison from five proof lines to one nlinarith application using the direct natural-floor upper bound. The exact original real-number API, strict threshold 10, docstring and sole caller remain unchanged.

Dedicated 24-item/42-rule audit, five actual searches, both effective binder probes, compiled weaker thresholds/generic field candidates and certified counterexamples, literature/inversion and measured tables pass. Broader variants were assessed and not recommended for public API churn. Independent immutable original nonself proof, exact full telescope metadata/conclusion recovery and actual built standard axioms pass. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: 349.782 (baseline 376.779, corrected disjoint kernel/linter accounting) ms; no whole-file performance claim.
Frozen owner full (89.100 s) then separate LeanEval (28.568 s) pass.
[Dedicated audit](Theta-sq_div_three_lt_floor_sq_div_two.md). Theta 25/35, overall 206/264 originals;9/14 files complete.
No new production helper; the prior helper remains separately audited. Next: original 26, min_le_sum_max.


## Published checkpoint26 — min_le_sum_max

Strengthened the positive-part arithmetic-sum bound by removing both public positivity/size hypotheses hrp and hθ; its exact real/natural domains and conclusion remain. Public proof46→7lines. The sole index_le_lem6 caller receives named θ/rp arguments and retains its entire original contract, including hq and DecidableEq.

Fresh original audit plus three separate fresh helper audits complete: all24/42/5-search, effective-binder compiled probes, literature/inversion and measured tables. Independently replayed immutable original min and ENTIRE index_le_lem6 proofs; exact old telescopes/adapters, BinderInfo/value and actual built standard axioms pass. Private linear hr removal, quadratic hr removal/weak cutoff and separate positive-core proof are independently verified. Module and complete unfiltered final LSP pass with 0 errors / 17 warnings.
Accepted uncontended exact-prefix profile: public165.806; linear460.921, positivecore543.552, quadraticwrapper304.757 (all four <750) ms; no whole-file performance claim.
Frozen owner full (92.510 s) then separate LeanEval (33.553 s) pass.
[Dedicated audit](Theta-min_le_sum_max.md). Theta 26/35, overall 207/264 originals;9/14 files complete.
Three new private helpers each received separate fresh dedicated audits; final bodies linear15, positivecore22, quadraticwrapper7. Helpers add0 original declarations. Next: original27, sum_max_sub_le_index_det (approved DecidableEqτ and hR removal).


## Published checkpoint27 — sum_max_sub_le_index_det

Applied exactly the approved DecidableEqτ and hR removals from the determinant-index lower bound, retaining the degree/weight interface and all other original arguments. Proof25→24lines with explicit nonnegativity and restricted linear arithmetic. The sole index_le_lem6 caller drops the obsolete argument/local proof and retains its entire original public contract.

Fresh24-item/42-rule audit, five actual searches, every effective binder compiled probe, literature/inversion and measured tables complete. Broader finite-family/strict-degree and generic determinant alternatives compiled but are not recommended for API churn. Independent immutable complete original target AND entire index_le_lem6 proof/type replay, exact old adapters/names/BinderInfo/value/universes/conclusions and actual standard axiom sets pass. Module and complete unfiltered final LSP pass with 0 errors / 14 warnings.
Accepted uncontended exact-prefix profile: 746.452 (clean baseline779.542, required clean repeat831.962; discarded closing-scope-error run excluded) ms; no whole-file performance claim.
Frozen owner full (110.300 s) then separate LeanEval (32.749 s) pass.
[Dedicated audit](Theta-sum_max_sub_le_index_det.md). Theta 27/35, overall 208/264 originals;9/14 files complete.
No new production helper; all prior helpers remain separately audited. Next: original28, index_det_le (approved DecidableEqτ, hl′, hδ and unused implicitδ removal; proof/performance cleanup).


## Published checkpoint28 — index_det_le

Applied approved DecidableEqτ/δ/hl′/hδ removals and the supported redundant hB removal under standing authorization. Uniform coefficient bounds imply the needed nonnegativity. Public proof94→24 physical lines including all3 Step comments; sole caller drops only obsolete application arguments and retains its entire original public contract.

Fresh24-item/42-rule/five-actual-search/every-effective-binder/literature/inversion/packing/inequality/11-step audits complete. Independent immutable complete original target AND entire index_le_lem6 proof/value/type replay, exact old adapters/names/BinderInfo/universes/conclusions and actual standard axiom sets pass. Both initially extracted private helpers received separate fresh audits; the coefficient helper was deleted using the existing constant-degree bound specialization, with actual built and trace absence checked. Module and complete unfiltered final LSP pass with 0 errors / 11 warnings.
Accepted uncontended exact-prefix profile: public742.222; retained helper655.221 (original public baseline2083.744; both final<750) ms; no whole-file performance claim.
Frozen owner full (91.138 s) then separate LeanEval (30.612 s) pass.
[Dedicated audit](Theta-index_det_le.md). Theta 28/35, overall 209/264 originals;9/14 files complete.
One retained private separated-product helper26lines, separately freshly audited; the initially added coefficient helper was separately freshly audited and deleted. New helpers and revisits add no original count. Next: original29, index_le_lem6 (approved DecidableEqτ removal, explicit hq retention, ordinary≤30 structuring and actual instrumented performance repair).


## Published checkpoint29 — index_le_lem6

Removed approved DecidableEqτ and extended the coordinate ratio from strict to nonstrict after concrete old-contract/caller verification. Replaced the default-heartbeat-failing broad arithmetic with a 22-line public assembly and separately audited weight, mapped-determinant and numeric arguments. Explicit hq remains; the entire original strict Θ_option_le caller contract is preserved.

Fresh full24/42/five-actual-search/every-binder/literature/inversion/packing/inequality/11-step audits complete. Immutable independent entire original29 and original30 proofs, exact original adapter, retained names/types/BinderInfo/universes/conclusions, actual opaque proof values and standard axiom sets pass. Each of the three new private helpers received its own separate fresh audit, including exact first-proof recovery and generalized private-contract adapters; no original count inflation. Module and complete unfiltered final LSP pass with 0 errors / 10 warnings.
Accepted uncontended exact-prefix profile: public895.050/854.163; weight408.013/361.605; mapped707.126/651.477; numeric939.576/873.525 (first/required-repeat; all<1000) ms; no whole-file performance claim.
Frozen owner full (92.063 s) then separate LeanEval (29.415 s) pass.
[Dedicated audit](Theta-index_le_lem6.md). Theta 29/35, overall 210/264 originals;9/14 files complete.
Three substantive retained private helpers separately freshly audited: numeric16lines (δ≤1,rp≥3, noδ positivity premise), weight12lines (no weight-positivity premise), mapped determinant14lines (same signature). No new public domain or conclusion change. Next: fresh dedicated supported original29 arithmetic-boundary revisit K (counts unchanged), then original30 Θ_option_le.


## Supported revisit of original 29 — index_le_lem6 arithmetic boundary

Extended the exact index bound to 0≤δ, δ≤1 and 3≤rnone, replacing the old strict reciprocal-degree restriction. Removed redundant public hr0 and hB after concrete reconstruction proofs: the ratio and positive distinguished weight force all weights positive, and a nonzero integer coefficient plus its uniform bound force1≤B. Explicit hq is retained.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Immutable independent
original proof and explicit old-telescope adapter recover the original contract from the actual
new theorem; exact retained types/order/BinderInfo/user names, selected-drop AST and actual
standard axioms pass. ENTIRE original Θ_option_le telescope and independent original proof retained; its minimal new proof explicitly calls the changed index theorem, forwards old strict δ bounds via.le, derives3≤rnone from the original reciprocal premise and omits only newly obsolete hr0/hB application arguments. Module and complete unfiltered final LSP pass with
0 errors and 11 warnings. Accepted uncontended exact-prefix aggregate:
public895.050/854.163, weight408.013/361.605, mapped707.126/651.477, numeric939.576/873.525 → public996.125/936.382, weight455.974/355.065, mapped722.709/634.434, numeric918.885/829.176 (first/required-repeat; all<1000) ms; no whole-file performance claim.
Frozen owner full build (92.105 s), then separate LeanEval (29.557 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-index_le_lem6-boundary-revisit.md).
Original counts unchanged: Theta 29/35, overall 210/264, 9/14 files. Next: original30 Θ_option_le (selected DecidableEq removal, explicit hq retained; assess corresponding supported boundary with concrete caller evidence).


## Published checkpoint30 — Θ_option_le

Removed approved `[DecidableEq τ]` and the derived `hr0` premise from `Θ_option_le`, extending its unchanged conclusion to closed δ bounds, `3 ≤ r none` and weak coordinate ratios. Retained `hq` and `hB`. The headline proof is five lines; the entire `Θ_lt` caller contract is preserved with minimal forwarding.

Fresh 24-item audit, 42 golf rules, five actual searches, every-binder probes, literature/inversion, packing, inequality and 11-step checks pass. Independent entire original30 and original Θ_lt proofs/adapters, actual new caller dependency, retained metadata and standard axioms pass. Owner cumulative recovery of all29 public contracts and all five definition values passes, including29 explicit old adapters,87 opaque body-type checks and87 actual standard axiom checks; both immutable original proof blocks are byte-identical. Module and complete unfiltered final LSP pass with 0 errors / 8 warnings.
Accepted uncontended exact-prefix profile: Θ_option158.615/144.368; public29 901.577/925.763; weight401.279/399.404; mapped693.423/723.578; numeric903.545/922.672 (first/required repeat; all<1000) ms; no whole-file performance claim.
Frozen owner full (113.288 s) then separate LeanEval (37.676 s) pass.
[Dedicated audit](Theta-Theta_option_le.md). Theta 30/35, overall 211/264 originals;9/14 files complete.
No new private helper; all three previously audited helpers unchanged. Original counts exclude revisits and helper audits. Next: original31 private one_lt_of_log_pos (assess direct existing Real.log_pos_iff replacement and actual deleted-wrapper absence/caller proofs).


## Published checkpoint31 — one_lt_of_log_pos

Deleted the five-line private `one_lt_of_log_pos` wrapper and used `Real.log_pos_iff` with the direct cast at its three `Θ_lt` call sites. All public contracts and every other helper remain unchanged.

Fresh private24/42/five actual searches/every-binder/counterexample/inversion/packing/inequality/11-step checks and exact independent FIRST/replacement/value/standard-axiom gates pass. The built wrapper is absent; the entire original Θ_lt type/value/standard axioms and exactly three direct log_pos_iff proof uses are checked. The bounded final actual-caller attempt stalled and was interrupted130 after four identical-output checks; no explicit Lean error or finite caller timing was observed. Module and complete unfiltered final LSP pass with 0 errors / 8 warnings.
Scoped direct-replacement certificate: 86.921 (real exact old-contract certificate; the deleted production declaration has no timing) ms; no whole-file performance claim. This is NOT an all-five performance pass: unchanged numeric/index29 failed the retained-prefix repeat at1068.193/1115.157ms after first876.997/935.661ms. Coordinator explicitly queues these independent prior proofs for mandatory final whole-file repair; no rollback or cherry-picked third sweep.
Frozen owner full (103.738 s) then separate LeanEval (34.051 s) pass.
[Dedicated audit](Theta-one_lt_of_log_pos.md). Theta 31/35, overall 212/264 originals;9/14 files complete.
Deleted one original private wrapper; no new helper. This still reviews one original declaration and adds no count from helpers/revisits. Next: original32 lem6M_lt (ordinary proof≤30; every new helper requires a separate fresh audit).


### Mandatory final performance repair queue after checkpoint31

The unchanged numeric/index29 required repeat failed at1068.193/1115.157 ms after
first876.997/935.661 ms. Both exact same-source traces are retained in the scoped31 report.
Baseline/final actual `Θ_lt` whole-source attempts stalled and only their own sessions were
interrupted130; neither produced a finite caller time or explicit Lean error. Original35 and
file-final profiling must resolve these obligations. Scoped31 certificate PASS does not establish
all-five or whole-file performance PASS. No third cherry-picked sweep was used.


## Published checkpoint32 — lem6M_lt

Simplified lem6M_lt from53 to21 proof lines using two substantive independently audited private estimates. Weakened p≥2 to p>0 and the logarithmic bound to≤, removed the derived positive-r₁ argument, and preserved the strict conclusion and entire Θ_lt caller contract.

Original32 and BOTH new helpers completed separate fresh24/42/five-search/every-binder/inversion/packing/inequality/11-step audits. Exact immutable old32 adapter, ENTIRE original/current Θ_lt independent proof/type/value/standard axioms, both INITIAL helper contracts and actual built opaque values/standard axioms pass. Current private bounds accept l≤2^r₁ and q≥0 while public32 retains its documented assumptions. Owner final-state cumulative verification passed47.118s: all29 exact original-public adapters,87 opaque body-type checks and87 actual standard-axiom sets; both full immutable proof blocks byte-identical. Module and complete unfiltered final LSP pass with 0 errors / 8 warnings.
Accepted uncontended exact-prefix profile: lem6M_lt675.914, factorial_coefficient_le_two_pow_aux290.063, two_pow_lt_rpow_aux597.526 (all below750; no threshold repeat required) ms; no whole-file performance claim.
Frozen owner full (91.810 s) then separate LeanEval (31.678 s) pass.
[Dedicated audit](Theta-lem6M_lt.md). Theta 32/35, overall 213/264 originals;9/14 files complete.
Two substantive private estimates have separate fresh completed audits: coefficient proof9lines with l≤2^r₁, exponential proof21lines with q≥0. Helper audits and supported revisits do not inflate original counts. Next: original33 lem7_Φ_bound, then34/35 and every final file phase.


## Published checkpoint33 — lem7_Φ_bound

Extended lem7_Φ_bound to the closed upper boundary δ≤1 while preserving its strict conclusion. Replaced broad nonlinear arithmetic with direct scaled bounds and restricted arithmetic, removed dead locals and one-use bounds, and forwarded the Θ_lt caller by.le. Proof22→20lines; no new helper.

Fresh24/42/five actual searches/every-binder/certified-counterexample/public-literature/inversion/packing/inequality/11-step gates pass. Exact immutable independent old33 proof, actual ROOT old-contract adapter and ENTIRE original/current Θ_lt independent proof/type/value/standard axioms pass. Final real target first/repeat876.021/757.251ms pass versus baseline1489.059ms. Owner final-state cumulative verification passed51.807s: all29 original-public adapters, all5 definition values,87 opaque body-type checks and87 actual standard-axiom sets, with both complete original proof blocks byte-identical. Module and complete unfiltered final LSP pass with 0 errors / 8 warnings.
Accepted uncontended exact-prefix profile: 876.021 / 757.251 (required same-source repeat passed; baseline1489.059) ms; no whole-file performance claim.
Frozen owner full (105.519 s) then separate LeanEval (38.323 s) pass.
[Dedicated audit](Theta-lem7_Phi_bound.md). Theta 33/35, overall 214/264 originals;9/14 files complete.
No new helper; existing separately audited private helpers are unchanged. Next: original34 lem7_numeric, then35 Θ_lt and all final file phases.


## Published checkpoint34 — lem7_numeric

Extended lem7_numeric to δ≤1 and the closed Φ upper bound, removed the unnecessary Φ≥0 premise, and preserved its strict conclusion. Explicit scaled-square comparisons replace broad nonlinear search; proof25→29lines with no helper. The Θ_lt call is minimally adapted and its full public contract preserved.

Fresh24/42/five actual searches/every-binder/public-literature/inversion/packing/inequality/11-step gates pass. Exact immutable old34 adapter, ENTIRE old/current/independent Θ_lt effective type, opaque proof value, standard axioms and actual dependency pass. Owner cumulative d34-values passed29 original-public adapters/all5 definition values/87 opaque body types/87 actual standard-axiom sets, with both complete immutable original proof blocks unchanged. Module and complete unfiltered final LSP pass with 0 errors / 8 warnings.
Accepted uncontended exact-prefix profile: 757.682 and required same-source repeat865.831 (baseline1429.265) ms; no whole-file performance claim.
Frozen owner full (108.121 s) then separate LeanEval (33.707 s) pass.
[Dedicated audit](Theta-lem7_numeric.md). Theta 34/35, overall 215/264 originals;9/14 files complete.
No new helper; existing separately audited helpers unchanged. No original-count inflation from helper/revisit audits. Next: original35 headline Θ_lt, every newhelper separate fresh audit, then mandatory performance repairs and all final file phases.


## Published checkpoint35 — Θ_lt

Factored Θ_lt into substantive numerical, transport, base and successor stages. Removed its δ upper bound and derived positive-weight/denominator premises, weakened the last weight to3≤rLast, closed adjacent product and log bounds, and preserved the strict conclusion. Headline stays within15lines (currently15 after base-helper contract cleanup); MainLemma receives only the necessary proof-call adaptation and keeps its entire public contract.

All ELEVEN introduced helper obligations freshly and separately audited (eight retained, three introduced/deleted), followed by the additional measured prefix performance repair. Frozen current-source359 checks preserve the entire original Index/Theta, original2b MainLemma and independent current MainLemma proof blocks, publicTheta9/Main26 contracts, exact original helper adapters/deletion AST checks and actual standard axioms. Owner cumulative29 probe passes29 full old-public adapters,87 opaque value/type checks,87 actual standard-axiom sets and all five definition equality recoveries; independent all50 actual retained declaration values/types/axioms also pass. Module and complete unfiltered final LSP pass with 0 errors / 8 warnings.
Accepted actual whole-source scoped final pair: public Θ_lt413.535/330.244; prefix757.698/767.127; phi887.425/641.027; successor852.192/728.387; all eight retained35 helpers below1000 in both captures ms; no whole-file performance claim. Whole traces match all50 actual declarations with strict UTF8 and disjoint anchored totals; final pair accepts all eight introduced retained helpers and headline on identical cfa source. Other older failures remain queued.
Frozen owner full (61.547 s) then separate LeanEval (31.863 s) pass.
[Dedicated audit](Theta-Theta_lt.md). Theta 35/35, overall 216/264 originals;9/14 files complete.
All11 introduced obligations complete: retained scaled_unique,delta_succ,prefix_lt,base,denominators,phi,successor,large_delta; introduced/deleted fin_option,prefix_log,last_lt_first each have their own fresh generic original-contract/deletion-replacement audit. No helper or revisit count inflation. Next: dedicated sequential numeric/index29 performance repairs, fresh independent filewide simplify review, all cumulative semantic/native/import/actual whole-file profile/full+separateLeanEval gates before Theta file-final publication.


## Performance revisit of original 26 — mul_sq_div_three_le_sum_max_of_pos_aux

Replaced arithmetic search with an explicit nonnegative polynomial certificate and broad field_simp with eq_div_iff plus ring. The exact six-binder private contract, callers and22-line proof length remain unchanged; no new helper. Deterministic heartbeats2624→2111.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. Exact independent FIRST source/context, current six-binder names/order/BinderInfo/universes/conclusion and opaque values/std axioms pass; no public signature/definition/domain change. Actual positive→quadratic-wrapper→public-min complete types, opaque values, standard axioms and positive dependencies pass; the entire366-check semantic scaffold preserves all359 prior gates and all four complete original/current proof blocks. Complete native responses for Theta and MainLemma pass with0errors/8+3warnings. Module and complete unfiltered final LSP pass with
0 errors and 8 warnings. Accepted uncontended exact-prefix aggregate:
historical1074.965/908.077 failed pair; published903.926/781.005 baseline → positive585.259/569.809; wrapper400.861/381.226; publicmin176.910/182.737 ms; no whole-file performance claim.
Frozen owner full build (77.937 s), then separate LeanEval (35.334 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-mul_sq_div_three_le_sum_max_of_pos_aux-performance.md).
Original counts unchanged: Theta 35/35, overall 216/264, 9/14 files. Next: fresh dedicated sum_max_sub_le_index_det performance revisit, then remaining six older repairs and independent filewide review/final gates.


## Performance revisit of original 29 — index_le_lem6

Replaced weight-cutoff arithmetic search with an exact Nat subtraction certificate, shared positive initial degree, and restricted terminal mul_add simplification. Exact public statement, explicit hq, shared existential witness and surrounding source remain unchanged; no new helper. Heartbeats4825→1946; proof27→26 noncomment lines.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. All original public adapters, exact retained names/order/BinderInfo/universes/conclusion and actual opaque values/standard axioms pass. No public signature, definition or domain changes. The entire373-check semantic scaffold preserves the complete preceding366 prefix and all four independent original/current proof blocks. Fresh preceding target and entire Θ_option_le proof/type/opaque value/standard axioms/dependency pass. Complete native Theta/MainLemma responses pass with0errors/8+3warnings. Module and complete unfiltered final LSP pass with
0 errors and 8 warnings. Accepted actual whole-source scoped profile:
published1235.462/1644.559 failed pair → index_le_lem6 498.642; Θ_option_le160.903 (both below750; repeat not required) ms; no whole-file performance claim.
Frozen owner full build (68.103 s), then separate LeanEval (33.964 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-index_le_lem6-performance.md).
Original counts unchanged: Theta 35/35, overall 216/264, 9/14 files. Next: fresh dedicated index_det_le performance revisit, then index_separated, index_numeric, sum_max, lem7_Φ_bound and lem7_numeric repairs, followed by independent filewide review/final gates.


## Performance revisit of original 28 — index_det_le

Replaced broad determinant coefficient-bound normalization with pinned finite-product, sum, cardinality, cast and power rewrites. Exact public contract, caller, surrounding source and all three Step comments remain unchanged; no new helper or import. Heartbeats4996→3357.

Fresh dedicated full 24-item audit, 42 golf rules, five actual searches, every-binder probes,
literature/inversion, packing, inequality scan and 11-step checklist pass. All original public adapters, exact retained names/order/BinderInfo/universes/conclusion and actual opaque values/standard axioms pass. No public signature, definition or domain changes. The entire380-check semantic scaffold preserves all373 preceding checks and four full canonical proof blocks. Fresh independent preceding target and entire index_le_lem6 proof/type/binder/universe/opaque value/standard axioms/nonself and actual caller dependency pass. Complete native Theta/MainLemma responses pass with0errors/8+3warnings. Module and complete unfiltered final LSP pass with
0 errors and 8 warnings. Accepted actual whole-source scoped profile pair:
latest1293.336 failed observation; historical1179.250/1424.714 failed pair → index_det_le822.592/726.010; index_le_lem6576.591/581.268; Θ_option_le170.607/142.216 ms; no whole-file performance claim.
Frozen owner full build (78.752 s), then separate LeanEval (32.808 s),
both pass on identical SHA. [Dedicated revisit audit](Theta-index_det_le-performance.md).
Original counts unchanged: Theta 35/35, overall 216/264, 9/14 files. Next: fresh dedicated index_separated_mul_le_aux performance revisit, then index_numeric, sum_max, lem7_Φ_bound and lem7_numeric plus newly required second theta_prefix_lt_aux repair, followed by independent filewide review/final gates.
