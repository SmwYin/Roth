# Dedicated fresh audit: `Roth.theta_denominators_one_lt_aux`

Seventh introduced-helper audit in original35's unpublished Θ_lt batch; no original
count credit or publication. Scope: this private declaration, its three necessary
routine proof calls, and this report. No Git/shared-log/pin write. All artifacts are
under `/private/tmp/theta35-denominators-fresh/` unless explicitly qualified.

The private contract is reduced from eleven to seven effective binders. Its initial
weight premise becomes `hrlast : 0 < r 0`, and its logarithm premise becomes
`hq1 : 0 < Real.log (q 0)`. The no-longer-needed δ/hδ0/hδ1/hratio binders disappear.
The full immutable FIRST eleven-binder adapter derives initial positivity from the
old final-weight/ratio assumptions and the old numerical log threshold. All retained
names/order/BinderInfo/universe arity/conclusion remain unchanged. Proof8→3 noncomment lines;
three routine calls derive the direct positivity certificates. No public header or
definition changes. No helper added/deleted. Public Θ proof stays15 lines.

Baseline: inherited identical90e complete unfiltered native Theta/MainLemma0errors8/3
warnings, from `/private/tmp/theta35-base-fresh/native-{theta,mainlemma}-final.json`.
Inherited actual whole51 pair: denominator264.797/287.209ms, phi580.209/523.160ms,
successor773.960/811.984ms, publicΘ258.708/275.710ms in that directory. These are
baseline evidence only. Historical successor874.046/1373.393 failed pair is preserved;
its separate later audit and performance repair remain required. Earlier whole-source
unrelated failures and MainLemma's cutoff before main_lemma are not claimed resolved.
Full project/cache/linter executable and separate final LeanEval are owner gates.

Lean4/mathlib-quality skills, full cleanup worker workflow, mandatory five references
and relevant style/naming/profiling references were read. Actual Lean4.34 profiling
uses --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0, superseding the old
reference spelling. No builtin simplify/buzz tool is available; their substantive
scoped holistic and performance workflows are performed directly.

## All24 audit items

| # | Item | Concrete disposition |
|---|---|---|
|1|Lint|Inherited complete same-source baseline has no target warning. Fresh unfiltered final diagnostics retained below.|
|2|Have scan|FIRST hanti has a by proof but belongs to the removed induction certificate; no longer needed. FIRST hr/hL/hLj are each single-use terms (hr/hL contain nested by certificates): hr/hL become direct hypotheses; hLj is inlined at log_pos_iff. Final target has no have. Existing phi hq has two uses (base positivity/singleton bound); existing successor hq has two uses (base positivity/all denominator positivity), retain both. Caller positivity certificates are proof arguments with by content.|
|3|Options|No production option/attribute/limit/scaffolding. Scratch automation lowers maxHeartbeats to10000, with default maxErrors.|
|4|Simp|No target simp. Only required routine calls lose old Nat.cast normalization because the direct log premise already matches hq1. All unrelated squeezed-prefix/performance exceptions preserved.|
|5|Naming|theta_denominators_one_lt_aux describes all denominators being greater than one; private snake_case/_aux; no forbidden abbreviation/number. No rename needed.|
|6|Packing|Every final signature line measured below; first two lines94/93 columns, next whole constituents exceed100.|
|7|By|:= by remains on declaration's last header line; no isolated by.|
|8|Format|Two-space proof indent, four-space header continuation, no blank proof line/semicolon chain.|
|9|Comments|The old `-- r is antitone` comment is removed as stale: the generalised target assumes no ratios and need not have antitone r. Actual successor antitone proof remains in its caller; all other comments preserved.|
|10|Docstring|Private helper has none; existing public/module documentation byte-identical.|
|11|Visibility|Private substantive weighted-log positivity transfer used at three production sites. No visibility change.|
|12|Structure|Target3 proof lines; phi29/successor28/publicΘ15 noncomment proof lines. No new >10 branch/subproof, conjunction or existential. No helper extraction.|
|13|Mathlib|Five actual methods, full-name/source search and eleven clean anonymous literal-current-goal trials. Scalar components used directly; no full weighted-log-to-Nat conclusion replacement found. Selected proof composes mul_pos, strict/non-strict trans_le, pos_of_mul_pos_right, log_pos_iff and two cast certificates: more than three substantive Mathlib/order calls, not a thin1–3-call wrapper.|
|14|Junk def|n/a: proposition, no def/abbrev/custom predicate.|
|15|Exists|n/a: no existential/witness wrapper.|
|16|Show/change|n/a: neither tactic occurs.|
|17|Negation|n/a: no push_neg/by_contra.|
|18|Generalise|All11 FIRST/current-old and7 current effective binders drop-probed; positivity weakening and point-locality compiled probes. Two direct premise weakenings/four binder removals applied with full FIRST adapter.|
|19|Inequality|All four current occurrences oriented smaller-side-left; no ≥/> or _ge_/_gt_ name.|
|20|Normal form|Natural denominator conclusion1<qj retained. Positive initial logarithm is equivalent to1<q0; log form chosen because every caller directly has a log lower bound.|
|21|Syntax generality|Direct initial weight/log premises match the mathematical positivity transfer, eliminating unrelated induction thresholds. hqr remains ∀j so its retained order precedes j; point-locality would require reordering j and is not applied under the explicit retained-order constraint.|
|22|Import fanout|n/a: no import added/removed.|
|23|Casts|Old final-weight→ℝ certificate gone from target; hrlast now natural. Two genuine Nat→ℝ crossings remain in hqr, and q arguments of Real.log. `exact_mod_cast hrlast` and final exact_mod_cast are load-bearing bridges. Caller real0/3 annotations pin cast targets; no decorative casts added.|
|24|Instances|No effective universe/class/decidability binder, no named/local/global instance introduced; current count7 verified on actual opaque type.|

## Five actual search methods and generic routes

| Method | Actual query | Observation |
|---|---|---|
|A Lean-Finder|natural number greater than one if logarithm positive weighted logarithms comparison positive natural coefficients|Unrelated posLog/Nat.log/recurrence results; no full target match.|
|B Loogle|Real.log, 0 < _|Real.log_pos and standard log comparison components.|
|C LeanSearch|positive logarithm if and only if one less than nonnegative real number|Real.log_pos_iff exact scalar component; ENNReal/logb variants examined.|
|D local source rg|theta_denominators_one_lt_aux; log_pos/log_pos_iff/pos_of_mul_pos_right/antitone_iff_succ_le|Full-name search empty, untruncated component results retained.|
|E local name patterns|Real.log_pos, limit10|Real.log_pos/log_pos_iff/negative branch and ENNReal variants; index unavailable, not an indexed absence proof.|

Raw responses `search.json`, `mathlib-full-name-search.log`, `mathlib-source-search.log`.
No common-equivalents discrete/finiteness/separation/bornology bucket applies. Auxiliary
log_pos/log_pos_iff/log_nonneg_iff/logb/ENNReal/negative variants were examined; the
negative-real logarithm branch is excluded by natural denominators. This search does
not claim universal absence. No Mathlib-complete match is substituted by a project wrapper.

The clean files start with exact CURRENT source bytes before the target, close
section Lemma7 then namespace Roth, and positively assert audited target/later RootΘ
absence. No import Roth.Theta contaminates this search. Every anonymous example has
literal CURRENT production header; no named failed theorem can be found by exact?/apply?.
Eleven strategies run in bounded batches5+6 with maxHeartbeats10000/default maxErrors.
Initial unpacked-header attempts remain archived; final repacked-header runs are the
literal final-source searches. Prefix before target itself did not change. Separate
PrefixAbsence exit0 is positive clean-environment evidence; negative trials are not
positive proof/value/axiom evidence. Full strategy/range/marker outcomes appended below.

## Every effective binder, mathematical generality and inversion

`Binder-old-{0..3}.lean` and `Binder-current-{0..2}.lean` drop each effective binder
individually with autoImplicit=false; bounded batches preserve every trial's diagnostics.
`Weaken.lean` probes both strict→weak premises and the point-local reordered alternative.
Proof-substitution failure is not a logical indispensability claim.

| Binder | Actual role | Compiled candidate/disposition |
|---|---|---|
|n|Finite index bound in r/q/j|FIRST/current drop fails in dependent statement. Keep; no standalone typeclass binder.|
|δ|Old ratio and numerical log threshold|FIRST direct drop fails; after supplying direct positivity, entire current proof compiles without δ. REMOVE.|
|hδ0|Old numerical threshold positive|FIRST drop fails positivity; current direct logarithm premise makes it unnecessary. REMOVE with adapter.|
|hδ1|Old antitone certificate|FIRST drop fails at hanti; current initial-positive premise needs no antitone certificate. REMOVE.|
|r|Natural nonnegative weights|FIRST/current drop fails dependent statement; needed in weighted log comparison. Keep domain: natural multiplicities are established caller domain.|
|q|Natural denominators|FIRST/current drop fails dependent statement; log and Nat conclusion cross through Real.log_pos_iff. Keep natural denominator domain.|
|hrlast|Old lower bound3 at final index, now positive initial weight|FIRST/current drop fails; direct initial positivity compiles; nonnegative substitution fails. APPLY weaker premise; old ratios/final bound derive it.|
|hratio|Old antitone certificate|FIRST drop fails hanti; direct initial positivity removes all use. REMOVE.|
|hq1|Old large numerical log lower bound, now positive initial log|FIRST/current drop fails; nonnegative log substitution fails. APPLY direct positivity. Original δ>0 and positive numerator imply it.|
|hqr|Weighted log lower bound for every j|FIRST/current drop fails. Point-local variant compiles after moving j before hqr, so consciously unapplied to preserve explicit retained binder order.|
|j|Chosen denominator|FIRST/current drop fails in conclusion. Keep explicit Fin index.|

No universe/class weakening: actual universes empty and mathematical data ℕ/ℝ are fixed
by finite index, natural denominator conclusion and Real.log. Strictness examples with
weight1 and denominator2 compile: new premises hold while old3-bound/numerical log
threshold fail. Generic arbitrary index/marked basepoint is mathematically possible but
would change the whole private indexing contract and introduce an extra basepoint;
three existing consumers all use Fin's canonical0, with no supported downstream benefit.
No extra helper/API/rename is recommended.

Literature search n/a: private auxiliary is explicitly exempt under cleanup§2.6d.
Mathematical generality/inversion still examined: no project Θ or other concrete witness
is unfolded; the theorem is already a scalar weighted-log positivity transfer. Real.log
is used by its named positivity equivalence at the conclusion, with natural nonnegativity
excluding the negative-real log branch. Replacing log with an arbitrary function would
need its corresponding positivity-to-denominator axiom, a generality of one in these
callers. Retain the supported direct-premise statement.

## All42 golfing rules

|Rule|Concrete disposition|
|---|---|
|1.1|n/a: no by-exact wrapper.|
|1.2|n/a: no by-rfl wrapper.|
|1.3|n/a: no rw/exact sequence.|
|1.4|n/a: no simp/exact sequence in target; old caller cast simpa no longer needed.|
|1.5|n/a: no trailing rfl.|
|1.6|n/a: no constructor chain.|
|1.7|n/a: no apply/exact chain.|
|1.8|n/a: no contradiction/negation branch.|
|1.9|Old hanti lambda disappears with unnecessary induction certificate.|
|1.10|APPLIED: single-use term hLj inlined; hr/hL become direct premises, hanti computation removed. No final have. Existing caller hq reused twice, retain.|
|1.11|n/a: no apply/intro.|
|1.12|n/a: no show.|
|1.13|n/a: no conjunction projection.|
|1.14|n/a: no rw.|
|1.15|n/a: no terminal simp only in target; unrelated measured squeezed-prefix exception preserved.|
|1.16|n/a: no bare nonterminal simp introduced.|
|1.17|Existing .trans_le connects positive initial product to each product directly.|
|1.18|Nested parenthesis delimit pos_of_mul_pos_right arguments and its first proof before the second; retain.|
|1.19|n/a: no push_neg.|
|1.20|n/a: no existential.|
|2.1|Whole literal-current-goal grind actually tried.|
|2.2|n/a: no production grind/preliminary steps.|
|2.3|No selected simp consolidation needed.|
|2.4|n/a: no function regularity property.|
|2.5|Whole-goal positivity tried; caller positive numerical quotient closes by positivity.|
|2.6|Whole-goal gcongr tried; direct multiplication-positivity transfer selected.|
|2.7|Whole-goal lia tried; nonlinear log comparison needs scalar log equivalence.|
|2.8|Whole-goal aesop tried.|
|2.9|Whole-goal norm_num tried; selected natural/real bridges use exact_mod_cast and caller concrete0<3 uses norm_num.|
|2.10|Whole-goal decide tried; no native_decide.|
|2.11|Whole-goal field_simp/ring tried. No selected identity needs field normalization.|
|2.12|n/a: selected proof has no ring/ring_nf-ending block.|
|2.13|n/a: no symmetric cases.|
|2.14|APPLIED direct term composition from positive initial product through hqr to log positivity, no calc needed.|
|2.15|n/a: no parallel uniform subgoals.|
|3.1|n/a: no erw.|
|3.2|n/a: no legacy continuity/measurability.|
|3.3|No omega; lia trial covers2.7.|
|3.4|n/a: no rcases/rfl.|
|3.5|No new automation attribute: private multihypothesis transfer with three explicit consumers.|
|3.6|Whole-goal simp_all actually tried; no selected simp_all only.|
|3.7|Zero production limits/options/scaffolding introduced/raised.|

Step-back/holistic simplify: the original proof first reconstructs assumptions stronger
than the actual positive-product/log argument needs. Direct initial positivity removes
that induction plumbing and inlines the terminal intermediate fact. Existing callers
already have initial weight positivity or antitonicity, and numerical log bounds;
no duplication/new helper/public contract adjustment is needed. All static HAVE/golf/
generality/packing/inequality decisions complete before final gates.

## Measured packing and inequalities

|Signature line|Width|Next complete constituent|Arithmetic/action|
|---|---|---|---|
|1|94|hq1,26|94+1+26=121>100; ok|
|2|93|j binder,17|93+1+17=111>100; ok|
|3|37|—|last line|

Initial first line75 left room for hrlast; it was repacked before final gates.
All final proof lines≤100. Effective type prints at format.width100 in semantic logs.

|Occurrence|Line:column|Relation|Action|
|---|---|---|---|
|hrlast|1:89|<|smaller-side-left|
|hq1|2:14|<|smaller-side-left|
|hqr|2:71|≤|smaller-side-left|
|conclusion|3:27|<|smaller-side-left|

## Final clean search and parameter outcomes

| Strategy | Observed result |
|---|---|
|grind|`grind` failed|
|aesop|Tactic `aesop` failed, made no progress|
|exact?|`exact?` could not close the goal. Try `apply?` to see partial suggestions.|
|apply?|(deterministic) timeout at `transform`, maximum number of heartbeats (10000) has been reached|
|simp_all|simp_all made no progress|
|gcongr|`gcongr` did not make progress.|
|positivity|not a positivity goal|
|norm_num|unsolved goals|
|lia|`grind` failed|
|decide|Expected type must not contain free variables|
|field_simp/ring|unsolved goals|

All eleven final BEGIN/END pairs reached. The field_simp/ring trial uses `try field_simp`
then actually runs ring; apply? hits the deliberately lower10000-heartbeat bound.
Initial unpacked-header trials remain in superseded-unpacked-header/, not current evidence.
All18 original/current binder drops have errors in their recorded ranges; both strict→weak
positivity substitutions fail. The reordered point-local hqr candidate also compiles alone
with exit0 (local-positive.json/.log), and is consciously unapplied to preserve retained
argument order. Full outcomes/ranges are binder-results.json and automation-results.json.
final-current-prefix-verification.json positively rehashes FINAL source/prefix and all11
literal headers. Later caller cast corrections do not change those compiled prefix/header
bytes. Default maxErrors was never raised.

## Immutable FIRST, entire semantic scaffold and actual built values

FirstIndependent.lean starts with ENTIRE exact immutable FIRST batch2 bytes (import,
namespace, before/after declarations, original proof, no added section/omit/universe/class).
The explicit old eleven-binder adapter derives initial positive weight from the original
antitone certificate/final3 bound and derives positive log from the numerical threshold.
The independent FIRST value is checked against actual-target/adapter/expected-current
self dependency. The old proof does not merely call the current helper.

The adapter/actual-current/independent-current opaque values use value!true; inferred types
and standard axioms checked. Exact full FIRST11↔adapter11 and expected7↔actual7 telescope
metadata/types/conclusions pass. Original↔actual retained names/order/BinderInfo/universes
and all unchanged binder types/conclusion pass, with four explicit removals and two joint
original-context-supported weaker premises. Natural weight1 and denominator2 strictness
examples compile. Actual phi/successor full FIRST/current telescope comparison passes;
all three actual consumers' opaque type/value/standard axioms/positive denominator
dependencies pass.

ActualSemanticsAugmented.lean retains the ENTIRE209-marker prior scaffold as an exact
byte prefix, then appends the complete FIRST batch2 namespace copy and new verifiers.
The independent exact-context FIRST file retains the original namespace; the combined
copy renames only that namespace and omits its already-loaded import. semantic-provenance.json
and immutable-complete-blocks.json verify inherited full prefix and all four full blocks:
Index72cf, Theta355a, ENTIRE original2b MainLemma proof and ENTIRE independent updated
MainLemma proof. Existing old Θ adapter/publicΘ9/scaled13/FIRST15/δ3/prefix18 with Antitone
adapter/base7 positivity API/both deleted wrappers remain intact. Main's complete26-binder
metadata/definitions/proof/standard axioms and positive actual main→RootΘ dependency
remain checked; independent original/current caller proofs do not use Root.main_lemma.
No imported current MainLemma is passed off as an independent proof.

The fresh successful logs contain42 clean FIRST markers and251 clean augmented markers
(209 inherited+42 new), with no PANIC/error/sorryAx/nonstandard axiom. Both actual affected
modules rebuild BEFORE Root value/axiom queries. All immutable FIRST texts and original
success log/status hashes remain unchanged (first-immutability-{before,final}.json).

## Fresh module/semantic/native gates

| Gate | Actual command/evidence | Result |
|---|---|---|
|build-theta-final|/Users/ramin/.elan/bin/lake build Roth.Theta; build-theta-final.json/.log|exit0, 4.800s|
|build-mainlemma-final|/Users/ramin/.elan/bin/lake build Roth.MainLemma; build-mainlemma-final.json/.log|exit0, 34.410s|
|first-independent-final|/Users/ramin/.elan/bin/lake env lean /private/tmp/theta35-denominators-fresh/FirstIndependent.lean; first-independent-final.json/.log|exit0, 50.459s|
|actual-semantics-final|/Users/ramin/.elan/bin/lake env lean /private/tmp/theta35-denominators-fresh/ActualSemanticsAugmented.lean; actual-semantics-final.json/.log|exit0, 125.493s|
|definition_protected|Exact source reconstruction|PASS, all def/abbrev/import/pin bytes unchanged|
|theorem_statement_protected|FIRST11 adapter and actual public contract checks|PASS with supported private generalisation; all public headers unchanged|
|structure_gate|line-counts.json|Target3, phi29, successor28, publicΘ15 noncomment proof lines; no >10 subproof|
|naming_gate|Descriptive denominators/one_lt/private _aux|PASS, no forbidden pattern|
|line_packing_gate|packing.json, all3 header lines|PASS|
|inequality_orientation_gate|inequalities.json, all4 occurrences|PASS|
|cumulative scoped consumers|Both builds, entire independent caller proofs, all affected values/axes, fresh natives|PASS|
|full project/separate LeanEval|Owner-only final frozen gates|PENDING; not claimed here|
|whole-file performance|Separate unrelated repair queue/MainLemma finite caller timing|NOT CLAIMED|

Fresh COMPLETE UNFILTERED diagnostics:

| Module | Success | Partial | Timed out | Errors | Warnings |
|---|---|---|---|---|---|
|theta|True|False|False|0|8|
|mainlemma|True|False|False|0|3|

Every warning is retained in raw native JSON and listed here; none is filtered:

|Module|Line|Severity|Message|
|---|---|---|---|
|theta|1|warning|* `-/`: Copyright too short!   Note: This linter can be disabled with `set_option linter.style.header false`|
|theta|93|warning|Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|theta|101|warning|Variable name `hB` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hB  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|theta|101|warning|Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|theta|109|warning|Variable name `hB` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hB  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|theta|129|warning|Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|theta|252|warning|Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|theta|547|warning|Variable name `hq` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hq  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|mainlemma|1|warning|* `-/`: Copyright too short!   Note: This linter can be disabled with `set_option linter.style.header false`|
|mainlemma|149|warning|Variable name `hδ0` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hδ0  Note: This linter can be disabled with `set_option linter.unusedVariables false`|
|mainlemma|149|warning|Variable name `hr₁` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr₁  Note: This linter can be disabled with `set_option linter.unusedVariables false`|

Three exploratory successor-call cast candidates failed; raw/status/source snapshots
selected-build-theta*, including -fixed/-explicit-fin, preserve them. An outer natural positivity
ascription or explicit Fin index did not resolve the inner cast metavariable. The selected
`(3 : ℝ) ≤ r 0` result ascription pins it and compiles; selected-build-theta-bound-typed.*
and final builds/semantics confirm this. No production limit/option/helper was added.

## Actual performance and drain

ALL own normal/native requests drain before each real profile; pre-final-{first,repeat}-drain.json
records dead process groups/pending[]. Command is lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Theta.lean, with external420s capture window and unchanged
Lean limits. Both complete actual whole51 captures have exit0, all51 actual declaration
anchors and strict UTF8 raw slices/byte offsets/hashes. Sum disjoint outer command plus
associated async proof/addDecl/linter rows; exclude nested macro/kernel duplication.
No diagnostic candidate timing stands in for production timing, no third same-source sample.

| Fresh run | Actual declaration | Conservative ms | Proof anchors |
|---|---|---|---|
|final-first|theta_denominators_one_lt_aux|111.594|1|
|final-first|theta_phi_lt_aux|733.339|1|
|final-first|theta_lt_succ_aux|919.777|1|
|final-first|Θ_lt|350.151|1|
|final-repeat|theta_denominators_one_lt_aux|110.493|1|
|final-repeat|theta_phi_lt_aux|811.469|1|
|final-repeat|theta_lt_succ_aux|968.310|1|
|final-repeat|Θ_lt|430.582|1|

Own denominator/phi/public Θ scoped budget acceptance follows the actual pair above.
Successor remains subject to its separate later dedicated audit; its historical
874.046/1373.393 failed pair stays preserved regardless of these checkpoint samples.
No original35 publication until every introduced-helper performance repair is resolved.
Unrelated whole-source failures in sum_max_sub_le_index_det, index_separated_mul_le_aux,
index_det_le, index_numeric_bound_aux/index29, index_le_lem6, lem7_Φ_bound, lem7_numeric
and the earlier positive-quadratic-helper1074.965ms belong to the owner final repair queue.
All fresh outside-scope over-budget rows remain in outside-scope-overbudget.json.
MainLemma's old180s cutoff before main_lemma remains unmeasured timing, despite semantic/
build/native success. This is never represented as finite timing or whole-file PASS.

## Simplify/refactoring/buzz and all11 steps

Simplify outcome: ISSUES-FOUND-AND-FIXED, performed directly because no builtin tool is
available. Direct positivity premises eliminate induction-only threshold computations;
inline terminal hLj; preserve meaningful comments and required cast ascription. No further
helper/refactoring recommended. Phase5a private generalisation is complete with FIRST
adapter; Phase5b has no rename/shared queue write. Buzz outcome is scoped FAST-BOARD
for owned denominator/phi/public Θ, with successor's dedicated audit and unrelated
whole-file queue explicitly outstanding. Zero limit raises/native_decide/scaffolding.

|Step|Result|
|---|---|
|1|✓ Required skills/workflow/references read|
|2|✓ All24 concrete audit dispositions|
|2.5|✓ Five actual methods,11 clean literal-current-prefix trials,positive absence compile|
|2.6|✓ Every11 FIRST/7 current binder probed; strictness,adapter,inversion/private exemption|
|2.7|✓ All3 signature lines measured/repacked|
|2.8|✓ All4 inequality occurrences measured|
|3|✓ All42 golf-rule dispositions|
|4|✓ Step-back/holistic simplify completed|
|5a|✓ Fresh complete unfiltered native diagnostics0errors|
|5b|✓ Actual module/entire semantics/type/value/axiom/scoped profiles/diff gates|
|6a|✓ No rename/shared queue mutation|

## Exact freeze and handoff

|Source|SHA256|
|---|---|
|Roth/Theta.lean|a5233643b514347d05747e03757a3a66590239ad91ac81fe57800e1531557095|
|Roth/MainLemma.lean|ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4|
|Roth/Main.lean|f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069|

Total source1009→1001 lines; target8→3 noncomment proof lines. One stale antitone comment
removed with the eliminated computation; no other comment/docstring changed. No helper
introduced/deleted; retained inventory51, original35 obligations remain11=9 retained+2
introduced/deleted. Counts215/264, Theta34/35 unchanged. No original-count credit/push/
publication by this leaf. Every FIRST hash/pin unchanged; all four complete immutable
semantic blocks retained.

Source edit authority is explicitly revoked at this freeze. All own compiler/native
requests are drained with pending[]; final-process-drain.json/final-freeze.json record
exact hashes and release. Scratch/report/compiler/native authority is also released at
terminal handoff. Owner still owes remaining fresh audits, cumulative29/allactual values/
axioms/final profile repairs/full lake build THEN separate frozen Roth.LeanEval before
ANY original35 publication. This report claims only the denominator-helper checkpoint.
