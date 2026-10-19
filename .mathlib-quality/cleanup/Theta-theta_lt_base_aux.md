# Dedicated fresh audit: `Roth.theta_lt_base_aux`

This is the sixth introduced-helper audit in original35's unpublished Θ_lt batch. No
original-count credit: counts remain215/264, Theta34/35. Scope is this entire private
helper, its necessary routine Θ caller proof, and this report. No Git/shared log/pin
writes. Artifacts below are under `/private/tmp/theta35-base-fresh/` unless absolute.

## Result and baseline

The private `hrlast` premise is weakened from `3 ≤ (r 0 : ℝ)` to `0 < r 0`, and `hq1`
from `3 / δ ≤ Real.log (q 0)` to `1 < q 0`. These are the exact positivity facts used by
Θ_unique_le. A full original-contract adapter derives both from FIRST's stronger
hypotheses. Independent concrete examples show each weakening is strict. All seven
retained names/order/BinderInfo/universe arity and the conclusion remain unchanged;
all other binder types remain equal. No public signature or definition changes.

The proof shrinks15→10 lines. The single-use term certificates hB and h2 are inlined;
the final linarith is replaced by a direct trans_lt chain through the existing exponent
comparison and lt_mul_of_one_lt_left. Normalization now targets only h1 and the goal,
instead of every local hypothesis. The sole public Θ caller derives positive weight
with an explicit Fin.last0/cast certificate and reuses the existing denominator helper.
Public Θ remains15 proof lines. No additional helper was introduced or deleted.

Baseline: inherited identical6bd complete unfiltered Theta/MainLemma native diagnostics
with0errors and8/3warnings; actual prior51-declaration profile pair base750.668/648.628ms
and direct publicΘ314.428/276.513ms in `/private/tmp/theta35-prefix-lt-fresh/`.
Historical9faa base821.682/1218.493ms failed pair remains preserved at
`/private/tmp/theta35-phi-fresh/actual-profile-complete-{first,second}.*`. It is not
relabeled PASS; the current changed proof requires fresh evidence below. No third
unchanged-source sample is chosen to erase a failed repeat.
Full project/cache/linter-executable baseline and final whole-project/separate LeanEval
are coordinator gates. The scoped affected modules, semantics, natives and timing are
verified here. No whole-file performance pass is inferred.

The Lean4/mathlib-quality skills, full worker workflow and mandatory golfing-rules,
proof-patterns,mathlib-search,generalisation-patterns,cleanup-gates references were read;
relevant style/naming/profiling guidance was consulted. The dispatch's actual Lean4.34
profile command supersedes the reference's obsolete -Dprofiler spelling.

## All24 audit items

| # | Item | Concrete disposition |
|---|---|---|
| 1 | Lint | Inherited same-source complete baseline has no target warning. Fresh unfiltered final diagnostics and every warning are retained below. |
| 2 | Have scan | Original hL/hq/hr derive precisely the new weaker premises and disappear. Original hB is a single-use term with nested by certificates: inline in Θ_unique_le. Original h2 is a single-use by-free Real.rpow_pos_of_pos term: inline at strict multiplier step. Final h/h1 each contain substantive by proofs; retain. The necessary caller hr has a by proof with Fin.last0/cast normalization; retain. No forwarding have survives. |
| 3 | Options | No production limits/options/attributes/scaffolding. Scratch automation lowers heartbeats to10000; default maxErrors unchanged. |
| 4 | Simp | Existing terminal simpa stays unsqueezed. Nonterminal numeric normalization remains norm_num only [pow_one], restricted to h1 and goal; no bare nonterminal simp. |
| 5 | Naming | theta_lt_base_aux describes the strict Theta induction base, snake_case/private _aux; no numeric auxiliary, scheme number or forbidden abbreviation. Retain. |
| 6 | Packing | Every one of three signature lines measured below; next complete binder/conclusion would exceed100. No target proof line exceeds100. |
| 7 | By | All := by attached to prior line; inline certificates likewise attached. |
| 8 | Format | Two-space proof indent, four-space header continuations, one tactic per line, no blank proof lines/semicolon chains. |
| 9 | Comments | No target/caller narrative comments removed; all unrelated source bytes preserved. |
| 10 | Docstring | Private helper has no docstring; public/module documentation untouched. |
| 11 | Visibility | Private substantive base proof, sole production consumer public Θ_lt. No API visibility change. |
| 12 | Structure | Ten proof lines; largest inner subproof four; public Θ15. No conjunction/existential statement, no >10 branch. No extraction/new helper needed. |
| 13 | Mathlib | All five actual methods plus eleven clean anonymous current-goal trials and a separate positive prefix-environment absence assertion. Scalar components used directly; no complete project-Θ match found. Not a one-to-three-Mathlib-call wrapper. |
| 14 | Junk def | n/a: theorem, no definition or custom predicate. |
| 15 | Exists | n/a: no existential statement/witness wrapper. |
| 16 | Show/change | n/a: no such tactic in target. Scratch and caller ascriptions pin cast types, not redundant goal changes. |
| 17 | Negation | n/a: no push_neg/by_contra. |
| 18 | Generalise | All seven effective FIRST/current binders drop-probed, strict-to-weak candidates compiled. Direct positive weight/denominator premises applied with full FIRST adapter. Detailed table below. |
| 19 | Inequality | Five signature occurrences all < or ≤; no ≥/>, no _ge_/_gt_ name. Per-occurrence table below. |
| 20 | Normal form | Established project Θ/rpow bound preserved. Positivity stated directly over natural weights/denominators rather than excessive real numerical thresholds. |
| 21 | Syntactic generality | Θ_unique_le takes the two direct natural positivity premises; the sole caller uses its existing denominator certificate. No bundled artificial predicate. |
| 22 | Import fanout | n/a: imports unchanged. |
| 23 | Casts | Removed original real weight threshold/certificate and hB real annotation. Retained q→ℝ and natural-weight→ℝ crossings in Θ/rpow, plus exponent real annotation; new log positivity proof needs explicit (1:ℝ)<q0 ascription, experimentally load-bearing. Caller bound annotation also needed to pin exact_mod_cast's intermediate type. |
| 24 | Instances | No effective universe/class/decidability binder and no production instance introduced. Exactly seven binders verified from actual type. |

## Five actual Mathlib methods and clean generic routes

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | Roth index theta bound one variable real power small positive delta | Unrelated Behrend/Roth-number results; no target match. |
| B Loogle | Real.rpow, _ ≤ _ ^ _ | Zero items. |
| C LeanSearch | real power exponent decreasing on positive base at most one | Real/NNReal/ENNReal rpow exponent comparison components. |
| D source rg | full theta_lt_base_aux; rpow_le_rpow_of_exponent_ge/rpow_pos_of_pos/one_le_rpow/log_pos_iff | Untruncated full-name search empty; scalar component source locations retained. |
| E local names | Real.rpow_le_rpow_of_exponent (limit10) | Six Real and two NNReal/ENNReal variants; index unavailable, so no indexed-absence inference. |

Remote search indexes can lag the pinned local Mathlib; source and compiled checks are authoritative.
Full native responses are search.json; untruncated source outputs are
mathlib-full-name-search.log/mathlib-source-search.log. Auxiliary _ge'/_le/_le_or_ge/
_of_imp and NNReal/ENNReal variants were examined; Θ is the project's polynomial index
construction, not additive-combinatorial Roth numbers. No discrete/finiteness/separation/
bornology common-equivalent bucket matches. Relevant components are already used directly.
This proof also specializes the project's Θ_unique_le, normalizes its logarithmic quotient,
and combines exponent comparison with a strict multiplier; it is substantive, not a thin
scalar Mathlib wrapper. Retain it. Search is not a general absence proof.

AutomationNegative.lean starts with literal CURRENT production bytes before this target,
then explicitly closes section Lemma7 and namespace Roth. It imports no Roth.Theta.
PrefixAbsence.lean positively checks the ACTUAL environment has neither the audited
private target nor later Root.Θ_lt, and compiles separately with exit0. Provenance hashes,
byte boundary and every anonymous example range are in automation-provenance.json.
final-current-prefix-verification.json additionally rehashes the exact FINAL90e source
prefix and checks equality with the compiled clean context and all eleven literal CURRENT
headers; the prefix bytes are unchanged from setup despite the later target/caller edit.
Every anonymous example uses the literal CURRENT seven-binder signature; there is no
named failed target to contaminate exact?/apply?. All eleven BEGIN/END markers and each
trial's actual compiler result are checked in automation-results.json. Conservative
scratch10000-heartbeat bound is lower than default; maxErrors is unchanged. No unbounded
native multi_attempt was repeated. Expected-exit1 searches do not certify axioms.

## Every effective binder and generality

Binder-old-{0,1}.lean and Binder-current-{0,1}.lean independently remove every binder
with autoImplicit=false. WeakenNegative.lean additionally tests strict/weak natural/real
premises. Raw logs/statuses and all source/error ranges are retained in binder-ranges.json
and binder-results.json. Proof substitution failure is not a logical indispensability proof.

| Binder | Class | Actual use | Compiled candidates and disposition |
|---|---|---|---|
| δ | implicit ℝ | rpow exponent/base and comparison | FIRST/current individual drop fails in dependent statement. Keep ℝ: Θ/Real.log/Real.rpow are fixed. |
| hδ0 | explicit proposition | Real.rpow_pos_of_pos and exponent order | FIRST/current drop; current0<δ→0≤δ both fail. Strict bound cannot cover δ=0 with strict zero RHS. |
| hδ | explicit proposition | exponent comparison on base≤1 | FIRST/current drop fails. Keep canonical small-δ regime; extending the numerical regime would replace the mathematical bound proof, not a mechanical parent weakening. |
| r | implicit Fin1→ℕ | Θ weights and exponent | FIRST/current individual drop fails. Natural multiplicities are established Θ domain; no field/typeclass weakening. |
| q | implicit Fin1→ℕ | Θ denominators and rpow | FIRST/current individual drop fails. Preserve denominator domain. |
| hrlast | explicit proposition | positive weight for Θ_unique_le | FIRST/current drop fails; FIRST3≤cast→current0<r0 full proof compiles; current0≤r0 substitution fails. APPLY supported direct-positive weakening. |
| hq1 | explicit proposition | base>1 and log nonzero | FIRST/current drop fails; FIRST3/δ≤log→current1<q0 full proof compiles; current0<q0 substitution fails. APPLY direct-denominator weakening. |

No hidden section instances/universes. FirstIndependent.lean contains exact full immutable
batch2 context/proof, without added section/omit/class/universe changes. Concrete positive
examples (weight1,denominator2 atδ1) witness strictness of the two weakenings. The old full
telescope adapter derives original positivity facts explicitly; all public premises,
including user-protected unused MainLemma assumptions, remain intact.

Literature: n/a, private auxiliary explicitly exempt under cleanup§2.6d. Mechanical and
mathematical generality still examined. Inversion: Θ is never unfolded; Θ_unique_le is
its existing abstract singleton API. After that application the argument is scalar log/rpow
arithmetic; replacing Θ by an arbitrary function would merely assume that same project
singleton estimate, yielding no supported reusable abstraction. Fin1 is the base dimension
of this induction, not a concrete witness forgotten after unfolding. No further inversion
or general-field restatement is recommended. No public API preference remains unresolved.

## All42 golfing rules

| Rule | Concrete disposition |
|---|---|
| 1.1 | n/a: no by exact wrapper. |
| 1.2 | n/a: no by rfl wrapper. |
| 1.3 | n/a: rw log normalization followed by field_simp, not rw/exact. |
| 1.4 | Existing terminal exponent comparison uses simpa using directly. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor chain. |
| 1.7 | Sole caller apply/normalization/exact is replaced by exact existing certificates. |
| 1.8 | n/a: no contradiction/negation branch. |
| 1.9 | n/a: target has no lambda. |
| 1.10 | APPLIED: inline by-free hB/h2; hL/hq/hr disappear under weaker premises. Final h/h1 have actual by proofs; keep. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no redundant show tactic. |
| 1.13 | n/a: no conjunction projection have. |
| 1.14 | Already single combined rw; no sequential pair. |
| 1.15 | n/a: target has no terminal simp only; terminal simpa already unsqueezed. |
| 1.16 | No bare nonterminal simp. Restricted norm_num only normalizes pow_one only where needed. |
| 1.17 | APPLIED: h.trans_lt/h1.trans_lt replace terminal linear arithmetic. Existing .trans_eq retained. |
| 1.18 | Nested certificates delimit arguments before further arguments/.trans; keep necessary parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not a trivial existential. |
| 2.1 | Actual clean anonymous whole-goal grind tried, result below. |
| 2.2 | n/a: no production grind/preliminary grind tactics. |
| 2.3 | Existing simpa exponent consolidation retained; no separate simp/exact sequence. |
| 2.4 | n/a: no regularity/function-property goal. |
| 2.5 | Existing rpow exponent/base positivity remains by positivity; whole-goal trial recorded. |
| 2.6 | Whole-goal gcongr tried; explicit strict multiplier composition expresses final comparison directly. |
| 2.7 | Whole-goal lia tried; target is real rpow/Θ, not Nat linear arithmetic. |
| 2.8 | Whole-goal aesop tried; no production broad search. |
| 2.9 | Whole-goal norm_num tried; concrete exponent1/2≤1 and1<10 use norm_num, cast bridge uses exact_mod_cast. |
| 2.10 | Whole-goal decide tried; no native_decide. |
| 2.11 | Whole-goal field_simp/ring tried; selected quotient identity closes with field_simp using explicit log nonzero. |
| 2.12 | n/a: no selected ring/ring_nf-ending proof with hypotheses. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | APPLIED equivalent term composition: h≤δ≤δ^half<10δ^half directly uses trans_lt rather than terminal arithmetic. |
| 2.15 | n/a: no parallel uniform subgoals in selected proof. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy regularity tactics. |
| 3.3 | n/a: no omega; lia trial covered2.7. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No automation attribute: private seven-premise base bound with one explicit consumer. |
| 3.6 | Whole-goal simp_all tried, no selected squeezed simp_all. |
| 3.7 | Zero production limits/options added/raised; no shipped scaffolding. |

Step-back/holistic simplify: the mathematical proof is singleton Θ≤δ, the small-base
power comparison δ≤sqrtδ, and sqrtδ<10sqrtδ. Direct premises/certificate composition make
that structure explicit and remove unnecessary threshold calculations from the helper.
No builtin simplify callable is available; the holistic pass is performed directly.
No duplication, new helper, rename or further refactoring recommended. All static HAVE,
packing, inequality, generality and golfing decisions completed before final gates.

## Measured signature packing and inequality orientation

| Signature line | Width | Next complete constituent width | Arithmetic | Action |
|---|---|---|---|---|
| 1 | 84 | 18 | 84+1+18=103>100 | ok |
| 2 | 40 | 70 | 40+1+70=111>100 | ok |
| 3 | 72 | — | last line | ok |

Actual effective-type printing at format.width100 is retained in both final semantic logs.

| Occurrence | Signature line:column | Relation | Action |
|---|---|---|---|
| 1 | 1:50 | < | unchanged; smaller-side-left |
| 2 | 1:63 | ≤ | unchanged; smaller-side-left |
| 3 | 2:17 | < | unchanged; smaller-side-left |
| 4 | 2:33 | < | unchanged; smaller-side-left |
| 5 | 3:35 | < | unchanged; smaller-side-left |

| Clean current-goal strategy | Observed result |
|---|---|
| grind | `grind` failed |
| aesop | unsolved goals |
| exact? | `exact?` could not close the goal. Try `apply?` to see partial suggestions. |
| apply? | (deterministic) timeout at `whnf`, maximum number of heartbeats (10000) has been reached |
| simp_all | unsolved goals |
| gcongr | `gcongr` did not make progress. |
| positivity | not a positivity goal |
| norm_num | unsolved goals |
| lia | `grind` failed |
| decide | Expected type must not contain free variables |
| field_simp/ring | unsolved goals |

All eleven BEGIN/END markers were reached, with no raised error cap. apply?'s bounded
internal whnf timeout is reported at1:1 by Lean, and attributed by its own BEGIN/END
markers; its actual partial suggestions do not close the goal. No target/self suggestion
is used. The separate prefix absence compile exits0. All17 drop/weakening trials have
actual errors in their recorded source ranges. An initial parser missed Lean's
error(lean.unknownIdentifier) spelling; the corrected analyzer recognizes both spellings
and verifies every row, without repeating/changing any proof experiment.

## Immutable FIRST and actual built semantic gates

FirstIndependent.lean begins with the ENTIRE exact immutable FIRST batch2 bytes, including
all original declarations before/after the target, original import/namespace, and the old
15-line base proof. No extra section, omit, universe or class binder is inserted. The
original proof is re-elaborated independently and rejects any actual-target/adapter/
expected-current self dependency. All three FIRST batch texts and original success
log/status retain their hashes; first-immutability-{before,final}.json records them.

An explicit old seven-binder adapter derives positive weight and denominator from FIRST's
exact strong hypotheses, then applies the current helper. Meta compares original↔adapter
and expected-current↔actual-current full telescopes and conclusion, including all names,
BinderInfo/order/universe arity. A direct original↔actual comparison verifies all retained
metadata and every other binder type, with exactly two explicit weakening rows. Independent
strictness examples compile. Original/adapter/independent-current/actual opaque value!true
inferred types and axioms are checked; only propext, Classical.choice, Quot.sound occur.

ActualSemanticsAugmented.lean preserves the ENTIRE verified preceding semantic scaffold
as an exact byte prefix (semantic-provenance.json). It appends the complete FIRST batch2
body in Roth.BaseFreshFirstContext (namespace renamed only to avoid existing probe names;
its already-loaded import omitted), then the base-specific checks. The separate
FirstIndependent.lean retains the exact original import/namespace/context; the renamed
copy inverse-reconstructs the complete original body byte-for-byte. Provenance is
semantic-FIRST-context-integration.json.
The original Index72cf and Theta355a blocks, ENTIRE immutable original2b MainLemma proof,
and ENTIRE independent CURRENT MainLemma proof remain byte-identical at all four recorded
UTF8 ranges/hashes in immutable-complete-blocks.json. It retains all preceding180 gates:
exact immutable old Θ adapter; publicΘ9/scaled13/FIRST15/δ3/minimum-prefix18; all26 Main
ordinary binder names/order/BinderInfo/types/conclusion including hq0,hq1,h32,h33; actual
RootΘ/main_lemma opaque values/standard axioms and positive main→RootΘ dependency; no
Root.main_lemma/private Root Main self-use in the independent old/current proofs.
The precise old Antitone-prefix adapter/current minimum-prefix contract is retained,
rather than reinstating the superseded raw equality. Deleted prefix-log seven-binder
replacement/actual constant/reference absence and deleted fin-option absence remain.
The retained inventory is51, with nine retained plus two introduced/deleted helper
obligations; all eleven fresh audits remain required.

Both affected modules rebuild BEFORE the actual Root queries. First-independent-final
exits0 with29 clean PASS markers; actual-semantics-final exits0 with209 clean PASS markers.
The complete marker lists are semantic-marker-summary-final.json. No PANIC, error,
sorryAx or nonstandard axiom is accepted. These are independent proof/value/contract
checks, not source-header equality alone.

## Fresh verification and actual source performance

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file Roth.Theta | PASS | build-theta-final.json/.log: /Users/ramin/.elan/bin/lake build Roth.Theta, exit0, 5.654s |
| lake_build_file Roth.MainLemma | PASS | build-mainlemma-final.json/.log: /Users/ramin/.elan/bin/lake build Roth.MainLemma, exit0, 36.902s |
| Independent complete FIRST proof and full old adapter | PASS | first-independent-final.json/.log: /Users/ramin/.elan/bin/lake env lean /private/tmp/theta35-base-fresh/FirstIndependent.lean, exit0, 37.778s |
| Entire old/current caller semantics and actual values/axes | PASS | actual-semantics-final.json/.log: /Users/ramin/.elan/bin/lake env lean /private/tmp/theta35-base-fresh/ActualSemanticsAugmented.lean, exit0, 109.340s |
| definition_protected | PASS | No def/abbrev/import bytes changed. |
| theorem_statement_protected | PASS with supported private weakening | Only two private premises weaken; exact FIRST adapter recovers old contract; every public header byte-identical. |
| structure_gate | PASS | Base10 lines, subproof≤4; publicΘ15, no >10 branch. |
| naming_gate | PASS | Descriptive base strict-bound/private _aux; no forbidden pattern. |
| line_packing_gate | PASS | Every three signature lines measured above; no repack row. |
| inequality_orientation_gate | PASS | Every five occurrence measured; zero reversed relation. |
| cumulative scoped callers | PASS | Both affected module builds, complete independent old/current caller proofs, fresh unfiltered diagnostics. |
| whole project and separate LeanEval | OWNER PENDING | Not run/claimed by this scoped worker. |
| whole-file performance | NOT CLAIMED | Separate mandatory repair queue persists; MainLemma actual caller timing remains unmeasured. |

scoped-source-reconstruction.json and owned-proof.diff establish exact target plus sole
public proof changes; every other source byte, definition, public statement, narrative
comment, import and pin is unchanged. Target proof15→10; full file1012→1009 lines.
The newly used external lt_mul_of_one_lt_left is positively #checked; existing scalar
identifiers are compiled in the selected independent proof. No new helper or rename.

Fresh complete UNFILTERED native diagnostics:

| Module | Success | Partial | Timed out | Errors | Warnings |
|---|---|---|---|---|---|
| theta | True | False | False | 0 | 8 |
| mainlemma | True | False | False | 0 | 3 |

Every warning is retained in the raw native JSON and listed here:

| Module | Line | Severity | Message |
|---|---|---|---|
| theta | 1 | warning | * `-/`: Copyright too short!   Note: This linter can be disabled with `set_option linter.style.header false` |
| theta | 93 | warning | Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| theta | 101 | warning | Variable name `hB` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hB  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| theta | 101 | warning | Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| theta | 109 | warning | Variable name `hB` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hB  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| theta | 129 | warning | Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| theta | 252 | warning | Variable name `hr` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| theta | 547 | warning | Variable name `hq` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hq  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| mainlemma | 1 | warning | * `-/`: Copyright too short!   Note: This linter can be disabled with `set_option linter.style.header false` |
| mainlemma | 149 | warning | Variable name `hδ0` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hδ0  Note: This linter can be disabled with `set_option linter.unusedVariables false` |
| mainlemma | 149 | warning | Variable name `hr₁` is not explicitly referenced.  Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:   [apply] _hr₁  Note: This linter can be disabled with `set_option linter.unusedVariables false` |

All normal/native requests drain before real profiling, with own process/process-group
liveness assertions and pending[] in pre-final-{first,repeat}-drain.json. The actual
command is `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0
Roth/Theta.lean`. The420s capture window is external; no Lean limit/heartbeat is changed.
Both complete actual whole-source captures/statuses and all51 declaration anchors are
preserved. Strict UTF8 slices retain exact raw bytes/offsets/hashes. Only disjoint outer
command plus associated async proof/addDecl/linter rows are summed; nested macro/kernel
rows are excluded. No diagnostic candidate timing is passed off as production timing,
and no third same-source sample is selected.

| Fresh run | Declaration | Conservative ms | Actual proof anchors |
|---|---|---|---|
| final-first | theta_lt_base_aux | 439.154 | 1 |
| final-first | Θ_lt | 258.708 | 1 |
| final-repeat | theta_lt_base_aux | 429.741 | 1 |
| final-repeat | Θ_lt | 275.71 | 1 |

The historical9faa failed base repeat1218.493ms remains preserved; the10-line current
proof and weaker contract are a real source change, with the fresh pair above supplying
its disposition. The inherited6bd750.668/648.628ms pair remains baseline evidence only.
The separate unrelated actual whole-source queue in sum_max_sub_le_index_det,
index_separated_mul_le_aux,index_det_le,index_numeric_bound_aux,index_le_lem6,lem7_Φ_bound,
lem7_numeric, and the earlier positive-quadratic helper remains coordinator-owned, as do
pending successor/large-delta failed pairs. All fresh outside-scope over-budget rows in
both whole-source captures are explicitly retained in outside-scope-overbudget.json. None was edited or silently declared fixed.
MainLemma's earlier180s cutoff stopped before main_lemma: build/semantic/native success
does not invent a finite caller timing. Whole-file performance PASS is not claimed.

The first combined semantic scaffold lacked a declaration for the independently copied
FIRST base (the preceding scaffold covered the prefix helper). That scratch integration
failed cleanly and is archived as superseded-missing-first-base.*. The complete FIRST
batch2 copy fixes it; no production source changed for this correction.
Earlier unsuccessful base candidates (missing log nonzero/type ascriptions), two failed
routine caller cast candidates, and all raw/status evidence remain preserved. They are
not positive evidence. The successful selected candidate, final-source affected module
builds and complete semantic/native gates supersede them; no production limits were
raised and no helper/scaffolding introduced. The normal/live compiler window is exclusive.

## Simplify/refactoring/buzz and all11 workflow steps

Simplify: direct holistic review completed (no builtin simplify tool available). Applied
the two supported premise weakenings, hB/h2 inlining, and explicit final inequality
composition; no further issue or additional helper recommended. Phase5a scoped
refactoring is complete with old adapter; Phase5b has no rename, no shared queue write.
Buzz: scoped base/direct public consumer pass both fresh final-source runs above.
Zero maxHeartbeats/other limit raises, zero native_decide, zero shipped scaffolding.
Whole-file/full-project/frozen separate LeanEval remain owner gates.

| Step | Result |
|---|---|
| 1 | ✓ — Required skills/workflow/references read. |
| 2 | ✓ — All24 concrete audit items. |
| 2.5 | ✓ — Five actual methods, eleven exact-current-prefix anonymous trials, separate exit0 environment absence assertion. |
| 2.6 | ✓ — Every seven FIRST/current binder drop; three strict/weak candidates; two supported weakenings/full FIRST adapter; private literature exemption/inversion. |
| 2.7 | ✓ — Every signature line measured/packed. |
| 2.8 | ✓ — Every inequality occurrence scanned. |
| 3 | ✓ — All42 rule dispositions. |
| 4 | ✓ — Step-back/holistic simplify review. |
| 5a | ✓ — Fresh complete unfiltered native diagnostics0errors. |
| 5b | ✓ — Scoped source/module/entire semantic/value/axiom/performance gates. |
| 6a | ✓ — No rename; no shared queue mutation. |

## Exact freeze and handoff

| Source | SHA256 |
|---|---|
| Roth/Theta.lean | 90e20c66da0b65ebbb5275e8a86387d9508dde654afaadbc0f26416a1a1f4941 |
| Roth/MainLemma.lean | ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4 |
| Roth/Main.lean | f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069 |

All FIRST hashes unchanged; all four complete immutable semantic blocks retained. No new
helper; no deleted helper in this audit. Nine retained/two introduced-deleted obligations
remain eleven; retained inventory51; no original-count increment or original35 publication.
Source edit authority is explicitly revoked. Scratch/report/compiler/native authority is
also released after final freeze. All own normal/native requests drained; pending[].
final-process-drain.json and final-freeze.json retain exact source/artifact hashes and
release state. Owner must complete remaining dedicated audits and cumulative29/all actual
values/axioms/final profiles/full build THEN separate frozen LeanEval before publication.
This report claims only the scoped base-helper checkpoint.
