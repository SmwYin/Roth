# Dedicated performance revisit: `index_numeric_bound_aux`

Scope: the existing private numerical proof only. The complete signature, arbitrary-negative-δ generality, entire public `index_le_lem6` declaration/proof and every other source byte remain unchanged. No new helper, API, import, option, axiom, rename, Git or shared-log mutation. Counts remain216/264,Theta35/35,completed files9/14; this revisit adds0 originals. The original helper audit remains authoritative historical evidence; its old public29 strictδ/10 cutoff discussion is historical, not the current approved API.

Fresh artifacts are under `/private/tmp/theta-numeric-performance/` unless an absolute path is given. Native Skill/slash invocation is unavailable; the cleanup/simplify/buzz workflows are performed directly, with actual compiler/native/profile evidence. Required lean4/mathlib-quality skills, cleanup/buzz workflows, full golfing/proof-pattern/search/generality/gate references and relevant style/naming/profiling sections were read.

## Baseline and immutable evidence

Inherited published HEAD `9f47150a49ad97995f793b912f3fc077379528c0`, source/audit checkpoint `ebb1021e9d72fc5aade7a9657a4a4b3e27c63616`. Dispatch confirms clean publication, full build83.979s THEN separate LeanEval35.554s and all17 pins. These are inherited evidence, not fresh leaf commands. Baseline Theta SHA256 `3631ff20d25efdec5d9a846640a8c5a4f5efcac876a37dfee83e39c638fcfcde`; exact same-source prior complete native diagnostics in `/private/tmp/theta-separated-performance/v2/native-theta-final.json` (success,partial=false,timed_out=false,0errors,8warnings) serve as baseline doctor under the explicit reuse rule. Optional cache/linter executables were not run.

Latest actual whole-file numeric total1097.018ms = outer command47.851 + associated async proof982.063 + addDecl30.550 + linter36.554. Exact selected UTF8 bytes120087437..131524962, raw/source/table at `/private/tmp/theta-separated-performance/v2/actual-profile-final-first.{log,json}`, `-table.json`, `final-Theta.lean`; copied strict slice and complete row are `inherited-numeric-strict-slice.log` and `inherited-numeric-row.json`. The prior1286.394ms `/private/tmp/theta-indexdet-performance/actual-profile-final-first-table.json` failure and all original historical failures remain preserved. `/private/tmp/roth-theta-all-known-whole-performance-failures.json` retains1271.059/1235.627/1237.417/1268.328ms samples and exact sources/tables; none is erased by a later incidental passing sample. Original helper941.711/972.100 and repaired787.045/810.470 were historical prefix-only evidence, not current whole-file acceptance.

Immutable FIRST fragment `/private/tmp/roth-theta-lem6/index_numeric_bound_aux-FIRST.lean`, SHA `b0d66a4601abec08b6e80f022298157d65da0dda19a6bc178f83d3a7898569ed`. Clean full FIRST source `/private/tmp/roth-theta-lem6/FIRST-compiled-numeric-full.lean`, SHA `b182acef13adc414fa0e27880cf048a66578a83f9afbc6ae42b30f925f8573b8`, manifest and original helper-candidate2 exit0 remain intact. Earlier weight/mapped source with later numeric errors is not called a clean numeric FIRST.

## Diagnosis, mathematics and proof repair

Actual inherited nested trace identifies first cubic `nlinarith`232.688ms, second cancellation `nlinarith`141.157ms and sqrt comparison356.739ms. These are diagnostic nested rows, never added to the disjoint declaration total. Taxonomy4, heavy terminal automation, is the root cause. Taxonomy1 instance synthesis,2 fat simp,3 defeq,5 missing expected types,6 casts,7 repeated large subterms and8 kernel/compilation are not dominant: pure real arithmetic has no casts/large domain terms, and actual addDecl30.550ms is small relative to982.063ms proof work.

The revised quadratic argument proves the linear coefficient estimate `3*l≤4*rp`, multiplies it by nonnegative `Φ+δ`, and combines that with three times the quadratic premise using an explicit `linear_combination`. Positive-rp cancellation is a direct order lemma. `le_of_sq_le_sq` reduces the root comparison to its squared certificate. The explicit certificate uses `δ≤max δ 0=√δ²`, `√Φ²=Φ`, and nonnegative mixed root product; it therefore preserves arbitrary negativeδ. No search over cubic monomials remains. One shared explicit `hrp0` replaces repeated arithmetic positivity inference.

The original comment is preserved verbatim. Physical proof16→16 lines; linear branch3 and quadratic branch9, each subproof≤5, ordinary cap30. `le_of_sq_le_sq (by ...)` and typed local certificates are mathematical proof arguments, not semicolon/limit/branch hiding. No helper is introduced to move time elsewhere.

The first scratch certificate had the wrong equality orientation for `Real.sq_sqrt hΦ`; compiler correctly left `8*Φ-8*√Φ²≤0`. `failed-sign-Candidate.lean` and `candidate.log/json` retain the failed source and error. Changing that equality to `.symm` gives clean `candidate-corrected.log/json`, exit0. No failed scratch certifies any positive gate.

## Full24-item substantive audit

|#|Item|Concrete result|
|---|---|---|
|1|LINT|Same-source baseline8 warnings, none at target; fresh complete native gate below retains every warning.|
|2|HAVE SCAN|hsΦ reused in linear and square certificates; hrp0 reused in sign inference and cancellation: retain both terms. Linear hθ, hsq, hsize and quadratic hθ contain proof content. Single-use hsum is inlined into the multiplication certificate. Old h1 removed with nonlinear search.|
|3|SET_OPTION|No production option, limit, trace, diagnostic or linter suppression.|
|4|SIMP SQUEEZE|No simp in target; caller unchanged.|
|5|NAMING|Descriptive private snake_case `_aux`, no forbidden numbering/abbreviation; no rename.|
|6|PACKING|Every signature line measured below, unchanged exact header.|
|7|BY|Every by ends its preceding line.|
|8|FORMAT|Two-space proof indent, no blank line/semicolon/haveI/letI, all≤100.|
|9|COMMENTS|1/1 narrative comment preserved verbatim; all other source comments unchanged.|
|10|DOCSTRING|Private helper appropriately has no docstring; public docs/header protected.|
|11|VISIBILITY|Private arithmetic lemma, sole public direct caller index29; unchanged.|
|12|STRUCTURE|16≤30 lines, branches3/9≤10, each nested proof≤5; no new extraction or correlated existential split.|
|13|MATHLIB|Five actual searches plus current-prefix anonymous automation and separate successful absence gate below. Existing partial square/order APIs used directly; no whole replacement discovered.|
|14|JUNK DEF|n/a: proposition-valued lemma, no new definitions.|
|15|EXISTS|n/a: no existential wrapper.|
|16|SHOW/CHANGE|Neither in target; caller preserved entirely.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All11 effective binder drops and4 weakening probes compiled, outcomes below. No contract change in this performance-only scope.|
|19|INEQUALITY|Seven signature and all local typed inequalities smaller-left; complete table below.|
|20|NORMAL FORM|Standard min bound and real sqrt conclusion; direct squared comparison uses established API, no bespoke predicates.|
|21|SYNTAX-GEN|Already pure arbitrary real arithmetic with no polynomial/point/finite-type baggage; no restatement needed.|
|22|IMPORT-FANOUT|n/a: zero import changes.|
|23|CASTS|No cross-type casts; `(0 : ℝ)` fixes numeric norm_num proof type, load-bearing. No redundant coercion.|
|24|INSTANCE-NAME|n/a: no instance binder/declaration in effective target type.|

## Five actual Mathlib searches and clean current-goal probes

|Method|Query|Actual outcome|
|---|---|---|
|A Lean-Finder|minimum of linear and quadratic bound implies bound by sum of square roots|4 hits: two_mul_le_add_mul_sq, NNReal Cauchy–Schwarz variants, Zsqrtd addition; no full target.|
|B Loogle|`Real.sqrt, _ ≤ _ + _`|5 hits, including sqrt_one_add_le and Japanese bracket; no full min/l/rp estimate.|
|C LeanSearch|inequality from minimum of linear quadratic expressions bounded by square roots|5 hits, including min_le_of_mul_le_sq and Real.le_sqrt_of_sq_le; partial building blocks only.|
|D pinned source rg|le_of_sq_le_sq, mul_le_mul_iff_right₀, sq_sqrt, le_sqrt_self_iff, sqrt_add_le, le_sqrt_of_sq_le, sqrt_mul|Pinned signatures verified; full-name untruncated search finds no index_numeric_bound_aux/sqrt_add_le in Mathlib source. This is textual search, not a proof of global absence.|
|E local search|le_of_sq_le_sq|Actual source hit in Algebra/Order/Ring/Abs; index=unavailable, not misrepresented as index absence.|

Raw responses are `search-results.json`; source hits are `mathlib-source.log`, complete full-name output `full-name-search.log`. Remote indexes are discovery aids; pinned compiler/source determine used APIs. Auxiliary sqrt comparison/multiplication/square/max variants reviewed. No common-equivalents custom topology/algebra predicate bucket matches. No new public API or thin wrapper is recommended.

`Automation.lean` uses the exact current source prefix ending BEFORE the target, no import-self, only anonymous literal-header examples. Distinct bounded10000-heartbeat whole-goal trials: grind,aesop,simp_all,exact?,apply?,nlinarith,positivity,gcongr,norm_num,decide. All errors and trial ranges remain in raw log/results; named failed declarations cannot pollute search. `PrefixAbsence.lean` separately compiles successfully and checks the private target and later public callers are absent. A failed automation file never establishes positive absence or axioms. No maxErrors increase or stalled unbounded multi_attempt was used.

## Every effective binder and generality

Effective type:5 implicit real scalars +6 explicit hypotheses, no instances/universes. `BindersNegative.lean` is isolated from proof search and successful semantic probes; autoImplicit=false makes scalar drops explicit. Every listed trial has recorded compiler errors. Failure means the attempted proof does not establish the candidate, not a general mathematical impossibility claim.

|Binder|Role|Actual drop/weakening probe|Decision|
|---|---|---|---|
|θ:ℝ|Unknown index subject|min/conclusion/proof references fail when dropped|Retain; real sqrt fixes scalar setting.|
|Φ:ℝ|Bound and root|min/conclusion/proof references fail|Retain.|
|δ:ℝ|Bound and root, arbitrary sign|References fail when dropped|Retain; no δ≥0 premise added.|
|rp:ℝ|Quadratic coefficient and size|References fail when dropped|Retain.|
|l:ℝ|Positive linear coefficient|References fail when dropped|Retain.|
|hΦ:0≤Φ|Square identity/final linear step|Drop fails; weaken0≤Φ+δ fails sq_sqrt premise|Retain.|
|hδ1:δ≤1|δ≤√δ linear branch|Drop fails|Retain closed endpoint.|
|hrp:3≤rp|rp positivity and3*l≤4*rp|Drop fails;0<rp fails coefficient inference|Retain.|
|hl:0<l|Sign inference and cancellation|Drop fails;0≤l fails strict cancellation|Retain.|
|hl':l≤rp+1|Linear coefficient bound|Drop fails; l≤rp+2 fails chosen coefficient proof|Retain.|
|hmin|Two cases of minimum|Drop fails|Retain.|

The intermediate coefficient fact `3*l≤4*rp` is established within the proof; exposing it as a changed telescope would add unnecessary private API churn in this narrowly authorized performance repair. No new recommendation is made. This is the current dispatch's preservation requirement, not an invented historical user veto. Strict→weak public29 and arbitrary-negative-δ private improvements already approved remain intact.

Literature: n/a, private declaration (cleanup2.6d). Public29 receives no edit or API recommendation, so its published audit is preserved rather than reopened. Inversion: n/a, statement is already about arbitrary real scalars and contains no distinguished object or unfolding. Abstract-field restatement lacks the real sqrt operation; no useful concrete-object inversion applies.

## All42 golfing rules

|Rule|Status/action|
|---|---|
|1.1|n/a: no by-exact wrapper.|
|1.2|n/a: no by-rfl proof.|
|1.3|Existing RWA direct cancellation retained.|
|1.4|n/a: no simp/exact chain.|
|1.5|n/a: no trailing rfl.|
|1.6|n/a: no constructor goal.|
|1.7|Direct le_of_sq_le_sq term used; no apply/exact chain.|
|1.8|n/a: no contradiction sequence.|
|1.9|n/a: no ordinary lambda.|
|1.10|Removed old h1; shared hsΦ/hrp0 kept. Single-use hsum sign fact inlined into the multiplication certificate.|
|1.11|n/a: no apply/intro.|
|1.12|n/a: no show.|
|1.13|n/a: no projection decomposition.|
|1.14|Existing combined RWA retained; no consecutive rw.|
|1.15|n/a: no target simp only.|
|1.16|n/a: no target bare simp.|
|1.17|Direct `.trans_le`, `.trans_eq`, `.symm`, `.le` order transport.|
|1.18|No avoidable trailing term parentheses; certificate arguments structurally required.|
|1.19|n/a: no push_neg.|
|1.20|n/a: no existential helper.|
|2.1|Actual bounded whole grind trial fails.|
|2.2|n/a: no retained grind prelude.|
|2.3|n/a: no simp consolidation opportunity.|
|2.4|n/a: no function-property goal.|
|2.5|Applied positivity only to nonnegative root RHS; whole goal trial fails.|
|2.6|Whole gcongr trial fails; explicit multiplication monotonicity certificate used.|
|2.7|n/a: real arithmetic, no integer/Nat goal.|
|2.8|Actual bounded aesop trial fails.|
|2.9|norm_num closes literal positivity only; whole norm_num fails. No casts.|
|2.10|Whole decide trial rejects free-variable goal; no native_decide.|
|2.11|No field_simp/ring sequence; fixed polynomial certificate replaces search.|
|2.12|APPLIED two explicit linear_combination certificates, removing three nlinarith calls.|
|2.13|n/a: asymmetric min branches, no symmetric wlog opportunity.|
|2.14|No calc; order/cancellation written directly as terms.|
|2.15|n/a: no similar repeated subgoals; distinct mathematical branches explicit.|
|3.1|n/a: no erw.|
|3.2|n/a: no continuity/measurability.|
|3.3|n/a: no omega.|
|3.4|n/a: no equality rcases.|
|3.5|No automation attribute: specialized min bound would add search noise.|
|3.6|Whole simp_all trial fails; no retained simp_all only.|
|3.7|No limit option added/raised.|

Step-back/simplify outcome **ISSUES-FOUND-AND-FIXED**: search-heavy polynomial reasoning replaced with explicit coefficient/sign/square certificates; no duplicate API, broad simp, hidden cast or unnecessary helper. Pure term-only compression would obscure the two cases; existing direct linear branch remains. Root-of-sum alternative lacks a pinned Real.sqrt_add_le lemma and would need more normalization. The chosen square comparison exposes exact nonnegative contributions, including negativeδ. The entire direct caller is byte-identical and measured after rebuilding.

## Signature packing and inequality tables

Every signature line, codepoints (conclusion included):

|Line|Width|Next complete group|Arithmetic|Action|
|---|---:|---|---|---|
|524|96|`(hl : 0 < l)`12|96+1+12=109>100|ok|
|525|93|complete conclusion27|93+1+27=121>100|ok|
|526|31|proof follows|n/a|ok|

No wide-hyp escape. `packing.json` stores exact source rows; all target lines≤96. Independent actual full-type pretty-printing uses format.width100.

|Location|Comparison|Orientation|
|---|---|---|
|hΦ|0≤Φ|smaller-left|
|hδ1|δ≤1|smaller-left|
|hrp|3≤rp|smaller-left|
|hl|0<l|smaller-left|
|hl'|l≤rp+1|smaller-left|
|hmin|min(lθ/2)(rpθ²/3)≤l(Φ+δ)|smaller-left|
|conclusion|θ≤2(Φ+√Φ+√δ)|smaller-left|
|local hsΦ/hrp0/hθ/hsq/hsize|0≤√Φ;0<rp;θ≤2(Φ+δ);θ²≤4(Φ+δ);3*l≤4*rp;θ≤2(√Φ+√δ)|all smaller-left|
|reverse ≥/>|zero in signature/body|no rewrite/rename|

## Independent semantics design and protection

The entire preceding353506-byte semantic input SHA `8c9f5dff626eca205c484433453402202bf38ec988e24b94a2b4f9672014c14a` is copied as an exact byte prefix; all444 checks remain. Only new independent proofs/checks are appended. No retained-inventory edit is necessary. All four full canonical proof blocks remain byte-identical at exact offsets with SHA72cfbff9…,355a5330…,96f1abe9…,859af5c8…; full hashes/offsets in `immutable-scaffold-and-blocks.json`.

FIRST is independently re-elaborated from its exact clean full source context, changing only namespace and adding scope closures. Current helper and the ENTIRE immediately preceding published current index29 proof are independently re-elaborated in their proper section-variable universe context. An explicit full OLD hδ0/strict/reciprocal adapter uses the independent current proof, not actual target. Checks cover effective types, retained names/order/BinderInfo, universe lists, conclusions, actual opaque value!true typing and standard axioms; independent proofs cannot cite actual corresponding targets. Independent and actual index29 values must contain their respective numeric helper constant. All29 original public recovery adapters, five public definition values, all eleven original35 introduced-helper/deletion audits, all prior repair checks, entire original2b MainLemma proof and entire independent current MainLemma proof, actual RootTheta/MainLemma values/types/axes/dependencies remain in the preserved prefix.

New external identifiers: le_of_sq_le_sq (actual local/source search+compiled candidate), linear_combination (existing imported tactic+compiled candidate), `.trans_eq` (compiled pinned order API), existing mul_le_mul_iff_right₀/mul_le_mul_of_nonneg_right/Real.sq_sqrt'/Real.sq_sqrt/Real.sqrt_nonneg (pinned source and compiled selected proof). `Positivity` tactic already in import closure, verified on exact nonnegative RHS. No guessed API used.

Phase3 file-level changes: none, narrow proof scope. Phase5a: none, no wrapper/API extraction warranted. Phase5b: no rename candidate; no queue or shared-log write. Owner full project build THEN separate LeanEval and publication remain owner-only final gates.


## Fresh final build, independent and whole-semantic gates

Only the scoped proof source changed; it stayed frozen during all accepted final gates.

|Actual command|Exit|Seconds|Evidence|
|---|---:|---:|---|
|lake build Roth.Theta|0|31.721|build-theta-final.log/json|
|lake build Roth.MainLemma|0|37.303|build-mainlemma-final.log/json|
|lake env lean Independent.lean|0|46.409|independent-final.log/json|
|lake env lean ActualSemanticsAugmented.lean|0|180.688|actual-semantics-final.log/json|

Independent input: **69 PASS**. Full augmented input: **513 PASS = all444 preceding checks + 69 fresh checks**. Entire preceding353506-byte prefix and all four full canonical blocks remain unchanged. No retained-inventory edit or inverse recovery is needed. Fresh semantic input SHA256 `dead52ef35a112373ecf1c77d0b899ab8fe657c440157a2a15a1f19fef62a65c`. Every accepted positive log is clean of errors/PANIC/sorryAx. All opaque actual/independent proof values use value!true, exact types, standard axioms only.

The first independent caller probe omitted its two private support declarations;
Lean reported unknown mapped_det_ne_zero_aux/weight_le_delta_aux and the explicit axiom
verifier rejected the resulting sorryAx. That failed source, augmented input, log,
status and process record remain in failed-private-context-* and certify no gate.
The correction copies the exact complete preceding weight and mapped proofs into the
independent namespace, preserving the ENTIRE caller text. Both support proofs already
have their original dedicated audits; no production helper was created. Exact section
variables, including preceding sigma universe context, remain present. Final standalone
independent compilation succeeds before the expensive whole-scaffold compilation.

An independent old-contract adapter AND an explicit adapter to the actual built private
constant recover all original hdelta0/strict/reciprocal binders, names/order/BinderInfo,
universes and conclusion. The exact FIRST proof is independently recompiled in its
immutable full original context. Actual current private type/value/standard axioms and
full public29 type/value/independent nonself proof are checked separately, with positive
actual and independent helper dependencies. An explicit negative-delta instance also
compiles. The all29 old public recoveries, all5 public definition values, all eleven original35 introduced-helper/
deletion audits and previous performance checks, original2b and independent current
full MainLemma blocks, actual RootTheta/MainLemma types/values/axes/dependencies all
freshly pass inside the preserved444-check prefix.

Scratch corrections are retained honestly: wrong-sign square certificate, initial
missing-# heartbeat command, and a checker regex initially missing Lean's error(code)
format. The corrected error parser associates compiler errors with every one of15
binder trials and10 anonymous automation trials; it does not change Lean or raise
maxErrors. Only corrected exit0 positive files certify success.

## Complete unfiltered native diagnostics

|File|success|partial|timed_out|Errors|Warnings|
|---|---|---|---|---:|---:|
|theta|true|false|false|0|8|
|mainlemma|true|false|false|0|3|

Both raw JSONs retain every diagnostic verbatim, with no declaration/range/severity filter. Warning inventory:

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

These are inherited header/protected-hypothesis warnings. No new target warning or suppression. All native requests returned complete; all ordinary process groups drained before actual profiling.

## Actual whole-Theta profiling, scoped acceptance

Actual command for each final capture:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`

Each capture uses an external420s limit only; Lean heartbeat/recursion limits remain
unchanged. Exact entire production source is snapshotted. Each final table inventories
all50 source declarations, with exactly one actual proof anchor per theorem/lemma.
Totals use anchored disjoint outer command + associated top-level async proof/addDecl/
compiler/linter rows. Nested macro/kernel/tactic timing is never added twice. All raw
UTF8 bytes, offsets, hashes, selected strict slices and failing rows remain preserved.

final-first: exit0, timed_out=false, 241.651s, raw bytes207397056, raw SHA256 `6d40899e248b56fde195fc9c149fee8edac7e6cb58c9444de77f95c048eed9d8`. Strict UTF8 valid, replacement sequences0.

|Declaration|Inherited latest ms|Fresh first ms|Fresh repeat ms|
|---|---:|---:|---:|
|index_numeric_bound_aux|1097.018|592.602|not required|
|index_le_lem6|550.944|480.114|not required|
|index_separated_mul_le_aux|568.792|636.691|not required|
|index_det_le|725.539|742.461|not required|
|Θ_option_le|156.723|157.674|not required|

Both scoped first rows are<750ms; no unchanged-source repeat is required or taken.
No third unchanged-source sample/cherry-pick. Heartbeats**4206->1954** independently support reduced proof work. The failed1097.018ms/1286.394ms and four original whole-file failures are preserved with validated raw/source/table hashes, exact copied source snapshots and strict UTF8 slices in preserved-failing-history.json. Other historical prefix samples remain in their original immutable audit artifacts.

Fresh nested diagnostics (nonadditive): squared bound164.878ms, root comparison135.029ms, coefficient subproof39.405ms. This confirms the actual measured repair at the original arithmetic hotspots; nested rows are diagnostic only and never added to scope totals. Exact anchors/line offsets are in final-nested-hotspots.json.

Buzz outcome: **FIXED for assigned numeric helper and unchanged direct index29 consumer**.
The actual cubic/sqrt automation hotspot is replaced by fixed certificates; no timing
has been transferred to a helper. MaxHeartbeats raises removed0, added0. Same-issue
propagation review: index29 forwards the numerical result only by name, hence unchanged
and measured. Remaining sum_max, lem7Phi/numeric and prefix have distinct combinatorial,
rpow/sqrt and finite-index/cast arguments; their dedicated repairs remain mandatory.
No unrelated optimization was made.

## Remaining queue and owner-only gates

Three older repairs remain: sum_max_sub_le_index_det, lem7_Φ_bound, lem7_numeric.
The prior theta_prefix_lt_aux1047.277/repeat721.307 failure remains a mandatory separate
second repair, irrespective of incidental lower observations. No whole-file performance
PASS is claimed. MainLemma actual caller timing remains **unmeasured after its bounded
cutoff before main_lemma**; successful build/semantics/native checks do not replace it.

|Separately queued declaration|Fresh first ms|Fresh repeat ms|
|---|---:|---:|
|sum_max_sub_le_index_det|1333.349|not taken|
|lem7_Φ_bound|1167.336|not taken|
|lem7_numeric|1262.083|not taken|
|theta_prefix_lt_aux|741.338|not taken|

No new overbudget declaration outside the known queue occurred.

Owner alone runs final cumulative/allactual checks, full `lake build` THEN separate
`lake build Roth.LeanEval`, exact-path stage/commit/push/clean before another source
edit. These owner gates are pending and never claimed here. No original count inflation.

## Gate status and eleven-step checklist

|Gate|Result/evidence|
|---|---|
|Module builds|PASS: fresh Theta THEN MainLemma actual commands/exit0 above|
|Statements/definitions protected|PASS: exact helper header; every prefix/suffix byte including entire public29 unchanged|
|Structure/naming/comments|PASS:16 lines, branches3/9, subproof<=5, private descriptive name,1/1 comment verbatim|
|Packing/inequality|PASS: all3 measured signature rows and all correctly oriented comparisons|
|Search/generality|PASS:5 actual methods,10 clean-prefix anonymous failures, independent successful absence, all15 binder probes|
|Independent and actual semantic evidence|PASS: exact FIRST proof/context; full old adapters; full current helper/caller; all444 preserved checks plus fresh checks|
|Native|PASS: complete unfiltered success,partial=false,timed_out=false,0errors for both files|
|Scoped actual performance|PASS: every target/direct-caller observation<1000ms; repeat rule honored|
|Trust/limits/scaffolding|PASS: no sorry/axiom/native_decide/limit/import/attribute change; clean opaque standard axioms|
|Owner full project/Eval/publication|PENDING OWNER|

- [✓]1 Skills, required references/workflows and failing raw evidence read.
- [✓]2 All24 audit items and every have reviewed.
- [✓]2.5 Five actual searches, literal clean-prefix automation and successful separate absence.
- [✓]2.6 Every effective binder drop/weakening, private literature exemption, inversion/design review.
- [✓]2.7 Every signature codepoint width and next-complete-group arithmetic.
- [✓]2.8 Entire inequality occurrence scan.
- [✓]3 All42 golf-rule statuses, explicit fixed certificates and single-use inlining.
- [✓]4 Holistic simplify and alternative strategy review; no new helper/API.
- [✓]5a Complete fresh unfiltered Theta/MainLemma native diagnostics.
- [✓]5b Actual module builds, exact original/current/caller full semantics, whole Theta actual trace/scoped budget.
- [✓]6a No rename needed; no shared-log/queue writes.

## Complete artifact map and terminal freeze

All fresh artifacts: `/private/tmp/theta-numeric-performance/`.

|Evidence|Artifacts|
|---|---|
|Baseline/final source and pins|baseline-Theta.lean; final-Theta.lean; source-hashes.json; all-source-pin-hashes.json; release-source-pin-hashes.json; all-FIRST-immutable-hashes.json; protected-report-hashes.json|
|Diff/static|owned-proof.diff; static-gates.json; packing.json; candidate-declaration.lean; independent-proof-blocks.json|
|All inherited required failures|preserved-failing-history.json; historical-0..5-Theta.lean; historical-0..5-numeric-strict-slice.log; inherited-numeric-row.json/strict-slice.log; original all-known failure inventory/hotspot source paths|
|Search/current goal|search-results.json; mathlib-source.log; full-name-search.log; PrefixAbsence.lean/log/json; Automation.lean/log/json; automation-ranges/results.json|
|Generality/heartbeats|BindersNegative.lean/log/json; binder-ranges/results.json; Heartbeats-before/after.lean/log/json; check-exploration.py|
|Independent/full semantics|Independent.lean; ActualSemanticsAugmented.lean; immutable-scaffold-and-blocks.json; independent-final.log/json; actual-semantics-final.log/json; semantic-marker-summary-final.json|
|Build/native|build-theta-final.log/json; build-mainlemma-final.log/json; native-theta-final.json; native-mainlemma-final.json|
|Actual profiling|actual-profile-final-first.log/json/-table.json; optional final-repeat counterparts; profile-final-*-strict-slices.json; scoped strict slice logs; profile-final-*-remaining-queue.json; new-actionable strict slices; profile-final-first-all-failures-strict-slices.json and every known failing-row slice; final-nested-hotspots.json|
|Preserved scratch failures|failed-sign-Candidate.lean; candidate.log/json; pre-inline-Candidate/declaration/binders/heartbeat files and logs; failed-private-context-*|
|Process ownership/artifact hashes|all *.pid.json; pre-profile-drain.json; optional pre-repeat-drain.json; final-process-drain.json; evidence-manifest.json; final-freeze.json|

Final Theta SHA256 **`f458cf85b2746b8d155074c3aaaccd8e8c0708bd2d7fa78787184d76ae008875`**. All17 source/pin files checked; only scoped proof differs. All16 inherited FIRST artifacts and all73 preceding Theta reports unchanged. Exact full hashes/offsets are in manifests. Four canonical proof hashes and entire preceding scaffold remain unchanged.

All own ordinary/native requests are drained, all tracked compiler process groups dead, pending[]. Terminal authority: **source/scratch/report/compiler/native REVOKED**; sole compiler/native window **RELEASED**. No own mutation/request follows this terminal freeze.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 87.943 s and 35.135 s.
Theta SHA256 `f458cf85b2746b8d155074c3aaaccd8e8c0708bd2d7fa78787184d76ae008875` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p05-full.log` and `/private/tmp/roth-theta-p05-leaneval.log`; machine record
`/private/tmp/roth-theta-p05-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 29 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
