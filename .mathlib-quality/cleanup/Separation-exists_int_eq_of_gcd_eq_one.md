# exists_int_eq_of_gcd_eq_one cleanup

Initial audit recorded before source edits. Scope: original declaration 26, lines 437–451,
15 declaration lines (2 signature + 13 body); no other source ownership.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md; Lean/mathlib skills and relevant style,
naming/profiling references read. Parent owns Git, public decisions, and cumulative gates.

## Initial 24-item audit
1. LINT: target none; complete baseline LSP has 0 errors, 6 unrelated warnings.
2. HAVE SCAN: no have declarations. z/hz Bézout and w/hw local integrality witnesses used.
3. SET_OPTION: none.
4. SIMP SQUEEZE: terminal simp at first calc identity; push_cast twice; no bare nonterminal simp.
5. NAMING: snake_case describes integer witness and gcd-one premise, no forbidden abbreviations
   or numeric patterns; no rename needed under naming_gate catalogue.
6. LINE PACKING: signature width arithmetic recorded below.
7. BY PLACEMENT: by at end of signature line.
8. FORMAT: standard indentation; calc has one inline rw; simp subproof, candidate consolidation.
9. COMMENTS: no inline narrative; preserve complete source docstring.
10. DOCSTRING: existing three-line description and source-specific explanation preserved.
11. VISIBILITY: public API explicitly retained.
12. STRUCTURE: 13 body lines <=30; conclusion single existential, no conjunction splitting.
13. MATHLIB: five actual search methods underway; gcd_eq_sum_mul supplies Bézout.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: n/a public nontrivial arithmetic theorem, not trivial private witness.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: all effective binders and drops to be probed in isolation; public signature fixed.
19. INEQUALITY: no <, >, <=, >= occurrences in signature or hypotheses.
20. NORMAL-FORM: existential integer cast equals rational is the downstream coefficient API;
    IsLocalization.IsInteger/range formulation possible but public restatement unnecessary.
21. SYNTAX-GEN: gcd-one premise directly matches primitive coefficients, keep.
22. IMPORT-FANOUT: no new imports proposed.
23. CASTS: all casts bridge integers/rationals; sum ascriptions fix integer summation type.
24. INSTANCE-NAME: n/a theorem, no instances.

Issues to test: replace the two expanded sum calculations by cast/sum/mul simp identities.
Refactoring needed: none. exists_sum_mul_eq_gcd API retained as explicitly directed.

## Signature widths (codepoints)
- L437: 93; next complete binder `{v : ℚ}`; 93 + 1 + 7 = 101 >100, packed.
- L438: 77; next complete binder `(body)`; signature end.

## Five-method mathlib search
A. Lean-Finder actual success: related IsIntegral.ratCast_iff and tactic IsRat/IsInt lemmas,
   no exact replacement returned. Raw /private/tmp/roth-d26finder.json.
B. Loogle actual success: Finset.gcd with rational query returned finite-place height result,
   not replacement. Raw /private/tmp/roth-d26loogle.json.
C. LeanSearch actual success: IsLocalization.IsInteger/range and IsIntegral results,
   not replacement. Raw /private/tmp/roth-d26search.json.
D. Unfiltered source/name grep found Finset.gcd_eq_sum_mul and its uses; full target name
   absent from mathlib; examined PrincipalIdealDomain.lean:233–242 actual implementation.
E. Native local name search found Finset.gcd_eq_sum_mul; index warming, so no absence claim
   based on index. Raw /private/tmp/roth-d26local.json.
Live exact? failed; apply? yielded only partial logical reformulations. grind/aesop failed.
No assertion of exhaustive mathematical absence; keep this public integer integrality API.
Six strict rules: generic API reused; no new wrapper/helper; existing public Bézout helper
explicitly retained by dispatch, not deletion-authorized; no new predicate or import.

## Literature search
Actual web search: Bezout identity primitive integer coefficients rational multiples integral
 gcd 1. Primary source textbook [The Bezout Identity](https://math.gordon.edu/ntic/ntic/section-bezout-id.html)
confirms gcd as integer linear combination. Local clean.tex:420–432 explicitly derives
integrality by multiplying that relation by the rational coefficient. The ring-wide version
is an inference from this argument, compiler-verified below; no claim that the source states it.

## Generalisation status (all effective binders)
| Binder | Probe / mathematical role | Result |
|---|---|---|
| ι : Type* | already universe-polymorphic index; s/u depend on it | cannot remove parameter without restating family |
| s : Finset ι | finite sum/gcd domain; no global Fintype or DecidableEq assumption | retain finite family; no stronger class to weaken |
| u : ι → ℤ | gcd and integral coefficients | retain; abstract Bezout coefficient base would change public API |
| hu : s.gcd u = 1 | actual isolated same-proof drop failed Unknown identifier hu and unsolved goal | retain; no compiler-certified semantic impossibility claim |
| v : ℚ | tested ℚ→arbitrary Ring R | compiles, proposed only |
| hv : ∀ a ∈ s, ∃ z : ℤ, ↑(u a)*v=↑z | actual isolated same-proof drop failed Unknown identifier hv / choose shape | already localized to s; retain |
No τ/Fintype/DecidableEq effective binders, confirmed with @target at format.width 100.
No strict inequalities, analytic global assumptions, or bundled bijections to weaken.
Inversion: proof uses rational numbers only for ring operations and integer casting;
concrete→Ring proposal compiled in /private/tmp/roth-d26-generalized.lean (no new repo helper).
ℤ coefficient/gcd abstraction would require separate IsBezout/algebra API design, not a
mechanical weakening. No public change applied. No decision needed to complete this cleanup.

## Inequality scan
| Location | Occurrences | Action |
|---|---|---|
| Entire target statement and hypotheses | zero | n/a equality/existential theorem |

## All 42 golfing rules
| Rule | Concrete status |
|---|---|
|1.1|n/a no by exact wrapper|
|1.2|n/a no by rfl|
|1.3|n/a no rw followed by exact on same goal|
|1.4|n/a no simp plus exact chain|
|1.5|n/a no trailing rfl|
|1.6|already anonymous existential witness|
|1.7|n/a no apply then exact|
|1.8|n/a no contradiction|
|1.9|n/a sum_congr membership lambdas need arguments|
|1.10|n/a no have|
|1.11|n/a no apply intro|
|1.12|n/a no show|
|1.13|already obtain z,hz rather than projections|
|1.14|n/a only rw blocks separated by actual work|
|1.15|terminal simp unsqueezed; rw hz plus simp becomes simp [hz]|
|1.16|n/a no nonterminal bare simp; push_cast retained|
|1.17|n/a no shorter natural dot-notation application|
|1.18|n/a no trailing parenthesized argument|
|1.19|n/a no push_neg|
|1.20|n/a public nontrivial theorem; no private trivial witness helper|
|2.1|actual live grind failed to find integer witness|
|2.2|n/a no existing grind prefix|
|2.3|calc first equality consolidated by terminal simp [hz]|
|2.4|n/a no function property goal|
|2.5|n/a no positivity goal|
|2.6|n/a no inequality monotonicity|
|2.7|n/a nonlinear variable products/rational casts; no Nat/Int linear arithmetic goal|
|2.8|actual live aesop made no progress|
|2.9|push_cast normalizes the sum once rather than twice; no numeric computation|
|2.10|n/a unbounded integer existential, not finite decidable computation|
|2.11|n/a no denominators/field identity|
|2.12|ring subgoal with hypotheses removed entirely by direct associativity rewrite; linear_combination unnecessary|
|2.13|n/a no symmetric branches|
|2.14|applied: merged two sum calc steps, direct sum_congr plus mul_assoc|
|2.15|n/a single residual equality after witness|
|3.1|n/a no erw|
|3.2|n/a no legacy continuity/measurability|
|3.3|n/a no omega|
|3.4|n/a no rcases rfl|
|3.5|no broad automation attribute: witness theorem not simplification normalization|
|3.6|n/a no simp_all only|
|3.7|n/a no maxHeartbeats option|
Live multiline calc attempts produced parser errors from insertion into existing calc,
so they were not accepted as tactic failures; isolated full proof then compiled successfully.
Live inline-column simp attempt also had insertion/parser failure; actual edit validated clean.

## Step-back / simplify review
Single tactic grind/aesop/exact? did not close goal; apply? only partial suggestions.
A different denominator-divisibility proof needs more API/casts. The retained Bézout proof
matches source prose; composing a large term would obscure finite sum algebra.
Outcome PASS-THROUGH after direct holistic review; built-in simplify tool unavailable,
so no claim of having invoked one. No duplicated new proof skeleton or helper needed.

## Final scope and arithmetic
Target declaration: 15→12 lines; body 13→10. File 564→561 lines (-3).
Git diff target source: 3 insertions, 6 deletions; only this target proof changed.
Signature, public name, docstring, narrative count (0→0) and all other source bytes preserved.
New external identifier mul_assoc verified by compilation; existing Finset.sum_mul reused.
No import/instance/attribute/limit changes, no sorry/axiom/native_decide/haveI/letI/scaffolding.
Phase 5a refactor none; Phase 5b rename queue empty; public optional Ring proposal above.

## Verification / gates
- Baseline: actual lake build Roth.Separation exit0, /private/tmp/roth-d26-build-baseline.log.
- Final: actual lake build Roth.Separation exit0, /private/tmp/roth-d26-build-final.log.
- Complete unfiltered native LSP: partial=false, timed_out=false, 0 errors / 6 known
  unrelated warnings (header1, exists_int_factors3, exists_det_eq_mul2), 0 target warnings;
  raw /private/tmp/roth-d26finaldiag-final.json (includes complete structured/text payload).
- Independent proof of exact ORIGINAL type, no reference to target theorem in proof:
  /private/tmp/roth-d26-independent.lean; fresh CLI exit0,
  /private/tmp/roth-d26-independent.log. Bézout obtained directly from Finset.gcd_eq_sum_mul.
- Actual built target, exists_int_factors and exists_det_eq_mul print axioms:
  propext, Classical.choice, Quot.sound only; same independent log. No affected private proof.
- Ring candidate: /private/tmp/roth-d26-generalized.lean, fresh CLI exit0,
  /private/tmp/roth-d26-generalized.log (empty). Public proposal only, unapproved/unapplied.
- Native isolation probes initially reported stale-import info while final build ran;
  fresh CLI checks after build completion supersede this limitation.
- Protection check: extracted signature byte-equal to ORIGINAL; replacing the target block
  by sentinel makes pre-worker and current entire source byte-equal. Comments/docs intact.

| Gate | Result / evidence |
|---|---|
| lake_build_file | PASS actual baseline/final commands exit0 |
| definition_protected | PASS no definition changed |
| theorem_statement_protected | PASS exact original signature |
| structure_gate | PASS body10<=30, no branches/conjunction splitting |
| naming_gate | PASS descriptive snake_case, no forbidden forms |
| line_packing_gate | PASS signature width arithmetic above |
| inequality_orientation_gate | PASS zero reversed inequalities |
| cumulative_no_unintended_breakage | module passes; parent owns whole-original/public cumulative/full builds |
| fresh independent original proof / actual axioms | PASS CLI evidence above |

## Eleven completion steps
- [✓] Step1 reference docs and full worker contract read.
- [✓] Step2 full 24-item initial audit recorded before edits.
- [✓] Step2.5 all five actual mathlib search methods recorded.
- [✓] Step2.6 effective-binder/generalisation and literature status recorded.
- [✓] Step2.7 every signature line width recorded; unchanged after edit.
- [✓] Step2.8 inequality scan table recorded.
- [✓] Step3 all42 golfing rules individually classified.
- [✓] Step4 step-back and holistic simplify review recorded (tool unavailable stated).
- [✓] Step5a complete unfiltered native module diagnostics; no target warnings.
- [✓] Step5b protection/style/build/independent proof/axiom gates recorded.
- [✓] Step6a rename queue empty; no shared sidecar mutation.

## Buzz pass
Outcome FAST-BOARD for target. Actual isolated repository command, after all Lean/MCP/build
requests drained: lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0
Roth/Separation.lean; exit0. Raw /private/tmp/roth-d26-final-profile.log; anchored table
/private/tmp/roth-d26-final-profile.log.json, parser /private/tmp/roth-separation-profile-table.py.
Target one outer command15.045ms + one outer asynchronous proof104.543ms =119.588ms.
Valid preceding actual unchanged-source baseline /private/tmp/roth-d25-final-profile.log(.json):
21.733+231.229=252.962ms. Both under750ms repeat trigger and1000ms budget; no repeat required.
Downstream actual final anchors also captured: exists_int_factors50.333+588.417=638.750ms;
exists_det_eq_mul102.116+392.834=494.950ms; proofs unchanged. These measurements do not imply
whole-project speedup. No nested node double counting, limit raises, profile scaffolding,
or overbudget target deferral. Only target performance gate owned here; parent owns all26.

## Freeze / ownership revocation
All Lean/MCP/compiler/build/profile requests completed and drained (profile exit0 last).
Final Roth/Separation.lean SHA256:
93d969933c89724c1c9d7a9ca23a76290e4af8bd3793307c34e95d3fbd1624dc
Source frozen; revoke ALL source ownership, including the target and all possible callers.
Report-only henceforth. No Git/shared progress mutations. Parent must complete cumulative
original/public/all-actual compatibility and sequential full project then LeanEval, commit/push.
Optional Ring generalisation remains unapproved/unapplied; it does not block this proof cleanup.

## Owner cumulative publication gates

Source FROZEN SHA256 `93d969933c89724c1c9d7a9ca23a76290e4af8bd3793307c34e95d3fbd1624dc`; leaf ownership revoked and requests drained before owner gates. Owner probe `49673` exit0,40.60s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d26-compatibility.{lean,log,json}`. Owner build session `79694` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,120.15s/27.37s; source hash stable. `/private/tmp/roth-separation-d26-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
