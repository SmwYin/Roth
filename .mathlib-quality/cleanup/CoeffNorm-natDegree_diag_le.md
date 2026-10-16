# Phase 4 — Roth.natDegree_diag_le

Owned declaration: `Roth/CoeffNorm.lean:178–184` (7 declaration lines, 5 proof lines).
Only source change: normalize the two mathematical lambda arrows from `=>` to `↦`.
Public signature and original two-line docstring are byte-identical. No other source touched.
SOURCE FROZEN whole-file SHA256:
`71a51cfdf91108c0cf3983c4718bfc70d51001ed9e2d8c45573a77220764e366`.
Ownership was revoked after that hash; all subsequent work is evidence/report only.

## Preparation

Read both skill files and the complete worker contract. Read golfing-rules.md,
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md,
style-rules.md, naming-conventions.md, and relevant mathlib-review-stages.md sections.
Inherited baseline: full `lake build` then separate `lake build Roth.LeanEval`, exit 0,
as supplied by coordinator (LeanEval session 47381); not repeated here.
Pinned Lean/mathlib unchanged. Native Lean MCP used successfully; no fallback needed.

Mathematics: each supported monomial has exponent `k j ≤ degreeOf j P ≤ r j`.
After substituting every variable by `X`, its exponent is `∑ j, k j ≤ ∑ j, r j`.
The degree of a sum is bounded by the largest summand degree, including cancellation/zero.

## Full audit

1. LINT: no warnings in target. Complete file diagnostics have zero errors and the same six
   outside warnings: header, four unused DecidableEq parameters, and hC. Outside scope.
2. HAVE SCAN: no `have` bindings.
3. SET_OPTION: none in the declaration; no limits or suppressions introduced.
4. SIMP SQUEEZE: no simp calls in retained proof.
5. NAMING: `natDegree_diag_le` describes the operation and bound, with standard natDegree
   capitalization and `_le`; no forbidden abbreviations or numeric patterns. No rename.
6. LINE PACKING: both signature lines measured, table below; no repack remains.
7. BY PLACEMENT: `:= by` terminates signature line 179.
8. FORMAT: two-space tactics, four-space signature continuation, no blank lines or semicolons;
   changed both lambda arrows to `↦`; no haveI/letI.
9. COMMENTS: no proof comments existed; docstring fully preserved, zero removed.
10. DOCSTRING: existing statement and source quotation preserved under explicit API contract.
11. VISIBILITY: descriptive public degree API retained as required; no privacy change.
12. STRUCTURE: five proof lines; no conjunction, case branches, or extraction trigger.
13. MATHLIB: five searches below; partial general evaluation bound found, no direct replacement.
14. JUNK DEF: n/a, target is a theorem.
15. EXISTS LEMMA: n/a, no existential conclusion or private witness wrapper.
16. SHOW vs CHANGE: no show/change.
17. PUSH_NEG: none.
18. GENERALISE: every parameter reviewed and drop-tested below; original API retained.
19. INEQUALITY: one `≤` in hP and one `≤` in conclusion; zero reversed inequalities.
20. NORMAL-FORM: natDegree and component degreeOf upper bounds are canonical natural-degree
    forms; no equality/iff conversion needed.
21. SYNTAX-GEN: OK; caller supplies the componentwise degree bound directly.
22. IMPORT-FANOUT: n/a, no import change; general evaluation route would need extra import.
23. CASTS: zero dropped, zero cross-type, zero load-bearing casts in diff.
24. INSTANCE-NAME: n/a, theorem declares no instance.

Issues found: two lambda arrow spellings, both fixed. Refactoring needed: none.

## Mathlib search-status

| Method | Actual query | Findings |
|---|---|---|
| A Lean-Finder | degree diagonal substitution multivariate polynomial at X bounded sum degreeOf | `MvPolynomial.aeval_natDegree_le`, plus unrelated Chevalley degree bounds |
| B Loogle | `MvPolynomial.eval₂, Polynomial.natDegree` | `Polynomial.eval₂_homogenize_of_eq_one`, unrelated to required estimate |
| C LeanSearch | multivariate polynomial evaluated at polynomials natural degree at most sum variable degrees | `MvPolynomial.aeval_natDegree_le`, restrictTotalDegree, homogeneous aeval |
| D source rg | aeval_natDegree_le, totalDegree_le.*sum, totalDegree.*degreeOf, natDegree.*eval₂ | evaluation theorem at RingTheory/Polynomial/Basic:898; degreeOf_le_totalDegree is reverse direction |
| E lean_local_search | natDegree_eval; aeval_natDegree_le | polynomial evaluation helpers; exact aeval theorem confirmed in source (index warming, not used as absence evidence) |

Auxiliary variants searched: totalDegree_le, degreeOf_le_totalDegree,
totalDegree_le_degrees_card, totalDegree_le_of_support_subset, totalDegree_finsetSum.
Existing proof building blocks verified by `#check`: natDegree_sum_le_of_forall_le,
Finsupp.degree_eq_sum, monomial_le_degreeOf.
Common-equivalents table: no matching discrete/finiteness/bornology bucket.

The evaluation theorem is a partial match: it bounds degree by totalDegree times a uniform
substitution degree. In current imports, an actual `#check MvPolynomial.aeval_natDegree_le`
fails `Unknown constant`; its source shows the additional totalDegree premise.
Using it requires an additional import and proving the same exponent estimate separately.
Keep the current explicit monomial argument, which directly proves the desired componentwise
bound in five lines. No absence claim is made. Six strict rules reviewed: no new wrapper,
all search routes tried, auxiliary variants checked, no custom predicate, no exact duplicate
identified for deletion, and existing module documentation preserved under scoped contract.

## Generalisation status

All experiments used standalone native `lean_run_code` with `autoImplicit false`; source
signature was never mutated. These are actual elaboration probes, not speculative success.

| Parameter | Class/use | Mechanical candidates and actual result |
|---|---|---|
| `{σ : Type*}` | type variable for polynomial/index sums | Drop: Unknown identifier σ. Already universe polymorphic; no weaker universe needed. Point-local/strict/class parent n/a: type parameter. |
| `[Fintype σ]` | typeclass, finite total sum and degree_eq_sum | Drop and replace by `[Finite σ]`: both fail to synthesize Fintype σ in statement and degree_eq_sum. No algebraic/analytic parent weakening applies. |
| `(P : MvPolynomial σ ℤ)` | structure value, support/coeff/diag/degreeOf | Drop: Unknown identifier P in hP. Point-local/strict weakening n/a: polynomial value. Abstract coefficient semiring would require changing diag itself, outside fixed API. |
| `{r : σ → ℕ}` | structure value, component and total bound | Drop: Unknown identifier r. Point-localizing does not support sum over all variables. No strict hypothesis or typeclass parents. |
| `(hP : ∀ j, degreeOf j P ≤ r j)` | proposition, used at every sum coordinate | Drop: Unknown identifier hP at closing step. Already weak ≤, no strict→weak candidate. Pointwise one-coordinate form cannot bound all summands. |

No decidability parameter is present. No hypothesis can be unbundled. No small-safe change
verified, so none applied. Inversion check: diag unfolds to monomial sum; the general abstract
evaluation estimate is already mathlib's aeval_natDegree_le, so no new abstraction/helper.
Optional coefficient/general-substitution restatements closed under preservation contract:
no concrete downstream need justifies changing public definitions/signature.

## Literature search status

Web query 1: `polynomial diagonal substitution degree sum individual degrees generalization`.
Top three returned hits recorded verbatim by title/link:

1. [Zeros of a system of diagonal polynomials over finite fields](https://www.sciencedirect.com/science/article/abs/pii/S107157972500053X): different diagonal notion, no usable weakening.
2. [Makar-Limanov's problem on values of polynomials on matrices](https://www.themoonlight.io/en/review/makar-limanovs-problem-on-values-of-polynomials-on-matrices): irrelevant matrix-valued problem.
3. [French review of the same matrix problem](https://www.themoonlight.io/fr/review/makar-limanovs-problem-on-values-of-polynomials-on-matrices): same mismatch.

Refined query: `multivariate polynomial composition degree bound total degree substitution lecture notes`.
Top three:

1. [Polynomials — ECGapprofondies](https://commeunjeu.org/cours/fr-ecgapprofondies-polynomials/?lang=en): sum/product/composition degree formulas.
2. [Polynomials — MPSI](https://commeunjeu.org/cours/fr-mpsi-polynomials/?lang=en): nonzero univariate composition degree equality; stronger assumptions than needed for upper bounds.
3. [Chi-Ning Chou's polynomial notes](https://cnchou.github.io/notes/polynomial.html): individually bounded degrees imply a total degree bound in low-degree extension construction.

Primary local source: clean.tex §6 around line 1468 explicitly uses
`s\leq\sum_jr_j\leq mr_1`, agreeing with retained theorem. Literature supports the standard
total-degree/product-sum argument; it supplies no necessary new hypothesis or useful scoped
API change. ChatGPT math MCP: n/a, no matching tool exposed in ALL_TOOLS.

## Line packing

Actual `set_option format.width 100; #check @Roth.natDegree_diag_le`:

```lean
@Roth.natDegree_diag_le : ∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) → (Roth.diag P).natDegree ≤ ∑ j, r j
```

| Signature line | Characters | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 178 | 72 | `(hP : ∀ j, degreeOf j P ≤ r j)` (30) | 72 + 1 + 30 = 103, exceeds 100 | ok |
| 179 | 72 | none, proof next | n/a, final signature line | ok |

Declaration max width 76, all seven lines measured mechanically. Existing break is necessary.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | hP, L179 | degreeOf j P ≤ r j | already correctly oriented | none |
| 2 | conclusion, L179 | (diag P).natDegree ≤ ∑ j, r j | already correctly oriented | none |
| — | signature | n/a: zero ≥/> occurrences | none | no _ge_/_gt_ name |

## All 42 golfing rules

- [1.1] n/a: proof contains multiple substantive steps, no by-exact wrapper.
- [1.2] n/a: no rfl wrapper.
- [1.3] n/a: rw is followed by refine, not immediately exact.
- [1.4] n/a: no simp/exact sequence.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor.
- [1.7] n/a: no apply/exact pair.
- [1.8] n/a: no contradiction proof.
- [1.9] lambdas depend on bound variables; no eta reduction. Both arrows normalized.
- [1.10] n/a: no have.
- [1.11] n/a: already refine with function binder.
- [1.12] n/a: no show.
- [1.13] n/a: no projection have.
- [1.14] n/a: rewrites act on different goals separated by refine.
- [1.15] n/a: no terminal simp only.
- [1.16] n/a: no nonterminal simp.
- [1.17] already uses `.trans` twice.
- [1.18] n/a: no disposable parenthesized trailing function argument.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no existential helper.
- [2.1] Tried grind after diag rewrite: fails on unconstrained natDegree of sum.
- [2.2] n/a: no retained grind sequence.
- [2.3] n/a: no simplification/closing sequence to consolidate.
- [2.4] n/a: no analytic function property.
- [2.5] n/a: upper bound compares nonzero expressions, not positivity goal.
- [2.6] Tried gcongr after rewrite: no progress.
- [2.7] Tried lia then omega: neither knows degree-of-sum facts, both fail.
- [2.8] Tried aesop after rewrite: no progress.
- [2.9] n/a: no numeric computation/cast identity.
- [2.10] n/a: symbolic arbitrary polynomial/index type, no closed finite decision.
- [2.11] n/a: no denominators or ring equality.
- [2.12] n/a: no ring/ring_nf ending or algebraic equality.
- [2.13] n/a: no symmetric case split.
- [2.14] n/a: no calc; already composed inequalities with trans.
- [2.15] n/a: only one subgoal from refine.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability.
- [3.3] lia tested under 2.7; no omega retained.
- [3.4] n/a: no rcases.
- [3.5] n/a: no evidence for global automation attribute; do not alter public normal forms.
- [3.6] n/a: no simp_all only.
- [3.7] n/a: no maxHeartbeats option.

## Reflection and probes

Whole after-rewrite automation tested in standalone code, cleanly isolated from remaining
source tactics: grind/simp/aesop/lia/omega/exact?/gcongr all failed. A preliminary live
multi_attempt at L181 also saw continuation parse errors, so those malformed attempts were
superseded by standalone examples. apply? did suggest natDegree_sum_le_of_forall_le, confirming
the existing first step. The normalized full proof independently compiled without reference
to natDegree_diag_le. There are no haves to inline or redundant rewrites: the two rewrites
expose precisely the sum-degree and exponent-sum APIs. A term expression would obscure the
rewrite boundaries without reducing mathematical work. The direct aeval route does not
remove the total-degree estimate and adds an import, so retained strategy is appropriate.

## Actual final verification and gates

`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`: session 84593, exit 0;
1658 jobs, CoeffNorm built in 19s. Only six known outside warnings.
Complete native lean_diagnostic_messages after edits: success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors, six known outside warnings.
Native final type assignment + nonself reproof + axioms: success=true, but stale-import info
appeared. Therefore final certification uses fresh CLI `/private/tmp/roth-d19-final.lean`,
which checks an exact universally quantified original type assignment, independent nonself
reproof, width100 #check, and `#print axioms` against freshly built module.
Fresh CLI session 32340 exited 0 with no warnings/errors; reported exactly
`[propext, Classical.choice, Quot.sound]`. No sorry/custom axiom/suppression introduced.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit 0, session 84593 |
| definition_protected | pass | only two lambda arrows changed in theorem proof |
| theorem_statement_protected | pass | both signature lines identical |
| structure_gate | pass | 5 proof lines, zero conjunctions or branches |
| naming_gate | pass | descriptive natDegree_diag_le, no forbidden patterns |
| line_packing_gate | pass | measured table, no repack rows |
| inequality_orientation_gate | pass | no ≥/> in signature |

Overall: pass. Before 7 lines; after 7 lines; saved 0. Two syntax issues fixed.
No renames queued; no refactoring needed; no comments removed; all docs/definitions preserved.

## Required phase checklist

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — all 24 audit items reported.
- [✓] Step 2.5 — five-method search-status reported.
- [✓] Step 2.6 — every parameter mechanically analyzed and probed.
- [✓] Step 2.7 — every signature line measured; width100 #check included.
- [✓] Step 2.8 — complete inequality scan table included.
- [✓] Step 3 — all 42 rules have individual statuses.
- [✓] Step 4 — reflection and alternative strategy considered.
- [✓] Step 5a — complete final LSP has zero errors.
- [✓] Step 5b — actual module build and protection/content gates reported.
- [✓] Step 6a — no rename applicable, no sidecar change required.
