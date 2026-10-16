# `MvPolynomial.degreeOf_taylor_le` dedicated audit

Target: `Roth/Taylor.lean:164–168` (original range 182–186).
Parent-supplied branch/baseline: `ramin-cleanup` / `e3400a8`.
Start SHA256: `4cd871acc4a0ad26ceba2c01bef9ee5c88e0f5117254a50d24a895b56af32f7a`.
Frozen SHA256: `1f69c55d06c8b562930bb9bbc90e9ab3a676f2491d6ddbf4f8dd4c08b8fe3de8`.
Source ownership revoked immediately after local gates; all subsequent work is report-only.

Read both SKILL.md files, the full worker contract, golfing-rules.md, proof-patterns.md,
mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, relevant style-rules.md
sections, and mathlib-review-stages.md normal-form, syntactic-generality and documentation sections.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

## Full audit (24 items)

1. LINT: native full-file diagnostics show no target warning/error; the existing line-1
   copyright/header warning remains outside ownership.
2. HAVE SCAN: no `have` in original or final proof, hence no use-count candidates.
3. SET_OPTION: no declaration-local option or resource-limit increase.
4. SIMP SQUEEZE: no simp call in original/final proof.
5. NAMING: `degreeOf_taylor_le` describes the variable-degree comparison; mixed-case
   `degreeOf` is the established mathlib operation name. No forbidden name pattern or abbreviation.
6. LINE PACKING: both signature lines measured below; neither requires repacking.
7. BY PLACEMENT: `:= by` ends line 165.
8. FORMAT: fixed both ordinary lambda arrows `=>` to `↦` at line 166. Two-space proof
   indentation, no empty proof lines/trailing whitespace/local instance syntax.
9. COMMENTS: no inline proof comments present; both docstring lines preserved verbatim.
10. DOCSTRING: existing public description and source citation preserved under explicit
    API/doc preservation and lean4 Rule A. No documentation rewrite proposed.
11. VISIBILITY: preserve public API; `Roth/Index.lean:243` directly uses this theorem.
12. STRUCTURE: three proof-body lines; no conjunction or long branch; no extraction needed.
13. MATHLIB: five methods below; retain support/coefficient proof using `degreeOf_le_iff`.
14. JUNK DEF: n/a, target is a theorem.
15. EXISTS LEMMA: n/a, no existential conclusion or witness helper.
16. SHOW vs CHANGE: n/a, neither occurs.
17. PUSH_NEG: n/a, no negation tactic occurs.
18. GENERALISE: all six effective parameters classified below; no accepted weakening.
19. INEQUALITY: `≤` is already correctly oriented; zero `≥`/`>` in signature.
20. NORMAL-FORM: degree bound uses mathlib's `degreeOf` and `≤`; support characterization
    stays inside proof. No equivalence-family restatement needed.
21. SYNTAX-GEN: OK; arbitrary variables, coefficients, translation and polynomial, without
    finiteness/decidability/domain assumptions. Bound directly composes with caller bounds.
22. IMPORT-FANOUT: n/a, no new imports.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing ascriptions introduced in diff.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues found/fixed: one formatting issue (two lambda arrows). Before 5 declaration lines,
after 5, saved 0; proof remains 3 lines. Rules applied: lambda syntax style rule.
Refactoring needed: none. No rename queued. No public-wrapper deletion performed/proposed.

## Mathlib search-status

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | `multivariate polynomial degreeOf substitution translation X plus constant does not increase degree` | `totalDegree_rename_le`, `degrees_rename`, `degreeOf_eq_natDegree`; related, no direct replacement |
| B Loogle | `MvPolynomial.degreeOf, MvPolynomial.eval₂` | empty items, no tool error |
| C LeanSearch | `MvPolynomial degreeOf eval₂ substitution bound` | `aeval_natDegree_le`, `ChevalleyThm.MvPolynomialC.degBound`, `eval₂`; first bounds univariate natDegree by totalDegree, not this variable-specific result |
| D source | `degreeOf_(eval|aeval|bind)`, `degreeOf.*X_add`, `degreeOf_taylor_le`, then degree/degrees evaluation variants in MvPolynomial source | no direct substitution bound; `degreeOf_le_iff` at Degrees.lean:235 verified; project Hasse vanishing at HasseDeriv.lean:213 |
| E local names | `degreeOf_eval`, then `degreeOf_le_iff` | first empty with index unavailable (not absence evidence); second located `MvPolynomial.degreeOf_le_iff`, index warming |

Auxiliary variants checked: `eval₂`/`aeval`/`bind`, `degrees` versus `degreeOf`,
renaming bounds and `degreeOf_eq_natDegree`. Source files Degrees.lean and Eval.lean
inspected/search-checked. Common-equivalents table: no matching topology/finiteness bucket.
Conclusion: partial match `degreeOf_le_iff`; retain local public translation result and
build on this support characterization plus existing `coeff_taylor` and Hasse vanishing.
This is not a claim of exhaustive mathematical absence. A native `exact?` probe at the
pre-proof state failed; `apply?` offered `degreeOf_le_iff.mpr` and generic arithmetic
reformulations, reached its time budget, and did not produce a closed replacement.
No new declaration/API-extraction signal: the existing three lines express the argument
without casts, wrapper round-trips, or typeclass plumbing.

## Generalisation status

| Parameter | Class | Used as | Mechanical candidates / evidence | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | index of α, j, polynomial | Drop would leave dependent binder types ill-formed; already independently universe polymorphic; no point-local/strict candidates | type dependency and compiled #check | keep |
| `{R : Type*}` | type variable | codomain of α and polynomial coefficients | Drop would leave dependent binder types ill-formed; already universe polymorphic; no concrete scalar restriction | type dependency and compiled #check | keep |
| `[CommSemiring R]` | typeclass | required by taylor and degreeOf | Drop / parent Semiring cannot support existing taylor API; scratch Semiring substitution reports failed synthesis `CommSemiring S` | CLI negative probe; no live source substitution | keep |
| `(α : σ → R)` | structure value | translation input | Drop with autoImplicit false reports unknown α at conclusion; no proposition/point-local/strict weakening; changing assignment type restates translation | CLI negative probe | keep |
| `(j : σ)` | structure value | selected degree | Drop with autoImplicit false reports unknown j at conclusion; no hypothesis to weaken | CLI negative probe | keep |
| `(P : MvPolynomial σ R)` | structure value | translated and original polynomial | Drop with autoImplicit false reports unknown P at conclusion; replacing polynomial carrier is a restatement | CLI negative probe | keep |

Negative probes were generated under `/private/tmp/Taylor-decl15-{drop-alpha,drop-j,drop-P,semiring}.lean`.
Each exited 1 with the stated dependency error; insertion after the existing attached docstring
also caused an independent `unexpected ... expected lemma` parser diagnostic. They therefore
establish the reported syntactic/instance obstacles, not a clean generalised theorem validation.
No candidate is marked diagnostics-clean or applied; no claim of a live-file weakening trial.
No explicit proposition, decidability, global continuity, strict inequality, bundled property,
or concrete-number hypothesis exists for the catalogue's other entries.
Inversion check: the abstract degree/support implication already exists as `degreeOf_le_iff`;
translation-specific coefficient identification remains the substantive input. No new abstract
restatement proposed. Big-change candidates: none.

## Literature search status

WebSearch query: `multivariate polynomial translation degree in each variable commutative semiring generalization`.
Top three hits were documentation mirrors of Mathlib.RingTheory.MvPolynomial.Basic at
[IISc](https://math.iisc.ac.in/~gadgil/proofs-and-programs-2023/doc/Mathlib/RingTheory/MvPolynomial/Basic.html),
[PhysLean](https://physlean.com/docs/Mathlib/RingTheory/MvPolynomial/Basic.html), and
[lean4.party](https://lean4.party/docs/Mathlib/RingTheory/MvPolynomial/Basic.html).
The authoritative [mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/Basic.html)
also appeared: variable-degree bounds are represented by `restrictDegree`.
[Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring) describes polynomial
construction over rigs and treating multivariate polynomials as univariate over a smaller
coefficient ring. Inference: existing commutative-semiring, arbitrary-index statement already
covers the standard algebraic breadth relevant to translation. No literature-supported
assumption drop or useful API restatement identified. No math ChatGPT MCP available among
discovered tools; unavailable, not silently skipped. Literature-driven big changes: none.

## Signature width and inequalities

Compiled isolated `#check` at `format.width 100`:

```lean
@degreeOf_taylor_le : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (j : σ)
  (P : MvPolynomial σ R), degreeOf j ((taylor α) P) ≤ degreeOf j P
```

| Signature line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 164 | 71 | conclusion `degreeOf j (taylor α P) ≤ degreeOf j P := by` (44) | 71 + 1 + 44 = 116 > 100 | ok |
| 165 | 48 | no next signature line | n/a, proof next | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | conclusion L165 | `degreeOf j (taylor α P) ≤ degreeOf j P` | already oriented | none |
| n/a | entire signature | zero `≥`/`>` | none needed | no `_ge_`/`_gt_` segment |

## Golfing rules (all 42)

1.1 n/a: original is not a by-exact wrapper.
1.2 n/a: no by-rfl.
1.3 n/a: rw simplifies a contradictory hypothesis; final `he rfl` is not `rwa`'s goal.
1.4 n/a: no simp/exact pair.
1.5 n/a: no simp/trailing rfl.
1.6 n/a: no constructor.
1.7 n/a: no apply/exact pair.
1.8 n/a: no by_contra/push_neg sequence.
1.9 n/a: both lambdas bind variables used nontrivially; normalized their syntax to ↦.
1.10 n/a: no have.
1.11 already uses refine with lambdas.
1.12 n/a: no show.
1.13 n/a: no projected have.
1.14 n/a: only one rw call.
1.15 n/a: no simp only.
1.16 n/a: no bare nonterminal simp.
1.17 already uses `.2`, `.1`; final `he rfl` is direct application.
1.18 already no removable outer parentheses around lambdas.
1.19 n/a: no push_neg.
1.20 n/a: no existential helper.
2.1 tried native `grind`: failed on degree inequality, no polynomial relation inferred.
2.2 n/a: original has no grind.
2.3 considered simpa consolidation; native multiline snippet insertion had parser errors,
     so no success claimed; retained compact, compiled rw/contradiction proof.
2.4 n/a: no analytic function property.
2.5 n/a: goal is general degree comparison, not positivity/nonzero.
2.6 tried native gcongr: no progress.
2.7 tried native lia: failed, missing substantive degree relation.
2.8 tried native aesop: failed, no progress.
2.9 n/a: no numeric computation/cast.
2.10 n/a: arbitrary symbolic polynomial degree, no closed finite computation.
2.11 n/a: no denominator identity.
2.12 n/a: no ring/ring_nf ending or ring equation.
2.13 n/a: no symmetric branches.
2.14 n/a: no calc.
2.15 n/a: refine creates a single subgoal.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability.
3.3 n/a: no omega retained; lia trial recorded in 2.7.
3.4 n/a: no rcases.
3.5 no attribute addition: degree inequality retained as ordinary public bound.
3.6 n/a: no simp_all.
3.7 n/a: no resource-limit option.

Step-back reflection: native simp failed to progress, exact? failed, and apply? suggested
precisely the existing support criterion. Lean-Finder's univariate degree equivalence and
LeanSearch's total-degree bound require more machinery and do not improve this direct
coefficient-vanishing argument. No have blocks/redundant show/calc remain. Keep proof
strategy, apply only the routine lambda syntax correction.

## Verification and gates

Native `lean_diagnostic_messages` after the edit returned `success: true`, `partial: false`,
`timed_out: false`, no failed dependencies, and only the original line-1 header warning.
Target range has no warning/error. No LSP fallback was needed.
Actual `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited 0: 1439 jobs, Taylor built in
18s; replayed Box/HasseDeriv and Taylor header warnings only.
`/Users/ramin/.elan/bin/lake env lean /private/tmp/Taylor-decl15-isolated.lean` exited 0.
The isolated file uses the exact pretarget prefix, excludes original target and all later
source, then defines the target with its unchanged original type and final proof. It imports
Box/HasseDeriv via the prefix, never Taylor. `#print axioms` reports exactly
`[propext, Classical.choice, Quot.sound]`.

Captured worker diff with `diff -u /private/tmp/Taylor-decl15-before.lean Roth/Taylor.lean`:
only two lambda arrows on line 166 changed. No Git operations or full-project build run.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0 |
| definition_protected | pass | no def/abbrev changes |
| theorem_statement_protected | pass | signature byte-identical |
| structure_gate | pass | 3 body lines, no conjunction/branch |
| naming_gate | pass | descriptive established degreeOf operation name, no forbidden pattern |
| line_packing_gate | pass | both measured rows ok |
| inequality_orientation_gate | pass | zero reversed inequalities |

Overall local gates: pass. Parent full build and separate LeanEval are pending parent evidence.

## Required phase checklist

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method search recorded.
- [✓] Step 2.6 — every effective parameter classified; probe limitations explicit.
- [✓] Step 2.7 — complete signature-width table and compiled width reference.
- [✓] Step 2.8 — inequality scan table.
- [✓] Step 3 — all 42 golfing rules have evidence or concrete n/a reason.
- [✓] Step 4 — step-back reflection and exact?/apply? probes.
- [✓] Step 5a — native diagnostics complete and clean in target.
- [✓] Step 5b — diff-gate table and actual successful module build.
- [✓] Step 6a — no rename needed, sidecar unchanged.
