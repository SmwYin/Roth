# Phase 4: Roth.normOne_hasseDeriv_le

Dedicated declaration audit. Source range originally143–165; final143–152.
Baseline supplied by owner: full `lake build` exit0, followed by separate
`lake build Roth.LeanEval` session24717 exit0. No repeated publication builds here.
Native baseline and final complete diagnostics: success true, partial false, timed_out false,
zero errors, six outside warnings (header, four DecidableEq, hC); target has no warning.
Only target proof changed; no new helpers, imports, public types, definitions, or docs.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. Also read both full SKILL.md files,
the full worker contract, and relevant style/naming references before editing.

## Full audit

1. LINT: no target warning; six outside warnings preserved within delegated scope.
2. HAVE SCAN: old hsub no by used twice (support membership and final subset sum),
   he' no by once, hc no by once. The new monomial-expansion strategy removes all three;
   there are zero remaining have declarations.
3. SET_OPTION: none in target or diff; no heartbeat/recursion increases.
4. SIMP SQUEEZE: no simp in either target body; no nonterminal simp to squeeze.
5. NAMING: normOne_hasseDeriv_le names the bound and uses existing API object spelling;
   no forbidden abbreviation or pattern; no rename needed.
6. LINE PACKING: both signature lines measured below; unchanged and packed.
7. BY PLACEMENT: := by stays on final signature line.
8. FORMAT: two-space tactics, no blank proof lines, one tactic per line, ↦ lambdas.
9. COMMENTS: no inline proof comments existed; existing docstring preserved verbatim.
10. DOCSTRING: public explanatory statement and source citation retained verbatim.
11. VISIBILITY: public main result used by determinant estimate; preserve export.
12. STRUCTURE: proof body21→8 lines, total declaration23→10, saving13;
    no conjunction and no case branch; main/headline ≤15 gate satisfied directly.
13. MATHLIB: five-method search below. Reuse hasseDeriv_apply, sum_le_sum and mul_sum.
14. JUNK DEF: n/a, theorem returns Prop and introduces no data definition.
15. EXISTS LEMMA: n/a, no existential or single-use witness helper.
16. SHOW vs CHANGE: none present or introduced.
17. PUSH_NEG: none present or introduced.
18. GENERALISE: each parameter examined and mechanically probed below; type preserved.
19. INEQUALITY: only ≤, table below; name already uses _le.
20. NORMAL-FORM: multiplicative bound with small side left; coefficient l1 norm is the
    existing project interface. Monomial expansion uses canonical MvPolynomial API.
21. SYNTAX-GEN: OK, degreeOf hypotheses support direct downstream application;
    support-local restatement tested but not adopted because it changes public API.
22. IMPORT-FANOUT: n/a, no new import.
23. CASTS: diff introduces no explicit cast/ascription. Existing cast manipulation replaced
    by named Int.cast_mul, Int.cast_natCast and Nat.abs_cast rewrites (cross-type ℤ/ℕ→ℝ).
24. INSTANCE-NAME: n/a, no instance declaration introduced or modified.

Issues fixed: oversized headline body, support-image plumbing, single-use have bindings,
old => proof lambdas, and unnecessary shifted coefficient/cast bookkeeping.
Renames queued: none. New helper audit obligations: none.

## Mathlib search-status

[A] Lean-Finder: “Hasse derivative sum absolute values coefficients bounded by 2 power
    degree”, top3: Chebyshev.leadingCoeff_le_of_forall_abs_le_one,
    Polynomial.hasseDeriv, Polynomial.natDegree_hasseDeriv_le. No complete match.
[B] Loogle: Finset.sum_le_sum; found generic finite-sum monotonicity and inspected its type.
[C] LeanSearch: “sum of absolute values of coefficients Hasse derivative polynomial”;
    Polynomial.hasseDeriv, LaurentSeries.hasseDeriv, Polynomial.sumIDeriv.
[D] Untruncated rg over Mathlib and Roth: normOne_hasseDeriv_le,
    norm.*hasseDeriv, hasseDeriv.*norm; only target and local determinant consumer.
    Read Roth/HasseDeriv.lean expansion and coefficient APIs.
[E] lean_local_search hasseDeriv returned project hasseDeriv_apply and monomial API,
    alongside univariate/Laurent counterparts. Index warming, so not used as absence proof.

Auxiliary variants: apply, monomial, coefficient, natDegree bound, finite-sum bound.
Common-equivalents lookup: none of discrete/finite/metric/bornological buckets applies.
Conclusion: partial generic matches; keep project theorem and use project Hasse expansion
plus Mathlib finite-sum machinery directly. No new wrapper helper. The generic whole-goal
`exact?` probe failed; `apply?` produced unrelated order-arithmetic partial suggestions.
No claim of absence based only on grep or index. Public name/doc preservation overrides
any generic deletion advice; no exact replacement was found.
Six strict rules reviewed: no added wrappers or predicates; all five routes tried;
auxiliary routes tried; no duplicate exact match to delete; this report records usages
because module docs are explicitly outside this declaration-only edit scope.

## Generalisation status

| Parameter | Class/use | Catalogue candidates and actual probe | Result |
|---|---|---|---|
| σ : Type* | universe/type variable | drop binder with autoImplicit false: Unknown identifier σ; universe already polymorphic | keep |
| [Fintype σ] | sum and binomial bound | drop and replace by [Finite σ]: both failed Fintype σ synthesis | keep |
| d : σ →₀ ℕ | derivative order | drop binder: derivative-polynomial application type mismatch | keep |
| P : MvPolynomial σ ℤ | polynomial argument | drop binder: derivative-polynomial application type mismatch | keep |
| r : σ → ℕ | coordinate bounds and exponent | drop binder: function expected at unknown r | keep |
| hP : ∀ j, degreeOf j P ≤ r j | support exponents bound | drop: Unknown identifier hP; replace by ∀ k ∈ P.support, ∀ j, k j ≤ r j and use hP k hk: compiles | retain original API |

All probes executed with native lean_run_code. Successful support-local probe initially
had a parenthesization error, corrected to hasseCoeff_le_two_pow (hP k hk) and compiled.
No strict inequality, continuity, topology, algebra class or bundled conjunction parameter
exists, so strict→weak, topological parents, point continuity and conjunction unbundling
catalogues are inapplicable. Fintype's Finite alternative does not elaborate the displayed
finite sum without additional instance/restatement machinery. ℤ/ℝ abstraction would require
changing normOne and other public definitions, outside this declaration contract.
Inversion check: after expansion the proof is generic sum monotonicity, but it still uses
hasseCoeff and monomial degree bounds; no unexplained concrete witness is hidden.
Big-change candidate: support-exponent bound in place of degreeOf could be a future API
variant, but no mathematical weakening has been established (these may be equivalent).
No required refactoring: this theorem's public type is intentionally preserved.

## Literature search

Web query: “Hasse derivative coefficient norm bound binomial polynomial generalization”.
Top3 returned results captured:
1. [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5):
   multivariate Hasse derivatives as coefficient extraction and Taylor expansion.
2. [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025):
   Hasse derivative by coefficient extraction in f(x+z).
3. [Polynomial Ideals in Algebraic Complexity](https://www.ideals.illinois.edu/items/128725/bitstreams/430038/data.pdf):
   Hasse derivatives for small characteristic and coefficient extraction.
These support the broad algebraic derivative notion; they do not supply this real l1 norm
inequality or justify dropping a coordinate bound. General normed coefficient versions
would require broader normOne definitions/public restatement. No literature-driven edit.
ChatGPT math MCP: n/a, no corresponding callable tool in available metadata.

## Line packing

Native #check with `set_option format.width 100`:
```lean
@Roth.normOne_hasseDeriv_le : ∀ {σ : Type u_1} [inst : Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    Roth.normOne ((MvPolynomial.hasseDeriv d) P) ≤ (2 ^ ∑ j, r j) * Roth.normOne P
```

| Signature line | Characters | Next atomic binder | Arithmetic | Action |
|---|---:|---|---|---|
|143|89|`(hP : ∀ j, degreeOf j P ≤ r j)` (30)|89+1+30=120 >100|ok|
|144|96|none, proof follows|n/a|ok|

No >100 target line; no repack required. Pretty-printer output above is recorded exactly,
including its long first diagnostic line; source itself satisfies width100.

## Inequality scan

| Location | Occurrence | Rewrite | Rename |
|---|---|---|---|
|143–144 signature and hP|zero ≥/>; hP and result use ≤|none|none|

## Golfing rule pass: all42

- [1.1] by exact wrapper: n/a, no such wrapper.
- [1.2] by rfl: n/a, no reflexivity proof.
- [1.3] rw+exact→rwa: n/a, final cast inequality needs a separate monotonicity step.
- [1.4] simp+exact→simpa: n/a, no simp sequence.
- [1.5] trailing rfl: n/a, no rfl.
- [1.6] constructor compression: n/a, no constructor goal.
- [1.7] apply+exact: used direct term `(normOne_sum_le _ _).trans` with refine.
- [1.8] by_contra!: n/a, no contradiction proof.
- [1.9] eta reduction: remaining lambda uses j as degree index, not eta-redex.
- [1.10] single-use have: old he' and hc eliminated through changed expansion strategy.
- [1.11] apply+intro: use Finset.sum_le_sum fun k hk ↦ directly.
- [1.12] redundant show: n/a, absent.
- [1.13] have+.1/.2: n/a, no projections.
- [1.14] merge rw: monomial/cast/abs rewrites share one rw call.
- [1.15] terminal simp only: n/a, no simp.
- [1.16] nonterminal simp: n/a, no simp.
- [1.17] dot notation: `.trans` for sum and degree inequalities.
- [1.18] <|: n/a, no removable final parenthesis around a terminal proof block.
- [1.19] push Not: n/a, no negation tactic.
- [1.20] trivial existential: n/a, no existential helper.
- [2.1] grind: actual whole-proof multi_attempt failed with unsolved negated inequality.
- [2.2] deleting before grind: n/a, no grind retained.
- [2.3] simpa consolidation: no simp chain; direct named rewrites retained.
- [2.4] fun_prop: n/a, no function regularity proposition.
- [2.5] positivity: actual probe on product inequality rejected “not a positivity goal”;
  abs_nonneg closes the actual nonnegativity premise directly.
- [2.6] gcongr: actual local probe reduces product inequality to same coefficient bound;
  explicit mul_le_mul_of_nonneg_right retained for its direct nonnegativity witness.
- [2.7] lia: actual local probe failed; no independent Nat linear arithmetic subgoal.
- [2.8] aesop: actual whole-proof probe failed, made no progress.
- [2.9] norm_num/norm_cast: local probes do not close product inequality;
  exact_mod_cast closes coefficient bound after explicit multiplication monotonicity.
- [2.10] decide: n/a, symbolic universal norm bound is not finite concrete computation.
- [2.11] field_simp/ring: n/a, no denominators or algebraic identity goal.
- [2.12] linear_combination: n/a, no ring-ending proof or polynomial identity.
- [2.13] wlog: n/a, no symmetric cases.
- [2.14] collapse calc: eliminated entire old three-stage calc using trans and sum bound.
- [2.15] <;>: n/a, no repeated sibling proof goals remain.
- [3.1] erw→rw: n/a, no erw.
- [3.2] continuity→fun_prop: n/a, no legacy regularity tactics.
- [3.3] omega→lia: n/a, neither retained; lia trial in2.7 failed.
- [3.4] rcases rfl: n/a, no substitution/case split.
- [3.5] automation attributes: n/a, specialized multiplicative bound is not a simp normal form.
- [3.6] simp_all: n/a, no simp_all only.
- [3.7] heartbeat option: n/a, no limit option present or added.

## Reflection

Changed mathematical strategy: expand over input monomials first, use normOne's triangle
inequality, bound each binomial product by2^sum r, and factor the fixed multiplier through
the input support sum. This removes output-support injectivity/subset bookkeeping entirely.
Whole-proof grind/simp/aesop and exact? failed; apply? only offered unrelated partial
arithmetic reductions. The short proof already exposes its two mathematical steps;
term mode would obscure intermediate sum types. No helper extraction necessary.

## Actual gates

Diff captured using `diff -u /private/tmp/d15-coeffnorm-before.lean Roth/CoeffNorm.lean`;
only proof lines in target changed, -13 net lines. Source frozen before final verification:
SHA256 `05f9128d32dfec65f7c590be5f25b23b2e817269ea2e042f38c68e29ffdcaf15`.
No source edits after ownership revoked.

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session14800 exit0, Built21s, 1658 jobs|
|definition_protected|pass|no def/abbrev/instance change in snapshot diff|
|theorem_statement_protected|pass|both signature lines and docstring byte-identical|
|structure_gate|pass|8 body lines ≤15, no conjunction/branch/helper|
|naming_gate|pass|descriptive existing API name, no forbidden pattern|
|line_packing_gate|pass|both rows above,89/96 codepoints|
|inequality_orientation_gate|pass|zero ≥/> signature/hypothesis occurrences|
|diagnostics|pass|native complete final diagnostics success true, partial false; zero errors, target warnings0|

Independent original-type assignment and nonself reproof in
`/private/tmp/d15-final-probe.lean`, compiled by fresh CLI after module build to avoid stale
imports (native snippets had informational stale-import notices). Both use exact original
public type; reproof invokes expansion and generic bounds without target theorem.
Axiom sets checked for target and independent_reproof: only propext, Classical.choice,
Quot.sound. Full CLI completion recorded below.

## Phase checklist

- [✓] Step1 — reference docs read.
- [✓] Step2 — all24 audit items printed.
- [✓] Step2.5 — five-method search-status printed.
- [✓] Step2.6 — every parameter and actual weakening probes recorded.
- [✓] Step2.7 — full signature width table and width100 #check printed.
- [✓] Step2.8 — inequality scan table printed.
- [✓] Step3 — all42 golfing rules addressed.
- [✓] Step4 — alternative-strategy reflection completed.
- [✓] Step5a — complete LSP clean of errors and target warnings.
- [✓] Step5b — actual module build and diff gates printed.
- [✓] Step6a — no rename needed; no shared sidecar write.

Result: declaration23→10 lines; body21→8 lines; saved13. No new helpers.
Refactoring needed: none. Public support-local restatement remains optional and unadopted.

Fresh CLI final gate: `/Users/ramin/.elan/bin/lake env lean /private/tmp/d15-final-probe.lean`,
session10408 exit0, no errors or warnings and no stale-import notice. Output:
```lean
@normOne_hasseDeriv_le : ∀ {σ : Type u_1} [inst : Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) → normOne ((hasseDeriv d) P) ≤ (2 ^ ∑ j, r j) * normOne P
'independent_reproof' depends on axioms: [propext, Classical.choice, Quot.sound]
'Roth.normOne_hasseDeriv_le' depends on axioms: [propext, Classical.choice, Quot.sound]
```
Overall gates: pass. Publication-wide full build/LeanEval remain file-owner gates.
