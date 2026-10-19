# SECOND performance repair: `Roth.sum_max_sub_le_index_det`

Proof-only original27 revisit; adds zero originals. Counts remain216/264, Theta35/35,
completed files9/14. This fresh worker owns only the scoped proof, scratch and this report;
no Git/shared-log/rename queue or unrelated source mutation. Public hq, Θ hB/hr, wrappers,
domains, header and every prior helper/FIRST/deletion audit stay protected.

Baseline HEAD/origin `29cb2f02579fbaa8afba4c4ac3c8ad817c91cbb8`;
preceding source/audit commit `3f4ab498398f79e9bad037de6df98b0ee5abfa2d`.
Baseline Theta SHA `3f9c23b83cd5bb8eaf9deb2b6d8c9182d0309464c5c76a3568c30eb1f86100ce`.
Owner inherited full build79.459s THEN separate LeanEval49.955s passed on all17 pins;
these are inherited gates, not this worker's final owner gates. Baseline complete native
source-bound diagnostics: `/private/tmp/theta-prefix-second-performance/native-*-final.json`,
Theta8/MainLemma3 warnings, zero errors, success=true, partial=false, timed_out=false.
Cache not needed; classic Lean dialect. All artifacts below use
`/private/tmp/theta-summax-second-performance/` unless an absolute path is given.

## Actual diagnosis and concrete repair

All24 supplied actual whole-Theta captures are independently rehashed, source/table bound,
strict UTF8 decoded and checked against their exact byte-offset slices and disjoint row sums
in `preserved-all24-history.json`. All24 raw/source/table/slice inputs remain untouched.
There are18 failed historical rows and6 passing observations; source differences are explicit.
A later unchanged-source pass does not erase a failure. Trigger ff964249 first1004.335/repeat809.108,
latest numeric first1131.027/repeat1065.136, previous first-repair948.179/914.928, and incidental
preceding prefix925.496/981.728 are all retained. No historical result is relabeled fresh.

The failed numeric trace has nested constant-sum `hlδ`225.887ms (simp221ms) and final sum192.181ms
(expected-type181.377ms); ff964249 likewise has hlδ197.790ms and final153.177ms. These overlapping
nodes diagnose the repair and are NEVER added to a disjoint declaration total.
Native LeanSearch found generic `Fin.sum_const`; pinned compilation verifies its generated
additive API. The proof now rewrites `[Fin.sum_const, nsmul_eq_mul]` directly, removing broad simp.
A typed `hentry` shares the product-entry nonzero certificate between index_prod and the final
summand bound. The first E-typed candidate fails syntactic rw matching against Matrix.of E;
its exact source/raw/status remain as `failed-E-entry-*` and `candidate.*`. Correcting hentry to
Matrix.of E compiles in `candidate-matrix-entry.*` before production application. No failed
candidate is positive proof evidence. Existing scalar-invariance and subtraction-order proofs
remain unchanged. New local certificates are not added declarations/helpers.

Deterministic exact-prefix measurements at unchanged default200000:
**3263 →2581 heartbeats,20.90% fewer** (`Heartbeats-before/after.lean`, logs/status).
Production proof27→28 lines, declaration35→36, no branch/subproof>10.

| Eight-cause taxonomy | Fresh trace assessment/action |
|---|---|
|1 instance synthesis|No dominant instance-synthesis node established; no instance workaround.|
|2 fat simp|Confirmed225.887ms constant-sum node; replaced by direct generic rewrite.|
|3 unification/defeq|Final expected-type181.377ms diagnosed; shared explicitly Matrix.of-typed entry certificate, with initial E-only failure preserved.|
|4 heavy automation|Prior direct subtraction transport retained; no new heavy production tactic.|
|5 metavariable churn|Entry certificate pins the matrix-entry family before index_prod and final sum; no independent unproved mvar root claim.|
|6 coercion churn|Finite sum nsmul→real multiplication crossed once; prior integer-sign map bridge retained.|
|7 duplicated subterms|Repeated entry-nonzero derivation shared locally; E remains a single local derivative-matrix definition.|
|8 kernel/compiler|All final disjoint addDecl/kernel/compiler/linter rows counted; nested kernel/macros never added twice.|

Scope includes actual target and entire unchanged direct index29 caller. Θ_option_le is also
inventoried as a transitive observation. Other declarations remain outside this repair.

## Fresh24 audit

|#|Item|Assessment/action|
|---|---|---|
|1|LINT|No target warnings in inherited complete diagnostics on exact release source; final fresh native whole-file gates retain all warnings.|
|2|HAVE SCAN|hterm: substantive 9-line derivative estimate. h1: rewritten before use. h2: used twice. hprod: typed product nonzero boundary feeding hentry, retained to pin the Matrix.of product before entry extraction. hentry: typed certificate reused twice. hidx: scalar index normalization. hlδ: finite-sum identity, now direct rewrite. No new constant.|
|3|SET_OPTION|No production options or profiling scaffolding.|
|4|SIMP SQUEEZE|The costly terminal constant-sum simp is replaced by direct rw [Fin.sum_const, nsmul_eq_mul]. Existing simpa only [map_intCast] is the preserved previously measured scalar-normalization exception.|
|5|NAMING|sum_max_sub_le_index_det describes the sum/max/subtraction determinant-index inequality, snake_case, no forbidden abbreviation or scheme. No rename. Index rename remains owner project-end work.|
|6|LINE PACKING|All eight signature lines measured in packing.json and table below; byte-identical to release.|
|7|BY PLACEMENT|Every by remains at end of its declaration/assignment line.|
|8|FORMAT|Two-space indentation; 100-character maximum; no empty proof line, semicolon, haveI/letI or new global setting.|
|9|COMMENTS|Protected source docstring and attribution preserved byte-for-byte; no original proof comment removed.|
|10|DOCSTRING|Existing mathematical determinant and loss description retained.|
|11|VISIBILITY|Public contract retained; publication visibility is not reopened during this performance revisit.|
|12|STRUCTURE|28 lines after := by (27 before), ordinary proof cap30; hterm9 lines, hidx4 lines, hlδ1 line. No branch/subproof>10, no new helper.|
|13|MATHLIB|All five actual methods performed; native remote methods succeed. Fin.sum_const is directly reused. Anonymous exact-current-prefix whole-goal probes do not establish an equivalent closer; no global absence claim.|
|14|JUNK DEF|Not a def; local set E names the repeated derivative matrix and avoids duplicated elaboration.|
|15|EXISTS LEMMA|No existential lemma or witness duplication.|
|16|SHOW vs CHANGE|Neither occurs in changed production proof.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All12 effective binders receive fresh located drop probes; strict→weak hr fails; full family-weight and uniform-degree variants compile. Inversion/literature assessment below.|
|19|INEQUALITY|All five statement inequalities oriented ≤/<; scan below.|
|20|NORMAL-FORM|Concrete range/max sum is the source and caller normal form. Existing scalar-index and subtraction transport remain, generic Fin constant-sum API now used directly.|
|21|SYNTAX-GEN|Current caller directly supplies D/hD/hdet/hr/global hδ; replacing hD/hδ with family-local weights would move useful routine specialization into that caller. No recommended contract change.|
|22|IMPORT-FANOUT|No new imports or file-level changes.|
|23|CASTS|No cast removed: Fin→Nat, Nat→Real, unit→Int→polynomial and the scalar bridge are genuine cross-type/load-bearing. No new redundant explicit cast in the diff.|
|24|INSTANCE-NAME|No instance declaration added or named; DecidableEq τ remains omitted as previously approved.|

## Five actual searches; clean automation

|Method|Fresh result/evidence|
|---|---|
|A Lean-Finder|Weighted-index/Hasse determinant query SUCCEEDS; unrelated determinant absolute-value/degree results, no target replacement. `native-search-finder.json`.|
|B Loogle|Finset.sum_const SUCCEEDS, generic finite constant-sum statement. Additional Matrix.det inequality pattern succeeds with unrelated degree/Cartan/charpoly results, no target closer. `native-search-loogle.json` and `native-search-loogle-whole-goal.json`.|
|C LeanSearch|Finite Fin constant sum query SUCCEEDS; supplies Fin.sum_const, used directly. `native-search-search.json`.|
|D Full source/name|Untruncated source scans `mathlib-full-name.log` and `mathlib-source.log` plus Index/project/Finset/order APIs inspected.|
|E Local name|sum_const returns source matches, index unavailable, so no index-absence claim. `native-search-local.json`.|

Auxiliary variants: sum_const/Fin.sum_const/card_univ/nsmul_eq_mul, sum_sub_distrib,
prod_ne_zero_iff, index_C_mul/map_intCast, sub_le_sub_left/sub_right_comm.
Remote indexes use their exposed mathlib snapshot (Finder4.28 default); actual pinned Lean4.34 compilation verifies every adopted API. No discrete/topological common-equivalents bucket matches. Partial mathlib match adopted
at the use site; no wrapper is added. Five methods support presence, not global absence.
`PrefixAbsence.lean` compiles separately (exit0), contains the exact current source prefix
BEFORE target (no self-import), positively checks preceding min_le_sum_max and checks
qualified target/index29 absence. #check verifies Fin.sum_const/nsmul_eq_mul and prior bridges.
`Automation.lean` uses five anonymous literal-header examples at that exact prefix;
grind/aesop/simp_all/exact? fail at located goals. apply? emits partial generic subtraction/order
suggestions then the10,000-heartbeat bound appears at file1:1 (outside its literal source range);
this is honestly retained as global final search timeout, not a falsely localized proof error.
All five ranges/raw diagnostics preserved; no maxErrors raise, named failed theorem or imported
target contaminates search. Negative batch exit1 is never positive absence/axiom evidence.
Known repeated native full-Theta multi_attempt stalls are respected; bounded direct compiler
probes are used for literal-goal exploration. Final native diagnostics remain mandatory.
LocalAutomation freshly tests positivity/lia/gcongr/norm_cast/subtraction transport: positivity
and degree-lia fail; finite-sum gcongr, scalar norm_cast and direct order examples have no errors.

## Every effective binder; generality, literature and inversion

Four separate negative batches use autoImplicit=false, each binder has actual located errors
in binders0–3-results.json. Structural dependency failures do not claim mathematical necessity.
Every one of12 effective parameters is accounted for; no σ classes/DecidableEq τ/hR are present
in the current telescope. Their earlier approved removals are preserved by exact old adapters.

|Binder/class|Fresh drop/weakening result and decision|
|---|---|
|τ:Type* / type|Already universe polymorphic; absent type produces Missingτ error; structural dependency.|
|Fintype τ / class|Omission fails referenced section instance, since index requires finite variable type. Finite-only restatement requires choosing the same finite structure; no domain redesign recommended.|
|R / value|Unknown R errors in dependent statement/proof; arbitrary real-polynomial domain retained.|
|l / value|Unknown l in Fin/matrix/sum; changing to abstract finite columns changes enumeration, no recommended API churn.|
|D / family|Unknown D; correlated differentiation witness remains shared.|
|hD / proposition|Drop fails actual hD use; uniform-degree<l complete variant freshly compiles. No change recommended: caller supplies degree≤μ.|
|hdet / proposition|Drop fails actual determinant nonzero use; zero index convention prevents inferring the same lower bound from mere nonnegativity.|
|α / point|Unknown α in all indices; no continuity/point-localization class applies.|
|r / weights|Unknown r in dependent index/weight types; natural weights retained.|
|hr / proposition|Drop fails index_prod; WeakHr strict→weak variant fails expected ∀j,0<r j at actual index_prod application.|
|δ / value|Unknown δ in bound/conclusion; arbitrary real loss retained.|
|hδ / proposition|Syntactically correct drop fails actual hδ use; complete family-local weight variant freshly compiles and removes hD.|

`Generality.lean` is a separate exit0 positive file for both complete variants, not a negative
batch. Family-local weight and uniform-degree alternatives were assessed and are not recommended
for this repair; the entire current caller already constructs the degree/global-weight interface.
The real coefficient-field/index API cannot mechanically weaken ℝ to an abstract field without
redesigning index; no false one-binder generalization is claimed. No API recommendation is pending.

Fresh two literature queries and primary PDF opens are retained in literature-results.json and
literature-primary-opened.json. [Min Ru's notes](https://www.math.uh.edu/~minru/fields/roth.pdf)
p.3 state the same index product/addition principles; [Princeton notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf)
are a canonical index-formulation source, without supporting a stronger claim here. Local primary
clean.tex815–840 gives the precise derivative determinant-loss bound. ChatGPT math MCP is not
available, so no external second opinion is claimed. No literature finding forces an API change.
The inversion diagnostic fires in the suffix after hterm: arbitrary matrix and column bounds
suffice for determinant summation. Fresh Inversion.lean compiles the complete abstract proof.
This is a valid abstraction option, not a user veto or an impossible generalization; introducing
another one-use API/helper does not remove the derivative estimate and is not recommended.

## Packing/inequality measurements

All8 signature lines are byte-identical. Unicode codepoint widths (not bytes), next complete
legal group and exact arithmetic are retained in packing.json; #check/type output uses width100.

|Line|Width|Next width|Arithmetic|Action|
|---|---:|---:|---|---|
|371|95|28|95+1+28=124>100|ok|
|372|69|75|69+1+75=145>100|ok|
|373|100|18|100+1+18=119>100|ok|
|374|50|63|50+1+63=114>100|ok|
|375|69|64|69+1+64=134>100|ok|
|376|68|34|68+1+34=103>100|ok|
|377|40|80|40+1+80=121>100|ok|
|378|88|—|final signature line|ok|

|Occurrence|Orientation|Action|
|---|---|---|
|hD|degree≤μ|retain|
|hr|0<r j|retain|
|hδ premise|degree≤l−1|retain|
|hδ result|weight≤δ|retain|
|conclusion|sum−lδ≤index(det)|retain|
|reversed code tokens|no≥/> in signature|no rewrite/rename|

## All42 golfing rules

|Rule|Fresh assessment|
|---|---|
|1.1|No by-exact wrapper.|
|1.2|No by-rfl wrapper.|
|1.3|No rw then exact on the same closing fact; h1 rewrites precede the h2/max estimate.|
|1.4|Scalar normalization uses simpa using directly.|
|1.5|No trailing rfl.|
|1.6|No constructor.|
|1.7|Direct exact/refine used.|
|1.8|No contradiction.|
|1.9|Dependent membership lambdas cannot eta-reduce; no trivial lambda wrapper.|
|1.10|hentry reused twice. h2 reused twice; h1 rewritten; hprod retained as typed product boundary feeding the entry certificate. hidx/hlδ carry normalization proofs, hterm carries the derivative estimate. No new trivial global helper.|
|1.11|le_index_sum uses refine with a function.|
|1.12|No redundant show.|
|1.13|Nonzero product gives an entry-indexed family, not a fixed conjunction destructuring.|
|1.14|Final hlδ/sum-subtraction rewrites merged already; h1 rewrites target a different location from goal rewrites.|
|1.15|Broad terminal constant-sum simp removed using direct Fin.sum_const/nsmul_eq_mul rewrite, rather than squeezing. Preserved scalar simpa-only is an inherited measured exception.|
|1.16|No nonterminal bare simp.|
|1.17|Order transport uses .trans and standard projection forms.|
|1.18|No trailing by block or parenthesized lambda improved by <|.|
|1.19|No push_neg.|
|1.20|No existential helper.|
|2.1|Fresh anonymous whole-goal grind fails; raw log retained.|
|2.2|Whole-goal grind already deletes all setup; no production grind.|
|2.3|Scalar simpa consolidation retained. Fin.sum_const eliminates the old broad simp entirely.|
|2.4|No analytic function predicate, not applicable to algebraic Hasse derivatives.|
|2.5|Fresh local nonnegativity positivity trial recorded; direct add_nonneg remains controlled.|
|2.6|Fresh finite-sum gcongr probe recorded; sum_le_sum is direct and expected-type-guided.|
|2.7|Fresh degree lia probe recorded; current Nat.le_sub_one_of_lt term avoids proof search.|
|2.8|Fresh anonymous whole-goal aesop fails.|
|2.9|Fresh scalar cast norm_cast probe recorded; selected Int.cast_ne_zero is direct.|
|2.10|Arbitrary polynomial inequality is not closed decidable computation; no decide/native_decide.|
|2.11|No denominator identity goal; no field_simp/ring endpoint.|
|2.12|No ring/ring_nf endpoint; preserved direct subtraction-order transport avoids arithmetic search.|
|2.13|No symmetric substantive branches remain after the first repair; no wlog opportunity.|
|2.14|No two-step calc; direct transitivity used.|
|2.15|No repeated goals remain after removing sign case split.|
|3.1|Only rw, no erw.|
|3.2|No legacy continuity/measurability.|
|3.3|No omega; local integer arithmetic probe uses lia.|
|3.4|No rcases-equality pattern remains.|
|3.5|Specialized determinant derivative estimate does not need global simp/grind registration.|
|3.6|Fresh anonymous simp_all whole-goal fails; no production simp_all.|
|3.7|No limit raises present or introduced.|

## Step back and simplify

The proof separates the derivative-entry estimate from determinant expansion/product addition.
Current scalar API and direct subtraction transport remain clear; generic Fin.sum_const removes
broad normalization and shared typed entry evidence removes duplicated elaboration. No global
wrapper or API is added to hide timing. All original comments/docstrings remain exact.
Built-in simplify callable is unavailable; its reuse/clarity/efficiency review is executed
directly. Outcome ISSUES-FOUND-AND-FIXED for these two local costs, then PASS-THROUGH at freeze.
Phase3 file-level changes none; Phase5a no cross-declaration changes; Phase5b no rename/queue
writes. Owner final independent file review remains a distinct responsibility.


## Fresh frozen validation gates

All normal compiler/build requests finish before native diagnostics, and all native requests
return complete before the actual trace. `pre-profile-drain.json`/`pre-repeat-drain.json`
(where required) and `final-process-drain.json` record every normal PID/process-group dead and
ordinary/native pending[]. Native JSON is complete and unfiltered: only file_path was supplied.
No production source edit follows static freeze; all17 final source/pin hashes stay exact.

|Gate|Fresh evidence/result|
|---|---|
|lake build Roth.Theta|exit0,15.947s,0 PASS markers; `build-theta-final.log/.json`.|
|lake build Roth.MainLemma|exit0,25.181s,0 PASS markers; `build-mainlemma-final.log/.json`.|
|independent full original27/current target and entire current index29 proof|exit0,20.637s,40 PASS markers; `independent-final.log/.json`.|
|cumulative actual RootTheta/MainLemma/all29 recovery/five definition values/all FIRST checks|exit0,246.114s,727 PASS markers; `actual-semantics-final.log/.json`.|
|Native theta|success=true,partial=false,timed_out=false,failed_dependencies=[],0errors,8warnings; `native-theta-final.json`.|
|Native mainlemma|success=true,partial=false,timed_out=false,failed_dependencies=[],0errors,3warnings; `native-mainlemma-final.json`.|
|definition_protected|PASS: no def/abbrev/import/file-header edits.|
|theorem_statement_protected|PASS: exact current public contract/docstring; entire direct index29 caller including hq and suffix byte-identical.|
|structure/naming/packing/inequality|PASS:28-line proof,subproof max9,no new helper,descriptive snake_case,all8 signature rows measured≤100,all5 inequalities≤/<.|
|new identifier|Fin.sum_const/nsmul_eq_mul independently #checked in successful pre-target absence file and compiled in selected proof; native search presence, pinned compilation authoritative.|
|trust/hygiene|No sorry/new axiom/native_decide/limit raises/production profiling scaffolding. All actual/independent opaque values use value! true, clean logs, standard axioms only propext/Classical.choice/Quot.sound.|
|scope cumulative|Build/native/full actual semantics pass for Theta and MainLemma; final owner full-project THEN separate LeanEval gates remain pending after this terminal revocation.|

The fresh independent namespace contains the full exact original27 proof in its original
context, not a call to the actual target. The original proof fragment and context hashes
below match immutable supplied evidence. Current independent target and entire direct caller
are re-elaborated from the full current preceding source in a new namespace; full universes,
effective binder types/order/names/BinderInfo/conclusion and opaque value! true types are
checked against actual rebuilt constants. Nonself checks and positive target dependency for
both independent and actual direct caller succeed. Exact old full-contract adapters in the
refreshed all29 recovery scaffold preserve the previously approved DecidableEq/hR removals.
No new API/visibility/helper retention change or inverse recovery edit is made.

The prior scaffold contains **687 PASS checks and591,288 bytes**. All591,288 bytes are an
identical prefix of the new727-check scaffold, with SHA
`2fd3699cd13d7ed3374f6bea933ca3c2ad45045b3e718fb6e0ee7172bc517dae`.
All687 marker categories recur in the fresh log; all four complete canonical original/current
proof blocks stay byte-identical. This includes complete original Index/Theta proof recovery,
whole original2b MainLemma and independent current MainLemma proofs, and refreshed actual
RootTheta/MainLemma type/value/stdaxiom/dependency checks. Negative exploration logs do not
certify any of these successful properties.

Remaining native warnings are preserved, never suppressed: Theta header; retained hr/hB
at93,101,109,129,252; deliberate hq at555. MainLemma header and retained hδ0/hr₁ at149.
Technical hr recommendations for index_le_Θ/Θ_unique_le remain the separate final reviewer's
assessment; this performance repair does not turn private retention choices into a user veto.

## Real uncontended actual whole-Theta profiles

Exact command (420s external capture, no Lean limit changes):

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean
```

Each final capture exits0 with complete source declaration inventory50/50, actual theorem
proof anchors exactly1, strict UTF8/no literal replacement sequences, source SHA bound to
final-Theta.lean. Table rows select the anchored OUTER command plus associated disjoint async
proof/addDecl/compiler/linter rows. Nested wrappers/macros/kernel children are included only
through their parent and never added twice. Complete raw logs/status/table and exact slices,
UTF8 byte offsets/hashes and all failing/new-actionable rows are preserved. This is scoped
acceptance evidence, not a whole-file timing PASS.

|Run|Declaration|Outer+associated disjoint total(ms)|Disjoint rows(ms)|
|---|---|---:|---|
|final-first|sum_max_sub_le_index_det|**900.517**|Elab.command=114.154; Elab.async=702.286; Elab.async=25.010; Elab.async=59.067|
|final-first|index_le_lem6|**659.696**|Elab.command=60.025; Elab.async=517.489; Elab.async=37.424; Elab.async=44.758|
|final-first|Θ_option_le|**184.508**|Elab.command=90.971; Elab.async=0.352; Elab.async=0.823; Elab.async=65.518; Elab.async=5.156; Elab.async=21.688|
|final-repeat|sum_max_sub_le_index_det|**748.233**|Elab.command=134.825; Elab.async=495.368; Elab.async=21.041; Elab.async=96.999|
|final-repeat|index_le_lem6|**552.163**|Elab.command=45.435; Elab.async=443.168; Elab.async=17.551; Elab.async=46.009|
|final-repeat|Θ_option_le|**217.591**|Elab.command=117.640; Elab.async=0.144; Elab.async=2.585; Elab.async=48.928; Elab.async=3.317; Elab.async=44.977|

Fresh nested diagnostics are overlapping/nonadditive and excluded from totals:

|Run|constant-sum step(ms)|final sum step(ms)|entry certificate(ms)|
|---|---:|---:|---:|
|final-first|14.597|143.579|44.909|
|final-repeat|10.359|84.963|49.774|

The historical failed numeric source has constant-sum225.887ms/final sum192.181ms; exact source differences and trace hashes remain explicit in the history inventory. These diagnostic comparisons do not substitute for complete final disjoint totals.

Separate mandatory actionable unrelated failure observations (a later passing unchanged-source observation never erases an earlier failure):

- final-first: `mapped_det_ne_zero_aux` **1049.976ms**, exact preserved strict slice `/private/tmp/theta-summax-second-performance/final-first-failure-mapped_det_ne_zero_aux-strict-slice.log`.

First owned target/direct scope reached750ms, so exactly one same-final-source repeat was required and performed; both owned rows pass<1000ms on both samples. No third unchanged-source capture.
Every earlier failed observation remains actionable historical evidence; passing rows are
not cherry-picked to erase it. The substantive source repair and heartbeat reduction give
concrete improvement, rather than a threshold waiver. Buzz outcome FIXED for this owned
repair, not whole-file FAST-BOARD. No maxHeartbeats raise removed/added(0/0), no timing-helper
extraction. All unrelated current≥1000ms rows, if present, are preserved as separate actionable
queue entries in profile-*-remaining-queue.json and strict failure slices; previously known
historical failures remain preserved with their repair history. Owner final cumulative/allactual
sweeps and independent filewide review still remain. MainLemma's actual main_lemma caller trace
remains unmeasured after its earlier bounded cutoff before main_lemma; ordinary semantics,
module build and native success do not substitute for that missing actual caller timing.

## Full source/proof/pin/FIRST hashes and artifact map

Paths below are concrete in the scratch directory. `evidence-manifest.json` lists every file
with exact SHA256 and byte size (including all failed exploration and history slices), and
final-freeze.json pins this report plus manifest. The24 original raw/source/table paths and
full hashes live in preserved-all24-history.json; all observations and source differences remain.
`complete-all26-target-history.json` appends exactly the two fresh accepted target observations to all24 supplied observations, preserving all18 historical failures (26 total,8 passing observations).
Protected current prior Theta reports (including the latest owner-clarified SECOND prefix
report) are individually hashed in protected-report-hashes.json and unchanged.

|Artifact group|Concrete files|
|---|---|
|Source/focused diff|baseline-Theta.lean,final-Theta.lean,original-declaration.lean,candidate-declaration.lean,owned-proof.diff,static-gates.json,packing.json|
|Original/full independent semantics|original27-proof-fragment.lean,independent-original-context.lean,Independent.lean,independent-final.log/.json|
|Cumulative semantics|ActualSemanticsAugmented.lean,actual-semantics-final.log/.json,semantic-marker-summary-final.json,immutable-scaffold-and-blocks.json|
|Immutable source/FIRST/reports|all-source-pin-hashes.json,source-hashes.json,all-FIRST-immutable-hashes.json,protected-report-hashes.json,complete-source-proof-hash-map.json|
|Candidate failure/success|failed-E-entry-Candidate.lean,failed-E-entry-declaration.lean,candidate.log/.json,candidate-matrix-entry.log/.json,Candidate.lean|
|Fresh audit/search/probes|native-search-*.json,mathlib-*.log/.json,literature-*.json,PrefixAbsence.lean,Automation.lean,automation-ranges/results.json,Binders0–3.lean,binders0–3-ranges/results.json,Generality.lean,Inversion.lean,WeakHr.lean,LocalAutomation.lean,Heartbeats-before/after.lean,all associated raw log/status/PID JSON|
|Complete native/build|native-theta-final.json,native-mainlemma-final.json,native-final-source-binding.json,build-theta-final.log/.json,build-mainlemma-final.log/.json|
|Actual profiles|actual-profile-final-first.log/.json/-table.json,profile-final-first-strict-slices.json,final-first-*-strict-slice.log; corresponding final-repeat files only if required|
|Failing rows/history|preserved-all24-history.json,complete-all26-target-history.json,history-00-strict-slice.log through history-23-strict-slice.log,profile-final-*-all-failures-strict-slices.json,profile-final-*-remaining-queue.json,profile-final-*-new-actionable-strict-slices.json|
|Drain/freeze|pre-profile-drain.json,(pre-repeat-drain.json if required),final-process-drain.json,final-freeze.json,evidence-manifest.json|

All hashes below are full SHA256:

```json
{
  "source_sha256": "2a41e042e8a363fd01a5038dadd04e3ddbd5d6e9ff57d788aa418e389ff7cd52",
  "entire_direct_caller_sha256": "f8801fce3bbf5f0a4b5bbe536870aa0da4f023eb1dbc9f05b61dea982333f5e6",
  "entire_direct_caller_byte_identical": true,
  "target_sha256": "7615bf7a4ec641d6ef05f94661216d6aeb7f5d726bcbc57991b91ccb8589c9fb",
  "original27_exact_fragment_sha256": "8a46309c2c64878e7008e77f90525c8b611b891c24fd44b0881dbfeb77a68a9f",
  "original27_actual_original_context_sha256": "6d5dfb09741217a2d7f6d0408d36777bff3b262dcfea00110c2e46da5ea23b4b",
  "no_new_helper": true,
  "all_static_decisions_finished": true,
  "cumulative_scaffold_sha256": "43d17f09c0e5535f820025fc8e922442773c1449cd18ed34cc19cf793751212a",
  "independent_scaffold_sha256": "c4174b21a9b1f61b74abc66192e7590b3db1890f5df96050e05de7fc3ac78373",
  "all17_final_hashes": {
    "Roth.lean": "6aaa74aab715cb9b6df91771ec2e7e127a39807f936e26a68fcdc026099914d2",
    "Roth/Box.lean": "a5d0da3d2d4ecfcb705d0c446294e393fcff048576e0bd23f67b70c06dadc827",
    "Roth/CoeffNorm.lean": "ee0b23cfee16cf674512a5c8f912a8030242e736db6e79fc1270be71675e67a9",
    "Roth/GenWronskian.lean": "5283b554baa1fcfce18f2298a0f5181cc58586f22b541dd2222745ef651b6e32",
    "Roth/HasseDeriv.lean": "de378f2d057787d9751044e53cace8ba8134c015d9401f503e57259ca09d0dba",
    "Roth/Index.lean": "30e6f151ddd2d9c344b9537d1bef87124e3f5814d2e58f3cba499a7e1ea6c939",
    "Roth/Lattice.lean": "a363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8",
    "Roth/LeanEval.lean": "e95c44ae19345ef1514a59ca5e8b182247e9a32aaf4b7d39f0ce57ae5ed27f56",
    "Roth/Main.lean": "f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069",
    "Roth/MainLemma.lean": "ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4",
    "Roth/Separation.lean": "df4193795f1618f8f5cdbd71869583fc45d20a0a45c21f4b5eaf5f824133f37a",
    "Roth/Taylor.lean": "31af75afd28f840ddee51978509ba63b28536aa84bba56dc047df2aa4b23fbdc",
    "Roth/Theta.lean": "2a41e042e8a363fd01a5038dadd04e3ddbd5d6e9ff57d788aa418e389ff7cd52",
    "Roth/Wronskian.lean": "b4f0c0db36bcbd81983f5a38c137dcefdf57bce18e12445e8241689a8abf888e",
    "lean-toolchain": "8733782dc070a99b312039cda424f601b80f3be6f6f512627da5ba25adc27632",
    "lake-manifest.json": "f3c041619f25b5f9013759113d877b6e510b91956b0d97b542fb3bae9b5f906e",
    "lakefile.toml": "6122f113a57760c6b0b9eb52d6f6aa0343efda1d3339534dd12db31d21788a5d"
  },
  "all16_FIRST_hashes": {
    "/private/tmp/theta35-audit/first-clean-helpers-batch2.lean": "8a7cb0fd8b366f0f251272bf6e9a16cfa2dc339b9147899b74f876d37c1b54a6",
    "/private/tmp/theta35-audit/helpers-fifth.log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "/private/tmp/theta35-audit/helpers-fifth.json": "32ade30842fdd9413e1f7e8bbf348fc2adcd57b2b702866ae4e15e72ff50cde2",
    "/private/tmp/theta35-audit/first-clean-helpers-batch1.lean": "0fbc16d1f06bbfe114d42a5c8f5fb2aee7263263b61ffc3dc8465bff941d1a54",
    "/private/tmp/theta35-audit/first-clean-helpers-batch3.lean": "a373382e41c4b79d5d50dcd375e43d630acfecb09ecfc989e56f23250a396700",
    "/private/tmp/theta35-audit/helpers-large-third.log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "/private/tmp/theta35-audit/helpers-large-third.json": "c7fb87b8a6a2843f705f8b2ce3908c905ea8e3101ac5b9004f77764e31f88de1",
    "/private/tmp/theta35-audit/helpers-second.log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "/private/tmp/theta35-audit/helpers-second.json": "797ee282e42ee2ae2b0c80c88899dc400ff1fc8f5cdd128538b115d679bc0e7a",
    "/private/tmp/roth-theta-quadratic-helper/new-helper-initial.lean": "bbfaa4824d09a1f10356cbeb795bfae23d296889f76a675a576bfaedcaa2225c",
    "/private/tmp/roth-theta-quadratic-helper/new-helper-first-introduction-full.lean": "7685f1536fd898cfe55e148154245193b37cb1c23bd642dd32bcea7429f265c5",
    "/private/tmp/roth-theta-quadratic-helper/new-initial-independent.lean": "464a44a93b4eb1c365d8f34d911e363850b61d9a40806588e30494c4945feff9",
    "/private/tmp/roth-theta-quadratic-helper/new-initial-independent.log": "2de42ddbba407bfa829991c0efbde5ed6659f36ffa1dd34178e9a6b600567ad7",
    "/private/tmp/roth-theta-index-det/index_separated_mul_le_aux-FIRST.lean": "82ea1dcd2a8ced63947dc92f7a43f06b3cf868156e85895cd843a16873a03c92",
    "/private/tmp/roth-theta-index-det/first-introduction-snapshot.lean": "42d60acc1b1b3d587ffe568e246cb9ba637ee0a6449a6a2b29d6f02249354ba4",
    "/private/tmp/roth-theta-index-det/new-helper-first-introduction.json": "764881453d4a7000fc30bab28471e058e9531676decd8b59d23650e35e974234"
  },
  "prior_scaffold_sha256": "2fd3699cd13d7ed3374f6bea933ca3c2ad45045b3e718fb6e0ee7172bc517dae",
  "prior_scaffold_byte_length": 591288,
  "prior_check_count": 687
}
```

Four whole canonical blocks (strict UTF8 raw byte offsets in the preserved scaffold):

```json
[
  {
    "sha256": "72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f",
    "raw_byte_start": 1414,
    "raw_byte_end": 15125,
    "verified": true
  },
  {
    "sha256": "355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da",
    "raw_byte_start": 16628,
    "raw_byte_end": 68797,
    "verified": true
  },
  {
    "kind": "whole-original-mainlemma-bytes.json",
    "sha256": "96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a",
    "raw_byte_start": 70475,
    "raw_byte_end": 105941,
    "verified": true
  },
  {
    "kind": "whole-updated-mainlemma-bytes.json",
    "sha256": "859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41",
    "raw_byte_start": 117380,
    "raw_byte_end": 152930,
    "verified": true
  }
]
```

## Eleven-step checklist and terminal ownership

- [✓]1 Full required references/workflow/profiling read; relevant style/naming consulted.
- [✓]2 All24 audit items and every have reviewed with concrete decisions.
- [✓]2.5 Five actual methods plus clean anonymous literal-prefix automation and separate positive absence/control.
- [✓]2.6 Every effective binder drop/weakening, literature and compiled inversion assessed.
- [✓]2.7 All8 signature rows measured with exact packing arithmetic.
- [✓]2.8 Every inequality occurrence scanned, no reversed code tokens.
- [✓]3 All42 golfing rules concretely assessed; applicable local automation actually tested.
- [✓]4 Step-back/simplify review complete; no recommended scoped change pending.
- [✓]5a Fresh complete unfiltered native Theta/MainLemma diagnostics, all warnings preserved.
- [✓]5b Fresh module builds, independent/cumulative full semantic/axiom gates, protected diff and actual profiles.
- [✓]6a No renames required; no shared queue/log/Git mutation.

No owned requests remain: ordinary/native pending[], every recorded own process/PID/group dead.
Terminally revoke **all source, scratch, report, compiler and native authority** from this worker.
No production or evidence/report edit follows final-freeze.json. Owner now owns final full
`lake build` THEN separate `lake build Roth.LeanEval` (p10), cumulative/allactual/filewide
review/publication checks, exact-path staging/commit/push/clean before the next source edit.
This report does not claim those future owner gates are done. Original counts remain216/264,
Theta35/35, completed files9/14 until file-final gates.


## Owner evidence review and scope clarification

The original frozen report is retained byte-for-byte at
`/private/tmp/theta-summax-second-performance/leaf-final-report-owner-input.md`, SHA256
`b9f14c50ea1a8ffda8fb6ca7ca4ae93e0200e7809d0356760b29f4a865a6f44e`.
The initial owner hash checker rejected the indirect freeze schema before starting owner builds;
this was a schema mismatch, not a Lean or source failure. The untouched leaf freeze and manifest
were represented by owner-normalized-freeze.json; all191 artifacts,17 source pins,16 FIRST pins
and four canonical blocks then verified successfully before the owner builds began.
`owner-checked.json` independently verifies the scoped proof diff, entire preceding687-check
scaffold prefix,40/727 successful semantic markers, complete native diagnostics, anonymous probes,
and all50 anchored disjoint profile totals plus strict UTF8 slices. Whole-goal apply? produced
partial suggestions followed by a global10000-heartbeat timeout at1:1 outside the example span:
this bounded attempt is inconclusive, never a successful proof or a located negative result.
The mapped helper's fresh failed1049.976ms observation remains mandatory despite its lower
829.583ms repeat. Its dedicated repair is next; no whole-file timing pass is claimed.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 70.803 s and 38.034 s.
Theta SHA256 `2a41e042e8a363fd01a5038dadd04e3ddbd5d6e9ff57d788aa418e389ff7cd52` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p10-full.log` and `/private/tmp/roth-theta-p10-leaneval.log`; machine record
`/private/tmp/roth-theta-p10-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 27 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
