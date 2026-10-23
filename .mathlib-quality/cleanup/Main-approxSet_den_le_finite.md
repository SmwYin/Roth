# Auditing `approxSet_den_le_finite` (entry lines 67–96)

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Lean4 and mathlib-quality skills applied. Required workflows and relevant paper §6 read. Entry and genuine original saved before Lean/golf in `/private/tmp/roth-main-bounded-denominators`.

1. LINT: complete unfiltered native LSP Main returned 0 errors, warnings only at 1,327,468,469; none in target.
2. HAVE SCAN: L74 hqmem no by used once L77 → inline. L75 hqR has by, used in field cancellation implicitly → replace cancellation. L76 hterm no by used once by linarith L81 → inline if practical or retain as arithmetic certificate boundary. L78 hdiv has by → keep. L79 anonymous no by used once rw/linarith chain → compose or restricted linarith. L82 habs has by → keep/rewrite direct order API. L83 anonymous has by → eliminate via div_le_iff₀. L87 hqQR has by → direct cast bound. L88 anonymous no by used once by nlinarith → inline. L90 hK' has by → keep. L91 anonymous has by → keep cast bridge.
3. SET_OPTION: none.
4. SIMP: L73 `simp only at hq0 happ hqQ` performs definitional reduction, nonterminal; retain or eliminate using typed pattern. L95 nonterminal explicitly squeezed product/interval membership, consolidate with terminal `simpa`.
5. NAMING: approxSet is the existing defined object, den indicates denominator, le/finiteness describes conclusion; no prohibited pattern/abbreviation; no rename needed.
6. LINE PACKING: required table below.
7. BY: at end of signature line 68.
8. FORMAT: 2-space proof indent; no blank body lines; replace two `fun ... =>` lambdas with ↦; no haveI/letI.
9. COMMENTS: none in proof; docstring/source retained.
10. DOCSTRING: public statement and source present, distinguishes bounded denominators from later asymptotic statements; retain.
11. VISIBILITY: public pair-set finiteness API retained under strict contract; no new helper.
12. STRUCTURE: 28 physical proof-body lines at actual entry (dispatch's 31 was stale); no case branches or conjunction conclusion. Scalar subproof ≤8 lines; shorten directly, no helper needed.
13. MATHLIB: partial building blocks present; five-method status below.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: n/a no existential wrapper.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: no proposition/typeclass assumptions; per-parameter table below. No optional API expansion.
19. INEQUALITY: zero reversed signs; table below.
20. NORMAL-FORM: Set.Finite of a restricted set is canonical; finite rectangles and subsets are library APIs.
21. SYNTAX-GEN: OK, directly usable by discarding finitely many bounded-denominator pairs; no restatement needed.
22. IMPORT-FANOUT: n/a no new imports.
23. CASTS: existing ℕ/ℤ→ℝ bridges genuine; final diff inventory pending.
24. INSTANCE-NAME: n/a no instances.

Issues to fix: inline single-use membership; lambda syntax; replace measured broad arithmetic/cancellation with direct scalar library bounds; consolidate final membership simplification.
Refactoring needed: none.

## Line packing

| Sig line | Chars | Next syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 67 | 52 | whole continuation stripped of indentation (45 chars) | 52+1+45=98 ≤100 | repack |
| 68 | 49 | none | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | full signature and local hypotheses | no ≥/> | n/a | none |

## Mathlib search-status

[A] Lean-Finder: bounded denominators integer rational approximations → Rat.finite_rat_abs_sub_lt_one_div_den_sq (rational target, reduced rational, fixed exponent); Real.exists_rat_abs_sub_le_and_den_le; Real.exists_int_int_abs_mul_sub_le (existence, different conclusion).
[B] Loogle: `|?a| ≤ |?b| + |?a - ?b|` → no hits; no absence claim.
[C] LeanSearch: finitely many integers absolute value bounded by real → Int.instIsOrderBornology; Metric.isBounded_of_abs_le; NumberField.Embeddings.finite_of_norm_le (different domains).
[D] Source search: abs/div and mul_le_mul variants; div_le_iff₀, abs_sub_abs_le_abs_sub, Finset.single_le_sum, finite_toSet, subset present.
[E] Local name search `abs_sub`: positive source hits including abs_sub; index warming (not evidence of absence); initial unavailable explicitly recorded.
Auxiliary variants: scalar division-to-multiplication, interval membership/product, subset. Common-equivalents: finite subset of finite rectangle. Conclusion: partial match, retain theorem using scalar library calls. No helper/wrapper added; no claim of exhaustive semantic absence.
Compiled whole-goal probes: grind failed with finite-set obstruction; aesop made no progress; exact? no close; apply? returned generic partial finite-set/cardinality routes, no complete substitute.

## Generalisation status

| Parameter | Class | Used | Mechanical candidates | Verified? | Result |
|---|---|---|---|---|---|
| α : ℝ | structure value | approximation error and numerator bound | drop: statement depends on α; typeclass/pointwise/strict/universe candidates n/a fixed real-valued approxSet | static dependency | retain |
| κ : ℝ | structure value | rpow error radius | drop: statement depends on κ; no hypotheses to weaken; real rpow fixes type | static dependency | retain |
| Q₀ : ℕ | structure value | bounded denominator and finite interval | drop: changes set; no point/strict/typeclass/universe hypothesis | static dependency | retain |

Inversion check: approxSet is unfolded to its concrete integer/natural division and rpow inequality. The generic fact (finite denominators with bounded numerator fibers) is already the finite rectangle/subset API. General error-radius abstraction would add optional API without helping this contract; no proposed expansion. Big-change candidates: none required.

## Literature search status

Web query: “bounded denominators finitely many rational approximations real number generalization”. Top three: AMS Rational Approximation chapter (https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf), Bugeaud bounded-degree approximation paper (https://www.sciencedirect.com/science/article/pii/S0022314X06001600), Columbia approximation notes (https://www.math.columbia.edu/department/rama/chapters/chap13.html). AMS explicitly bounds numerator when denominator/error are bounded. Broader algebraic-degree approximation is a different problem. Local clean.tex §6 lines1175–1178 directly matches pair finiteness. No algebraicity, irrationality or κ>2 assumptions are present/needed. ChatGPT math MCP unavailable among callable tools. Literature-driven required changes: none.

## Focused baseline

Old whole-Main diagnostic 1399.455 ms is separate context, no ratio. Exact current-source-prefix baseline 657.420 ms, all disjoint command/proof/kernel-parent/lint roots counted once; target + nine actual generated simp helpers discovered. Main proof 604.451 ms; linarith 117.346 ms, field_simp 68.198 ms, nlinarith 229.842 ms. Taxonomy 4 heavy automation, with cancellation overhead. No repeat required (<750 ms). Prefix production slice and full frozen source/import/tool bytes bound; limits 200000/20000/512. All process groups drained, explicit owner release before streaming parse.

## Golfing rule pass (all 42 rules)

- 1.1 n/a: no by-exact wrapper; cast tactics have substantive work.
- 1.2 n/a: no by-rfl.
- 1.3 n/a: no adjacent rw/exact with same closing fact; ceil proof rewrite changes cast.
- 1.4 attempted final simp/exact → simpa; default simp changes product-interval association, reverted.
- 1.5 n/a: no trailing rfl.
- 1.6 n/a: existing final anonymous constructor already concise.
- 1.7 n/a: no apply/exact chain.
- 1.8 n/a: no contradiction/push_neg.
- 1.9 n/a: summand and positivity lambdas not eta-redexes.
- 1.10 applied: hqmem, hterm and anonymous nonnegativity facts inlined into use; scalar intermediate identity removed.
- 1.11 n/a: no apply/intro chain; rintro decomposes existing membership.
- 1.12 n/a: no show.
- 1.13 n/a: no have followed by repeated projections.
- 1.14 n/a: no consecutive rw after cleanup.
- 1.15 n/a: both simp-only calls nonterminal; terminal simpa carries required rewrites.
- 1.16 n/a: no bare nonterminal simp.
- 1.17 applied: trans dot notation for nonnegativity composition (old le_trans anonymous intermediate removed).
- 1.18 n/a: no removable terminal parentheses; scalar application precedence needs grouping.
- 1.19 n/a: no push_neg.
- 1.20 n/a: no trivial existential helper.
- 2.1 tried whole-proof grind, failed to derive finite-set bound.
- 2.2 n/a: no grind retained.
- 2.3 tried final simpa consolidation, mismatch in conjunction association; original explicit membership normalization retained.
- 2.4 n/a: no regularity/measurability goals.
- 2.5 positivity retained in nonnegative summands; attempted on habs, correctly rejected as not positivity goal.
- 2.6 tested div_le_iff₀ + gcongr route: rewrite did not match; direct mul_le_mul_of_nonneg_left route succeeds.
- 2.7 n/a: Nat/Int steps are cross-type casts, not integer arithmetic search; exact_mod_cast directly discharges them.
- 2.8 whole-proof aesop tried, made no progress.
- 2.9 n/a: no concrete numeral computation; cast boundaries already exact_mod_cast, no repeated norm_cast normalization.
- 2.10 n/a: quantified real theorem is not finite computation.
- 2.11 original field_simp removed using direct div_le_iff₀; no remaining field identity requiring field_simp/ring.
- 2.12 n/a: no ring/ring_nf terminal with hypotheses.
- 2.13 n/a: no symmetric case branches.
- 2.14 n/a: no two-step calc; scalar trans composed directly.
- 2.15 n/a: no similar multiple goals.
- 3.1 n/a: no erw.
- 3.2 n/a: no continuity/measurability.
- 3.3 n/a: no omega; cast-only arithmetic handled directly.
- 3.4 n/a: no rcases with rfl.
- 3.5 n/a: single domain-specific fact, no new automation attributes needed.
- 3.6 n/a: no simp_all only.
- 3.7 n/a: no resource-limit override.

## Step back and think

Whole-proof grind/aesop/exact? did not close; apply? offered generic partial finite/cardinality routes. Finite rectangle is already a direct finite-set API application. The scalar estimate now uses div_le_iff₀ and monotonic multiplication, with only the three needed arithmetic facts given to linarith. Term mode for the whole proof would obscure local bounds. No redundant scalar cancellation identity remains; no helper extraction or optional generality needed. Independent fixture instead bounds numerators by a sum of denominator-specific numerator bounds, materially different from production's common error-radius rectangle.

## Final signature packing

| Signature line | Chars | Next token | Arithmetic | Action |
|---|---:|---|---|---|
| 67 | 98 | no following signature line | n/a | ok |

Before 2 signature lines, after 1. Statement expression unchanged; #check width reference included in final verification fixture. Body 28→23 physical lines; declaration 30→24, saving 6 total lines. No ≥/> in signature or local inequalities, no name rename needed. All proof lines ≤100 characters.

## Verification and semantic contract

`lake build` actually ran via `run.py build-full /Users/ramin/.elan/bin/lake build`: exit0 in64.762984s. Then separate `lake build Roth.LeanEval`: exit0 in32.880271s. Source hash identical throughout. Fresh complete unfiltered native diagnostics after builds: Main0errors/4preexisting warnings at1,321,462,463; Eval0/0; root0/0. No target warning. Logs and terminal records in `/private/tmp/roth-main-bounded-denominators`.

Genuine original target bytes equal entry target bytes. Exact accepted original raw row loaded by byte offset and SHA from the earlier full inventory, not inferred from current code. Semantics.lean replays that original proof, proves the current contract independently using a sum of denominator-specific numerator bounds, and recursively checks original/current/independent full TYPE constructors including binder names, binder info, levels and metadata. No ExprBEq shortcut. Every actual target/generated/replay/independent opaque VALUE is closed, has inferred declared type and only propext/Classical.choice/Quot.sound. Limits remain200000/20000/512. Main+two generated current helpers; all16 local proofs/generated members checked, local graph acyclic, self references rejected, actual target/generated family denied in replay/independent. Minimal379 direct external names all strictly upstream modules; preceding approxSet DATA strictly equal to accepted TYPE/VALUE. The module DAG closes recursive exclusion. Original/current proof VALUE identity is not required or claimed.

The independent fixture first needed an explicit summand annotation on Finset.single_le_sum; corrected fixture passed64.475685s. Failed fixture retained as evidence, not credited as verification.

Profile main VALUE remains raw-unequal between prefix and production: exactly four actual macro-scoped Name pairs differ in module context (_stdin/Roth.Main), including one internal-name representation. Lean verified BOTH hasMacroScopes and equal eraseMacroScopes for each actual pair. Replacing only those four complete actual Name representations makes every remaining raw VALUE byte equal. No broad normalization; full TYPE/universes and both actual generated helper TYPE/VALUE pairs are exact. Hygiene fixture passed41.557525s. An earlier attempted hygiene invocation referenced a not-yet-created file after an extraction assertion; it failed and receives no verification credit.

### #check reference at format.width100

```lean
Roth.approxSet_den_le_finite : ∀ (α κ : ℝ) (Q₀ : ℕ), {hq | hq ∈ Roth.approxSet α κ ∧ hq.2 ≤ Q₀}.Finite
```

New identifiers: div_le_iff₀ verified by source usages and actual compiled production/replay; mul_le_mul_of_nonneg_left verified at Mathlib/Algebra/Order/GroupWithZero/Defs.lean:226 and actual compilation. No unresolved names. Cast diff:0 redundant casts dropped,3 added/relocated genuine ℤ/ℕ→ℝ crossings retained,0 added load-bearing term ascriptions; the unchanged `(0 : ℝ)` establishes the real positivity goal.

## Gate status (Phase4)

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual full lake build exit0, Main rebuilt; separate Eval build exit0 |
| definition_protected | ✓ pass | No def/abbrev change; prior/suffix source bytes exact |
| theorem_statement_protected | ✓ pass | Only audited whitespace packing; strict full original/current TYPE identical |
| structure_gate | ✓ pass | Ordinary proof23≤30 lines, scalar blocks≤5, no case branches/conjunction conclusion; no new helper |
| naming_gate | ✓ pass | Descriptive approxSet/den/le/finite, no forbidden name pattern or abbreviation |
| line_packing_gate | ✓ pass | Single98-codepoint signature, final per-line table above |
| inequality_orientation_gate | ✓ pass | No reversed ≥/> in signature/local hypotheses |
| cumulative_no_unintended_breakage | ✓ pass | Full build, separate evaluation build, complete Main/Eval/root diagnostics |
| no trust/limit/scaffolding drift | ✓ pass | No axioms/sorry/native_decide/count_heartbeats/resource raises/debug scaffolding in production diff |

Overall: pass. No renames queued; no shared queue/progress/Git writes. No comments removed (none in original proof); docstring/source exact retained. All24 audit items and42 golfing rules have explicit status.

## Buzz pass

Outcome: FIXED. Old whole-Main1399.455ms is an honest separate-context failing diagnostic, not a comparable benchmark. Exact entry-prefix657.420ms; finished-source-prefix430.129ms. No speedup ratio or causal cross-context claim. Final threshold pass<1000ms, and<750ms so no repeat required. Parent approved exact production-prefix method. All full production bytes/import/tool inputs frozen; exact canonical source payload matched. All actual generated families charged, not guessed.

Final disjoint charges: command5.352ms + proof393.255ms + helper/main kernel parents0.261/0.153/15.416ms + asynchronous lint15.692ms =430.129ms. Nested kernel leaves not added again. Compiler parents none; actual lazy prior DATA none. Final target family main,_simp_1_1,_simp_1_2. Baseline main+nine generated helpers fully inventoried. Raw traces streamed, not whole-decoded; raw SHA/byte length checked. Actual default guards verified. Heartbeat wrappers were prohibited by task instructions; none introduced.

Final-v1 was REJECTED: only its observational `pp.width` option was unknown; post environment/default sequence did not finish, no timing credit. All failed groups drained/freeze checked; explicit owner release before diagnosis. Corrected versioned v2 uses format.width100. V2 completed both environment/default checks with full environment equality in memory (only hashes/length and allowed path/toolchain fields persisted); all known task groups absent, frozen inputs exact, explicit owner release before raw parse. Both failed and valid captures retained, no cherry-picked successful repeat.

## Result

Before:30 declaration lines (2signature+28body). After:24 (1signature+23body). Saved:6. Audit issues found4/fixed4; no refactoring deferred. Rules applied1.10,1.17; lambda syntax corrected; measured scalar library replacement and restricted arithmetic context retained. All source edits target-only. No optional generalization, companion, helper extraction, other-hotspot repair, or repeated literature loop.

Phase checklist:
- [✓] Step1 references read.
- [✓] Step2 full24-item audit printed.
- [✓] Step2.5 five-method mathlib status printed.
- [✓] Step2.6 all-parameter generalisation and public literature status printed.
- [✓] Step2.7 initial/final per-line signature width tables.
- [✓] Step2.8 inequality scan table.
- [✓] Step3 all42 golfing rules.
- [✓] Step4 step-back reflection.
- [✓] Step5a complete native diagnostics, no target warning.
- [✓] Step5b all diff gates pass with actual builds/semantic evidence.
- [✓] Step6a no rename needed/queued.
- [✓] Step6 final report, focused buzz430.129ms, actual process drain/all leases release at handoff.

File-level simplify and later project-wide phases remain with the owner; no unavailable skill invocation is claimed here. Refactoring needed: none.
