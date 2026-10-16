# Phase 4: Roth.normOne_zero

Dedicated single-declaration worker; source range Roth/CoeffNorm.lean:60–62
(attribute plus theorem and proof); docstring at line 59. C5 is the standard descriptive
norm-zero simp API. Scope: this declaration and this report only. No Git operations,
shared-log writes, other source changes, dependency or toolchain changes.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read the mathlib-quality
and lean4 SKILL.md files, the complete worker contract
`/private/tmp/roth-coeffnorm-worker-contract.md`, style-rules.md,
naming-conventions.md, and mathlib-review-stages.md from
`/Users/ramin/.codex/skills/mathlib-quality/references/`.

## Result

Before: 2 theorem/proof lines. After: 2. Saved: 0.
The existing `by` / `simp [normOne]` proof is retained after actual candidate testing.
Docstring, simp attribute, visibility, universe parameter, statement, and proof unchanged.
No local refactoring or rename needed. No issues fixed because none were found in scope.

Source frozen and source ownership relinquished to the parent at SHA256
`62cc00913634a7662c2313a3c36a98f0891f663db3577869a49ff676bbd4e1e5`.
No source edits were made before or after freeze. Post-freeze source block equality
against the starting literal was checked by Python and returned True; whole-file hash
also matched. The parent acknowledged revoked source ownership.

## Baseline and final diagnostics

Parent-provided baseline: sequential full build and separate LeanEval, session 36875, exit 0.
This worker did not rerun a full build. Native Lean MCP discovery used ALL_TOOLS metadata.
Both baseline and final unfiltered native `lean_diagnostic_messages` calls on the entire
file returned `partial=false`, `success=true`, `timed_out=false`, no failed dependencies,
0 errors, and the same 6 out-of-scope warnings. Target range has no warning.
Warnings are header (line 1), four public DecidableEq parameters (normOne_mul_le,
normOne_prod_le, normOne_det_le, abs_coeff_det_hasseDeriv_le), and hC in normOne_det_le.
Header is user-preserved; the four DecidableEq parameters and hC await the user's API
scope decision. No suppression or unapproved argument removal was applied.

Final module command `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm` completed
successfully, exit 0 (1658 jobs, replayed module); same existing module warnings.
Dependency replay also showed existing Box and HasseDeriv header warnings. No new warning.
Native tools returned completely; no fallback, cancellation, cached-import workaround,
or fresh CLI workaround was necessary.

## Full audit

1. LINT: none in the declaration; six outside warnings recorded above.
2. HAVE SCAN: no `have` declarations, hence no use-count/inlining candidate.
3. SET_OPTION: none in scope; no heartbeat or recursion override.
4. SIMP SQUEEZE: one terminal `simp [normOne]`; leave unsqueezed.
5. NAMING: normOne_zero describes the definition applied to zero, has the standard
   `_zero` suffix, and contains no forbidden pattern or abbreviation. Embedded
   lowerCamelCase `normOne` is the definition name, as in standard mathlib API names.
6. LINE PACKING: one 63-codepoint signature line; complete table below.
7. BY PLACEMENT: `by` is at the end of the signature line.
8. FORMAT: two-space tactic indentation, one tactic, no empty internal line or trailing
   space; no `haveI`/`letI`.
9. COMMENTS: no inline proof comments; existing one-sentence docstring preserved verbatim.
10. DOCSTRING: public basic API lemma has the succinct existing zero-polynomial description;
    no proof sketch to relocate and no nontrivial application caveat to add.
11. VISIBILITY: retain public zero-value simp API; not a private implementation helper.
12. STRUCTURE: one proof-body line, no conjunction, branch, or extraction candidate.
13. MATHLIB: five methods, compiled generic routes, and six-rule review below.
14. JUNK DEF: n/a, this declaration is a theorem; normOne definition is outside ownership.
15. EXISTS LEMMA: n/a, no existential statement/witness helper.
16. SHOW vs CHANGE: n/a, neither occurs.
17. PUSH_NEG: n/a, no negation tactic.
18. GENERALISE: only the already universe-polymorphic implicit σ; actual drop-test below.
19. INEQUALITY: zero reversed inequalities; occurrence scan below.
20. NORMAL-FORM: already canonical `normOne 0 = 0`, with zero on RHS and simp orientation.
21. SYNTAX-GEN: OK; a no-argument simp theorem is convenient for rewriting and elaboration.
22. IMPORT-FANOUT: n/a, no new imports or file movement.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing casts in diff (empty diff).
    Existing `(0 : MvPolynomial σ ℤ)` fixes the polynomial and variable types.
24. INSTANCE-NAME: n/a, theorem, no instance declaration or new instance.

Issues to fix: none. Refactoring needed: none for this target.

## Mathlib search-status

A. Lean-Finder: query "The l1 coefficient norm of the zero multivariate polynomial is
   zero"; top 3 hits Polynomial.gaussNorm_zero, MvPolynomial.monomial_zero,
   Polynomial.hilbertPoly_zero_left. These concern other constructions, not Roth.normOne.
B. Loogle: broad `"norm", "zero"` returned unrelated Rat normalize/BV normalization hits.
   Refined actual pattern `Finset.sum ∅ _ = 0` found Finset.sum_empty, the generic
   finite-sum building block used by the current proof.
C. LeanSearch: query "The sum of the absolute values of the coefficients of the zero
   polynomial is zero"; top 3 Polynomial.coeff_zero, MvPolynomial.coeffs_zero,
   Polynomial.leadingCoeff_eq_zero. Relevant support/coefficients building blocks,
   not a theorem about this project's definition.
D. Untruncated `rg -n 'normOne_zero' .lake/packages/mathlib/Mathlib` returned no hit.
   Source search found MvPolynomial.support_zero at Algebra/MvPolynomial/Basic.lean:492.
   No conclusion of generic absence is inferred from grep alone.
E. Native lean_local_search `norm_zero` returned Algebra.norm_zero,
   CStarModule.norm_zero, MeasureTheory.Lp.norm_zero, Module.Basis.norm_zero.
   `support_zero` returned DFinsupp, DirectSum, Finsupp, FreeAbelianGroup variants.
   Index was warming, so negative-index evidence is explicitly not claimed.
   Existing relevant names were independently verified by the compiled reproof below.

Auxiliary variants: support_zero, coeff_zero, coeffs_zero, sum_empty, norm_zero,
monomial_zero, gaussNorm_zero. Common-equivalents table: no listed bucket matches;
finite-support zero sum is the relevant primitive.

Concluded: partial mathlib match support_zero + sum_empty; keep the project's
zero-value simp API and its direct simplification proof. This theorem exposes the
project-defined coefficient norm, rather than duplicating a theorem about the same
already-bundled mathlib object. The frozen public API is explicitly preserved by scope.

Six strict rules checked: (1) no new wrapper added; this existing simp API belongs to
normOne, (2) all five searches plus actual generic route probes performed,
(3) auxiliary variants inspected, (4) no custom predicate or replaceable assumption,
(5) no equivalent theorem for the same public object was found (exact?/apply? produced
Real.ext_cauchy rfl, not an existing normOne theorem), (6) no import/API replacement to
explain in the module docstring. Scope does not permit changing that existing docstring.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable/universe | index of MvPolynomial | drop binder with autoImplicit false | yes, native lean_run_code | fails `Unknown identifier σ`; keep |

Already arbitrary Type u_1, as width-100 #check confirms. No class parents, strict
hypotheses, global predicates, structures, or decidability assumptions exist to weaken
or point-localise. Actual drop probe used `import Roth.CoeffNorm`,
`set_option autoImplicit false`, and `example : Roth.normOne (0 : MvPolynomial σ ℤ) = 0
:= by simp [Roth.normOne]`; expected error at σ confirms essential type dependence.
The successful independent type/reproof probe below confirms no hidden Fintype or
DecidableEq constraint. This isolated candidate did not alter production source.

Inversion check: after unfolding normOne, the content is the generic empty finite-sum
fact, already supplied by Finset.sum_empty. No missing abstract helper is warranted.
Generalising coefficients or codomain changes the normOne definition itself and is
outside this declaration; no such public restatement is proposed by this elementary fact.
Big-change candidates: none for this target.

## Public literature search

Web query: `polynomial coefficient l1 norm zero generalization normed vector space`.
Top three returned hits were:

1. [Normed vector space](https://en.wikipedia.org/wiki/Normed_vector_space) — norm axioms;
   discovery result only, not used as primary technical evidence.
2. [Joseph Powers lecture notes](https://www3.nd.edu/~powers/ame.30314/notes.pdf) — normed
   spaces and zero-length property.
3. [Polynomial least deviating from zero](https://encyclopediaofmath.org/wiki/Polynomial_least_deviating_from_zero)
   — approximation norms, not the target's coefficient norm; no weakening suggested.

A further primary source returned by the same query, [André Tits, ENEE 664 notes,
September 2024](https://user.eng.umd.edu/~andre/664.pdf), was opened successfully:
it discusses polynomial coefficient sequences and their ℓ¹ norm. Inference from the
finite coefficient sum: zero polynomial has empty support independently of finite
variable type or decidable equality. The general zero law needs no additional target
hypothesis. Math MCP n/a: no chatgpt-math tool available in ALL_TOOLS metadata.
Literature-driven big-change candidates: none.

## Line packing

Width-100 native Lean probe output:

```lean
@Roth.normOne_zero : ∀ {σ : Type u_1}, Roth.normOne 0 = 0
```

| Sig line | Chars | Next signature token | current + 1 + next ≤ 100? | Action |
|---|---:|---|---|---|
| 61 | 63 | none; proof body follows | n/a, complete signature including := by fits | ok |

Measured with Python Unicode codepoint length. No other signature line exists.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| n/a | entire signature and parameters | no ≥ or > | none | none; no _ge_ or _gt_ |

Post-freeze mechanical signature scan counted 0 reversed inequalities.

## Actual tactic probes

Native lean_multi_attempt at line 62, in the live pre-theorem context:

| Candidate | Result |
|---|---|
| rfl | closes, no diagnostics |
| simp | fails: simp made no progress, target normOne 0 = 0 remains |
| simp [normOne] | closes, no diagnostics; retained |
| grind [normOne] | error: grind failed; empty goals alone is not treated as success |
| aesop | closes, no diagnostics; no clarity/length advantage |
| exact? | closes, suggestion exact Real.ext_cauchy rfl |
| apply? | closes, same Real.ext_cauchy rfl suggestion |

## Golfing rule pass (all 42 rules)

- 1.1 by exact: n/a, proof is simp rather than exact wrapper.
- 1.2 by rfl: n/a in source; actual rfl alternative succeeds but current proof exposes
  stable support/sum API, avoiding reduction through real/finite-support representations.
- 1.3 rw + exact: n/a, neither chain occurs.
- 1.4 simp + exact: n/a, simp already closes.
- 1.5 trailing rfl: n/a, no trailing tactic.
- 1.6 constructor chain: n/a, atomic equality.
- 1.7 apply + exact: n/a, no application chain.
- 1.8 contradiction: n/a, no contradiction proof.
- 1.9 eta lambdas: n/a, no lambda.
- 1.10 single-use have: n/a, no have.
- 1.11 apply + intro: n/a, no introduction.
- 1.12 redundant show: n/a, no show.
- 1.13 projections: n/a, no pair/have.
- 1.14 consecutive rw: n/a, no rw.
- 1.15 terminal simp only: n/a, terminal simp already unsqueezed.
- 1.16 nonterminal simp: n/a, sole simp closes.
- 1.17 dot notation: n/a, no explicit theorem application needing dot notation.
- 1.18 <|: n/a, no nested application parentheses.
- 1.19 push_neg: n/a, none.
- 1.20 trivial existential helper: n/a, no existential.
- 2.1 whole-proof grind: tried grind [normOne], failed; keep simp.
- 2.2 delete before grind: n/a, no grind in source or preceding tactic.
- 2.3 simpa consolidation: n/a, no simp-followed-by-close sequence.
- 2.4 fun_prop: n/a, no function regularity proposition.
- 2.5 positivity: n/a, equality to zero rather than positivity/nonnegativity target.
- 2.6 gcongr: n/a, no inequality or monotonicity.
- 2.7 lia/omega: n/a, equality involves normOne and ℝ, not Nat/Int arithmetic.
- 2.8 aesop: tried successfully; unchanged proof is more direct and equally one tactic.
- 2.9 norm_num/norm_cast: n/a, no numeric arithmetic/cast goal after support simplification.
- 2.10 decide: n/a, no computational decidability proof of real norm equality.
- 2.11 field_simp/ring: n/a, no denominator or ring identity.
- 2.12 linear_combination: n/a, no ring-ending proof or algebraic hypotheses.
- 2.13 wlog: n/a, no symmetric branches.
- 2.14 calc collapse: n/a, no calc.
- 2.15 multiple-goal closing: n/a, one atomic goal.
- 3.1 erw: n/a, absent.
- 3.2 continuity/measurability: n/a, absent.
- 3.3 omega→lia: n/a, no arithmetic tactic.
- 3.4 rcases with rfl: n/a, absent.
- 3.5 automation attributes: existing @[simp] is exactly the useful zero normal form;
  retained and independently tested by bare simp after importing the compiled module.
- 3.6 simp_all only: n/a, absent.
- 3.7 limits: n/a, no maxHeartbeats override.

## Step-back reflection

Whole proof is already one tactic. rfl works but exposes definitional implementation
rather than the support/sum simplification API; aesop hides the elementary empty-sum
reason and supplies no shorter tactic. exact?/apply? suggest a longer real-representation
term. Term-mode Real.ext_cauchy rfl is less direct. No have composition, dead step,
case split, cast chain, or missing helper exists. Keep the source unchanged.

## Independent compiled verification

Native lean_run_code succeeded (timed_out=false) on this entire code:

```lean
import Roth.CoeffNorm
set_option format.width 100
#check @Roth.normOne_zero
example : ∀ {σ : Type*}, Roth.normOne (0 : MvPolynomial σ ℤ) = 0 := @Roth.normOne_zero
example {σ : Type*} : Roth.normOne (0 : MvPolynomial σ ℤ) = 0 := by
  simp only [Roth.normOne, MvPolynomial.support_zero, Finset.sum_empty]
example {σ : Type*} : Roth.normOne (0 : MvPolynomial σ ℤ) = 0 := by simp
#print axioms Roth.normOne_zero
```

The second example re-proves the original statement without using normOne_zero;
explicit `simp only` here is a verification probe, not production terminal-simp style.
Axioms exactly `[propext, Classical.choice, Quot.sound]`. No sorry/new axiom/limit or
linter suppression introduced. Original signature verified independently by exact term.

## Diff gates

Actual owned-block comparison to starting literal: identical=True; diff empty.
The script also measured the signature and checked naming/inequalities/forbidden tokens.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | lake build Roth.CoeffNorm, exit 0, 1658 jobs |
| definition_protected | ✓ pass | empty source diff; all definitions untouched |
| theorem_statement_protected | ✓ pass | exact starting source block equality; independent original type |
| structure_gate | ✓ pass | body 1 line; no conjunction or branch |
| naming_gate | ✓ pass | forbidden-pattern regex false; descriptive normOne_zero |
| line_packing_gate | ✓ pass | complete 63-codepoint signature table above |
| inequality_orientation_gate | ✓ pass | actual scan count 0; occurrence table above |
| complete_LSP | ✓ pass | final partial=false, success=true, no errors/dependency failure |
| standard_axioms | ✓ pass | propext, Classical.choice, Quot.sound only |
| cumulative_no_unintended_breakage | ✓ pass | no source change; target module build succeeds |

Overall: pass. Renames queued: none. Comments preserved: existing docstring unchanged;
no proof comments present. Pending: only the existing outside-warning API decisions
listed above; no declaration-specific pending work.

## Required phase checklist

- [✓] Step 1 — all required reference docs read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method search-status and generic probes reported.
- [✓] Step 2.6 — every parameter audited, actual drop probe and literature search reported.
- [✓] Step 2.7 — width-100 #check and every signature-line width table reported.
- [✓] Step 2.8 — complete inequality scan table reported.
- [✓] Step 3 — all 42 golfing rules have an explicit status.
- [✓] Step 4 — step-back reflection and tested alternatives reported.
- [✓] Step 5a — complete final live-file diagnostics: 0 errors, 0 target warnings.
- [✓] Step 5b — actual module build and all diff gates pass.
- [✓] Step 6a — no rename needed; sidecar untouched.
