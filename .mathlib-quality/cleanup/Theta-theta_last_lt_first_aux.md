# Dedicated fresh audit: `Roth.theta_last_lt_first_aux`

Eighth introduced-helper audit in original35's unpublished Θ_lt batch; no original
count credit or publication. Scope: private helper, its necessary phi proof call, this
report. Artifacts `/private/tmp/theta35-last-first-fresh/`. No Git/shared-log/pin writes.

The helper is DELETED. Its sole phi caller now uses natural-order transitivity and
Mathlib's scalar contraction lemma directly. This uses the first adjacent ratio,
avoiding the previous last-ratio monotonicity detour. The original eight-binder
contract is recovered by an explicit independently compiled adapter. Public contracts
and all definitions/docstrings/comments are unchanged.

An explored seven-binder candidate removed hδ0, localized hanti/hratio, and replaced
the final≥3 premise with initial positivity. It compiled, but holistic review rejected
retention because a natural outer comparison makes the result a thin Mathlib wrapper.
That candidate and its evidence are explicitly superseded. Final proof7→deleted;
phi29→30, successor28/publicΘ15 unchanged. No helper introduced; eight introduced
helpers remain and three introduced/deleted obligations remain, total11.

Baseline: preceding same-a523 complete unfiltered Theta/MainLemma native diagnostics,
0errors8/3warnings in `/private/tmp/theta35-denominators-fresh/native-*-final.json`.
Inherited same-a523 whole51 profiles remain baseline only. All existing unrelated
performance failures, historical successor874.046/1373.393 failed pair and MainLemma
180s cutoff before main_lemma remain outstanding owner/later-audit obligations.
Full-project and separate LeanEval gates belong to owner.

Lean4 and mathlib-quality skills, full cleanup worker workflow, golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and applicable
style/naming/profiling references read. There is no callable builtin simplify/buzz;
the substantive scoped holistic and real performance workflows run directly.

## All24 audit items

|#|Item|Concrete disposition|
|---|---|---|
|1|Lint|No baseline target warning. Fresh complete unfiltered diagnostics required below.|
|2|HAVE scan|FIRST hr contains two by cast/numeric certificates, used once; h used once after rw; hle contains a cast certificate, used once. New first-ratio argument removes every have and rw, retaining all substantive casts inline. Caller hr0 already serves positivity at multiple sites, so reuse hr0 0. hM is proof-bearing and reused, keep.|
|3|Options|No target option/limit/attribute/debug scaffolding. Scratch search lowers maxHeartbeats to10000; default maxErrors unchanged.|
|4|Simp|No final target simp. The superseded candidate caller terminal `by simpa using hratio 0` disappears; direct cast bridge recognizes castSucc_zero definitionally. Prior unrelated measured simp exceptions retained.|
|5|Naming|Descriptive last_lt_first conclusion, private snake_case/_aux. No forbidden abbreviation/scheme number. Final helper deleted; no rename.|
|6|Packing|All3 explored candidate signature lines89/70/80 columns; final target deleted, packing N/A; next whole constituent overflows137/112. Initial first-line repack applied before final gates.|
|7|By|:= by on last header line, inline cast certificates use by on same line.|
|8|Format|Two-space proof/four-space continuation; no blank line or semicolon chain in target.|
|9|Comments|No target comments; all prior source narrative comments byte-preserved by exact reconstruction.|
|10|Docstrings|Private helper has none. Every public/module docstring unchanged.|
|11|Visibility|Private indexed Nat↔Real contraction transfer becomes a thin Mathlib composition after simplification: DELETE and inline at its one production consumer.|
|12|Structure|Target deleted (candidate2), phi30, successor28, publicΘ15 noncomment proof lines. hM8 lines including caller correction, no >10 subproof/new helper. No conjunction/existential statement.|
|13|Mathlib|Five actual search methods; full-name/source search; clean anonymous literal-final-prefix whole-goal probes. Generic scalar `mul_lt_of_lt_one_left` used directly. No complete indexed mixed-Nat/Real target found. Holistic simplification moves the outer comparison back to ℕ, leaving only a scalar contraction and order/cast composition. This IS a thin wrapper: DELETE and use Mathlib directly in phi. The initial retention argument was rejected before final gates.|
|14|Junk def|n/a: theorem, no def/abbrev/custom predicate.|
|15|Exists|n/a: no witness/existential wrapper.|
|16|Show/change|Superseded term-mode real show disappears: outer comparison stays in ℕ; no final show/change.|
|17|Negation|n/a: no by_contra/push_neg.|
|18|Generalise|Every8 FIRST and7 explored candidate effective binder drop-probed; explored candidate strict→weak tests; FIRST/replacement independent proof/adapter. Explore one removal and three local/positivity changes, then DELETE the wrapper.|
|19|Inequalities|All5 signature occurrences smaller-side-left; no ≥/>/_ge_/_gt_.|
|20|Normal form|Natural strict conclusion unchanged. Natural positive initial weight is the canonical caller hr0 certificate, real ratio retains natural→real crossing.|
|21|Syntax generality|Point comparisons were explored in the superseded candidate. The final direct proof uses caller hanti, hr0 0 and hratio 0 without any new API/binder.|
|22|Import fanout|n/a: no import edit.|
|23|Casts|Direct replacement keeps the outer last≤successor comparison in ℕ, needing only positive-weight and strict-order casts. Superseded third comparison cast/show disappears.|
|24|Instances|Explored candidate effective type has no universe/class/decidability binder; none introduced. Fin nonemptiness remains derivable from n+2.|

## Five actual Mathlib methods

|Method|Actual query/evidence|Outcome|
|---|---|---|
|A Lean-Finder|antitone natural sequence last strictly less first if contraction ratio delta less one and positive initial value|Generic lt_geom and unrelated seminorm/Stirling sequences, no whole goal match.|
|B Loogle|`_ ≤ ?c * ?b, ?c < 1, _ < ?b`|Geometric convergence/ENNReal bounds, no mixed-Nat/Real Fin theorem.|
|C LeanSearch|if a is positive and delta less than one then delta times a is less than a|mul_lt_of_lt_one_left/right/primed, mul_lt_iff_lt_one_right, smul variant. Selected scalar lemma already correct.|
|D rg Mathlib sources|Full theta_last_lt_first_aux, plus mul_lt_of_lt_one_left/succ_last/antitone_iff_succ_le|Full-name empty, untruncated scalar/Fin source hits retained.|
|E local name pattern|mul_lt_of_lt_one_left, limit8|Both primed/unprimed scalar facts verified; index unavailable, not an indexed absence proof.|

Raw `search.json`, `mathlib-{full-name,source}-search.log`. Auxiliary strict/weak,
left/right/primed/scalar/geometric/smul variants examined. Common-equivalents discrete,
finiteness,separation,bornology buckets do not apply. Searches establish no selected
complete replacement, never universal absence.

Final generic whole-goal search uses anonymous examples of the literal selected local replacement statement against the exact FINAL prefix before
the target, closes Lemma7 then Roth, positively asserts target/later Root.Θ_lt absence.
No import Roth.Theta/failed named trial contaminates automation. Eleven bounded
strategies in split5+6 batches,10000 heartbeats/default maxErrors; every BEGIN/END
must be reached. Initial unpacked-header runs archived and literal final-header reruns
used in final evidence. Negative trial files never certify positive values/axioms.

## Every FIRST/explored-candidate binder, generality and inversion

|Binder|Drop/weakening candidate and actual role|Disposition|
|---|---|---|
|n|FIRST/explored candidate drop fails dependent Fin bound; concrete finite ordered indices required by unchanged conclusion|Keep implicit ℕ, no new universe.|
|δ|FIRST/explored candidate drop fails real ratio and hδ1|Keep real contraction scalar; no fixed-field abstraction used elsewhere.|
|hδ0|FIRST proof drop fails multiplication monotonicity; first-ratio candidate compiles with no nonnegative premise|REMOVE; original/full adapter verifies recovery. New natural first-ratio+positive initial weight already forces nonnegative δ, so this removal is redundancy elimination, not evidence of realizable negative δ.|
|hδ1|FIRST/explored candidate drop fails strict scalar contraction; δ≤1 substitution fails|Keep strict δ<1; constant sequence at δ1 refutes weakening.|
|r|FIRST/explored candidate drop fails dependent statement and all ratio/order hypotheses|Keep natural multiplicities/Fin domain; established caller domain.|
|hanti|FIRST/explored candidate drop fails comparison; global Antitone replaced by rlast≤r(succ0), compiled|Superseded candidate local premise. Original hanti (Fin.le_last _) supplies it.|
|hrlast|FIRST/explored candidate drop fails positivity; lower final≥3 replaced by 0<r0; nonnegative replacement fails|Superseded candidate initial-positive requirement; old final bound+antitone derives it.|
|hratio|FIRST/explored candidate drop fails chain; all adjacent ratios replaced by first one, compiled|Superseded candidate local premise; original ratio0 with castSucc_zero supplies it.|

No effective typeclass/universe/decidability argument to weaken. Drop-test failures
are proof-substitution observations, not claims of logical necessity. Original
hδ0 is inferred from other old facts in an alternative proof; selected candidate makes
this redundancy explicit. `Weaken.lean` negative tests separate from successful FIRST/
replacement proof and strictness examples. Natural initial1,last0 satisfies new positive
premise but fails old final≥3. `![2,0,1,0]` satisfies explored candidate local premises with δ0 while
failing global antitonicity and the old all-ratio requirement; examples compiled in
positive semantic files. The explored candidate strictly broadens the old private theorem; the final production helper is absent.

Public-literature search n/a: private declaration is explicitly exempt under
cleanup§2.6d. Mathematical generality/inversion still examined. No project Θ object is
unfolded; proof immediately works with order/cast arithmetic. A scalar ordered-ring
restatement simply composes the existing scalar contraction/order API; creating another
public theorem would duplicate Mathlib and add no supported downstream user. Replacing
Fin indexing or ℕ weights would change retained telescope/conclusion/universe arity and
the established callers' natural-weight setting. No such broad abstraction/new API is recommended. Delete the scalar wrapper and use Mathlib directly at the existing caller.

## All42 golf rules

|Rule|Concrete disposition|
|---|---|
|1.1|No by-exact wrapper; exact_mod_cast performs genuine conversion.|
|1.2|n/a no by-rfl.|
|1.3|FIRST rw/exact chain disappears with last-ratio construction.|
|1.4|Superseded caller simpa eliminated in direct replacement; castSucc_zero recognized definitionally.|
|1.5|n/a no trailing rfl.|
|1.6|n/a no constructor.|
|1.7|n/a no apply/exact chain.|
|1.8|n/a no contradiction/negation branch.|
|1.9|No target lambda; hratio universal removed.|
|1.10|APPLIED: all3 FIRST have computations disappear, inline local cast and scalar contraction; existing reused caller hr0 retained.|
|1.11|n/a no apply/intro.|
|1.12|Superseded real show eliminated; final outer comparison stays in ℕ.|
|1.13|n/a no conjunct projections.|
|1.14|FIRST only rw eliminated; no consecutive rw.|
|1.15|No target simp only; new caller terminal simpa unsqueezed.|
|1.16|No new bare nonterminal simp.|
|1.17|.trans_lt directly composes both local comparisons.|
|1.18|Nested parentheses delimit hanti conversion and scalar proof arguments before trans_lt; retain.|
|1.19|n/a no push_neg.|
|1.20|n/a no ∃ wrapper.|
|2.1|Whole literal-current-goal grind actually tried.|
|2.2|n/a no production grind/preliminary tactic steps.|
|2.3|Final ratio0 casts recognized directly, no simpa needed.|
|2.4|n/a no function regularity property.|
|2.5|Whole-goal positivity actually tried.|
|2.6|Whole-goal gcongr actually tried.|
|2.7|Whole-goal lia actually tried.|
|2.8|Whole-goal aesop actually tried.|
|2.9|Whole-goal norm_num tried; selected exact_mod_cast supplies true Nat/Real bridges.|
|2.10|Whole-goal decide tried; no native_decide.|
|2.11|Whole-goal try field_simp followed by actual ring tried.|
|2.12|n/a selected proof has no ring/ring_nf block.|
|2.13|n/a no symmetric cases.|
|2.14|APPLIED nested term composition, no calc/hle detour.|
|2.15|n/a no parallel uniform subgoals.|
|3.1|n/a no erw.|
|3.2|n/a no legacy continuity/measurability.|
|3.3|No omega; lia actual trial as2.7.|
|3.4|n/a no rcases/rfl.|
|3.5|No simp/grind attribute: private multi-assumption contraction intended for explicit phi call.|
|3.6|Whole-goal simp_all tried; no simp_all only.|
|3.7|Zero production limits/options raised/introduced.|

Holistic simplify outcome ISSUES-FOUND-AND-FIXED. FIRST last-ratio route unnecessarily
needs nonnegative scaling of an earlier weight comparison; first-ratio route gives
strict descent immediately and only requires the last≤first-successor comparison.
Inline scalar/cast chain, reuse existing caller hr0, DELETE the resulting thin wrapper and inline the scalar/cast/order proof directly in phi.
All static24/42/HAVE/generality/packing/inequality decisions complete BEFORE final
module/semantic/native/profile cycle; no further source edit planned.

## Measured packing and inequalities

|Signature line|Width|Next complete constituent width|Arithmetic/action|
|---|---|---|---|
|1|89|hanti47|89+1+47=137>100; ok|
|2|70|hratio41|70+1+41=112>100; ok|
|3|80|—|last line; ok|

Every proof line≤100. Effective type printed at format.width100 in semantic log.

|Occurrence|Line:column|Relation|Disposition|
|---|---|---|---|
|hδ1|1:64|<|smaller-left|
|hanti|2:35|≤|smaller-left|
|hrlast|2:65|<|smaller-left|
|hratio|3:36|≤|smaller-left|
|conclusion|3:70|<|smaller-left|


## Final deletion decisions before final gates

The final replacement keeps natural order for last≤first-successor, and casts only
the strict real first-ratio contraction. This reduces the content to `LE.le.trans_lt`,
`mul_lt_of_lt_one_left` and genuine Nat/Real casts, with no independent indexed
mathematical estimate. The rule forbidding thin Mathlib wrappers therefore applies.
The full direct-source candidate compiled exit0 in30.159s before application. It
keeps phi30 lines and hM8 lines, with publicΘ15, no new helper, no public change.
All earlier seven-binder proof/build/search/parameter evidence and the cancelled
retained-candidate gate queue are preserved in superseded-seven-binder/. A graceful
stop-before-next-request cancelled that queue BEFORE any final module/semantic
launch; there was no orphan process or rejected compiler result hidden as success.

Final clean searches use the literal SELECTED LOCAL REPLACEMENT statement/premises
as anonymous examples; the seven-binder removed candidate is never called CURRENT
production evidence. The selected local statement uses hδ1, Antitone r, ∀j positivity
and all adjacent ratios, exactly the supporting premises actually available at phi. They use the exact
FINAL source prefix ending at the deleted declaration location, which is unchanged,
and positively assert target/later RootΘ absence. Earlier candidate7 searches remain
superseded evidence. The independent FIRST8 proof is re-elaborated with its entire
exact original context. A separate independent selected-site replacement7 proof and its explicit
original8 adapter recover the full old contract. The module has50 actual declarations,
not51; all50 opaque values are checked for deleted-target references. Actual phi,
successor and publicΘ values/types/axioms and positive scalar→phi→successor→Θ
dependencies are checked. Deleted-target production timing is N/A, never0.

The preceding251 scaffold receives EXACTLY TWO retained-helper inventory edits:
remove theta_last_lt_first_aux from the actual value/axiom loop and the actual type/
binder-print loop. Inverse replacements reconstruct every prior scaffold byte. All
unaffected checks and four full immutable proof blocks remain exact; the one prior
retained-target value marker is superseded by explicit actual-constant/reference
absence markers. No claim that the entire final preceding scaffold bytes are identical.

All24 audit/all42 golf/HAVE/generality/inversion/packing/inequality decisions completed
now, before the FINAL deletion module/semantic/native/profile cycle. Source frozen.

Final signature packing: production target deleted, N/A. Immutable FIRST signature
widths81/88/69/36, next whole constituent widths21/63/34 give103/152/104>100;
all unchanged (`packing-original.json`). The candidate7 three-line packing table
above is explicitly superseded evidence. Actual deleted-target type/value absence
is a required final gate; no empty/zero timing stands in for it. All scratch
replacement theorems are verification-only and introduce no production helper.


## Final clean search and parameter evidence

The final eleven anonymous searches use exactly selected-local-replacement.txt's
literal local statement and the exact final pre-deletion-location source prefix.
All11 BEGIN/END pairs reached with default maxErrors and10000 scratch heartbeats.
Positive prefix target/RootΘ absence compiled exit0, and final prefix/source/header
hash reconstruction passes. Candidate7 automation and unpacked-header runs remain
explicitly superseded, never CURRENT production evidence. Every8 FIRST and7 explored
candidate binder has a diagnostic in its own drop range; both candidate strict→weak
premises fail. These negative observations are not indispensability/axiom claims.
The independent selected local replacement and FIRST8 adapter are successful positive
proof evidence. `automation-results-final.json`, `binder-results.json`,
`final-current-prefix-verification.json` retain all ranges/provenance.

|Final selected-site strategy|Observed result|
|---|---|
|grind|`grind` failed|
|aesop|Tactic `aesop` failed, made no progress|
|exact?|`exact?` could not close the goal. Try `apply?` to see partial suggestions.|
|apply?|(deterministic) timeout at `whnf`, maximum number of heartbeats (10000) has been reached|
|simp_all|simp_all made no progress|
|gcongr|`gcongr` did not make progress.|
|positivity|not a positivity goal|
|norm_num|unsolved goals|
|lia|`grind` failed|
|decide|Expected type must not contain free variables|
|field_simp/ring|`ring_nf` made no progress on the goal|

## Immutable FIRST, complete semantic scaffold, actual built values

FirstIndependent.lean starts with the ENTIRE exact FIRST batch2 bytes, including its
original import/namespace and all before/after declarations, no added section/universe/
class/omit. The FIRST8 proof independently re-elaborates and has no dependency on the
replacement or adapter. The explicit old8 adapter invokes a separately proven literal
selected-site7 replacement; all8 old names/types/BinderInfo/order/universe arity and
conclusion compare exactly. The replacement uses the same hδ1, Antitone r, hr0 and
adjacent ratios and proof expression as the final phi site; it is scratch-only, no
production helper. FIRST/adapter/replacement opaque values use value!true with inferred
types and standard axioms only. Exact immutable FIRST success logs/status/texts remain
unchanged.

The preceding251 scaffold receives exactly two minimal actual-helper-inventory edits,
removing the deleted target from actual value/axiom and type/binder loops. Inverse edits
recover its ENTIRE original bytes, SHA63962bfe..., not a header-only reconstruction.
All250 unaffected prior PASS checks remain; the one retained-target value check becomes
explicit deletion/reference-absence checks. The four immutable full blocks remain byte-
identical: Index72cf, Theta355a, ENTIRE original2b MainLemma proof, ENTIRE independent
updated MainLemma proof. Metadata offsets are recomputed after the54-byte inventory
shrink, hashes unchanged. All earlier explicit old adapters, deleted-wrapper checks,
publicΘ9 and MainLemma's ENTIRE26-binder contract/definitions remain intact.

Actual current phi's full FIRST/current telescope compares names/types/BinderInfo/order/
universes/conclusion. Actual phi/successor/publicΘ opaque values/types/standard axioms
and positive scalar→phi→successor→Θ dependencies pass. Actual MainLemma value/axioms/
RootΘ dependency and complete independent original/current caller proofs recheck through
the inherited scaffold; imported Root.main_lemma is never used as independent proof.
The deleted production target is positively absent, and all50 actual Theta opaque values
have no reference to it. Fresh successful FIRST log20 clean PASS markers; combined
semantic log270=250 unaffected+20 fresh, no PANIC/error/sorryAx/nonstandard axiom.
Both actual module builds occur BEFORE Root opaque-value queries.

## Fresh module, semantic and native gates

|Gate|Actual command/evidence|Result|
|---|---|---|
|build-theta-final|/Users/ramin/.elan/bin/lake build Roth.Theta; build-theta-final.json/.log|exit0, 30.382s|
|build-mainlemma-final|/Users/ramin/.elan/bin/lake build Roth.MainLemma; build-mainlemma-final.json/.log|exit0, 38.649s|
|first-independent-final|/Users/ramin/.elan/bin/lake env lean FirstIndependent.lean; first-independent-final.json/.log|exit0, 63.452s|
|actual-semantics-final|/Users/ramin/.elan/bin/lake env lean ActualSemanticsAugmented.lean; actual-semantics-final.json/.log|exit0, 128.086s|
|definition_protected|Exact entire source inverse reconstruction, only target deletion/one phi proof replacement|PASS, all defs/abbrevs/imports/pins unchanged|
|theorem_statement_protected|FIRST8 adapter, phi complete original/current type, inherited publicTheta9/Main26 metadata|PASS, no public contract change|
|structure_gate|line-counts.json|Deleted targetN/A, phi30, successor28, publicΘ15; hM8/no>10 subproof|
|naming_gate|Deleted helper; all retained names unchanged|PASS, no forbidden name/rename|
|line_packing_gate|Final target deletedN/A; full immutable FIRST and superseded candidate measured|PASS, no underpacked final target|
|inequality_orientation_gate|All five superseded candidate occurrences and full FIRST oriented smaller-left; final target absent|PASS|
|cumulative scoped consumers|Both builds, complete independent callers, actual values/axes/dependencies, complete natives|PASS|
|full project/separate LeanEval|Owner-only final frozen gates|PENDING, not claimed here|
|whole-file performance|Unrelated slow declarations/MainLemma unmeasured finite caller|NOT CLAIMED|

Fresh COMPLETE UNFILTERED diagnostics (all warning objects retained verbatim in raw JSON):

|Module|Success|Partial|Timed out|Errors|Warnings|
|---|---|---|---|---|---|
|theta|true|false|false|0|8|
|mainlemma|true|false|false|0|3|

Every unfiltered warning, with complete message below:

- theta:1:2, warning:

```text
* `-/`:
Copyright too short!


Note: This linter can be disabled with `set_option linter.style.header false`
```

- theta:93:43, warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:101:27, warning:

```text
Variable name `hB` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hB

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:101:64, warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:109:28, warning:

```text
Variable name `hB` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hB

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:129:81, warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:252:6, warning:

```text
Variable name `hr` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- theta:547:47, warning:

```text
Variable name `hq` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hq

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- mainlemma:1:2, warning:

```text
* `-/`:
Copyright too short!


Note: This linter can be disabled with `set_option linter.style.header false`
```

- mainlemma:149:28, warning:

```text
Variable name `hδ0` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hδ0

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

- mainlemma:149:69, warning:

```text
Variable name `hr₁` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _hr₁

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

No target warning or new warning introduced. Header metadata and the explicitly selected
public hq/extra Θ hB/hr premises follow user choices. Other unused hypotheses remain under
their existing checkpoint scope or technical retention decisions; this audit does not
turn those decisions into a user veto. Scratch adapter's unused original hδ0 is
intentional full-contract recovery, never deleted/silenced. Whole-source direct candidate
and final builds/semantics are positive evidence; failed/negative automation is separate.

## Simplify/refactoring and all11 steps

Simplify outcome ISSUES-FOUND-AND-FIXED, performed directly (no callable builtin tool).
The initial retained7 candidate was rejected as a thin wrapper after moving the outer
comparison to ℕ. Final action: DELETE and use Mathlib directly; no other helper/API/
rename recommended. Phase5a deletion complete with FIRST adapter/actual absence checks;
Phase5b has no rename/shared queue mutation. Buzz performance evidence follows below.

|Step|Result|
|---|---|
|1|✓ Required skills/workflow/references read|
|2|✓ All24 concrete audit dispositions and deletion decision|
|2.5|✓ Five actual methods,11 final selected-site literal-prefix trials,positive absence|
|2.6|✓ Every8 FIRST/7 explored candidate binder probed; strictness,FIRST adapter,inversion/private exemption|
|2.7|✓ Every4 FIRST/3 superseded candidate signature line measured; final deletedN/A|
|2.8|✓ All5 candidate inequality occurrences measured; FIRST same orientation; final absent|
|3|✓ All42 golf-rule dispositions; thin-wrapper deletion applied|
|4|✓ Holistic review chose direct natural comparison/scalar contraction|
|5a|✓ Fresh complete unfiltered native diagnostics0errors|
|5b|✓ Actual modules/complete independent semantics/opaque values/types/axioms/deletion gates; final profiles below|
|6a|✓ No rename/shared queue mutation|


## Actual final performance and drain

All normal/native requests drain before BOTH real captures; pre-final-{first,repeat}-
drain.json records dead process groups/pending[]. Command:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Theta.lean`. External420s capture window changes no
Lean limit. Both complete actual whole50 traces exit0, strictUTF8, all50 source anchors.
Raw logs/strict slices retain byte offsets/hashes. Count disjoint outer command plus
associated async proof/addDecl/linter rows; nested kernel/macro duplication excluded.
Exactly two final-source captures, no third cherry-picked sample. Deleted-target
production timing N/A, never0; no diagnostic/candidate timing stands in for production.

|Run|Actual declaration|Conservative ms|Proof anchors|
|---|---|---|---|
|final-first|theta_phi_lt_aux|794.875|1|
|final-first|theta_lt_succ_aux|1021.004|1|
|final-first|Θ_lt|347.571|1|
|final-first|theta_last_lt_first_aux|N/A, deleted|N/A|
|final-repeat|theta_phi_lt_aux|609.435|1|
|final-repeat|theta_lt_succ_aux|958.222|1|
|final-repeat|Θ_lt|339.537|1|
|final-repeat|theta_last_lt_first_aux|N/A, deleted|N/A|

Scoped acceptance concerns the deleted target's direct phi replacement: both actual
phi samples must be<1000ms. First phi794.875ms required the repeat (≥750ms), preserved
without cherry-picking. PublicΘ samples are reported for completeness. Successor's
first1021.004ms is a NEW actual failure on this frozen source and remains for its
separate fresh audit, alongside historical874.046/1373.393ms; this checkpoint NEVER
claims successor or whole-file performance PASS. All fresh outside-scope over-budget
rows retained in outside-scope-overbudget.json with raw samples and actual anchors.

The separate mandatory final repair queue also retains sum_max_sub_le_index_det,
index_separated_mul_le_aux, index_det_le, index_numeric_bound_aux/index29,
index_le_lem6, lem7_Φ_bound, lem7_numeric, and the earlier positive-quadratic-helper
1074.965ms. No unrelated declaration edited, no historical failure erased. MainLemma's
old180s cutoff before main_lemma remains unmeasured finite caller timing; build/native/
semantic PASS never substitutes a finite performance sample for it.

Buzz outcome: scoped FAST-BOARD for deleted target's direct phi replacement ONLY,
with mandatory successor and whole-file repair obligations explicitly outstanding.
Zero limit raises/options/scaffolding/native_decide/sorry/new axioms. No further
simplify/recompression pass follows measurements.

## Exact freeze and complete handoff

|Source|SHA256|
|---|---|
|Roth/Theta.lean|c31bd43e04be12fa6f1dadfe98e7b2092d8467ef76eb906b7cf68d1621b14b8f|
|Roth/MainLemma.lean|ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4|
|Roth/Main.lean|f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069|

Total source1001→990 lines (-11); helper7 proof lines→deleted, phi29→30 noncomment
proof lines, hM8, publicΘ15. No comments/docstrings/definitions/public header/import/
pin changed. One helper deleted, no helper introduced; introduced-helper inventory
now8 retained+3 introduced/deleted=11 fresh obligations, no obligation lost. Remaining
fresh audits after this target are successor, large-δ, and introduced/deleted fin_option.
Counts215/264, Theta34/35 unchanged. No original-count credit, commit, push or publication.

FIRST three batch texts and original success log/status hashes all unchanged; four
complete immutable proof blocks unchanged. Minimal retained-inventory edits are
explicitly recorded and inverse-verified; no whole-preceding-scaffold byte identity
is claimed. Final semantic20/270 markers, native complete0errors, actual profile
raw/table/strict-slice provenance and exact sources/pins/artifact hashes are frozen
in final-freeze.json. Report `.mathlib-quality/cleanup/Theta-theta_last_lt_first_aux.md`.

Source edit authority explicitly REVOKED. All own source/scratch/report/compiler/native
requests drained with pending[], normal_pending[], native_pending[]; all such authority
released at terminal handoff (`final-process-drain.json`, `final-freeze.json`). No source
edit after freeze. Owner retains Git/shared logs and still owes all remaining fresh
introduced audits, cumulative29/allactual values+axioms/final performance repairs,
full lake build THEN separate frozen Roth.LeanEval before ANY original35 publication.
This report claims only the last<first-helper deletion checkpoint.


## Owner evidence clarification

Owner verified all247 original artifact hashes before this prose-only clarification.
The exact leaf report matching its frozen hash is archived as
`/private/tmp/theta35-last-first-fresh/leaf-final-report-owner-input.md`; the immutable
leaf freeze remains historical evidence. No source or compiled gate changed.
Final selected-site negative captures are `automation-final-{0,1}.log/.json`;
`automation-{0,1}.log/.json` are superseded seven-binder candidate captures. The actual
final apply? timeout is reported by Lean at source10:58; its diagnostic occurs within
its own final BEGIN/END markers. All other final strategy errors occur in their
literal example ranges; the independent positive prefix-absence compile exits0.
The retention of private Fin/Nat/Real domains is a technical recommendation here,
not a separate user prohibition against generalization.
