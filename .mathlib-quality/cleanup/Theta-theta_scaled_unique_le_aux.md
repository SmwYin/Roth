# theta_scaled_unique_le_aux — dedicated fresh introduced-helper audit

Status: dedicated helper audit COMPLETE; original35 remains unpublished. This helper earns no original-declaration
count credit. All fresh artifacts are in `/private/tmp/theta35-scaled-fresh/`.

## Baseline and mathematical content

Inherited baseline Theta SHA9faa85d31dce678483027d1580c79d4a8ad220636806af1040ecc5da53738d94,
MainLemma SHAca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4.
The preceding phi audit's complete native results establish zero errors and eight/three existing
Theta/MainLemma warnings. Its actual complete pair gives scaled639.588/678.305ms,
phi648.100/918.689ms and publicΘ290.589/527.984ms. These are inherited baseline evidence,
not fresh final measurements. Owner baseline full build is inherited; full project build and
separate LeanEval remain owner gates. Cache fetching and unrelated warnings are outside scope.

The lemma bounds one-variable polynomial-index Θ at height M by δ. Monotonicity enlarges
M to q₁ raised to δlr₁; the one-variable estimate bounds Θ by the logarithmic quotient;
the balanced logarithm hypothesis compares that quotient to δ. This is substantive project
mathematics, using project Θ_mono and Θ_unique_le plus real-power/logarithm arithmetic,
rather than a wrapper around one to three Mathlib facts.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, plus the lean4/mathlib-quality
skills, complete cleanup workflow and applicable style/naming/profiling references.
The dispatched 30-line proof/10-line subproof bounds govern this private helper.
No Git, shared logs, rename queue, pins or unrelated declarations are owned here.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | No inherited target warning; fresh final full native gate required below. Existing public warnings remain protected. |
| 2 | Have scan | Inline hL₁; replace single-use hC1 with hM1.trans hM. Final hL is shared twice and hL₂ three times to derive hr₂/hq₂ and denominator positivity. Retain substantive cast/sign proofs; inner typed h pins the rpow inversion expected type after documented inference failures. |
| 3 | Options | No production option/limit; none added. Anonymous scratch automation uses the lower10000 heartbeat bound only. |
| 4 | Simp | No original simp command; exact_mod_cast and push_cast perform genuine cast bridges. New terminal simpa reduces the q₁^0 side; leave unsqueezed. |
| 5 | Naming | Mathematical snake_case describes scaled one-variable Θ upper bound; private _aux, no scheme numbers/forbidden abbreviation/_ge_/_gt_. No rename needed. |
| 6 | Packing | Greedily pack complete binders and conclusion toward100 codepoints; every final signature line measured below. |
| 7 | By | All := by placements end the preceding line. |
| 8 | Format | Two-space proof indent; no blank proof lines, semicolon chains, haveI/letI or production scaffolding. |
| 9 | Comments | Target has none. Preserve every surrounding and phi signpost comment. |
| 10 | Docstring | Private helper appropriately has none; all public documentation protected. |
| 11 | Visibility | Retain private: sole direct consumer is phi in this file. |
| 12 | Structure | Final proof and all local subproof counts below; no conjunction, existential or case split. No new helper needed. |
| 13 | Mathlib | Five actual methods and clean anonymous generic-route probes below. Generic log APIs are building blocks, not full Θ replacement. |
| 14 | Junk def | n/a: theorem, not a data definition. |
| 15 | Exists | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | No occurrence; no definitional scaffolding. |
| 17 | Negation | No push_neg/contradiction transformation. |
| 18 | Generalise | All15 FIRST effective parameters drop-probed. Remove hδ0 and hr₂ with concrete compiled derivations; recover full FIRST contract independently. Other applicable weakenings tested below. |
| 19 | Inequalities | All in smaller-side-left form; reverse-inequality scan below. |
| 20 | Normal form | Nat weights/denominators, real logs/rpow and project Θ are canonical here; no pairwise equivalence API added. |
| 21 | Syntax generality | Dropping derivable δ nonnegativity and r₂ positivity makes the sole caller easier; remaining premises expose exactly the scaling/log comparison data. |
| 22 | Imports | n/a: no import added; MainLemma unchanged. |
| 23 | Casts | Nat→Real bridges remain genuine. Explicit real expected types are load-bearing in rpow inversion and positive product; candidate inference failures demonstrate this. |
| 24 | Instances | n/a: no instance declaration or class binder introduced. Actual metadata checks hidden effective binders. |

## Search, generic routes and reflection

All four native response objects are preserved in search.json. Full source grep logs are
untruncated and separate from compiled positive semantic evidence.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Weighted one variable polynomial index theta bound using logarithmic denominator comparison and a real power bound | Roth-number/Behrend, Hurwitz-kernel, Chevalley facts; different constructions |
| B Loogle | Real.log, _ * _ ≤ _ * _ | Fernique logRatio inequality; different statement |
| C LeanSearch | logarithm monotonic real power bound product logarithms division inequality | Real.logb_le_logb_of_le, log_le_log_iff etc.; useful generic components only |
| D source rg | full theta_scaled_unique_le_aux/scaled_unique/Θ in Mathlib NumberTheory/Pow | no full helper equivalent; unrelated theta notation preserved in raw log |
| E local names | log_rpow | positive Real.log_rpow and ENNReal.log_rpow hits; symbol index unavailable, so no absence inference |

Auxiliary variants examined: monotonic log/logb quotient bounds, real-power exponent inversion,
nonnegative scaled logarithmic comparisons, one-variable Θ. Common-equivalents discrete,
finiteness, separation and bornology buckets do not match this polynomial-index theorem.
No absolute absence claim follows from these bounded searches.

AutomationNegative.lean contains exact source before the target, then anonymous examples
with the full original statement; neither imported current target nor named failed target
is available to exact?/apply?. grind fails, aesop makes no progress, exact? cannot close,
apply? reaches the deliberately lower10000-heartbeat limit; positivity is not a positivity
goal, norm_num leaves goals, gcongr makes no progress. Raw automation-negative-clean logs
retain every failure. An early started duplicate scratch request was interrupted; it is
not positive evidence and is drained before final performance work. The clean complete
run is the cited search evidence. No unbounded native multi_attempt was repeated.

The proof's mathematical outline remains monotonicity, unique-variable Θ, and logarithmic
comparison. Inlining pure forwarding facts and using the available height interval avoids
recomputing a power lower bound. Blind whole-goal automation cannot see the specialized
project argument. A separate generic log lemma would require nearly the same assumptions
and a one-off caller; no missing reusable API or substantive new helper is justified.

## Generalisation and inversion

Every original binder is covered by compiled drop trials, with autoImplicit=false, in
four small BinderNegative files. binder-ranges.json records the exact per-trial ranges;
final diagnostic mappings below distinguish expected failures from positive evidence.

| Binder | Role | Mechanical candidate | Disposition |
|---|---|---|---|
| δ | Real exponent and result | drop | dependent statement cannot elaborate |
| M | height in Θ and interval | drop | dependent statement cannot elaborate |
| hδ0 | sign used in final scaling | drop original proof; independently derive sign | recommended removal compiled; production13-binder statement recovers original15 |
| q₁ | original base/logarithm | drop | dependent hypothesis cannot elaborate |
| q₂ | target denominator/logarithm | drop | dependent conclusion cannot elaborate |
| r₁ | base weight/exponent | drop | dependent hypotheses cannot elaborate |
| r₂ | target weight/logarithm | drop | dependent hypotheses/conclusion cannot elaborate |
| l | positive natural scaling | drop | dependent exponent/conclusion cannot elaborate |
| hq₁ | positive logarithm and exponent inversion | drop; 1≤q₁ | proof cannot derive strict log positivity |
| hr₁ | strict balanced-log transfer, exponent sign inversion | drop; 0≤r₁ | strict product positivity unavailable |
| hr₂ | positive Θ weights/denominator | drop; 0≤r₂ original proof; independent derivation | TwoWeakCandidate exit0 proves it redundant; remove, derive from positive balanced-log product |
| hl | positive scaling | drop; 0≤l | Nat.mul_pos requires strict positive l |
| hqr | balanced logarithm comparison | drop | missing final comparison and q₂ positivity transfer |
| hM1 | lower height endpoint | drop; 0<M | Θ_mono/Θ_unique_le require1≤M |
| hM | upper height endpoint | drop | missing monotonicity bound |

Positive WeakCandidateCorrected.lean exits0. Its δ≥0 derivation first uses
Real.rpow_le_rpow_left_iff at base q₁>1 on hM1.trans hM, obtaining
0≤δ*(l*r₁); positive l*r₁ then yields δ≥0 by nonneg_of_mul_nonneg_left.
Thus hδ0 is redundant mathematically, not merely unused syntactically. Parent explicitly
confirmed the compiled recommendation. Its sole private phi call drops hε0.le. A subsequent positive TwoWeakCandidate.lean (exit0,27.114s) also derives hr₂ from the positive balanced-log product: hL gives log q₂>0 by Nat.cast_nonneg r₂, then pos_of_mul_pos_left hL hL₂.le gives r₂>0. The same sole call therefore drops the redundant last-weight positivity argument. No new helper is introduced.
WeakCandidate.lean and Candidate.lean initial failed casts/positivity trials remain raw;
only the corrected clean candidate certifies the recommendation.

The remaining strict hq₁/hr₁/hl hypotheses protect nondegenerate bases/weights; weakening them
would need separate zero/base-one cases with altered Θ assumptions. No such redesign is
supported by a clean compiled candidate here. This is a checked mechanical audit, not a
claim of mathematically maximal assumptions. There is no effective typeclass or universe
binder in this fixed Nat/Real statement. Abstracting Real would require redesigning Θ/log/rpow,
rather than merely moving to a parent typeclass. No point-global premise applies.

Literature: n/a, private auxiliary declaration, explicitly exempt under cleanup§2.6d.
Inversion: Θ is used through two specific project estimates throughout the argument, then
a scalar logarithmic inequality. That scalar step already uses generic Mathlib order
APIs. No additional abstract-witness statement with concrete reuse is identified.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: none |
| 1.3 rw/exact | n/a: no adjacent rw/exact |
| 1.4 simp/exact | n/a: no such pair; new terminal simpa directly supplies exponent comparison |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor | n/a: no conjunction proof |
| 1.7 apply/exact | n/a: composed .trans applications already direct |
| 1.8 contradiction | n/a: none |
| 1.9 eta | constant Unit lambdas change domain, not eta expansions |
| 1.10 single-use have | inline hL₁/replace hC1; final hL/hL₂ have2/3 uses; retain substantive local cast/sign proofs |
| 1.11 refine/fun | n/a: no apply/intro chain |
| 1.12 show | n/a: none |
| 1.13 projections | log positivity iff .1 used once, no repeated bundled projections |
| 1.14 merge rw | one existing rw only |
| 1.15 terminal simp | new terminal simpa unsqueezed |
| 1.16 nonterminal simp | n/a: none; push_cast performs cast normalization |
| 1.17 dot notation | .trans/.trans_le/.1 used directly |
| 1.18 trailing parens | grouped applications have following arguments/outer trans; retaining grouping makes expected types clear |
| 1.19 push Not | n/a: no negation tactic |
| 1.20 exists inline | n/a: no existential helper |
| 2.1 grind | actual clean whole-goal failure |
| 2.2 before grind | n/a: selected proof has no grind |
| 2.3 simpa | selected exponent inversion uses direct terminal simpa |
| 2.4 fun_prop | n/a: no function-property goal |
| 2.5 positivity | original positive base rw remains; denominator positivity replaced with explicit products/log_pos; whole-goal probe is inapplicable |
| 2.6 gcongr | actual no-progress whole-goal probe; final inequality is multiplicative rearrangement plus hqr |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic goal needing automation; Nat.mul_pos is direct |
| 2.8 aesop | actual clean-prefix no-progress failure |
| 2.9 norm_num/cast | exact_mod_cast/push_cast retained for real bridges; whole-goal norm_num leaves goals |
| 2.10 decide | n/a: arbitrary real inequalities and project Θ are not finite computation |
| 2.11 field_simp/ring | n/a: no denominator equality; div_le_iff₀ is the direct order API |
| 2.12 linear_combination | n/a: no final ring/ring_nf identity; nlinarith uses the explicit scaled inequality |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 calc | n/a: no calc remains; trans already term-mode |
| 2.15 parallel goals | n/a: no similar multiple goals |
| 3.1 erw | n/a: none |
| 3.2 legacy function tactics | n/a: none |
| 3.3 omega/lia | n/a: no omega or integer arithmetic tactic |
| 3.4 rcases/rfl | n/a: none |
| 3.5 attributes | sole private specialized theorem, not a general simplification/automation rule |
| 3.6 simp_all | n/a: none |
| 3.7 limits | no production limit added/raised; no profiler scaffolding |

## Packing and inequality artifacts

Final widths, structural inventory, native/build/semantic/profile gates and exact freeze follow.

Widths are Unicode codepoints; next item is a complete binder.

| Signature line | Width | Next item width | Arithmetic | Action |
|---|---:|---:|---|---|
| 734 | 100 | 12 | 100+1+12=113>100 | ok |
| 735 | 80 | 36 | 80+1+36=117>100 | ok |
| 736 | 93 | none | last line | ok |

| Reverse occurrence | Location | Rewrite | Rename |
|---|---|---|---|
| none | all signature/hypotheses/result | no ≥/> | no _ge_/_gt_ |

Signature counts {'≤': 4, '<': 3, '≥': 0, '>': 0}; proof21 lines, maximum owned width100. Local hδ0 derivation7 lines including its declaration; hr₂ one line and hq₂ two lines; every subproof≤10. Target comments0/0, all phi signposts preserved.

## Immutable proof, actual semantics and scope protection

FirstIndependent13.lean begins with the ENTIRE byte-identical FIRST batch1 context:
SHA0fbc16d1f06bbfe114d42a5c8f5fb2aee7263263b61ffc3dc8465bff941d1a54,
import Roth.Theta, namespace Roth.Theta35Candidate, no section/class/universe context.
It re-elaborates the complete original proof independently, locates the current private
module constant by exact suffix, and explicitly recovers the whole original15-binder
contract by applying the generalized13-binder helper. It checks every retained ordinary
name, BinderInfo, binder order/type, universe arity and conclusion, allowing exactly the
derivable hδ0/hr₂ removals. Actual/independent/adapter opaque values use value! true, infer
at their declared types and have only standard axioms; no self-use in the FIRST proof.
This independent old proof is separate from calling the current theorem via the adapter.

first-immutability.json verifies all three inherited FIRST contexts plus original success
logs/statuses, unchanged. immutable-original-blocks.json verifies literal original Index
and Theta blocks at inherited offsets, SHA72cfbff9…/355a5330…. The full original semantic
scaffold remains a literal prefix of ActualSemanticsFinal13.lean; only an appended assertion
checks the supported13-binder actual helper. No old public contract check is weakened.

source-inventory.json reconstructs the exact baseline by restoring only the owned helper
block and sole authorized phi call arguments; equality passes. MainLemma/Main are unchanged.
New helpers introduced:0; deleted:0. The existing deleted finite-option wrapper remains
absent and all ten inherited retained helpers remain subject to their dedicated audits.
No definition, docstring, public theorem contract, import or pin changed.

The new external identifiers Real.rpow_le_rpow_left_iff, nonneg_of_mul_nonneg_left,
pos_of_mul_pos_left, mul_nonneg and Nat.cast_nonneg are resolved positively in the independent verifier,
besides their use in the compiled production proof. Initial scratch cast inference and
left/right factor API errors are preserved, corrected, and excluded from positive gates.

Two original negative scratch files over-applied binder removal to cast expressions;
their parsing-error contexts/logs remain preserved. BinderNegativeCorrected0/1 retain
all casts and remove ONLY the intended leading binder. Corrected diagnostics, together
with unchanged BinderNegative2/3, are mapped to all20 actual trial ranges in
binder-results.json. No error limit is raised and no incomplete batch counts as coverage.

Preserved INTERIM14-binder module gates: lake build Roth.Theta exit0 in32.660s, then lake build Roth.MainLemma exit0 in35.611s; build-theta-final/build-mainlemma-final logs and statuses. Independent FIRST+actual+adapter run exit0 in37.481s (first-independent-final.json): exactly14 current and15 adapter binder checks,3 actual opaque value/standard-axiom PASS markers, and the independent no-self-use check. No PANIC, sorryAx or error occurs in this positive raw log.


Final13-binder source supersedes the preserved interim14-state evidence:
Theta SHA0fc24bf43cf815e06e3593a9d4c7d6b4d2dd256319ac6ac42810ef2911acb977.
Fresh sequential lake build Roth.Theta exits0 in31.589s, then Roth.MainLemma exits0
in33.509s (build-theta-final13/build-mainlemma-final13 logs/statuses).
FirstIndependent13.lean exits0 in37.170s (first-independent-final13.json), with exactly13
current and15 original-adapter binder checks,3 clean opaque value/standard-axiom checks,
and independent FIRST no-self-use. Removed private premises hδ0/hr₂ alone are explicitly
accounted for; all retained names/BinderInfo/order/types/universe arity/conclusion match.
Both FIRST copies begin with the same untouched immutable full batch1 bytes. The final
semantic scaffold starts with the entire previous verified scaffold byte-for-byte;
its only addition asserts the13-binder actual contract. No immutable proof was modified.

Final full semantic refresh: ActualSemanticsFinal13.lean exits0 in64.375s (actual-semantics-final13.json),68 PASS markers and no PANIC/error/sorryAx. It independently re-elaborates the ENTIRE immutable original2b MainLemma proof plus all48 copied declarations, an independent updated caller, exact immutable old Θ adapter, actual Root Θ_lt/main_lemma opaque values/standard axioms and all ten private helpers. The actual main_lemma→Θ_lt dependency is positive; independent old/new callers have no imported Root.main_lemma self-use. The public Θ9 contract and whole MainLemma contracts/definitions remain exact. Positive weakenings and all original mechanical failures are separately indexed, so failed unchanged-proof drop trials are never treated as impossibility proofs.

## Fresh complete native diagnostics and performance protocol

native-theta-final.json and native-mainlemma-final.json contain the COMPLETE UNFILTERED
fresh native responses after final13 module/semantic verification. Both success=true,
partial=false,timed_out=false,failed_dependencies=[],isError=false; zero errors, no warning
suppression. All existing warnings remain represented:

| File | Warning locations | Content |
|---|---|---|
| Theta | 1;93;101 twice;109;129;252;547 | copyright plus protected existing hr/hB/hq names;8 total |
| MainLemma | 1;149 twice | copyright and existing hδ0/hr₁ names;3 total |

No target warning occurs. MainLemma's unused public hypotheses are preserved for its later
dedicated audit; source remains byte-identical. pre-profile-drain.log is empty: every own
normal and native request completed before real timing. Profiling uses the unchanged
Lean4.34/default limits command `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Theta.lean`, external420s capture allowance only.
The timeout runner drains its entire process group; no Lean resource limit is changed.

The first fresh measurement and any required same-final-SHA repeat are actual whole-source
captures. The parser retains all52 declaration anchors, raw UTF-8, byte offsets and strict
owned-helper/phi/public-Θ slices, and adds only disjoint outer command/async proof/addDecl/
linter rows. Nested macro/kernel rows are not added twice. Any ≥750ms scoped result requires
one same-source repeat, and no failed result is replaced by a third cherry-picked run.
The existing unrelated actual whole-source failures remain a separate mandatory owner queue.


## Accepted actual-source performance

| Scoped declaration | First ms | Repeat ms | Result |
|---|---:|---:|---|
| theta_scaled_unique_le_aux | 624.889 | not required | PASS scoped |
| theta_phi_lt_aux | 575.334 | not required | PASS scoped |
| Θ_lt | 282.723 | not required | PASS scoped |

first: actual whole-source exit0 in267.812s;52/52 source anchors, strict UTF-8 with zero malformed bytes/replacement sequences. Raw SHAf9eadd0b9a1cfeffaf8b7597a70a377310db85d825ececbae06df2da8530577b; full table actual-profile-first-table.json and profile-first-strict-slices.json retain all offsets and disjoint rows.

theta_scaled_unique_le_aux: raw bytes189758681..194909202, total624.889ms; strict slice first-theta_scaled_unique_le_aux-strict-slice.log.

theta_phi_lt_aux: raw bytes216486400..220757138, total575.334ms; strict slice first-theta_phi_lt_aux-strict-slice.log.

Θ_lt: raw bytes237604418..239766727, total282.723ms; strict slice first-Θ_lt-strict-slice.log.


All samples are from the same final source SHA. No third sample was selected to discard
failure. All normal/native/trace requests are completed and the final process-drain log
has no matching compiler/capture process. MainLemma's complete semantics/module/native
checks pass, but its actual main_lemma timing remains UNMEASURED: the inherited bounded
trace did not reach it, so no finite timing or zero is claimed here.

Whole-file performance remains OPEN. Preserved previous failed pairs for sum_max_sub_le_index_det,
index_separated_mul_le_aux,index_det_le,index_numeric_bound_aux,index_le_lem6,lem7_Φ_bound,
lem7_numeric, the positive quadratic helper, and separately queued base/successor/large-δ
helpers remain mandatory owner repairs. Fresh complete tables are diagnostic evidence for
those scopes; this leaf does not edit or certify them. Cumulative29/all actual constants,
all eleven introduced-helper audit acceptance, final filewide simplify/performance,
full lake build and separate Roth.LeanEval still belong to the owner before publication.
Original counts remain215/264,Theta34/35, with no helper or revisit credit.

## Final scoped gates and workflow result

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | lake build Roth.Theta,exit0,31.589s; build-theta-final13.json |
| affected caller build | PASS | subsequent lake build Roth.MainLemma,exit0,33.509s; build-mainlemma-final13.json |
| independent FIRST/full old adapter | PASS | entire untouched batch1 proof context; first-independent-final13.json,exit0,37.170s;13 retained current/15 old adapter binders |
| actual values/standard axioms/full caller semantics | PASS | actual-semantics-final13.json,exit0,64.375s,68 PASS; positive Root dependency; all actual values value! true |
| public/definition protection | PASS | exact Θ9/full MainLemma contracts, original72cf/355a blocks, source-inventory reconstruction; only supported private hδ0/hr₂ removals |
| structure/naming | PASS | target21 proof lines, subproof≤7; mathematical private snake_case _aux name |
| packing/orientation | PASS | widths100/80/93 with full arithmetic table; no ≥/> |
| fresh complete unfiltered natives | PASS | both final JSONs;0errors,8/3 preserved existing warnings,partial=false,timed_out=false |
| actual owned/direct phi/public performance | PASS | accepted actual-source measurements above; all scoped results<750, repeat not triggered |
| whole-file performance | OPEN owner queue | unrelated failures retained, no whole-file PASS |
| cumulative/full build/separate LeanEval/publication | owner pending | not run or claimed by this leaf |

Simplify outcome: ISSUES-FOUND-AND-FIXED in the dedicated scoped review: remove two
provably redundant private hypotheses, inline the one-use initial log fact, replace hC1
with the height interval, share substantive positive product/log evidence. No callable
built-in simplify handoff is available; the independent filewide owner pass remains pending.
Buzz outcome: FAST-BOARD for the owned helper/direct phi/public consumer scope on accepted
actual source captures; unrelated mandatory repair queues explicitly remain OPEN.
No production heartbeat/depth limit raises, new axioms, sorry/native_decide, profiler
scaffolding, new helper, deleted helper, import/pin change or public premise removal.

Proof delta15→21 lines reflects deriving previously assumed facts; signature5→3 lines.
Target total20→24 lines. The sole necessary phi call drops exactly the two redundant
arguments. No target comment existed; all surrounding/phi narrative comments are preserved.
No rename is required or queued; shared rename sidecar remains owner-controlled.

## Eleven-step checklist

1. References: complete lean4/mathlib-quality worker workflow, mandatory five full references and applicable style/naming/profiling read.
2. Audit: all24 concrete items above.
3. Mathlib search: all five methods actually executed; raw responses/source logs and uncontaminated anonymous generic routes preserved.
4. Generalisation: all15 original effective binders mechanically probed,20 diagnostic trial ranges mapped; two supported independent positive removals; exact full-FIRST15 adapter, literature exemption and inversion recorded.
5. Packing: every signature line measured, all final rows ok.
6. Inequalities: entire signature scanned; zero reverse occurrences, explicit empty table.
7. Golf: all42 rules have concrete status above.
8. Reflection: specialized mathematical outline, generic routes and extraction alternatives examined.
9. Native: both fresh full unfiltered final files complete,zero errors.
10. Diff/module/semantic/profile gates: all scoped gates pass; owner cumulative/whole-file/full-build/LeanEval gates explicitly pending.
11. Rename sidecar: n/a,no rename; shared sidecar not modified.

Source authority is REVOKED and returned to the owner. All own normal/native/profile
requests are drained,pending[]. No further source edit or Lean request is authorized for
this leaf. final-freeze.json records exact source/report/artifact hashes, unchanged FIRST
history, full fresh evidence and inherited helper history. No new helper was introduced.


## Owner clarification: independent updated caller evidence

The earlier scaffold verified the entire independent ORIGINAL MainLemma proof and the
actual updated Root.main_lemma body/type/standard axioms/dependency. Its wording above
about an independent updated caller overstated the evidence: it did not separately copy
the CURRENT caller proof. Those historical67/68-marker runs are retained without relabeling.
The fresh delta-helper audit supplies that missing supplement in
`/private/tmp/theta35-delta-fresh/ActualSemanticsAugmented.lean`: the entire prior scaffold
is a byte-identical prefix, followed by the ENTIRE current MainLemma module copy, its
opaque-value/standard-axiom checks, all26 effective binder names/order/BinderInfo/types
and conclusion, direct Root.Θ_lt dependence, and AST exclusion of imported Root.main_lemma
and private Root MainLemma helpers. Its actual fresh run passed92.739s/114 PASS markers
on Theta3ea263890113e18bef9a29203ef1db57d929c18e40fd5201e34c9e4f0e776fc2;
MainLemma remains ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4.
Owner verified all96 artifact/source hashes and raw clean output in
`/private/tmp/theta35-delta-fresh/owner-checked.json`. This augmented scaffold is required
in subsequent final-source helper/batch gates. The exact report before this clarification
is preserved in `/private/tmp/theta35-owner-report-corrections/`; source and prior measurements
are unchanged. Original35 publication and whole-file final gates remain pending.
