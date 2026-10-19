# Fresh introduced-helper audit: theta_lt_of_large_delta_aux

Tenth of eleven introduced-helper audits in unpublished original35. No original-count
credit:215/264,Theta34/35 remain unchanged. Published HEAD88d92dfa11fab6296160d9baa4a9862ce208ee96.
Scope: private large-delta helper, necessary routine proof consumers, this report only.
No Git/shared logs/pins/definitions/public contract edits. All artifacts under
/private/tmp/theta35-large-delta-fresh unless an absolute historical path is supplied.
Eight retained plus three introduced/deleted helpers remain eleven historical obligations.
No new production helper or new subagent.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md and cleanup-gates.md, both Lean/mathlib-quality SKILLs,
full cleanup workflow, relevant style/naming/profiling references, exact dispatch,
preceding successor report and frozen handoff. Single-declaration worker mode.
Baseline doctor inherits exact-c8aba564 complete native diagnostics/module/full semantic
evidence from the preceding released audit, verified by owner; no redundant baseline
full build. Owner owns final full project build THEN separate LeanEval. Fresh final
module/semantic/native/profile gates are required below. No stale modules used for
actual current opaque checks. No universal whole-file performance PASS is claimed.

## All24 audit items

|#|Item|Concrete decision|
|---|---|---|
|1|Lint|No target warning in inherited complete8/3-warning natives; fresh complete final natives required.|
|2|HAVE scan|hp has by and is reused by div comparison/square bound/reciprocal; keep. hq has substantive log/cast proof, used once for rpow base; keep. hB no by, single-use; INLINE into Θ_le_card. hinv no by, single-use; INLINE into self_le_rpow. hpow by proof and nested h no-by, single-use: replace with direct self_le_rpow_of_le_one and INLINE entire comparison at final multiplication. hp2 has cast proof; keep. hsq no-by calc, single-use: INLINE multiplication-bound calc into lt_div_iff₀ certificate, removing two square simp conversions. Final only hp,hq,hp2 remain, each has by and actual proof content.|
|3|Options|No production options/limit changes/attributes. Scratch whole-goal trials lower maxHeartbeats10000, default maxErrors.|
|4|Simp|Old hpow terminal simpa removed entirely via direct self_le_rpow lemma. Old two terminal simp-only square conversions removed via multiplication form. Final only terminal simpa for Fintype.card_fin from Θ_le_card, unsqueezed. No nonterminal bare simp.|
|5|Naming|theta_lt_of_large_delta describes strict bound from largeδ; snake_case,private,_aux; no numeric-scheme/forbidden abbreviation. No rename recommended.|
|6|Packing|Every signature line measured below; original71+1+28=100 underpacking fixed; first hδ moved to line1, r/q and hq1 combined; final three-line header100/98/84 widths measured below.|
|7|By|:= by and each local by on preceding expression line.|
|8|Format|2-space proof and suitable continuations; no interior blank lines/multiline semicolon/haveI/letI.|
|9|Comments|Target originally has no narrative comment; entire module/public docstrings and all other proof comments preserved byte-for-byte.|
|10|Docstrings|Private auxiliary correctly has none; public documentation unchanged.|
|11|Visibility|Retain private substantive cardinality/numerical bound; not a1–3-Mathlib-call wrapper. Two public branches consume it.|
|12|Structure|Final≤30 proof lines, nested numerical calc≤10, each local subproof≤10; no conjunction/case branch to split; publicΘ15,phi30 unchanged.|
|13|Mathlib|Five actual search methods; direct self_le_rpow_of_le_one,pow_le_pow_left₀,mul_one_div selected. Literal current-header exact-prefix anonymous searches with positive target/RootΘ absence. No complete replacement found; no universal absence claim from search.|
|14|Junk def|n/a theorem; no def/abbrev/custom predicate.|
|15|Exists|n/a no existential witness wrapper.|
|16|Show/change|No target show/change. Numeric/real type ascriptions fix actual Nat→Real bridges and overloaded exponents.|
|17|Push_neg|n/a no negation tactic.|
|18|Generalise|Every7 effective binder drop-probed; δ strict→nonnegative and quantitative largeδ→nonnegative probed. Separately prove δ positivity from hδ and weaker base-q version. Retain orchestration contract for technical reasons explained below, not necessity claims.|
|19|Inequality|All signature and proof inequalities smaller-left; no reversed ≥/>; per-occurrence table below.|
|20|Normal form|Θ cardinality,real rpow/log and Fin dimension already domain canonical; use multiplication form inside lt_div to avoid square normalization.|
|21|Syntax generality|Current quantitative logarithm premise is exactly available in both public branches; moving weaker base predicate proof to callers duplicates casts and enlarges the headline proof. No API restatement recommended.|
|22|Import fanout|n/a no imports changed.|
|23|Casts|Genuine Nat→Real bridges (n,q,r) and numeric real ascriptions retained. Removed square-only normalization via multiplication; no new redundant cast.|
|24|Instances|No effective classes/decidability/universes/instance names; verified full telescope.|

## Five actual search methods

|Method|Actual query/evidence|Outcome|
|---|---|---|
|A LeanFinder|real reciprocal natural successor/small-exponent power/exponential n² bound|Behrend/AP-three and Bertrand bounds; different subject, no replacement.|
|B Loogle|Real.rpow_le_rpow_of_exponent_ge|Existing generic comparison lemma found; local hpow is better served by self_le_rpow.|
|C LeanSearch|positive real at most1,exponent at most1 increases it|Real.self_le_rpow_of_le_one exact partial match; used DIRECTLY. Also rpow_le_self,NNReal variants.|
|D rg pinned Mathlib source|self_le_rpow_of_le_one,pow_le_pow_left₀,pow_le_pow_left,lt_two_pow_self,theta_lt_of_large_delta_aux|Exact selected source signatures verified; no target-name match. Untruncated output retained.|
|E native local search|pow_le_pow_left₀|Source match pow_le_pow_left returned with index unavailable; never treated as indexed absence. Selected full name independently verified by source/#check/compiler.|

Auxiliary variants self_le_rpow/rpow_le_self, strict/weak power bases and natural-two-power
route examined. Discrete/finiteness/separation/bornology equivalence buckets unrelated.
No whole Θ replacement selected after actual searches and compiled exact?/apply? trials.
Target is substantial numerical reasoning, not a1–3-call wrapper. No public API extraction
recommended: direct existing lemmas remove the ugly rpow/square normalization chain.
All11 strategies use anonymous examples with literal current header, exact current prefix
BEFORE target (imports exclude Roth.Theta), end Lemma7 then Roth; independent successful
absence assertion is required. Named parameter probes are separate expected-failure files.
All trials bounded/split with default maxErrors and each BEGIN/END checked. Remote search
hits establish presence, not exhaustive absence. Native multi_attempt is not retried after
its established stalled-request limitation; ordinary isolated compiler trials used.

## Every effective parameter, generality and inversion

|Binder|Role and compiled mechanical candidates|Decision|
|---|---|---|
|n|Drop under autoImplicit false; controls Fin dimension,cast scalar,power|Keep ℕ; finite cardinality and natural dimension substantive.|
|δ|Drop real parameter|Keep ℝ; real exponent/log API; generic ordered-field replacement changes the object.|
|hδ0|Drop;0<δ→0≤δ; separate derived-positive proof from hδ|Keep explicit orchestration positivity supplied by both callers, without claiming logical necessity.|
|hδ|Drop; reciprocal lower bound→0≤δ|Keep quantitative lower bound, used for final rpow comparison. Strictness already weak.|
|r|Split grouped binder/drop|Keep natural multiplicity function; conclusion/domain depend on r.|
|q|Split grouped binder/drop|Keep natural denominators; conclusion/log premise depend on q.|
|hq1|Drop quantitative log premise; independent weaker-base theorem with1<q0|Keep matching public branch premise; weaker_base.lean documents mathematical generality without duplicating conversion at callers.|

No class parents/universe/point-localization candidates apply: all parameters concrete,
log premise already only q0; r/q Fin function domains are inherent to Θ. Negative
proof-substitution diagnostics are not logical indispensability evidence.
DerivedPositive compiles an entire candidate proof after removing explicit hδ0 and
recovering it by positive reciprocal≤δ. WeakerBase compiles entire final numerical proof
under merely1<q0. These are supported mathematical improvements in generality, but no
new API is recommended: retaining explicit positiveδ keeps consistency with the public
branch orchestration and the rest of the induction helpers; replacing hq1 duplicates
log-to-base casts in both headline branches. This is a technical judgment, not a user
veto or a false assertion that the stronger premises are mathematically necessary.

Public-literature search n/a: private auxiliary expressly exempt by cleanup§2.6d.
Inversion STILL examined: Θ appears only at the cardinality step; all remaining content
is the general scalar inequality m<10^m δ^(2^-m), for m≥1,δ≥1/m. An abstract version
could accept an arbitrary real X≤m and return X<10^m δ^(2^-m). This scalar estimate is
already local, has no supported second external caller, and adding it plus a concrete
wrapper would introduce another helper/audit without removing mathematical work.
Keeping the two-use private boundary and direct existing scalar lemmas is appropriate.
No new helper, public wrapper, modified conclusion or stronger IH introduced.

## All42 golfing rules

|Rule|Disposition|
|---|---|
|1.1|No redundant by-exact wrapper; exact_mod_cast performs actual transport.|
|1.2|n/a no by-rfl.|
|1.3|No rw+exact closure; rw then norm_num evaluates base4.|
|1.4|Old simpa chain replaced by direct self_le_rpow lemma; card simpa already consolidated.|
|1.5|n/a no simp+rfl.|
|1.6|n/a no constructors.|
|1.7|Direct term applications used for scalar bounds.|
|1.8|n/a no by_contra.|
|1.9|n/a no lambda.|
|1.10|Inline hB,hinv,hpow,inner h and hsq; final three have blocks have proof content.|
|1.11|n/a no apply+intro.|
|1.12|n/a no show.|
|1.13|n/a no conjunction projection.|
|1.14|No consecutive rw; single ←mul_pow step.|
|1.15|Two terminal simp-only square conversions eliminated; final terminal card simpa unsqueezed.|
|1.16|n/a no nonterminal bare simp.|
|1.17|.trans for scalar power comparisons; .symm for mul_one_div.|
|1.18|Use <| calc in lt_div certificate, avoiding nested parentheses.|
|1.19|n/a no push_neg.|
|1.20|n/a no existential lemma.|
|2.1|Whole-goal grind tried clean anonymous prefix; results below.|
|2.2|n/a no grind retained.|
|2.3|Remove square simpa consolidations entirely via multiplication form.|
|2.4|n/a no function-property goal.|
|2.5|Positivity retained for hp,reciprocal/exponents/base; whole-goal tried separately.|
|2.6|Whole-goal gcongr tried; local4^m≤10^m replaced by exact pow_le_pow_left₀.|
|2.7|Whole-goal lia tried; real reciprocal scalar certificate uses explicit linarith only. No integer linear subgoal left.|
|2.8|Whole-goal aesop tried clean anonymous prefix.|
|2.9|norm_num whole-goal tried; retained for closed0≤4/4≤10/half≤1 and rewrite base2*2=4; exact_mod_cast retained for genuine bridges.|
|2.10|Whole-goal decide tried; no native_decide.|
|2.11|Whole-goal field_simp/ring tried; final division identity uses mul_one_div directly.|
|2.12|Old final ring identity eliminated by exact mul_one_div, so no retained ring ending to test linear_combination against.|
|2.13|n/a no symmetric case split.|
|2.14|Use .trans for two-step rpow chain; heterogeneous outer cardinal/division/multiplication calc retained.|
|2.15|n/a no repeated sibling goals.|
|3.1|n/a no erw; rw works for ←mul_pow.|
|3.2|n/a no continuity/measurability.|
|3.3|No omega retained; lia whole-goal trial in2.7.|
|3.4|n/a no rcases-rfl.|
|3.5|No automation attribute: private2-use numerical orchestration helper should not pollute global search.|
|3.6|Whole-goal simp_all tried; none retained.|
|3.7|No production maxHeartbeats/maxRecDepth/debug option to remove or add.|

## Holistic reflection and simplify

Ordinary builtin simplify/buzz invocations unavailable in this host; their full scoped
review/performance work is performed explicitly. Outcome ISSUES-FOUND-AND-FIXED:
remove the hpow simplification detour through self_le_rpow_of_le_one, inline every
single-use term have, stay in multiplication form for division comparison, replace
gcongr with direct pow_le_pow_left₀ and ring with mul_one_div. No new helper or API
change. The old failed repeat's hpow365.233ms (including closing simpa171.525ms),
hsq226.959ms and total1450.876ms guided these substantive changes. Raw timings remain
historical evidence, never erased by later samples. Both owned target and direct public
consumer require fresh same-final-source profiles after all other requests drain.
All static24/42/HAVE/generality/packing/inequality decisions precede final gates.

## Count clarification

The earlier update saying34→24 mixed nonempty declaration lines (including signature)
with proof lines. Exact parser on inherited target-before.txt gives30 nonempty noncomment
proof lines, four signature lines; final gives24 proof lines, three signature lines.
Nonempty whole declarations34→27; physical blocks35→28 including trailing blank;
entire Theta988→981 lines. This explicitly corrects that update; no timing/gate rerun
is required solely for reporting the correct counts.

## Measured packing and inequalities

|Signature line|Width|Next complete constituent width|Arithmetic/action|
|---|---|---|---|
|1|100|23|100+1+23=124>100; ok|
|2|98|80|98+1+80=179>100; ok|
|3|84|—|last signature line; ok|

Full effective type is printed with format.width100 in successful semantic output.
Repacked four signature lines to three; retained exact FIRST7 telescope, no classes/universes omitted.

|Occurrence|Line:column|Relation|Action|
|---|---|---|---|
|1|1:68|<|smaller-left; no rewrite|
|2|1:97|≤|smaller-left; no rewrite|
|3|2:80|≤|smaller-left; no rewrite|
|4|3:35|<|smaller-left; no rewrite|

Final body counts:{'theta_lt_of_large_delta_aux': 24, 'theta_lt_succ_aux': 27, 'theta_phi_lt_aux': 30, 'Θ_lt': 15}. All lines≤100, no branch/subproof>10.

Cast audit:0 redundant ascriptions removed individually; casts.json enumerates all14 final proof ascriptions:7 genuine Nat→Real bridges and7 numeric real-type pins. Eliminating the square detour removed its additional normalization ascriptions.

## Final compiled search and parameter results

Every11 anonymous strategy reached BEGIN/END with exact current packed header and
positive target/later RootTheta absence. Every7 binder and both weakening trials has
a diagnostic in its own source range, binder-results.json. These are direct proof
substitution observations, not mathematical necessity claims or axiom evidence.
DerivedPositive and CandidateChecks compile successfully; the latter also includes
entire weaker-base numerical proof and selected-identifier #checks. Initial unpacked
header trials are archived in superseded-unpacked-header and were rerun cleanly; no
claim they are final literal-header evidence. First candidate compiled; final inlining
removes all single-use term haves and square-normalization round trips.

|Strategy|Actual result|
|---|---|
|grind|`grind` failed|
|aesop|unsolved goals|
|exact?|`exact?` could not close the goal. Try `apply?` to see partial suggestions.|
|apply?|(deterministic) timeout at `delab`, maximum number of heartbeats (10000) has been reached|
|simp_all|unsolved goals|
|gcongr|`gcongr` did not make progress.|
|positivity|not a positivity goal|
|norm_num|unsolved goals|
|lia|`grind` failed|
|decide|Expected type must not contain free variables|
|field_simp/ring|unsolved goals|

## Independent FIRST, full semantic scaffold and actual built values

FirstIndependent.lean contains the ENTIRE immutable FIRST batch3 bytes unchanged,
with its original import/namespace/all surrounding helper proofs, no inserted section,
class,universe or omit. A preceding Roth.MainLemma import enables actual current caller
checks. FIRST target is re-elaborated independently, not inferred from the current
helper adapter. Exact FIRST7 adapter and actual opaque helper recover all7 names,
types,order,BinderInfo,universe arity and conclusion. No weakening applied. Actual opaque
values use value!true,inferType and collectAxioms; only propext,Classical.choice,Quot.sound.
Actual target has direct positive dependencies on the three selected generic lemmas;
RootTheta depends on target; actual MainLemma depends on RootTheta.

The preceding303-check scaffold is an exact byte prefix, retained-helper inventory
unchanged. Index72cf/Theta355a and ENTIRE immutable original2b and independent updated
MainLemma proofs remain four complete byte-identical blocks, with hashes/offsets
in immutable-complete-blocks.json. This retains publicTheta9 and entire Main26 contracts
/definitions, exact immutable-oldTheta adapter, full original/current caller bodies,
positive actual caller dependency and no imported RootMainLemma as independent proof.

Independent FIRST markers:27; combined markers:330.
No PANIC,error,sorryAx or nonstandard axiom. Both rebuilt modules precede actualRoot
queries. Full inherited FIRST/scaffold proofs are retained; no old raw adapter tail
was substituted for the verified current scaffold.

## Fresh final gates

|Gate|Command/evidence|Result|
|---|---|---|
|build-theta-final|/Users/ramin/.elan/bin/lake build Roth.Theta; build-theta-final.log/.json|exit0,32.264s|
|build-mainlemma-final|/Users/ramin/.elan/bin/lake build Roth.MainLemma; build-mainlemma-final.log/.json|exit0,37.446s|
|first-independent-final|/Users/ramin/.elan/bin/lake env lean /private/tmp/theta35-large-delta-fresh/FirstIndependent.lean; first-independent-final.log/.json|exit0,38.169s|
|actual-semantics-final|/Users/ramin/.elan/bin/lake env lean /private/tmp/theta35-large-delta-fresh/ActualSemanticsAugmented.lean; actual-semantics-final.log/.json|exit0,154.793s|
|definition_protected|Exact target-only reconstruction,scoped-source-reconstruction.json|PASS; all defs/imports/pins/comments/public proofs unchanged|
|theorem_statement_protected|FIRST7 exact telescope and inherited publicTheta9/Main26|PASS; packing only, no contract change|
|structure_gate|line-counts.json|PASS target24,successor27,phi30,publicTheta15; nested≤10|
|naming_gate|Descriptive private large-delta strict bound/_aux|PASS; no rename|
|line_packing_gate|Every3 signature lines in packing.json|PASS100/98/84|
|inequality_orientation_gate|Every occurrence,inequalities.json|PASS all smaller-left|
|scoped cumulative consumers|Both module builds,full original/current caller,actual values/dependencies/axioms,natives|PASS|
|full project THEN separate LeanEval|Owner-only frozen final gates|PENDING,never claimed here|
|whole-file performance/MainLemma finite caller timing|Separate mandatory queue|NOT CLAIMED|

Fresh COMPLETE UNFILTERED native diagnostics; all warning objects retained verbatim:

|Module|Success|Partial|Timed out|Errors|Warnings|
|---|---|---|---|---|---|
|theta|true|false|false|0|8|
|mainlemma|true|false|false|0|3|

- theta:1:2,warning:

```text
* `-/`:
Copyright too short!


Note: This linter can be disabled with `set_option linter.style.header false`
```

- theta:93:43,warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:101:27,warning:

```text
Variable name `hB` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hB

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:101:64,warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:109:28,warning:

```text
Variable name `hB` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hB

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:129:81,warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:252:6,warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:547:47,warning:

```text
Variable name `hq` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hq

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- mainlemma:1:2,warning:

```text
* `-/`:
Copyright too short!


Note: This linter can be disabled with `set_option linter.style.header false`
```

- mainlemma:149:28,warning:

```text
Variable name `hδ0` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hδ0

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- mainlemma:149:69,warning:

```text
Variable name `hr₁` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr₁

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

No new/target warning. Retained publicMain unused hδ0/hr₁ await that file audit;
explicit earlier hq and globalTheta hB/hr choices preserved. Header metadata unchanged.

## All11 cleanup steps

|Step|Result|
|---|---|
|1 Required skills/workflow/references|✓|
|2 Every24 audit item/HAVE decisions|✓|
|2.5 Five actual methods,11 clean literal-prefix strategies,positive absence|✓|
|2.6 Every7 binders,2 weakening probes,derived-positive/weaker-base,private exemption/inversion|✓|
|2.7 Every3 signature lines measured/repacked|✓|
|2.8 Every signature inequality|✓|
|3 Every42 golf rule disposition|✓|
|4 Holistic simplify and substantive repair,no helper|✓|
|5a Fresh complete unfiltered final native diagnostics|✓|
|5b Both modules,full semantic/actual opaque/contracts/protection/performance gates|✓|
|6a No rename/shared-queue mutation|✓|

All static decisions preceded final module/semantic/native/profile cycle,
static-decisions-complete.json. No post-profile source polish.

## Actual final performance

All normal/native requests drained before BOTH actual whole50 captures. Command:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Theta.lean`; external420s capture window changes no
Lean limit. Sum disjoint outer command+associated async proof/addDecl/linter rows;
exclude nested macro/kernel duplication. Both raw traces exit0,strictUTF8,all50 source
anchors; exact source hashes,byte offsets,strict slices and raw hashes retained.
No third unchanged-source sample.

|Run|Actual declaration|Conservative ms|
|---|---|---|
|final-first|theta_lt_of_large_delta_aux|939.532|
|final-first|Θ_lt|428.450|
|final-repeat|theta_lt_of_large_delta_aux|733.980|
|final-repeat|Θ_lt|354.847|

Buzz outcome FIXED for owned helper and its direct public consumer only. Both actual
same-final-source samples<1000ms; any≥750ms is covered by mandatory same-source repeat.
Historical9faa870.970/1450.876 FAILED pair is preserved with exact source/raw/table/slice
hashes and offsets in preserved-historical-large-delta-failures.json. Later passing
c31(983.200/841.034),c8(919.521/920.676) remain inherited baseline,not fresh audit evidence
and do not erase that failure. Fresh first939.532ms does NOT establish a speedup over
the immediate c8 baseline919.521/920.676ms. This audit records a clearer/shorter proof,
a meaningful repair of historical hotspots and supported final-source budget acceptance;
it makes no performance-improvement claim over c8. The final repair targets old hpow/
simpa/hsq costs; no limit raises,masking,scaffolding,sorry,newaxiom,native_decide.

No whole-file performance PASS. Prefix834.213/1098.066 failed repeat on c8 remains a
separate mandatory fresh prepublication revisit; source before target is byte-identical,
and its failure is not cleared by fresh incidental sampling here. Other mandatory
final-repair queue: sum_max_sub_le_index_det,index_separated_mul_le_aux,index_det_le,
index_numeric_bound_aux/index29,index_le_lem6,lem7_Φ_bound,lem7_numeric and historical
positive-quadratic-helper1074.965ms. Both fresh outside-scope overbudget rows retained
in outside-scope-overbudget.json,not claimed repaired. Phi historical988.865/1013.946
failed pair stays governed by its fresh audit. MainLemma's180s cutoff before main_lemma
has no finite caller timing; module/native/semantic gates do not substitute one.

## Exact frozen handoff

|Source|SHA256|
|---|---|
|Roth/Theta.lean|039806e8ae3cddcd6c7e87ddd60b5f23b15b1b9a71089fc8e1f00db0c625b3e5|
|Roth/MainLemma.lean|ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4|
|Roth/Main.lean|f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069|

Theta988→981 lines; target30→24 nonempty noncomment proof lines (correcting the early
34→24 mixed count),signature4→3; successor27,phi30,publicTheta15 unchanged.
All retained names/types/order/BinderInfo/universe arity/conclusion preserved. FIRST all
three batch texts and relevant immutable original success logs/statuses unchanged,
including FIRSTbatch3a373382e41c4b79d5d50dcd375e43d630acfecb09ecfc989e56f23250a396700.
All303 inherited checks/four full canonical blocks retained. Helper history8 retained+
3 introduced/deleted=11 obligations, no new/deleted helper, no original count credit.
After this tenth audit, deleted fin_option still needs its distinct replacement/deletion
audit; dedicated prefix revisit and final repair queue remain prepublication obligations.
Counts215/264,Theta34/35 unchanged. No Git/commit/push/publication.

Source edit authority explicitly REVOKED. All own source/scratch/report/compiler/native
requests DRAINED,pending[],normal_pending[],native_pending[]. All authority released
at terminal handoff,final-process-drain.json/final-freeze.json. No source edit after
freeze. Owner retains Git/shared logs and owes remaining introduced-helper audit,
prefix revisit,cumulative29/allactual/final performance repair sweep,full lake build
THEN separate frozen Roth.LeanEval before ANY original35 publication.

Owner scope clarification: the introduced prefix performance revisit is required before original35 publication. The eight older, unrelated declaration performance revisits remain required after original35 publication and before file-final completion. No whole-file performance pass is claimed.
