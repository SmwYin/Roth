# theta_delta_succ_lt_aux — dedicated fresh helper audit

Status: dedicated helper audit COMPLETE; no original-declaration credit. The original35 Θ_lt
checkpoint remains unpublished. Artifacts: `/private/tmp/theta35-delta-fresh/`.

## Scope and mathematics

Inherited baseline is exact Theta SHA0fc24bf43cf815e06e3593a9d4c7d6b4d2dd256319ac6ac42810ef2911acb977;
MainLemma SHAca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4.
Baseline target415.183ms, direct phi575.334ms, publicΘ282.723ms are explicitly inherited
from the preceding dedicated scaled audit, not new measurements. Its complete native
Theta/MainLemma diagnostics establish eight/three warnings, zero errors. Owner supplied
baseline full-build evidence. Optional cache fetch and extra linter executable not run.
Fresh final native/module/semantic/profile evidence is recorded below when complete.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md and cleanup-gates.md in full, the full cleanup workflow,
lean4/mathlib-quality skills, and relevant style/naming/profiling references.
Only this target proof and this report are owned. No Git/sharedlog/pin/queue writes.
The public Θ_lt nine-binder API, all original definitions and MainLemma contract remain
protected; the supported scaled13-binder API and full FIRST15 recovery remain preserved.

Writing x=n+1>0 and u=1/(x+1), the bound δ≤u gives δ(1+u)≤u(1+u).
The identity u(x+1)=1 implies u(1+u)x=1−u²<1. Dividing by positive x
proves the strict bound required by the induction. No δ positivity is used: negative δ
already works. This polynomial reciprocal estimate is substantive algebraic content,
not a renamed direct Mathlib fact or a wrapper around one to three library calls.

The final proof transfers δ≤u first, clears the positive target denominator, and gives
only the reciprocal cancellation identity and u²>0 to nlinarith. This replaces the local
u abbreviation, two intermediate identities and the calc with six proof lines; no new
helper or caller change is needed. All original target/surrounding comments are preserved
(target has zero comments). All experiments and failures are retained.

## All 24 audit items

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | Baseline has no target warning; fresh final native diagnostics below. Existing unrelated warnings remain protected. |
| 2 | Have scan | Original hu0/huP/h1/h2 have proof content or substantive algebra; h3 is a one-use forwarding term. Replace all with early monotone transfer and direct cancellation/square inputs. Final hN is one-line proof content used once; hN2 is proof content used twice. Trial hP/hpos forwarding terms were both inlined in CandidateFinal. |
| 3 | Options | No production option or limit; none added. Search-only10000 heartbeat cap is lower than default and stays in scratch. |
| 4 | Simp | Original terminal simpa only [mul_assoc] disappears with the calc; no simp command remains. |
| 5 | Naming | Mathematical delta/successor strict-bound snake_case with private _aux; no forbidden scheme/numbered helper/abbreviation/_ge_/_gt_ pattern. |
| 6 | Packing | Every signature line measured below; original two-line signature is unchanged. |
| 7 | By | All := by placements are on preceding statement lines. |
| 8 | Format | Two-space proof indentation, no internal blank line/semicolon/instance scaffolding. |
| 9 | Comments | Target0/0; surrounding signpost comments preserved literally. |
| 10 | Docstring | Private auxiliary appropriately has none; public documentation unchanged. |
| 11 | Visibility | Sole direct consumer phi is in this file; retain private. |
| 12 | Structure | Six proof lines; positivity subproofs each one line, no branches/conjunction/exists; no extraction justified. |
| 13 | Mathlib | Five actual methods below; reciprocal-order/cancellation building blocks, no direct replacement found. Clean generic-route examples cannot close entire goal. |
| 14 | Junk def | n/a: this is a lemma, not a data definition. |
| 15 | Exists | n/a: no existential conclusion or witness. |
| 16 | Show/change | n/a: no show/change. |
| 17 | Negation | n/a: no push_neg or contradiction transformation. |
| 18 | Generalise | Every effective n/δ/hδ binder has compiled drop trial; a real nonnegative parameter candidate is compiled separately and assessed below. No supported hypothesis removal. |
| 19 | Inequality | All inequalities smaller-side-left; exact scan below. |
| 20 | Normal form | Ordered-field rational inequality with Nat cast, canonical division/≤/< form. No equivalent-form API proliferation. |
| 21 | Syntax | Existing n and hδ are supplied directly by phi; signature requires no extra positivity proof. Preserve this usable private contract. |
| 22 | Import fanout | n/a: no production import changes. |
| 23 | Casts | Nat→Real casts in hN/hN2 are genuine cross-type bridges fixing positivity target. No redundant same-type coercion added. |
| 24 | Instances | n/a: no instance declaration, typeclass binder or universe parameter. Actual metadata verifies full effective telescope. |

## Five actual searches and generic routes

Full native responses: search.json. Source searches are untruncated raw logs.

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | For positive real x and δ≤1/(x+1), δ(1+1/(x+1))<1/x | LiouvilleNumber.aux_calc, exists_nat_one_div_lt, sub_one_div_inv_le_two: different statements |
| B Loogle | _ * (1 + 1 / _) < 1 / _ | no hits |
| C LeanSearch | reciprocal successor bound (1/(x+1))*(1+1/(x+1))<1/x | Nat.one_div_lt_one_div, one_div_lt_one_div, one_div_le_one_div_of_le, le_one_div: useful order components only |
| D source rg | full target/delta_succ_lt/one_div.*succ/succ.*one_div | unrelated reciprocal-successor/series hits; no full-name hit |
| E local names | one_div | reciprocal order/cancellation names; index unavailable, so no absence inference |

Auxiliary variants: one_div_lt_one_div(_of_lt), le_one_div/lt_one_div, one_div_mul_cancel,
left/right multiplication transfer. Standard Mathlib Algebra/Order/Field/Basic is the
relevant component source. Discrete/finiteness/separation/bornology buckets do not apply.
These bounded searches do not assert global absence from Mathlib.

AutomationNegative.lean imports Roth.Index, so the target and no named failed trial is
available. Distinct anonymous examples test grind, aesop, exact?, apply?, positivity,
gcongr, norm_num and field_simp/nlinarith. grind fails; aesop exhausts search; exact?
cannot close; apply? offers reciprocal-order partial proofs before the deliberately
lower10000-heartbeat bound; positivity is inapplicable; gcongr makes no progress;
norm_num leaves the rational inequality; field_simp/nlinarith leaves an inequality
without the denominator-positivity certificates. No new library equivalent is certified
by these failures. No native multi_attempt stall was repeated. CandidateFinal.lean is a
separate clean exit0 positive proof, not an expected-failure batch masquerading as proof.

Initial Candidate.lean imported the entire Mathlib umbrella and reached the90s external
capture timeout with no output; its process group was terminated/drained. The corrected
Roth.Index import succeeds. CandidateMathlibTimeout.lean retains the exact initial
Mathlib-import variant (reconstructed from the initial generation); its provenance JSON
records that the original timeout ran at Candidate.lean before the import correction. Initial BinderNegative used the old proof but Roth.Index
lacks linear_combination: that batch is retained as failed setup and does not certify
the drop-hδ trial. BinderNegativeCorrected uses the selected clean proof; its distinct
failures below are the definitive mechanical evidence.

## Every binder, generalisation and inversion

| Binder | Class/use | Compiled mechanical probe | Disposition |
|---|---|---|---|
| n : ℕ, explicit | Denominator index; cast into ℝ | remove with autoImplicit=false; replace with nonnegative real n in separate corrected positive candidate | Drop fails unknown n in dependent statement; real candidate broadens parameter domain but adds hn and changes caller shape, with no concrete extra reuse. Preserve Nat API. |
| δ : ℝ, implicit | Scalar in hypothesis/result | remove with autoImplicit=false | Unknown δ in dependent statement; retain. Concrete ℝ→abstract field considered separately below. |
| hδ : δ≤1/(n+2), explicit | Early monotone multiplication | drop | Selected proof cannot resolve hδ; retain. Already weak ≤, no strict→weak step. |

No hidden section class/universe binder appears: the actual telescope has exactly n/δ/hδ
and universe arity0. There is no point-global premise, bundled conjunction, class-parent
weakening or decidability argument. δ has no lower-bound premise to remove. Dropping hδ
is mathematically invalid: n=0,δ=1 gives1.5<1, false; a positive compiled counterexample
is included in the final auxiliary checks.

GenericCandidate initially failed because nlinarith only did not receive hn explicitly;
GenericCandidateCorrected adds hn to that input list and exits0. This successful real
parameter-domain candidate is a diagnostic, not an automatically recommended
production API: n indexes the enclosing Nat induction and the sole caller uses Nat n.
An abstract ordered field would likewise require new type/class binders and a different
private API without any extra concrete use. These are unsupported scope expansions,
not unfinished recommended changes. No mathematical maximality claim is made.

Literature search: n/a, private declaration, explicitly exempt by cleanup§2.6d. The
mechanical/generalisation/inversion checks still apply. Inversion has no named concrete
object: the statement already is a scalar reciprocal inequality. It does not unfold Θ,
a construction or a witness and then forget it; Nat nonnegativity supplies denominator
positivity. No additional abstract-witness helper or public API is justified.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: none |
| 1.3 rw/exact | Original final rw/exact replaced by direct nlinarith input; no adjacent pair remains |
| 1.4 simp/exact | n/a: no such pair |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor | n/a: no conjunction |
| 1.7 apply/exact | n/a: apply opens nontrivial scalar inequality; no immediately following exact |
| 1.8 contradiction | n/a: none |
| 1.9 eta | n/a: no lambda |
| 1.10 single-use have | Inline original h3 structurally; candidate forwarding hP/hpos both inline in final proof; positivity hN/hN2 have proof content |
| 1.11 refine/fun | n/a: no introduction chain |
| 1.12 show | n/a: none |
| 1.13 projections | n/a: no bundled have projections |
| 1.14 merge rw | Original rewrites disappear; none remain |
| 1.15 terminal simp | Terminal simpa only disappears with calc; final no simp |
| 1.16 nonterminal simp | n/a: none |
| 1.17 dot notation | .trans_lt and .2 already direct |
| 1.18 trailing parentheses | Grouping protects elaboration of chained application; no trailing by/function wrapper |
| 1.19 push Not | n/a: none |
| 1.20 exists inline | n/a: no existential |
| 2.1 grind | Actual anonymous whole-goal probe fails |
| 2.2 before grind | n/a: selected proof has no grind |
| 2.3 simpa | Calc/simpa eliminated by early monotone transfer |
| 2.4 fun_prop | n/a: scalar inequality, no function-property goal |
| 2.5 positivity | Used for both denominators and multiplier; whole-goal probe correctly inapplicable |
| 2.6 gcongr | Whole-goal makes no progress; targeted mul_le_mul_of_nonneg_right transfer is direct |
| 2.7 lia/omega | n/a: no Nat/Int arithmetic subgoal; inequality is real rational/nonlinear |
| 2.8 aesop | Actual exhaustive-search failure |
| 2.9 norm_num/cast | Actual norm_num leaves goal; genuine Nat→Real casts retained |
| 2.10 decide | n/a: arbitrary δ, not finite computation |
| 2.11 field_simp/ring | Original identity ring eliminated; actual whole-goal field_simp/nlinarith lacks sign data; selected reciprocal cancellation API supplies it explicitly |
| 2.12 linear_combination | Original h1 linear_combination was useful; h2 ring now eliminated wholesale by polynomial certificate search, no final ring identity remains |
| 2.13 wlog | n/a: no symmetric cases |
| 2.14 calc | Entire original calc collapsed to .trans_lt followed by scalar estimate |
| 2.15 parallel goals | n/a: no similar multiple goals |
| 3.1 erw | n/a: none |
| 3.2 legacy function tactics | n/a: none |
| 3.3 omega/lia | n/a: no integer arithmetic tactic |
| 3.4 rcases/rfl | n/a: none |
| 3.5 attributes | One-off scalar induction estimate, not a canonical simp/grind rewrite; no new attribute |
| 3.6 simp_all | n/a: none |
| 3.7 limits | No production limit/trace/scaffolding introduced |

Step-back reflection: blind automation needs denominator signs and the strict square
certificate. The short selected proof exposes precisely those inputs. It avoids a new
single-use generic helper and retains a clear monotonicity/strictness separation. The
available reciprocal-order lemmas do not directly establish the strict perturbed bound.

## Packing and inequality artifacts

Signature widths are Unicode codepoints; the next token is the complete conclusion.

| Signature line | Width | Next item width | Arithmetic | Action |
|---|---:|---:|---|---|
| 759 | 88 | 57 | 88+1+57=146>100 | ok |
| 760 | 61 | none | final signature line | ok |

The fresh FIRST verifier prints the actual effective type at format.width100:
`∀ (n : ℕ) {δ : ℝ}, δ ≤ 1 / (↑n + 1 + 1) → δ * (1 + 1 / (↑n + 1 + 1)) < 1 / (↑n + 1)`.

| Reverse occurrence | Location | Rewrite | Rename |
|---|---|---|---|
| none | whole signature/all hypotheses | no ≥/> | no _ge_/_gt_ |

Counts: ≤1, <1, ≥0, >0. Final proof6 lines, maximum target width88,
positivity subproofs1 line each, no branch>10. packing-inequality.json records all data.

## Independent and actual semantic verification

FirstIndependent.lean starts with the ENTIRE immutable FIRST batch1 file, byte-identical
SHA0fbc16d1f06bbfe114d42a5c8f5fb2aee7263263b61ffc3dc8465bff941d1a54,
including its original namespace/import/context, no sections/classes/universes. It also
retains byte-identically the preceding FirstIndependent13.lean, so the prior scaled15→13
recovery and precise retained metadata checks are not lost. Only an appended delta check
is new. Independent FIRST proof is separate from the explicit current-helper adapter.

Fresh first-independent-final exits0 and locates actual private
`_private.Roth.Theta.0.Roth.theta_delta_succ_lt_aux`. It verifies original/current/adapter
universe arity0, exact full n/δ/hδ order/types/names/BinderInfo and conclusion, actual
opaque values via value! true at their declared types, and only propext/Classical.choice/
Quot.sound. The original full proof does not cite the current target or public Θ_lt.
All three FIRST batch files and original success logs/statuses are unchanged, verified
in first-immutability.json; no immutable evidence file is overwritten.

ActualSemantics.lean is byte-identical to the supplied ActualSemanticsFinal13.lean.
immutable-original-blocks.json freshly verifies the literal original Index72cfbff9… and
Theta355a5330… blocks at inherited raw byte offsets. Fresh actual-semantics-final exits0:
ENTIRE immutable original2b MainLemma proof and all copied auxiliaries, exact old Θ
adapter, actual updated Root Θ_lt/main_lemma opaque values and standard axioms, positive
actual Root.main_lemma→Root.Θ_lt dependency, publicΘ9 telescope and scaled13 assertion
all pass. Actual production deleted finite-option wrapper remains absent. Both modules
were rebuilt before actual Root queries; no stale MainLemma olean is accepted.

Inspection found that this inherited scaffold's updated caller check was the actual Root
body, without a separately copied updated caller namespace. This audit supplements that
historical evidence with an ENTIRE current MainLemma copy under Theta35CallerUpdated,
including all its own declarations/proofs and no imported Root.main_lemma use. The
augmented scaffold preserves the complete prior scaffold byte-for-byte as a prefix and
appends the current body plus metadata/value/axiom/dependency checks. Its final fresh
verification is recorded below. This is scratch evidence only, no production scope change.

Fresh corrected mechanical probes: BinderNegativeCorrected.lean exits1 with expected
unknown n/δ in dependent signatures and unknown hδ at the early multiplication step.
The corrected batch has no unknown tactic. AuxiliaryPositive.lean exits0, verifies the
n=0,δ=1 counterexample to dropping hδ, supplies an explicit negative-δ example, and
resolves every external name used by the selected proof via #check.
GenericCandidateCorrected.lean exits0 for any real n≥0 after explicitly supplying hn
to nlinarith only; that broader diagnostic is not adopted as a new private API.

Fresh UpdatedCallerIndependent.lean exits0 and independently elaborates the entire
current MainLemma body plus all its own copied definitions/private proofs, checking all
copied opaque values/standard axioms, full actual main_lemma type, positive direct
Root.Θ_lt dependency and absence of Root.main_lemma self-use. The final augmented
scaffold additionally compares every effective actual binder name/BinderInfo/order/type
and conclusion and rejects any direct imported private Root MainLemma helper reference.

Source-inventory.json reconstructs the exact baseline by restoring only this target
proof; equality passes. Target signature is byte-identical. MainLemma/Main are unchanged;
no definitions/public documentation/public hypotheses/caller proof changed. Introduced0,
deleted0 helpers. The pre-existing finite-option wrapper deletion remains inherited.

## Remaining owner scope

This helper receives no original count credit. Counts remain215/264, Theta34/35 until the
owner's original35 publication gates. All eleven dedicated helper audits, cumulative29
recovery/all actual values, full build then separate LeanEval remain owner gates.
Existing unrelated whole-source budget failures in sum_max_sub_le_index_det,
index_separated_mul_le_aux, index_det_le, index_numeric_bound_aux, index_le_lem6,
lem7_Φ_bound and lem7_numeric, plus the earlier positive-quadratic sample, remain a
separate final repair queue. Pending base/succ/largeδ helper failed pairs likewise retain
their own fresh-audit queues. The old phi988.865/1013.946 pair remains historical failed
evidence superseded only by its own audit's disposition. No whole-file timing PASS is
claimed here, and MainLemma's actual main_lemma finite timing remains unmeasured.

GenericFieldCandidate.lean also exits0 over a universe-polymorphic K with Field,
LinearOrder and IsStrictOrderedRing, retaining Nat n. Thus the scalar mathematics does
extend beyond ℝ; the compiled proof establishes that fact rather than assuming it.
Production remains the exact private Nat/Real induction API: no caller needs another
field, and introducing unused extra type/class parameters adds an unsupported API here.
This candidate is assessed and deliberately not recommended, not a pending required fix.

ActualSemanticsAugmented.lean fresh exit0 (92.739s) retains the full prior semantic
scaffold as a byte-identical prefix and appends the ENTIRE current MainLemma copy.
Its exact actual telescope has26 binders, including q/hq0/hq1/h32/h33/h/hh, retaining
ordinary names/order/BinderInfo/types/conclusion. All copied values have standard axioms,
no direct imported Root.main_lemma or private Root MainLemma helper is used, and the
copied main_lemma has a positive direct Root.Θ_lt dependency. Actual Root checks and
complete independent original proof remain present and pass. The standalone prior
updated-copy check also passed35.760s; augmented success is the stronger final evidence.

Fresh complete unfiltered native-theta-final.json/native-mainlemma-final.json have
success=true, partial=false, timed_out=false, zero errors and exactly8/3 existing warnings.
Theta warnings: header at1; hr at93; hB/hr at101; hB at109; hr at129/252; hq at547.
The exact raw messages/locations are authoritative in JSON. MainLemma's protected
existing warning hypotheses are retained. No warning is masked or filtered.

Before final actual profiling, every recorded normal request PID was checked absent;
all normal statuses were drained and both native requests completed. pre-profile-drain.json
records pending[] and the exact final source SHA. Timing commands use default Lean
limits, --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0, and an external420s
capture window. This is not a Lean heartbeat/recursion limit increase.

The independent caller copies also receive exact whole-body byte verification:
whole-original-mainlemma-bytes.json compares `git show 2b64544…:Roth/MainLemma.lean`
(read-only Git access) with the ENTIRE transformed original namespace in the augmented
scaffold, changing only namespace and inserting the old-Θ alias. Exact containment passes;
original full-source SHAa3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8.
whole-updated-mainlemma-bytes.json likewise checks the ENTIRE current body under its new
namespace, current full-source SHAca9099ad…; exact containment passes. It also verifies
that the entire old full scaffold SHA0eec8ba2… is the augmented file's literal prefix.
This supplements independent compilation with byte evidence, rather than header-only
comparison. These files retain strict UTF8 raw offsets of each whole body.


## Final actual profile and gates

Fresh actual whole-source capture(s) elaborate all52 source declarations with one actual
owned proof anchor each, exit0 and no timeout; strict UTF8 raw logs and disjoint outer
command+async proof/addDecl/linter rows are retained. Nested kernel/macro rows are not
added twice. Each table records exact source/raw SHA and raw byte offsets; strict slices
and their SHA are in profile-*-strict-slices.json. No third cherry-picked run is used.

| Declaration | Fresh run | Disjoint total ms |
|---|---|---:|
| theta_delta_succ_lt_aux | first | 595.275 |
| theta_phi_lt_aux | first | 572.808 |
| Θ_lt | first | 276.360 |

The target595.275ms is higher than its inherited415.183ms baseline; the change is a
proof simplification16→6 lines, not a speed-improvement claim. Direct phi572.808ms and
publicΘ276.360ms are close to the inherited575.334/282.723ms. All scoped values are
below750ms, so no repeat is required. Any first-run value≥750ms has its required same-source
repeat above. These are actual source declarations, not import-only theorem invocations.
No whole-file budget PASS follows: unrelated >1000ms rows remain visible in the unfiltered
all52 table and belong to the separate mandatory owner repair queue. No new MainLemma
finite main_lemma timing is claimed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | lake build Roth.Theta exit0,35.333s; then lake build Roth.MainLemma exit0,49.867s; build-*-final JSON/logs |
| definition_protected | PASS | Only target proof changed; baseline reconstruction/source-inventory equality |
| theorem_statement_protected | PASS | Target signature byte-identical; exact FIRST/current/adapter and old/public/current caller telescopes |
| structure_gate | PASS | Six lines, no branch/subproof>10, no conjunction |
| naming_gate | PASS | Mathematical snake_case/private _aux, no forbidden patterns |
| line_packing_gate | PASS | Both measured signature rows justified |
| inequality_orientation_gate | PASS | Required scan, no reversed inequalities |
| standard_axioms/opaque_values | PASS | FIRST, actual, adapter, full old/current caller and all copied declarations; value! true |
| native_diagnostics | PASS | Complete unfiltered final native8/3 warnings,0errors; no timeout/partial |
| cumulative caller semantics | PASS | Whole independent original2b/current MainLemma, actual Root dependency and all26 binders; modules rebuilt first |
| scoped performance | PASS | Actual whole-source declaration anchors and required repeats above |
| full project/LeanEval | OWNER PENDING | Full build then separate LeanEval belongs to owner after all helper audits |

Built-in simplify/buzz invocation tools are not exposed in this host. Their scoped work
was performed directly: holistic reuse/quality/efficiency review found no additional
supported change, and real uncontended profile/trace gates above supply the buzz evidence.
No claim is made that an unavailable tool was invoked.

## Required eleven-step checklist

- [✓] Step1: mandatory references read.
- [✓] Step2: every24 audit item has concrete disposition.
- [✓] Step2.5: all five actual Mathlib search methods and clean generic-route trials.
- [✓] Step2.6: every effective binder drop probe, real/abstract-field probes, literature exemption/inversion.
- [✓] Step2.7: complete measured signature packing table.
- [✓] Step2.8: complete reverse-inequality occurrence table.
- [✓] Step3: all42 golfing rules have statuses.
- [✓] Step4: whole-proof strategy/reuse reflection and selected clean proof.
- [✓] Step5a: fresh complete unfiltered native diagnostics.
- [✓] Step5b: diff/protection/semantic/axiom/build/performance gates with artifacts.
- [✓] Step6a: no renames needed; shared queue untouched by scope.

Before16 proof lines, after6, saved10. No helper introduced/deleted, no caller edits,
no Git mutation, no original-count credit and no publication. All normal/native requests
are drained with pending[]. Source authority is revoked at this handoff; no further source
edits will be made by this worker. Exact hashes and every artifact SHA are in final-freeze.json.
