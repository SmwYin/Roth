# Fresh private audit: mapped_det_ne_zero_aux

Scope: this private helper only, independently audited after the accepted weight audit. Original-declaration contribution **0**. No Git operations, shared report/rename-queue writes, public API edits, retained public hypothesis changes, new helpers, import changes, or DomainCommSemiring revisit. The ordinary proof cap is30; this is not a module Main result.

I read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full, the Lean/mathlib-quality skills, full cleanup workflow, and relevant style/naming/profiling references. Session instructions override older approval/threshold/profiler syntax in those documents.

## Baseline and provenance

Start source SHA `aad8c2999fcfb469c9d3cf75ed3913884d3797923abf8d6653c2b9c67e0d82fc`,937 lines, mapped14/weight12/numeric16/public29body22. Accepted identical-SHA baseline inherited explicitly from `/private/tmp/roth-weight-helper/final-lsp.json`: complete unfiltered native LSP, success=true,partial=false,timed_out=false,deps=[],0errors/10warnings. Inherited REAL exact global-prefix profiles (final/repeat ms): mapped661.006/664.630,weight336.843/356.888,numeric941.689/875.463,public951.482/856.651. These are inherited, not fresh measurements. Owner full build/separate LeanEval remain owner work.

FIRST provenance: `/private/tmp/roth-theta-lem6/first-manifest.json`, exact `mapped_det_ne_zero_aux-FIRST-with-context.lean`, SHA `52d001067f8c51f34e14f870145f76fef796676f8957788a239ca36c00cb6104`. Original context already omits Fintype/DecidableEq. The first full candidate had later numeric errors; it is not reported as a whole-file pass. `first-contract.lean` recompiles the exact first proof independently against the clean exact production prefix BEFORE the target, closes Lemma6 then Roth, exit0. Searches likewise use this clean prefix and anonymous examples; no import of current Theta or later public29 theorem.

Mathematics: commute coefficient mapping with the determinant and Hasse derivatives; injectivity of coefficient mapping reduces to the integer determinant, its given separated factorization, and injectivity of the variable renamings and polynomial/one-variable equivalence. Both factors must be nonzero. This uses more than1–3 mathlib calls and project Hasse/separation API, so it is not a trivial wrapper.

## Changes / simplify and rejected performance variant

Final retained change is signature packing only: move the D binder to line498 and hV to line499 after measured underpacking. The exact original14-line rw/congr/Matrix.ext certificate is restored. Source937→937, body14→14, effective telescope/order/BinderInfo/names/universes unchanged. No comments/docstrings existed on helper; surrounding narratives untouched.

A compiled alternative replaced the3-tactic determinant certificate with terminal `simp [RingHom.map_det, Matrix.map, hasseDeriv_map]`, body14→12. First simp without Matrix.map failed, corrected candidate2 compiled. Frozen rejected source04171753 had clean module/actual/LSP gates, but first real all4prefix timings mapped1010.205/weight694.343/numeric1292.465/public1247.211ms exceeded budget; required same-SHA repeat mapped779.268/weight421.974/numeric915.361/public907.739ms passed. Owner rejected retaining a2-line simplification with no substantive benefit after a legitimate failed sweep, explicitly regranted source authority ONLY to restore the14-line certificate and rerun final gates, retaining packing. Coordinator independently confirmed. No overbudget run is silently converted into success; both rejected sweeps and all raw evidence are immutable under `rejected-simp-04171753/`. The source was re-frozen immediately after this narrow correction; no numeric/public edits.

Holistic simplify outcome PASS-THROUGH for proof / PACKING FIXED: typed hmapdet isolates determinant functoriality; original direct rw/congr/ext proof retained for its explicit transport structure. No duplicated skeleton needs extraction, no new helper. Full automation searches did not replace the proof. A fully nested term obscures the injectivity transports with no demonstrated gain. Direct workflow performed because no built-in simplify callable is exposed.

## All24 audit items

|#|Item|Substantive result|
|---:|---|---|
|1|Lint|No warning on assigned helper in inherited complete LSP; fresh final native evidence below. Inherited10 public/header warnings retained per user decisions.|
|2|Have scan|Only hmapdet, typed proof-bearing have used once; retain to isolate determinant functoriality. No single-use term have.|
|3|set_option|None in assigned production declaration; no limit raises added.|
|4|Simp|Original terminal simp inside Matrix.ext retained unsqueezed; rejected consolidated variant documented above. No nonterminal bare simp.|
|5|Naming|Descriptive snake_case mapped determinant nonzero, private `_aux`, no numbered scheme/forbidden abbreviation; no rename.|
|6|Packing|Measured7-line signature table below; fixed two underpacked binder groups.|
|7|by|At end of signature/have line.|
|8|Format|2-space tactics, no blank proof lines or semicolon chain, lambdas↦, widths≤100.|
|9|Comments|None in target;0removed; all surrounding source/comments preserved.|
|10|Doc|Private helper correctly has no docstring.|
|11|Visibility|Private and only used by public29 in same file.|
|12|Structure|14≤30 proof lines, local hmapdet proof3lines, no branching/∧/∃ output; no decomposition needed.|
|13|Mathlib|All5 actual search routes and clean generic compiler searches below; partial match only.|
|14|Junk def|n/a theorem, no data definition.|
|15|Exists|n/a nonvanishing theorem, no existential wrapper.|
|16|show/change|Neither present.|
|17|push_neg|Absent.|
|18|Generalise|Every effective binder probed; class omissions already present; generic coefficient alternative assessed below.|
|19|Inequality|No ordered inequalities; ≠ nonzero is correctly oriented; table below.|
|20|Normal form|Nonzero determinant and factor nonzero are standard forms; no new equivalence/simp tag.|
|21|Syntax generality|Existing hF is exactly the separated factorization furnished by caller; generic det≠0 assumption would discard useful content and merely shift proof work to caller.|
|22|Import fanout|No new imports.|
|23|Casts|0cast edits; Fin→ℕ ν coercion genuinely cross-type, X none target ascription fixes coefficient/variable ring.|
|24|Instance names|No declared instances; no synthetic name scaffolding.|

## Five ACTUAL Mathlib search methods

Raw results `/private/tmp/roth-mapped-helper/search-results.json`.

|Method|Actual query/result|
|---|---|
|A LeanFinder|nonzero determinant of Hasse derivative matrix mapped integer polynomial to reals with separated variables factorization;5results including det_mvPolynomialX_ne_zero (different matrix), no full replacement.|
|B Loogle|RingHom.map_det; exact generic functoriality theorem, used directly in certificate.|
|C LeanSearch|MvPolynomial map injective rename aeval X nonzero determinant; map_injective/rename_injective/map_injective_iff building blocks, no full separated-Hasse result.|
|D source rg|Full untruncated target-name Mathlib search empty; map_det/hasseDeriv_map/aeval_X_eq_rename search in determinant/MvPolynomial sources finds map_det; project search identifies latter two in Roth.HasseDeriv/Separation. Full logs saved.|
|E native local search|map_det returned5names including RingHom.map_det. Symbol index reports unavailable, so empty results would not establish absence; actual returned matches used only for presence.|

Auxiliary variants map_injective_iff, rename_injective, map_ne_zero_iff, map_eq_zero_iff, RingHom.map_det checked in searches and selected proof compiler. Clean exact?/apply? anonymous examples run against exact prefix BEFORE helper (`automation.lean/log`). exact? fails; apply? suggests `refine ne_zero_iff.mpr ?_`, leaving a nonzero-coefficient witness (no theorem proving the content), then default heartbeat timeout while elaborating suggestion. Grind fails with remaining determinant/equality facts, aesop and simp_all leave nonzero goal, positivity cannot prove nonzero. No claimed global mathematical absence theorem; no full replacement found by these bounded methods. Known native multi_attempt stall limitation inherited and avoided per dispatch; ordinary compiler fallback used for these bounded tests, with no resource raises.

## Generalisation, every effective binder

Negative compiled probes `binder-negative.lean/log`: τ omission rejects referenced section variable; all R,l,D,U,V syntactic removals use autoImplicit=false and produce the expected unknown-identifier dependency failures; hU removed fails at use, hV removed leaves V≠0 unresolved, hF removed fails at factorization rewrite. Expected-failure file exit1 is not positive proof/axiom evidence. V removal also reaches default200000 heartbeat timeout; it does not certify impossibility. These are proof drop-tests, not claims that every imaginable restatement is impossible.

|Binder|Role / drop or weakening probe|Decision|
|---|---|---|
|τ : Type u|Referenced by R,D,U, variable renaming; `omit τ` error; universe-polymorphic already.|Keep; no type variable can disappear while target uses it.|
|R|Polynomial under derivatives, target and hF depend; drop fails with autoImplicit=false.|Keep.|
|l|Matrix dimension; D, Fin l and determinant depend; drop fails.|Keep.|
|D|Derivative row multi-indices; drop fails.|Keep arbitrary map (no injectivity/degree/finite τ assumptions).|
|U|Separated factor; hU/hF depend; drop fails.|Keep arbitrary polynomial.|
|V|Other factor; hV/hF depend; drop fails.|Keep arbitrary polynomial.|
|hU|Required factor nonzero; drop fails. True weakening tested separately; zero U yields zero factorization even if V=1.|Keep.|
|hV|Required second factor nonzero; drop leaves goal. True weakening tested separately; zero V yields zero factorization even if U=1.|Keep.|
|hF|Determines integer determinant; drop fails; without hF choose R=0 and U=V=1.|Keep equality supplied by actual caller.|
|Fintype τ/DecidableEq τ|Not effective binders: exact FIRST and actual final omit them; independent first proof compiles without them.|Already removed, no fictional new improvement claimed.|

Positive counterexample building blocks and generic coefficient alternative in positive-extra.lean are kept separate from expected-failure tests. They establish the zero1×1 determinant, zero-factor products, and nonzero unit factors in the R=0 case. No unsupported proof of absolute logical minimality is claimed.

Generic coefficient alternative: compiled the12-line variant of the same argument over arbitrary A,B with CommRing A,IsDomain A,CommRing B, an injective f:A→+*B. This is mathematically sensible but adds7effective binders (A/B,3classes,f,hf replace concrete casting) and requires every caller to supply injected hom/domain context. There is one real caller, over ℤ→ℝ, and no downstream generic use. The existing statement already permits arbitrary τ,D,R,U,V with no ambient finite assumptions. Recommendation: retain concrete private statement; do not add an unused second helper or churn its signature. This is an assessment of actual benefit, not a prohibited public DomainCommSemiring revisit.

Inversion check: hmapdet abstracts determinant transport, but that operation is already RingHom.map_det; the remaining chain specifically uses Hasse derivative map compatibility, the separated Option-variable factorization and injective renamings. An abstract injective-hom nonvanishing statement is map_ne_zero_iff/map_injective, already used. No new abstraction yields a new useful theorem or shorter actual caller. Literature: n/a private declaration, public-literature pass exempt; no web absence assertion.

## Line packing / inequality

Width reference: #check @firstMapped at format.width100 in first-contract.log and actual final log. Complete following binder/expression units are measured, rather than splitting a token from its dependent type.

|Signature line|Codepoints|Next complete unit|Arithmetic|Action|
|---:|---:|---|---|---|
|498|99|{U : MvPolynomial τ ℤ},22|99+1+22=122|ok|
|499|71|hF opening matrix binder expression,34|71+1+34=106|ok|
|500|38|hasseDeriv…R).det =,72|38+1+72=111|ok|
|501|78|rename…V) :,74|78+1+74=153|ok|
|502|82|Matrix.of…+,63|82+1+63=146|ok|
|503|67|Finsupp.single…:=by,71|67+1+71=139|ok|
|504|77|proof follows|n/a|ok|

The first baseline line76+1+D22=99 and second81+1+hV12=94 required repack; both applied. Final hF spans180chars and its opening matrix binder expression alone needs34chars; no wide-hyp escape is used.

|Inequality occurrence|Location|Result|
|---|---|---|
|none|entire signature/hypotheses|No ≥ or >. Three ≠ occurrences express nonzero; no _ge_/_gt_ name.|

## Every42 golfing rules

|Rule|Result|
|---|---|
|1.1|n/a no by-exact wrapper.|
|1.2|n/a no by-rfl.|
|1.3|Final rwa already combines rewrite and closure.|
|1.4|n/a no simp/exact pair.|
|1.5|n/a no trailing rfl.|
|1.6|n/a no constructor.|
|1.7|n/a no apply/exact pair.|
|1.8|n/a no contradiction.|
|1.9|Remaining injectivity lambda proves Unit equality; no eta reduction. Matrix.ext lambda retained; rejected simplification removes it but failed performance acceptance.|
|1.10|hmapdet proof-bearing have retained, not single-use term have.|
|1.11|n/a no apply/intro.|
|1.12|n/a no show.|
|1.13|n/a no conjunction projections.|
|1.14|Consecutive proof rewrites separated by injectivity subgoals; cannot merge through refine. Inner certificate has a single rw followed by congr/ext.|
|1.15|No terminal simp only; original terminal simp left unsqueezed.|
|1.16|No nonterminal bare simp.|
|1.17|Existing .2 equivalence projections direct; no verbose applicable namespace chaining.|
|1.18|No trailing proof parentheses needing <|; theorem arguments naturally parenthesized for .2.|
|1.19|No push_neg.|
|1.20|Not existential.|
|2.1|Actual grind whole theorem failed, automation.log.|
|2.2|n/a selected proof has no grind.|
|2.3|Compiled consolidation to simp; first variant failed, Matrix.map variant compiled, rejected after profiling.|
|2.4|n/a no analytic function property.|
|2.5|Actual positivity failed to prove nonzeroness.|
|2.6|n/a no ordered inequality/monotonicity.|
|2.7|n/a no arithmetic constraint.|
|2.8|Actual aesop left determinant nonzero goal.|
|2.9|n/a no numeric/cast arithmetic; counterexample simp separately tested.|
|2.10|No executable decidability for symbolic polynomial nonzero.|
|2.11|n/a no denominators.|
|2.12|n/a no ring/ring_nf or linear polynomial identity.|
|2.13|n/a no symmetric branches.|
|2.14|n/a no calc.|
|2.15|n/a no repeated multiple goals.|
|3.1|No erw.|
|3.2|No continuity/measurability.|
|3.3|No omega or integer arithmetic.|
|3.4|No rcases/rfl.|
|3.5|Private one-caller technical fact; no new automation attribute justified.|
|3.6|Actual simp_all failed on full theorem; no simp_all only in selected proof.|
|3.7|No production maxHeartbeats option to remove/add.|

Step back: direct existing Mathlib building blocks are appropriate; no one-tactic full proof found. No thin-wrapper deletion candidate, new helper, missing abstraction or required rename. Caller proof unchanged, public29body22; mapped14/weight12/numeric16 unchanged. All public docstrings and user-retained wrappers/hypotheses preserved.

Verifier correction: the first appended actual tail placed a structure field after `{` at incompatible indentation, producing a parser error at1649. The immutable inherited prefix and production source were untouched. Corrected the appended metaprogram to the multiline structure syntax, preserved first-attempt log separately, and reran the complete actual compatibility source. Only the clean corrected run is positive certification.


## Fresh final gates and real performance

All normal compiler/build/LSP requests were terminal before profiling. REAL Lean4.34 command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Source is the exact full production prefix through public29, retaining all preceding imports/context/declarations, with `end Lemma6` then `end Roth`. These are prefix-only performance certificates; no later whole-module timing sweep claimed. Totals sum the outer Elab.command and associated disjoint top-level Elab.async proof/kernel/compiler/linter nodes, excluding nested doublecount. Actual anchors saved in timings JSON.

|Declaration|Inherited ms (final/repeat)|Fresh final ms|Required repeat ms|Final/repeat outer log line|
|---|---:|---:|---:|---|
|mapped_det_ne_zero_aux|661.006/664.630|707.126|651.477|1134311/1135947|
|weight_le_delta_aux|336.843/356.888|408.013|361.605|1086825/1088434|
|index_numeric_bound_aux|941.689/875.463|939.576|873.525|1236612/1238213|
|index_le_lem6|951.482/856.651|895.050|854.163|1346088/1346386|

final: exit0,172.263273s wall,154945859rawUTF8bytes,prefixSHA `eee4cecc7c2da79b21374267e46ddda0a774fbe412dcb6b8fa20125adb2879ac`,full/liveSHA `47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`.

repeat: exit0,169.332299s wall,154967373rawUTF8bytes,prefixSHA `eee4cecc7c2da79b21374267e46ddda0a774fbe412dcb6b8fa20125adb2879ac`,full/liveSHA `47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`.

The first final-SHA timing table was inspected before repeat; at least one target≥750ms required repeating on the same final SHA. Both fresh CURRENT-SHA runs pass1000ms for all4targets. Earlier overbudget0417 variant is rejected history only, documented separately; no source scaffolding or limit raises. Buzz FAST-BOARD.

|Gate|Result|Evidence|
|---|---|---|
|final-module-build|PASS|Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,41.227689s,currentSHA;final-module-build.log|
|actual-compatibility-final|PASS|Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-mapped-helper/actual-compatibility-final.lean` exit0,57.773713s,currentSHA;actual-compatibility-final.log|
|Fresh complete unfiltered native LSP|PASS|success=true,partial=false,timed_out=false,deps=[],0errors/10warnings; final-lsp.json. No filtering.|
|Independent FIRST / full old adapter|PASS|Exact saved first-context proof independently recompiled exit0; final actual tail repeats it. Full effective telescope/order/BinderInfo/ordinary names/common positional universes/conclusion checked and exact full old λ adapter verified.|
|Actual values / axioms|PASS|Private suffix located programmatically, unique actual constant; opaque value!true checks plus standard axioms only. Entire inherited original29 and original30 independent proofs/adapters, all other private actual checks, deleted coeff wrapper absence preserved byte-identically and recompiled.|
|Definitions / public statements|PASS|No definition/import/public statement/docstring/visibility changes. Only target proof and signature wrapping altered. No effective private API change.|
|Structure|PASS|Mapped14≤30, local proof3, no branches; weight12,numeric16,public29body22 unchanged. No new helper.|
|Naming|PASS|Descriptive private snake_case _aux; no forbidden name/abbreviation; no queue writes.|
|Packing / inequality|PASS|All7measured signature rows,≤100codepoints; two binder repacks applied. No≥/> code occurrences.|
|Compatibility source provenance|PASS|`/private/tmp/roth-mapped-helper/actual-compatibility-final.lean` starts with ENTIRE immutable accepted `/private/tmp/roth-weight-helper/actual-compatibility-final.lean`; mapped tail appended. Exact prefix SHA/bytes in compatibility-provenance.json.|
|Scope / caller effects|PASS|No caller proof needed; Roth.Theta builds; actual old29/ENTIREold30 independent sources and adapters compile. Protected public hq/domains/wrappers/globalΘ hB/hr retained.|
|Real all4 performance|PASS|Both fresh current-SHA exact-prefix runs under1000ms for all4; required≥750 same-SHA repeat honored. Rejected0417history preserved.|
|Requests / freeze|PASS|Source edits frozen/revoked; all compiler/LSP/profile requests terminal/drained before report; source-freeze.json + freeze-manifest.json.|
|Owner full build / separate LeanEval|PENDING OWNER|Not run/claimed here. Owner runs sequential full lake build then separate Roth.LeanEval after fresh helper batch.|
|Queued public29 boundary revisit|PENDING OWNER, NOT THIS LEAF BLOCKER|Still strict δ/rp10δ; approved hratio≤/DecEqdrop and hq retention preserved. Separate fresh public29 revisit after this batch/push.|

Ten inherited native warnings concern user-retained header metadata/public arguments and old30 decidability binders; none belongs to assigned helper. No suppressions/masking. Negative tests are explicitly expected-failure artifacts, not positive evidence. Weak hU/hV→True probes fail with argument type mismatch or unresolved nonzero goal; generic/counterexample positive file passes separately with standard axioms. The generic variant is assessed but not recommended for production because no concrete extra caller benefits.

## Eleven-step checklist

- [✓] Step1: skills/full workflow/required refs read.
- [✓] Step2: all24 substantive audit entries and have/simp/comments.
- [✓] Step2.5: all5 actual searches, auxiliary variants/full-name scan, clean generic compiler search.
- [✓] Step2.6: every effective binder drop/weakening probe, positive generic/counterexamples, private-literature exemption and inversion check.
- [✓] Step2.7: all7signature packing arithmetic rows, two repacks.
- [✓] Step2.8: full inequality occurrence/orientation table.
- [✓] Step3: all42 golf rules and actual relevant automation trials.
- [✓] Step4: whole proof/helper/term/generic alternatives and holistic simplify assessed.
- [✓] Step5a: fresh complete unfiltered native final diagnostics.
- [✓] Step5b: module/actual compatibility/old values/axioms/protection/style and all4real current-SHA first/repeat performance gates pass.
- [✓] Step6a: no rename needed, no queue/Git/shared report writes.

Overall PRIVATE HELPER PASS, contributes0original count. Owner-authorized narrow restoration completed; both fresh final-SHA timing sweeps pass. Proof14→14/source937→937 (0); no new helpers or effective type changes. All source edit authority is revoked, all requests drained. Owner full build/separate LeanEval and public29 revisit remain owner work.

Final source SHA256 **`47369dc4b524f54d2981a0c23e67786b442f061e86c1ec2f6141d6c46fb62c69`**. Raw evidence `/private/tmp/roth-mapped-helper/`.
