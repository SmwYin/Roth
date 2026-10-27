---
decl: Roth.abs_prod_pow_le_rpow_of_le_weight
file: Roth/Main.lean
line: 347
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Roth-specific estimate turning coordinate bounds |x_j| at most q_j^(-κ) and q_0^(r_0/r_j) at most q_j into |∏ x_j^(d_j)| at most q_0^(-r_0 c κ) when c is at most weight r d; single caller abs_eval_lt_of_le_index, no mathlib analogue.
action: Keep as private helper for its single call site Roth/Main.lean:400 (abs_eval_lt_of_le_index); no change needed.
---

# Roth.abs_prod_pow_le_rpow_of_le_weight

## Inventory entry

### `theorem Roth.abs_prod_pow_le_rpow_of_le_weight`
- **Type**: `∀ {m : ℕ} [NeZero m] {r q : Fin m → ℕ}, (∀ j, 0 < q j) → ∀ {κ : ℝ}, 0 ≤ κ → ∀ {x : Fin m → ℝ}, (∀ j, |x j| ≤ 1 / (q j : ℝ) ^ κ) → (∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) → ∀ (d : Fin m →₀ ℕ) {c : ℝ}, c ≤ weight r d → |∏ j, x j ^ d j| ≤ (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ)`
- **What**: If each coordinate x_j is bounded by q_j^(-κ) (κ ≥ 0, q_j positive integers), and the denominators grow as q_j ≥ q_0^(r_0/r_j), then for any multi-index d whose weight ∑ d_j/r_j is at least c, the monomial ∏ x_j^(d_j) has absolute value at most q_0^(-r_0 c κ). This is the term estimate in §7 of the Roth proof ("|∏ (h_j/q_j - α)^{i_j}| < q_1^{-r_1(γ-η)κ}").
- **How**: `Finset.abs_prod`, then a 4-step `calc`: (1) `Finset.prod_le_prod₀` with `abs_pow`, `Real.rpow_mul`, `Real.rpow_natCast`, `Real.rpow_neg`, `pow_le_pow_left₀` gives ∏ q_j^(-κ d_j); (2) `Finset.prod_le_prod₀` with `Real.rpow_le_rpow_of_nonpos` (negative exponent reverses `hqr`) gives ∏ (q_0^(r_0/r_j))^(-κ d_j); (3) `Real.rpow_mul`, `Real.rpow_sum_of_pos`, unfolding `weight`, `Finset.mul_sum`, `ring` collapses to q_0^(-r_0 κ weight r d); (4) `Real.rpow_le_rpow_of_exponent_le` (q_0 ≥ 1) with `mul_le_mul_of_nonpos_left hw`.
- **Hypotheses**: `[NeZero m]` (to name index `0 : Fin m`); `hq : ∀ j, 0 < q j`; `hκ : 0 ≤ κ`; `hx` coordinate bounds; `hqr` denominator growth; `hw : c ≤ weight r d`. All are used (hκ for sign of exponent in steps 2 and 4, hq for positivity/q_0 ≥ 1). No positivity of r needed (r j = 0 gives exponent 0 and a zero weight term, consistently).
- **Uses from project**: `Roth.weight` (Roth/Box.lean:71, unfolded in step 3).
- **Used by**: Roth/Main.lean: `abs_eval_lt_of_le_index` (l.400) only — `grep -rn abs_prod_pow_le_rpow_of_le_weight Roth/` gives the definition (l.347) and that use. Transitively feeds the upper bound of §7 used in the main theorem.
- **Visibility**: private
- **Lines**: 347–373, proof length 24 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). Preceded by a plain `--` comment rather than a docstring (acceptable for a private lemma).

## Junk check (Step 8)
- Used anywhere? Yes, once: `abs_eval_lt_of_le_index` (Roth/Main.lean:400), where it bounds each Taylor term, with `x j := h j / q j - α` and `c ≤ weight r d` supplied by `index_le_weight`.
- Wrapper of 1–2 mathlib calls? No: a 24-line four-step rpow/product estimate.
- Does mathlib have it? No. leansearch (query on product of powers bounded via weighted exponent) returns only generic product-norm bounds (`norm_prod_le_of_le`, `Finset.nnnorm_prod_le`, `Multipliable.abs_tprod`, ultrametric variants, `MvPowerSeries.le_weightedOrder_prod`), none of which is this estimate; it depends on the project's `weight` and the Roth-specific growth condition `hqr`.
- Too specific / inline? It is specific to Roth's §7, but inlining would bloat `abs_eval_lt_of_le_index` (already ~25 lines) by a nested 20-line calc inside a term argument; the separate helper is the cleaner factoring.
- Well-chosen? Yes; the statement isolates exactly the analytic estimate, with hypotheses in the form available at the call site.
- Conclusion: `KEEP` — action: keep as private helper for `abs_eval_lt_of_le_index`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Main.lean:347).

Even if public, it would not be a mathlib candidate: it is a Roth-specific estimate phrased in terms of the project's `weight` and the denominator-growth condition from Roth's theorem.

## Evidence
- `grep -rn abs_prod_pow_le_rpow_of_le_weight Roth/`: definition l.347, single use l.400.
- `grep` of mathlib `Analysis/SpecialFunctions/Pow/Real.lean`: confirmed the used lemmas `Real.rpow_sum_of_pos` (l.243) and `Real.rpow_le_rpow_of_nonpos` (l.565) exist; no combined estimate.
- `lean_leansearch` (1 query, 6 results listed above): no matching lemma.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
