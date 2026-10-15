# Declaration audit: `Roth.weight_le_degree_div`

Dedicated fresh Phase-4 worker, baseline `43f44a1`, original lines 120–124;
final lines 121–125. Scope: this declaration and this report only.
The user approved removal of verified unused DecidableEq assumptions; `hm`, `hr`,
the conclusion, all remaining parameters, visibility, and docstring are preserved.

## Step 1 — references

Read the full supplied declaration-worker instructions, lean4 and mathlib-quality
skills, golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md, and applicable style-rules sections
(width, indentation, signatures, comments, documentation, inequalities, tactics,
visibility, coercions). No rename defect requires a naming-reference escalation.

## Step 2 — all 24 audit items

1. **LINT:** Baseline complete LSP reported unusedSectionVars and unusedDecidableInType
   for `[DecidableEq σ]`. Scoped `omit` removes both. Final complete LSP has no target warning.
2. **HAVE SCAN:** No `have` or `let` in the original or final proof; nothing to inline.
3. **SET_OPTION:** No declaration-scoped option or raised resource limit.
4. **SIMP SQUEEZE:** No simp call in either proof. Tested whole-proof simp and simp_all;
   neither closes the sum comparison, so no squeeze or unsqueeze applies.
5. **NAMING:** `weight_le_degree_div` describes the inequality from weight to degree
   divided by a lower bound. Snake case, no forbidden abbreviation, number pattern,
   single-letter public name, `_ge_`, or `_gt_`. No rename queued.
6. **LINE PACKING:** Original first signature line underpacked; moved the `d` binder
   and colon up. Complete before/after arithmetic below.
7. **BY PLACEMENT:** `:= by` remains at the end of the conclusion line.
8. **FORMAT:** Two-space tactic indentation, four-space signature continuation,
   no blank line in the declaration, no semicolon chain, no haveI/letI.
   Replacing the manual lambda proof also eliminates its ASCII lambda arrow.
9. **COMMENTS:** No inline proof comments existed; none removed. The complete existing
   four-line public docstring is byte-identical.
10. **DOCSTRING:** Preserved bound and source description; it identifies the common
    lower bound and its use for total-degree estimates. No new documentation needed.
11. **VISIBILITY:** Public weight API remains public. Current project search finds no
    external call of this theorem, but absence of a present consumer does not authorize
    reducing the established public API.
12. **STRUCTURE:** Three proof lines before and after; no conjunction, branches,
    helper duplication, or decomposition threshold crossed.
13. **MATHLIB:** Five-method search below. Reuses existing degree/sum/division and
    monotonicity API; no exact replacement of the project-specific theorem established.
14. **JUNK DEF:** n/a: theorem, no definition being introduced or modified.
15. **EXISTS LEMMA:** n/a: no existential statement or private witness wrapper.
16. **SHOW vs CHANGE:** Neither appears; no redundant goal restatement.
17. **PUSH_NEG:** None.
18. **GENERALISE:** Approved DecidableEq removal verified. Fintype is needed by the
    definition; hm and hr cannot be dropped or weakened as proposed, with compiled
    counterexamples below. No broader public API change.
19. **INEQUALITY:** All three signature inequalities already have the smaller side
    left; complete scan below.
20. **NORMAL-FORM:** A weight upper bound by cast degree divided by cast lower bound
    is the existing API normal form. The proof rewrites degree and sum division only
    internally; no competing equivalence or normalization rule added.
21. **SYNTAX-GEN:** OK: pointwise bound `∀ j, m ≤ r j` matches denominator comparison
    directly. Support-local bounds would change the API without an identified consumer.
22. **IMPORT-FANOUT:** n/a: no import changes; gcongr already available in this file.
23. **CASTS:** No explicit cast added or removed in the source diff. Genuine Nat-to-Real
    coercions in the statement remain inferred. gcongr discharges cast plumbing;
    a redundant attempted norm_cast was rejected after its unused-tactic warning.
24. **INSTANCE-NAME:** n/a: this is not an instance declaration; no named instance added.

Issues fixed: two related unused-instance warnings, underpacked signature, manual
sum/division proof plumbing. Refactoring needed: none. No hidden API migration proposed.

## Step 2.5 — mathlib search status

| Method | Query / evidence | Result |
|---|---|---|
| A Lean-Finder | Sum of nonnegative terms divided by lower bounded positive denominators, at most sum divided by lower bound | Returned weighted Cauchy–Schwarz, power-sum, and NNReal power-mean inequalities; none is this upper bound. |
| B Loogle | `_ / _ ≤ _ / _` | Returned Nat.div_le_div_right, Nat.div_mul_div_le_div, Nat.div_le_div_of_mul_le_mul, Nat.div_le_div_left. These are natural division results, not the Real-valued weight bound. |
| C LeanSearch | Natural-language denominator/sum bound | Known inherited service HTTP 500; unavailable, not evidence of absence. Local source, Finder and Loogle used instead. |
| D Source rg | Untruncated weight_le_degree_div, div_le_div_of_nonneg_left, sum_le_sum, degree_eq_sum in relevant project/mathlib directories | Finsupp.degree_eq_sum, Finset.sum_le_sum/division API and related Finsupp sums found; project-specific name only in Box. |
| E Name pattern | `sum_le_sum` via lean_local_search | Finsupp.sum_le_sum, sum_le_sum_index, GCongr.Finset.sum_le_sum and variants; index warming, so no absence inference. |

Auxiliary variants considered: Finset versus Fintype sums, sum_le_sum_index,
div_le_div_of_nonneg_left, Nat.div_le_div_left, degree_eq_sum.
An isolated `#check Fintype.sum_le_sum` and proof attempt failed: unknown constant.
The original Finset lemma and gcongr route both compile; no guessed identifier remains.
Common-equivalents table: no discrete/compact/separation/bornology match.

Live `exact?` failed at the original target. `apply?` in an isolated snippet offered
partial order/division reductions, not a complete replacement (and also saw the
imported project theorem, which is not independent evidence). No broad absence claim
is made. Conclusion: partial matches reused via degree rewrites and `gcongr`;
retain the documented public project API, as required by authorized scope.
No global decidability instance, coset representation, or custom predicate introduced.

## Step 2.6 — generalisation and literature

| Parameter | Class/use | Mechanical candidate and evidence | Result |
|---|---|---|---|
| `{σ : Type*}` | Index type | Already universe-polymorphic; removing type makes r/d ill-formed. No smaller universe constraint exists to remove. | Retain. |
| `[Fintype σ]` | Finite sum in weight | Dropped in isolated example: elaboration fails to synthesize Fintype σ at weight. Finite alone supplies no chosen instance at this statement. | Retain. |
| `[DecidableEq σ]` | Ambient decidability | Drop via scoped omit; isolated proof, complete LSP, final module all succeed. | Removed, approved. |
| `{r : σ → ℕ}` | Denominators | Appears in hr and conclusion; deleting without replacement leaves unbound data. Real-valued parameters require changing weight itself. | Retain. |
| `{m : ℕ}` | Common lower bound/divisor | Appears in hm, hr and conclusion; cannot delete while preserving statement. | Retain. |
| `hm : 0 < m` | Strict positivity of divisor | Drop or weaken to `0 ≤ m`: counterexample m=0, r=1, d=single () 1 gives 1 ≤ 0. Isolated negation compiled by simp. | Retain strict hypothesis. |
| `hr : ∀ j, m ≤ r j` | Pointwise denominator comparison | Drop: m=2, r=1, d=single () 1 gives 1 ≤ 1/2. Isolated negation compiled by norm_num. A support-only assumption is a restatement, not an unused hypothesis. | Retain. |
| `d : σ →₀ ℕ` | Nonnegative multi-index | Appears on both sides; arbitrary signed coefficients would invalidate termwise monotonicity. | Retain. |

The two counterexample snippets used Unit and `Finsupp.single () 1`, unfolding
weight and degree_eq_sum, and produced no error diagnostics. Thus positivity here
differs from the genuinely unused positivity arguments removed earlier in Box.
Inversion check: after rewriting degree, the underlying content is finite-sum
monotonicity and division antitonicity, already provided by mathlib and gcongr.
No new abstract wrapper is justified. Big-change candidates selected: none;
an ordered-field/real-coefficient API would require redesigning the existing definition.

Literature search status:

- Web query `weighted sum upper bound positive minimum denominator generalization`:
  top three results were two versions of a random-multiplicative-function paper
  (ScienceDirect S0022314X26001149) and [generalized weighted means](https://link.springer.com/article/10.1186/s13660-016-1233-7).
  These address different inequalities; no unsupported generalization was inferred.
- Follow-up official-doc queries for division antitonicity and Finsupp weight/degree
  found [Finsupp.Weight](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/Weight.html),
  [Finsupp.DegLex](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/MonomialOrder/DegLex.html),
  and [Finsupp.MonomialOrder](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/MonomialOrder.html).
  Weight/degree is the relevant primary documentation; order variants do not replace this inequality.
  Local `#check div_le_div_of_nonneg_left` confirms its abstract GroupWithZero/ordered
  multiplicative formulation with strict positive denominator, supporting the proof's basis.
- ChatGPT math MCP: n/a, no such callable tool is available in the exposed inventory.

## Step 2.7 — measured signature packing

Original signature:

| Line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 120 | 81 | `(d : σ →₀ ℕ)` = 12 | 81 + 1 + 12 = 94 ≤ 100 | Repack, also move colon. |
| 121 | 50 | No next signature line | n/a | No additional token. |

Final signature:

| Line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 121 | 96 | `weight` = 6 (whole conclusion 31) | 96 + 1 + 6 = 103 > 100 | OK. |
| 122 | 35 | No next signature line | n/a | OK. |

Final width-100 pretty-printer reference:

```lean
@Roth.weight_le_degree_div : ∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ} {m : ℕ},
  0 < m → (∀ (j : σ), m ≤ r j) → ∀ (d : σ →₀ ℕ), Roth.weight r d ≤ ↑(Finsupp.degree d) / ↑m
```

## Step 2.8 — inequality scan

| Occurrence | Location | Expression | Rewrite / rename |
|---|---|---|---|
| 1 | hm | `0 < m` | Already oriented; none. |
| 2 | hr | `m ≤ r j` | Already oriented; none. |
| 3 | conclusion | `weight r d ≤ d.degree / m` | Already oriented; none. |
| n/a | Whole signature | No `≥` or `>` | No `_ge_`/`_gt_` name; no rename. |

## Step 3 — all 42 golfing rules

- [1.1] by exact wrapper: n/a, preceding rewrite is necessary.
- [1.2] by rfl: n/a, no reflexivity proof.
- [1.3] rw + exact to rwa: tested consolidation conceptually against transformed sum;
  exact proves a newly formed inequality, not a hypothesis that rwa can directly close.
  gcongr gives the clearer replacement, verified live.
- [1.4] simp + exact: n/a, no original simp chain.
- [1.5] trailing rfl after simp: n/a, neither exists.
- [1.6] anonymous constructor: n/a, no conjunction or constructor.
- [1.7] apply + exact: n/a, no such chain.
- [1.8] by_contra!: n/a, no contradiction argument.
- [1.9] eta reduction: original lambda has denominator-dependent expression, not eta form;
  gcongr removes the lambda entirely.
- [1.10] single-use have: n/a, none.
- [1.11] apply + intro: n/a, none.
- [1.12] redundant show: n/a, none.
- [1.13] have projections: n/a, none.
- [1.14] merge rw: already one rewrite list; retained and included weight unfolding.
- [1.15] terminal simp only: n/a, none.
- [1.16] nonterminal simp: n/a, selected proof has none.
- [1.17] dot notation: n/a, no retained receiver-style application to shorten.
- [1.18] `<|` parentheses: n/a, final proof has no parenthesized terminal proof argument.
- [1.19] push_neg: n/a, none.
- [1.20] existential helper: n/a, not an existential lemma.
- [2.1] grind: tried live, failed to close original real weighted-sum inequality.
- [2.2] deletion before grind: n/a, no grind in selected proof.
- [2.3] simpa consolidation: whole simp/simp_all attempts leave the sum inequality;
  sum_div rewrite and monotonicity still required. No simp sequence retained.
- [2.4] fun_prop: n/a, no regularity predicate.
- [2.5] positivity: isolated original-style proof with positivity replacing cast of hm succeeds;
  selected gcongr invokes the positivity side-condition solver automatically.
- [2.6] gcongr: applied; handles sum and denominator comparison, leaving `m ≤ r j`.
- [2.7] lia/omega: tried lia on remaining natural inequality; failed because hr is universally
  quantified. Direct `exact hr j` is sufficient; no omega fallback needed.
- [2.8] aesop: tried live; failed, no progress on the original inequality.
- [2.9] norm_num/norm_cast: norm_cast after gcongr reported unused tactic; deleted.
  exact_mod_cast works but is unnecessary because the remaining goal is already natural.
  norm_num successfully verifies the numerical generalisation counterexample.
- [2.10] decide: n/a, symbolic real inequality with arbitrary function data is not a closed computation.
- [2.11] field_simp; ring: n/a, inequality needs order/positivity, not a rational identity.
- [2.12] linear_combination: n/a, no ring-ending equality or linear equality context.
- [2.13] wlog: n/a, no symmetric branches.
- [2.14] calc composition: n/a, no calc block.
- [2.15] `<;>`: n/a, final proof has one remaining comparison, no repeated goals.
- [3.1] erw to rw: n/a, rw already used.
- [3.2] continuity/measurability: n/a, no such tactic or goal.
- [3.3] omega to lia: covered by 2.7; no omega introduced.
- [3.4] rcases rfl: n/a, no destructuring.
- [3.5] automation attributes: no attribute added; arbitrary lower-bound parameter is not
  a canonical simplifier normal form, and no demonstrated automation consumer requires it.
- [3.6] simp_all: tested live; leaves sum comparison, not selected.
- [3.7] resource options: n/a, none to remove and none added.

## Step 4 — step back

Whole-proof grind, simp, aesop, simp_all and exact? do not close the original target.
An attempted direct Fintype API was unavailable; the verified Finset term route works
but keeps explicit sum/positivity/cast arguments. The final three-line gcongr proof
reads as the mathematics and uses no speculative identifiers. Its last `exact` is
already minimal. No have-block, term-mode composition, or helper extraction improves it.

## Step 5 — final verification and gates

- Final `lake build Roth.Box` (absolute lake executable) exited **0**, session **85473**,
  **1154 jobs**. Log: `/private/tmp/roth-box-d13-module.log`.
  Earlier session 9564 also passed, but the final gate is 85473 after removing redundant exact_mod_cast.
- Complete final native LSP: `success=true`, `partial=false`, `timed_out=false`;
  no errors and no target warnings. Remaining warnings: known header limitation and
  the next declaration's unused decidability assumptions; neither belongs to this worker.
- Independent final example, with no DecidableEq binder and no use of the target theorem,
  compiled successfully using exactly the final proof.
- Final `#check` verifies the only elaborated signature change is removal of DecidableEq.
- Native lean_verify and `#print axioms`: only propext, Classical.choice, Quot.sound;
  no nonstandard axioms or suspicious source patterns.
- `git diff --check` passed. Context diff contains only this theorem's scoped omit,
  signature whitespace, and proof; no import, definition, other declaration, or Index edit.
- Full project and separate LeanEval gates are the parent worker's sequential checkpoint
  responsibility; this report does not claim those builds have run.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Final session85473 exited0, 1154jobs. |
| definition_protected | PASS | No def/abbrev change. |
| theorem_statement_protected | PASS, approved exception | Only unused DecidableEq removed; parameters/conclusion identical after whitespace normalization. |
| structure_gate | PASS | Three proof lines; no conjunction or branch. |
| naming_gate | PASS | Mathematical snake-case name, no forbidden patterns. |
| line_packing_gate | PASS | All signature lines in measured final table. |
| inequality_orientation_gate | PASS | Three forward-oriented comparisons, zero reversed symbols. |
| docstrings/comments | PASS | Existing docstring byte-identical; zero inline comments removed. |
| axioms/isolation | PASS | Independent proof and standard axiom basis verified. |

## Step 6 — result and checklist

Before: 5 declaration lines. After: 5 declaration lines; one scoped omit line added.
Audit issues fixed as above. Rules principally applied: 2.6, 2.9, signature packing,
and approved unused-instance removal. Renames queued: none. Refactoring needed: none.
Comments preserved: none present in proof; existing docstring unchanged.

- [x] Step 1 — reference docs read.
- [x] Step 2 — all 24 audit items reported.
- [x] Step 2.5 — five-method search and limitations reported.
- [x] Step 2.6 — every parameter, weakening, inversion and public literature audit reported.
- [x] Step 2.7 — complete measured line-packing tables.
- [x] Step 2.8 — complete inequality scan.
- [x] Step 3 — all 42 rules given concrete statuses.
- [x] Step 4 — alternative strategies and whole-proof automation considered and tested.
- [x] Step 5a — complete native LSP clean for target.
- [x] Step 5b — module, isolation, type, axioms and diff gates passed.
- [x] Step 6a — no rename necessary; no sidecar write.

Source ownership released after the final module/LSP pass; report-only work followed.

Publication verification: full `lake build` session 46898 exited 0 (2586 jobs;
`/private/tmp/roth-box-d13-full.log`); separate `lake build Roth.LeanEval` session 24692
exited 0 (2585 jobs; `/private/tmp/roth-box-d13-leaneval.log`). All affected dependents pass.
