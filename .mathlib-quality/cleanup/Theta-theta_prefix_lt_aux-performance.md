# Dedicated prepublication performance revisit: `Roth.theta_prefix_lt_aux`

This is the mandatory additional repair before original35 publication; it adds no original
or helper audit count. Counts remain215/264, Theta34/35,9/14 files. All eleven introduced
helper audits remain complete (eight retained, three introduced/deleted). This worker
changes exactly one tactic in the private target and introduces no helper. Git, shared
logs, other declarations, publicTheta9/Main26 contracts, comments, imports and pins are
unchanged. Artifacts below are under `/private/tmp/theta35-prefix-performance/`.

I have read both mandatory skills, golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md, the entire cleanup worker workflow,
buzz workflow and relevant style/naming/profiling references. The dispatched Lean4.34
command overrides the obsolete profiler command in the reference.

## Repair and inherited baseline

The dimension-numerator comparison has identical quadratic terms on both sides. With
x=(n:ℝ)+1 its difference is4*x+3=4*n+7. `linarith only [Nat.cast_nonneg (α := ℝ) n]`
normalizes this comparison and finds a linear certificate; nonlinear product generation
from `nlinarith only` is unnecessary. The exact division transport and endpoint proof
remain unchanged, including the measured terminal
`simpa only [mul_assoc, Fin.castSucc_zero]` exception.

The original failed actual pair834.213/1098.066ms on c8 remains preserved at
`/private/tmp/theta35-successor-fresh/actual-profile-final-{first,repeat}.*`, its
`final-Theta.lean` and `owner-prefix-failed-pair-strict-slices.json`. The owner diagnostic
`/private/tmp/roth-theta-prefix-c8-repeat-diagnostic-hotspots.json` identifies249.173ms
in the numerator nlinarith subtree and116.989ms endpoint transport (nested, nonadditive).
No third unchanged-source capture discharges that failure. The later incidental758.869ms
prefix sample on release039806e8 is historical baseline evidence, not acceptance.

Baseline doctor reuses the preceding exact039806e8 complete native Theta/MainLemma
responses and successful module builds in `/private/tmp/theta35-fin-option-fresh/`.
They have0errors and8/3warnings. Optional cache/linter executable and whole-project
baseline are coordinator work, not repeated here. Fresh final affected-module builds,
independent semantic checks, complete native diagnostics, and actual production profiles
are the scoped acceptance gates below. Full build THEN separate LeanEval remain owner
obligations.

## All24 audit dispositions


| # | Item | Concrete disposition |
|---|---|---|
| 1 | Lint | Inherited same-SHA baseline is complete and unfiltered: eight Theta/three MainLemma warnings, none on this helper. Fresh final complete diagnostics below. |
| 2 | Have scan | hr0 is a three-line positivity certificate used under Θ_mono. The inner certificate was already inlined by the first dedicated audit; retain it. hCeq names the cast/Fin normalization needed by rw; h2 bridges the last-minimum comparison to the scaled lower bound; both have explicit by proofs. The by-free ratio certificate is already inlined; retain it. Final production has only hr0/hCeq/h2, each with proof content. |
| 3 | Options | No production per-declaration option, raised limit, attribute or diagnostic scaffolding. Only scratch whole-goal automation lowers maxHeartbeats to 10000. |
| 4 | Simp | hCeq ends with unsqueezed simp [Nat.cast_mul]. Actual unsqueezed terminal simpa [mul_assoc] compiled but caused a508.747ms hotspot and1409.941ms full target regression on f23. Restore terminal simpa only [mul_assoc, Fin.castSucc_zero] as the measured performance exception explicitly permitted by profiling.md; raw/source/trace preserved. |
| 5 | Naming | theta_prefix_lt_aux describes the strict Theta bound on a prefix, uses snake_case/private _aux, and matches no numbered auxiliary/scheme/forbidden-abbreviation pattern. No rename. |
| 6 | Packing | Every one of fourteen current signature lines measured in packing.json; all complete-next-item sums exceed100. The existing signature break separates the longer localized hanti from hrlast. No proof line exceeds100. |
| 7 | By | All := by occur on the preceding statement line; inline by certificates are likewise attached. No standalone by. |
| 8 | Format | Two-space proof indentation, no empty proof lines or tactic semicolon chains. Existing finite-index lambdas retain ↦. |
| 9 | Comments | No target narrative comments existed; none removed. Sole necessary caller's one-variable/prefix/combine comments and every unrelated comment preserved byte-for-byte. |
| 10 | Docstring | Private helper correctly has no docstring; public and module documentation untouched. |
| 11 | Visibility | Private auxiliary, sole direct production consumer theta_phi_lt_aux. No external API surface added. |
| 12 | Structure | Twenty-eight proof lines, ratio branch eight, remaining branches/subproofs at most five. No statement conjunction or trivial existential. No new helper needed. Public Θ_lt remains within15. |
| 13 | Mathlib | All five search methods freshly executed, plus fresh exact-CURRENT-prefix anonymous generic-route trials below. An independent exit0 environment check proves the audited helper/later Root Θ_lt absent. The earlier import Roth.Theta batch is superseded/contaminated and excluded from search evidence. Generic scalar components remain used directly; this substantive Θ induction transport is retained. |
| 14 | Junk def | n/a: theorem, no data definition or custom predicate. |
| 15 | Exists | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | n/a: neither tactic appears. |
| 17 | Negation | n/a: no push_neg/by_contra; no negation normalization required. |
| 18 | Generalise | All eighteen current effective binders freshly drop-tested; FIRST originals remain independently verified; strict/weak numerical and point-local candidates compiled. Retain the already localized minimum premise, exact immutable-FIRST adapter, and current-type assertion without further weakening. Details below. |
| 19 | Inequality | Sixteen signature inequality occurrences use < or ≤. No reversed ≥/>; name contains no _ge_/_gt_. Per-occurrence artifact below. |
| 20 | Normal form | Finite prefix/scaled exponent transport uses the established Θ convention and ordinary smaller-side-left inequalities. No alternate custom canonical predicate. |
| 21 | Syntactic generality | Localized last-minimum premise is directly supplied by fun j ↦ hanti (Fin.le_last j) at the sole consumer; all other arguments and IH convention stay identical. |
| 22 | Import fanout | n/a: imports unchanged. |
| 23 | Casts | The removed inner have carried (3 : ℝ) ≤ r j; its annotation moves onto the inline positivity expression and is load-bearing (untyped inline candidate fails with unresolved cast result type). No new cross-type coercion is introduced. Existing Nat-to-Real crossings and α:=ℝ in the selected linear-only numerator certificate remain necessary; zero redundant casts recommended. |
| 24 | Instances | No universe, typeclass or decidability binder and no new instance. Both original/current effective telescopes contain precisely eighteen ordinary/implicit binders. |


## Fresh five-method search and exact prefix trials

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | prefix restriction of finite family Roth theta scaled radii induction bound | Three unrelated additive-combinatorial Roth-number/Behrend results. |
| B Loogle | `_ / _ ≤ _ / _` | Generic Nat division inequalities; no project Θ transfer. |
| C LeanSearch | product of nonnegative ordered factors is monotone | Monotone.mul and Finset.prod_le_prod scalar components. |
| D source rg | full theta_prefix_lt_aux, theta/prefix variants; div_le_div₀ and multiplication variants | No full-name match; exact generic division/multiplication lemmas located. |
| E local name | div_le_div₀ | Source match div_le_div; index unavailable, so no indexed absence claim. |

Full raw responses are `search-results.json`; untruncated source outputs are
`mathlib-full-name.log` and `mathlib-source.log`. Auxiliary variants include
mul_le_mul_of_nonneg_left/right, mul_le_mul_of_nonneg, div_le_div₀ and Monotone.mul.
The common discrete/finiteness/separation/bornology buckets do not describe this goal.
Generic components are used directly; the higher-order Θ induction transport remains
substantive, not a one-to-three-call wrapper. No claim of exhaustive theorem absence
follows from remote indexes or name searches.

`PrefixAbsence.lean` preserves the exact current source byte prefix before the target,
then closes `Lemma7` and `Roth`. A successful independent compile asserts ACTUAL matching
private target and later Root.Θ_lt absent. `Automation.lean` uses that identical literal
prefix and current minimum-premise eighteen-binder header in eleven anonymous examples.
It tests grind, aesop, exact?, apply?, simp_all, gcongr, positivity, norm_num, lia,
decide, and field_simp/ring under a lowered10000 scratch heartbeat cap. Each actual
failure is mapped to its own source range by `automation-results.json`; expected-exit1
searches never certify positive proof or axioms. No imported matching target, named
failed trial or unbounded native multi_attempt contaminates these searches.

## Every effective binder and generality

Current final-body probes: `BinderFinalNegative.lean` freshly tests all18 drops with
autoImplicit=false and strict→weak hδ0/hl substitutions; `OtherWeakeningsNegative.lean`
tests1≤M→0≤M and3≤last→1≤last. `binders-results.json` maps every individual drop to
actual compiler errors. These mechanical failures do not establish logical necessity.
The immutable FIRST original type/proof and Antitone adapter are freshly compiled in
`FirstIndependent.lean` and the entire latest semantic scaffold; no premise is changed.

| Binder | Class | Use | Compiled candidates | Disposition |
|---|---|---|---|---|
| n | implicit ℕ | Finite dimensions and numerical exponent | individual drop | Unknown n in dependent types; retain Nat dimension. |
| δ | implicit ℝ | ratio and denominator | individual drop | Unknown δ; no generic field widening with project Θ/Real.log/rpow fixed. |
| ε | implicit ℝ | IH ratio/rpow and bound | individual drop | Unknown ε; same Real-valued construction restriction. |
| M | implicit ℝ | Θ argument and scale comparison | individual drop | Unknown M in dependent statement. |
| hδ0 | explicit proposition | strict lower denominator in div_le_div₀ | drop;0<δ→0≤δ | Both fail; retained strict positivity. |
| hδε | explicit proposition | quotient order and scaled ratio | drop | Unknown hδε in both certificates; already weak ≤. |
| r | implicit Fin(n+2)→ℕ | all weights and prefix | individual drop | Unknown r; finite natural multiplicities are part of Θ. |
| q | implicit Fin(n+2)→ℕ | logarithmic denominators and prefix | individual drop | Unknown q; established Θ denominator domain preserved. |
| hanti | explicit proposition | last-weight minimum at two uses | drop; point-localize to ∀j,rlast≤rj | Drop fails; prior point-local candidate compiled; existing localization retained without further weakening. |
| hrlast | explicit proposition | positivity and IH last lower bound | drop;3≤last→1≤last | Both mechanical proofs fail; retain numerical threshold3. |
| hratio | explicit proposition | prefix successor-ratio certificate | drop | Unknown hratio; already point-local finite-index family/weak inequality. |
| hq1 | explicit proposition | log bound after quotient comparison | drop | Unknown hq1; already weak ≤. |
| hqr | explicit proposition | weighted-log ordering for every prefix index | drop | Unknown hqr; every prefix point is used, no single-point replacement supplies entire family. |
| l | implicit ℕ | scaled natural multiplicities | individual drop | Unknown l in statement; replacing ℕ by ℝ changes Θ domain. |
| hl | explicit proposition | Nat.mul_pos and one≤cast-l | drop;1≤l→0≤l | Both fail; retain positive integer scale. |
| hM1 | explicit proposition | Θ_mono lower-scale hypothesis | drop;1≤M→0≤M | Both fail; Θ_mono requires1≤M. |
| hM | explicit proposition | Θ_mono upper-scale bound | drop | Unknown hM; already weak ≤. |
| ih | explicit higher-order proposition | lower-dimensional Θ bound | drop | Unknown ih; all inner Fin/weight/log premises transport substantively. |


Literature: n/a, private auxiliary exemption under cleanup§2.6d. Inversion: Θ is used
through Θ_mono and the IH, never unfolded then forgotten. Prefix restrictions, natural
multiplicity scaling and Real.log/rpow remain tied to this existing construction.
Abstracting Θ would add its same monotonicity/IH premises without a supported reusable
new object. No public API or mathematical generality change is recommended. Ordinary
argument names, order, BinderInfo, universes, current minimum premise and all FIRST
adapters remain fixed.

## All42 golfing rules

The historical unsqueezed508.747ms/1409.941ms failure remains a retained reason for the
terminal simp exception, not a fresh experiment. Existing prior inlining/localization
is recorded as inherited. All anonymous whole-goal searches are freshly rerun here.


| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | rw hCeq precedes an induction application with multiple certificates, not a closing exact; no rwa pair. |
| 1.4 | Final cast/product transfer already uses simpa using; preserve composition. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: no constructor chain. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction branch. |
| 1.9 | Finite-index lambdas precompose q/r and multiply by l; they are not eta wrappers. hr0 lambda proves positivity and cannot eta-reduce. |
| 1.10 | Already inlined in the inherited release: inner positivity certificate and by-free ratio certificate. Final hr0/hCeq/h2 retain substantive proof content; no forwarding have remains. |
| 1.11 | n/a: no apply followed by intro. |
| 1.12 | n/a: no redundant show. |
| 1.13 | n/a: no conjunction projection have. |
| 1.14 | n/a: only one rw hCeq, separated from cast normalization. |
| 1.15 | TRIED/REJECTED by actual measurement: unsqueezed terminal simpa [mul_assoc]508.747ms; target1409.941ms. Retain original simpa only [mul_assoc, Fin.castSucc_zero] as a documented measured performance exception. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Already uses .trans/.trans_lt composition; keep. |
| 1.18 | Remaining parentheses delimit arguments before additional arguments or .trans; no avoidable trailing-parenthesis block. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no trivial existential helper. |
| 2.1 | Actual anonymous whole-proof grind fails under conservative scratch cap. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.2 | n/a: no selected grind block with preceding tactics. |
| 2.3 | Final normalized weighted-log transfer remains one simpa using application. Unsqueezed complete candidate compiles but regresses actual performance; selected version uses the measured squeezed exception. |
| 2.4 | n/a: no analytic regularity/property goal. |
| 2.5 | Existing scalar numerator/product nonnegativity uses positivity. Whole-proof positivity correctly reports not a positivity goal. |
| 2.6 | Whole-proof gcongr makes no progress. Replace only the restricted numerator nlinarith with linarith; preserve div_le_div₀ and do not restore the previously measured broad-context gcongr failure. No repeated broad strategy experiment. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.7 | Whole-proof lia fails: real rpow/Theta/IH transfer, not a linear Nat/Int goal. Concrete 0<3 remains norm_num. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.8 | Actual anonymous whole-proof aesop fails; no production broad search. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.9 | Whole-proof norm_num leaves the induction goal; existing exact_mod_cast/norm_num certificates retained. Positive strict-weakness example uses finite cases/norm_num. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.10 | Whole-proof decide rejects free variables/noncomputable real proposition; no native_decide. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.11 | Actual field_simp/ring whole-proof trial leaves Theta inequality. The sole equality is multiplicative permutation without denominators. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.12 | Fresh CandidateLinearCombination replaces only the ratio identity ring by linear_combination and compiles. Both close a hypothesis-free polynomial permutation; retaining ring expresses that intent directly, no clarity/length advantage from alternative. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | Three-row mixed ≤/= /≤ calc needs an explicit multiplicative permutation. Collapsing to a long transported term hides the scale/ratio argument; current .trans composition already removes two-step bound chains elsewhere. |
| 2.15 | Final induction side-goals have distinct lower-bound/ratio/log-invariant proofs; uniform automation does not apply. No duplicated goal closers to distribute. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy continuity/measurability tactic. |
| 3.3 | n/a: no omega; actual lia whole-goal trial fails as recorded in2.7. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No automation attribute: private higher-order induction transport with large parameter telescope has one explicit caller. |
| 3.6 | Actual anonymous simp_all whole-goal trial fails under conservative cap; no selected squeezed simp_all. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 3.7 | Zero production limits added/raised; no profiling scaffolding or suppression. |


Step-back and simplify pass: pass-through beyond the selected restricted arithmetic
repair. The proof applies Θ_mono then the IH to a prefix with multiplicities scaled by l.
Each remaining certificate has a distinct mathematical role. No single tactic solves
all transports; no duplicate skeleton warrants a new helper. No built-in simplify
callable is exposed; this is a direct holistic review, not a claimed tool invocation.
Phase5a: no other refactoring. Phase5b: no rename needed; no shared queue write.

## Packing, inequality, protection

All14 signature lines are byte-identical to the inherited release. Fresh measurement
asserts their exact text against `packing.json`; all complete-next-item arithmetic
exceeds100. `format.width100` effective type printing is preserved in the semantic
scaffold. The28-line proof and8-line longest branch are unchanged.

| Signature line | Width | Next item width | Sum | Action |
|---|---|---|---|---|
| 1 | 81 | 23 | 105 | ok |
| 2 | 69 | 41 | 111 | ok |
| 3 | 45 | 63 | 109 | ok |
| 4 | 67 | 76 | 144 | ok |
| 5 | 80 | 62 | 143 | ok |
| 6 | 87 | 13 | 101 | ok |
| 7 | 56 | 310 | 367 | ok |
| 8 | 63 | 50 | 114 | ok |
| 9 | 56 | 62 | 119 | ok |
| 10 | 68 | 58 | 127 | ok |
| 11 | 64 | 77 | 142 | ok |
| 12 | 83 | 112 | 196 | ok |
| 13 | 73 | 47 | 121 | ok |
| 14 | 54 | — | last line | ok |

| Inequality | Actual line:column | Relation | Action |
|---|---|---|---|
| 1 | 768:64 | < | canonical; unchanged |
| 2 | 768:78 | ≤ | canonical; unchanged |
| 3 | 769:64 | ≤ | canonical; unchanged |
| 4 | 770:17 | ≤ | canonical; unchanged |
| 5 | 771:49 | ≤ | canonical; unchanged |
| 6 | 772:64 | ≤ | canonical; unchanged |
| 7 | 773:44 | ≤ | canonical; unchanged |
| 8 | 773:84 | ≤ | canonical; unchanged |
| 9 | 774:14 | ≤ | canonical; unchanged |
| 10 | 774:27 | ≤ | canonical; unchanged |
| 11 | 775:40 | ≤ | canonical; unchanged |
| 12 | 776:36 | ≤ | canonical; unchanged |
| 13 | 777:51 | ≤ | canonical; unchanged |
| 14 | 778:40 | ≤ | canonical; unchanged |
| 15 | 779:37 | < | canonical; unchanged |
| 16 | 780:73 | < | canonical; unchanged |

Zero reversed ≥/> in code; no _ge_/_gt_ name. `static-gates.json` verifies the ENTIRE
production file equals the inherited source with exactly one `nlinarith`→`linarith`
replacement. Every unaffected byte, all other source/pin hashes and all narrative
comments are protected. No new external lemma identifier, definition, instance, limit,
attribute, public signature or profiling scaffolding. `linarith` is compiled in the
successful selected candidate; no unverified identifier is introduced. Total source
line delta0; proof28→28. All casts in the diff are existing genuine Nat→Real or
load-bearing α:=ℝ ascriptions; zero new/redundant casts.

## Independent FIRST, entire semantic scaffold, and fresh final gates

`ActualSemanticsAugmented.lean` is the ENTIRE exact latest359 scaffold from
`/private/tmp/theta35-fin-option-fresh/ActualSemanticsAugmented.lean`,
SHAb7f8b1456db538ba9b1ea6e4b2440b04c2edd8e26b5e16085192d24998215106.
No old byte or prior adapter/deletion gate is omitted or edited. The four WHOLE
Index/originalTheta/originalMainLemma/current-independentMainLemma proof blocks retain
all offsets/hashes in `immutable-complete-blocks.json`. FIRST batch2 and its original
context are unchanged; all three FIRST batches and successful historical artifacts
retain their hashes in `first-immutability-before.json`.

The fresh FIRST independent compile re-elaborates the original proof, rejects current
self-use, and checks the exact18-binder original Antitone adapter plus CURRENT minimum
premise. The entire semantic compile freshly verifies current opaque values with
`value! true`, inferred types, standard axioms only (propext/Classical.choice/Quot.sound),
all unaffected prior adapters/deletions, complete affected callers and publicTheta9/
Main26 contracts. Theta then MainLemma are built before actual built-constant checks.
No stale raw equality tail, default opaque value!, PANIC, error or sorryAx is accepted.

The complete final normal cycle has exit0: `lake build Roth.Theta`31.483s, then
`lake build Roth.MainLemma`4.710s, independent FIRST31.210s, entire semantic scaffold
146.716s. The fresh FIRST has62 prefix PASS markers; the full scaffold has359 PASS
markers, including62 prefix markers. `semantic-marker-summary-final.json` rejects
errors/PANIC/sorryAx and verifies all source/FIRST/four-block hashes.

Fresh unfiltered native responses are `native-theta-final.json` and
`native-mainlemma-final.json`; both success=true, partial=false, timed_out=false,
0errors, no failed dependencies. Every warning is retained in full in those raw JSONs.

| Module | Line | Warning |
|---|---|---|
| theta | 1 | * `-/`: |
| theta | 93 | Variable name `hr` is not explicitly referenced. |
| theta | 101 | Variable name `hB` is not explicitly referenced. |
| theta | 101 | Variable name `hr` is not explicitly referenced. |
| theta | 109 | Variable name `hB` is not explicitly referenced. |
| theta | 129 | Variable name `hr` is not explicitly referenced. |
| theta | 252 | Variable name `hr` is not explicitly referenced. |
| theta | 547 | Variable name `hq` is not explicitly referenced. |
| mainlemma | 1 | * `-/`: |
| mainlemma | 149 | Variable name `hδ0` is not explicitly referenced. |
| mainlemma | 149 | Variable name `hr₁` is not explicitly referenced. |

These are protected existing header/unused-public-premise warnings, not regressions.
No helper warning is suppressed.

The heartbeat cross-check uses the pinned `#count_heartbeats in` command in isolated
exact-prefix scratch files:3118→2886 (232 fewer;7.44%). No instrumentation ships in
production. The initial candidate's missing Lemma7 scope closure and an initial
unprefixed count_heartbeats scratch command failed; exact failed sources/logs/statuses
are preserved as `CandidateClosureFailed.lean`/candidate.* and
`Heartbeats-before-syntax-failed.lean`/heartbeats-before-syntax-failed.*. Both corrected
positive runs exit0. The exploration checker was corrected to recognize Lean's tagged
`error(lean.unknownIdentifier)` diagnostics; all20 current drop/strict-weak ranges now
have actual errors, and the other two weakenings fail individually. No failed scratch
run is counted as positive proof, axiom or timing evidence.

## Actual production performance and scoped buzz result

The actual command is
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`.
The external420s capture window is not a Lean limit increase. Every ordinary/native
request is complete before the first capture and again before the repeat; all process
groups are dead in `pre-profile-drain.json`/`pre-repeat-drain.json`. Source is identical
through the complete final pair. No third unchanged-source sample is used.

The dynamic inventory matches all50 actual declarations exactly once. Full strict UTF8
raw log hashes/offsets are in `actual-profile-final-*-table.json`, with exact target/
caller slices and slice hashes in `profile-final-*-strict-slices.json`. Only disjoint
outer command and associated async proof/addDecl/compiler/linter rows are summed.
Nested macro/kernel and tactic rows are diagnostic and not double-counted.

| Final run | Declaration | Conservative ms | Actual proof anchors |
|---|---|---|---|
| first | theta_prefix_lt_aux | 757.698 | 1 |
| first | theta_phi_lt_aux | 887.425 | 1 |
| first | theta_lt_succ_aux | 852.192 | 1 |
| first | Θ_lt | 413.535 | 1 |
| repeat | theta_prefix_lt_aux | 767.127 | 1 |
| repeat | theta_phi_lt_aux | 641.027 | 1 |
| repeat | theta_lt_succ_aux | 728.387 | 1 |
| repeat | Θ_lt | 330.244 | 1 |

The selected numerator tactic roots (nonadditive diagnostic rows) are 82.288ms (first), 95.511ms (repeat). The preserved failed-repeat nonlinear root was249.173ms. Exact UTF8 row byte offsets, hashes and nested-row exclusions are in `final-numerator-hotspots.json`; these diagnostic times are never added to outer command totals.

Buzz outcome: FIXED for this scoped prefix repair, with supported source change and
fresh final-source actual acceptance. The preserved834.213/1098.066 failed pair is not
erased; `preserved-failed-pair.json` records its complete original row/raw/table hashes.
Limits removed0/added0; no new helper, global instance, attribute or scaffolding.
The known eight older Theta repairs remain separate final-file obligations. MainLemma's
bounded actual trace remains unmeasured before main_lemma. This is not a whole-file
performance PASS and does not discharge the owner's later cumulative profile obligations.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | build-theta-final.json and build-mainlemma-final.json, exact commands above, exit0 |
| definition_protected | PASS | exact whole-file one-tactic reconstruction; no definitions changed |
| theorem_statement_protected | PASS | entire target signature and all caller source bytes unchanged |
| structure_gate | PASS |28 lines, longest branch8, no conjunction/witness wrapper |
| naming_gate | PASS | descriptive snake_case private _aux; no forbidden patterns |
| line_packing_gate | PASS | all14 signature rows measured above and in packing.json |
| inequality_orientation_gate | PASS | all16 occurrences measured; no reversed relations |
| semantic/axioms/FIRST | PASS | fresh62/359 markers, exact opaque values/types/standard axioms/adapters/callers |
| complete native | PASS | both returned complete,0errors,8/3 existing warnings |
| scoped performance | PASS | actual final pair above;≥750 cases have same-source repeat |
| source/pins/comments/profiling protection | PASS | static-gates.json; exact single-tactic edit only |
| owner full build THEN separate LeanEval | OWNER PENDING | not run by this worker |
| owner cumulative29/all-actual/final-file profiles/publication | OWNER PENDING | no whole-file PASS claimed |

## All11 workflow steps and terminal handoff

| Step | Result |
|---|---|
|1|✓ Both skills and all mandated references/workflows read.|
|2|✓ All24 concrete audit dispositions.|
|2.5|✓ Five fresh search methods, exact-current-prefix anonymous routes, independent positive absence.|
|2.6|✓ Every current effective binder drop/weakening probe; exact independent FIRST adapter; private literature exemption and inversion.|
|2.7|✓ Every signature line measured.|
|2.8|✓ Every inequality scanned.|
|3|✓ All42 golfing rules with concrete outcomes.|
|4|✓ Step-back and direct holistic simplify pass; no further change.|
|5a|✓ Fresh complete unfiltered native responses,0errors.|
|5b|✓ Build/protection/semantic/axiom/performance gates complete.|
|6a|✓ No rename needed; no shared queue writes.|

Refactoring needed: none. No new helper needing another audit. Source line delta0,
proof28→28. Counts remain215/264,Theta34/35,9/14 files; all eleven introduced helper
obligations retain their existing accounting. Owner alone publishes original35 after
remaining cumulative29/allactual/finalprofiles/full+separateEval gates.

Frozen source hashes:

| File | SHA256 |
|---|---|
| Roth/Theta.lean | cfa05489380deeae6eb1bc63202249c3754b791357912aabff24e29e1cae4788 |
| Roth/MainLemma.lean | ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4 |
| Roth/Main.lean | f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069 |

`final-freeze.json` and `final-process-drain.json` bind final artifact/report hashes,
exact sources, FIRST/four-block evidence and pending[]. All source, scratch, report,
ordinary compiler and native authority is explicitly REVOKED/RELEASED at terminal
handoff; every own ordinary/native request is drained. No source edit follows final
freeze. No Git or shared-log mutation was made.
