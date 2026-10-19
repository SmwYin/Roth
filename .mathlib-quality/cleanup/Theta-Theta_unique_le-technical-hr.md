# Fresh original20 Θ_unique_le technical hr checkpoint

Scope: remove only public `Θ_unique_le.hr`, repair its two actual private call arguments, and
explicitly expose the base caller's already-required nonzero denominator evidence. No new original
credit: 216/264, Theta35/35, 9/14 files until owner file-final gates. User-selected dedicated fresh
worker; no Git/shared-log/rename-queue changes. MainLemma source remains byte-identical.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, together with Lean/mathlib-quality skills,
cleanup workflow, relevant style/naming and profiling/buzz references.

## Baseline / doctor

Inherited published checkpoint `73e260450bf91912548fef9130a46d5b0daf422f`, exact Theta SHA
`0afac9d3af66eb80eab0bc2d8aa9c50dd2f61d693ff0868663b274a550509763` and MainLemma SHA
`a002b02724dc9f4bcef52280bc96c736eb2fd9acbc06b5352c6eff55b94dd689`. The immediately preceding
owner full build (78.617s), then separate Eval (56.394s), and complete native baseline diagnostics
are inherited evidence, not fresh worker full-project gates. Cache fetch skipped: cached imports
available. Final worker module builds and complete live diagnostics are recorded below. The
source snapshots and all 17 source/pin baseline hashes are frozen in this artifact directory.

## Mathematical audit

For each allowed nonzero integer polynomial, the already audited private logarithmic bound
controls its single-variable index by the same quotient. `Θ_le_of_forall_index_le` lifts that
bound to the supremum. The private bound divides by a nonnegative natural weight; Lean's total
real division makes the zero case valid. The public positivity premise supplied no proof input.
Removing it admits `Θ B q (fun _ ↦ 0) ≤ 0` directly. The scaled caller still needs positive weights
for its `Θ_mono` premise, exponent sign, and final denominator. The base caller still needs
`hrlast` to identify the quotient with δ. Its `field_simp` now explicitly receives
`ne_of_gt (by exact_mod_cast hrlast : (0 : ℝ) < r 0)`.

## Full 24-item fresh audit

| # | Item | Finding/action |
|---|---|---|
|1|Lint|Old target hr warning eliminated. Six final Theta warnings remain, enumerated below; none on either edited caller.|
|2|Have scan|Target has no have declarations; no single-use binding to inline.|
|3|Options|No target/production options or resource raises.|
|4|Simp|One coefficient-normalization `simpa only`; unsqueezed alternative freshly fails at default maximum recursion depth, retained as negative evidence. Keep the exact successful two-lemma form.|
|5|Naming|`Θ_unique_le` states unique-variable upper bound; no forbidden abbreviation/numeric scheme; no rename.|
|6|Packing|Both signature lines measured below; conclusion treated as a signature expression token.|
|7|By|Term proof; inner `by simpa` is on its expression line.|
|8|Format|Two-space term indentation, no empty proof line, no haveI/letI, no tactic chain.|
|9|Comments|Every source comment/docstring byte-identical; no narrative deleted.|
|10|Docstring|Existing Lemma5/source description retained exactly.|
|11|Visibility|Protected public wrapper/domain choice; public Lemma5 retained.|
|12|Structure|Three proof-body lines, no ∧ result or branches; below headline 15/branch 10.|
|13|Mathlib|All five actual methods plus clean anonymous automation below; no replacement established.|
|14|Junk def|n/a theorem, no definition.|
|15|Exists lemma|n/a public inequality, no existential result.|
|16|Show/change|No show/change in target.|
|17|Push neg|No push_neg.|
|18|Generalise|hr drop compiled; every retained effective binder/drop and relevant weaker form tested below. No further public alteration.|
|19|Inequality|All three statement inequalities use ≤/<; exact occurrence table below.|
|20|Normal form|Already Θ upper bound by a log quotient, matching Lemma5.|
|21|Syntax generality|Dropping unused hr makes zero weights usable with the same statement; no extra wrapper needed.|
|22|Import fanout|n/a no new import.|
|23|Casts|No target proof cast change. Base caller's `(0 : ℝ)`/`: (0 : ℝ) < r 0` pin a real nonzero denominator while exact_mod_cast bridges Nat positivity.|
|24|Instance names|No introduced instance; retained anonymous Fintype/Unique binders, prior DecidableEq removal preserved.|

## Five actual searches and clean automation

`native-search-finder.json`: semantic Roth/index/logarithm query returned additive-combinatorial
Roth-number/Chevalley results, no applicable logarithmic index theorem. `native-search-loogle.json`:
`Polynomial.rootMultiplicity, Real.log` returned empty. `native-search-search.json`: natural-language
root-multiplicity/height query found Polynomial.rootMultiplicity machinery, not this supremum
bound. `mathlib-source.log`: untruncated source search for rootMultiplicity/log/Θ_unique/index_unique
found no exact replacement. `native-search-local.json`: rootMultiplicity name search returned
actual declaration paths, but index=unavailable; this is explicitly not a proof of indexed absence.
The selected private bound and public supremum API are already the established proof components;
no new wrapper/helper is introduced.

`Automation.lean` uses anonymous examples, the exact literal new header (only the declaration
keyword/name changed), and exact pre-target source context; no import of Roth.Theta, target,
failed named theorem, or later declaration contaminates search. Fresh bounded trials: grind,
aesop, simp, exact?, apply?, rfl, gcongr, positivity, norm_num, linarith. None completes; exact?/apply?
reach the local lowered2000-heartbeat budget. No unbounded multi_attempt repeated (documented
session tool limitation). `PrefixAbsence.lean` separately succeeds with qualified/public/private-
suffix absence of Θ_unique_le and both later callers/main_lemma, and three present controls.
`Candidate.lean`, `Positive.lean`, and full independent semantics succeed separately; expected-
failure files are never used as positive proof/absence/axiom evidence.

## Every effective binder and weakening

Actual old original telescope has10 binders; actual new has8, dropping historical DecidableEq
and this checkpoint's hr only. Exact ordinary names/order/BinderInfo, instance class/order,
universe parameters, conclusion and full original adapter are checked by Lean. Prior current
production has9 binders; only hr changes now. Anonymous instance generated names may renumber.

| Binder | Fresh drop/weakening result | Decision |
|---|---|---|
|σ : Type*|`omit σ` fails: referenced section variable; dependent domains require σ.|Retain universe-polymorphic domain.|
|Fintype σ|Drop and Finite weakening fail: cannot omit referenced instance used by Θ.|Retain exact finite setting.|
|Unique σ|Drop fails Inhabited/default obligations; weaker Inhabited and Inhabited+Subsingleton fail required Unique synthesis.|Retain exact class.|
|B|Drop fails unknown B with autoImplicit=false.|Retain bound parameter.|
|hB : 1 ≤ B|Drop fails missing hB; weakening to 0 ≤ B fails supremum API expected 1 ≤ B.|Retain exact nonemptiness bound.|
|q|Drop fails dependent q/default/log references.|Retain denominator function.|
|hq : 1 < q default|Drop fails missing hq; weakening to 0 < q default fails logarithmic private bound expected 1 < q default.|Retain exact strict log positivity.|
|r|Drop fails conclusion's dependent r references.|Retain weight function.|
|hr : 0 < r default|Fresh omitted and weak 0≤r forms compile; actual new AST has no hr.|Remove exactly selected binder.|
|DecidableEq σ|Already removed in preceding historical cleanup; actual new AST confirms absent.|Preserve previous approved drop.|

Negative `Binders.lean`/`Generality.lean` logs are bounded proof-contract probes, not claims that no
alternative mathematical formulation exists. `Positive.lean` freshly checks the generic
conditionally-complete-lattice supremum lifting route and omitted/weak hr proofs with standard
axioms. Fresh actual zeroWeights application is checked in the semantic gate.

Public literature search: local primary manuscript `.mathlib-quality/references/clean.tex`,
§5 lines645–700, explicitly assumes positive integral weights for its informal family and proves
Lemma5 through root multiplicity and leading coefficients. The original positive theorem remains
recoverable exactly. The zero case is a Lean total-division extension, not a claim that the source
paper changed its convention. Fresh web searches are archived; the first exact-title query found
no relevant primary result. A broader search found [Stanford lecture notes](https://math.stanford.edu/~ksound/TransNotes.pdf)
on Roth's index bound and [AMS text preview](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf)
on the one-variable multiplicity interpretation; neither supplies a broader replacement API.
No verbatim external text is incorporated.

Mandatory inversion check: the supremum abstraction is already `Θ_le_of_forall_index_le`, and
the polynomial abstraction is already `index_unique_le_log_div`. A generic `csSup_le` positive
probe is compiled; introducing another abstract/private helper would duplicate the existing API.
Real/Nat/Int domains and public wrappers remain protected; no new generalisation recommendation.

## Measured signature packing and inequality inventory

| Signature line | Codepoints | Next signature expression width | Arithmetic | Action |
|---|---|---|---|---|
|1|98|60|159|ok|
|2|64|0|n/a|last|

The conclusion is a60-codepoint signature expression;98+1+60=159>100. Splitting its application head from its arguments would not improve readability.

| Line | Column | Relation | Result |
|---|---|---|---|
|1|48|≤|canonical|
|1|73|<|canonical|
|2|13|≤|canonical|

## Full 42-rule golfing pass

| Rule | Fresh disposition |
|---|---|
|1.1 by exact|No by-exact wrapper; term proof already direct.|
|1.2 by rfl|No by-rfl.|
|1.3 rwa|No rw/exact sequence.|
|1.4 simpa|Coefficient normalization already one simpa using; selected form compiles.|
|1.5 simp/rfl|No redundant trailing rfl.|
|1.6 constructor|No constructor goals.|
|1.7 apply/exact|Already direct application.|
|1.8 contradiction|No by_contra.|
|1.9 eta|Lambda consumes membership/coprimality fields; cannot eta-reduce to same argument types.|
|1.10 have inline|No have.|
|1.11 refine/fun|Already term lambda; no apply/intro.|
|1.12 show|No show.|
|1.13 projections|RSet field projections feed different arguments directly; destructuring adds a tactic block.|
|1.14 rw merge|No rw.|
|1.15 terminal simp|Unsqueezed anonymous simpa alternative fails max recursion at default limit; retain working fixed normalization.|
|1.16 nonterminal simp|No nonterminal simp.|
|1.17 dot notation|hR.1/hR.2.2 use direct field projections.|
|1.18 parentheses|Required parentheses around by-normalization argument; removing would alter parse.|
|1.19 push Not|No push_neg.|
|1.20 existential inline|No existential helper.|
|2.1 grind|Fresh anonymous exact-goal trial fails under2000 budget.|
|2.2 grind subsumption|No preceding tactics to delete; whole trial unsuccessful.|
|2.3 simpa consolidation|Already a single local normalization; broad alternative fails recursion.|
|2.4 fun_prop|n/a inequality with no function-property goal.|
|2.5 positivity|Exact-goal trial rejects non-positivity goal.|
|2.6 gcongr|Exact-goal trial makes no progress.|
|2.7 lia/omega|n/a main goal is logarithmic real supremum bound, no linear Nat/Int chain.|
|2.8 aesop|Fresh anonymous exact-goal trial unsuccessful.|
|2.9 norm_num/norm_cast|Norm_num exact-goal trial leaves goal; no cast-only target block.|
|2.10 decide/kernel|n/a not a closed decidable finite computation.|
|2.11 field_simp/ring|n/a no target algebraic identity; base caller existing field_simp explicitly receives necessary evidence.|
|2.12 linear_combination|n/a no ring terminator or polynomial certificate in target.|
|2.13 wlog|n/a no symmetric branches.|
|2.14 calc|n/a proof already term composition, no calc.|
|2.15 <;>|n/a no similar unresolved goals.|
|3.1 erw/rw|No erw.|
|3.2 fun_prop legacy|No continuity/measurability tactic.|
|3.3 omega/lia|No target arithmetic tactic.|
|3.4 rcases/rfl|No rcases.|
|3.5 attributes|No new automatic rewrite/instance justified; none added.|
|3.6 simp_all|No simp_all; no local-hypothesis saturation needed.|
|3.7 options|No production option, limits or profiling scaffolding.|

Manual holistic simplify pass: PASS-THROUGH. The established abstraction pair already isolates
supremum lifting and polynomial logarithmic work. No callable built-in simplify tool is exposed;
manual review found no helper/duplication/decomposition action within this scoped checkpoint.
The compiled broad-simp failure confirms that the restricted coefficient rewrite is intentional.
The two private callers retain all original assumptions and mathematical bodies except routine
arity repair and explicit denominator evidence. No new helper needs a separate audit.

## Static scope and retained histories

`static.py` verifies entire production Theta against the exact compiled prospective candidate;
`Theta-scoped.diff` contains only the target header and the two routine callers. All 47 other source
declarations are byte-identical; target body and all source comments/docstrings/imports/definitions
are unchanged. MainLemma is byte-identical and its full 26-binder actual type/opaque value/proof
and all independently copied source bodies are freshly checked. `final-callers.json` has exactly
two production calls, both in Theta; no MainLemma direct target call exists. All 50 source Theta
declarations and all MainLemma declarations are inventoried.

`inherited-histories-hashes.json` preserves the historical97 external reference inventory,
proof-comment inventory, all 35 original/22 introduced-helper (18 retained, 4 deleted) audit histories,
original9 inverse/checker provenance and protected report map. `protected-report-hashes.json`
reflects the actual post-publication baseline bytes; inherited maps certify their own old freezes.
`all-FIRST-immutable-hashes.json` is freshly verified against every retained FIRST artifact.
Line count990→991: the public hr binder disappears, while explicit caller denominator evidence
adds one source line. No original-credit counter changes or unrelated rename/report writes.

## Eleven-step checklist

1. Current dispatch/preliminary/reference/context read; published baseline frozen.
2. All24 audit items resolved above.
3. All five fresh actual search methods executed, limitations explicit.
4. Every effective binder/drop/relevant weakening, generic+zero routes, literature and inversion checked.
5. Every signature line measured by codepoints.
6. Every target statement relation inventoried.
7. All42 golf rules resolved above, exact anonymous search files retained.
8. Holistic reflection completed; no new helper/API action needed.
9. Complete unfiltered final native Theta and MainLemma requests returned green.
10. Module builds, independent/current/original contracts, opaque/axioms, cumulative migration and actual profile gates below.
11. No rename needed; owner sidecars/Git/shared reports untouched.

## Fresh verification, cumulative migration and trust

All successful positive gates below have exit0, no timeout/PANIC/error/sorryAx, and drained child groups.

| Gate | Seconds | Result |
|---|---|---|
|candidate|35.657|exit0; 0 pass markers|
|candidate-full|51.794|exit0; 0 pass markers|
|prefixabsence|50.831|exit0; 7 pass markers|
|positive|32.411|exit0; 0 pass markers|
|build-theta-final|36.334|exit0; 0 pass markers|
|build-mainlemma-final|36.927|exit0; 0 pass markers|
|independent-final|76.945|exit0; 170 pass markers|
|actual-semantics-final|453.906|exit0; 1223 pass markers|

Commands are preserved verbatim in each `.json`/`.pid.json`: normal builds were
`/Users/ramin/.elan/bin/lake build Roth.Theta` THEN `... lake build Roth.MainLemma`; original/current
proof probes used `lake env lean` on the named frozen scratch files. These are worker module gates.
Owner's frozen full build THEN separate Eval/publication gates remain pending.

`Independent.lean` re-elaborates the entire immutable original Index+Theta context, the entire
prior current Theta, entire final Theta, and entire final MainLemma under distinct namespaces.
The immutable original20 proof is real proof source, not an application of actualRoot. The exact
original 10-binder adapter recovers all original instances/ordinary names/order/BinderInfo/universes
and conclusion. Current actual 8-binder Root is compared against independent full current proof;
removed hr and DecidableEq AST binders are absent. The actual generic zeroWeights application
uses the new production constant. Θ_unique_le's proof body remains byte-identical.

Both entire affected private callers are independently re-elaborated from exact prior and final
source; their full 13- and 7-binder contracts match actual Root exactly. Old/current/actual opaque
values are type-checked with `value! true`, only `propext`, `Classical.choice`, and `Quot.sound` axioms allowed, nonself assertions checked,
and each full caller has a positive dependency on its corresponding Θ_unique_le. The actual
and entire independently copied MainLemma have the same 26-binder type, valid opaque values,
standard axioms, no Root self/private aliasing, positive Θ_lt dependency, and no direct Θ_unique_le
call. Every copied MainLemma source declaration and generated value has its own successful
value/type/axiom/nonself check. Differences in compiler-generated auxiliary inventory are exact:

```json
{
  "independent_mainlemma_copied_count": 46,
  "cumulative_mainlemma_copied_count": 44,
  "independent_only": [
    "Roth.UniqueHrMain.eta._proof_1",
    "Roth.UniqueHrMain.lam._proof_1"
  ],
  "cumulative_only": [],
  "explanation": "Compiler-generated proof-sharing auxiliaries can be omitted in a richer cumulative environment; every source declaration remains checked; exact inventories differ only in listed ._proof_ names."
}
```

The full cumulative fresh run has 1,223 successful markers, preserving
all 1,055 preceding marker categories/counts under exactly the historical mapping recorded in
`migration-operations.json`; 168 fresh UNIQUE HR direct checks
are distinct from the retained historical checks. The original 29 full public old-contract
adapters and five definition values freshly pass. Full all29 aligned verifier copy supports BOTH
index_le_Θ.hr and Θ_unique_le.hr drops; `all29-generator.patch` documents the minimal owner patch,
while the owner's generator is untouched.

Migration operations retain old call arity in seven explicitly HISTORICAL namespaces outside
canonical blocks, add a historical old-current type adapter, retarget the preceding retained-hr
AST check to that old contract, and update the retained all29 selected-drop inventory. The
historical AST marker category maps exactly `TECHNICAL HR THETA_UNIQUE_HR RETAINED` →
`HISTORICAL COMPATIBILITY TECHNICAL HR THETA_UNIQUE_HR RETAINED`. Historical checks are never
presented as new actualRoot target checks. New actualRoot checks are the separate UNIQUE HR tail.

`inverse.py` deterministically reverses all operations to recover all 806,170 input bytes with SHA
`903f10bdf10c4be5508886910804af3ebca2f978f5eafbc5116ddef2f5ee8da7`, including every 1,055-check input
byte, not merely four blocks. Prior inverse/migration/checker to the earlier 806-check layer remain
untouched and hash-bound. `immutable-scaffold-and-blocks.json` gives exact current raw offsets and
hashes for four COMPLETE canonical blocks: OriginalIndex72cf, OriginalTheta355a,
original2bMainLemma96f1 and preceding-currentMainLemma859a. All four are byte-identical.

## Complete native diagnostics and all-warning exceptions

Final complete UNFILTERED native Theta/MainLemma requests both have success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors; full raw JSON is retained. Theta has 6
warnings: protected header at1, Θ_nonneg hB/hr at101, Θ_le_card hB at109, Θ_mono hr at129,
and explicitly protected index_le_lem6 hq at553. The prior target hr warning at252 is the only
removed production diagnostic; no added warning. MainLemma has 3 unchanged warnings: protected
header at1 and hδ0/hr₁ at149. No warning suppressions or header/preference changes.
Scratch historical source copies emit their original unused-section/hypothesis warnings and old
arithmetic-style text; raw logs are unfiltered and retain all warnings. Historical compatibility
wrappers also have unused hr binders intentionally, because their purpose is old-contract recovery.
Build replay warnings also retain protected headers in Box/HasseDeriv/CoeffNorm/Taylor/Index/
Wronskian/GenWronskian/Separation (and Lattice for MainLemma), plus pre-existing unused Fintype
reports at GenWronskian.exists_genWronskian_ne_zero:241 and Separation.exists_det_eq_mul:531.
The Theta build has 16 warnings including imports; MainLemma build has 20. Independent scratch has 29
warnings and cumulative scratch 120; all remain in the unfiltered logs and summary counts.
The authoritative production native outputs above distinguish those historical warnings from
current source diagnostics. Expected-failure automation/binder/generalisation/simp files retain
exit1 and do not certify any positive gate. Broad simp failed at the unchanged default recursion
limit; no resource limit was raised. A targeted sandbox ps inspection was denied; owned-process
drain uses exact recorded PID/process-group probes, never a claimed systemwide process scan.

## Actual anchored performance / scoped buzz

Fresh exact command after all other own compiler/native requests drained:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean
```

External 420s timeout only; no Lean resource-limit change. All 50 current source declarations
accurately inventoried. Raw logs and slices decode strict UTF8; each proof row has one actual
anchor and disjoint outer-command/async-proof/addDecl/linter/compiler accounting, with no nested
double count. Raw/slice hashes and byte offsets are in the frozen tables. Budget 1,000 ms.

| Declaration | Inherited baseline ms | Fresh first ms | Fresh repeat ms |
|---|---|---|---|
|Θ_unique_le|66.189|75.070|n/a|
|theta_scaled_unique_le_aux|652.177|519.579|n/a|
|theta_lt_base_aux|616.343|482.899|n/a|

No first own target/direct-caller sample reached 750 ms, so no worker repeat was warranted.

final-first: all-file ≥750ms observations []; ≥1000ms observations [].

Scoped buzz acceptance only: all fresh own target/direct-caller samples are under 1,000 ms. This is
NOT final whole-file FASTBOARD acceptance. Any unrelated≥750 whole-file repetition belongs to
owner's final file gates; unrelated borderline rows alone do not trigger this worker's repeat.
No new≥1000 observation is silently deferred. No performance fix, option, or helper introduced.

MainLemma actual `main_lemma` timing remains unavailable: the immediately preceding fresh 60s
bounded actual-profile run stopped before that target (5/27 declarations). MainLemma source is
unchanged and has no direct Θ_unique_le call, so this known costly pre-target timeout was not
repeated gratuitously. Fresh whole MainLemma semantics and normal/native builds pass, but neither
normal/native wall time nor prefix timing substitutes for main_lemma timing. No whole-project
performance claim is made. The inherited bounded trace/summary remains explicitly a limitation.

## Gate status and terminal handoff

Definition/header/import/comment/domain/conclusion protections: PASS. Sole public change:
approved Θ_unique_le.hr removal; prior approved index_le_Θ.hr removal retained. Exact original
contracts recoverable; public hq/global Θ hB/hr/header/wrappers/domain choices remain protected.
No new helper, axiom, sorry, native_decide, raised limit, masking, or production profiling scaffold.
All 47 untouched Theta source declarations and entire MainLemma source remain byte-identical.
All 17 source/pin hashes, FIRST histories, protected existing reports and the old inverse layers
are verified in the final freeze.

Final Theta SHA256 `ff85b7f132cf83c980323449b38558699e7e39d5a1b8bd895ac3374d78310207`.
Final MainLemma SHA256 `a002b02724dc9f4bcef52280bc96c736eb2fd9acbc06b5352c6eff55b94dd689`.

`final-process-drain.json` records every owned ordinary process/PID-group dead and every native
request returned complete, with pending=[], normal_pending=[], native_pending=[]. The terminal
`final-freeze.json` revokes source/scratch/report/compiler/native authority and releases the
compiler/native window. No further worker edit or request follows that freeze. Owner must inspect
hash/detail/semantics/profile evidence, then run frozen full `lake build` THEN separate
`lake build Roth.LeanEval`, exact-stage/commit/push clean, before fresh final filewide review.
Those owner gates and publication are not claimed by this worker report.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 78.682 s and 50.523 s.
Theta SHA256 `ff85b7f132cf83c980323449b38558699e7e39d5a1b8bd895ac3374d78310207` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p13-full.log` and `/private/tmp/roth-theta-p13-leaneval.log`; machine record
`/private/tmp/roth-theta-p13-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 20 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
