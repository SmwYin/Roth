# Roth.det_choose_eq — Phase 4 declaration report

Baseline `e5a6285`, `Roth/Wronskian.lean` lines 77–92. Final lines 77–89.
Declaration 16 → 13 lines; proof body 12 → 9 lines. Public signature, mathematical content,
docstring and imports preserved (lambda notation changes only in statement).

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, plus the relevant style sections,
naming conventions, the complete worker contract and both Lean/mathlib-quality skills.

The proof factors inverse row factorials from the binomial matrix, identifies the remaining
matrix with the transpose of evaluations of monic descending Pochhammer polynomials, then
uses the polynomial-basis Vandermonde identity. Expressing that transpose directly in `h1`
eliminates the separate definitional equality `h2`.

## Full audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | No diagnostic in target. Complete file has the inherited copyright warning and unused `hφ`, `hd` warnings in a later theorem. |
| 2 | HAVE SCAN | Original L81 `h1 := by ...`: proof content, one use, retained with transpose orientation. Original L86 `h2 := rfl`: no `by`, one use at L89, eliminated entirely by orienting `h1` correctly. |
| 3 | SET_OPTION | No per-declaration options or limit raises. |
| 4 | SIMP SQUEEZE | Sole `simp [Nat.cast_choose_eq_descPochhammer_div, div_eq_inv_mul]` closes the matrix-entry goal; retain terminal unsqueezed simp. No nonterminal bare simp. |
| 5 | NAMING | `det_choose_eq` describes determinant of choose entries and equality conclusion, snake_case, no forbidden abbreviations/numeric patterns; no rename. |
| 6 | LINE PACKING | All four signature lines measured below; no repack necessary at complete expression boundaries. |
| 7 | BY PLACEMENT | Both `by` tokens finish their preceding line. |
| 8 | FORMAT | Two-space tactic indentation; no blank internal lines, semicolon chains, haveI/letI or separate sequential rewrites. Mathematical lambdas changed to ↦. |
| 9 | COMMENTS | No inline comments present; existing five-line source-linked docstring preserved byte-for-byte. |
| 10 | DOCSTRING | Existing statement/product description plus exact source citation retained under the explicit doc-preservation instruction. |
| 11 | VISIBILITY | Public headline theorem listed in module Main results; preserve public API. It is used in the distinct-degree proof at current L170. |
| 12 | STRUCTURE | Nine proof-body lines ≤15 headline bound, no conjunction, no case branch. No extraction needed. |
| 13 | MATHLIB | Five-method results below: reuse existing determinant/scaling/evaluation/Pochhammer building blocks; no exact replacement established. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: not an existential helper. |
| 16 | SHOW/CHANGE | No show/change retained; no definitional equality workaround added. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Per-parameter mechanical and public-literature audit below; no API change applied. |
| 19 | INEQUALITY | No reversed inequality in source signature or local hypotheses; table below. |
| 20 | NORMAL-FORM | Explicit binomial determinant equals factorial factor times ordered Vandermonde product; existing orientation is directly usable by rw in caller. |
| 21 | SYNTAX-GEN | OK: arbitrary natural degree vector already explicit; no injectivity/nonzero assumptions burden callers. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | Changed proof retains genuine Fin→Nat factorial/index coercions and Nat→K coefficients/evaluation casts; dropping evaluation `(d i : K)` experimentally produces a Nat/K mismatch. No redundant casts added; removed h2 removes its duplicate Nat→K cast. Statement casts retained unchanged. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues fixed: eliminate single-use definitional h2; use ↦ lambdas. Refactoring needed: none.

## Mathlib search-status

- **A Lean-Finder:** query `determinant binomial coefficients choose Vandermonde product factorial`;
  hits `Matrix.det_vandermonde_id_eq_superFactorial`, `Matrix.det_projVandermonde`,
  `Matrix.det_vandermonde` (partial matches, not this binomial determinant).
- **B Loogle:** `Matrix.det, Polynomial.eval`; hits `eval_det`, `eval_det_add_X_smul`,
  `Matrix.eval_charpoly`, `Matrix.det_one_add_smul`; none replaces the target.
- **C LeanSearch:** unavailable: inherited, previously established HTTP 500 service failure;
  not retried per file-worker instruction. This is not evidence of absence.
- **D source search:** untruncated `rg` for `det_choose_eq`,
  `det_eval_matrixOfPolynomials_eq_det_vandermonde`, `det_mul_column`,
  `cast_choose_eq_descPochhammer_div`, transpose/of variants. Found the exact used building
  blocks in `LinearAlgebra/Vandermonde.lean:280`, determinant Basic and Pochhammer:530.
- **E local name search:** `det_eval` returned
  `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`; index unavailable, source hit
  verified by actual successful `#check`, not treated as complete semantic-index absence.

Auxiliary variants examined: transpose/of, determinant row/column scaling, projected
Vandermonde, evaluation matrices, descending Pochhammer choose identity. Common-equivalents
lookup has no applicable discrete/topological bucket. Full-name project search shows one
proof caller and module documentation. `exact?` could not close the real goal; `apply?`
only suggested incomplete invertibility/product conversions. No claim of exhaustive absence.
Conclusion: partial match; retain the public binomial specialization and build directly on
existing mathlib. No new wrapper/helper API is introduced. The monic polynomial-basis
abstraction already exists in mathlib, so a new local generalized wrapper is unnecessary.

## Generalisation status

| Parameter | Class/use | Mechanical candidate/result |
|---|---|---|
| `{K : Type*}` | Type variable, coefficient field | Already universe polymorphic. Dropping would leave all field coefficients unbound; no narrower concrete specialization added. |
| `[Field K]` | Determinant, commutative products, factorial inverses | Actual isolated substitution with DivisionRing fails `CommRing K` and `CommMonoid K`; CommRing fails `Inv K` (also NoZeroDivisors for Pochhammer degree API). Dropping all structure cannot elaborate those same operations. No small compatible weakening found. |
| `{l : ℕ}` | Matrix dimension | Used by every Fin index. Dropping leaves dependent types unbound. Arbitrary finite indexing requires choosing an order/enumeration and changes the statement, no present caller need. |
| `[CharZero K]` | Binomial/factorial division | Actual drop-test leaves the binomial-to-Pochhammer equality unsolved. Retain. Finite characteristic variants require characteristic-dependent dimension restrictions, not a mechanical drop. |
| `(d : Fin l → ℕ)` | Explicit degree vector | Used in entries and product differences, cannot drop. Replacing natural choices with abstract polynomial evaluations changes the object; the existing mathlib polynomial-basis theorem already supplies that abstraction. |

Inversion check: after the conversion, the proof is abstract polynomial-basis evaluation;
that theorem is exactly `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`, already
used directly. Thus no missing abstract API to extract. Optional alternative polynomial or
finite-characteristic formulations closed as unnecessary for current callers, not pending work.

Public literature query: `binomial determinant Vandermonde polynomial basis determinant
generalization Krattenthaler`. Relevant returned primary sources:

1. [Krattenthaler, Advanced Determinant Calculus](https://arxiv.org/abs/math/9902004).
2. [Generalized Vandermonde appendix](https://api.unil.ch/iris/server/api/core/bitstreams/de50cf35-02f2-4382-8eff-c6d7cae0bce9/content): search excerpt states the same Vandermonde determinant for monic degree-indexed polynomial bases.
3. [Calculation of some determinants using the s-shifted factorial](https://arxiv.org/abs/math-ph/0401006): falling/rising factorial Vandermonde generalizations.

These support considering polynomial-basis generality; the current proof already uses
mathlib's abstract theorem. No literature-driven API change proposed. ChatGPT math MCP:
n/a, no callable mathematical second-opinion capability available in this worker.

## Line packing

Actual `#check @Roth.det_choose_eq` with `format.width 100`:

```lean
@Roth.det_choose_eq : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] (d : Fin l → ℕ),
  (Matrix.of fun μ ν ↦ ↑((d ν).choose ↑μ)).det = (∏ μ, (↑(↑μ).factorial)⁻¹) * ∏ i, ∏ j > i, (↑(d j) - ↑(d i))
```

Pretty-printer `∏ j > i` is its rendering of `∏ j ∈ Finset.Ioi i`; source keeps explicit Ioi.
Widths measured in Unicode codepoints, not bytes. Next tokens are complete expression
units at the current syntactic breaks (matrix lhs, factorial product factor, nested product).

| Sig line | Chars | Next expression/token width | Arithmetic | Action |
|---|---:|---:|---|---|
| 77 | 52 | Matrix lhs including `=`: 56 | 52+1+56=109>100 | ok |
| 78 | 60 | Factorial product including `*`: 42 | 60+1+42=103>100 | ok |
| 79 | 48 | Nested product and `:= by`: 56 | 48+1+56=105>100 | ok |
| 80 | 64 | No next signature line | n/a | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Full signature and h1 | n/a — no ≥/> inequalities in Lean source | none | no `_ge_`/`_gt_` name |

## Every golfing rule

| Rule | Status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: h2 already used term rfl; its entire declaration eliminated instead. |
| 1.3 | n/a: no rw followed by exact. |
| 1.4 | n/a: terminal simp already closes h1. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | Lambdas use Nat coercions in their arguments; simple eta-reduction cannot remove those coercions. Changed all mathematical arrows to ↦. |
| 1.10 | Applied: removed one-use term equality h2 by putting transpose in h1 itself. |
| 1.11 | n/a: no apply/intro sequence. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected conjunction have. |
| 1.14 | Single final rw chain already merged; retained. |
| 1.15 | n/a: terminal simp not squeezed. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Used `.transpose` projection in the substantive matrix identity. |
| 1.18 | n/a: no avoidable trailing application parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Actual live whole-goal grind failed on determinant equality. |
| 2.2 | n/a: no retained grind prefix. |
| 2.3 | Direct simp_rw conversion tried; determinant scaling fails through Matrix.of transparency. Retained substantive ext/simp identity. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: equality, not positivity/nonzeroness. |
| 2.6 | n/a: no inequality monotonicity. |
| 2.7 | n/a: no linear Nat/Int arithmetic goal; field determinant is essential. |
| 2.8 | Actual live aesop failed after exhaustive search. |
| 2.9 | n/a: variables are symbolic, cast conversion requires the named binomial theorem; removing evaluation cast tested and fails Nat/K elaboration. |
| 2.10 | n/a: arbitrary field/dimension, not closed finite computation. |
| 2.11 | n/a: denominators occur but the non-algebraic binomial/Pochhammer identity is essential; terminal named simp closes it directly. |
| 2.12 | n/a: no ring/ring_nf endpoint or algebraic hypotheses. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: no multiple similar goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases substitutions. |
| 3.5 | No automation attribute added: large determinant-to-product expansion is an explicit-use theorem. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no limits/options. |

## Actual experiments and reflection

- Live `lean_goal` inspected the original target. `lean_multi_attempt` tried grind, simp,
  aesop, exact?, apply?, and direct simp_rw/determinant rewrite. None closed the whole goal.
  The line replacement tool also produced suffix parse noise from the multiline original
  have; failures above are based on actual tactic-goal diagnostics, not that suffix noise.
- Isolated direct conversion with fully supplied scaling matrix failed due Matrix.of
  transparency; removing Matrix.of then failed subsequent rewrite type correctness.
- Merely deleting h2 from the old rw chain failed to match the transposed evaluation matrix.
- Selected proof: put the transpose in h1, use forward det_transpose, preserve terminal
  ext/simp. Actual isolated `lean_run_code` success=true with zero diagnostics.
- Unknown guessed `Matrix.transpose_of` rejected by #check; not used. Final #check probe
  of every selected determinant/Pochhammer identifier succeeded.
- Step back: one-tactic alternatives failed; term mode would still require the matrix
  conversion. Current nine-line proof exposes precisely the conversion, row scaling and
  polynomial-basis determinant. No additional helper or unrelated API is useful.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Wronskian`, session 45382, exit 0, 1826 jobs, reported 21s. |
| Complete LSP | PASS | `lean_diagnostic_messages` whole file: success=true, partial=false, timed_out=false, failed_dependencies=[]; only inherited three warnings outside target. |
| Isolated proof | PASS | Exact selected proof under only Vandermonde/Pochhammer imports, success=true, zero diagnostics. |
| definition_protected | PASS | No definition/abbreviation/import changes. |
| theorem_statement_protected | PASS | Same theorem name/binders/proposition; only `=>` to `↦` in signature. |
| structure_gate | PASS | Nine body lines ≤15 headline maximum; no conjunction or case branch. |
| naming_gate | PASS | Descriptive snake_case, no forbidden abbreviation/pattern; no renames. |
| line_packing_gate | PASS | Four-row measured table above; no residual repack. |
| inequality_orientation_gate | PASS | Zero reversed source inequalities; scan table above. |
| Trust gate | PASS | Actual `#print axioms Roth.det_choose_eq`: propext, Classical.choice, Quot.sound only; no sorry/admit/axiom/native_decide/options introduced. |
| Comments/scope | PASS | Existing docstring untouched; only target source and this report edited. |
| Dependents | Parent-owned | Source frozen and module/LSP success sent to file worker before parent full build and LeanEval. |

Overall worker gates: PASS. Renames queued: none. Refactoring needed: none.

## Phase checklist

- [x] Step 1: all required reference documents read.
- [x] Step 2: all 24 audit items printed.
- [x] Step 2.5: five-method search status and actual API checks recorded.
- [x] Step 2.6: all parameters, weakening probes, inversion check and public literature recorded.
- [x] Step 2.7: complete measured signature width table.
- [x] Step 2.8: inequality scan table.
- [x] Step 3: all 42 golfing rules have concrete dispositions.
- [x] Step 4: alternative-strategy reflection and real experiments recorded.
- [x] Step 5a: complete clean LSP (known out-of-scope warnings explicitly recorded).
- [x] Step 5b: module build and all diff gates passed.
- [x] Step 6a: no rename warranted; no sidecar edit.
