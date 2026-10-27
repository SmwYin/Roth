---
decl: Roth.roth_product_bound_aux
file: Roth/Main.lean
line: 481
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private step of the section 7 proof of Roth's theorem packaging three facts about B = mainCoeffBound delta q_0 r_0 (B > 0, B at most q_0^(delta r_0), prod (r_j + 1) < B^delta) from (32) via sqrt_lt_floor, four_lt_rpow and three_small_factors; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
action: Keep as private helper of its single call site Roth/Main.lean:559 (roth_of_isIntegral); no change.
---

# Roth.roth_product_bound_aux

## Inventory entry

### `theorem Roth.roth_product_bound_aux`
- **Type**: `∀ {m : ℕ} [NeZero m] {α A δ : ℝ}, 0 ≤ δ → 0 ≤ A → ∀ {q r : Fin m → ℕ}, 0 < r 0 → (∀ j, r j ≤ r 0) → 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0) → 0 < (mainCoeffBound δ (q 0) (r 0) : ℝ) ∧ (mainCoeffBound δ (q 0) (r 0) : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) ∧ (∏ j, ((r j : ℝ) + 1)) < (mainCoeffBound δ (q 0) (r 0) : ℝ) ^ δ`
- **What**: Let m ≥ 1, δ ≥ 0, A ≥ 0, natural degrees r_j with r_0 > 0 maximal among them, and suppose the size condition (32) 2m + 1 + 2m log(1+A) + 2m log(1+|α|) ≤ δ² log q_0 holds. Then the coefficient scale B = ⌊q_0^{δ r_0}⌋ satisfies B > 0, B ≤ q_0^{δ r_0}, and ∏_j (r_j + 1) < B^δ. These are exactly the three facts about B consumed by the logarithmic comparison `roth_log_bound_aux` in §7 of the source.
- **How**: From (32), m ≥ 1, and nonnegativity of the two logarithms (`Real.log_nonneg`, `le_add_of_nonneg_right`) `linarith` gives 3 ≤ δ² log q_0; `Roth.four_lt_rpow` (Roth/MainLemma.lean:122) turns this into 4 < q_0^{δ r_0}, and `Roth.sqrt_lt_floor` (Roth/MainLemma.lean:115) gives √X < ⌊X⌋₊ ≤ X, whence B > 0 (via `Real.sqrt_nonneg`) and B ≤ q_0^{δ r_0}. For the product: each r_j + 1 ≤ 2^{r_j} ≤ 2^{r_0} (`Nat.lt_two_pow_self`, `Nat.pow_le_pow_right`, hr0max), so mathlib's `Finset.prod_le_pow_card` gives ∏ (r_j + 1) ≤ (2^{r_0})^m = 2^{m r_0} (cast to ℝ with `pow_mul`, `mul_comm`, `exact_mod_cast`), and the first component of `Roth.three_small_factors` (Roth/MainLemma.lean:180), 2^{m r_0} < B^δ, finishes.
- **Hypotheses**: hδ0 (for `four_lt_rpow`, `three_small_factors`); hA (log(1+A) ≥ 0 in h32', and `three_small_factors`); hr0 (for `four_lt_rpow`, `three_small_factors`); hr0max (bounding each factor by 2^{r_0}); h32 (source of h32' and input to `three_small_factors`); `[NeZero m]` (gives hm1 : 1 ≤ m, used implicitly by `linarith` for 2m + 1 ≥ 3). All used, none redundant. α appears only through h32.
- **Uses from project**: `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.sqrt_lt_floor` (Roth/MainLemma.lean:115), `Roth.four_lt_rpow` (Roth/MainLemma.lean:122), `Roth.three_small_factors` (Roth/MainLemma.lean:180).
- **Used by**: Roth/Main.lean:559 `Roth.roth_of_isIntegral` (destructured into hBpos, hBX, hN, passed to `roth_log_bound_aux`). `grep -rn roth_product_bound_aux Roth/` gives only the definition (l.481) and this use. Transitively feeds `Roth.roth` and `Roth.roth_rat`.
- **Visibility**: private
- **Lines**: 481–502, proof length 16 lines (487–502; statement 481–486)
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; preceded by a plain `--` comment, not a docstring (acceptable for private). `hm1` is never named in a term but is required by the `linarith` call in `h32'`. Degrees r_j are only used through hr0max, so q and r beyond index 0 matter only via the product.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Main.lean:559 in `roth_of_isIntegral`.
- Wrapper of 1–2 mathlib calls? No. It chains three project lemmas (`four_lt_rpow`, `sqrt_lt_floor`, `three_small_factors`) with a product estimate through `Finset.prod_le_pow_card`; about five substantive steps.
- Does mathlib have it? No: the statement is about the Roth-specific `mainCoeffBound` and the Roth size condition (32); nothing general. The only general ingredient, ∏ (r_j + 1) ≤ 2^{m·max r}, is already a direct `Finset.prod_le_pow_card` application (Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:286) plus `Nat.lt_two_pow_self` (Lean core Init/Data/Nat/Lemmas.lean:1231).
- Too specific (inline?)? Specific to its one call site and could be inlined into `roth_of_isIntegral`, but it is deliberately factored out together with its sibling `_aux` lemmas (`exists_roth_parameters_aux`, `exists_roth_approximants_aux`, `one_lt_roth_eval_bound_aux`, `roth_log_bound_aux`) so the main proof reads as a short chain mirroring §7 of the source; inlining would lengthen `roth_of_isIntegral` by ~16 lines with no gain.
- Well-chosen statement? Yes: hypotheses are the minimal ones the three helper lemmas require (non-strict `hδ0`, `h32` in the weakened `≤` form; the caller passes `.le`), and the three conclusions match the `hBpos`, `hBX`, `hN` hypotheses of `roth_log_bound_aux` verbatim with B := mainCoeffBound δ (q 0) (r 0).
- Conclusion: `KEEP`. Action: keep as private helper of its single call site (Roth/Main.lean:559); no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Main.lean:481; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the ingredients are assessed under their own entries (`Roth.mainCoeffBound.md`; `Roth.sqrt_lt_floor`, `Roth.four_lt_rpow`, `Roth.three_small_factors` under theirs).

## Evidence
- `grep -rn roth_product_bound_aux Roth/`: definition Roth/Main.lean:481, single use Roth/Main.lean:559.
- Read the body (Roth/Main.lean:480–502), the call site (Roth/Main.lean:545–563) and the dependency statements `mainCoeffBound` (Roth/MainLemma.lean:69), `sqrt_lt_floor` (l.115), `four_lt_rpow` (l.122), `three_small_factors` (l.180).
- Located the mathlib/core lemmas used: `Finset.prod_le_pow_card` (Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:286), `Nat.lt_two_pow_self` (Lean v4.34.0 Init/Data/Nat/Lemmas.lean:1231).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
