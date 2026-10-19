# theta_prefix_log_le_aux — fresh dedicated helper deletion audit

Status: dedicated fresh helper DELETION audit COMPLETE; no original-declaration credit.
This is one of the eleven introduced-helper obligations in original35's unpublished Θ_lt batch.
No original-declaration credit: count215/264 and Theta34/35 remain owner-controlled.
Scope: delete this target, its necessary routine private caller proof, and this report only.
No Git, sharedlog, rename queue, pin or unrelated declaration mutation.

## Baseline and mathematics

Exact inherited Theta SHA3ea263890113e18bef9a29203ef1db57d929c18e40fd5201e34c9e4f0e776fc2.
Inherited target290.916ms, prefix caller546.609ms, phi572.808ms and publicΘ276.360ms are
preceding delta audit's actual uncontended same-source measurements, not fresh samples.
Inherited final native baseline is complete8/3 warnings, zero errors; owner supplied baseline
full-build evidence. Optional cache fetch/extra linter not needed. This worker's fresh builds,
full native diagnostics and semantic/profile refresh appear below. Full project then separate
LeanEval remain mandatory owner gates after all eleven helper audits.

I have read the required golfing-rules, proof-patterns, mathlib-search,
generalisation-patterns and cleanup-gates references, cleanup worker workflow,
Lean4/mathlib-quality skills and relevant style/naming/profiling rules.

Put x=n+1≥1 and C(x)=x(2x+1). The original proof separately decreases the reciprocal
by δ≤ε, increases C(x) to C(x+1), then uses hL. Mathlib div_le_div₀ already combines
both monotonicities. The remaining polynomial comparison is immediate polynomial arithmetic (compiled both
by targeted gcongr/linear arithmetic and by a restricted nlinarith certificate). It adds no substantive independent mathematical content to the generic
library result, so the no-wrapper rule requires deletion and direct use at its sole caller.
The exact direct argument is:

```lean
((div_le_div₀ (by positivity) (by
  nlinarith only [Nat.cast_nonneg (α := ℝ) n]) hδ0 hδε).trans hq1)
```

Initial scratch four-line and two-line nlinarith candidates and targeted gcongr compiled.
A real source profile then rejected the broad-context gcongr/linarith replacement. The
final inline proof uses an explicit restricted nlinarith certificate. To retain30 caller
lines when wrapping that certificate within100 columns, its existing hCeq rw/rfl proof
becomes terminal simp [Nat.cast_mul], one line shorter. All experiments are preserved. No new helper
was introduced. The frozen target had eight nonblank/noncomment proof lines, counted by
splitting at the FIRST := by only. An early progress note incorrectly said ten; corrected
from exact source before the change, consistent with original35's inventory. Production
target timing after deletion is N/A, never0. The necessary private prefix caller keeps
its exact full telescope and30 proof lines, and all public statements/definitions stay fixed.

## Every24 audit item

| # | Item | Concrete disposition |
|---|---|---|
| 1 | Lint | Inherited same-SHA unfiltered native baseline has eight Theta/three MainLemma warnings, none on this target. Fresh final unfiltered diagnostics recorded below; preserve unrelated public hypotheses. |
| 2 | Have scan | No have in the original eight-line proof or direct replacement. No forwarding binder to inline. |
| 3 | Options | No production option, limit, attribute or scaffolding; scratch automation cap10000 only lowers the search budget. |
| 4 | Simp | No simp in the scalar original/replacement. Necessary caller hCeq now uses terminal unsqueezed simp [Nat.cast_mul]. |
| 5 | Naming | Original mathematical prefix/log bound snake_case/private _aux passes forbidden-pattern scan. Delete name with wrapper; no rename. |
| 6 | Packing | All three historical signature lines measured below. Deleted target has no final signature. Final direct replacement lines37/73 codepoints; repair-packing.json. |
| 7 | By | Original := by on statement line; both replacement subproofs inline by. No standalone by. |
| 8 | Format | Two-space proof indentation; no empty lines or semicolon chain. Final restricted scalar subproof occupies one tactic line; diagnostic <;> variants remain scratch only. |
| 9 | Comments | Target zero narrative comments; zero removed. All surrounding comments and documentation byte-identical. |
| 10 | Docstring | Private helper had none. Delete declaration; no public docstring edits. |
| 11 | Visibility | Sole direct caller is private theta_prefix_lt_aux. Mathlib direct use removes unnecessary private surface. |
| 12 | Structure | Original8 lines; generic replacement2 in scratch, inline production argument2 lines. Caller stays30, all its branches/subproofs at most10; public Theta13 remains within15. |
| 13 | Mathlib | Five actual searches, source components and clean anonymous generic-route probes below. div_le_div₀ is a direct replacement once trivial numerator monotonicity is discharged by restricted polynomial arithmetic. DELETE wrapper. |
| 14 | Junk def | n/a: lemma, no data definition or custom predicate. |
| 15 | Exists | n/a: scalar inequality, no existential witness. |
| 16 | Show/change | n/a: neither present. |
| 17 | Negation | n/a: no push_neg or contradiction proof. |
| 18 | Generalise | All seven effective binders have compiled drop probes; strict-to-weak fails. Real-index and abstract ordered-field candidates compile. No production private API remains to generalize; direct Mathlib lemma already has generic typeclasses. |
| 19 | Inequality | Historical statement/hypotheses use only smaller-side-left < and ≤; no ≥/>. Replacement adds no reversed inequality. |
| 20 | Normal form | Canonical ordered-field division inequality. Direct Mathlib form avoids a specialized alternative API. |
| 21 | Syntax generality | Caller supplies hδ0/hδε/hq1 directly. Library division comparison followed by .trans exactly matches its needed bound; no restated public API. |
| 22 | Import fanout | n/a: no import change. |
| 23 | Casts | Removed target-specific Nat-to-Real casts with deleted signature/proof. No redundant cast added: the final α:=ℝ selects the real Nat.cast_nonneg certificate, avoiding an ambiguous class metavariable. |
| 24 | Instances | No old class, universe, decidability or instance binder. Replacement uses existing generic Mathlib typeclass inference; no named/new instance. |

## Five actual searches and clean generic-route trials

Raw complete native responses: search.json. Full source rg logs: mathlib-full-name-search.log
and mathlib-source-search.log; no head/truncation used to establish a negative claim.

| Method | Actual query | Finding |
|---|---|---|
| A Lean-Finder | 0<δ≤ε implies (n+1)(2(n+1)+1)/ε≤(n+2)(2(n+2)+1)/δ | Szemeredi/Stirling/sqrt-series unrelated results; no direct target hit |
| B Loogle | _ / _ ≤ _ / _ | Broad shape returned Nat/Int division-order components, not full real target |
| C LeanSearch | division decreases with positive denominator and quadratic numerator increases on nonnegative numbers | monotone_div_right_of_nonneg, strictMono_div_right_of_pos and Monovary division; components |
| D source rg | target full name; div_le_div_of_nonneg / div_le_div₀ / mul_le_mul_of_nonneg | Found simultaneous division comparison div_le_div₀ at Algebra/Order/GroupWithZero/Basic:1279. Full-name target no hit, not an absence proof |
| E local names | div_le_div_of_nonneg | Both original comparison components located; symbol index unavailable, so do not infer absence |

The source comment explicitly says div_le_div₀ is strictly more general than the original
single-denominator-order lemma. Its four hypotheses are nonnegative upper numerator,
numerator comparison, positive lower denominator, denominator comparison. A compiled
CandidateGcongr and CandidateTwoLines prove the entire original goal by this lemma followed by .trans; selected
production uses it directly and deletes the wrapper. AuxiliaryPositive #checks the exact
library names. No global Mathlib absence claim is needed or made. Discrete/finiteness/
separation/bornology equivalence buckets do not describe this scalar inequality.

AutomationNegative imports Roth.Index, which does not expose the target. Anonymous
examples test grind, aesop, exact?, apply?, positivity, gcongr, norm_num,
field_simp/nlinarith and simp_all. No named failed candidate can contaminate exact?/apply?.
All fail to close the complete goal; apply? reaches the deliberately lower10000-heartbeat
cap and lists only partial division-order routes. No limit is increased, and no unbounded
native multi_attempt repeated. Positive replacement/axiom evidence is in separate exit0
files, never inferred from this expected-exit1 batch.

## Every binder; generalisation and inversion

Actual FIRST effective telescope: seven binders, no universe/class/section binders.
Every drop is compiled with autoImplicit=false in BinderNegative.lean.

| Binder | Classification/use | Compiled candidates | Disposition |
|---|---|---|---|
| n explicit ℕ | index in both numerators | Drop; ℝ index with hn:0≤n | Drop gives unknown n; real candidate compiles. Deleted wrapper needs no new scalar API; sole caller's n is Nat induction index. |
| δ implicit ℝ | lower denominator/positive premise | Drop individually | Unknown δ in dependent statement; keep in exact scratch replacement adapter. |
| ε implicit ℝ | conclusion denominator | Drop individually | Unknown ε in hδε/conclusion; keep in adapter. |
| L implicit ℝ | upper bound | Drop individually | Unknown L in hL/conclusion; keep in adapter. |
| hδ0 explicit 0<δ | denominator positivity | Drop; weaken to 0≤δ | Both fail. Compiled δ=0, ε=1, L=0 counterexample satisfies weak premises but result3≤0 false. |
| hδε explicit δ≤ε | reciprocal comparison | Drop | Unknown hδε in proof; compiled δ=1, ε=1/10, L=10 makes result30≤10 false. Already weak ≤. |
| hL explicit C(n+2)/δ≤L | terminal upper bound | Drop | Unknown hL/unclosed result; compiled δ=ε=1,L=0 gives3≤0 false. Already weak ≤. |

The extra grouped-real-binder drop also fails, recorded honestly but does not replace the
three individual rows. GenericReal and GenericField both compile as successful diagnostic
weakenings of the concrete scalar setting (the field has Field/LinearOrder/IsStrictOrderedRing).
They are not production additions: deleting the wrapper uses Mathlib's already generic
field/order lemma directly. No global-to-point premise, bundled conjunction, decidability,
universe or unused typeclass weakening applies. Counterexamples are positive norm_num
proofs in AuxiliaryPositive, separate from mechanical failure evidence.

Literature: n/a, private auxiliary explicitly exempt under cleanup§2.6d. Mechanical
and mathematical generality checks still run. Inversion: no named concrete construction
occurs in the statement, and no unfolding rewrites hide an abstract theorem. The mathematics
is already a scalar quotient-order instance; direct generic Mathlib use is the supported
inversion/generalisation outcome, without another specialized helper.

## All42 golfing rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper |
| 1.2 | n/a: no by-rfl |
| 1.3 | n/a: no rw/exact |
| 1.4 | n/a: no simp/exact |
| 1.5 | n/a: no trailing rfl |
| 1.6 | n/a: no conjunction constructor |
| 1.7 | Original apply-div followed by nontrivial nlinarith; replace whole comparison by div_le_div₀ |
| 1.8 | n/a: no contradiction |
| 1.9 | n/a: no eta lambda |
| 1.10 | n/a: no have |
| 1.11 | n/a: no intro chain |
| 1.12 | n/a: no show |
| 1.13 | n/a: no bundled hypothesis projections |
| 1.14 | n/a: no rw |
| 1.15 | n/a: no terminal simp |
| 1.16 | n/a: no nonterminal simp |
| 1.17 | Use .trans hq1 on direct Mathlib division inequality |
| 1.18 | Grouping needed for constructor application to ih and method .trans; no avoidable trailing block |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: no existential |
| 2.1 | Actual anonymous whole-goal grind probe fails |
| 2.2 | n/a: no grind in selected proof |
| 2.3 | Necessary caller hCeq rw/rfl becomes terminal simp [Nat.cast_mul], offsetting the wrapped certificate line |
| 2.4 | n/a: scalar rational inequality, no analytic function property |
| 2.5 | Both original positivity obligations become one positive quadratic numerator nonnegativity proof, by positivity |
| 2.6 | Actual whole-goal gcongr fails before upper-bound transfer; targeted numerator variants compile; actual broad-context profile fails, so final uses nlinarith only with the explicit real cast nonnegativity input |
| 2.7 | n/a: final comparison is real polynomial arithmetic; no Nat/Int tactic goal |
| 2.8 | Actual whole-goal aesop fails |
| 2.9 | Actual norm_num does not close symbolic inequality; numeric counterexamples use norm_num in scratch |
| 2.10 | n/a: arbitrary real parameters, no finite decision |
| 2.11 | Actual field_simp/nlinarith leaves inequality without denominator sign transfer; no final identity needing ring |
| 2.12 | n/a: no original/final ring or ring_nf exit |
| 2.13 | n/a: no symmetric case branches |
| 2.14 | Eliminate entire repeated-expression calc using Mathlib simultaneous numerator/denominator monotonicity and .trans |
| 2.15 | Diagnostic gcongr side-goal closure tried with <;> linarith, linarith only and norm_num; final restricted nlinarith has one goal |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no legacy function tactics |
| 3.3 | n/a: no omega/lia; real linear side goal uses linarith |
| 3.4 | n/a: no rcases/rfl |
| 3.5 | n/a: deleted one-use wrapper needs no automation attribute |
| 3.6 | Actual simp_all whole-goal probe makes no progress |
| 3.7 | No production limit raised/added; no masking or diagnostic option shipped |

Step-back reflection: the original calc duplicated long polynomial expressions because it
handled numerator and denominator separately. Simultaneous Mathlib division monotonicity
is the stronger abstraction. Restricted polynomial arithmetic avoids the expensive full-context
gcongr/linarith step measured in the actual caller. Retaining even
the compiled two-line wrapper would preserve avoidable surface and another proof to audit.

## Packing, inequalities and source protection

Historical signature table uses Unicode codepoints and whole next binders/conclusion:

| Historical sig line | Width | Next complete item width | Arithmetic | Action |
|---|---:|---:|---|---|
| declaration with n/δ/ε/L/hδ0/hδε | 85 | hL with colon64 |85+1+64=150>100|ok|
| hL line |68|conclusion53|68+1+53=122>100|ok|
| conclusion := by |57|none|n/a|ok|

Deleted production target: final packing N/A. Final direct argument lines37/73≤100. Caller signature
is byte-identical; no new signature packing defect introduced. First/replacement adapter
type printing at format.width100 is captured in fresh verification log.

| Inequality occurrence | Original | Rewrite | Status |
|---|---|---|---|
| hδ0 |0<δ|none|smaller side left|
| hδε |δ≤ε|none|smaller side left|
| hL |C(n+2)/δ≤L|none|smaller side left|
| conclusion |C(n+1)/ε≤L|none|smaller side left|
| reverse ≥/> in signature |none|n/a|zero; no _ge_/_gt_ name|

owned-proof-repaired.diff contains target deletion and necessary private caller argument/hCeq proof repair.
owned-proof.diff and final-Theta.lean preserve the earlier failed performance variant.
All other source bytes reconstruct from the frozen baseline. No definition or public signature
changed; no header/docstring/narrative comment changed; no pin/options/scaffolding added.
The actual production constant and every production reference are checked absent in Lean's
built environment, separately from source-text scans. The actual caller contains div_le_div₀.

## Immutable FIRST and complete semantic refresh

FirstIndependent.lean independently re-elaborates the EXACT complete immutable FIRST target
and complete FIRST direct consumer, under the exact import/namespace context with no hidden
section/class/universe binders. Literal blocks are archived separately and compared byte-for-byte.
The full original seven-binder telescope is recovered by an explicit independent Mathlib
replacement adapter; names, BinderInfo, order, dependent argument types, conclusion and universe
arity are compared via Meta, and all opaque values use value! true plus inferred-type and
standard-axiom checks. Original proofs do not invoke the replacement or actual current consumer.
Actual retained direct consumer receives its own full FIRST metadata/value/axiom comparison.
Deleted production target has no actual value; environment/reference absence is the right gate.

ActualSemanticsAugmented.lean derives from the corrected114-PASS delta scaffold. Exactly two
retained-helper-list entries for the deleted prefix-log constant are removed, recorded in
semantic-prefix-deletion-adjustment.diff and provenance JSON. Otherwise the ENTIRE old scaffold
is byte-identical, including immutable72cf Index/355a Theta original proofs, full original2b
MainLemma proof, ENTIRE independent CURRENT MainLemma module, all26 current BinderInfo/names/order/
types/conclusion including hq0/hq1/h32/h33, actual RootΘ dependency and AST rejection of imported
Root.main_lemma/privateRootMain helpers. New FIRST/deletion/adapter/actual-consumer checks append.
This is an explicitly documented inventory adjustment, not an assertion that the old unedited
scaffold remains a literal prefix. Both modules are rebuilt before actual Root queries.
The supported scaled13/FIRST15 recovery, delta3 and publicΘ9 contracts remain intact.

## Fresh gates and actual performance

The initial real source variant, SHA cdd7c6f8122d3b97314086450f8cc921e8a0e80acb78b8a8bc2f60df901693d6,
completed an actual51-declaration whole-source capture in284.099s but FAILED the owned caller
budget: prefix1539.851ms, phi724.358ms, public347.768ms. Raw actual-profile-first.log/.json,
table, strict UTF8 slices/offsets, failed disposition and immutable final-Theta.lean snapshot
remain preserved. These are failed historical measurements, not accepted final samples.
The trace attributes423.055ms to gcongr and270.539ms to its all_goals linarith subtree
(nested rows are diagnostic, never double-added to the total).

Full consumer-copy diagnostic variants, labeled NONPRODUCTION, measured control863.562,
restricted-linear660.313, norm_num567.068, explicit numerator certificate508.203ms. These
identify a repair; they do not certify actual source performance. DiagnosticConcise drops
α:=ℝ and FAILS unresolved IsOrderedRing metavariables, preserved as a failed trial.
DiagnosticPacked uses the full consumer proof, section type/classes, explicit certificate
and hCeq simp repair; it compiles exit0. Both modules/FIRST/full augmented semantics and
complete native diagnostics are refreshed after applying that repair, before new actual
source measurements. No unchanged failed third run or cherry-picking is used.

Actual whole-source captures succeed with all51 declarations matched, one actual proof anchor per
scoped retained declaration. Tables preserve strict UTF8 raw bytes/offsets, command+async proof/
addDecl/linter outer rows without nested kernel/macro duplication. No third cherry-picked run.

| Declaration | Fresh run | Disjoint total ms |
|---|---|---:|
| theta_prefix_log_le_aux | deleted production | N/A |
| theta_prefix_lt_aux | final-first | 877.212 |
| theta_phi_lt_aux | final-first | 682.808 |
| Θ_lt | final-first | 357.826 |
| theta_prefix_lt_aux | final-repeat | 918.895 |
| theta_phi_lt_aux | final-repeat | 521.668 |
| Θ_lt | final-repeat | 302.810 |

All scoped retained values are <1000ms. Any first value≥750ms has its mandatory same-final-source
repeat above; if all are <750ms, no repeat is required. Target deletion is never measured as0.
The full unfiltered51-row table still records unrelated >1000ms declarations; this scoped audit
does NOT certify whole-file performance. The separate numerical/index/quadratic and base/succ/
large-delta queues remain owner work. No finite MainLemma main_lemma timing was measured here.

| Gate | Result | Fresh evidence |
|---|---|---|
| lake_build_file Roth.Theta | PASS | lake build Roth.Theta, exit0, 47.390s; build-theta-repaired-final.log/.json |
| lake_build_file Roth.MainLemma | PASS | lake build Roth.MainLemma, exit0, 43.615s; build-mainlemma-repaired-final.log/.json |
| definition_protected | PASS | No def/abbrev changed; exact baseline reconstruction |
| theorem_statement_protected | PASS | Supported private wrapper deletion; all51 retained signatures byte-identical; independent full metadata adapters |
| structure_gate | PASS | Deleted target; caller30→30, Θ13→13; no scoped branch/subproof>10 |
| naming_gate | PASS | No forbidden surviving target name or new name, no rename |
| line_packing_gate | PASS | Historical three-line table; final deleted signature N/A; restricted inline library argument split into37/73-codepoint lines |
| inequality_orientation_gate | PASS | Four historical proper-oriented occurrences, zero reversed |
| native_diagnostics | PASS | Fresh complete unfiltered8/3 warnings,0errors; success=true,partial=false,timed_out=false |
| independent FIRST/replacement | PASS | Whole exact FIRST target+FIRST consumer, adapter7/actual consumer18 metadata; standard axes and value! true |
| actual deletion/reference absence | PASS | Programmatic module constant lookup and AST reference scan, direct library dependency in actual consumer |
| full old/current caller semantics | PASS | Fresh augmented139-PASS run, immutable Index/Theta and ENTIRE original/current MainLemma proofs; full26/Θ9/scaled13 metadata |
| scoped performance | PASS | Actual51 capture(s), UTF8 strict slices and all mandatory repeats |
| full project then separate LeanEval | OWNER PENDING | Required after all eleven helper audits; no publication here |

Native warning inventory remains literal in the two unfiltered native JSON files: Theta header1;
unused hr at93/101/129/252, hB at101/109, hq at547. MainLemma header1 and unused hδ0/hr₁ at149.
These existing warnings are outside this audit or protected by explicit user/API choices.

Fresh FirstIndependent exits0 in50.738s; augmented semantic refresh exits0 in117.127s with139 PASS markers.
Raw fresh native paths: native-theta-repaired-final.json and native-mainlemma-repaired-final.json.
Both logs are clean of error/PANIC/sorryAx. Immutable complete-block hashes/ranges are refreshed
in immutable-complete-blocks.json; all FIRST files and immutable success log/status hashes match.

Simplify/buzz invocation tools are unavailable in this host. Their scoped work was performed
directly: holistic reuse/quality/efficiency review selected Mathlib replacement/deletion, and
uncontended actual trace measurements above supply the performance gate. No unavailable-tool
invocation is claimed. No additional recommended change remains undone.

## Required eleven-step checklist

- [✓] Step1: required references and workflows read.
- [✓] Step2: all24 audit items have concrete dispositions.
- [✓] Step2.5: all five actual searches and clean generic-route probes.
- [✓] Step2.6: every seven effective binder probed; real/field candidate, counterexamples, literature exemption and inversion.
- [✓] Step2.7: complete historical signature packing table; deleted final signature N/A.
- [✓] Step2.8: complete inequality occurrence table, zero reversed.
- [✓] Step3: every42 golf rule has concrete status.
- [✓] Step4: whole-strategy/reuse reflection, direct replacement selected.
- [✓] Step5a: fresh complete unfiltered native diagnostics.
- [✓] Step5b: source/API/independent semantic/axiom/build/actual profile gates.
- [✓] Step6a: no renames; shared queue untouched.

Original target8 proof lines→deleted; caller30→30; Θ13→13; file1025→1013 lines (−12).
No production helper introduced; this dedicated audit deletes inherited theta_prefix_log_le_aux.
Retained new35 helpers9; total original35 helper audit obligations remain11 (9retained+2deleted).
No Git mutation, original-count credit or publication. All normal/native requests drained, pending[].
Source authority is revoked at this final handoff; no further source edits by this worker.
Exact source/FIRST/report/artifact hashes are in final-freeze.json.
