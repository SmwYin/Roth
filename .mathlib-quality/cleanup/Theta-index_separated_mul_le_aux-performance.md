# Dedicated performance revisit — `Roth.index_separated_mul_le_aux`

Scope: the existing private separated-product helper belonging to original28, its unchanged direct public `index_det_le` consumer, and this report. No new helper, public/private signature, definition, instance, import, comment, or caller-proof change. Original counts remain **216/264**, Theta **35/35**, completed files **9/14** until owner file-final gates. This revisit adds **0 original declarations**. No Git, shared-log or rename-queue writes.

Published release HEAD/origin `dd482bee7c4117b489ec4e908747db4b88e6f880`; source/audit `51dc3bbfc5957ba6223f02ab148ccb6877bf49ab`. Inherited baseline Theta SHA256 `2760ef227eb2d729381057ad02c2a0ac54c3fdc49e99a3a5a22c025b3fb6c145`. Owner baseline full build78.752s THEN separate LeanEval32.808s and complete unfiltered prior Theta/MainLemma native diagnostics were green at that published source. These are inherited doctor evidence, not fresh leaf executions. The latest same-source baseline profile pair measured helper **1298.995/1133.509ms**. Both fail1000ms; a lower repeat does not erase a failure.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md and cleanup-gates.md in full; both Lean4/mathlib-quality skills, full cleanup workflow, buzz workflow, profiling taxonomy and relevant style/naming sections were consulted. Standing user authorization to implement supported recommendations governs; prior explicit hq/Theta/hB/hr/header/wrapper/domain decisions remain protected. Prior technical retention choices are assessed on their merits, never described as a user veto.

## Mathematics and actual trace diagnosis

Convert integer univariate V to a Unit-indexed multivariate polynomial V′. Its nonzero, degree and coefficient bounds establish RSet membership. Injective renaming and coefficient mapping preserve the two factors' nonzeroness. Product index adds, renaming restricts the coordinates, and the defining Θ bound at scaled weights divides each original index by l. Positive l clears the denominator; adding gives lΦ.

The latest failing actual source trace is preserved in `baseline-actual-nested-hotspots.json`: index rewrite **523.077ms**, its index_mul argument elaboration **393.282ms**, mapped-U/mapped-V nonzero terms **193.861/196.665ms**, final selected simpa **422.423ms**. These nested costs overlap and are **never added**. They corroborate the older9faa nested558.589/436.358/211.895/222.417/387.478ms diagnosis. Nine inherited whole-source samples, including every supplied failure and both latest paired samples, have exact source/raw/table hashes, UTF8 strict slices and raw byte offsets in `preserved-baselines.json`. Their original full logs/sources remain in place. Historical0cb/9faa and positive/index29 timing records remain preserved rather than overwritten.

Eight-cause review:

|Cause|Evidence and decision|
|---|---|
|1 instance synthesis|The inferred coefficient hom leaves target types open under the nested nonzero argument; pin the concrete existing hom, without a new instance or changed priority. No evidence supports global instance changes.|
|2 fat simp|Even the historically justified terminal only-list still normalizes both large index inequalities, costing422.423ms. Replace it with three direct rewrites and the existing correctly oriented division lemma.|
|3 unification/defeq|Unknown map hom metavariables in actual expected-type nodes support early concrete hom arguments. Function composition is definitionally equal and accepted directly at final exact.|
|4 heavy automation|No grind/linarith/ring in selected proof; no heavy arithmetic search to optimize.|
|5 missing expected type|Actual mapped-factor nodes explicitly show `map ?m`; concrete `Int.castRingHom ℝ` in both map_injective calls resolves that information early.|
|6 coercion churn|One retained natural→real positivity bridge; no repeated cast normalization added.|
|7 duplicate large subterms|Existing V′ binding already avoids repeating its conversion; no new binding/helper is warranted by the trace.|
|8 kernel/compiler|Associated addDecl/compiler/linter work remains in disjoint totals; nested kernel children are not double-counted or hidden.|

Implemented repair: retain typed real-map nonzero certificates hmU/hmV, prove them directly by map injectivity and map_zero, and pass explicit real rename homomorphisms to both remaining map_ne_zero_iff calls. Replace terminal normalization by `rw [lem6Φ, mul_add, add_comm]` and direct `add_le_add` using **div_le_iff₀'**, matching the scale on the left and the reversed factor order. No helper shifts the cost elsewhere. Proof now has **30 lines**, and no branch/subproof exceeds10. The first scratch attempt passed bounds in the wrong order after add_comm; `failed-order-Candidate.lean` and candidate.log/json retain that exact error. Corrected candidate-two compiles exit0. Production only received the corrected candidate.

Initial repaired-source exact-prefix heartbeat comparison (unaccepted failed-pair checkpoint): **6894 → 3132** (−54.6%), default200000 maximum unchanged, exit0 for both. Raw logs, exact prefix sources and commands: `Heartbeats-{before,after}.lean`, `heartbeats-{before,after}.{log,json,pid.json}`. These are scratch-only wrappers; none appears in production. The subsequent typed-certificate repair measures2410 heartbeats and receives separate fresh final gates below.

## Full24-item audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|No target warning in corrected prefix candidate; full unfiltered final native diagnostics and all unrelated warnings are recorded below.|
|2|HAVE SCAN|hV′0 is a typed conversion proof used in membership/nonzero; hVmem is a substantive degree/coefficient conversion; hinjV is used by nonzero/index_rename; hUΘ/hVΘ are rewritten then consumed; hlR is used twice. New hmU/hmV are single-use typed nonzero certificates deliberately retained for measured elaboration performance (3132→2410 heartbeats), rather than re-inlined into the previously measured expensive generic argument.|
|3|SET_OPTION|None in production. Lower2000 heartbeat search limits only in scratch anonymous examples; no production/profile limit raised.|
|4|SIMP|The sole terminal selected simpa was a previously measured exception. Its actual current422.423ms cost is now removed through direct APIs; no remaining helper simp or gratuitous unsqueeze.|
|5|NAMING|Describes index/product/separated variables/inequality, private snake_case `_aux`; no forbidden abbreviation, numeric scheme or inequality reversal. No rename.|
|6|PACKING|All7 signature lines measured in codepoints below, including complete dependent conclusion continuations. Signature unchanged.|
|7|BY|All := by stays at line end.|
|8|FORMAT|Two-space proof/four-space signature, Unicode mathematical lambdas, no semicolon chain, blank proof line, haveI/letI or long introduced line.|
|9|COMMENTS|No helper proof comments originally. Entire direct public caller and all3 Step comments byte-identical; no module/header/docstring changes.|
|10|DOCSTRING|Private helper has none; public documentation unchanged.|
|11|VISIBILITY|Substantive private estimate used by one same-file public proof; preserve private visibility and classic import dialect.|
|12|STRUCTURE|30≤30; hVmem6 physical lines including statement, individual branches2 lines. No >10 branch, conjunction conclusion or existential packing.|
|13|MATHLIB|Five fresh actual methods, generic-route probes and pinned #checks below. Existing index/rename/Θ/division APIs used directly; no full replacement found in bounded search.|
|14|JUNK DEF|n/a: lemma, no def/abbrev introduced. V′ is the existing local binding used in multiple conversions.|
|15|EXISTS|n/a: real inequality, no trivial existential helper.|
|16|SHOW/CHANGE|Neither used in helper.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every16 effective parameter dropped in compiled trials plus six weakenings; successful equivalents/support bound independently compiled. Full FIRST/current contract retained.|
|19|INEQUALITY|Five correctly oriented comparisons; no ≥/> or _ge_/_gt_ name. Full occurrence table below.|
|20|NORMAL FORM|RSet membership, natural degree/weights, integer coefficients and real index≤lΦ match existing interfaces; Φ expanded only for final arithmetic.|
|21|SYNTAX GENERALITY|Global coefficient bound supplied directly by actual caller; equivalent support-local formulation adds reconstruction work. No more applicable rebundling identified.|
|22|IMPORT FANOUT|n/a: no import change.|
|23|CASTS|No redundant cast added. Existing ℤ→ℝ/ℕ→ℝ bridges remain; explicit ℝ coefficient type and Unit/Option τ domain annotations on rename pin its full hom type early. These are load-bearing elaboration annotations, not identity casts. Earlier redundant innerℤ removal preserved.|
|24|INSTANCE NAME|No instance declaration/name introduced. DecidableEq omission retained, Fintype remains anonymous with exact effective telescope checked.|

## Five fresh actual search methods and clean goal probes

|Method|Query/results and action|
|---|---|
|A Lean-Finder|Weighted-order/index product, disjoint variables, rational points and coefficient bound: MvPowerSeries.weightedOrder_le/le_weightedOrder_prod and unrelated Chevalley bounds. Partial generic ingredients; not rational weighted index/Θ upper bound. search-finder.json.|
|B Loogle|`MvPolynomial.rename, _ * _`: algebra presentation/generator and Witt identities, no matching estimate. search-loogle.json.|
|C LeanSearch|Weighted order of product as sum: MvPowerSeries.weightedOrder_mul/prod and IsWeightedHomogeneous.prod; distinct codomain/weights and no rational supremum bound. search-search.json.|
|D source rg/files|Full target name and index_mul/index_rename/index_mul_left_weights, aeval_X_eq_rename, map/rename injectivity, uniqueAlgEquiv degree/coefficients and div_le_iff₀' across project/mathlib standard files. Full raw mathlib-source.log, no truncated absence search.|
|E native local|index_mul finds Roth.index_mul/index_mul_left_weights and unrelated subgroup results. Index unavailable: source-backed results only, never evidence that generated declarations are absent. search-local.json.|

Auxiliary variants: `_mul/_prod`, `_left`, rename/injective/map-ne-zero iff, uniqueAlgEquiv degree/coefficient conversion and both division orientations. Common-equivalents discrete/compact/coset/bornology buckets do not match this quantitative polynomial theorem. Generic order results are partial matches; current proof already builds directly on existing APIs. It has substantive RSet/Θ content and30 lines, not a1–3-call wrapper. No new public API or restored coefficient wrapper recommended.

Fresh literal-current-goal tests use **exact source prefix before helper**, explicit `omit [DecidableEq τ]`, anonymous `example`s and no import Roth.Theta. All eleven bounded trials (grind,simp,aesop,exact?,apply?,lia,positivity,gcongr,norm_num,decide,simp_all) produce mapped expected errors; no failed named theorem can contaminate search. Separate successful PrefixAbsence.lean asserts helper and all later callers absent, exit0 with PASS. Its first scratch version used resolving double-name quotations for absent constants and failed; `failed-quoted-absence.*` preserves it, corrected single-name quotation gate alone certifies absence. Full errors, tactic markers/ranges and results are in automation-{ranges,results}.json and Automation.lean/log. No maxErrors increase. Known stalled native multi_attempt is not repeated under the standing bounded-fallback instruction and is not counted as a search.

Pinned names: SourceSearch.lean/log exit0 checks div_le_iff₀', Int.castRingHom, map_injective/map_ne_zero_iff, rename_injective, aeval_X_eq_rename, uniqueAlgEquiv conversions and all four index/Θ APIs. The new references are the existing primed division orientation and map_zero, both compiled (#check map_zero also refreshed in v2/SourceSearch.lean). No hallucinated lemma introduced.

## Every effective parameter and mechanical generality

BindersNegative.lean contains16 exact full-proof deletion trials with autoImplicit=false, plus six weakenings. Each has its own mapped compiler error, no maxErrors cap reached, no raised limits. Unknown data identifiers establish signature formation/use; unchanged-proof failure does not establish mathematical necessity or refute possible extensions. Successful positive checks remain separate.

|Parameter|Class/use, compiled tests and decision|
|---|---|
|τ : Type*|Arbitrary universe-polymorphic variable domain. Drop ill-scopes dependent header; already Type*, no meaningful narrower universe to generalize. Retain.|
|[Fintype τ]|Finite Θ/index context. Drop and Finite replacement fail Fintype synthesis. No local-instance scaffold or domain churn; retain anonymous structure.|
|r|Natural pointwise weights/degrees. Drop ill-scopes hr0/degrees/conclusion. Concrete ℕ is required by degree/index APIs; retain.|
|hr0|All coordinates need positive scaled weights/product index. Drop fails, 0≤r fails Nat.mul_pos/index_mul. Nonzero equivalent compiles independently via Nat.pos_of_ne_zero; retain clearer positive form.|
|q|Natural rational denominators and Θ inputs. Drop ill-scopes point/Φ; no positivity assumption to weaken/add. Retain arbitrary q.|
|h|Integer numerators. Drop ill-scopes hh/point. General coefficient ring would restate coprimality/indexSet; no beneficial change.|
|hh|All-coordinate coprimality enters both Θ bounds, some/none exhaust Option τ. Drop fails use; no proper point-local weakening.|
|M|Arbitrary real coefficient bound/Θ input. Drop ill-scopes membership/coefficient conclusion. No positive-M assumption added.|
|l|Natural degree scale. Drop ill-scopes degree/RSet/conclusion. Concrete ℕ matches degree/weights; retain.|
|hl|Positive scale clears denominator and scaled weights. Drop and0≤l fail. l≠0 equivalent compiles independently; no new zero-case wrapper.|
|U|Arbitrary multivariate integer factor. Drop ill-scopes hU/conclusion. Already arbitrary; retain.|
|hU|RSet nonzero/degrees/coefficients. Drop fails, nonzero-only/degree-only/coefficient-only each fail actual membership/nonzero use. Current bundled form supplied by caller directly.|
|V|Arbitrary univariate integer factor. Drop ill-scopes hV/hVd/hVc/conclusion. Unit-equivalent rebundling shifts conversion to caller; retain.|
|hV|Nonzero factor for RSet and product index. Drop fails conversion use; no natural ordered-polynomial sign relaxation. Zero-factor extension would alter this positive-product stage and bring no actual caller benefit.|
|hVd|Natural degree upper bound. Drop fails degree conversion. Already weak ≤; arbitrary larger bound would not prove needed RSet cap. natDegree/degree equivalence adds no application benefit.|
|hVc|All coefficient absolute bounds. Drop fails membership. Support-local version independently compiles: nonzero V supplies one supported coefficient, so M≥0; unsupported coefficients are zero. Equivalent under hV and adds witness/case reconstruction for already-global-bound caller. Retain.|

All16 are the immutable FIRST effective contract; DecidableEq was already omitted in FIRST, not newly removed. `Alternative.lean`, `SupportBound.lean`, `Positivity.lean` independently re-elaborate complete proofs (exit0) for natural nonzero equivalents, support-local coefficients and `by positivity` at hlR. These are explicit successful mathematical alternatives, not calls to production helper. They do not justify unnecessary contract churn. Positive weights/nonzero V describe the intended product stage; failed weak trials are not claimed as counterexamples to a different zero-case theorem.

Literature status: n/a, private declaration explicitly exempt; public caller's full statement/documentation is unchanged and its prior original/revisit literature audits remain protected. Inversion check: determinant/R/D are already absent; this IS the existing arbitrary-separated-product abstraction. Generalizing further to two arbitrary renamed MvPolynomials would merely relocate index_mul/index_rename, lose the convenient univariate caller interface and require another audit. No independently useful broader API identified. Existing RSet and lem6Φ are the theorem's actual quantitative content.

## Measured signature packing and inequality inventory

All widths are Unicode codepoints. Complete next binder/application units are used, preserving mathematical expressions and dependent type ascriptions. Exact full effective #check-style rendering, names/order/BinderInfo/universes/conclusion are logged by independent/full semantic verifiers at format.width100.

|Line|Codepoints|Next complete unit|Arithmetic|Action|
|---|---:|---|---|---|
|405|99|`{h : Option τ → ℤ}`|99+1+18=118>100|retain|
|406|89|`{U : MvPolynomial τ ℤ}`|89+1+22=112>100|retain|
|407|88|`(hV : V ≠ 0)`|88+1+12=101>100|retain|
|408|86|`index (map (Int.castRingHom ℝ)`|86+1+30=117>100|retain|
|409|34|`(rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V))`|34+1+74=109>100|retain|
|410|82|`(fun j ↦ (h j : ℝ) / q j)`|82+1+25=108>100|retain|
|411|59|``|final line|retain|

|#|Location|Comparison/action|
|---|---|---|
|1|hr0|0 < r j; retain|
|2|hl|0 < l; retain|
|3|hVd|V.natDegree ≤ l*r none; retain|
|4|hVc|absolute real coefficient ≤ M; retain|
|5|conclusion|index … ≤ l*lem6Φ …; retain|
|6|entire signature|zero ≥/> occurrences, no reversal/name change|

## All42 golfing rules

|Rule|Concrete result|
|---|---|
|1.1 by exact|No trivial wrapper.|
|1.2 by rfl|Absent.|
|1.3 rw+exact|hV′0 already rwa; membership branches do genuine degree/coeff conversion before exact.|
|1.4 simp+exact|Previous final simpa replaced by direct rewrite and exact existing division/addition APIs for measured performance.|
|1.5 trailing rfl|Absent.|
|1.6 constructor|RSet refine ⟨nonzero,degree,coeff⟩ already explicit; branches require distinct conversions.|
|1.7 apply+exact|No pair; direct terms already.|
|1.8 by_contra|Absent.|
|1.9 eta|Lambdas express constant weights, restricted coordinates or Unit injectivity, not redundant wrappers.|
|1.10 inline have|All eight haves inventoried; hmU/hmV retained as a measured performance exception to single-use term inlining, avoiding the same delayed generic inference diagnosed in the failed pair. Other conversions/rewrites/multi-use terms retained.|
|1.11 apply+intro|Absent.|
|1.12 redundant show|Absent.|
|1.13 obtain projections|Only one hU nonzero projection; membership passed whole separately. No repeated decomposition.|
|1.14 merge rw|Existing map/index chain merged; final expansion must occur after Θ bounds, separate mathematical stage.|
|1.15 terminal unsqueeze|Historical measured exception retained until actual422.423ms diagnosis; now eliminate the entire terminal simp via correctly oriented division API.|
|1.16 squeeze nonterminal|No bare simp remains.|
|1.17 dot notation|map iff .2, division .1 and hU.1 already direct.|
|1.18 parens|Group nested multiline theorem arguments; no gratuitous trailing wrapper or dollar.|
|1.19 push Not|No push_neg.|
|1.20 ∃ helper|n/a: inequality, no existential helper.|
|2.1 grind|Fresh anonymous exact-prefix whole-goal attempt fails, mapped log preserved.|
|2.2 pre-grind|No selected grind.|
|2.3 simpa consolidation|Chosen direct final exact removes normalization of large proof types.|
|2.4 fun_prop|No function-property goal.|
|2.5 positivity|Fresh whole-goal fails; targeted hlR positivity compiles in complete independent proof, same line/step as explicit cast. Retain explicit bridge.|
|2.6 gcongr|Fresh whole-goal leaves structural goal; terminal monotonicity direct add_le_add.|
|2.7 lia/omega|Fresh whole-goal lia fails; weight positivity already exact Nat.mul_pos, no linear arithmetic subgoal.|
|2.8 aesop|Fresh clean anonymous trial fails.|
|2.9 norm_num/cast|Whole norm_num fails; single exact_mod_cast bridge suffices.|
|2.10 decide|Fresh trial fails on symbolic arbitrary-polynomial inequality.|
|2.11 field_simp/ring|No identity goal; direct div_le_iff₀' avoids algebraic normalization.|
|2.12 linear_combination|No ring/ring_nf endpoint or algebraic certificate goal.|
|2.13 wlog|No symmetric case branches; domains τ and Unit differ.|
|2.14 calc|No calc; existing direct add_le_add with division orientation is compact.|
|2.15 <;>|Membership degree and coefficient branches use different APIs/data; no common closing automation.|
|3.1 erw|Absent; rw/rwa work.|
|3.2 legacy function tactics|Absent.|
|3.3 omega→lia|No omega introduced; lia trial recorded under2.7.|
|3.4 rcases rfl|No destructuring substitution.|
|3.5 attributes|Private quantitative estimate does not warrant global simp/grind registration.|
|3.6 simp_all|Fresh clean anonymous trial fails; no selected simp_all only.|
|3.7 limits|No production override or raise; scratch lower search budgets preserved, not hidden.|

Step-back/simplify: performed in-thread; no built-in simplify tool is exposed, so no tool invocation is claimed. Whole-goal automation failed within recorded bounds, direct existing APIs handle conversion/product/supremum stages, and the concrete hom plus typed nonzero certificates and primed division orientation removes the measured elaboration work without extracting another helper. No extra API, parameter bundle or further cosmetic edit is recommended. All static decisions and selected source settled before final validation.

Phase3 file-level fixes: n/a dedicated scoped leaf. Phase5a non-rename change: only selected proof repair, no new/deleted helper. Phase5b rename: none warranted, queue untouched. No original count increment. Total source/proof line delta **+4** (helper26→30; file980→984).

## Semantic preservation design

Exact immutable helper FIRST text `82ea1dcd2a8ced63947dc92f7a43f06b3cf868156e85895cd843a16873a03c92`; full FIRST context `42d60acc1b1b3d587ffe568e246cb9ba637ee0a6449a6a2b29d6f02249354ba4`. Independent.lean re-elaborates **the entire exact FIRST proof in all its original preceding context**, transporting only namespace Roth to Roth.SeparatedRevisitFirstContext and adding scope closure. Exact helper bytes remain unchanged. A separate namespace independently repeats the entire final selected helper and **entire unchanged public index_det_le proof**, whose local call resolves to the independent helper. It never substitutes a call to actual target for the independent proof.

The verifier checks exact FIRST/current/actual16-binder telescopes and current/actual22-binder caller telescopes: full effective types, retained ordinary names/order/BinderInfo, exact universe parameters and conclusions. Anonymous synthetic instance names alone are exempt from name equality; their class/types/order/BinderInfo are checked. Exact old-full-type adapter terms are typechecked. Both opaque values use `value! true`, inferType, standard-only axioms and nonself proof checks; actual caller positively depends on actual private helper and independent caller positively depends on independent helper.

Latest entire380-check scaffold is retained as **exact320014-byte prefix** SHA256 `3874fec52129ab1e9af28a7937112281ceea8bba306b7329e7c2cbd0bf23e27e`, followed only by these new independent checks. No retained-inventory edit or inverse-recovery exception is needed. All29 original public recoveries, five definition values, original public28/29 proof context, whole-original MainLemma, independent-current MainLemma, actual RootTheta/MainLemma values/types/axioms/dependencies, all eleven helper audits from original35 and prior performance checks re-execute on the full augmented input. Four canonical full proof block hashes remain unchanged:

- Index original `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`.
- Theta original `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`.
- MainLemma original `96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a`.
- MainLemma independent current `859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41`.

The inherited13-file FIRST inventory plus the exact helper FIRST/context/manifest (16 protected files total) and all72 preceding Theta reports are SHA256-protected. Complete current project/source/pin17-map is retained in all-source-pin-hashes.json, baseline map separately in release-source-pin-hashes.json. Existing introduced-helper retention/deletion audits and all four proof blocks remain preserved.

Fresh final build/native/semantic/profile outcomes, warnings, artifact hashes and terminal authority revocation follow below; no owner full build/LeanEval or whole-file performance pass is inferred here.


## Failed repaired-source pair preserved; second concrete repair

First repaired source b84d3c204624812a1f2a6401f2495b2d19f5864356b9ad0f738a4461a63c51ee
removed terminal simp and pinned only the inner map hom. Its complete whole-Theta pair
was **831.865/1001.920ms** for the helper and775.546/864.328ms for the unchanged caller,
exit0 both,253.188/250.519s. The second helper sample fails1000ms. It is NOT accepted,
and no third unchanged-source sample was taken. Root final-Theta.lean, both actual-profile-
final-{first,repeat} raw/status/table files, strict slices, sources and hashes remain
untouched. failed-pair-current-nested-hotspots.json records the actual residual rewrite
637.082ms, index_mul argument477.182ms, mapped-factor265.059/210.828ms and still-generic
outer map_ne_zero_iff141.298/134.330ms (overlapping diagnostics, never summed).

The new proof isolates two typed real-map nonzero certificates using direct injectivity,
then pins the full real rename homs in the remaining generic zero-hom lemma. This is a
second concrete cause3/5 repair; it retains the successful direct division/addition
normalization. It adds4 proof lines (30 total), no helper, no API or caller change.
Measured fresh prefix cross-check: **2410 heartbeats**, versus3132 for failed repair
and6894 original. Retaining these single-use typed certificates is the supported
performance exception, not an arbitrary style waiver. Prefix compiles exit0; all final
proof/semantic/native/profile gates are repeated on the new source. New evidence lives
in `/private/tmp/theta-separated-performance/v2`; root evidence is immutable failure history.

V2 preparation initially rejected the intentionally changed live Theta against the
published baseline pin; the correction preserves/asserts original baseline via its source
snapshot and checks all unrelated live pins. A premature missing-file scratch request
failed before preparation completed; its returned exit/status is recorded in the session
but the original empty/missing-file scratch log was overwritten by the subsequent quoted-
name trial. No proof/absence gate relies on that orchestration mistake. The resolving-
quotation failure itself is fully preserved as v2/failed-quoted-PrefixAbsence.lean and
failed-quoted-prefix-absence.log/json. Corrected single-name positive absence is separate.


Fresh accepted-source nested diagnostics (not added to declaration totals): the formerly637.082ms rewrite is now200.665ms; the two typed certificates cost47.157/29.726ms, and final direct expansion/exact cost17.261/22.268ms. All are exact anchored rows in v2/final-nested-hotspots.json and its full strict slice. This confirms that the remaining generic-inference hotspot was reduced rather than moved into a new helper.

## Fresh final sequential build, semantic and native gates

Production source stayed frozen throughout the following ordinary commands, in this order:

|Actual command/gate|Exit|Seconds|Raw evidence|
|---|---:|---:|---|
|lake build Roth.Theta|0|37.035|build-theta-final.log/json|
|lake build Roth.MainLemma|0|34.731|build-mainlemma-final.log/json|
|lake env lean Independent.lean|0|38.477|independent-final.log/json|
|lake env lean ActualSemanticsAugmented.lean|0|218.561|actual-semantics-final.log/json|

The corrected separate independent file has **64 PASS**. The whole augmented semantic
input has **444 PASS = all380 preceding checks +64 new checks**. No PANIC/error/sorryAx
occurs in either clean final log. The earlier standalone current-context universe-name
mismatch is retained in failed-universe-*; the correction restores the same preceding
σ declaration and keeps exact universe-list comparison. It does not weaken a gate.
The canonical four full proof blocks and entire320014-byte preceding scaffold remain
byte-identical; no retention inventory or adapter edit was needed. Exact full FIRST,
current helper and entire current caller proofs were independently re-elaborated,
including opaque value!true/type/standard axioms, full binders/universes/conclusions,
old full-contract adapters, nonself checks and positive actual caller dependency.
All29 original public recoveries, all5 definition values, whole original and independent
current MainLemma, actual RootTheta/MainLemma values/types/standard axioms/dependencies,
all eleven helper-audit records from original35 and all prior performance repairs freshly pass as part of
that same full input.

|Complete unfiltered native file|success|partial|timed_out|Errors|Warnings|
|---|---|---|---|---:|---:|
|theta|true|false|false|0|8|
|mainlemma|true|false|false|0|3|

Native raw JSON retains **every warning verbatim**, with no range/declaration/severity filter. Warning inventory:

- theta:1:2: * `-/`:
- theta:93:43: Variable name `hr` is not explicitly referenced.
- theta:101:27: Variable name `hB` is not explicitly referenced.
- theta:101:64: Variable name `hr` is not explicitly referenced.
- theta:109:28: Variable name `hB` is not explicitly referenced.
- theta:129:81: Variable name `hr` is not explicitly referenced.
- theta:252:6: Variable name `hr` is not explicitly referenced.
- theta:551:47: Variable name `hq` is not explicitly referenced.
- mainlemma:1:2: * `-/`:
- mainlemma:149:28: Variable name `hδ0` is not explicitly referenced.
- mainlemma:149:69: Variable name `hr₁` is not explicitly referenced.

All warnings are inherited header/protected-hypothesis findings; no new target warning
or suppression. Exact raw messages, hints, locations and dependencies are in the two
native files. The semantic input SHA256 is
`8c9f5dff626eca205c484433453402202bf38ec988e24b94a2b4f9672014c14a`.

## Actual full Theta traces and scoped buzz result

All owned ordinary/native requests were drained before real profiling. Actual command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`

final-first: exit0, timeout=false, 248.706s; raw SHA256 `667f81dd77209259e49b7c5bcf4489eef4764ae927c95d7b6deff3f6c5190001`, 214004392 bytes.

Each completed table inventories all50 current source declarations and match every source anchor;
each theorem/lemma has exactly one actual proof anchor. Strict UTF8 decoding succeeds
with zero invalid bytes or replacement sequences. Full source snapshot and hashes,
raw offsets, exact disjoint rows and strict slice hashes are retained. Totals sum only
the selected outer source command and associated top-level async proof/addDecl/compiler/
linter rows; nested macro/tactic/kernel rows are never added again.

|Declaration|Inherited latest pair ms|Fresh first ms|Fresh repeat ms|
|---|---:|---:|---:|
|index_separated_mul_le_aux|1298.995/1133.509|568.792|not required|
|index_det_le|822.592/726.010|725.539|not required|
|index_le_lem6|576.591/581.268|550.944|not required|
|Θ_option_le|170.607/142.216|156.723|not required|

Both scoped first rows are<750ms, so no same-source repeat is required or taken.
No third unchanged-source sample or timing cherry-pick. Every inherited failed sample
remains preserved. Heartbeats6894→2410 independently support lower proof elaboration
work. Buzz outcome: **FIXED for assigned separated-product helper**, with unchanged
direct index_det_le consumer passing the scoped budget. No API/helper/limit/axiom change.
The formerly deleted coefficient wrapper remains absent.

Same-issue propagation check: direct index_det_le uses the repaired helper only by name,
so its complete proof is kept and measured. Remaining index_numeric_bound_aux uses real
min/sqrt nonlinear estimates, sum_max_sub_le_index_det uses determinant/permutation and
finite-sum index conversion, lem7_Φ_bound/lem7_numeric use rpow/sqrt arithmetic, and
theta_prefix_lt_aux transports finite-index/cast inequalities. They do not contain this
inferred coefficient-hom plus terminal separated-index normalization pattern. Their
separate mandatory scoped repairs remain queued; no unrelated proof edit was made.

## Remaining queue, scope and owner gates

Four older failures remain: index_numeric_bound_aux, sum_max_sub_le_index_det,
lem7_Φ_bound and lem7_numeric. The previously failed theta_prefix_lt_aux1047.277ms /
repeat721.307ms remains a separate **mandatory second repair**, regardless of any lower
sample below. All known failures remain mandatory until their own repaired-source gates.
This revisit provides **no whole-file timing PASS**. MainLemma's actual caller timing
remains **unmeasured after its prior bounded cutoff before main_lemma**; ordinary/native/
semantic success never substitutes for that actual trace.

|Separate queued declaration|Fresh first ms|Fresh repeat ms|
|---|---:|---:|
|index_numeric_bound_aux|1097.018|not taken|
|sum_max_sub_le_index_det|1233.766|not taken|
|lem7_Φ_bound|1190.021|not taken|
|lem7_numeric|1253.038|not taken|
|theta_prefix_lt_aux|695.066|not taken|

No new overbudget declaration outside the known queue occurred.

Owner alone performs final cumulative/allactual checks, full `lake build` THEN separate
`lake build Roth.LeanEval`, exact-path stage/commit/push/clean before the next revisit
edit. Those owner gates are pending and not claimed here. Counts stay216/264,Theta35/35,
completed files9/14; original count increase0.

## Gate status and required eleven-step checklist

|Gate|Result/evidence|
|---|---|
|Module builds|PASS: actual Theta THEN MainLemma commands/exit0 above|
|Definitions/statements protected|PASS: only scoped proof changes; exact helper header and all surrounding bytes unchanged|
|Direct caller/comments|PASS: entire index_det_le proof/signature/docstring and all3 Step comments byte-identical|
|Structure/naming|PASS: helper30≤30, subproof≤6, branches≤2; descriptive private name|
|Packing/inequality|PASS: all7 measured signature rows and five correctly oriented comparisons|
|Trust/scaffolding|PASS: no new axiom/sorry/native_decide/limits/imports; opaque/std-axiom checks clean|
|Independent semantics|PASS: exact FIRST actual-context proof, entire current helper/caller, exact full old adapter and444 checks|
|Native|PASS: complete unfiltered success/partial=false/timed_out=false,0errors in both files|
|Scoped actual performance|PASS: every final target/direct-caller observation<1000ms, repeat rule honored|
|Owner full project/Eval/publication|PENDING owner; never inferred|

- [✓]1 Both skills, required references/workflows and actual failing evidence read.
- [✓]2 All24 audit items and every local have reviewed.
- [✓]2.5 Five actual searches,11 clean anonymous current-goal trials and positive absence gate.
- [✓]2.6 All16 effective drops, six weakenings, independently compiled successful equivalents/support-local bound; private literature exemption/inversion recorded.
- [✓]2.7 All7 signature codepoint widths and complete-next-unit arithmetic.
- [✓]2.8 All5 comparison occurrences; no reverse orientation.
- [✓]3 All42 golf rules assessed with concrete statuses.
- [✓]4 In-thread holistic simplify/reuse/efficiency review, no unneeded helper/API.
- [✓]5a Fresh complete unfiltered native Theta/MainLemma diagnostics.
- [✓]5b Sequential module builds, exact FIRST/current/caller independent proofs, entire380+64 semantics and actual full Theta/scoped profiling.
- [✓]6a No rename warranted, shared queue/log untouched.

## Complete artifact map and frozen release

Fresh accepted final artifacts are under `/private/tmp/theta-separated-performance/v2`; immutable failed-pair and earlier audit evidence remains at the parent directory:

|Evidence|Concrete artifacts|
|---|---|
|Source/pins/FIRST/reports|baseline-Theta.lean; final-Theta.lean; source-hashes.json; release-source-pin-hashes.json; all-source-pin-hashes.json; all-FIRST-immutable-hashes.json; protected-report-hashes.json|
|Diff/static|owned-proof.diff; static-gates.json; packing.json; independent-proof-blocks.json|
|Exploration|Candidate.lean; candidate-declaration.lean; parent failed-order-Candidate.lean/candidate logs and failed-pair source/traces; Heartbeats-before/after.lean and logs/json; parent scratch-corrections.md|
|Clean goal/generality|PrefixAbsence.lean/log/json; Automation.lean/log/json; automation-ranges/results.json; BindersNegative.lean/log/json; binder-ranges/results.json; Alternative/SupportBound/Positivity.lean and successful logs/json|
|Search|parent search-finder/loogle/search/local.json; v2 mathlib-source.log and SourceSearch.lean/log/json|
|Full semantics|Independent.lean; ActualSemanticsAugmented.lean; immutable-scaffold-and-blocks.json; independent-final.log/json; actual-semantics-final.log/json; semantic-marker-summary-final.json; parent failed-universe-* retained|
|Build/native|build-theta-final.log/json; build-mainlemma-final.log/json; native-theta-final.json; native-mainlemma-final.json|
|All inherited failures|parent preserved-baselines.json, baseline-*-separated-strict-slice.log, baseline-actual-nested-hotspots.json and failed-first-repair-manifest.json; original raw/source/table files retained at exact manifest paths|
|Actual profiles|actual-profile-final-first.log/json/-table.json; optional final-repeat counterparts; profile-final-*-strict-slices.json; scoped strict slice logs; profile-final-*-remaining-queue.json; profile-final-*-new-actionable-strict-slices.json|
|Request drain/freeze|pre-profile-drain.json; optional pre-repeat-drain.json; final-process-drain.json; evidence-manifest.json; final-freeze.json|

Final Theta SHA256 **`3631ff20d25efdec5d9a846640a8c5a4f5efcac876a37dfee83e39c638fcfcde`**. All17 source/pin files checked; only scoped Theta proof changed. All13 inherited FIRST artifacts plus helper FIRST/context/manifest and all72 preceding reports unchanged. The four full canonical proof hashes and exact preceding semantic prefix remain unchanged.

All owned compiler process groups are dead; ordinary/native pending lists are empty.
Terminal authority release: **source/scratch/report/compiler/native REVOKED**, sole
compiler/native window **RELEASED**. No own mutation or compiler/native request follows
this terminal freeze. Full project/Eval/publication remain exclusively with owner.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 83.979 s and 35.554 s.
Theta SHA256 `3631ff20d25efdec5d9a846640a8c5a4f5efcac876a37dfee83e39c638fcfcde` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p04-full.log` and `/private/tmp/roth-theta-p04-leaneval.log`; machine record
`/private/tmp/roth-theta-p04-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 28 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
