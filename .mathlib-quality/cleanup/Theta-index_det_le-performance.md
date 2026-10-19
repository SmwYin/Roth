# Dedicated performance revisit — Roth.index_det_le (original28)

This revisit owns only public index_det_le's proof and this report. Release2986584b61985402c7d84546b4ab3de1c6eef35e, source/audit45d50ba0a5355cb403701aae5c8b1b299ff8eb87. Baseline Theta5458997a96e7dfd6c5a86d35e210f86c533b3c4b62a5e532a163b5c80c34fe1a. Counts remain216/264 originals, Theta35/35, files9/14 until owner file-final gates. No Git, shared-log, rename queue or unrelated proof edits. All existing original/helper/deletion reports remain preserved.

## Actual failure and measured repair design

The preserved original corrected trace measured2083.744ms;9faa repeat1422.778ms; last positive pair1179.250/1424.714ms; immediately preceding release1293.336ms. An unchanged-source later success would not erase these failures. Raw/source/table/hash/slices are retained in preserved-baselines.json and the inherited original audits.

Diagnostic /private/tmp/roth-theta-whole-profile-repair-hotspots/index_det_le.json: broad hFcoef simpa615.455ms, entire coefficient block675.614ms, proof1053.182ms. These nested values overlap and are never added. Eight-cause diagnosis: (1) no dominant instance-synthesis node, (2) **fat simp is the supported primary cause**, (3) defeq/cast normalization contributes inside it, (4) no heavy terminal arithmetic, (5) determinant argument inferred successfully and not yet evidence for explicit-argument churn, (6) identity Nat cast occurs in finite-sum normalization, (7) repeated determinant subterms are required in existing coefficient uses, no evidence for a new binding, (8) kernel/addDecl overhead stays in conservative disjoint totals. Repair replaces broad normalization by the pinned finite-product/sum/cardinality/power/commutation rewrites plus Nat.cast_id. This is the profiling reference's measured terminal-simp exception. No coefficient wrapper is restored, and no new helper moves the cost.

First minimal Candidate.lean failed only on the identity Nat cast inside the exponent; failed-minimal-Candidate.lean and candidate.log/json remain immutable evidence. The corrected candidate adds Nat.cast_id and compiles exit0 (candidate-two.log/json). Production never contained the failed probe. Final measured evidence is appended below; no claim relies on an uncompiled suggestion.

## Full24-item substantive audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|No target warning in successful candidate; fresh full unfiltered native diagnostics required below.|
|2|HAVE|hFcoef is used twice and retained; hUc/hVc feed final RSet and coefficient arguments; both local h1 estimates are rewritten before transitivity and retained. hVc's a₀/ha₀ correlated nonzero witness stays together.|
|3|SET_OPTION|No production override; low bounded search-only heartbeat options live only in scratch.|
|4|SIMP|The single target simpa is terminal; measured broad-simp hotspot justifies exact only-list. Other rewrite/proof structure unchanged.|
|5|NAMING|index_det_le names the index inequality for a determinant; no banned abbreviation, numeric scheme, _ge_/_gt_, single-letter public name or rename needed.|
|6|PACKING|All11 signature lines measured below with complete next mathematical units.|
|7|BY|Every := by remains at line end.|
|8|FORMAT|Two-space proof, four-space signature, no blank internal lines, Unicode mathematical lambdas, no haveI/letI.|
|9|COMMENTS|All3 Step comments byte-identical in order and anchored to the same mathematical stages.|
|10|DOCSTRING|Original public determinant/source documentation byte-identical.|
|11|VISIBILITY|Public inequality used by actual index_le_lem6 retained; no visibility/API change.|
|12|STRUCTURE|Ordinary≤30 target, outside module Main-results headline list; hFcoef,hUc,hVc each≤10, no long branch, no helper needed for an invented15-line cap.|
|13|MATHLIB|Five actual methods and successful pinned #checks below; existing determinant coefficient, separated index and integer absolute-value facts used directly.|
|14|JUNK DEF|n/a: theorem; no new def/abbrev.|
|15|EXISTS|n/a: inequality, not a trivial existential helper.|
|16|SHOW/CHANGE|Neither occurs in target.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective binder audited below; unchanged current public contract, exact old adapter and full old/current callers independently checked.|
|19|INEQUALITY|Six comparisons across header, all < or ≤; no ≥, >, _ge_ or _gt_ name.|
|20|NORMAL FORM|Real index≤lΦ, natural degree bounds, integer coefficients and exact separated factorization already canonical.|
|21|SYNTAX GENERALITY|RSet carries exactly caller's input; public wrapper and domains protected by prior user choices. No parameter bundling improves application.|
|22|IMPORT FANOUT|No production import change.|
|23|CASTS|Diff adds no coercion/ascription; identity cast is eliminated by existing Nat.cast_id. Existing coefficient ℤ→ℝ, point ℤ/ℕ→ℝ and Fin→ℕ bridges are load-bearing.|
|24|INSTANCE NAME|No instance declaration or name introduced. Current DecidableEq omission retained.|

## Five actual search methods and fresh goal probes

1. Native local search finds Roth.abs_coeff_det_hasseDeriv_le in Roth/CoeffNorm.lean; index unavailable is explicitly not an absence proof (search-local.json).
2. Native Loogle Finset.prod_const returns the exact finite constant-product theorem (search-loogle.json).
3. Native Lean Finder queried determinant/Hasse coefficient bounds, returning polynomial Hasse coefficient formula and unrelated Chevalley/matrix facts; no matching full index bound (search-finder.json).
4. Native LeanSearch queried product/separate-variable index bounds; returned natDegree/degreeOf multiplication facts, which do not establish Roth index/Θ content (search-search.json).
5. Direct rg keyword/name and standard-file organization searches inspect CoeffNorm/Index/Theta and mathlib finite-big-operator, Fintype Option, Nat cast and polynomial Hasse/degree files. Exact pinned signatures rechecked in SourceSearch.lean/log; mathlib-source.log retains inspected source locations. Existing project-specific separated-product helper is the actual abstraction, not duplicated.

No claim that an unavailable index or nonmatching remote query proves absence. Exact-prefix anonymous examples run grind/simp/aesop/exact?/apply?/lia/positivity/gcongr/norm_num/decide/simp_all under a lower2000-heartbeat scratch bound. Automation.lean contains the exact source prefix **before** target, explicit omit DecidableEq, no import-self, no named failed theorem. Separate successful PrefixAbsence.lean asserts target and all later public callers absent. Markers/ranges and all compiler errors retained. Five-method search does not manufacture a replacement for the composed Roth proof.

## Every effective parameter and generality

Every retained ordinary group is tested by literal-header drop using autoImplicit=false and complete proof; data drops establish signature formation/use, never mathematical necessity. All tests/ranges/results are retained. Fintype drop/Finite replacement are separately bounded; τ's type-variable drop is checked separately. Positive full exact types/values/axioms are never inferred from an expected-failure batch.

|Binder|Use and compiled candidate/decision|
|---|---|
|τ : Type*|Arbitrary universe-polymorphic variable domain; drop ill-scopes dependent header. Retain.|
|[Fintype τ]|cardinality inside lem6M and finite index/Θ; drop and Finite replacement cannot synthesize required Fintype. Retain explicit structure.|
|r|Natural degrees and weights; drop ill-scopes hr0/hr₁/conclusion.|
|hr0|All positive weights feed separated index; drop fails, weak0≤r fails positive helper contract.|
|r₁|Uniform natural cap in hr₁/M; drop ill-scopes header.|
|hr₁|Transitive polynomial degree cap in coefficient theorem; drop fails use.|
|q|Arbitrary natural point denominators; drop ill-scopes point/Φ. No positivity assumption added.|
|B|Arbitrary real coefficient bound in RSet/M; drop ill-scopes. No B≥1 reintroduced.|
|R|Arbitrary integer multivariate polynomial; drop ill-scopes hR/determinant.|
|hR|RSet nonzero/degrees/coefficients; drop fails coefficient bound projections. Retain explicit user wrapper/domain choice.|
|h|Integer rational-point numerators; drop ill-scopes hh/point.|
|hh|Coordinate coprimality feeds separated Θ proof; drop fails use. All some/none coordinates needed.|
|l|Natural determinant dimension/scale; drop ill-scopes D/Fin and RHS.|
|hl|Positive dimension,1≤l; drop fails use, weak0≤l fails separated helper contract. Zero-size extension would require a different stage wrapper, not improve actual caller.|
|D|Arbitrary Fin l derivative multi-indices; drop ill-scopes determinant.|
|U|Arbitrary separated multivariate factor; drop ill-scopes hU/degrees/factorization.|
|V|Arbitrary integer univariate factor; drop ill-scopes hV/degrees/factorization.|
|hU|Nonzero coefficient witness and RSet membership; drop fails.|
|hV|Leading coefficient nonzero and index product nonzero; drop fails.|
|hUd|Pointwise degree bound for Θ membership; drop fails. Already weak inequality.|
|hVd|Univariate natural degree cap; drop fails. Already weak inequality.|
|hF|Exact separated factorization used in both coefficient bounds and final index rewrite; drop fails.|

Current effective telescope has22 parameters (τ,Fintype plus20 ordinary groups). DecidableEq,δ,hδ,hl′,hB were already removed by approved original audit; none is reintroduced. Natural nonzero/positive equivalents are equivalent restatements, not useful strict weakenings. Generic coefficient fields would lose the integer nonzero-absolute-value≥1 fact; ℝ/index/Option/RSet interfaces carry the actual theorem's content. No API change recommended.

Public literature and inversion: fresh reading of local primary transcription .mathlib-quality/references/clean.tex735–777 confirms unique coefficient products, integral coefficient absolute values≥1, scaled Θ bounds and equation(17), precisely the3 retained stages. Existing original audit's primary literature links are preserved; no new bibliographic claim. Inversion fires on the post-factorization index stage, which is already isolated as substantive index_separated_mul_le_aux and has its own following performance revisit. Coefficient stage already calls arbitrary derivative-matrix theorem in CoeffNorm directly. A new one-use normalization wrapper would repeat the previously deleted thin coefficient helper; no such restoration or broader API churn recommended.

## All42 golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by exact|No trivial wrapper; terminal direct helper exact remains.|
|1.2 by rfl|No rfl wrapper.|
|1.3 rw+exact|h1 is rewritten then passed to a nontrivial transitive inequality; rwa cannot replace that reasoning.|
|1.4 simp+exact|hFcoef already simpa using direct general estimate; narrowed for measured cost.|
|1.5 trailing rfl|Absent.|
|1.6 constructor|Final RSet constructor already ⟨hU,hUd,hUc⟩.|
|1.7 apply+exact|Direct theorem application already.|
|1.8 by_contra|Absent.|
|1.9 eta|Lambdas introduce coefficient indices/pointwise degrees, not eta-only wrappers.|
|1.10 have inline|hFcoef used twice; hUc/hVc feed final arguments; h1 rewritten, all substantive and retained.|
|1.11 apply+intro|Absent.|
|1.12 show|Absent.|
|1.13 obtain|hVc's a₀/ha₀ obtained together and genuinely used. hR fields passed/projection-specific, not redundant decompositions.|
|1.14 merge rw|Each h1 normalization already one combined chain. Final hF rewrite has distinct index goal.|
|1.15 terminal simp|Exact-list exception justified by actual fat-simp trace and fresh measurements below; no aesthetic-only squeeze.|
|1.16 nonterminal simp|No nonterminal simp in target.|
|1.17 dot notation|hR.2.1/.2.2 and .trans already natural.|
|1.18 parentheses|Retained nested determinant/casts and by proof arguments group applications; none gratuitous.|
|1.19 push Not|Absent.|
|1.20 trivial existential|No such helper.|
|2.1 grind|Clean bounded anonymous trial retained; no matching direct proof.|
|2.2 pre-grind|No production grind.|
|2.3 simpa consolidation|hFcoef uses direct simpa using; no extra simp/exact sequence.|
|2.4 fun_prop|n/a: no function-regularity goal.|
|2.5 positivity|Clean trial does not prove general index bound; abs_nonneg is exact local fact.|
|2.6 gcongr|Clean whole trial fails; factor estimates use exact le_mul_of_one_le_left/right.trans.|
|2.7 lia/omega|Clean lia trial fails; statement is symbolic real index, not linear integer arithmetic.|
|2.8 aesop|Clean bounded trial retained; no direct proof.|
|2.9 norm_num/cast|Clean norm_num trial fails full goal; two exact_mod_cast bridges establish integer abs≥1. No numeric compute needed.|
|2.10 decide|Symbolic real index with arbitrary polynomials, not closed finite computation; actual trial retained.|
|2.11 field_simp/ring|No denominator algebra identity; separated helper already handles scaling.|
|2.12 linear_combination|No ring/ring_nf terminal or polynomial identity with hypotheses.|
|2.13 wlog|U,V have different variable domains; no symmetric case duplication.|
|2.14 calc compression|No calc chain.|
|2.15 <;>|No pair of identical branch goals; factor estimates require distinct leading/existential witnesses.|
|3.1 erw|None.|
|3.2 legacy analysis|Neither continuity nor measurability.|
|3.3 omega→lia|No omega; clean lia trial already.|
|3.4 rcases rfl|Absent.|
|3.5 attributes|No canonical global rewrite supplied by this quantitative theorem; no new attribute.|
|3.6 simp_all|Clean anonymous trial retained; no production simp_all only.|
|3.7 limits|No production limit or diagnostic scaffolding.|

Scoped simplify review:3 mathematical stages, direct existing APIs, shared coefficient bound, two distinct integral factor arguments. The focused rewrite list fixes the identified normalization cost without speculative helper/API changes. No further refactoring recommended. Built-in simplify handoff unavailable, so holistic review performed directly and reported honestly. Existing helper deletion/retention audits remain intact.

## Measured signature packing and inequality inventory

|Line|Codepoints|Next complete unit|Arithmetic|Action|
|---|---:|---|---|---|
|444|91|`{q : Option τ → ℕ}`|91+1+18=110>100|retain|
|445|82|`{h : Option τ → ℤ}`|82+1+18=101>100|retain|
|446|81|`{D : Fin l → (τ →₀ ℕ)}`|81+1+22=104>100|retain|
|447|94|`(hUd : ∀ j, degreeOf j U ≤ l * r (some j))`|94+1+42=137>100|retain|
|448|79|`(hF : (Matrix.of fun μ ν : Fin l ↦`|79+1+34=114>100|retain|
|449|38|`hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =`|38+1+72=111>100|retain|
|450|80|`rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) :`|80+1+74=155>100|retain|
|451|80|`index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦`|80+1+59=140>100|retain|
|452|63|`hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)`|63+1+71=135>100|retain|
|453|79|`(fun j ↦ (h j : ℝ) / q j)`|79+1+25=105>100|retain|
|454|93|``|final line|retain|

|Occurrence|Location|Orientation/action|
|---|---|---|
|1|hr0|0 < r j; retain|
|2|hr₁|r j ≤ r₁; retain|
|3|hl|1 ≤ l; retain|
|4|hUd|degreeOf j U ≤ l*r(some j); retain|
|5|hVd|V.natDegree ≤ l*r none; retain|
|6|conclusion|index … ≤ l*lem6Φ …; retain|

No reversed comparisons or inequality-name rename. Packing uses exact current source and whole application/binder groups. All static design decisions are complete before final sequential validation.

## Bounded exploration and deterministic comparison

Successful exact-prefix count runs: baseline **4996**, selected normalization **3357** heartbeats (32.8% reduction), both under the unchanged default200000. A further compiled directed-normalization alternative applies the coefficient inequality with trans_eq before simplifying its scalar bound, measuring3326 heartbeats, only31 below the simpler selected proof. It is not selected: the extra tactic line yields no material deterministic benefit. Its full source and successful raw log/status remain Heartbeats-directed.lean and heartbeats-directed.log/json. No speculative explicit-matrix argument change is applied without supporting evidence.

The initial count wrapper was placed after an omit/docstring modifier and failed syntax; its full source/log/status are preserved as failed-wrapper-* and do not certify a count. Only the before wrapper was executed initially; the matching unexecuted after template is preserved separately. Corrected successful wrappers enclose the full omit/docstring/declaration. Every automation trial has its own in-range error marker (automation-results.json); lower-budget timeouts are bounded failures, never proofs of mathematical absence. Initial bounded binder trials also hit lower-budget timeouts and section-omit diagnostics. Default-budget literal-proof reruns plus standalone domain/class probes refine these diagnostics; all failed samples remain. No maxErrors/production heartbeat/recursion setting is raised.

71 preceding Theta audit reports are hash-preserved in protected-report-hashes.json, including all original/helper/deletion audits. All13 immutable FIRST source/success-evidence hashes are independently rechecked; their complete exact path/hash map is all-FIRST-immutable-hashes.json. No new helper is introduced and no additional helper audit is required.

## Final sequential ordinary, semantic and native checks

No source edit followed the final source snapshot. Fresh commands are sequential:

|Command/gate|Exit|Seconds|Raw evidence|
|---|---:|---:|---|
|build-theta-final|0|32.404|build-theta-final.log/json|
|build-mainlemma-final|0|35.143|build-mainlemma-final.log/json|
|preceding-independent-final|0|29.357|preceding-independent-final.log/json|
|actual-semantics-final|0|162.411|actual-semantics-final.log/json|

The complete preceding **373-check** semantic scaffold is an exact byte prefix,
SHA301813191a6e6dd42c35651508b203e9c06263bf29d11a695b4b75efc2f96691.
All373 checks are freshly re-executed. All29 immutable original public contracts and5
public definition values, original35 helper FIRST/deletion audits, positive quadratic
FIRST, whole independent original2b MainLemma and independent whole current MainLemma,
actual RootTheta/MainLemma opaque values/types/standard axioms/dependencies all pass.
No retained-inventory edits or inverse adaptation are necessary.

The four entire canonical proof blocks retain their original exact byte offsets and hashes:

- bytes[1414,15125): `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`
- bytes[16628,68797): `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`
- bytes[70475,105941): `96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a`
- bytes[117380,152930): `859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41`

The exact original index_det_le proof is independently re-elaborated within that preserved
original namespace/context, with its exact old contract adapter. A new complete preceding-current
namespace independently re-elaborates release index_det_le, its existing separated helper,
and the ENTIRE release index_le_lem6 caller with its preceding private context. It also
retains complete Θ_option_le context. Seven new successful checks bring the combined run
to **380 PASS**; the separate independent file has7 PASS. Full effective types, every
retained binder's type/order/BinderInfo/ordinary name, exact universe list, conclusions,
opaque value!true/type and standard axioms are checked against ACTUAL built constants.
Both independent target/caller proof values contain no call to the corresponding actual
target; actual index_le_lem6→index_det_le dependency is positively required. No self
forwarding is used as an independent proof. No PANIC/error/sorryAx appears in successful
verification logs. The current public contract is unchanged; caller hq and every explicit
prior Θ hB/hr/wrapper/domain choice remain intact.

|Complete unfiltered native file|success|partial|timed_out|Errors|Warnings|
|---|---|---|---|---:|---:|
|theta|true|false|false|0|8|
|mainlemma|true|false|false|0|3|

All warnings are retained verbatim in native-theta-final.json/native-mainlemma-final.json;
no severity/range filter or truncated request certifies this gate. Final source/pin/FIRST
and preceding-report hashes are rechecked independently.

## Actual full-module trace and scoped buzz result

After all ordinary/native requests drained, ran the exact live-module command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`

final-first: exit0, no timeout, 251.037s. Complete raw UTF8 log/status/table/source and all scoped strict slices preserved.

final-repeat: exit0, no timeout, 249.114s. Complete raw UTF8 log/status/table/source and all scoped strict slices preserved.

All50 source declarations are inventoried and matched; each theorem/lemma has exactly
one actual anchored proof. The tables/slices record byte offsets and SHA256 hashes.
Totals add only disjoint command+async proof/addDecl/compiler/linter rows. Nested
macro/tactic/kernel children are diagnostic-only and never double counted. Strict UTF8
has no invalid bytes/replacement sequences.

|Scope|Inherited latest ms|Fresh first ms|Fresh repeat ms|
|---|---:|---:|---:|
|index_det_le|1293.336|822.592|726.010|
|index_le_lem6|498.642|576.591|581.268|
|Θ_option_le|160.903|170.607|142.216|

Scoped≥750ms triggered exactly one unchanged-final-source repeat; every final scoped observation is<1000ms.
No third unchanged-source sample, erased failure or timing cherry-pick. Selected
normalization measured4996→3357heartbeats, with actual timing above. Buzz outcome:
**FIXED for assigned index_det_le**, direct caller passes. No helper/API change, no raised
limit, no trust downgrade. Existing separated helper proof remains untouched for its own
next dedicated audit. The deleted thin coefficient wrapper stays absent.

## Remaining mandatory queue and limits

These five older failures remain a separate mandatory repair queue, regardless of any
individual favorable current sample. This scoped result is **not a whole-file timing PASS**.
MainLemma actual caller timing remains **unmeasured after its prior bounded cutoff before
main_lemma**; ordinary build/semantic/native results do not certify its timing.

|Separate older target|Fresh first ms|
|---|---:|
|index_separated_mul_le_aux|1298.995|
|index_numeric_bound_aux|1286.394|
|sum_max_sub_le_index_det|1411.317|
|lem7_Φ_bound|1525.009|
|lem7_numeric|1556.938|

New actionable queue additions: theta_prefix_lt_aux 1047.277ms (final-first).

Owner alone performs cumulative/allactual checks, full project lake build THEN separate
Roth.LeanEval, exact-path staging/commit/push/clean before the next revisit edit.
Those owner gates remain pending and are never claimed completed here. Counts remain
216/264,Theta35/35,files9/14; this revisit adds0 originals.

## Gates and eleven-step checklist

|Gate|Result|
|---|---|
|Module build|Theta THEN MainLemma exit0, raw commands/status above|
|Definitions/statements protected|Only2 assigned proof lines changed; full header and surrounding file bytes identical|
|Structure/naming|24 proof lines≤30; all subproofs≤10; all3 Step comments retained; descriptive name|
|Packing/inequality|All11 measured signature rows and6 comparison occurrences; no reverse orientation|
|Trust/scaffolding|No new axiom/sorry/native_decide/limits/imports; successful opaque/std-axiom checks|
|Independent compatibility|Exact original target and whole old/current callers;380 combined positive checks|
|Native|Complete unfiltered success,partial=false,timed_out=false,0errors for both modules|
|Actual scoped performance|Every final target/direct-caller observation<1000ms; repeat rule honored|
|Full project/Eval/publication|Owner pending|

- [✓]1 Required skills/workflow/references and actual failure read.
- [✓]2 Full24 substantive audit and complete local fact/witness inventory.
- [✓]2.5 Five actual mathlib searches;11 bounded anonymous current-goal trials and separate positive absence.
- [✓]2.6 All22 effective parameters;20 ordinary drops,2 positivity weakenings, standalone domain/class probes; public literature/inversion/retained-interface decisions.
- [✓]2.7 All11 per-line codepoint packing measurements.
- [✓]2.8 All6 inequalities checked.
- [✓]3 All42 golf rules assessed.
- [✓]4 Holistic simplify/reuse/efficiency review; no further extraction.
- [✓]5a Fresh complete unfiltered native Theta/MainLemma diagnostics.
- [✓]5b Sequential module builds, independent exact old/current semantics,380 positive checks, actual full trace/scoped measurements.
- [✓]6a No renames or shared queue/log mutation.

## Full artifact map and terminal freeze

All new artifacts are in /private/tmp/theta-indexdet-performance:

|Evidence|Artifacts|
|---|---|
|Sources/pins/FIRST|baseline-Theta.lean;final-Theta.lean;source-hashes.json;release-source-pin-hashes.json;all-source-pin-hashes.json;all-FIRST-immutable-hashes.json;protected-report-hashes.json|
|Diff/static|owned-proof.diff;static-gates.json;packing.json;independent-current-proof-blocks.json|
|Exploration|Candidate.lean;failed-minimal-Candidate.lean;candidate.log/json;candidate-two.log/json;Heartbeats-before/after/directed.lean and successful logs/json;failed-wrapper-* preserved|
|Goal/generality|PrefixAbsence.lean and successful log/json;Automation.lean/log/json;automation-ranges/results.json;BindersNegative.lean/log/json;BindersDefault.lean/log/json;binder-ranges/results.json;DropDomain.lean/log/json;ClassWeakening.lean/log/json|
|Search|search-local/loogle/finder/search.json;mathlib-source.log;SourceSearch.lean/log/json|
|Whole semantics|ActualSemanticsAugmented.lean;PrecedingIndependent.lean;immutable-scaffold-and-blocks.json;actual-semantics-final.log/json;preceding-independent-final.log/json;semantic-marker-summary-final.json|
|Module/native|build-theta-final.log/json;build-mainlemma-final.log/json;native-theta-final.json;native-mainlemma-final.json|
|All historical failures|preserved-baselines.json;baseline-*-strict-slice.log;immutable original and9faa/positive/index29 source/raw/table paths retained in original audits/dispatch/map|
|Actual profiles|actual-profile-final-first.log/json/-table.json;optional final-repeat counterparts;profile-final-*-strict-slices.json;exact scoped slice logs;profile-final-*-remaining-queue.json;profile-final-*-new-actionable-strict-slices.json|
|Drain/freeze|pre-profile-drain.json;optional pre-repeat-drain.json;final-process-drain.json;evidence-manifest.json;final-freeze.json|

Final Theta SHA256 `2760ef227eb2d729381057ad02c2a0ac54c3fdc49e99a3a5a22c025b3fb6c145`.

All17 source/pin files are checked, with16 unchanged and only scoped Theta proof changed.
All13 immutable FIRST artifacts and71 preceding Theta reports remain unchanged. Final
process/group drain confirms no owned ordinary/native request remains. Terminal release:
**source/scratch/report/compiler/native authority REVOKED**, compiler window RELEASED.
No further own mutation or compiler/native request follows this handoff.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 78.752 s and 32.808 s.
Theta SHA256 `2760ef227eb2d729381057ad02c2a0ac54c3fdc49e99a3a5a22c025b3fb6c145` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p03-full.log` and `/private/tmp/roth-theta-p03-leaneval.log`; machine record
`/private/tmp/roth-theta-p03-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 28 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
