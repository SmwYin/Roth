# theta_phi_lt_aux — fresh dedicated introduced-helper audit

Status: dedicated phi audit and scoped performance repair COMPLETE. The whole35 batch remains
unaccepted pending the other ten helper audits and owner gates. No original-declaration count credit.
Scope is the private Φ estimate and necessary routine proof calls only. All artifacts below
are under `/private/tmp/theta35-phi-fresh/` unless an absolute path is given.

## Baseline, mathematics and ownership

Inherited exact baseline: Theta `0cb111c95cb755ec1e80a5a39ac4c1a35ad0460dfd3c75988be0fd89e4ed7118`;
MainLemma `ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4`.
The matching complete native baseline is the owner's `final-native-{theta,mainlemma}-final.json`;
0 errors, 8/3 existing warnings. The owner's previous full build is inherited, not rerun here.
Fresh module builds, independent proofs, complete native diagnostics and actual profiles are
required below. Cache downloads and whole-project/LeanEval gates belong to the owner.

The helper bounds the two parts of Lemma 6's Φ at every permitted integer scale l.
It proves positivity of all weights and q₀>1, puts M between 1 and q₀ raised to the
enlarged exponent ε=δ(1+1/(n+2)), applies the one-variable and prefix estimates,
and combines their sum with the previously separated scalar square-root estimate.
It is substantive induction assembly, not a wrapper around 1–3 Mathlib facts.

Read the lean4 and mathlib-quality skills, the cleanup worker workflow, golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style, naming and
profiling references. The dispatched 30/10-line limits and protected public contracts
override broader default limits. No Git, shared logs, rename queue or unrelated declarations edited.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | Lint | Inherited baseline has no target warning; final unfiltered native gate recorded below. Existing public warnings remain protected. |
| 2 | Have scan | Inventory below; inline all six pure single-use forwarding facts. Keep substantive cast proofs and facts used at least twice. |
| 3 | Options | No target option/limit; add none. Scratch automation uses a lower 10000-heartbeat budget only. |
| 4 | Simp squeeze | Keep `dsimp only` and nonterminal `simp only` on hb. Squeeze both costly terminal hM cast conversions for measured performance; this is the profiling reference's explicit terminal-simp exception. |
| 5 | Naming | `theta_phi_lt_aux` states the Φ upper bound, snake_case, private `_aux`; no forbidden abbreviation, numbered scheme or _ge_/_gt_. No rename. |
| 6 | Packing | Measure all 17 signature lines below; move the complete `{l : ℕ}` binder onto the preceding line. Mathematical telescope unchanged. |
| 7 | By placement | `:= by` ends the conclusion line. |
| 8 | Format | Two-space tactics, no blank proof lines, no semicolon chains, no haveI/letI, maximum owned line width 93 codepoints. |
| 9 | Comments | Preserve/re-anchor 3/3: combine, one-variable term, lower-dimensional induction. None deleted. |
| 10 | Docstring | Private helper has no docstring; preserve surrounding public documentation. |
| 11 | Visibility | Already private and used by the successor estimate in this file; retain. |
| 12 | Structure | 30 nonblank noncomment proof lines before/after; longest local by proof 5 lines; no explicit case branch or conjunction conclusion. Composed final subexpression 9 lines including its comments. No new helper needed. |
| 13 | Mathlib | Five actual search methods and uncontaminated compiled generic routes below. No full replacement identified; no absolute absence claim. |
| 14 | Junk def | n/a: theorem, no data definition. M/ε are local mathematical abbreviations used repeatedly. |
| 15 | Exists | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | No `show` or `change` occurrence. |
| 17 | Push negation | No `push_neg`, contradiction or negation transformation. |
| 18 | Generalise | All 15 effective parameters drop-tested, four applicable weakenings compiled. No class/universe weakening is available on the fixed Nat/Real Θ construction. Preserve full current/FIRST contract. |
| 19 | Inequality | Zero reversed ≥/> in code; per-occurrence empty scan below. |
| 20 | Normal form | Natural weights and denominators, multiplicative weak ratios, real rpow/log/sqrt; retain canonical project form, no pairwise equivalence API. |
| 21 | Syntax generality | Φ is a let-bound sum and the IH is the adjacent helper's bounded form. No additional bundle eases this sole caller. Unrestricted IH is a stronger premise, not a weakening. |
| 22 | Import fanout | n/a: no new import. MainLemma's source is byte-identical to baseline. |
| 23 | Casts | No casts added/dropped in the diff. Nat-to-Real coercions and `(0 : ℝ)` fix genuinely different source/target types. Explicit `Nat.cast_nonneg` replaces positivity inference. |
| 24 | Instance names | n/a: no instance declaration, binder or local instance introduced. |

## Have inventory and simplification

Counts are identifier uses after each binding within the owned proof; the hb rewrite is a use.

| Have | Original uses | Proof content | Action |
|---|---:|---|---|
| hlr | 1 | pure order composition | inline into lem6M_lt |
| hr0 | 2 | function with cast proof | keep |
| h (inside hr0) | 1 | contains exact_mod_cast subproof | keep substantive cast proof |
| hq | 2 | denominator estimate with cast proof | keep |
| hε0 | 2 | originally positivity | replace with `mul_pos hδ0 (add_pos zero_lt_one (hδ0.trans_le hδ))` |
| hδε | 1 | order composition | inline; replace denominator positivity search by `(hδ0.trans_le hδ).le` |
| hB | 1 | rpow nonnegativity | inline into hM1; use `mul_nonneg hδ0.le (Nat.cast_nonneg _)` |
| hM1 | 2 | named common bound | keep |
| hp | 2 | exact Nat successor terms | keep |
| hM | 2 | substantive lem6M_lt/cast proof | keep, squeeze both cast conversions |
| hΘ1 | 1 | forwarding application | inline under its preserved signpost |
| hΘ2 | 1 | forwarding application | inline under its preserved signpost |
| hb | 2 | numeric bound, then cast normalization | keep |
| hΦ | 1 | pure inequality composition | inline in final numeric application |

## Five actual Mathlib searches and compiled automation

`search.json` preserves raw native responses. All methods actually ran:

| Method | Query | Outcome |
|---|---|---|
| A Lean-Finder | Roth lemma theta lattice point counting Phi bound square root dimension induction | 5 additive-combinatorial Roth-number facts; different mathematical object |
| B Loogle | `Real.sqrt, _ + _ + _ < _` | no results |
| C LeanSearch | Roth lemma weighted lattice point count induction estimate theta square root | Behrend/Roth numbers, asymptotic Theta, Z-lattice counting; none matches polynomial-index Θ |
| D full source rg | theta_phi_lt_aux / Θ / Roth / lem6M in Mathlib NumberTheory and real powers | unrelated Jacobi theta, asymptotics and Liouville reference; no target wrapper hit; output untruncated |
| E name pattern | `theta`, limit 50 | positive Chebyshev/OrderType/project names; index unavailable, so no absence inference from empty/missing hits |

Auxiliary/normal-form variants examined: real sqrt sum estimates, Θ/polynomial-index versus
asymptotic Theta, prefix/scaled one-variable bounds. The common-equivalents table's discrete,
finiteness, separation and bornology entries do not match this theorem.

`AutomationNegative.lean` ends before the audited target in an exact source prefix, so
neither an imported target nor named failed target declaration can contaminate search.
Anonymous whole-goal trials: grind failed; aesop failed internally in simp; exact? failed;
apply? hit the deliberately lower 10000-heartbeat budget; positivity reported not a
positivity goal; norm_num left goals; gcongr made no progress. Raw `automation-negative.log`
and status preserve these bounded failures. No tactic failure certifies absolute absence.
The selected proof uses the existing specialized estimates plus Mathlib order/rpow/cast
APIs directly. There is no missing wrapper/coercion API requiring a new public lemma.

## Generalisation, effective binders and inversion

`BinderNegative.lean` and `BinderNegativeTail.lean` contain actual elaborated drop/weakening
trials with autoImplicit=false. `binder-results-final.json` maps every parameter to its
diagnostic. Initial batching reached the default maxErrors before all trailing trials;
the tail was rerun separately without changing any limit. Two exploratory scratch files
initially omitted the open `Lemma7` closing command; their failed raw logs are retained.
The corrected candidate exits 0; corrected negative tail closes both Lemma7 and Roth and
has only the intended probe failures. Negative logs are not positive semantic evidence.

| Parameter | Role / actual use | Compiled mechanical trial | Result |
|---|---|---|---|
| n | Fin dimension and power exponents | drop | unknown dimension in dependent telescope |
| δ | real scale in bounds/conclusion | drop | unknown scale in telescope |
| hδ0 | strict lem6M/denominator/IH positivity | drop; 0≤δ | missing proof; strict application mismatch on weakened premise |
| hδ | upper bound at induction enlargement | drop | missing bound in epsilon order terms and theta_delta_succ_lt_aux |
| hδ1 | strict weight decrease and numeric bound | drop; δ≤1 | missing strict proof; theta_last_lt_first_aux needs δ<1 |
| r | natural weights defining Θ | drop | dependent statement fails |
| q | natural denominators defining Θ | drop | dependent statement fails |
| hanti | every weight positive and prefix restriction | drop | missing Antitone evidence at three applications |
| hrlast | lower weight bound | drop; 3≤last to 2≤last | missing premise; specialized denominator/prefix estimates need 3 |
| hratio | adjacent multiplicative comparisons | drop | missing premise at last/denominator/prefix calls |
| hq1 | logarithm lower bound | drop | missing premise for denominator/lem6M/prefix estimates |
| hqr | all balanced logarithms | drop | missing premise in denominator/unique/prefix estimates |
| ih | all smaller-dimensional input sequences | drop | missing induction proof |
| l | natural scale in Φ/M | drop | dependent result fails |
| hl | permitted positive scale range | drop; Icc 1 to Icc 0 | missing membership; positive-scale application mismatch |

No effective typeclass or universe parameter is hidden by the surrounding section: final
actual metadata and the explicit immutable FIRST adapter check the entire 15-binder
telescope, ordinary names, BinderInfo, order, universe arity and conclusion.

Point-localisation of Antitone cannot retain this proof's all-index positivity and prefix
restriction with a proper smaller domain. Generalising Nat/Real would restate Θ/lem6M/log/rpow,
not merely weaken a typeclass. Replacing the bounded IH by unrestricted IH would strengthen
the premise and require independent recovery for all affected helpers; no such redesign is
recommended here. Retaining the adjacent-helper contract avoids an unsupported API change.

Literature search: n/a, private auxiliary declaration. Cleanup §2.6d explicitly exempts
private/aux declarations; all mechanical mathematical checks above still run.
Inversion check: lem6M's bound and the two specific Θ contributions remain essential
throughout the proof; they do not disappear after one unfolding. The generic scalar
square-root combination is already a separate `lem7_numeric` estimate. No further
abstract-witness theorem with demonstrated reuse is identified.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: none |
| 1.3 rw/exact | n/a: no consecutive rw/exact |
| 1.4 simp/exact | already uses simpa using for casts; retain |
| 1.5 trailing rfl | n/a: none |
| 1.6 anonymous constructor | n/a: no constructor proof |
| 1.7 apply/exact | final applications compose through .2 and lem7_numeric; partial apply goals are informative expected types, not one-argument forwarding |
| 1.8 by_contra | n/a: no contradiction |
| 1.9 eta reduction | hr0 lambda has cast proof; Θ's constant/Fin lambdas change indexing, cannot eta-reduce |
| 1.10 one-use have | applied to all six pure forwarding facts, inventory above |
| 1.11 refine/fun | n/a: no apply/intro |
| 1.12 show | n/a: none |
| 1.13 projections | Icc membership already obtained by destructuring |
| 1.14 merge rw | n/a: no rw |
| 1.15 terminal simp | measured terminal-squeeze exception for hM; no unrelated terminal squeeze introduced |
| 1.16 nonterminal simp | hb already squeezed; dsimp only explicit |
| 1.17 dot notation | use .trans, .trans_le, .le, .2 consistently |
| 1.18 <\| | parenthesized subexpressions have following arguments/compose inside a larger expression; <\| does not improve grouping |
| 1.19 push Not | n/a: none |
| 1.20 existential inline | n/a: no existential helper |
| 2.1 grind | actual clean-prefix whole-proof failure |
| 2.2 before grind | n/a: selected proof has no grind |
| 2.3 simpa consolidation | existing direct lem6M/cast conversion retained and narrowed |
| 2.4 fun_prop | n/a: no function-property goal |
| 2.5 positivity | existing success replaced by exact terms at measured hotspots; whole-goal trial is not a positivity goal |
| 2.6 gcongr | actual whole-goal no-progress result; no bare congruence chain remains |
| 2.7 lia/omega | hp/hlr already exact Nat terms, no integer arithmetic tactic remains |
| 2.8 aesop | actual clean-prefix failure |
| 2.9 norm_num/cast | retain norm_num for 0<2 and 0<3, exact_mod_cast for genuine Nat/Real bridges; whole-goal norm_num leaves goals |
| 2.10 decide | n/a: arbitrary real inequalities and IH are not finite computation |
| 2.11 field_simp/ring | n/a: no algebraic denominator equality |
| 2.12 linear_combination | n/a: no ending ring/ring_nf or polynomial identity |
| 2.13 wlog | n/a: no symmetric case split |
| 2.14 collapse calc | pure order compositions are term mode; no calc remains |
| 2.15 <;> | n/a: no parallel similar goals |
| 3.1 erw | n/a: none |
| 3.2 legacy function tactics | n/a: none |
| 3.3 omega/lia | no omega or lia remains; explicit Nat terms preferred for this measured target |
| 3.4 rcases/rfl | n/a: no equality substitution |
| 3.5 attributes | private specialized IH assembly is not an automation rule; no global attribute added |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 limits | no production limit or profiler option added/raised |

Step-back reflection: the clean-prefix automation/search trials cannot close this analytic
induction assembly. The proof's real content is its two specialized Θ estimates plus the
already extracted numeric bound. The chosen exact order/cast terms preserve that outline
and avoid expensive general simplification/positivity search. Further monolithic automation
or a new helper would obscure the same argument without demonstrated reuse.

## Packing and inequality artifacts

All widths are Unicode codepoints. A complete logical antecedent is the atomic item inside
the multi-line IH; split subterms of an antecedent are not independent binders.
The actual width-100 effective type is printed by `FirstIndependent.lean`.

| Signature line | Width | Next complete atomic item width | Arithmetic | Action |
|---|---:|---:|---|---|
| 877 | 93 | 13 | 93+1+13=107>100 | ok |
| 878 | 62 | 41 | 62+1+41=104>100 | ok |
| 879 | 45 | 63 | 45+1+63=109>100 | ok |
| 880 | 67 | 76 | 67+1+76=144>100 | ok |
| 881 | 80 | 62 | 80+1+62=143>100 | ok |
| 882 | 66 | 48 (first IH clause) | 66+1+48=115>100 | ok |
| 883 | 52 | 53 (quantified first premise) | 52+1+53=106>100 | ok |
| 884 | 59 | 52 (ratio antecedent with arrow) | 59+1+52=112>100 | ok |
| 885 | 56 | 64 (log antecedent) | 56+1+64=121>100 | ok |
| 886 | 68 | 60 (balanced-log antecedent) | 68+1+60=129>100 | ok |
| 887 | 64 | 75 (IH result and close) | 64+1+75=140>100 | ok |
| 888 | 89 | 52 (hl binder and result colon) | 89+1+52=142>100 | ok |
| 889 | 56 | 54 (M let) | 56+1+54=111>100 | ok |
| 890 | 58 | 87 (first Φ summand) | 58+1+87=146>100 | ok |
| 891 | 91 | 67 (second Φ summand) | 91+1+67=159>100 | ok |
| 892 | 73 | 68 (result through := by) | 73+1+68=142>100 | ok |
| 893 | 72 | no next signature item | n/a | ok |

| Reverse inequality occurrence | Location | Rewrite | Rename |
|---|---|---|---|
| none | entire signature, all hypotheses and result | zero ≥/>; no change | no _ge_/_gt_ name |

## Simplify, performance, semantic and native gates

Dedicated holistic simplify review applied the six one-use inlinings, retained meaningful
common bounds, and re-anchored comments. No separate callable built-in simplify tool exists
in this environment; the owner's fresh independent filewide simplify remains an owner gate.
Dedicated buzz diagnosis identified broad hM simpa (253.025ms), hB positivity/casts (106.918ms)
and hε0 positivity (84.372ms) in the failed exact-0cb trace. The previous required pair
988.865/1013.946ms remains preserved and failed; it is not cured by a third same-source sample.

Final source snapshot is Theta `9faa85d31dce678483027d1580c79d4a8ad220636806af1040ecc5da53738d94`;
MainLemma remains `ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4`.
`source-inventory.json` verifies only the owned declaration changed, its signature changed
only in whitespace, proof length is 30, maximum width 93, and no helper was introduced.
`packing-inequality.json` records actual widths and 10 ≤ / 5 < / 0 reversed occurrences.

`lake build Roth.Theta` exited 0 in 31.239s (`build-theta-final.log/.json`), followed by
`lake build Roth.MainLemma` exit 0 in 38.368s (`build-mainlemma-final.log/.json`).

`FirstIndependent.lean` begins with the entire byte-identical FIRST batch2 source;
its immutable prefix SHA is `8a7cb0fd8b366f0f251272bf6e9a16cfa2dc339b9147899b74f876d37c1b54a6`.
It independently re-elaborates that original proof in the exact namespace/no-section/no-class
context, locates the actual private module-mangled constant by its exact suffix, and supplies
an explicit original-telescope adapter. Corrected final run exited 0 in 46.929s:
`first-independent-corrected.log/.json`. All 15 retained ordinary names, BinderInfo, order,
argument types, universe arity and conclusion match both current helper and adapter.
The FIRST/current/adapter opaque values use `value! true`, infer at their actual types and
have only propext, Classical.choice, Quot.sound. The independent FIRST constant inventory
contains no Root phi or Root Θ_lt self-use. An initial scratch adapter accidentally supplied
the unapplied constant; the verifier rejected its sorryAx. The failed raw log is retained
as `first-independent-final.log`; only the corrected clean run certifies the adapter.

`first-immutability.json` records all three original FIRST files and original success
logs/statuses without changing them. `immutable-original-blocks.json` verifies the literal
original Index/Theta blocks at the inherited exact byte offsets, SHA72cfbff9…/355a5330…;
the entire semantic scaffold remains byte-identical, SHA42f1d44c… .

New external identifiers `mul_pos`, `add_pos`, `zero_lt_one`, `mul_nonneg`, `Nat.cast_nonneg`,
`le_mul_of_one_le_right`, `le_add_of_nonneg_right`, `Nat.succ_le_of_lt` are all positively
resolved with getConstInfo in the clean FIRST verifier, and compiled in the final module.

The unchanged whole scaffold `ActualSemanticsFinal.lean` re-elaborated after both module
builds: exit 0, 65.833s, 67 PASS markers (`actual-semantics-final.log/.json`). This refresh
checks the entire immutable original2b MainLemma proof and all 48 copied caller declarations,
their effective telescopes/opaque values/standard axioms/old-Theta dependence/no Root.main_lemma
self-use, an independent updated caller, the exact old Θ adapter, actual updated Root Θ_lt
and main_lemma opaque values and all ten current private helper values, and positive actual
main_lemma→Θ_lt dependence. The literal nine-binder public Θ contract remains exact.
Actual deleted-wrapper absence and successor's direct Θ_option_le/Θ_equiv dependencies pass.

Fresh complete UNFILTERED native results: `native-theta-final.json` and
`native-mainlemma-final.json`; both success=true, partial=false, timed_out=false,
failed_dependencies=[], isError=false, 0 errors. All warnings are preserved:

| File | Warning locations | Findings |
|---|---|---|
| Theta | 1;93;101 twice;109;129;252;547 | pre-existing copyright and hr/hB/hq unused-name warnings, eight total |
| MainLemma | 1;149 twice | pre-existing copyright and hδ0/hr₁ unused-name warnings, three total |

These unrelated warnings are outside this private-helper audit; their classification as
owner-preserved or explicitly user-preserved hypotheses is not reopened here. No warning
is suppressed, and no new target warning appears.

| Identifier | Positive verification | Result |
|---|---|---|
| mul_pos | final module compile + getConstInfo | pass |
| add_pos | final module compile + getConstInfo | pass |
| zero_lt_one | final module compile + getConstInfo | pass |
| mul_nonneg | final module compile + getConstInfo | pass |
| Nat.cast_nonneg | final module compile + getConstInfo | pass |
| le_mul_of_one_le_right | final module compile + getConstInfo | pass |
| le_add_of_nonneg_right | final module compile + getConstInfo | pass |
| Nat.succ_le_of_lt | final module compile + getConstInfo | pass |

Initial final-source trace capture had an insufficient external 180s bound:
`actual-profile-first.log/.json`, exit -15/timeout/drained at 180.022s. Its raw
159338514 bytes contain zero phi and zero public Θ proof anchors, so target timing is
UNMEASURED, not zero or a failed numerical sample (`partial-profile-status.json`).
The preceding accepted whole traces took 274.451/272.970s. The replacement capture uses
420s external wall time, with identical Lean command/default limits and unchanged source.
`profile-process-window.log` verifies the old request drained and only this replacement
profiler runs. No timing sample is discarded to select a faster value.

First COMPLETE actual-source trace: `actual-profile-complete-first.log/.json`, exit 0,
267.478s. `actual-profile-complete-first-table.json` matches all 52 declarations and
strictly validates raw UTF-8: zero malformed bytes and zero replacement sequences.
`profile-first-strict-slices.json` records exact byte offsets, raw SHA, strict slices and
the disjoint top-level timing rows. Nested macro/kernel timings are not added twice.

| Declaration | Command | Async proof | Async addDecl/etc | Linter | Total ms |
|---|---:|---:|---:|---:|---:|
| theta_phi_lt_aux | 184.696 | 425.554 | 5.974 | 31.876 | 648.100 |
| theta_lt_succ_aux (unmodified immediate private caller) | 165.226 | 673.059 | 10.105 | 25.656 | 874.046 |
| public Θ_lt | 71.841 | 199.942 | 3.898 | 14.908 | 290.589 |

First target raw slice is bytes216328349..220636912. The same-source repeat was required
by the immediate private caller's ≥750ms measurement. Both complete source captures are retained.

Whole-file performance is NOT passed. The owner's comparison against the preserved0cb
third/fourth tables corrected the previously too-narrow final repair queue:

| Unrelated declaration | Preserved0cb third/fourth ms | First9faa ms |
|---|---|---:|
| mul_sq_div_three_le_sum_max_of_pos_aux | 785.891 / 769.292 | 1074.965 |
| sum_max_sub_le_index_det | 1443.748 / 1345.298 | 1704.995 |
| index_separated_mul_le_aux | 1159.900 / 1227.606 | 1352.455 |
| index_det_le | 1219.574 / 1155.674 | 1427.252 |
| index_numeric_bound_aux | 1271.059 / 1235.627 | 1237.417 |
| index_le_lem6 | 1518.596 / 1343.022 | 1438.663 |
| lem7_Φ_bound | 1473.482 / 1361.659 | 1398.602 |
| lem7_numeric | 1495.040 / 1426.549 | 1473.078 |

All these source blocks are unchanged by this late private-helper edit. The seven already
failed whole-source pairs are mandatory owner file-final repairs, not phi-induced proof
regressions; the positive helper has a fresh ≥1000 flag. This supersedes the dispatch's
incomplete description of only a numeric/index29 repeat queue. The earlier1068.193/1115.157
index29 failure remains preserved history, not the latest accepted whole-file timing.
MainLemma's inherited bounded actual trace still provides no finite main_lemma timing;
this audit refreshes its complete semantics/build/native gates and does not claim caller
timing passed. All ten other introduced-helper dedicated audits and owner cumulative/full
build/separate LeanEval/publication gates remain pending.

Second COMPLETE actual-source trace: `actual-profile-complete-second.log/.json`, exit0,
271.736s, again52/52 anchors, zero invalid UTF-8 or replacement sequences. Its table is
`actual-profile-complete-second-table.json`; `profile-second-strict-slices.json` and the
three `second-*-strict-slice.log` files retain exact offsets, strict bytes and timing rows.
Second phi raw slice is bytes216132807..220442044. No third same-source sample was taken.

| Scoped declaration | First / second ms | Result |
|---|---|---|
| owned theta_phi_lt_aux | 648.100 / 918.689 | PASS, both<1000, same final SHA repeat supplied |
| public Θ_lt | 290.589 / 527.984 | PASS, both<1000 |
| unmodified immediate private theta_lt_succ_aux | 874.046 / 1373.393 | FAIL required repeat; repair in its own queued fresh audit |

Second phi disjoint rows: command142.408 + async proof712.742 + addDecl14.071 +
linter49.468 =918.689ms; nested kernel13.970ms is not added again. The original failed
0cb pair988.865/1013.946ms remains the before measurement, never silently discarded.
The actual proof repair therefore passes the owned helper/public-consumer budget.

Unrelated second values: sum_max1648.430, separated1325.417, index_det1422.778,
index_numeric1268.328, index29 1480.482, Φ_bound1684.326, lem7_numeric1984.602ms.
The positive helper's first1074.965/second908.077 pair also contains a failure.
Two remaining unmodified helper audits additionally inherit failed pairs:
theta_lt_base_aux821.682/1218.493 and theta_lt_of_large_delta_aux870.970/1450.876ms.
No unrelated declaration is edited or falsely certified by this leaf. The owner has
acknowledged and expanded the separate file-final repair queue.

Source authority is now REVOKED/returned to the owner; no further source edits or Lean
requests are authorized for this leaf. All normal, native and profile requests completed;
`final-profile-drain.log` is empty and confirms no profiler/capture child remains.
Final release manifest: `/private/tmp/theta35-phi-fresh/final-freeze.json` with exact
source/report/artifact hashes, full fresh evidence paths, immutable FIRST history,
new-helper history and pending[]. This leaf introduced no helpers and deleted none.

## Diff and scoped gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual `lake build Roth.Theta`, exit0,31.239s; build-theta-final.json |
| affected caller build | pass | actual subsequent `lake build Roth.MainLemma`, exit0,38.368s; build-mainlemma-final.json |
| definition protected | pass | no def/abbrev/instance/import changes; source before/after owned block byte-identical |
| theorem statement protected | pass | only binder whitespace repack; exact FIRST/current/adapter effective telescope verified; public contracts untouched |
| structure | pass | proof30; local by block≤5; final composed expression9; no case branch>10 |
| naming | pass | mathematical snake_case, private _aux, no forbidden scheme/abbreviation |
| packing | pass | all17 signature lines measured above; maximum target line93 |
| inequality orientation | pass | zero ≥/>; measured10 ≤ and5 < in signature |
| final native | pass | both complete unfiltered native results;0errors, unchanged8/3warnings |
| independent FIRST and old telescope | pass | first-independent-corrected.json, exit0; whole immutable FIRST context, actual opaque proof values, exact15binder adapter |
| actual axioms and caller semantics | pass | actual-semantics-final.json, exit0,67PASS; standard axioms only, full original caller proof and updated independent caller |
| scoped performance | pass | actual whole source sameSHA phi648.100/918.689 and public290.589/527.984, both<1000 |
| unmodified private caller performance | OPEN own fresh audit | successor874.046/1373.393 required-repeat FAIL; no unrelated edit |
| whole-file performance | OPEN owner queue | unrelated repeated ≥1000 declarations above; no whole-file performance PASS |
| cumulative all29 / all actual constants | owner pending | leaf evidence does not replace owner aggregate |
| full lake build then separate Roth.LeanEval | owner pending | not run or claimed by this leaf |

Simplify outcome: ISSUES-FOUND-AND-FIXED in this dedicated scoped review (six pure one-use
facts inlined, all comments preserved, common semantic bounds retained); separate callable
simplify handoff unavailable, fresh independent filewide owner pass pending.
Buzz outcome: FIXED for owned phi/public-consumer scope on two complete actual-source captures;
unmodified successor and whole-file repair queues remain explicitly OPEN with the owner.
Production maxHeartbeats/maxRecDepth raises added:0; profiler/scaffolding additions:0;
new helpers:0; signature/conclusion weakenings:0; comments preserved:3/3.
Total target proof delta:30→30 lines; fewer named forwarding steps, explicit faster proof terms.

## Eleven-step phase checklist

1. References read: done.
2. Full 24-item audit: recorded above.
3. Five-method Mathlib search: raw native responses and source search recorded.
4. Generalisation: every effective parameter probed, scoped mathematical analysis recorded.
5. Packing: all 17 lines measured, required l-binder repack applied.
6. Inequality: entire signature scanned, zero reversed occurrences.
7. All 42 golfing rules: explicit statuses above.
8. Step-back reflection: mathematical assembly and alternatives examined.
9. Final complete native diagnostics: done, both full unfiltered 0-error results.
10. Actual module/semantic/profile diff gates: done; owned phi/public-consumer pair PASS, all unrelated failures retained for owner queues.
11. Rename sidecar: n/a, no rename needed and shared queue not owned.


## Owner clarification: independent updated caller evidence

The earlier scaffold verified the entire independent ORIGINAL MainLemma proof and the
actual updated Root.main_lemma body/type/standard axioms/dependency. Its wording above
about an independent updated caller overstated the evidence: it did not separately copy
the CURRENT caller proof. Those historical67/68-marker runs are retained without relabeling.
The fresh delta-helper audit supplies that missing supplement in
`/private/tmp/theta35-delta-fresh/ActualSemanticsAugmented.lean`: the entire prior scaffold
is a byte-identical prefix, followed by the ENTIRE current MainLemma module copy, its
opaque-value/standard-axiom checks, all26 effective binder names/order/BinderInfo/types
and conclusion, direct Root.Θ_lt dependence, and AST exclusion of imported Root.main_lemma
and private Root MainLemma helpers. Its actual fresh run passed92.739s/114 PASS markers
on Theta3ea263890113e18bef9a29203ef1db57d929c18e40fd5201e34c9e4f0e776fc2;
MainLemma remains ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4.
Owner verified all96 artifact/source hashes and raw clean output in
`/private/tmp/theta35-delta-fresh/owner-checked.json`. This augmented scaffold is required
in subsequent final-source helper/batch gates. The exact report before this clarification
is preserved in `/private/tmp/theta35-owner-report-corrections/`; source and prior measurements
are unchanged. Original35 publication and whole-file final gates remain pending.
