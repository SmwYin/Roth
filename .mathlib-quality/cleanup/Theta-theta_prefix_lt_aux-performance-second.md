# SECOND performance repair: `Roth.theta_prefix_lt_aux`

This dedicated revisit has zero original/helper audit credit. Counts remain216/264,
Theta35/35,9/14 files. Only this private proof changes; no new helper, contract, public
API, caller, definition, import, comment or pin changes. Entire private theta_phi_lt_aux
is byte-identical. All earlier reports and all16 FIRST evidence paths remain immutable.
Report/evidence directory: `/private/tmp/theta-prefix-second-performance/`.

Both Lean/mathlib-quality skills, full cleanup worker workflow, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, buzz workflow,
profiling and relevant style/naming sections were read. No model change or delegation.

## Baseline doctor and actual failure diagnosis

Owner baseline full build86.052s THEN separate LeanEval40.867s passed on published
HEAD6effbcd04f9913e9916f61abc5a530751ee2c30f, exact Theta70465cb863f51a834bd0bf203bc14776e7492270ad4c345536d8fa8a06cc7b25
(`/private/tmp/roth-theta-p08-builds.json`). Reuse the preceding identical-source complete
native responses in theta-lem7numeric-performance-v2 as baseline doctor. Optional cache
and standalone linter are not repeated. Fresh final module/native gates are below.

Mandatory trigger: actual1047.277ms on2760ef227eb2d729381057ad02c2a0ac54c3fdc49e99a3a5a22c025b3fb6c145;
repeat721.307ms does not discharge that failure. Latest unchanged baseline879.331/858.176ms
are incidental history, not acceptance. Earlier first repair757.698/767.127ms and earlier
c8 failures remain preserved in all-historical-prefix-rows.json with source/raw/table,
strict UTF8 byte offsets, disjoint timing rows and strict-slice hashes. The complete
historical inventory additionally verifies all38 preexisting historical prefix timing captures,
raw SHA256s and matching exact source snapshots in complete-historical-prefix-inventory.json;
all five historical ≥1000ms rows remain explicit history, never erased by later samples.

The actual failing raw trace identifies numerator positivity171.605ms, cast-product
positivity107.893ms and ratio calculation166.152ms (nested, NONADDITIVE diagnostic rows).
The selected repair gives the elaborator nonnegative factor certificates directly and
uses `mul_left_comm` for the exact permutation. It keeps the already linear numerator
comparison and the measured terminal `simpa only [mul_assoc, Fin.castSucc_zero]` exception.
No helper moves cost elsewhere. Candidate compiled exit0 before the scoped source patch.

| Taxonomy cause | Actual disposition |
|---|---|
|1 instance synthesis|No dominant repeated instance-search evidence; no new instance.|
|2 fat simp|Existing measured terminal exception retained; hCeq is not the failed dominant node.|
|3 defeq|Coercion-heavy positivity normalization contributes; direct typed certificates avoid search.|
|4 heavy automation|Primary: two positivity searches and ring for a direct permutation; replaced.|
|5 mvar churn|No broad independent culprit; hn fixes its real-valued expected type.|
|6 coercions|Existing push_cast crossings retained; direct Nat.cast_nonneg supplies normalized product.|
|7 duplicated subterms|hn is used twice to share the numerator-factor certificate; no new declaration.|
|8 kernel/compiler|No independent dominant replay/compiler culprit; final disjoint accounting retains them.|

## All24 fresh audit dispositions

| # | Item | Concrete disposition |
|---|---|---|
| 1 | Lint | Baseline inherits the identical published-source complete native responses (eight Theta/three MainLemma warnings); fresh complete final responses are required below. No warning at this helper. |
| 2 | Have scan | hr0/hCeq/h2 contain real proof content. New hn is a direct nonnegative-addition term used twice in the numerator certificate, so it is retained rather than duplicated. No by-free single-use forwarding have. |
| 3 | Options | No production per-declaration option, raised limit, attribute or diagnostic scaffolding. Only scratch whole-goal automation lowers maxHeartbeats to 10000. |
| 4 | Simp | hCeq ends with unsqueezed simp [Nat.cast_mul]. Actual unsqueezed terminal simpa [mul_assoc] compiled but caused a508.747ms hotspot and1409.941ms full target regression on f23. Restore terminal simpa only [mul_assoc, Fin.castSucc_zero] as the measured performance exception explicitly permitted by profiling.md; raw/source/trace preserved. |
| 5 | Naming | theta_prefix_lt_aux describes the strict Theta bound on a prefix, uses snake_case/private _aux, and matches no numbered auxiliary/scheme/forbidden-abbreviation pattern. No rename. |
| 6 | Packing | Every one of fourteen current signature lines measured in packing.json; all complete-next-item sums exceed100. The existing signature break separates the longer localized hanti from hrlast. No proof line exceeds100. |
| 7 | By | All := by occur on the preceding statement line; inline by certificates are likewise attached. No standalone by. |
| 8 | Format | Two-space proof indentation, no empty proof lines or tactic semicolon chains. Existing finite-index lambdas retain ↦. |
| 9 | Comments | No target narrative comments existed; none removed. Sole necessary caller's one-variable/prefix/combine comments and every unrelated comment preserved byte-for-byte. |
| 10 | Docstring | Private helper correctly has no docstring; public and module documentation untouched. |
| 11 | Visibility | Private auxiliary, sole direct production consumer theta_phi_lt_aux. No external API surface added. |
| 12 | Structure | Thirty proof lines, ratio branch eight, remaining branches/subproofs at most five. No statement conjunction or trivial existential. No new helper needed. Public Θ_lt remains within15. |
| 13 | Mathlib | All five search methods freshly executed, plus fresh exact-CURRENT-prefix anonymous generic-route trials below. An independent exit0 environment check proves the audited helper/later Root Θ_lt absent. The earlier import Roth.Theta batch is superseded/contaminated and excluded from search evidence. Generic scalar components remain used directly; this substantive Θ induction transport is retained. |
| 14 | Junk def | n/a: theorem, no data definition or custom predicate. |
| 15 | Exists | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | n/a: neither tactic appears. |
| 17 | Negation | n/a: no push_neg/by_contra; no negation normalization required. |
| 18 | Generalise | All eighteen current effective binders freshly drop-tested; FIRST originals remain independently verified; strict/weak numerical and point-local candidates compiled. Retain the already localized minimum premise, exact immutable-FIRST adapter, and current-type assertion without further weakening. Details below. |
| 19 | Inequality | Sixteen signature inequality occurrences use < or ≤. No reversed ≥/>; name contains no _ge_/_gt_. Per-occurrence artifact below. |
| 20 | Normal form | Finite prefix/scaled exponent transport uses the established Θ convention and ordinary smaller-side-left inequalities. No alternate custom canonical predicate. |
| 21 | Syntactic generality | Localized last-minimum premise is directly supplied by fun j ↦ hanti (Fin.le_last j) at the sole consumer; all other arguments and IH convention stay identical. |
| 22 | Import fanout | n/a: imports unchanged. |
| 23 | Casts | New (0 : ℝ) pins hn to the target ordered field; n is genuinely cast from Nat. The existing α:=ℝ in the linear numerator certificate and remaining Nat casts bridge actual domains. No redundant casts added. |
| 24 | Instances | No universe, typeclass or decidability binder and no new instance. Both original/current effective telescopes contain precisely eighteen ordinary/implicit binders. |


## Five actual searches and clean generic routes

All five methods were actually executed afresh. Initial bounded shell fallback attempts
returned DNS errors; their raw responses/stderr are preserved. Corrected native tool
searches succeed: Lean-Finder returns five unrelated additive-combinatorial Roth-number
results; Loogle returns eight Nat/Int division bounds; LeanSearch returns generic
mul_nonneg and related ordered-product components. Full native responses are
native-search-{leanfinder,loogle,leansearch}.json. Name-pattern search finds
mul_left_comm in Algebra.Group.Basic;
its index is unavailable, so no indexed absence claim. Full-name rg has exit1 and empty
untruncated output; component-source rg finds the direct order/algebra lemmas. Common-equivalents discrete/finiteness/separation/bornology buckets do not describe this
Theta induction transport. Auxiliary variants div_le_div₀, mul_le_mul_of_nonneg_left/right,
mul_nonneg, add_nonneg and mul_left_comm are inspected through actual source/search/type checks.

| Method | Actual query | Fresh result |
|---|---|---|
|A Lean-Finder|Roth theta prefix restriction scaled natural multiplicities induction bound|Five unrelated additive-combinatorial Roth-number results|
|B Loogle|_ / _ ≤ _ / _|Eight generic Nat/Int division inequalities|
|C LeanSearch|nonnegative product of two nonnegative real numbers|Generic mul_nonneg and related ordered-product components|
|D source rg|theta_prefix_lt_aux and component declaration regex|Empty full-name output; direct component source matches|
|E local name|mul_left_comm|Four source matches, index unavailable (no indexed absence claim)|

Every
new identifier is independently #checked in positive PrefixAbsence and verified again
in the full semantic scaffold. Scalar components use mathlib directly. The substantive
Theta prefix/IH transport remains; it is not a one-to-three-call generic wrapper.

Automation.lean uses eleven anonymous examples against the literal current source
prefix ending BEFORE this target, with default maxErrors and conservative10000 scratch
heartbeats. Fresh separate PrefixAbsence.lean succeeds with actual private suffix
absence, later private/public absence AND present preceding private/public controls.
No import-self/named failed theorem contamination. Each trial is mapped
individually to source ranges in automation-results.json. apply? stops with bounded
partial suggestions and an incomplete-proof warning (Lean internally inserts sorry);
it is explicitly unsuccessful search evidence, never positive proof evidence. The
initial parser expected an error for every tactic, stopped on this warning, and was
corrected to retain that distinct partial outcome. The unmodified raw is preserved.
Failed/incomplete search files never certify
positive semantics/axioms. Known stalled multi_attempt is not retried unboundedly.

## Every effective binder, generality and inversion

Fresh Binders0..4 files drop-test every effective binder with autoImplicit=false and the
FINAL selected proof. Four additional candidates test0<δ→0≤δ,1≤l→0≤l,1≤M→0≤M and
3≤last→1≤last. Each actual failure is mapped to its own range; mechanical failure does
not prove logical necessity. The exact immutable FIRST Antitone proof is independently
re-elaborated in its entire successful context with all18 metadata, and its old-contract
adapter is preserved. The current weaker minimum-bound contract remains unchanged.

| Binder | Class | Use | Compiled candidates | Disposition |
|---|---|---|---|---|
| n | implicit ℕ | Finite dimensions and numerical exponent | individual drop | Unknown n in dependent types; retain Nat dimension. |
| δ | implicit ℝ | ratio and denominator | individual drop | Unknown δ; no generic field widening with project Θ/Real.log/rpow fixed. |
| ε | implicit ℝ | IH ratio/rpow and bound | individual drop | Unknown ε; same Real-valued construction restriction. |
| M | implicit ℝ | Θ argument and scale comparison | individual drop | Unknown M in dependent statement. |
| hδ0 | explicit proposition | strict lower denominator in div_le_div₀ | drop;0<δ→0≤δ | Both fail; retained strict positivity. |
| hδε | explicit proposition | quotient order and scaled ratio | drop | Unknown hδε in both certificates; already weak ≤. |
| r | implicit Fin(n+2)→ℕ | all weights and prefix | individual drop | Unknown r; finite natural multiplicities are part of Θ. |
| q | implicit Fin(n+2)→ℕ | logarithmic denominators and prefix | individual drop | Unknown q; established Θ denominator domain preserved. |
| hanti | explicit proposition | last-weight minimum at two uses | drop; point-localize to ∀j,rlast≤rj | Drop fails; prior point-local candidate compiled; existing localization retained without further weakening. |
| hrlast | explicit proposition | positivity and IH last lower bound | drop;3≤last→1≤last | Both mechanical proofs fail; retain numerical threshold3. |
| hratio | explicit proposition | prefix successor-ratio certificate | drop | Unknown hratio; already point-local finite-index family/weak inequality. |
| hq1 | explicit proposition | log bound after quotient comparison | drop | Unknown hq1; already weak ≤. |
| hqr | explicit proposition | weighted-log ordering for every prefix index | drop | Unknown hqr; every prefix point is used, no single-point replacement supplies entire family. |
| l | implicit ℕ | scaled natural multiplicities | individual drop | Unknown l in statement; replacing ℕ by ℝ changes Θ domain. |
| hl | explicit proposition | Nat.mul_pos and one≤cast-l | drop;1≤l→0≤l | Both fail; retain positive integer scale. |
| hM1 | explicit proposition | Θ_mono lower-scale hypothesis | drop;1≤M→0≤M | Both fail; Θ_mono requires1≤M. |
| hM | explicit proposition | Θ_mono upper-scale bound | drop | Unknown hM; already weak ≤. |
| ih | explicit higher-order proposition | lower-dimensional Θ bound | drop | Unknown ih; all inner Fin/weight/log premises transport substantively. |



Literature: n/a, private auxiliary exemption under cleanup§2.6d; no new public result.
Inversion: Θ is used through Θ_mono and the higher-order IH, never unfolded away.
Generalizing the construction would duplicate its current axioms without an independently
supported reusable object; no API change is recommended. Ordinary names/order/BinderInfo,
universes and conclusion remain exact. All retained/deleted helper audits are preserved.

## All42 fresh golfing dispositions

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | rw hCeq precedes an induction application with multiple certificates, not a closing exact; no rwa pair. |
| 1.4 | Final cast/product transfer already uses simpa using; preserve composition. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: no constructor chain. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction branch. |
| 1.9 | Finite-index lambdas precompose q/r and multiply by l; they are not eta wrappers. hr0 lambda proves positivity and cannot eta-reduce. |
| 1.10 | Already inlined in the inherited release: inner positivity certificate and by-free ratio certificate. Final hr0/hCeq/h2 retain substantive proof content; new hn is used twice. No single-use forwarding have remains. |
| 1.11 | n/a: no apply followed by intro. |
| 1.12 | n/a: no redundant show. |
| 1.13 | n/a: no conjunction projection have. |
| 1.14 | n/a: only one rw hCeq, separated from cast normalization. |
| 1.15 | Historical TRIED/REJECTED by actual measurement: unsqueezed terminal simpa [mul_assoc]508.747ms; target1409.941ms. Retain original simpa only [mul_assoc, Fin.castSucc_zero] as a documented measured performance exception. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Already uses .trans/.trans_lt composition; keep. |
| 1.18 | Remaining parentheses delimit arguments before additional arguments or .trans; no avoidable trailing-parenthesis block. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no trivial existential helper. |
| 2.1 | Actual anonymous whole-proof grind fails under conservative scratch cap. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 2.2 | n/a: no selected grind block with preceding tactics. |
| 2.3 | Final normalized weighted-log transfer remains one simpa using application. The preserved historical unsqueezed complete candidate compiled but regressed actual performance; selected version uses the measured squeezed exception. |
| 2.4 | n/a: no analytic regularity/property goal. |
| 2.5 | Actual whole-goal positivity fails. Replace the two traced heavy positivity searches with direct mul_nonneg/add_nonneg/Nat.cast_nonneg certificates. This addresses measured search cost rather than hiding it behind a helper. |
| 2.6 | Fresh whole-proof gcongr fails. Retain the already narrow linarith only numerator comparison and div_le_div₀; direct positivity terms address the actual failed hotspots. |
| 2.7 | Whole-proof lia fails: real rpow/Theta/IH transfer, not a linear Nat/Int goal. Concrete 0<3 remains norm_num. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 2.8 | Actual anonymous whole-proof aesop fails; no production broad search. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 2.9 | Whole-proof norm_num leaves the induction goal; existing exact_mod_cast/norm_num certificates retained. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 2.10 | Whole-proof decide rejects free variables/noncomputable real proposition; no native_decide. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 2.11 | Actual field_simp/ring whole-proof trial leaves Theta inequality. The sole equality is multiplicative permutation without denominators. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 2.12 | No final ring/ring_nf remains: replace the multiplicative permutation by the exact mul_left_comm theorem. The previous successful linear_combination alternative is preserved as historical exploration; no fresh tactic experiment is needed once the direct library equality is selected. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | Three-row mixed ≤/= /≤ calc now uses the direct mul_left_comm permutation. Collapsing to a long transported term hides the scale/ratio argument; current .trans composition already removes two-step bound chains elsewhere. |
| 2.15 | Final induction side-goals have distinct lower-bound/ratio/log-invariant proofs; uniform automation does not apply. No duplicated goal closers to distribute. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy continuity/measurability tactic. |
| 3.3 | n/a: no omega; actual lia whole-goal trial fails as recorded in2.7. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No automation attribute: private higher-order induction transport with large parameter telescope has one explicit caller. |
| 3.6 | Actual anonymous simp_all whole-goal trial fails under conservative cap; no selected squeezed simp_all. Fresh anonymous trial uses the literal CURRENT source prefix before the target, with a separate positive absence/control compile. |
| 3.7 | Zero production limits added/raised; no profiling scaffolding or suppression. |



Step-back/simplify: direct holistic review found no further useful refactoring. The proof
applies Θ_mono then IH to the scaled prefix and provides distinct endpoint/ratio/log
certificates. All single-tactic routes failed in fresh clean anonymous trials. No exposed
built-in simplify callable exists, so this records a direct review, not an invented tool
invocation. Phase5a no further refactoring; Phase5b no rename/shared queue write.

## Measured packing, inequality and source protection

All14 signature lines are unchanged. Fresh codepoint arithmetic and full next-items are
in packing.json; current+1+next always exceeds100. Effective types are printed at
format.width100. No signature/body line exceeds100; proof28→30, longest branch8,
all branch/subproofs≤10 and target≤30. No new helper needs another audit.

| Sig line | Chars | Next width | Sum | Action |
|---|---|---|---|---|
|1|81|23|105|ok|
|2|69|41|111|ok|
|3|45|63|109|ok|
|4|67|76|144|ok|
|5|80|62|143|ok|
|6|87|13|101|ok|
|7|56|310|367|ok|
|8|63|50|114|ok|
|9|56|62|119|ok|
|10|68|58|127|ok|
|11|64|77|142|ok|
|12|83|112|196|ok|
|13|73|47|121|ok|
|14|54|—|last|ok|

| Inequality | Actual line:column | Relation | Action |
|---|---|---|---|
|1|776:64|<|canonical; unchanged|
|2|776:78|≤|canonical; unchanged|
|3|777:64|≤|canonical; unchanged|
|4|778:17|≤|canonical; unchanged|
|5|779:49|≤|canonical; unchanged|
|6|780:64|≤|canonical; unchanged|
|7|781:44|≤|canonical; unchanged|
|8|781:84|≤|canonical; unchanged|
|9|782:14|≤|canonical; unchanged|
|10|782:27|≤|canonical; unchanged|
|11|783:40|≤|canonical; unchanged|
|12|784:36|≤|canonical; unchanged|
|13|785:51|≤|canonical; unchanged|
|14|786:40|≤|canonical; unchanged|
|15|787:37|<|canonical; unchanged|
|16|788:73|<|canonical; unchanged|

static-gates.json verifies exact whole-file reconstruction by replacing only this proof,
exact signature/caller/comments, all17 source/pin paths, all16 FIRST paths and protected
report hashes. owned-proof.diff is the entire change. No source proof option, maxErrors
raise, heartbeat/recursion raise, sorry/new axiom/native_decide, attribute or scaffolding.


Corrected non-Lean driver errors are preserved in corrected-driver-errors.json: the
apply? warning classifier, unavailable Python hashlib.file_digest (replaced by verified
streaming SHA256), and sandbox-blocked global ps (replaced by tracked PID/PGID checks).
None is positive proof/timing evidence; no failed raw/log/source is overwritten.
## Fresh independent semantics, opaque values and native diagnostics

The entire latest640-check semantic input (SHAa5eec7feb0e2019010872f3a346f360452b7c2eff1ed6c421cb30233c298126e)
is an exact unchanged byte prefix of ActualSemanticsAugmented.lean. The appended independent
CURRENT namespace re-elaborates the complete current target and ENTIRE current private phi
proof in their source context. It checks exact full effective types/universes, every retained
name/order/BinderInfo/conclusion, actual opaque values via value! true, inferred types,
standard axioms only, NONSELF proofs and positive actual/independent target dependencies.
The preceding all29 public old-contract recoveries, five definition values, every prior
helper audit/deletion, ENTIRE original2b MainLemma and ENTIRE independent current MainLemma
proof blocks execute afresh. Actual built Root Θ_lt/main_lemma values/types/axioms and
dependencies are checked by that unchanged cumulative input. No adapter invokes the target
to stand in for an independent proof.

FirstIndependent.lean starts with the ENTIRE exact immutable successful FIRST batch2,
SHA8a7cb0fd8b366f0f251272bf6e9a16cfa2dc339b9147899b74f876d37c1b54a6.
Its full original18-parameter Antitone proof and exact old adapter are re-elaborated;
current minimum-bound metadata are checked independently. Historical success log SHA
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 and success JSON
SHA32ade30842fdd9413e1f7e8bbf348fc2adcd57b2b702866ae4e15e72ff50cde2 remain unchanged.
All16 FIRST-map paths are hash-verified. No new helper or helper audit credit.

| Sequential actual command | Exit | Seconds | PASS markers |
|---|---|---|---|
|lake build Roth.Theta|0|36.807|—|
|lake build Roth.MainLemma|0|39.526|—|
|lake env lean FirstIndependent.lean|0|41.886|62|
|lake env lean ActualSemanticsAugmented.lean|0|230.059|687|

Every successful log is clean of error/PANIC/sorryAx. Failed automation and its internal
incomplete-proof warnings are separate and never certify semantics or axioms.

| Whole canonical block | Byte start | Byte end | SHA256 |
|---|---|---|---|
|1|1414|15125|72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f|
|2|16628|68797|355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da|
|3|70475|105941|96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a|
|4|117380|152930|859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41|

Fresh complete UNFILTERED native responses are native-theta-final.json and
native-mainlemma-final.json: success=true, partial=false, timed_out=false,0errors and
no failed dependencies. Every full warning is preserved in those raw JSONs. Summary:

| Module | Line | Warning |
|---|---|---|
|theta|1|Copyright too short; full warning retained in raw JSON|
|theta|93|Variable name `hr` is not explicitly referenced.|
|theta|101|Variable name `hB` is not explicitly referenced.|
|theta|101|Variable name `hr` is not explicitly referenced.|
|theta|109|Variable name `hB` is not explicitly referenced.|
|theta|129|Variable name `hr` is not explicitly referenced.|
|theta|252|Variable name `hr` is not explicitly referenced.|
|theta|554|Variable name `hq` is not explicitly referenced.|
|mainlemma|1|Copyright too short; full warning retained in raw JSON|
|mainlemma|149|Variable name `hδ0` is not explicitly referenced.|
|mainlemma|149|Variable name `hr₁` is not explicitly referenced.|

All existing warnings are retained. Header and explicit hq/D–F choices follow user decisions.
The unused hr in index_le_Θ and Θ_unique_le are technical retentions reserved for fresh
final review, not user vetoes; MainLemma hδ0/hr₁ remain for its later dedicated file audit.

## Actual production profiles and scoped buzz result

All ordinary/native requests are drained before each uncontended actual whole-Theta capture.
Command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`.
The external420s window changes no Lean limit. Both runs have exit0 with complete output.
All50 source declarations have exact actual anchors, no invalid UTF8 or replacement
sequences. Strict source/raw hashes/offsets and target/caller slices are retained.
Accounting sums only disjoint outer command and associated async proof/addDecl/compiler/
linter rows; nested macro/kernel/tactic rows are diagnostic, never double-counted.

| Run | Declaration | Conservative ms |
|---|---|---|
|final-first|theta_prefix_lt_aux|718.309|
|final-first|theta_phi_lt_aux|731.235|
|final-first|theta_lt_succ_aux|695.026|
|final-first|Θ_lt|363.595|
|final-repeat|theta_prefix_lt_aux|758.076|
|final-repeat|theta_phi_lt_aux|754.888|
|final-repeat|theta_lt_succ_aux|706.206|
|final-repeat|Θ_lt|382.420|

Both scope declarations are under1000ms on the identical final source pair. Both first scoped rows are below750ms, so the threshold did not require a repeat.
The started second capture is an additional same-source confirmation, preserved completely;
its outcome remains actionable. No further unchanged-source sample is taken.
The actual1047.277ms failure and its later721.307ms sample remain explicit immutable
history. This is a concrete changed-proof repair with fresh acceptance, not resampling.
Heartbeat cross-check:2886→2463 (423 fewer,14.66%). No instrumentation ships in source.
Buzz outcome: FIXED for the scoped SECOND prefix revisit; no helper hides cost.

All older published repairs retain their reports. SECOND sum_max_sub_le_index_det remains
a separate mandatory repair queue (original1004.335/809.108, latest previous1131.027/1065.136);
no incidental sample clears it. Every fresh≥1000ms row, including unrelated failures,
has exact strict UTF8 slices and disjoint totals in profile-final-*-all-failures-strict-slices.json.
Fresh queue additions are recorded in profile-final-*-remaining-queue.json for the owner.
MainLemma actual main_lemma caller timing remains UNMEASURED after its previous bounded
cutoff; successful ordinary semantics/build/native do not substitute. No whole-file or
MainLemma timing PASS is claimed. Final filewide cumulative/allactual/profile gates remain owner work.

## Gate status and all11 workflow steps

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|PASS|Actual sequential Theta THEN MainLemma commands/statuses above|
|definition_protected|PASS|Exact one-proof reconstruction, all other source bytes unchanged|
|theorem_statement_protected|PASS|Exact full effective type/metadata and immutable FIRST adapter|
|structure_gate|PASS|30 lines, longest branch8, all branches/subproofs≤10; no helper|
|naming_gate|PASS|Descriptive snake_case private _aux; no forbidden patterns|
|line_packing_gate|PASS|All14 measured codepoint/complete-next-item rows above|
|inequality_orientation_gate|PASS|All16 occurrences canonical, zero≥/> in source signature|
|semantic/opaque/axioms/NONSELF/dependencies|PASS|Fresh FIRST and entire augmented scaffold above|
|cumulative_no_unintended_breakage|PASS|Affected modules rebuilt; all29 old public recoveries and whole independent MainLemma proofs re-executed|
|complete native diagnostics|PASS|Both complete unfiltered responses,0errors|
|scoped production performance|PASS|Final identical-source pair above, strict disjoint rows|
|source/pins/FIRST/reports/comments/scaffold|PASS|static-gates.json, full hash maps, byte-prefix/four blocks|
|owner full build THEN separate LeanEval/publication|OWNER PENDING|Not run by this worker|
|owner remaining repair/file-final cumulative/allactual sweeps|OWNER PENDING|No whole-file timing PASS|

| Step | Result |
|---|---|
|1|✓ Both skills/full required cleanup/buzz and references read|
|2|✓ All24 fresh concrete audit dispositions|
|2.5|✓ Five actual search methods; anonymous literal-prefix automation and separate positive absence|
|2.6|✓ All18 binder drops/four weakenings; immutable FIRST18; private literature exemption/inversion|
|2.7|✓ Every signature line measured|
|2.8|✓ Every inequality scanned|
|3|✓ All42 golfing-rule dispositions|
|4|✓ Direct holistic simplify/step-back review; no further recommendation|
|5a|✓ Fresh complete unfiltered native diagnostics|
|5b|✓ Actual builds/semantic/protection/performance gates|
|6a|✓ No rename or shared queue mutation|

No further scoped refactoring, new helper or deferred scoped defect. Production line delta+2;
proof28→30. Revisit credit0;216/264 originals,Theta35/35,9/14 files remain unchanged.

## Artifact map, full source/pin hashes and terminal authority release

| Evidence | Paths under /private/tmp/theta-prefix-second-performance/ |
|---|---|
|Exact source/candidate/change|baseline-Theta.lean, original-declaration.lean, candidate-declaration.lean, Candidate.lean, candidate.{log,json}, final-Theta.lean, owned-proof.diff|
|Fresh audit/search/generalization|report-draft.md, packing.json, inequalities.json, static-gates.json, native-search-*.json, lean_*.{json,stderr}, mathlib-*.{log,json}, PrefixAbsence.lean, prefix-absence.*, Automation.lean, automation-{ranges,results}.json, Binders0..4.lean, binders*-{ranges,results}.json, exploration-summary.json|
|Heartbeats|Heartbeats-{before,after}.lean, heartbeats-{before,after}.{log,json}|
|Normal semantic/build|FirstIndependent.lean, ActualSemanticsAugmented.lean, immutable-scaffold-and-blocks.json, build-{theta,mainlemma}-final.*, first-independent-final.*, actual-semantics-final.*, semantic-marker-summary-final.json|
|Native complete raw|native-{theta,mainlemma}-final.json, native-final-source-binding.json|
|Final actual profiles|actual-profile-final-{first,repeat}.{log,json}, actual-profile-final-*-table.json, profile-final-*-strict-slices.json, final-*-*-strict-slice.log|
|Every failure/remaining queue|profile-final-*-all-failures-strict-slices.json, profile-final-*-new-actionable-strict-slices.json, profile-final-*-remaining-queue.json|
|Historical failures/incidental rows|complete-historical-prefix-inventory.json (all38), all-historical-prefix-rows.json (eight dispatch-critical), history-*-prefix-strict.log; original sources/raw logs remain in their recorded paths|
|Immutability/process/freeze|all-source-pin-hashes.json (baseline), source-hashes.json (final), all-FIRST-immutable-hashes.json, protected-report-hashes.json, pre-profile-drain.json, pre-repeat-drain.json, final-process-drain.json, evidence-manifest.json, final-freeze.json|

| Final source/pin path | SHA256 |
|---|---|
|Roth.lean|6aaa74aab715cb9b6df91771ec2e7e127a39807f936e26a68fcdc026099914d2|
|Roth/Box.lean|a5d0da3d2d4ecfcb705d0c446294e393fcff048576e0bd23f67b70c06dadc827|
|Roth/CoeffNorm.lean|ee0b23cfee16cf674512a5c8f912a8030242e736db6e79fc1270be71675e67a9|
|Roth/GenWronskian.lean|5283b554baa1fcfce18f2298a0f5181cc58586f22b541dd2222745ef651b6e32|
|Roth/HasseDeriv.lean|de378f2d057787d9751044e53cace8ba8134c015d9401f503e57259ca09d0dba|
|Roth/Index.lean|30e6f151ddd2d9c344b9537d1bef87124e3f5814d2e58f3cba499a7e1ea6c939|
|Roth/Lattice.lean|a363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8|
|Roth/LeanEval.lean|e95c44ae19345ef1514a59ca5e8b182247e9a32aaf4b7d39f0ce57ae5ed27f56|
|Roth/Main.lean|f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069|
|Roth/MainLemma.lean|ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4|
|Roth/Separation.lean|df4193795f1618f8f5cdbd71869583fc45d20a0a45c21f4b5eaf5f824133f37a|
|Roth/Taylor.lean|31af75afd28f840ddee51978509ba63b28536aa84bba56dc047df2aa4b23fbdc|
|Roth/Theta.lean|3f9c23b83cd5bb8eaf9deb2b6d8c9182d0309464c5c76a3568c30eb1f86100ce|
|Roth/Wronskian.lean|b4f0c0db36bcbd81983f5a38c137dcefdf57bce18e12445e8241689a8abf888e|
|lean-toolchain|8733782dc070a99b312039cda424f601b80f3be6f6f512627da5ba25adc27632|
|lake-manifest.json|f3c041619f25b5f9013759113d877b6e510b91956b0d97b542fb3bae9b5f906e|
|lakefile.toml|6122f113a57760c6b0b9eb52d6f6aa0343efda1d3339534dd12db31d21788a5d|

final-freeze.json binds all17 final source/pin hashes, all16 FIRST paths, every protected
prior Theta report, all four full canonical block hashes, complete semantic/native/
profile maps, report/manifest hashes, all tracked process groups dead and pending[].
No Git, shared-log or rename-queue mutation. Every own ordinary/native request is drained.

At terminal freeze, all source/scratch/report/compiler/native authority is explicitly
REVOKED and the sole compiler/native window RELEASED to the owner. No source edit follows
freeze. Owner alone performs full build THEN separate Roth.LeanEval, cumulative/allactual
checks and exact-path stage/commit/push/clean before the next SECOND summax scope edit.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 79.459 s and 49.955 s.
Theta SHA256 `3f9c23b83cd5bb8eaf9deb2b6d8c9182d0309464c5c76a3568c30eb1f86100ce` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p09-full.log` and `/private/tmp/roth-theta-p09-leaneval.log`; machine record
`/private/tmp/roth-theta-p09-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 35 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
