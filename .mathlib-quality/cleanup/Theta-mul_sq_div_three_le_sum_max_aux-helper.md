# Dedicated new-helper audit: `Roth.mul_sq_div_three_le_sum_max_aux`

This leaf audits exactly the new private quadratic estimate. Original-declaration count
contribution: **0**. Standing authority permits supported recommendations. No Git or shared
report mutation was performed. The separately audited linear sibling is byte-identical.
The public `min_le_sum_max` retains its current domain/name/conclusion; only its routine proof
is simplified. The complete original `index_le_lem6` telescope, including `hq` and DecidableEq,
remains protected. Owner full-project build and separate LeanEval remain pending for this batch.

## Baseline, source and scope

Release SHA256: `ed77a5f89c25d8a54cb4d66a2a3d0ca05478906540635d8aebaef84eb97ee328`.
Inherited SAME-SOURCE complete unfiltered native diagnostics:
`/private/tmp/roth-theta-linear-helper/final-lsp.json`: success true, partial false,
timed_out false, failed_dependencies [], zero errors, 17 warnings, none in this helper.
Inherited real exact-prefix measurement and anchors in that directory:
`final-profile.log`, `profile-status.jsonl`: quadratic562.377ms, linear467.473ms,
publicmin267.293ms. These are inherited measurements, not fresh leaf measurements.
Older original25 full89.100s/LeanEval28.568s belong to a different source and are not current gates.

Scratch evidence below is under `/private/tmp/roth-theta-quadratic-helper/` unless stated.
`release.lean` preserves the starting module. `frozen-source.lean` preserves the final module.
Final source SHA256: `1e01b2a8d662c434a0fe32c58544459dc4a9d5a24065329876eecc341003f685`.
Dialect: classic imports; no module-system conversion. Header metadata and all narrative comments
and docstrings are untouched. No imports, attributes, global options or definitions changed.

Read lean4 and mathlib-quality SKILL.md, full cleanup workflow, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates; relevant style,
naming, normal-form, syntactic-generality and profiling references. The explicit leaf scope
supersedes file-wide edits and owner build responsibilities.

The first-introduction original helper is independently recovered from
`/private/tmp/roth-theta-min-sum/edited-source.lean`, SHA256
`08e55dec3fe02fe2cf3c9324eca959cf60c81f180bee5af389b9f5aa40ea1248`, agreeing with
`initial-helpers.lean`, SHA256
`f87ff08d34f1db5705f643ee0fbf779eadacc50064cde54da2457868438bb23b`.
`initial-text-match.txt` is True. `initial-independent.lean` independently compiles its initial
25-line nlinarith proof without invoking the current helper, exit0 in29.327s; actual standard
axioms only. The literal full first-introduction snapshot predates a caller correction and is
not presented as successful-module evidence.

## Findings and changes

1. Remove private `hr : 0 < r`. For `r ≤ 0`, the left side is nonpositive and every summand
   is nonnegative. This is a genuine strengthening, not merely an unused-proof-argument deletion.
2. Weaken private `hl : θ * r < l` to `θ * r ≤ l`. At equality use the audited linear bound,
   multiply the equality by θ, and the nonnegativity of `r * θ²`.
3. Preserve `hθ : 0 ≤ θ`. A compiled counterexample has θ=-1, r=1, l=0: the size assumption
   holds but the left side is1/3 and the sum is0. Dropping the size assumption likewise fails
   at θ=3,r=1,l=0. See `necessity.lean`/`.log`, exit0.
4. The positive-r continuation exceeded the10-line branch limit even in a29-line proof.
   Extract it into new private `mul_sq_div_three_le_sum_max_of_pos_aux` (22 body lines,
   no case branches). The assigned wrapper has7 body lines; its r-positive continuation has4,
   nonpositive case2, strict case1 and endpoint case2. No structural deferral remains.
5. The routine public proof no longer needs its rp=0 case. Keep θ≤0 treatment, then the two
   size cases; use `le_of_not_ge hθ` directly. Public proof13→7 body lines, exact type unchanged.
6. Preserve scoped `linarith only`, the explicit square/product certificate, and abstraction
   of θ*r before arithmetic in the extracted positive case. Combine cast normalization and
   the termwise sum rewrite; do not restore expensive unrestricted nlinarith.

The new helper requires a **separate fresh dedicated audit** after this leaf. Its exact first
text is `new-helper-initial.lean`, SHA256
`bbfaa4824d09a1f10356cbeb795bfae23d296889f76a675a576bfaedcaa2225c`.
First complete source snapshot: `new-helper-first-introduction-full.lean`, SHA256
`7685f1536fd898cfe55e148154245193b37cb1c23bd642dd32bcea7429f265c5`.
Only signature packing subsequently moved `{l : ℕ}` onto its first line. Its initial positive-r,
nonnegative-θ, strict-size contract is unchanged. `new-initial-independent.lean` independently
compiles that exact initial proof and checks the actual built suffix/type/standard axioms.

## Full substantive24 audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Inherited and final diagnostics: no warning in assigned helper, new helper or routine min. Other17 warnings remain documented and outside scope. |
| 2 | HAVE SCAN | Final assigned proof has no `have`. Original hθr removed; hn moved to positive case, hnle/hnlt retained there for floor bounds, hsum normalized then used for hbound, and nontrivial hbound retained as arithmetic stage. Positive helper receives its own subsequent audit. |
| 3 | SET_OPTION | None in target or diff; no limits raised or suppressed warnings. |
| 4 | SIMP SQUEEZE | Assigned proof has none. Extracted positive sum uses explicit nonterminal `simp only [Finset.sum_div, sub_div, mul_div_cancel_right₀ _ hr.ne']`; cast normalization combined. |
| 5 | NAMING | `mul_sq_div_three_le_sum_max_aux` describes inequality, snake_case, private `_aux`, no forbidden abbreviation/number pattern. Extracted `_of_pos_aux` describes its positive-r case. No rename warranted. |
| 6 | LINE PACKING | Measured codepoint table below, all rows pass. |
| 7 | BY PLACEMENT | `by` ends declaration line; none alone. |
| 8 | FORMAT | Two-space tactic indent, four-space signature continuation; no blank proof lines, haveI/letI, sequential semicolon chains or trailing whitespace introduced. |
| 9 | COMMENTS | None inside initial helper; all surrounding original narratives/docstrings unchanged. |
| 10 | DOCSTRING | Private helper correctly has none; existing public source prose preserved. |
| 11 | VISIBILITY | Assigned and extracted helper private; no public helper added. |
| 12 | STRUCTURE | Assigned7, new positive22, publicmin7; no independent conjunction; all assigned/public branches≤10. New helper has no branches. |
| 13 | MATHLIB | Five actual searches plus clean pretarget anonymous compiled exact?/apply? trials; no full replacement located. Building blocks found and used directly. Details below. |
| 14 | JUNK DEF | n/a: theorem, not a definition; no def/abbrev change. |
| 15 | EXISTS LEMMA | n/a: no existential witness conclusion/construction. |
| 16 | SHOW/CHANGE | No show or change in assigned proof/diff. |
| 17 | PUSH_NEG | None; no deprecated tactic introduced. |
| 18 | GENERALISE | All six original effective binders probed; drop hr and weak hl implemented, remaining hypotheses certified necessary/dependent. Generic scratch succeeds, not recommended for this one-use concrete private API. |
| 19 | INEQUALITY | No ≥/> token in signatures; table below. |
| 20 | NORMAL-FORM | Canonical Finset.range sum, max0 truncation, powers and real division. No duplicate representation or equivalence API needed. |
| 21 | SYNTAX-GEN | Dropping hr and allowing endpoint makes call easier; old strict call adapts with `.le`. Public type unchanged. |
| 22 | IMPORT-FANOUT | n/a: no new import; no downstream dependency expansion. |
| 23 | CASTS | No redundant real-to-real cast added. Nat→real casts in hl/hnle and hsum bridge different types; explicit0:ℝ in arithmetic certificate fixes target type. No forced section instances added. |
| 24 | INSTANCE-NAME | n/a: no instance declaration or named class binder introduced. |

## Actual five-method mathlib search

| Method | Actual query/evidence | Result |
|---|---|---|
| A Lean-Finder | `search-finder.json`: lower bound rθ²/3 for truncated arithmetic-progression sum | Floor-power reciprocal estimates and unrelated Roth-number bounds, no matching result. |
| B Loogle | `search-loogle.json` first query `Finset.sum, max, _ ≤ _` rejected ambiguous max; corrected `Finset.sum, Max.max, _ ≤ _` in `search-loogle-corrected.json` | `Finset.max_sum_le` is a partial generic sum/max bound, not this quadratic estimate; other hits unrelated. |
| C LeanSearch | `search-search.json`: lower bound sum positive part arithmetic progression square floor | Nat.floor_le building block and unrelated floor-power estimates; no equivalent. |
| D source search | `source-search.log`: sum_range/floor/sum/max in BigOperators/Intervals and Floor/BigOperators; `full-name-search.log` untruncated full candidate-name sweep of mathlib | Arithmetic-sum identity available; candidate name absent from textual source. This does not prove semantic absence. |
| E name-pattern | `search-local.json`: sum_range | `Finset.sum_range_id_mul_two`, range-sum and sum-integral tools. Index unavailable, so empty results would not be absence evidence. |

Auxiliary variants considered: sum_range_id, sum_range_id_mul_two, max_sum_le,
sum_le_sum, sum_le_sum_of_subset_of_nonneg, range_subset_range, Nat.floor_le,
Nat.floor_lt and Nat.lt_floor_add_one. These build the proof but do not directly replace it.
Common-equivalents lookup: no discrete/finite/compact/separation bucket matches.
No 1–3 mathlib-call wrapper replacement was found. The substantive floor argument is isolated,
and the assigned wrapper combines meaningful sign/boundary cases with project estimates.

`automation.lean` ends the exact source prefix BEFORE the assigned original target, so no imported
copy of that theorem or named failed trial can contaminate exact?/apply?. Distinct anonymous
examples tried grind, aesop, exact?, apply?, simp, positivity, gcongr, lia, norm_num, decide,
field_simp/ring and linear_combination. Exit1 is expected and is not axiom certification:
none closes the original sum bound; apply? gives partial suggestions only. Final stronger-wrapper
automation against the extracted support helper is separately recorded in final-automation.log.
The known stalled native multi_attempt limitation was respected; ordinary bounded isolated
compiler trials were used. No claim of exhaustive semantic absence is made from search alone.

## All-effective-binder compiled probes and generality

| Original binder | Role | Actual drop/weakening probe | Decision |
|---|---|---|---|
| `{θ : ℝ}` | Value in square, summands, hθ, hl | Header-only deletion with autoImplicit=false in dependent-drops.lean and current-drops.lean rejects unknown θ; generic K candidate compiled separately. | Retain real value; no parameter-free statement exists with the same conclusion. |
| `{r : ℝ}` | Value in square factor, denominators, hl | Header-only deletion rejects unknown r; field/floor-ring candidate compiled. | Retain real value/domain. |
| `hr : 0 < r` | Original denominator/sign argument | Unedited drop fails hr.le/hr.ne'; redesigned nonpositive branch + positive case compiles. Weaker0≤r follows from stronger drop result. | Drop completely. |
| `hθ : 0 ≤ θ` | Floor/product control | Unedited/current drop fails hθ; necessity.lean proves explicit counterexample to resulting statement. Already weak inequality. | Retain. |
| `{l : ℕ}` | Finset.range length | Header-only deletion autoImplicit=false rejects unknown l; range domain requires Nat. | Retain natural value; no applicable class-parent/pointwise/universe weakening. |
| `hl : θ * r < l` | Truncation length | Drop fails hl and has certified θ=3,r=1,l=0 counterexample. Nonstrict candidate and final wrapper compile; endpoint supplied by linear sibling. | Weaken to θ*r≤l. |

`negative-binders.lean` separately records the six original proof drop trials. Initial θ/r
string replacement also touched proof text and produced parse errors; these two trials are
superseded by **header-only** corrected `dependent-drops.lean`, with proper unknown-identifier
failures. `current-drops.lean` independently repeats all five remaining effective binder drops
against the final support prefix. Expected-failure exit1 files never certify axioms.
`necessity.lean` is a separate exit0 counterexample certificate.
`generic.lean` compiles a field/linear-order/strict-ordered-ring/floor-ring version of the
candidate (and supporting linear estimate), standard axioms only. It is useful evidence that
no analytic real property is used, but no abstract-API churn is recommended for a private
case estimate with one concrete caller. There are no effective σ/τ, Fintype or DecidableEq
binders on this helper; actual built type inspection verifies this rather than relying on
visible header text. No untested class binder is silently omitted.

Literature search: n/a, private helper exemption. Inversion check: no named concrete construction
is unfolded and then abandoned. Finset.range/max and the natural floor are used substantively
throughout the extracted positive proof. The generic ordered-field candidate above is the
applicable algebraic abstraction; it introduces no changed public result or extra public API.

## Measured signature packing and inequality scan

Widths count codepoints, including indentation and `:= by` on the final line. Actual built
#check-style type rendering uses `format.width 100` in private-compatibility.log.

| Declaration / signature line | Chars | Next full binder/conclusion token | Arithmetic | Action |
|---|---:|---|---|---|
| assigned342 |95| conclusion including `:= by`,61 |95+1+61=157>100|ok|
| assigned343 |65| no next signature line |n/a|ok|
| new-positive317 |96| `(hl : θ * r < l)`,16 |96+1+16=113>100|ok|
| new-positive318 |84| no next signature line |n/a|ok|
| routine min357 |49| full conclusion including `:= by`,81 |49+1+81=131>100|ok|
| routine min358 |85| no next signature line |n/a|ok|

| Occurrence | Location | Original orientation | Rewrite / rename |
|---|---|---|---|
| 0 | All assigned/new/public signatures | No ≥/> token | n/a; all≤/< already smaller-first; no `_ge_`/`_gt_` declaration name |

## All42 golfing-rule checks

| Rule | Concrete result |
|---|---|
|1.1 by exact|n/a: no by-exact wrapper.|
|1.2 by rfl|n/a: no by-rfl wrapper.|
|1.3 rw+exact→rwa|n/a in assigned proof; extracted sum chain replaced together by simp+sum_le_sum.|
|1.4 simp+exact→simpa|Considered for extracted sum; explicit nonterminal simp plus pointwise order theorem keeps expected types clear.|
|1.5 trailing rfl|n/a: none.|
|1.6 anonymous constructor|n/a: no conjunction/product construction.|
|1.7 apply+exact|n/a: no apply sequence.|
|1.8 by_contra!|n/a: no contradiction proof.|
|1.9 eta reduction|Nonnegative-sum membership lambda is required by Finset API; not eta-reducible.|
|1.10 inline single-use have|Final assigned proof has none; original hθr removed; transformed hsum and arithmetic hbound remain in extracted stage.|
|1.11 refine+fun|n/a in assigned proof; extracted sum uses direct term lambda.|
|1.12 redundant show|n/a: none.|
|1.13 obtain pairs|n/a: no projection extraction.|
|1.14 merge rw|No adjacent rw commands left.|
|1.15 terminal simp|n/a in assigned proof; extracted simp is nonterminal.|
|1.16 nonterminal simp squeeze|Extracted sum uses only named sum/division lemmas; no bare nonterminal simp introduced.|
|1.17 dot notation|Uses `.trans`, `.ge`, `.le`; direct theorem application where no natural dot receiver.|
|1.18 <| over parens|Existing parenthesized proof application groups multiargument order lemmas; no dollar or avoidable trailing-parenthesis chain introduced.|
|1.19 push Not|n/a: no negation-push tactic.|
|1.20 existential junk|n/a: no existential conclusion.|
|2.1 grind whole|Actual clean pretarget trial failed; final supporting-helper trial separately logged.|
|2.2 delete before grind|n/a: no selected grind.|
|2.3 simpa consolidation|Sum block consolidated from5 to3 lines; no simp/exact chain in assigned proof.|
|2.4 fun_prop|n/a: no continuity/differentiability/measurability goal.|
|2.5 positivity|Actual whole bound trial rejected non-positivity goal; uses direct product/sum nonnegativity for nonpositive r. Numeric denominator supplied by norm_num.|
|2.6 gcongr|Actual whole trial makes no progress; quadratic truncation needs floor arithmetic. Direct div comparison retained in positive stage.|
|2.7 lia|Actual trial fails on real nonlinear finite sum; no omega fallback introduced.|
|2.8 aesop|Actual trial fails; final wrapper attempt separately logged.|
|2.9 norm_num/cast|Whole norm_num trial leaves symbolic sum; norm_num closes numeric denominator; cast normalization merged.|
|2.10 decide|Actual trial rejects free-variable proposition; no native_decide.|
|2.11 field_simp/ring|Actual whole trial leaves symbolic sum; field_simp closes extracted algebraic division identity.|
|2.12 linear_combination|Actual whole trial fails on sum; selected scoped linear certificate at endpoint and positive arithmetic retained.|
|2.13 wlog|n/a: positive/nonpositive r cases have different mathematical behavior, not symmetric cases.|
|2.14 calc term|Positive stage has genuine algebraic/division/termwise/subset steps; no redundant2-step calc. Assigned proof has none.|
|2.15 common-goal <;>|n/a: sign and endpoint cases need distinct facts.|
|3.1 erw→rw|n/a: no erw.|
|3.2 fun_prop migration|n/a: no legacy continuity/measurability tactic.|
|3.3 omega→lia|No omega in assigned/extracted/public proof; lia trial recorded under2.7.|
|3.4 rcases rfl|n/a: case hypotheses are inequalities/equality, no auto-substitution pattern needed.|
|3.5 automation attributes|No global registration warranted for a single-use private case estimate.|
|3.6 simp_all|n/a: no simp_all only; no selected context-saturation proof.|
|3.7 limits|No maxHeartbeats/maxRecDepth or tactic-limit raise introduced.|

Step-back reflection: direct mathlib search and clean exact?/apply? did not eliminate the
nontrivial floor bound. A global tactic is less explicit about the needed sign and endpoint
cases. The final7-line proof states those cases directly; the nontrivial positive floor proof
is independently named and stays under30 lines. No cosmetic new public API is recommended.

## Identifier verification

| Introduced/reference identifier | Verification | Result |
|---|---|---|
|`mul_sq_div_three_le_sum_max_of_pos_aux`|New declared private case; independent initial proof and actual suffix/type/axioms check|pass|
|`lt_or_eq_of_le`|Mathlib/Order/Defs/PartialOrder.lean:223 + final module|pass|
|`mul_nonpos_of_nonpos_of_nonneg`|Mathlib/Algebra/Order/GroupWithZero/Basic.lean:76 + final module|pass|
|`div_nonpos_of_nonpos_of_nonneg`|Same source:1109 + final module|pass|
|`le_of_not_ge`|Mathlib/Order/Defs/LinearOrder.lean:94, corrected #check output + final module|pass|
|`congrArg`, `le_or_gt`, existing sum/floor/order names|Existing source uses, actual selected proof compiled in final module|pass|

Untruncated raw source results: `identifier-source-verification.log`. No unverified identifier
or generated-name assumption remains in production. Private constant names are found by suffix.

## Exact original and actual-built compatibility

`private-compatibility.lean` includes the independently compiled exact initial25-line proof
in namespace InitialQuadratic; programmatic suffix lookup locates actual
`_private.Roth.Theta.0.Roth.mul_sq_div_three_le_sum_max_aux`. The old telescope is not taken from
the weakened current declaration. Every retained binder's name/order/BinderInfo/type is checked;
exact drop set `[hr]`, and only hl changes from strict to weak via `le_of_lt`. The adapter
`fun {θ r} hr hθ {l} hl ↦ actual hθ (le_of_lt hl)` has the exact initial type; proof equality
recovery is kernel checked. Actual built and independently initial axioms are exactly the usual
propext/Classical.choice/Quot.sound, as are the recovery equality axioms.

The first private probe printed `ConstantInfo.value!` with its default `allowOpaque=false`,
which caused an internal panic/dummy printing despite process exit0. Its raw log is retained
but is **superseded** by `private-compatibility-corrected.log`: `value! true` obtains the actual
independent theorem value and its inferred type is explicitly checked before certification.
Only the corrected clean run certifies proof-value inspection (exit0 in39.394s).

`actual-compatibility.lean` is copied verbatim from the immutable prepared
`/private/tmp/roth-theta-min-sum/actual-compatibility.lean`; its independent complete original
Index+Theta namespace and fixed original adapters were not edited. Final run exit0 in50.167s.
It independently compiles original public proofs, recovers full min_le_sum_max original
telescope with exact approved drops `[hrp,hθ]` only, and recovers index_le_lem6 with drop set`[]`.
The latter explicitly includes hq, Fintype and DecidableEq; all old names/order/BinderInfo and
conclusions are checked. Logs report FULL ORIGINAL TYPE/VALUE/BINDERINFO/AXIOMS PASS for both,
and actual helper/public/caller standard axioms. No public drop set or independent namespace
was relaxed by this leaf. The new positive helper initial independent/type/axiom check also
passes exit0 in34.710s. `final-probe-status.jsonl` records expected-failure files separately.

## Final verification and leaf gates

Final module command: `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0 in47.864s,
`final-module-build.log` and `final-module-build-status.json` on the exact final SHA above.
The earlier45.734s build was before the last routine-public simplification and is not the final gate.
Fresh complete **unfiltered** native `lean_diagnostic_messages` on Roth/Theta.lean after that
build: success true, partial false, timed_out false, failed_dependencies [], zero errors,
17 inherited warnings. Raw `final-lsp.json`, summary `diagnostic-summary.json`; none of the17
warnings lies in assigned/extracted/min proofs. They concern protected/out-of-scope header,
public hypotheses and section-instance warnings. No warning was hidden or filtered away.

| Gate | Result | Concrete evidence |
|---|---|---|
|lake_build_file|pass|Final actual module command/log/status above.|
|definition_protected|pass|worker.diff has no def/abbrev changes.|
|theorem_statement_protected|pass|Only supported private hr removal/hl weakening, declared structural extraction and routine public proof changes; exact independent private/public/caller adapters verified.|
|structure_gate|pass|assigned7, positive22/no branches, publicmin7; maximum assigned positive continuation4.|
|naming_gate|pass|Descriptive snake_case private aux names; no rename needed.|
|line_packing_gate|pass|Every changed signature line measured above; all rows ok.|
|inequality_orientation_gate|pass|Zero ≥/> in changed signatures.|
|actual_built_axioms|pass|Corrected private, new independent/actual, immutable public/caller logs.|
|cumulative_no_unintended_breakage|pass in leaf scope|Roth.Theta compiled; public+sole routine index_le_lem6 original compatibility recovered; linear sibling byte-identical. Owner full/LeanEval and separate newly extracted helper audit remain required.|
|no_scaffolding|pass|No sorry/newaxioms/native_decide, limit raises, trace or profiling options introduced.|
|lake_build + separate LeanEval|owner pending|Not run/claimed by this leaf for this source.|

Scope-local gates pass; this report does not claim the newly introduced positive helper's
separate audit or the owner's final cumulative project/publication gates are complete.

## Simplify and buzz passes

Simplify performed in-session (standalone simplify tool unavailable): identified long positive
continuation, extracted it; identified redundant public rp=0 case, removed it; replaced public
linarith positivity with direct `le_of_not_ge`; retained all source narratives. No unresolved
scope-local issue. Newly extracted helper awaits its mandatory separate dedicated audit.

Buzz outcome: **FAST-BOARD** for all four measured declarations. Fresh uncontended exact
prefix run99.067s, exit0, after every normal compiler/LSP/search request drained:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-quadratic-helper/final-prefix.lean`

| Declaration | Inherited release ms | Fresh final ms | Budget |
|---|---:|---:|---|
|audited linear estimate|467.473|500.838|<1000|
|new positive quadratic case|n/a|568.967|<1000|
|assigned quadratic wrapper|562.377 before extraction|314.604|<1000|
|public min_le_sum_max|267.293|189.315|<1000|

The two final quadratic declarations total883.571ms; splitting/generalizing does not constitute
a whole-implementation speedup over the old562.377ms helper. It satisfies the structural rule
and keeps each elaboration below budget. No new/sibling incidental overbudget target occurred.
All four are below750ms, so no repeat was required by the repeat threshold.
`profile-status.jsonl` records exit/time/aggregate values. `final-profile.log` preserves raw
UTF8 traces. For each full declaration name above there is
`final-profile-<name>-anchor.txt`, recording its outer Elab.command and associated disjoint
Elab.async proof/addDecl/kernel/linter roots. Their sums are used; nested macro/tactic/kernel
children are not counted twice. Compiler work, where present, is already within those roots.
Final source/prefix correspondence is checked in `evidence-manifest.json`.
maxHeartbeats/maxRecDepth raises added0; removed0; profiling scaffolding added0.
Deferred overbudget declarations within this measured scope: none.

No whole-module profiling pass is claimed: the exact prefix ends after min_le_sum_max and
preserves all preceding imports/source/context. The known later index_le_lem6 instrumentation
heartbeat failure is reserved to original29. No heartbeat limit was raised, and no trace/options
or profiling scaffolding appears in production source.

## Eleven-step phase checklist

- [x] Step1: references read.
- [x] Step2: full24-item substantive audit recorded.
- [x] Step2.5: five actual searches and compiled clean generic routes recorded.
- [x] Step2.6: every effective binder classified/probed; selected supported strengthenings applied.
- [x] Step2.7: every signature line measured in codepoints.
- [x] Step2.8: inequality occurrence table recorded.
- [x] Step3: all42 golfing rules have individual status.
- [x] Step4: independent strategy/whole-proof reflection completed.
- [x] Step5a: complete unfiltered final native diagnostics success, no errors.
- [x] Step5b: focused diff gates recorded, actual final module command cited.
- [x] Step6a: no rename required; no shared queue mutation.

Initial assigned proof25→final7 (-18). Release assigned26→final7 (-19), with new positive22;
combined implementation29 body lines, +3 against release. Routine public min13→7 (-6).
No original count increment or publication is performed by this leaf.

Final freeze: all compiler, native LSP, search and profiler requests are drained. Source edits
are revoked at SHA256`1e01b2a8d662c434a0fe32c58544459dc4a9d5a24065329876eecc341003f685`.
This report is frozen after evidence recording. The owner must assign the new positive case
its separate fresh helper audit, then run full project and separate LeanEval and publication gates.

