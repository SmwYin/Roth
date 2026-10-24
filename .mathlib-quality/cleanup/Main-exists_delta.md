# Main original10 — Roth.exists_delta

# Auditing: `exists_delta` (entry L225–268, 39 body lines)

1. LINT: reused complete accepted same-source Main diagnostics, zero target-range warnings.
2. HAVE SCAN: complete inventory below; mathematical rewrite replaces explicit error budgets with continuity.
3. SET_OPTION: none.
4. SIMP SQUEEZE: L249/L254 `simp only [hμ, lt_min_iff]` are nonterminal, targeted lists; final proof removes both. No bare nonterminal simp.
5. NAMING: `exists_delta` is descriptive snake_case existential parameter choice, no forbidden abbreviation or numerical scheme, no rename required.
6. LINE PACKING: entry signature has underpacked lines; final table will measure each signature line and next expression.
7. BY PLACEMENT: `by` ends the signature line, preserved.
8. FORMAT: remove inline `rw [hc]; field_simp` semicolon by replacing entire obsolete explicit-budget argument; use two-space proof indentation, four-space signature continuation, no empty body lines.
9. COMMENTS: no inline proof comments in original or entry target, none removed.
10. DOCSTRING: preserve source citation and mathematical description, add the new valid n=0 application context.
11. VISIBILITY: retain public parameter-choice API and metadata; available to clients of Roth.Main, not an auxiliary extracted proof.
12. STRUCTURE: 39 body lines requires substantive shortening; bounded continuity-at-zero route compiles at 16 body lines, no helper needed. Correlated conjunction belongs under one existential witness and cannot be split independently without losing the common δ.
13. MATHLIB: all five methods performed; partial match ContinuousAt.eventually_lt and Metric.eventually_nhds_iff, used directly. No full project-specific eta/gam parameter-choice theorem found; compiled proof uses existing analysis API.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, public nontrivial witness with several strict numerical bounds, not trivial private reflexive witness.
16. SHOW/CHANGE: no show in entry. New `show ... by fun_prop` is term-mode expected-type annotation required for `.div` elaboration, not a tactic-mode rewriting show.
17. PUSH_NEG: none.
18. GENERALISE: remove hn and h47 when strengthened proof + sole caller diagnostics validate; every parameter assessed below. Retain strict hm/h47' if weak trials fail.
19. INEQUALITY: zero ≥/> in entire entry signature, name has no ge/gt. No orientation rewrite required.
20. NORMAL-FORM: existential shared δ with strict inequalities is the natural local parameter-choice form, no simp attribute or equivalence proliferation.
21. SYNTAX-GEN: hm and final ratio hypothesis suffice; removing derived assumptions simplifies sole caller. Keep order and correlated conclusion.
22. IMPORT-FANOUT: n/a, no imports added.
23. CASTS: real cast of m genuinely bridges ℕ→ℝ, `(1 / 2 : ℝ)` fixes real-rpow exponent; final explicit types on continuity terms supply expected types after actual untyped `.div` failure. No redundant same-type cast introduced.
24. INSTANCE-NAME: n/a, no instance.

## Complete entry HAVE scan

| Entry line | Name | Proof content / uses | Action |
|---|---|---|---|
|230|hm0|by, used hmR|replace with continuity proof|
|231|anonymous positivity|by, used omega|replace|
|233|hmR|by, used hsm and positivity|replace|
|234|hn'|by, positivity context|replace|
|235|hsm|no by, positivity context|replace|
|236|hG|by, hκ0 and division|replace|
|237|hκ0|no by, repeated positivity context|replace|
|239|hE|by, repeated positivity context|replace|
|245|hc0|by, eta bound and positivity|replace|
|248|hμ0|by, hδ0/hδlt|replace|
|251|hδ0|by, h29/h30 and witness/eta|replace|
|252|hδlt|by, hδlt'|replace|
|253|hδlt'|no by, simp then obtain (mutable local)|replace|
|259|hgam|no by, final denominator positivity|reuse uniform bound at zero instead|
|260|hceq|by rw/field_simp, heta|remove explicit budget identity|
|261|heta|no by, a3|remove budget estimate|
|262|a1|by, final linarith|remove|
|263|a2|by, final linarith|remove|
|264|a3|by, final linarith|remove|

Issues: (1) >30-line explicit-budget proof, (2) redundant hn/h47 hypotheses, (3) signature packing, (4) application documentation. No new helper or global rename needed.

## Search status
[A] Lean-Finder: continuity preserves strict inequality near zero → ContinuousAt.eventually_lt.
[B] Loogle: `ContinuousAt, _ < _` → same exact general continuity lemma.
[C] LeanSearch: continuous function inequality eventually near point → ContinuousAt.eventually_lt.
[D] Source grep: ContinuousAt.eventually_lt (OrderClosed L691), Metric.eventually_nhds_iff (Pseudo.Defs L782), Real.continuousAt_rpow_const (Pow.Continuity L218), div_div_eq_mul_div (Group.Basic L505).
[E] Local name query ContinuousAt.eventually_lt: index unavailable, empty not absence; actual grep and compiled use independently verify name.
Auxiliary variants: ContinuousAt.rpow_const / Real.continuousAt_rpow_const / Filter.Tendsto.rpow_const_nhds_zero. Existing MainLemma.exists_delta_bound provides other numerical constraints uniformly near zero.
Common-equivalents lookup: no discrete/finiteness/separation/bornology bucket applies.
Conclusion: partial match; build directly on general continuity API, retain substantive parameter-choice theorem.

## Generalisation status

| Binder | Class | Drop/weakening candidate | Evidence/action |
|---|---|---|---|
|n : ℕ|structure value|drop impossible while n free in eta/gam constraint; ambient abstract type unsupported by concrete definitions|retain|
|m : ℕ|structure value|drop impossible while m free throughout conclusion; no universe/typeclass candidate|retain|
|hn : 0 < n|proposition|drop; strict→weak weaker than successful drop|bounded strengthened continuity proof compiled without hn; keep drop after live diagnostics|
|hm : 16*n²<m|proposition|drop, strict→weak|existing exists_delta_bound requires strict; weak trial recorded separately; m=n=0 admits ratio 0<1 but conclusion forces 0<δ<0, so cannot weaken/drop|
|κ : ℝ|structure value|drop impossible while κ free in conclusion; no point-localization/universe candidate|retain|
|h47 : 4*n*sqrt m<m|proposition|drop; strict→weak subsumed by drop|derive denominator nonzero from exists_delta_bound at zero; compiled clean|
|h47' : 2*m/(m-4*n*sqrt m)<κ|proposition|drop/strict→weak|strict inequality at zero feeds eventually_lt; weak trial recorded separately, retain strict|

No explicit typeclass/decidability/type-variable/universe binders; no global function-property hypotheses to point-localize. Inversion: lam/gam/eta do reduce to continuous elementary expressions, and mathlib already supplies the correct abstract continuity theorem; use it directly without an optional abstraction/helper.
Literature query: `Roth theorem choice delta small continuity parameters generalization`; top three relevant logged hits: Chapman–Chow Generalised Rado and Roth (different additive theorem, no applicable weakening); Roth ICM1958 lecture (parameter choice within Diophantine approximation, no concrete extra weakening); CMC GNT Roth lecture notes (standard theorem and references, no concrete extra weakening). MSE continuity-choice result disregarded as secondary/unrelated. ChatGPT math MCP unavailable. No optional ambient generalization proposed.

## Golfing rule pass (all 42 rules)

| Rule | Status |
|---|---|
|1.1 by exact|n/a: no outer `by exact` wrapper; continuity terms contain substantive fun_prop subproofs.|
|1.2 by rfl|n/a: none.|
|1.3 rw/exact→rwa|n/a in final: obsolete explicit budget/rwa argument replaced mathematically.|
|1.4 simp/exact→simpa|applied: quotient-at-zero and metric-distance transformations close by simpa using the premise.|
|1.5 trailing rfl|n/a: none.|
|1.6 anonymous constructor|applied: one final constructor packages the common δ and all four bounds.|
|1.7 apply/exact|applied: continuity `.div` and order transitivity are direct terms, no apply/exact chains.|
|1.8 by_contra!|n/a: no contradiction proof.|
|1.9 eta reduction|n/a: lambdas contain actual arithmetic/gam application, not `fun x ↦ f x` boilerplate.|
|1.10 single-use have|applied: removed all 19 entry haves except a newly established continuity certificate; inlined eta continuity and zero-gap fact. Final hc has substantive `by fun_prop` proofs inside its typed composed term and is the named mathematical certificate, not a one-call alias.|
|1.11 apply/intro|n/a: no implication introduction.|
|1.12 redundant show|n/a: two term-mode shows provide expected ContinuousAt types; actual first untyped `.div` experiment failed without one.|
|1.13 obtain pairs|applied: obtain uniform bounds, neighborhood radius, witness, and the two earlier inequalities directly.|
|1.14 merge rw|applied by elimination: all three final consecutive rw calls in entry disappear under continuity argument.|
|1.15 terminal simp only|n/a: final has no simp only; terminal simpa stays unsqueezed.|
|1.16 nonterminal simp|n/a: final has no nonterminal simp.|
|1.17 dot notation|applied: `.div`, `.sub`, `.const_mul`, `.eventually_lt`, `.trans_le`, `.ne'`.|
|1.18 <\| vs parentheses|n/a: parentheses group arguments followed by further arguments, preserving needed precedence; no trailing by block removable by <\|.|
|1.19 push_neg|n/a: none.|
|1.20 trivial existential helper|n/a: nontrivial public shared witness, no trivial private helper.|
|2.1 grind|tried once at initial live proof state L231; failed, with unresolved existential/zero-cast case; continuity needed.|
|2.2 tactics before grind|n/a: no grind retained.|
|2.3 simpa consolidation|applied: constant quotient at zero becomes h47' by direct simpa, metric bound similarly.|
|2.4 fun_prop|applied: numerator and gam continuous; explicit rpow continuity supplies eta at zero.|
|2.5 positivity|applied: nonnegative rpow exponent and nonzero positive exponent required for zero_rpow.|
|2.6 gcongr|n/a: final order steps are direct transitivity and min projections; no monotone-expression inequality subproof.|
|2.7 lia/omega|applied by elimination: original positivity-of-m omega proof removed; no Nat/Int arithmetic goal remains.|
|2.8 aesop|tried once at initial live proof state; exhaustive search left existential goal; retained continuity proof.|
|2.9 norm_num/norm_cast|n/a: no numeric equality/cast goal remains; real exponent signs close by positivity.|
|2.10 decide|n/a: existential real-parameter problem is not finite decidable computation.|
|2.11 field_simp/ring|applied by elimination: explicit budget identity and denominator field_simp removed; `div_div_eq_mul_div` supplies quotient normalization directly.|
|2.12 linear_combination|n/a: final proof has no ring/ring_nf step or algebraic certificate search; continuity replaces old final linear arithmetic.|
|2.13 wlog|n/a: no symmetric branches.|
|2.14 calc term mode|n/a: no calc remains; order chains are direct terms.|
|2.15 <;> multiple goals|n/a: final constructor uses supplied terms, no duplicated residual branches.|
|3.1 erw→rw|n/a: none.|
|3.2 continuity→fun_prop|applied: function-property goals use fun_prop, no legacy continuity tactic.|
|3.3 omega→lia|already satisfied in 2.7: source no longer contains any target omega call.|
|3.4 rcases/rfl|n/a: no equality substitution.|
|3.5 automation attributes|n/a: shared existential choice is not a simp/fun_prop rule; no new helper or global attribute.|
|3.6 simp_all only|n/a: none.|
|3.7 limits|n/a: no limit override in original, entry, or final.|

## Step back and think

The explicit E/c/four-way minimum proof was replaced by continuity of the quotient at zero. The already accepted uniform δ-bound lemma gives denominator positivity at zero and the other numerical inequalities for the same chosen δ. A single open-neighborhood inequality and `exists_between` finish the proof. Live `exact?` could not close the whole theorem; `apply?` offered partial existential rewrites with unsolved obligations, not a proof. `grind` and `aesop` failed at the same initial state. No helper, optional abstraction, or theorem duplication is needed.

## Final HAVE scan

The only final have is `hc`, a ContinuityAt certificate built by composing actual `by fun_prop` subproofs and the rpow continuity theorem. Both earlier one-call single-use facts (heta and hgap) have been inlined. hc appears once in the neighborhood extraction, and preserves the load-bearing expected function type after the initial compiler failure without expected type. All uniform bound pairs are destructured with obtain.

## Baseline and scope

The accepted same-source entry baseline is reused from `/private/tmp/roth-main-eta-bound` and the owner's eta-bound acceptance receipt: full build, separate Eval build, fresh native Main/Eval/root and complete diagnostics were already clean apart from four existing Main warnings. No unchanged baseline rebuild was run for a label. This worker owns only `exists_delta`, its conditionally authorized sole caller repair, this report, and scratch evidence. No Git, shared queue/progress, next-target, or new project helper edits occurred.

Genuine original Main684 (`f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`) and entry Main632 (`910ef04480715846d6b22eacf0aa70f5d9e260e0af2abccfef644088758fbc83`) were saved BEFORE any Lean/golf experiment. Both target declarations had 44 lines / 39 body lines. They are not identical: the exact four earlier accepted differences are `exists_delta_bound hn hm → exists_delta_bound hm`; strict bound arguments → `.le` arguments; eta-bound arguments → `.le` arguments; final `nlinarith → linarith only [a1,a2,a3]`. See `entry-original-save.json` for exact diff and separate hashes. The dispatch's sole-eta description was corrected, with owner acknowledgement, without reopening prior audits.

## Final generalisation verification

Dropped `hn` and `h47` in the compiled continuity proof, with the owner's narrow caller lease: `exists_delta (by omega : 0 < n) hm h47 h47' → exists_delta hm h47'`. Both are logically unnecessary because the accepted uniform `exists_delta_bound hm` at zero supplies positive `gam - eta`. The only source caller, in `roth_of_isIntegral`, compiles and its full original TYPE was structurally compared. `h47` remains available at other uses. All Lean project files, including Eval, were searched for actual calls.

Weak `hm : 16*n² ≤ m` failed at the strict existing `exists_delta_bound` application; it also admits n=m=0, where the conclusion forces 0<δ<0. Weak final quotient premise failed at the strict inequality needed by `ContinuousAt.eventually_lt`. Both actual bounded trial diagnostics are saved, and strict premises retained. There are no further concrete safe weakening or optional abstract-type candidates in scope.

## Line packing — final `exists_delta`

Actual `set_option format.width 100 in #check @Roth.exists_delta` was included in the frozen profile prefix. Its elaboration trace exposes the full result:

```lean
@Roth.exists_delta : ∀ {n m : ℕ},
  16 * n ^ 2 < m → ∀ {κ : ℝ}, 2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ →
    ∃ δ, 0 < δ ∧ δ < 1 / ↑m ∧
      Roth.eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2 ∧
      ↑m * (1 + 4 * δ) / (Roth.gam δ n m - Roth.eta δ m) < κ
```

The displayed reference reflows whitespace from the actual trace; no unobserved standalone #check output is claimed. Signature packing uses complete binder/relation units, measured in codepoints:

| Sig line | Chars | Next binder/relation unit | Arithmetic | Action |
|---|---:|---|---|---|
|226|60|`(h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ)` (43)|60+1+43=104 >100|ok|
|227|78|`eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧` (50)|78+1+50=129 >100|ok|
|228|54|`(m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ := by` (55)|54+1+55=110 >100|ok|
|229|59|no next signature line|n/a|ok|

`final-source-measurements.json` contains every measured source line and unit. Final declaration 20 lines / 16 physical body lines; no branch exceeds ten lines and no artificial helper/fact tuple was introduced. The conjunction remains under one existential so the four constraints hold for the same δ.

## Inequality scan — final `exists_delta`

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
|1|complete signature and all hypotheses|n/a: zero ≥/>; hm, h47' and all witness inequalities use <|none|none; name has no ge/gt|

## Casts and identifier verification

Casts: 0 isolated redundant-ascription removals / 5 final genuine natural-to-real casts retained / 1 real numeric exponent ascription retained as load-bearing. The two term-mode ContinuousAt expected-type annotations are also load-bearing; the first untyped `.div` attempt failed. Other old casts disappear with the replaced mathematical argument, not as an unsupported same-type-cast claim.

| Introduced/reference identifier | Verification |
|---|---|
|ContinuousAt.eventually_lt|Finder, Loogle, LeanSearch, exact local source OrderClosed L691, compiled use|
|Metric.eventually_nhds_iff|exact source Pseudo.Defs L782, compiled use|
|Real.continuousAt_rpow_const|exact source Pow.Continuity L218, compiled use|
|div_div_eq_mul_div|exact source Group.Basic L505, compiled use|
|exists_between, lt_min, min_le_left/right|compiled use in live proof and fresh native source|
|ContinuousAt.div/sub/const_mul, continuousAt_const|compiled use and independent proof|
|exists_delta_bound, eta_lt_gam_iff|accepted earlier MainLemma API, actual compiled use|

## Semantic evidence

`Semantics.lean` reuses the accepted full structural comparator for every Expr, Name, Level, BinderInfo and metadata node, without Expr BEq short-circuiting. Accepted old target and caller TYPE strings alone were read by bounded indexed seeks: target23719B (read cap49438B), caller2391B (cap6782B), indexed SHA/length checked. No old VALUE or whole giant caller row was decoded or copied.

A distinct independent proof uses continuity of the scalar gap `κ*(gam-eta)-m*(1+4δ)` and a half-minimum witness, followed by the positive-denominator division inequality. Production uses quotient continuity and `exists_between`. The independent proof never refers to the target; original-contract recovery uses the target intentionally. Actual family enumeration includes public descendants and actual privateToUserName? descendants; observed target/independent/recovery families each consist of their one root.

All three actual opaque VALUEs were checked in memory for closure, inference and standard axioms propext/Classical.choice/Quot.sound at defaults200000/20000/512. Saved VALUE length/hash receipts are target858116B, independent4056517B, recovery10558B. Full original recovery TYPE, current target/independent TYPE, and original `Roth.roth_of_isIntegral` caller TYPE match structurally. The actual current caller opaque VALUE was also inferred, closed and std3 checked in memory. Fresh local closure is acyclic; every external constant has actual strictly upstream ModuleIdx, while accepted preceding Main evidence is reused. No identity between different proofs or modules is claimed.

Actual semantic launch exited0 in131.750s; receipt `semantics-receipt.json`, native log `semantics.stdout`, complete streams retained. The one initial independent build failed on expected-type/dotted-notation annotations; its full failure log remains. One precise annotation repair produced exit0 in31.025s, without changing project source or adding limits. Initial bounded continuity attempts failed on a missing expected type, the nested-division normalization, and the metric binder name; each was repaired using the relevant verified API. Expected rejected weakenings are not counted as unexplained verification failures.

## Verification and gates

Actual full `/Users/ramin/.elan/bin/lake build` exited0 in59.459s. Then separate `/Users/ramin/.elan/bin/lake build Roth.LeanEval` exited0 in58.838s (root excludes Eval). Between them, the owner requested only a doc simplification to `The parameter n may be zero.` Exact inverse SHA binds that doc-only edit to the actual full-build/LSP source (`full-build-LSP-source.lean`); proof/code full-build evidence is reused with this qualification. The Eval build and all fresh native compiles consumed the final exact source.

Fresh unfiltered `lake env lean Roth/Main.lean` exited0 in30.780s; Eval28.800s; root29.521s. Full separate stdout/stderr are retained. Complete actual Main LSP was partial=false/success=true/0errors, four existing warnings at then1/254/395/396 (final doc-only rebasing1/253/394/395), no target warning. Exact inverse source hash qualifies its doc-only reuse. Complete final Eval/root LSP were partial=false/success=true with no diagnostics. No LSP ran during compiler/native/semantic/profile work.

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|PASS|actual full build and separate Eval build above; final exact native source checks|
|lake_build|PASS|actual full build exit0; only later edit is exactly qualified owner-requested doc wording|
|definition_protected|PASS|no def/abbrev or other declaration source changed|
|theorem_statement_protected|PASS, authorized strengthening|audit item18 drops hn/h47, recovery proves exact original contract; exact sole caller lease repair|
|structure_gate|PASS|16 body lines, no >10-line branch; coherent existential witness preserved|
|naming_gate|PASS|exists_delta snake_case, no forbidden pattern/abbreviation; no rename queued|
|line_packing_gate|PASS|all four signature lines measured above, no repack row|
|inequality_orientation_gate|PASS|zero ≥/> in code signature/hypotheses|
|cumulative_no_unintended_breakage|PASS|full+Eval build, fresh Main/Eval/root native, actual caller VALUE/originalTYPE and complete diagnostics|
|no trust/limit/scaffolding drift|PASS|no sorry/new axiom/native_decide/count_heartbeats/limit raise; profiling additions only in scratch|

## Simplify and buzz

Built-in Skill(simplify) is unavailable in this environment; no invocation or pass-through is fabricated. This scoped pass performs the substantive reuse/quality review above, and the fresh independent whole-file final review remains the owner's scheduled file-final gate. The owner independently reviewed current source and the complete target-specific semantic/profile evidence in `/private/tmp/roth-main-owner/delta-choice-owner-review-v1.json`.

Buzz outcome: FIXED, target final exact-prefix453.636ms <1000ms and <750ms (no repeat required). Historical valid FAIL2310.533ms belongs to its actual Main689 whole-file source after earlier accepted MainLemma caller repairs, not genuine Main684 or the current prefix. Its full canonical payload and all six disjoint roots were verified with bounded indexed seeks; both contexts remain separately bound, with no ratio or noise-causation claim.

Final fresh capture used exact production imports, preceding commands, target prefix and namespace close; actual family TYPE/universes exactly match semantic production, while each context's actual VALUE is independently inferred/closed/std3. Four disjoint roots: command39.439ms + proof392.561ms + addDecl/kernel parent7.761ms + lint13.875ms =453.636ms. Nested kernel7.704ms is included in its parent and not added again. No target compiler root or lazy prior-DATA root was observed. Full canonical payload, source map, byte offsets, raw stream SHA/length, and the complete current trace are saved in final-profile. Default assertions, exact frozen inputs and full parent/Lake environment byte equality passed; full environments stayed in memory and only approved fields/hashlength were persisted.

Profile protocol: explicit owner HOLD ACK preceded ANY preparation; all five capture launches and capture driver exited0 and their groups/PID were actually absent; then an UNPARSED drain notice was sent; explicit owner RELEASE preceded parsing. `actual-drain-unparsed.json`, owner hold/release receipts and `target-profile-acceptance.json` bind this sequence. No additional profile run or optional probe was needed.

## Result and phase checklist

Before44 declaration/39 body lines; after20/16; saved24 declaration/23 body lines. Main632→609 lines (net−23 including the one added doc line),34752→33974B. Final Main SHA4248f0cd2d75850e16ac260b14a2ad8921e5bb8017cf1e64cff38f5d4f4328a9.
Audit issues4, fixed4, original10 refactoring deferred0. Rules applied1.4/1.6/1.7/1.10/1.13/1.14/1.17/2.3/2.4/2.5/2.7/2.11/3.2; whole-goal grind/aesop/exact?/apply? tried without a closing proof. Renames queued:none. Comments preserved:none present in original/entry proof; original source citation retained, new application fact n=0 documented. Refactoring needed:none for original10. Separately, owner has queued the newly unused prior private eta_lt_of_lt for fresh independent FILE-FINAL consumer-confirmed pruning; no source lease expansion or prior audit reopening occurred, and the five global END renames remain untouched.

- [✓] Step1: installed skills, full cleanup/cleanup-all and mandatory references read.
- [✓] Step2: all24 concrete audit items and complete original/final HAVE scans recorded.
- [✓] Step2.5: all five search methods and auxiliary variants recorded.
- [✓] Step2.6: all binders classified, concrete drops verified, rejected weak trials retained, literature status recorded.
- [✓] Step2.7: every signature-line width and next-unit arithmetic recorded.
- [✓] Step2.8: inequality occurrence scan recorded.
- [✓] Step3: every one of42 rules has concrete status/reason.
- [✓] Step4: whole-proof alternate strategy and bounded whole-goal attempts evaluated.
- [✓] Step5a: actual complete Main/Eval/root diagnostics, qualified doc-only Main reuse.
- [✓] Step5b: build/protection/structure/naming/packing/orientation/caller/trust/performance gates passed.
- [✓] Step6a: no new rename; shared sidecars untouched.
- [✓] Step6b: evidence/report/actual END and lease-release handoff completed.
