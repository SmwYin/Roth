# Dedicated original6 cleanup: `Roth.one_mem_RSet`

Scope: only the original public declaration in `Roth/Theta.lean`, now lines 66–67.
Owner released this leaf after original5 checkpoint `dbfe215f15e0ca4a5481ecd5bbd0434a81603c61`.
This leaf made no Git/shared-log/rename-queue writes. Source edit is proof-only; public
instances, hypotheses, argument order, name, visibility and original docstring are preserved.

## Result and mathematics

The proof body falls from 3 lines to 1. The new terminal `simp` unfolds membership, uses
`degreeOf_one` and `coeff_one`, carries casts/absolute values through the coefficient conditional,
and closes its two values using `hB` and `zero_le_one.trans hB`. It removes case splitting and
`linarith`. No helper or new import was introduced. No caller edits were necessary.

```lean
  simp [RSet, coeff_one, apply_ite, ite_apply, hB, zero_le_one.trans hB]
```

## Preparation/baseline

Read full dispatch `/private/tmp/roth_theta_leaf_instructions.md`; Lean4/mathlib-quality skills;
full cleanup workflow; full golfing-rules, proof-patterns, mathlib-search,
generalisation-patterns, cleanup-gates; relevant style, naming and profiling references.
Read target immediately before its narrowly matched patch. Read-only preparation honored:
no source/report mutation or Lean request before release.

Owner supplied baseline full build75.907s then separate LeanEval22.076s before release.
Leaf complete unfiltered native baseline diagnostics: success=true, partial=false,
timed_out=false; raw `/private/tmp/roth-one-mem-baseline-lsp.json`. Target warnings were
unused-section Fintype and unused-in-type Fintype/DecidableEq. They remain contract candidates,
not permission to change the public API. Header warning and unrelated declarations' warnings
are outside this leaf. No linter suppressions were added.

## Full substantive audit (24 items)

| # | Item | Finding/action |
|---|---|---|
|1|LINT|Three target instance warnings retained pending public-menu decision; no new source warning expected. Full diagnostic payload retained, unfiltered.|
|2|HAVE SCAN|No `have` in old or new body.|
|3|SET_OPTION|No target option; none added. Scratch automation used a lowered2000 budget only.|
|4|SIMP SQUEEZE|Old branch `simp` was nonterminal before linarith; replaced entire proof by terminal unsqueezed simp.|
|5|NAMING|`one_mem_RSet` expresses one-membership in the existing named set; no forbidden abbreviation/number scheme; no rename.|
|6|LINE PACKING|One95-codepoint signature line; measured table below.|
|7|BY PLACEMENT|`:= by` ends signature line.|
|8|FORMAT|One72-codepoint body line, two-space indentation; no empty proof lines or haveI/letI.|
|9|COMMENTS|No original inline proof comment; docstring preserved byte-for-byte.|
|10|DOCSTRING|Existing public docstring and source citation preserved.|
|11|VISIBILITY|Public API retained; changing public visibility is outside unapproved contract changes.|
|12|STRUCTURE|One-line body; no explicit conjunction in public statement or branch over10lines; no helper needed.|
|13|MATHLIB|Five actual methods below; use existing degree/coeff/conditional API, no equivalent custom-RSet theorem claimed absent.|
|14|JUNK DEF|n/a: theorem, no definition edited.|
|15|EXISTS LEMMA|n/a: no existential statement/witness.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective parameter covered by compiled positive/negative probes below; no public change applied.|
|19|INEQUALITY|Only `1 ≤ B`, canonical orientation; no reversed relation.|
|20|NORMAL FORM|Membership in the existing RSet API is canonical here; no new equivalence family. Scratch threshold iff identifies exact B requirement only.|
|21|SYNTAX GENERALITY|Existing hB then r call shape works for both callers; changing to iff or constant-polynomial API would be separate public design.|
|22|IMPORT FANOUT|n/a: no import change.|
|23|CASTS|No explicit cast introduced in diff; existing `(1 : MvPolynomial σ ℤ)` statement annotation preserved and load-bearing.|
|24|INSTANCE-NAME|n/a: no instance declaration or name.|

## Line packing and inequality tables

Actual `#check @Roth.one_mem_RSet` at width100:

```
@one_mem_RSet : ∀ {σ : Type u_1} [Fintype σ] [DecidableEq σ] {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), 1 ∈ RSet B r
```

| Sig line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
|66|95|none (body next)|n/a, complete signature already one line|ok|

| # | Location | Occurrence | Rewrite | Rename |
|---|---|---|---|---|
|1|hB signature|`1 ≤ B`|none, smaller side left|none|
|2|entire signature|zero `≥`/`>` occurrences|n/a|none|

## Mathlib search-status: five actual methods

Raw results `/private/tmp/roth-one-mem-search-results.json`.

| Method | Actual query/result |
|---|---|
|A Lean-Finder|`multivariate polynomial one coefficients are zero or one degree zero`; found `MvPolynomial.degrees_one`, `degreeOf_one`, `coeffs_one_of_nontrivial`.|
|B Loogle|`MvPolynomial.coeff (1 : MvPolynomial _ _) _` failed unknown constant in remote index; actual retry `"degreeOf_one"` found `MvPolynomial.degreeOf_one`. Remote-index failure is not absence evidence.|
|C LeanSearch|`multivariate polynomial coefficient one degreeOf one`; found degreeOf_one, coeff_X/coeff_X', Polynomial.coeff_one.|
|D source rg|Unfiltered scoped `one_mem_RSet|RSet|theorem degreeOf_one|theorem coeff_one`; found degreeOf_one and coeff_one. Auxiliary scan covered coeff_one_zero/coeffs_one_of_nontrivial/degreeOf_one. No source truncation in this scoped query.|
|E local name search|`coeff_one`, limit10: textual MvPolynomial.coeff_one hit; index=error, so no absence claim. Source and successful compile verify identifier.|

Auxiliary variants inspected: coeff_one_zero, coeffs_one_of_nontrivial, degreeOf_one,
coeff_C, coeff_C_of_ne_zero, degreeOf_C. Common-equivalents lookup: no discrete/finite/
separation bucket applies. Conclusion: partial exact building blocks exist in mathlib;
keep the custom RSet membership API and use the blocks directly. This report does not
claim exhaustive absence of a generic theorem from failed searches.

No-Theta-import compiled probes tried `exact?`/`apply?` so they cannot invoke the theorem
under audit. Both hit the deliberately lowered2000 scratch heartbeat budget, hence
inconclusive; never treated as proof of absence. Full raw automation log retained.

New identifier check: `apply_ite` exists in Lean Init/ByCases.lean:44; `ite_apply` exists in
Mathlib/Basic/Logic/Basic.lean:958; `zero_le_one` and `.trans` are verified by selected proof
compilation. `RSet`/`coeff_one` are existing identifiers. No hallucinated name entered source.

## Generalisation: every effective parameter

Actual compiled artifact `/private/tmp/roth-one-mem-hypotheses.lean` and corresponding log.
Negative dependency artifact `/private/tmp/roth-one-mem-dependent-drop.lean` and log.
All public amendments remain UNAPPLIED; owner/root has not approved menu A+B.

| Parameter | Class/use | Compiled candidates | Result |
|---|---|---|---|
|`σ : Type*`|type-variable; polynomial variables/r domain|Arbitrary universe-polymorphic σ in all positive probes; drop σ with autoImplicit=false; Sort* substitution|Type* already polymorphic; literal drop/Sort fail dependent type elaboration.|
|`[Fintype σ]`|typeclass, unused mathematically|dropFintype; replace with Finite; dropBoth|All three positive proofs compile; retained pending approval.|
|`[DecidableEq σ]`|decidability for coeff_one|dropDecEq with local classical; dropBoth|Both compile; retained pending approval.|
|`B : ℝ`|value used in coefficient bound|Arbitrary B in positive probes; literal binder drop with autoImplicit=false; threshold equivalence|Drop fails unknown B; exact requirement is1≤B. ℝ→abstract ordered structure would require changing RSet, separate API.|
|`hB : 1 ≤ B`|proposition; bounds coefficient1 and0|Compiled exactThreshold iff1≤B; compiled B=0 counterexample|Cannot drop hB or weaken to0≤B:0≤0 but1∉RSet0r. No strict inequality to weaken.|
|`r : σ → ℕ`|structure value; arbitrary coordinate bound|All positive probes permit arbitrary r including0; literal binder drop autoImplicit=false|Drop fails unknown r; no positivity assumption exists to remove. ℕ bound type is defined by RSet.|

No global/pointwise, bundled/unbundled, strict-to-weak or algebraic-class weakening applies
beyond these entries. No hidden section parameter omitted. Candidate-only constant theorem
`C a ∈ RSet B r` from a≠0 and |a|≤B compiles with no variable finiteness assumptions.
This is inversion evidence, not an applied generalization/new wrapper.

## Public literature and inversion check

Read local source `clean.tex` §Index across sets of polynomials, lines644–666: integral,
nonzero polynomials, coordinate degree bounds and coefficient bounds; constant1 is admitted.
The source uses positive r and finite m, but the compiled proof confirms no such restriction
is needed for this membership observation.

Actual web queries: `Roth theorem auxiliary polynomial coefficient bound constant polynomial 1 generalization`;
`"Formalizing Roth" "polynomial" Takloo Yin`; `Roth constant polynomial coefficient height 1 polynomial ring arbitrary variables`.
First query top3: Barcelona proof of Roth, AMS chapter4, JTNB paper; none supplied a stronger
version of this elementary membership fact. Combined later results included UCLA ring-theory
notes, UCLA algebra text, a proof-design repository. No specialized generalization was inferred.
Useful primary background: [UCLA polynomial-ring notes](https://www.math.ucla.edu/~sharifi/notes/algebra-ch03.html)
and [Milojević's Roth exposition](https://aleksa-milojevic.github.io/expository/roth.pdf), which
uses polynomial height as maximum absolute coefficient. External results provide context;
compiled probes establish the precise local hypotheses. ChatGPT math MCP is unavailable
(no matching exposed tool), recorded rather than silently skipped.

Inversion check fires in the limited sense that unfolding RSet leaves only nonzero/degree/
coefficient conditions;1 is discharged by standard degreeOf_one/coeff_one. Compiled constantMem
with C a is a concrete broader candidate, but would be a new public API and is not required
by either existing caller. It remains assessed/unapplied. The underlying polynomial lemmas
already work over broad commutative semirings; changing RSet's ℤ/ℝ design is separate work.

## All42 golfing rules

| Rule | Status |
|---|---|
|1.1 by-exact|n/a: absent.|
|1.2 by-rfl|n/a: absent.|
|1.3 rw/exact|n/a: no such chain; old rw removed with entire proof.|
|1.4 simp/exact|Whole proof closes with selected terminal simp.|
|1.5 trailing rfl|n/a: absent.|
|1.6 anonymous constructor|Old refine constructor replaced by whole simplification.|
|1.7 apply/exact|n/a: absent.|
|1.8 by_contra/push|n/a: absent.|
|1.9 eta|Old lambdas disappear with simplification.|
|1.10 inline have|n/a: no have.|
|1.11 apply/intro|n/a: absent.|
|1.12 show|n/a: absent.|
|1.13 projections/obtain|n/a: absent.|
|1.14 merge rw|n/a: one old rw removed.|
|1.15 terminal simp|Selected terminal simp left unsqueezed.|
|1.16 nonterminal simp|Old nonterminal simp removed; none remains.|
|1.17 dot notation|`zero_le_one.trans hB` uses dot notation.|
|1.18 parens/<||n/a: no needless trailing parens.|
|1.19 push_neg|n/a: absent.|
|1.20 exists inline|n/a: no existential helper.|
|2.1 grind|Actually compiled no-Theta probe fails degree case; no success claimed.|
|2.2 delete before grind|n/a: no grind in retained proof.|
|2.3 simpa|Term alternative with ite_le_sup compiled, but longer; whole simp chosen.|
|2.4 fun_prop|n/a: no function-property goal.|
|2.5 positivity|No remaining independent positivity subgoal; explicit trans supplies0≤B.|
|2.6 gcongr|n/a: no monotonicity expression or calc chain.|
|2.7 lia/omega|Nat degree bound closes by simp; real B bound uses hB directly, no arithmetic search needed.|
|2.8 aesop|Actual no-Theta probe hits lowered2000 scratch heartbeat budget; inconclusive, not retained.|
|2.9 norm_num/cast|Casts normalized by chosen simp; threshold counterexample compiled with simp.|
|2.10 decide|n/a: arbitrary real B/arbitrary σ, no finite decidable computation closes hB-parametric theorem.|
|2.11 field_simp/ring|n/a: no denominators/equality.|
|2.12 linear_combination|n/a: no ring/ring_nf terminator or polynomial identity.|
|2.13 wlog|n/a: no symmetric independent cases.|
|2.14 calc collapse|n/a: no calc.|
|2.15 <;>|Old multi-branch terminal chain eliminated entirely.|
|3.1 erw/rw|n/a: no erw.|
|3.2 legacy fun tactics|n/a: absent.|
|3.3 omega/lia|n/a: neither required.|
|3.4 rcases-rfl|n/a: absent.|
|3.5 attributes|No automation attribute change: new global normal form is public API.|
|3.6 simp_all|n/a: no multiple local dependent hypotheses to simplify.|
|3.7 options|No source options present/added.|

Step-back reflection: selected one-tactic proof is shorter and exposes only standard facts.
Two earlier simp candidates failed because a conditional function application remained;
adding `ite_apply` closes it. Initial speculative `ite_le` was rejected as unknown in
scratch; corrected term route through existing `ite_le_sup` compiled, but is longer.
No failed scratch term entered source. No private helper/wrapper was added.

Native multi_attempt stalled and was explicitly canceled by terminating exec cell17, as
owner directed. It supplies no claimed result; ordinary compiled probes supply actual
results. All ordinary verification and final diagnostics were drained before profiling.

## Simplify pass

Manual equivalent review (no callable built-in simplify tool available): PASS-THROUGH.
The single terminal simp has no duplicated skeleton, single-use have, cast wrapper or
unnecessary private helper. No source changes during this pass.

## Verification, performance, freeze

Actual module command: `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0,
51.177s, raw `/private/tmp/roth-one-mem-module.log`, machine status adjacent.

Complete final native unfiltered `lean_diagnostic_messages(file_path="Roth/Theta.lean")`:
success=true, partial=false, timed_out=false, failed_dependencies=[],27 warnings/0errors,
same27warnings as baseline (line shifts reflect two removed lines). Raw unfiltered payload:
`/private/tmp/roth-one-mem-final-lsp.json`. Three target instance warnings remain only because
owner/root has not approved the public contract menu; no new warnings or suppressions.

Independent original declaration gate: original RSet and original three-line proof are copied
into `Original6`, with no self invocation. The artifact compares definitions and theorem proof
values via rfl as corroboration, prints actual full type, and checks both constants' axioms.
Most strongly, a `run_cmd` reads both declarations using `Lean.getConstInfo`, alpha-aligns
universe parameters, and applies `Lean.Meta.isDefEq` directly to the two `.type` fields.
This is not an implicitly eta-expanded theorem application. Direct exact-type result: PASS.
`lake env lean /private/tmp/roth-one-mem-original-compatibility.lean` exit0; final direct-check
raw log `/private/tmp/roth-one-mem-strong-types.log`. Earlier independent proof run also
passed29.101s. Original6 and actual built Roth.one_mem_RSet both use exactly
`[propext, Classical.choice, Quot.sound]`. No custom axioms/sorry/native_decide/source limit raise.

### Buzz: FAST-BOARD, exact-prefix only

Before and after preserve every exact preceding import/source/context, terminating just after
target with `end Roth`. Each real command was
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
Before prefix `/private/tmp/roth-one-mem-before-prefix.lean`, after prefix
`/private/tmp/roth-one-mem-after-prefix.lean`; both exit0, wall34.822s/31.236s.
All ordinary module/LSP/probe work completed before these sequential profiler runs; both
profiler processes completed before final direct-type compile. No active exec/compiler request remains.

| Target | Outer command | Async proof | Async addDecl/kernel/realization | Async linters | Aggregate |
|---|---:|---:|---:|---:|---:|
|before|3.623ms|187.603ms|11.015ms|9.248ms|211.489ms|
|after|4.097ms|154.580ms|5.837ms|8.516ms|173.030ms|

The after kernel aggregate includes all associated outer async addDecl nodes (0.024+5.813ms)
and zero-time realization. Nested Meta/tactic/kernel timing children are not double-counted.
Actual raw anchors are line5383(before)/5379(after), beginning with target docstring;
raw `/private/tmp/roth-one-mem-before-profile.log` and `...after-profile.log`, summary
`/private/tmp/roth-one-mem-profile-summary.jsonl`. Both aggregates are below750ms, so no
borderline repeat required under the supplied policy; budget1000ms. No per-proof heartbeat
number is claimed. No profiling scaffolding entered source. Parent's full-module profile sweep
remains mandatory after the known late index_le_lem6 cleanup; this prefix says nothing about
that late declaration or whole-file performance.

### Eleven leaf gates

| Gate | Result/evidence |
|---|---|
|lake_build_file|PASS, actual `lake build Roth.Theta` exit0 51.177s, raw module log.|
|definition_protected|PASS, exact baseline transformation verifies only old target body replaced.|
|theorem_statement_protected|PASS, signature/docstring/name/visibility byte-identical; direct elaborated-type check preserves all implicit instances.|
|structure_gate|PASS,1body line, no >10line branch/helper.|
|naming_gate|PASS, descriptive membership name, no forbidden pattern.|
|line_packing_gate|PASS, required one-row95-codepoint table.|
|inequality_orientation_gate|PASS, required table, zero reversed relations.|
|cumulative_no_unintended_breakage|PASS at leaf scope: no caller edits; both internal callers elaborate in actual module/full live LSP. Owner downstream full-build gates pending.|
|independent_original_contract|PASS, copied independent original proof and direct constant-type comparison, not self invocation.|
|standard_axioms|PASS, actual built and independent original only propext/Classical.choice/Quot.sound.|
|buzz/no_scaffolding|PASS,173.030ms exact-prefix aggregate; no limit raises or source traces.|

Leaf gates pass with existing unapproved public-instance warnings explicitly retained.
Full project build then separate Roth.LeanEval are owner-only pending checkpoint gates.

Freeze: this leaf revokes further source edits. SHA256 of final `Roth/Theta.lean`:
`555407fefac3d3c452906b586e4b98953d4a54593beb2e538f212dd805b0b45b`.
Only target proof changed; body3→1lines (−2), file4line diff (1added/3removed). Detailed report
is the only repository sidecar this leaf wrote. All requests/processes used by this leaf drained.


## Phase checklist (11)

1. ✓ Required full reference reading.
2. ✓ Full substantive24audit.
3. ✓ Five actual search methods, bounded failures recorded honestly.
4. ✓ Every effective parameter compiled/probed; literature+inversion recorded.
5. ✓ Per-line packing table.
6. ✓ Per-occurrence inequality table.
7. ✓ All42rules have concrete status.
8. ✓ Step-back reflection, one-tactic and term alternatives considered.
9. ✓ Complete unfiltered final live diagnostics; baseline warnings unchanged.
10. ✓ All11leaf gates passed, with owner full/LeanEval explicitly pending.
11. ✓ No rename required, so sidecar untouched; comments/docstring preserved.

Phase5a/5b: no refactoring or rename applied; candidate public assumptions remain explicitly
pending owner decision. No new helper needing another dedicated audit. File header left
unchanged as instructed. Owner full build and separate LeanEval gates remain pending this
leaf report and source freeze; this report does not claim they ran on the new proof.

## Owner frozen checkpoint gates

All leaf compiler/LSP/profile requests drained and source authority revoked before owner checks.
Source SHA256 `555407fefac3d3c452906b586e4b98953d4a54593beb2e538f212dd805b0b45b` stayed
unchanged through sequential `lake build` (exit0,60.236s) THEN separate `lake build Roth.LeanEval`
(exit0,16.524s). Logs `/private/tmp/roth-theta-d06-{full,leaneval}.log`; structured exit codes,
timing and hashes `/private/tmp/roth-theta-d06-builds.json`. Exact-path stage/commit and successful
cleanup-branch push complete the checkpoint before the next original declaration edit.
After successful publication: Theta6/35 originals; overall187/264;9/14files complete.
No public amendment or new helper; whole-module final profiling remains pending.
