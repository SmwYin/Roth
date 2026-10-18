# Fresh private helper audit: `index_numeric_bound_aux`

Scope: only this private helper plus necessary routine `index_le_lem6` proof forwarding in `Roth/Theta.lean`. This audit contributes **0 original declarations**. No Git mutation, shared report, rename queue or production helper added. The required lean4 and mathlib-quality skills, full cleanup worker workflow, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, and relevant style/naming/profiling references were read. Classic Lean file dialect. The unavailable Skill invocation API is not fabricated: simplify and buzz workflows were performed directly.

## Baseline and first introduction

Inherited baseline is the exact dispatch source SHA `08a24ad6a1f91295e80a640d19f67bcff901c1ef5c03a8c185c6ca9c9643a894`, 934 lines. SAME-SHA complete native LSP evidence is `/private/tmp/roth-theta-lem6/final-lsp.json`: success, partial=false, timed_out=false, failed_dependencies=[], 0 errors, 10 warnings. Inherited accepted uncontended real prefix timings (first/repeat ms): numeric 941.711 / 972.100; public29 700.891 / 675.629; weight 194.730 / 217.380; mapped 668.049 / 733.404. These are explicitly inherited baseline evidence, not newly run doctor calls. Optional cache/linter executables were not invoked. Whole-project baseline and final full build/separate LeanEval remain coordinator gates.

Exact numeric FIRST text: `/private/tmp/roth-theta-lem6/index_numeric_bound_aux-FIRST.lean`, SHA `b0d66a4601abec08b6e80f022298157d65da0dda19a6bc178f83d3a7898569ed`. Exact FIRST clean full source `/private/tmp/roth-theta-lem6/FIRST-compiled-numeric-full.lean`, SHA `b182acef13adc414fa0e27880cf048a66578a83f9afbc6ae42b30f925f8573b8`, original `helper-candidate2.log` exit0. The manifest distinguishes this clean numeric introduction from the earlier weight/mapped file's later numeric errors; no failing whole file is represented as a clean numeric proof.

Fresh independent reproof is `first-contract.lean/log`, exit0: copied exact FIRST proof in `NumericFirstContract.firstNumeric`, independently proved stronger arithmetic theorem, full OLD telescope adapter, opaque values, exact binder names/order/BinderInfo/types/conclusion, universe parameters and standard axioms. The old adapter calls the independently proved stronger arithmetic result, not the original target itself. Final actual built constant is separately checked by suffix, not assumed from a public alias.

All paths below without a directory prefix are under `/private/tmp/roth-numeric-helper/`.

## Result and reasoning

Private API now assumes only `0≤Φ`, `δ≤1`, `3≤rp`, positive `l`, `l≤rp+1`, and the same minimum bound. `hδ0` is removed entirely: even negative δ works. In the quadratic branch, nonnegativity of Φ+δ follows from its bound on a nonnegative square and l>0; `Real.sq_sqrt'` handles √δ²=max δ 0. Direct order lemmas cancel positive l and derive nonnegative Φ+δ. The final nonlinear certificate first proves θ≤2(√Φ+√δ), then linear arithmetic adds Φ. This avoids squaring a target containing Φ and the associated irrelevant mixed monomials. Single-use `hsδ` is inlined; the existing narrative comment is preserved.

Public29's full effective API stays frozen: strict δ bounds and 10/δ<r none remain; its proof forwards δ<1 as δ≤1, derives 3≤r none by `le_div_self` and transitivity, and directly composes the final minimum/subtraction bounds. Public30's entire interface and production proof are untouched. Public29 proof20→22 physical lines; numeric proof15→16 lines, quadratic branch10 lines, linear branch3. Both ordinary declarations remain≤30; no needless branch helper was introduced.

## Full 24-item audit

| # | Item | Concrete result/action |
|---|---|---|
|1|LINT|Inherited whole-file10 warnings; none in the numeric declaration. Final complete LSP and build recorded below. Public hq remains deliberately retained under prior user choice.|
|2|HAVE SCAN|Old hsδ: no by, used once→inline. hsΦ: no by, used twice in final nonlinear certificate→keep. Linear hθ has by→keep. Old hrp10 removed by weaker API. New hsum has no by and is used twice→keep; hsq, h1, quadratic hθ have substantive by proofs→keep.|
|3|SET_OPTION|No production limit/debug/linter options added, removed or raised. Scratch automation uses lower10000 heartbeat budgets only.|
|4|SIMP SQUEEZE|Old terminal simpa for hrp10 disappears; final helper has no simp. Routine caller's existing nonterminal simp only calls stay unchanged.|
|5|NAMING|Descriptive snake_case, private `_aux`, no numeric aux suffix, forbidden abbreviation, scheme number or reversed inequality name. No rename needed/queued/applied.|
|6|LINE PACKING|All signature lines measured in codepoints; complete table below.|
|7|BY PLACEMENT|`by` ends the preceding declaration/have line throughout.|
|8|FORMAT|2-space proof indentation; no blank line inside; no semicolon; no haveI/letI. Quadratic h1/hsq certificates are scoped.|
|9|COMMENTS|1/1 existing narrative comment retained verbatim and still explains δ≤√δ in the linear branch. No original docs/header changed.|
|10|DOCSTRING|Private helper has no docstring, appropriate. Original public docstrings protected.|
|11|VISIBILITY|Private numerical implementation detail, sole caller remains public29; no public wrapper introduced.|
|12|STRUCTURE|Ordinary helper16≤30 lines; branches3/10≤10; no conjunction/exists conclusion. Public29's correlated existential l and facts stay shared.|
|13|MATHLIB|All five actual searches, untruncated full-name grep and clean-prefix automation below; partial sqrt API used directly, no full replacement found.|
|14|JUNK DEF|n/a: proposition-valued lemma, no new definitions.|
|15|EXISTS LEMMA|n/a: no trivial existential witness wrapper.|
|16|SHOW/CHANGE|No show/change in helper. Existing load-bearing cast ascriptions in routine caller retained.|
|17|PUSH_NEG|No deprecated push_neg.|
|18|GENERALISE|Every effective scalar/hypothesis compiled drop/weakening probe below; hδ0 removal, δ≤1 and rp≥3 applied privately.|
|19|INEQUALITY|All inequalities use smaller-left ≤/<; complete occurrence table below.|
|20|NORMAL FORM|Minimum bound, sqrt notation and smaller-left bounds are canonical arithmetic forms; no bespoke predicate.|
|21|SYNTAX GENERALITY|Pure real arithmetic, no polynomial/finite-type baggage. Removed irrelevant positive δ and nonlinear reciprocal condition; old full adapter certified.|
|22|IMPORT FANOUT|No import changed; no new dependency.|
|23|CASTS|No cross-type casts introduced in helper. `(x := δ)` fixes the sq_sqrt' instantiation; explicit `(3 : ℝ)` in routine forwarding fixes numeric type. No redundant ↑ bridge added.|
|24|INSTANCE NAMES|No instances declared, no inherited typeclasses in the effective numeric type.|

## Five actual Mathlib search methods and compiled generic routes

Raw `search-results.json` retains tool responses:

| Method | Actual query | Outcome |
|---|---|---|
|A Lean-Finder|real minimum of linear and quadratic bound implies bound by square roots|5 hits, including two_mul_le_add_mul_sq and Real.sqrt_one_add_le; no whole target.|
|B Loogle|`Real.sqrt, _ + _`|8 hits including Real.sqrt_one_add_le, complex norm and distance formulas; no minimum/rp/l theorem.|
|C LeanSearch|real number bounded by sum of square roots from quadratic inequality|Real.sq_le/sq_lt and Cauchy–Schwarz building blocks, no whole target.|
|D source rg|sqrt_add_le, le_sqrt_of_sq_le, le_sqrt_self_iff, sqrt_mul, rpow_add_le_add_rpow in Real/Sqrt and MeanInequalitiesPow|`grep-search.log`: actual sqrt and rpow building blocks. Pinned sqrt_add_le absent from searched source; no invented name used. Untruncated `full-name-search.log`: no Mathlib index_numeric_bound_aux.|
|E local name search|`le_sqrt`|9 source hits, including Real.le_sqrt_of_sq_le/le_sqrt_self_iff. index=unavailable, explicitly not an index-based absence proof.|

Remote search indexes are discovery aids (Lean-Finder defaults to its v4.28 index); pinned local source and compilation, not a remote empty response, determine retained names. No global absence theorem is claimed.

Auxiliary routes inspected: Real.le_sqrt_of_sq_le, Real.le_sqrt', Real.sq_le, Real.sqrt_mul, Real.sq_sqrt', sqrt self comparison, rpow addition. Common-equivalents lookup has no matching custom predicate/class bucket. Real.rpow_add_le_add_rpow would require exponent rewrites and a broader analysis import without eliminating min/l/rp arithmetic; no import added. The helper is substantive two-branch arithmetic, not a1–3-call wrapper.

`automation.lean/log` uses exact original source prefix ending BEFORE numeric, no import-current-Theta, anonymous examples and separate bounded trials. All10 whole-proof trials fail: grind, aesop, simp_all, exact?, apply? (lower10000-heartbeat timeout), nlinarith, positivity (not a positivity goal), gcongr (no progress), norm_num and decide (free-variable goal). It exited1 as expected; this never certifies any proof/axiom. exact?/apply? follow only anonymous examples, no failed named theorem pollution or circular public29 search. Multi_attempt was not repeated after the documented prior two stalls. Searches establish partial building blocks and bounded failure to find a full replacement; unavailable indexing is not claimed as global absence.

## Generalisation: effective binders and compiled probes

The original effective type has exactly5 implicit real scalars +7 explicit hypotheses, no universes/typeclasses/section parameters. The final type has5 implicit scalars +6 hypotheses. Exact first/full/current types, user-written names, BinderInfo and old adapter are checked in successful positive files.

| Effective original binder | Use | Compiled candidate/evidence | Decision |
|---|---|---|---|
|θ implicit ℝ|subject in min/conclusion|drop_θ in final-binder-negative: unknown identifier with autoImplicit=false|retain; real square root is load-bearing, abstract-field restatement not applicable to this API.|
|Φ implicit ℝ|linear part and sqrt|drop_Φ: unknown identifier|retain.|
|δ implicit ℝ|min RHS and sqrt|drop_δ: unknown identifier|retain; positivity hypothesis removable, scalar itself essential.|
|rp implicit ℝ|quadratic coefficient and l upper bound|drop_rp: unknown identifier|retain.|
|l implicit ℝ|linear coefficient/min and size bound|drop_l: unknown identifier|retain; scalar abstraction already avoids a nat cast.|
|hΦ:0≤Φ|sqrt square identity and final linear step|drop and weaken to0≤Φ+δ fail scoped arithmetic|retain.|
|hδ0:0<δ|old reciprocal and sqrt identity|first `general.lean` verifies0≤δ; `no-delta.lean`, `first-contract.lean` verify complete removal|DROP privately; recover old argument by exact full lambda adapter.|
|hδ1:δ<1|δ≤√δ|weaken toδ≤1 compiles; drop fails unknown hδ1|apply δ≤1.|
|hrp:10/δ<rp|old rp>10 then rp>3|weaken to3≤rp compiles; drop fails;0<rp fails hsq/certificate|apply3≤rp, the actual coefficient threshold.|
|hl:0<l|linear cancellation and deriving Φ+δ≥0|drop fails; weaken0≤l fails|retain strict.|
|hl':l≤rp+1|size in quadratic estimate|drop fails; l≤rp+2 fails|retain.|
|hmin|branch source|drop fails unknown hmin plus branch failures|retain.|

`final-binder-negative.lean/log` compiled15 named negative trials (11 final effective binders +4 additional weakenings), exit1 expected. `final-binder-results.json` associates every declaration's exact source span and all errors; every trial has at least one expected error. Earlier `binder-negative.lean/log` additionally probes the intermediate nonnegative-δ contract. Named negatives are isolated from proof searches and successful proof/axiom files. Trial failure is evidence about attempted proofs, not an unproved claim of mathematical impossibility.

Literature status: **n/a: private declaration, literature search not required** under cleanup2.6d. Inversion check: the helper is already pure arithmetic over arbitrary real θ/Φ/δ/rp/l and contains no distinguished polynomial, point, finite type, source construction or unfolding step; no further concrete-object inversion is applicable. `hδ0` removal is nevertheless certified and applied.

## Concrete additional PUBLIC29 recommendation: QUEUED owner revisit

Owner reviewed and accepted a separate future public29 revisit to `hδ0:0≤δ`, `hδ1:δ≤1`, `hrp:3≤(r none:ℝ)`, retaining the approved nonstrict hratio and explicit hq. **Not applied in this helper checkpoint; not a private handoff blocker.** Owner will implement under a fresh dedicated public29 checkpoint after publication of the current batch; original counts unchanged.

`public-candidate.lean/log` (exact pre-helper source prefix) compiles this precise public candidate and standard axioms. `public-candidate-compatibility.lean/log` copies the ENTIRE immutable `/private/tmp/roth-theta-lem6/actual-compatibility-final.lean` verbatim, then APPENDS the independently built candidate, exact full original29 strict+DecEq lambda adapter (strict hratio→≤), ordinary-name/BinderInfo/universe/result/value/stdaxiom verifiers, and the minimal NEW public30 caller proof with exactly its old telescope. `NumericScratch.candidate_Θ_option_le` forwards the three weakened arguments and hratio.le. Its opaque proof value explicitly contains `NumericScratch.numeric_public_candidate`, verified by expression traversal. Its exact full old30 adapter/type/value/standard axioms pass. The complete independent original30 proof is preserved, not replaced by invoking the current theorem. This corrects the preliminary probe that checked only unchanged actual public30: candidate-call preservation is claimed only from the corrected final exit0 probe,50.921s.

## Every golfing rule (42)

|Rule|Status|
|---|---|
|1.1 by exact|n/a: no by-exact theorem wrapper.|
|1.2 by rfl|n/a: no reflexivity theorem body.|
|1.3 rw+exact|APPLIED RWA for direct positive-l cancellation in the linear branch.|
|1.4 simp+exact|Old terminal simpa removed with obsolete hrp10.|
|1.5 trailing rfl|n/a: no trailing rfl.|
|1.6 constructors|n/a: no constructor conclusion.|
|1.7 apply+exact|n/a: no such sequence.|
|1.8 by_contra!|n/a: no manual contradiction/push sequence.|
|1.9 eta reduction|n/a: no lambda in numeric helper.|
|1.10 single-use have|APPLIED hsδ inlining; hsΦ reused; remaining haves have proof content.|
|1.11 apply+intro|n/a: no such sequence.|
|1.12 redundant show|n/a: no show.|
|1.13 have projections|n/a: no conjunction projections.|
|1.14 merge rw|APPLIED one combined RWA over mul/div/cancellation/commutativity.|
|1.15 terminal simp only|n/a: no helper simp only.|
|1.16 nonterminal simp|n/a: no helper simp.|
|1.17 dot notation|Applied direct `.trans` chains in routine old-contract forwarding; existing .2 root comparison kept.|
|1.18 <\||n/a: no avoidable trailing term parentheses.|
|1.19 push Not|n/a: no push_neg.|
|1.20 trivial exists|n/a: no existential helper.|
|2.1 grind|Actual bounded clean-prefix trial fails.|
|2.2 delete before grind|n/a: no retained grind.|
|2.3 simpa consolidation|Obsolete terminal simpa eliminated by better private arithmetic contract.|
|2.4 fun_prop|n/a: no analytic property goal.|
|2.5 positivity|Whole goal actual trial rejects; square/mixed-product nonnegativity uses explicit lightweight certificates.|
|2.6 gcongr|Actual whole-goal trial makes no progress; multiplication monotonicity is already a direct term.|
|2.7 lia/omega|n/a: real nonlinear goal, no integer arithmetic subgoal; no omega introduced.|
|2.8 aesop|Actual bounded trial leaves goal.|
|2.9 norm_num/casts|Whole norm_num leaves symbolic goal; norm_num directly proves numeric3≤10 in required caller reconstruction.|
|2.10 decide|Actual trial rejects free-variable proposition. No native_decide.|
|2.11 field_simp/ring|n/a: inequality target; div_le_iff₀ and direct order cancellation replace polynomial search.|
|2.12 linear_combination|n/a: no ring/ring_nf terminal proof; scoped nlinarith needs square positivity and sign-sensitive cancellation.|
|2.13 wlog|n/a: linear/quadratic branches are asymmetric.|
|2.14 calc→term|No calc; routine scalar reconstruction uses transitivity directly.|
|2.15 <;>|n/a: no repeated similar subgoals; heterogeneous branches remain explicit.|
|3.1 erw→rw|n/a: neither appears.|
|3.2 fun_prop migration|n/a: no continuity/measurability tactics.|
|3.3 omega→lia|n/a: no omega in helper or added proof.|
|3.4 rcases rfl|n/a: min disjunction branches are inequalities, no equality substitution.|
|3.5 attributes|No simp/grind attribute: specialized internal minimum estimate would add search noise.|
|3.6 simp_all|Actual whole-goal trial fails; no simp_all only retained.|
|3.7 limits|No production maxHeartbeats/maxRecDepth added or raised.|

Step-back reflection: exact?/apply? and generic automation do not replace the arithmetic. A sqrt-of-sum/rpow route would add normalization/import work; the split square certificate gives a direct normal form and avoids a helper cycle. Removing the reciprocal condition reveals the actual rp≥3 threshold. No new private wrapper just to shorten a ten-line branch. Simplify outcome **ISSUES-FOUND-AND-FIXED** directly: unnecessary positive-δ assumption and mixed final-square monomials removed; single-use hsδ inlined; docs/comments preserved. Native `/simplify` command is unavailable, so no external skill invocation is claimed.

## Measured signature packing

Reference: successful `#check @NumericFirstContract.numericGeneral` at format.width100 in first-contract.log prints exactly5 implicit real parameters, then the6 explicit hypotheses and unchanged θ-bound. The built constant's full names/types/BinderInfo are independently compared to this telescope by actual-tail.

| Signature line | Codepoints | Next complete group | Arithmetic | Action |
|---|---:|---|---|---|
|519|96|`(hl : 0 < l)`12|96+1+12=109>100|ok|
|520|93|`θ ≤ 2 * (Φ + √Φ + √δ) := by`27|93+1+27=121>100|ok|
|521|31|proof body next|n/a|ok|

No wide-hyp escape invoked. Conclusion participates in packing. Entire helper and added caller lines≤100 codepoints.

## Complete inequality occurrence scan

| Location | Inequality | Orientation/action |
|---|---|---|
|hΦ|0≤Φ|smaller-left, keep|
|hδ1|δ≤1|smaller-left, keep|
|hrp|3≤rp|smaller-left, keep|
|hl|0<l|smaller-left, keep|
|hl'|l≤rp+1|smaller-left, keep|
|hmin|min(lθ/2)(rpθ²/3)≤l(Φ+δ)|smaller-left, keep|
|conclusion|θ≤2(Φ+√Φ+√δ)|smaller-left, keep|
|reversed occurrences|n/a: zero≥/> in signature or body|no rewrite/rename|

## Public/source protection and actual proof evidence

`actual-compatibility-final.lean` is an exact verbatim copy of the supplied immutable compatibility artifact, followed only by appended FIRST private proof, stronger independent numeric proof, FIRST full adapter, and ACTUAL private suffix/type/value/full-old-adapter checks. Its inherited verification also checks **all** actual new retained helper opaque values and standard axioms, and deleted `coeff_det_le_lem6M_aux` absence. The private constant is located by suffix programmatically; opaque values use `value! true`, never default `value!`. Independent old29 strict+DecEq proof and **entire** old30 proof/contract remain untouched, and actual public29/public30 values and exact old adapters are rechecked.

The first final compatibility attempt had a scratch record-layout parse error (actual-compatibility-first-failed.log); it is explicitly not success evidence. The corrected final run, its clean raw output and all pass markers are the certification. No error/PANIC/sorryAx or unsupported axioms are allowed in a positive final log. Successful standard axiom sets are subsets of propext, Classical.choice, Quot.sound.

New external names in the source diff: `Real.sq_sqrt'` and `le_max_left` are verified by actual Mathlib source and compiled module/independent proof; `sub_nonneg` by the compiled scoped certificate; `le_div_self` by source-existing usage, compiled reconstruction and compiled exact old adapters. Numeric type ascriptions are load-bearing. No new imports/definitions/instances/attributes/options, no unrelated declaration change. Production scope is the private helper, necessary routine public29 forwarding and owner-approved routine final inequality composition only. Exact public29 and public30 effective types are recovered by final actual compatibility, including their section instances.

Final live native LSP preserves all10 unfiltered warnings: header1; retained unused hr/hB lines93,101(two),109,129,252; original30 DecidableEq section warning578 and type warning575; retained user-required hq546. No warning falls in the numeric declaration. These preexisting/scoped public choices are not silently removed in this private audit. Raw final-lsp.json has the full messages, categories, and positions, success=true, partial=false, timed_out=false, failed_dependencies=[],0 errors. No filtered diagnostics request was used.

Phase3 file-level fixes: n/a single-declaration scope; original header/imports/docs untouched. Phase5a: no Mathlib replacement or junk wrapper; additional PUBLIC29 weakening is concretely verified and QUEUED for owner revisit, not applied. Phase5b rename pass: no candidate, no sidecar mutation. Refactoring needed for this private checkpoint: none. Owner full `lake build` and separate `lake build Roth.LeanEval` remain pending coordinator execution after all three independent helper audits; neither is claimed done here.

## Trace-driven direct-order stage

The first syntax-preserving performance idea (split sqrt certificate with old numeric API) compiled and measured numeric800.588ms in candidate-profile.log, an exploratory exact prefix through numeric only, not an accepted final all4 sweep. After genuine private API weakening, the first complete all4 trace at SHA `db2d07831e365f67f4d5dab2aae95c582553a4d6a093224afffdd6e27f067dc9` gave numeric 963.521ms / public29 813.037 / weight 206.976 / mapped 648.537. Raw source, log, manifest, timings and full LSP are preserved as **pre-direct-*** artifacts; these are explicitly intermediate evidence.

That trace attributed164ms to nonlinear positive-l cancellation,188ms to deriving Φ+δ≥0, and222ms to public29's final broad linear normalization. These are routine ordered-field consequences. The final stage uses combined RWA with pinned `mul_le_mul_iff_right₀`, `nonneg_of_mul_nonneg_right` plus explicit nonnegative multiplication/division, and owner-approved direct public29 transitivity with `sub_le_iff_le_add`. The first scratch spelling `mul_le_mul_left hl` failed because the pinned name means multiplication monotonicity rather than cancellation; direct-linear.log/direct-both.log retain that failure. Corrected direct-selected-prefix.lean/log exit0 validates both numeric changes and the public29 composition. No failed scratch is used as positive evidence.

Fresh FINAL `lake build Roth.Theta` on the direct stage exited0 in43.958951417s; fresh actual compatibility exited0 in66.401280584s, recorded in direct-final-gate-status.json. **Current-source positive actual log is direct-actual-compatibility-final.log**, not the earlier pre-direct actual-compatibility-final.log. A further complete unfiltered native final LSP passed on the direct stage,0errors10warnings/no partial/no timeout/dependency failures. Every ordinary request was then drained before real final all4 trace, with a repeat only if a CURRENT-SHA target is≥750ms.

| New/direct external identifier | Verification |
|---|---|
|Real.sq_sqrt', le_max_left|Actual pinned source rg, independent first/stronger proof and compiled final module|
|mul_le_mul_iff_right₀|Exact pinned GroupWithZero/Defs source, corrected prefix compile and final module|
|nonneg_of_mul_nonneg_right|Exact pinned Ring/Unbundled/Basic source and final module|
|div_nonneg, sub_nonneg|Compiled final scoped direct certificates and actual opaque-value checks|
|mul_div_assoc, div_le_iff₀, mul_comm|Compiled corrected RWA prefix and final module|
|sub_le_iff_le_add|Compiled prefix/final public29 composition and actual public value/stdaxiom check|
|le_div_self|Compiled exact old adapter and production public29 reconstruction|

Public terminal `simpa [mul_add]` is unsqueezed. No production terminal simp-only introduced. This stage increases numeric physical body15→16 to remove polynomial search; performance has priority over cosmetic line savings. The exact first contract and final actual type do not change between the pre-direct and direct stages.


## Final uncontended real all4 profiles / buzz

Both runs use the REAL Lean4.34 command `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Each source is the exact ENTIRE production prefix through public29, preserving every preceding import/declaration/context and closing **end Lemma6 then end Roth**. No import-current-Theta shortcut, masking, raised limit or production profiling scaffolding. All ordinary/compiler/LSP requests drained before profiling; the two Lean processes ran sequentially. These certify prefix-only performance, not the later full-module/whole-project sweep.

Every total sums the outer declaration command plus its associated disjoint top-level async proof/kernel/addDecl/linter jobs. Nested Meta/tactic nodes are not double-counted. Raw UTF8 logs and exact node/line anchors are in final-timings.json and repeat-timings.json.

| Declaration | Inherited first/repeat ms | Final ms | Required repeat ms | Final outer/proof log lines | Repeat outer/proof lines |
|---|---:|---:|---:|---|---|
| index_numeric_bound_aux | 941.711 / 972.100 | **787.045** | **810.470** | 1220519 / 1220564 | 1221211 / 1221256 |
| index_le_lem6 | 700.891 / 675.629 | **843.584** | **839.167** | 1328718 / 1328800 | 1329464 / 1329546 |
| weight_le_delta_aux | 194.730 / 217.380 | **228.983** | **191.727** | 1088354 / 1088383 | 1089054 / 1089083 |
| mapped_det_ne_zero_aux | 668.049 / 733.404 | **637.956** | **643.007** | 1118117 / 1118220 | 1118819 / 1118922 |

final-profile.log: exit0, 172.352474375s wall, 152457353 UTF8 bytes; prefix SHA `2961a79906e4ddf5be55deb984ca6a238195075e2dbac332078ebebf126e23f5`; full/live SHA `c1aa9de515850c72246fb7e8ef531937ceaa5616dcbd155f808d00dd2a468691`.

repeat-profile.log: exit0, 171.014639250s wall, 152516838 UTF8 bytes; prefix SHA `2961a79906e4ddf5be55deb984ca6a238195075e2dbac332078ebebf126e23f5`; full/live SHA `c1aa9de515850c72246fb7e8ef531937ceaa5616dcbd155f808d00dd2a468691`.

The CURRENT-source first numeric 787.045 / public29 843.584 trigger the≥750ms repeat rule. The sequential driver was conditional: all4<750ms would have skipped a second Lean invocation; the actual current timings required the repeat. The earlier different-source963/813 numbers were not used to justify repetition. All4 current targets pass1000ms in both runs. The public29 trans proof is mathematically direct, but no public timing improvement is claimed against pre-direct813.037ms; the numeric arithmetic is improved and strictly more general.

Buzz outcome: **FIXED** scoped nonlinear cancellations replaced by direct order certificates; no remaining over-budget declaration among all4 measured targets. maxHeartbeats raises removed0, added0. No performance deferral, no decompose flag, no new production helper. Native buzz/Skill API unavailable; its real trace workflow performed directly.

## Final gate status

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|PASS|Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,43.958951417s, current SHA; direct-final-module-build.log|
|independent FIRST/full-old private adapter|PASS|Exact immutable FIRST proof independently recompiled; full binder names/order/BinderInfo/universes/conclusion recovered; first-contract plus current actual compatibility|
|actual opaque values/standard axioms|PASS|direct-actual-compatibility-final.log exit0,66.401280584s; actual numeric and ALL new helpers checked; deleted wrapper absence; only propext/Classical.choice/Quot.sound|
|public theorem/definition protection|PASS|Exact unchanged public29 signature, full original strict+DecEq adapter; ENTIRE independent original30 proof/type/value/stdaxioms; no definition/import/header/doc change|
|structure_gate|PASS|Numeric16≤30, branches3/10; public29 ordinary22≤30; no new helper; shared existential l preserved|
|naming_gate|PASS|Private descriptive `_aux`, no forbidden pattern/abbreviation, no rename|
|line_packing_gate|PASS|All3 signature rows measured, next complete group would exceed100|
|inequality_orientation_gate|PASS|All7 signature inequalities audited, zero≥/> in code|
|scope/no unintended breakage|PASS|Exact prefix before numeric and suffix from public30 unchanged; sole caller proof compiled; current module and exact public adapters pass|
|final native LSP|PASS|COMPLETE unfiltered success,partial=false,timed_out=false,deps=[],0 errors/10 recorded inherited warnings|
|real all4 final+repeat profiles|PASS|Both exit0 on same current full/live SHA, exact same entire prefix; each declaration<1000ms, current≥750 repeat honored|
|owner full build/separate LeanEval|PENDING OWNER|Not run/claimed by this helper leaf; owner executes after all3 fresh helper audits|
|PUBLIC29 boundary weakening|QUEUED OWNER REVISIT|Concrete candidate+minimal new old30 caller+exact old adapters/type/value/stdaxes and actual candidate dependency verified; no live public type edit here|

## Eleven-step phase checklist

- [✓] Step1: all required skill/cleanup/reference documents read.
- [✓] Step2: full24-item audit report.
- [✓] Step2.5: all5 actual Mathlib search methods, generic routes and honest limitations.
- [✓] Step2.6: every effective original/final parameter compiled drop/weakening coverage, private literature exemption and inversion check.
- [✓] Step2.7: every signature line's codepoint packing arithmetic.
- [✓] Step2.8: complete inequality occurrence scan.
- [✓] Step3: all42 golfing rules with concrete action or n/a reason.
- [✓] Step4: holistic simplify/alternative-strategy reflection and measured direct-order optimization.
- [✓] Step5a: fresh COMPLETE unfiltered native diagnostics,0 errors.
- [✓] Step5b: all protection/content/actual value/standard axiom/build/real profile gates.
- [✓] Step6a: no rename needed, no sidecar mutation.

Overall **private helper PASS**, contributes **0 originals**. Source934→936 lines, net+2 (private signature4→3, numerical proof15→16; required caller proof20→22); increased explicit order reasoning avoids heavy nonlinear search. Original comments1/1 preserved. No original/public declaration removed or renamed, no new helper.

Source edits are now **frozen/revoked** and all compiler/LSP/profile requests are **drained**. Final SHA256 **`c1aa9de515850c72246fb7e8ef531937ceaa5616dcbd155f808d00dd2a468691`**. Coordinator full build/separate LeanEval, remaining private helper audits, and the queued public29 dedicated revisit remain coordinator work, not hidden pass claims.
