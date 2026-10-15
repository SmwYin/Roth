# `Roth.weight_mul_left` — declaration 12/14

Dedicated fresh worker `/root/cleanup_continuation/box_file/decl12`.
Baseline `c486b4d`; original lines 111–113, final lines 112–114.
Scope: this theorem and this report. The parent owns the Index caller and project checkpoints.

## Result

Removed the unused `hl : 0 < l` and section `[DecidableEq σ]`, explicitly approved by
the user (“Follow your recommendation”). Changed the lambda arrow to `↦`. The equality,
remaining binders, name, visibility, and docstring are preserved. The same simp proof
works even at `l = 0` because real division in Lean is total.

Before: 3 declaration lines. After: 3. Saved: 0; the scoped `omit` adds one surrounding
command line. Three target warnings removed. No new helper, import, attribute, or option.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, the relevant style sections,
the Lean 4 and mathlib-quality skills, and the full worker prompt at
`/private/tmp/roth-box-declaration-worker.md`.

## Full audit (24 items)

1. **LINT:** baseline reports unused `hl`, unused section `DecidableEq σ`, and unused
   decidability in the type. Complete final LSP removes all three.
2. **HAVE SCAN:** none: the body is one terminal simp.
3. **SET_OPTION:** none in the declaration; no source options introduced.
4. **SIMP SQUEEZE:** terminal `simp [weight, Finset.sum_div, div_div, mul_comm]` closes
   the equality. Keep unsqueezed. Removing arithmetic hints was tested and fails.
5. **NAMING:** `weight_mul_left` is snake_case describing multiplication on the left
   of each parameter. No forbidden abbreviation, numeric scheme, `_auxN`, `_ge_`,
   `_gt_`, or single-letter public identifier; no rename needed.
6. **LINE PACKING:** both signature lines measured below; the full signature would
   require 108 codepoints, so the break before its equality is necessary.
7. **BY PLACEMENT:** `by` ends the conclusion line; no standalone `by`.
8. **FORMAT:** two-space proof indent, four-space signature continuation, no proof
   blank lines, semicolon chains, `haveI`, or `letI`. Normalize lambda to `↦`.
9. **COMMENTS:** no inline proof comments existed; none removed.
10. **DOCSTRING:** existing two-line public statement and source citation unchanged.
11. **VISIBILITY:** retain public: `Roth/Index.lean:221` uses the theorem.
12. **STRUCTURE:** one proof line, no conjunction or branches; no decomposition needed.
13. **MATHLIB:** generic sum division and division associativity provide the proof.
    The local theorem exposes the behavior of the project's `weight`; searches and
    generic-route probes below found building blocks, not an exact reusable replacement.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: no existential statement or private witness wrapper.
16. **SHOW vs CHANGE:** neither occurs.
17. **PUSH_NEG:** none.
18. **GENERALISE:** apply exactly the approved positivity/decidability removals; complete
    per-parameter table below. No broader representation change.
19. **INEQUALITY:** initial `0 < l` was already correctly oriented and is now removed;
    no inequality remains in the conclusion or hypotheses.
20. **NORMAL-FORM:** scaling parameters rewrites to division of the original weight;
    this is the form consumed by Index. Multiplication by the inverse is equivalent
    but unnecessary here; the caller chooses that form with `div_eq_inv_mul`.
21. **SYNTAX-GEN:** dropping the proof argument simplifies rewriting. Other arguments
    retain their original explicitness/order. No new normal-form attributes.
22. **IMPORT-FANOUT:** n/a: no import changes or new dependencies.
23. **CASTS:** 0 explicit casts dropped, 0 new explicit cross-type casts, 0 new
    load-bearing ascriptions. Inferred natural-to-real casts remain necessary.
24. **INSTANCE-NAME:** n/a: no instance declaration or named local instance.

Issues found: unused positivity, unused decidability, lambda syntax; all fixed.
Refactoring needed: parent updates the one Index use from `weight_mul_left hl` to
`weight_mul_left` before its required full project build. This is already authorized.
No Phase 5 mathematical generalization, decomposition, or rename queued.

## Mathlib search-status (five methods)

| Method | Query / evidence | Result |
|---|---|---|
| A: Lean-Finder | “sum of fractions divided by a common factor scaling denominator” | `div_add_div`, `div_add_div_same`, `Rat.add_divInt`; elementary related division formulas, no exact weight theorem. |
| B: Loogle | `Finset.sum, _ / _` | `Int.sum_div`, `Nat.sum_div`, `Finset.sq_sum_div_le_sum_sq_div`; integer divisibility/inequality results differ from the real identity. |
| C: LeanSearch | Inherited service diagnosis HTTP 500 | Unavailable; no repeated retry, no absence claim based on its outage. |
| D: source search | Untruncated `weight_mul_left` over Mathlib; `sum_div`, `div_div`, weight/mul/smul variants in Finsupp/Weight | No same-name source declaration; confirmed `Finset.sum_div` and `div_div`, plus `div_mul_eq_div_div_swap`. |
| E: native name search | `div_div`, `Finset.sum_div`, `div_mul_eq_div_div_swap` | Source-backed hits; index unavailable/warming, so empty index results would not prove absence. |

Auxiliary variants checked: `div_mul_eq_div_div_swap`, `div_div_eq_mul_div`,
`Multiset.sum_map_div`, and Finsupp weight scalar/multiplication API. The swap lemma
also gives a compiled one-line proof but has a longer hint list by characters.
Common-equivalents lookup: no discrete, compactness, boundedness, or separation bucket applies.

Compiled generic-route evidence: live `exact?` cannot close the original goal; `apply?`
only proposes partial Cauchy-representation or nonzero-denominator reductions, leaving
goals. Those incomplete suggestions are rejected. We make no universal absence claim.
Conclusion: partial match in generic arithmetic; keep the established weight API and
its single terminal simp. No new wrapper or missing-API extraction is warranted.

## Generalisation status

| # | Parameter | Class | Use | Candidates / verification | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Indexes `r`, `d`, and the finite sum | Already universe polymorphic; dropping it leaves the dependent signature unbound | Retain |
| 2 | `[Fintype σ]` | typeclass | Required by `weight` and its `univ` sum | Drop-test checked independently; cannot synthesize `Fintype σ`. Replacing by `Finite` would require choosing a Fintype and restating the definition | Retain |
| 3 | `[DecidableEq σ]` | decidability | No proof/type use | Drop in isolated example and scoped live omission; complete LSP passes | Removed, approved |
| 4 | `{l : ℕ}` | structure value | Parameter scale and final denominator | Dropping binder leaves `l` unbound; no order hypothesis needed; explicitness unchanged | Retain |
| 5 | `(hl : 0 < l)` | proposition | No proof use | Weakest candidate is complete deletion; independently compiled and live LSP verified. Therefore a weaker `0 ≤ l` assumption would also be redundant | Removed, approved |
| 6 | `(r : σ → ℕ)` | structure value | Denominator function | Appears on both sides; dropping leaves expression unbound. No bundled proposition to weaken | Retain |
| 7 | `(d : σ →₀ ℕ)` | structure value | Numerators | Appears on both sides; dropping leaves expression unbound. Changing to arbitrary function would restate the weight definition | Retain |

Inversion check: after unfolding `weight`, this is generic finite-sum division and
commutative denominator reassociation. Those abstractions already exist as
`Finset.sum_div` (over a division semiring) and `div_div` (over a division commutative
monoid). Thus no missing abstract lemma needs extraction. Generalizing the real-valued
weight definition or changing its natural-valued inputs is outside this approved change
and offers no necessary caller improvement. Big-change candidates queued: none.

## Literature search

Web query: “weighted sum scaling denominator generalization sum fractions common divisor”.
Top three hits captured: [OpenStax rational expressions](https://openstax.org/books/intermediate-algebra-2e/pages/7-2-add-and-subtract-rational-expressions),
[Androma barycentric scaling](https://androma.org/theorems/13853), and
[weighted gcd sums](https://arxiv.org/abs/1801.03647).
The first supports elementary common-denominator arithmetic; the latter two concern
different objects and supply no additional generalization of this theorem. No claim
depends on their authority. The local project source `clean.tex:636–641` states the index
scaling identity for positive `l`; that extended-nonnegative-real statement differs from
the present finite real weight identity. The zero-scale extension here is established
by Lean's compiled proof, not inferred from the paper's index statement.

ChatGPT math MCP: n/a, no mathematical second-opinion tool is exposed. Literature-driven
big-change candidates: none. Ordinary division formulas already explain the proof;
the existing mathlib generic algebraic signatures were checked by Lean.

## Line packing

`#check @Roth.weight_mul_left` at `format.width := 100` is recorded in final verification.
Measurements use Unicode codepoints.

| State / sig line | Chars | Next signature unit | Combined | Action |
|---|---:|---|---|---|
| Before 111 | 71 | Equality and `:= by` (50 chars, ignoring indentation) | 71 + 1 + 50 = 122 > 100 | ok |
| Before 112 | 54 | No next signature line | n/a | ok |
| After 112 | 58 | Equality and `:= by` (49 chars, ignoring indentation) | 58 + 1 + 49 = 108 > 100 | ok |
| After 113 | 53 | No next signature line | n/a | ok |

## Inequality scan

| # | Location | Original | Final / action | Rename |
|---|---|---|---|---|
| 1 | Original hypothesis `hl` | `0 < l` | Approved removal; no reversal was needed | none |
| 2 | Final full signature | No `≥` or `>` and no remaining inequality | n/a | none |

## Golfing rule pass (42 rules)

- [1.1] `by exact`: n/a, no exact wrapper.
- [1.2] `by rfl`: n/a; live whole-proof `rfl` fails definitional equality.
- [1.3] rw + exact: n/a, no rewrite/exact chain.
- [1.4] simp + exact: n/a, simp is already terminal.
- [1.5] trailing rfl: n/a, none.
- [1.6] constructor pair: n/a, equality has no constructor block.
- [1.7] apply + exact: n/a, none.
- [1.8] by_contra + push_neg: n/a, no contradiction proof.
- [1.9] eta reduction: n/a, lambda performs multiplication after applying `r`.
- [1.10] inline single-use have: n/a, no have.
- [1.11] apply + intro: n/a, none.
- [1.12] redundant show: n/a, none.
- [1.13] have projections: n/a, none.
- [1.14] merge rw: n/a, no rw.
- [1.15] unsqueeze terminal simp: already unsqueezed; keep.
- [1.16] squeeze nonterminal simp: n/a, sole simp closes.
- [1.17] dot notation: n/a, simp hints are constants rather than receiver applications.
- [1.18] `<|`: n/a, no removable enclosing proof parentheses.
- [1.19] push Not: n/a, no push_neg.
- [1.20] existential helper: n/a, not existential.
- [2.1] grind: live `grind [weight]` fails; retain deterministic simp.
- [2.2] delete before grind: n/a, no selected grind.
- [2.3] simpa consolidation: n/a, no following closing step to consolidate.
- [2.4] fun_prop: n/a, no analytic function property.
- [2.5] positivity: n/a, goal is equality of arbitrary weights, not a sign goal.
- [2.6] gcongr: n/a, no inequality or monotonicity goal.
- [2.7] lia/omega: n/a, finite sums and real division are not Presburger arithmetic.
- [2.8] aesop: live attempt fails with no progress.
- [2.9] norm_num/norm_cast: n/a, no concrete numeric computation or standalone cast equality;
  `Nat.cast_mul` is already handled by simp.
- [2.10] decide: n/a, symbolic equality of arbitrary real-valued finite sums is not finite computation.
- [2.11] field_simp/ring: attempted on the generic scalar identity; `field_simp` is an
  unknown tactic under this file's imports. Do not add an import for an unnecessary
  alternative to the already successful one-line simp.
- [2.12] linear_combination: n/a, no ring-ending proof or algebraic equality hypotheses.
- [2.13] wlog: n/a, no symmetric branches.
- [2.14] collapse calc: n/a, no calc.
- [2.15] shared `<;>`: n/a, one goal and one tactic.
- [3.1] erw: n/a, none.
- [3.2] legacy continuity/measurability: n/a, none.
- [3.3] omega→lia: n/a, neither arithmetic tactic occurs.
- [3.4] rcases rfl: n/a, no case split.
- [3.5] automation registration: retain ordinary theorem; adding simp/grind attributes is
  an unnecessary normal-form/API change, and the caller explicitly rewrites it.
- [3.6] simp_all: n/a, no retained hypotheses and no simp_all only.
- [3.7] heartbeat options: n/a, none.

## Step back and think

The proof is already one tactic. Live alternatives: `rfl`, `simp [weight]`, and
`simp [weight, Finset.sum_div, div_div]` fail; the final failure is exactly the reversed
order of denominator factors. Original simp succeeds. `grind [weight]`, `aesop`, and
`exact?` fail; `apply?` only offers incomplete reductions and is rejected. The isolated
alternative `simp [weight, Finset.sum_div, div_mul_eq_div_div_swap]` also succeeds, but
is longer in characters without improving the explanation or dependence structure.
Term-mode composition would spell out sum congruence and casts, so it offers no
improvement over the single existing simp. No unused proof steps or helper blocks remain.

## Verification and diff gates

`/Users/ramin/.elan/bin/lake build Roth.Box` completed successfully (1154 jobs).
Actual process session 25415 exited 0; log `/private/tmp/roth-box-d12-module.log`.
The complete final LSP call reports `success: true`, `partial: false`, no errors,
and no warning for this declaration. Remaining warnings are the preserved file header
and the two as-yet-unprocessed declarations.

Independent no-positivity/no-decidability example compiled with the selected proof.
A separate `l = 0` example compiled. Neither proof calls `weight_mul_left`.

Final native `lean_verify`: standard trust, exactly `propext`, `Classical.choice`, and
`Quot.sound`; no nonstandard axioms and no source-scan warnings. Native `#print axioms`
agrees. The final `#check` output at width 100 is:

```lean
@Roth.weight_mul_left : ∀ {σ : Type u_1} [inst : Fintype σ] {l : ℕ} (r : σ → ℕ) (d : σ →₀ ℕ),
  Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / ↑l
```

The intentionally failing Fintype drop-test reports `failed to synthesize Fintype σ`.
The optional scalar `field_simp` experiment reports an unavailable tactic; this scratch
failure is separate from the passing source, module, and isolated selected proof.
Neither experiment changed repository source. No native probe remains running.
`git diff --check` passed. A direct extraction comparison confirms the docstring is
byte-identical; the sole Box diff is the authorized two assumptions and lambda glyph.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit 0, session 25415, 1154 jobs |
| definition_protected | pass | No def/abbrev changes |
| theorem_statement_protected | pass under user authorization | Only approved `hl` and `DecidableEq σ` removals; equality preserved |
| structure_gate | pass | One proof line; no conjunction/branches |
| naming_gate | pass | Descriptive snake_case; no forbidden patterns |
| line_packing_gate | pass | Both final signature rows measured; combined 108 > 100 |
| inequality_orientation_gate | pass | Zero reversed inequalities in final signature |
| comments/docstrings | pass | No inline comments existed; docstring byte-identical |
| trust | pass | Standard three axioms only, no suspicious source patterns |

Overall: pass. Parent handles the authorized Index caller and full project plus separate
LeanEval build checkpoint; those are not claimed by this declaration worker.

## Phase checklist

- [x] Step 1 — required reference docs read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — all five search methods accounted for; unavailable service explicit.
- [x] Step 2.6 — every parameter and public literature search recorded.
- [x] Step 2.7 — complete before/after signature width tables.
- [x] Step 2.8 — inequality occurrence table.
- [x] Step 3 — all 42 rules have concrete statuses.
- [x] Step 4 — alternative strategies and complete proofs considered.
- [x] Step 5a — complete LSP diagnostics verified.
- [x] Step 5b — actual module build and all diff/trust gates recorded.
- [x] Step 6a — no rename needed or queued.

Comments preserved: no inline comments present; public docstring unchanged.
Ownership released: final source and this report are complete; parent owns external caller.

Parent compatibility verification: removed only the obsolete `hl` argument at
`Roth/Index.lean:221`. Complete native Index LSP success=true, partial=false, no errors
(26 warnings belonging to Index; its own declarations remain for dedicated cleanup).

Publication verification: full `lake build` session 84040 exited 0 (2586 jobs;
`/private/tmp/roth-box-d12-full.log`); separate `lake build Roth.LeanEval` session 7710
exited 0 (2585 jobs; `/private/tmp/roth-box-d12-leaneval.log`). All affected dependents pass.
