# Fresh audit: private degreeOf_aeval_X_none_of_ne

Original declaration 13; baseline HEAD 8afe156, 570 lines / 26 retained declarations.
Parent baseline complete native LSP: 0 errors, 31 warnings. Actual baseline profile
`/private/tmp/roth-separation-d12-final-profile.log`: command 16.936 ms + async 36.242 ms = 53.178 ms.
This initial audit precedes source edits. Both skills and full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, relevant style,
naming and profiling references and cleanup Phase 4 read. No delegation.

## Initial 24-item audit

| Item | Concrete status/action |
| --- | --- |
| 1 Lint | No target-specific warning. Final complete unfiltered diagnostics required. |
| 2 Have scan | L138 anonymous have has `by`, used once at L141: legitimate proof content; try removing entire support argument via degrees rename API. |
| 3 Set option | None. |
| 4 Simp squeeze | L141 terminal simp with explicit mapDomain argument; leave unsqueezed if retained. |
| 5 Naming | degreeOf is mathlib operation, X is generator, none is Option constructor; descriptive equality-of-ne name has no forbidden abbreviation or numeric scheme. No rename. |
| 6 Line packing | Two signature lines measured below; both require breaks. |
| 7 By placement | `by` ends conclusion line. |
| 8 Format | Two-space indentation, no empty body lines, no haveI/letI. Replace ordinary lambda arrows when proof changes. |
| 9 Comments | Zero inline proof comments; surrounding documentation preserved. |
| 10 Docstring | Private implementation lemma: no docstring required. |
| 11 Visibility | Already private; two genuine callers. |
| 12 Structure | Eight body lines, one local three-line proof, no conjunction or long branch; no extraction. |
| 13 Mathlib | Five actual searches below; degreeOf/degrees rename API may replace support argument. No absence claim. |
| 14 Junk def | Lemma, no definition. |
| 15 Exists lemma | Equality, not existential. |
| 16 Show/change | None in original proof. |
| 17 Push neg | None. |
| 18 Generalise | Probe each effective binder R, CommSemiring R, τ, o, ho, V and Semiring weakening. Fintype/DecidableEq already omitted. |
| 19 Inequality | No statement comparison other than disequality; original proof intermediate bound uses ≤ correctly. |
| 20 Normal form | Degree equals zero is canonical for derivative callers. |
| 21 Syntax generality | Arbitrary Option index with local exclusion supports both callers directly. Broader arbitrary variable types unnecessary for private implementation. |
| 22 Import fanout | No imports proposed. |
| 23 Casts | MvPolynomial target fixes aeval algebra; Option target on constant map fixes codomain. Retain only load-bearing ascriptions. |
| 24 Instance name | No instance declaration. |

Issues to fix: test a shorter proof using degrees of injective renaming; retain private helper unless exact replacement justifies deletion. Public signatures/docs preserved. No new helper proposed.

## Initial width table

| Line | Characters | Next signature token | Reason |
| --- | ---: | --- | --- |
| 132 | 93 | degreeOf | Full next conclusion does not fit within 100. |
| 133 | 82 | body | Conclusion and by fit; body starts next line. |

## Inequality occurrence table

| Region | Occurrence | Orientation |
| --- | --- | --- |
| Signature/all hypotheses | o ≠ none; no <, >, ≤, ≥ | Disequality, no reversal |
| Original body | Nat.eq_zero_of_le_zero / degreeOf_le_iff encode ≤ 0 | Correct ≤ direction |
| Name | No _ge_ or _gt_ | No rename |

## Search and literature status

Private implementation helper: explicit private-literature exemption; no public literature search required.
Actual native queries: Lean Finder `degreeOf polynomial aeval X variable different zero`
returned degreeOf_X and degree lemmas; Loogle `MvPolynomial.degreeOf, MvPolynomial.rename`
returned degreeOf_rename_of_injective and degreeOf_eq_natDegree; LeanSearch
`MvPolynomial degreeOf rename variable not in range zero` returned degreeOf_rename_of_injective.
Source rg in MvPolynomial Degrees/Variables/Equiv inspected degreeOf, degrees rename,
mem_vars_iff_degreeOf_ne_zero and support API. Local `degreeOf` query returned textual results,
index unavailable (not indexed absence). Exact source and compiler checks are the fallback.
Five methods actually attempted, all available; no claim of absence.
Six strict rules: search all methods, inspect variants, use existing class formulation,
replace exact duplicates if discovered, preserve public docs under explicit contract;
no topological common-equivalent applies. Retained helper is not yet a 1–3-call wrapper.

## Owner-directed wrapper deletion trial

The shorter proof compiled and complete LSP stayed at 0 errors / 31 warnings.
Owner review correctly asks that the helper be tested for deletion rather than
retained merely because its simp list contains several API facts. There are two
callers, the derivative callback and the degree-of-product rewrite. Next edit
removes the private declaration and substitutes the exact degree calculation at
both callers; public statements and docstrings remain byte-identical. This is
routine private-wrapper deletion explicitly authorized by dispatch and owner.

## Full 42-rule golf pass

| Rule | Concrete result |
| --- | --- |
| 1.1 by exact | No wrapper in original; deletion removes declaration entirely. |
| 1.2 by rfl | None. |
| 1.3 rw + exact | No adjacent rw/exact; final degree caller rw now followed by terminal simp. |
| 1.4 simp + exact | None; direct degree calculation replaces whole support proof. |
| 1.5 trailing rfl | None. |
| 1.6 constructor | No conjunction or constructor. |
| 1.7 apply + exact | No such pair. |
| 1.8 by_contra | None. |
| 1.9 eta reduction | Constant rename map is not eta expansion; injective proof replaced by injective_of_subsingleton. |
| 1.10 single-use have | Original anonymous range proof eliminated with helper. |
| 1.11 apply + intro | Original already uses refine/fun; deleted. |
| 1.12 show | No redundant show; trial explicit injectivity ascription removed by named API. |
| 1.13 have projections | No projection pair. |
| 1.14 consecutive rw | No adjacent rw pair. |
| 1.15 terminal simp only | All new terminal simp calls left unsqueezed. |
| 1.16 nonterminal simp | No new nonterminal bare simp. |
| 1.17 dot notation | No applicable qualified method call after replacement. |
| 1.18 trailing parentheses | No removable trailing lambda/by parentheses. |
| 1.19 push_neg | None. |
| 1.20 private existential | Equality helper, not an existential; removed under general wrapper rule. |
| 2.1 grind | Actually tried on initial goal via native multi_attempt; failed on uninterpreted degree. |
| 2.2 before grind | No retained grind block. |
| 2.3 simpa consolidation | No simp/closing pair; whole support calculation replaced by simp of degrees. |
| 2.4 fun_prop | No analytic function-property goal. |
| 2.5 positivity | Goal is equality to zero, not positivity/nonnegativity/nonvanishing. |
| 2.6 gcongr | No monotonicity calculation; original bound discharged via exact zero computation. |
| 2.7 lia/omega | Actually tried lia on original final mapDomain bound; failed without structural mapDomain fact. |
| 2.8 aesop | Actually tried on initial goal and final mapDomain goal; failed. |
| 2.9 norm_num/norm_cast | No concrete arithmetic or cast calculation. |
| 2.10 decide | Arbitrary polynomial over arbitrary semiring; not finite computation. |
| 2.11 field_simp/ring | No denominators or coefficient ring identity. |
| 2.12 linear_combination | No ring/ring_nf ending or algebraic hypotheses. |
| 2.13 wlog | No symmetric cases. |
| 2.14 calc collapse | No calc. |
| 2.15 multi-goal closing | No new sibling goals needing common closing tactic. |
| 3.1 erw | None; actual caller uses rw. |
| 3.2 continuity | No legacy analytic tactic. |
| 3.3 omega to lia | No omega introduced; lia trial failed as recorded. |
| 3.4 rfl substitution | Original obtain substitutes renamed support index; entire argument eliminated. |
| 3.5 attributes | Deleted implementation helper needs no simp/grind registration. |
| 3.6 simp_all | No simp_all only. |
| 3.7 limits | No limits present or introduced. |

## Step-back review and simplify pass

Actual native initial-goal trials grind, simp, aesop failed. Exact? on the original
mapDomain bound found no direct proof. First direct degree trial exposed a
multiset-replicate membership goal; adding the existing mem_replicate theorem
closed it. The mathematical argument is simply that injective renaming maps all
univariate variables to none, so their degree multiset contains no other index.
The owner review found the resulting helper was disposable; both exact caller
substitutions now compile via complete native LSP. No new helper, general API,
attribute, import, docstring rewrite, or public deletion is needed.
Built-in simplify capability is unavailable in this tool environment; manual
holistic reuse/quality/efficiency review performed, with owner independent review
leading to wrapper deletion. Outcome: ISSUES-FOUND-AND-FIXED (private wrapper).

## Phase 5a/5b

Removed the private helper and substituted its proof at both exact callers.
Rename queue additions: 0; no numerical or forbidden names. No rename action.
Pending public instance menu and public aeval_X_eq_rename deletion are untouched.

## Every effective binder and generalisation probe

Raw compiler probes: `/private/tmp/roth-separation-d13-binders.json` and
`/private/tmp/roth-separation-d13-drop-{0..6}.lean`; `autoImplicit false`.
Each variant was actually compiled. Three probes initially raced a module build
and saw missing olean; all three were retried successfully to real binder errors.
These are rejected experimental variants, never source changes or proofs using sorry.

| Binder | Actual candidate | Compiler result |
| --- | --- | --- |
| τ : Type* | Drop (0) | Unknown τ in o and aeval target; required variable type, already universe polymorphic. |
| R : Type* | Drop (1) | Unknown R in class/polynomial/target; required coefficient type, already universe polymorphic. |
| CommSemiring R | Drop (2); weaken Semiring R (6) | Missing Semiring/CommSemiring for drop; missing CommSemiring for parent. MvPolynomial API requires commutative coefficients. |
| o : Option τ | Drop (3) | Unknown o in ho and degree target; required queried index. |
| ho : o ≠ none | Drop (4) | Original proof cannot refer to ho; required exclusion. No strict-order weakening applies to Option disequality. |
| V : Polynomial R | Drop (5) | Unknown V in evaluation; arbitrary value, no pointwise weakening. |

Fintype τ and DecidableEq τ were already explicitly omitted in original target;
independent original proof compiles without either. No hidden instance removal.
No strict inequalities, bundled facts, analytic global hypotheses, or concrete
coefficient restriction to weaken. Inversion check: original support argument is
abstract after renaming; degrees_rename_of_injective already supplies that abstract
API. Reuse it directly at the callers; no new generalized helper or public API.
Literature: n/a, private declaration, explicitly exempt. Big changes: none applied.

## Final width / casts / comments

The private declaration has been removed, so no final target signature survives.
Original signature measured below with whole next expression as the packing unit:

| Original line | Width | Next complete signature unit | Arithmetic | Action |
| --- | ---: | --- | --- | --- |
| 132 | 93 | full degreeOf conclusion | 93 + 1 + 78 = 172 > 100 | ok (deleted) |
| 133 | 82 | none; body follows | 82 + 1 + 0 = 83; signature ends | ok (deleted) |

Both changed caller signatures are byte-identical to starting HEAD; their width
and contract are preserved. Added proof lines have maximum width 99 codepoints.
No new casts or ascriptions: casts 0 dropped / 0 cross-type / 0 load-bearing added.
Zero inline comments in the removed proof; all Lean block comments and docs are
byte-identical to starting HEAD (actual extraction comparison). No new identifiers
besides Function.injective_of_subsingleton and Multiset.mem_replicate; both are
source-confirmed and #checked in independent-final log, alongside degrees rename.

## Verification gates (worker scope)

| Gate | Result | Evidence |
| --- | --- | --- |
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Separation` exit 0 after final removal; `/private/tmp/roth-separation-d13-build-removal.log` ends Build completed successfully (1876 jobs). |
| Complete native LSP | PASS | `/private/tmp/roth-separation-d13-removal-lsp.json`: unfiltered, partial false, timed_out false, success true; 0 errors, 31 unchanged baseline warnings. |
| Original type / independent non-self proof | PASS | `/private/tmp/roth-separation-d13-independent.lean` copies exact original target with explicit original effective binders, reproduces independent original support proof; compiler exit 0, `/private/tmp/roth-separation-d13-independent-final.log`. |
| Actual changed caller axioms | PASS | Built Roth.hasseDeriv_rename_mul_aeval and Roth.degreeOf_rename_mul_aeval each only propext, Classical.choice, Quot.sound; independent-final log. Removed target has no retained constant. |
| definition_protected | PASS | No definition line changed. |
| theorem_statement_protected | PASS | Authorized private deletion; both public caller signatures byte-identical to HEAD. |
| structure_gate | PASS | Removed helper; inserted terminal callback three lines, degree proof terminal simp three lines; no new long branch or conjunction. |
| naming_gate | PASS | No forbidden pattern/name introduced; helper removed, zero renames. |
| line_packing_gate | PASS | Target removed; preserved public signatures, all added lines ≤99. |
| inequality_orientation_gate | PASS | No new ≥ or >; no statement inequality change. |
| Diff hygiene | PASS | git diff --check exit 0; exact target name has 0 references. |
| Full project / LeanEval / cumulative original compatibility | Parent-owned postfreeze | Not duplicated or claimed run by worker. |

Warnings preserved under dispatch: header metadata and pending public-instance
menu account for baseline lint; no warning suppression. No sorry, axioms,
native_decide, limits, imports, global attributes, or new helpers introduced.

## Performance / buzz

Actual repository module profiled with
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`.
Final removal log `/private/tmp/roth-separation-d13-removal-profile.log`;
parser `/private/tmp/roth-separation-profile-table.py` produces adjacent `.log.json`.
One outer command plus one outer async proof anchor per changed caller, without
nested double counting:

| Declaration | Before command + async ms | Final command + async ms | Final conservative ms |
| --- | --- | --- | ---: |
| Removed private target | 16.936 + 36.242 | Removed | 0 |
| hasseDeriv_rename_mul_aeval | 65.655 + 182.016 | 75.763 + 393.163 | 468.926 |
| degreeOf_rename_mul_aeval | 26.208 + 36.834 | 49.778 + 95.879 | 145.657 |

Before actual module log supplied by parent: d12-final-profile.log. Both changed
callers remain below 750 ms trigger and 1000 ms budget. Local timings increased;
this cleanup removes an implementation wrapper and does not claim a performance
improvement. No limit increases or profiling scaffolding in source. Outcome:
FAST-BOARD for the owned target and affected callers, no over-budget deferrals.

## Eleven completion steps

- [x] Step 1: references read.
- [x] Step 2: substantive full 24-item initial audit before source edits.
- [x] Step 2.5: all five actual mathlib search methods; raw search JSON preserved.
- [x] Step 2.6: every effective binder drop and parent weakening compiled; private literature exemption explicit.
- [x] Step 2.7: signature width tables; target deleted, callers unchanged.
- [x] Step 2.8: inequality occurrence table; no reversed comparisons introduced.
- [x] Step 3: all 42 golf rules with concrete status.
- [x] Step 4: alternate mathematical proof tried; owner step-back review led to deletion.
- [x] Step 5a: complete unfiltered native diagnostics; unchanged 31 baseline warnings, no errors.
- [x] Step 5b: module, independent original-type proof, actual caller axioms, diff/style/protection/profile gates.
- [x] Step 6a: no rename necessary, zero sidecar queue mutations.

## Result and scope

Removed one private lemma and exactly replaced its two calls. Original target
body 8 lines; no target remains. File 570 → 562 lines (−8), exact git numstat
7 additions / 15 deletions. Retained declarations 26 → 25. No helper added.
Public API, all docstrings and narrative block comments unchanged. Shared logs,
Git operations, whole-original/cumulative compatibility, project and LeanEval
builds remain parent-owned. Existing public-instance menu and public aeval bridge
deletion proposals remain pending and are not applied by this worker.

## Freeze

Final actual-module profile command exited 0; final independent compiler exited 0;
final module build exited 0. All Lean, MCP, compiler, binder-probe and profiler
requests have completed and been drained. Final source SHA256:
`ba6cdd854cc9e3ae0df16663905d80233ae16b8f2240e8c8326e5ea801b1e1d2`.

ALL source ownership is revoked. Worker is report-only; no further source edits.
No Git mutation performed. Parent may now run sequential project / LeanEval and
cumulative compatibility gates, then exact-path commit and push.

## Owner cumulative publication gates

Source FROZEN SHA256 `ba6cdd854cc9e3ae0df16663905d80233ae16b8f2240e8c8326e5ea801b1e1d2`; leaf ownership revoked and requests drained before owner gates. Owner probe `86125` exit0,47.19s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d13-compatibility.{lean,log,json}`. Owner build session `25929` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,128.57s/30.90s; source hash stable. `/private/tmp/roth-separation-d13-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
