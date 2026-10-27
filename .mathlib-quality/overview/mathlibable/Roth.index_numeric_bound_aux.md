---
decl: Roth.index_numeric_bound_aux
file: Roth/Theta.lean
line: 531
kind: lemma
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private helper (Step 9a SKIP); it isolates the purely real-arithmetic final step of Lemma 6 (from min(l theta/2, r_p theta^2/3) at most l(Phi+delta) to theta at most 2(Phi+sqrt Phi+sqrt delta)), used once in index_le_lem6, about 17 lines of genuine case analysis that mathlib does not and should not contain.
action: Keep in Roth/Theta.lean:531-551 (sole call site Roth/Theta.lean:582 in Roth.index_le_lem6); no change needed.
---

# Roth.index_numeric_bound_aux

## Inventory entry

### `lemma Roth.index_numeric_bound_aux`
- **Type**: `{θ Φ δ rp l : ℝ} (hΦ : 0 ≤ Φ) (hδ1 : δ ≤ 1) (hrp : 3 ≤ rp) (hl : 0 < l) (hl' : l ≤ rp + 1) (hmin : min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ l * (Φ + δ)) : θ ≤ 2 * (Φ + √Φ + √δ)`
- **What**: The numerical conclusion of the source's Lemma 6 (§5). If `Φ ≥ 0`, `δ ≤ 1`, `r_p ≥ 3`, `0 < l ≤ r_p + 1` and `min(lθ/2, r_p θ²/3) ≤ l(Φ + δ)`, then `θ ≤ 2(Φ + Φ^{1/2} + δ^{1/2})`. In the paper this is the closing step "comparing the lower and upper bounds for the index of the Wronskian-type determinant `F`".
- **How**: `rcases min_le_iff.1 hmin`. Case 1 (`lθ/2 ≤ l(Φ+δ)`): cancel `l` with `mul_div_assoc`, `mul_le_mul_iff_right₀ hl`, `div_le_iff₀` to get `θ ≤ 2(Φ+δ)`, then `linarith only` with `Real.le_sqrt_self_iff.2 hδ1` (`δ ≤ √δ`) and `Real.sqrt_nonneg`. Case 2 (`r_p θ²/3 ≤ l(Φ+δ)`): from `hl'`, `hrp` get `3l ≤ 4 r_p`; a `linear_combination` (using `mul_le_mul_of_nonneg_right` and `nonneg_of_mul_nonneg_right` to get `Φ + δ ≥ 0`) plus `mul_le_mul_iff_right₀ hrp0` gives `θ² ≤ 4(Φ+δ)`; then `le_of_sq_le_sq` with a `linear_combination` of `Real.sq_sqrt'`, `Real.sq_sqrt hΦ`, `le_max_left` and `mul_nonneg (√Φ) (√δ)` yields `θ ≤ 2(√Φ + √δ)`, finished by `linarith only [hθ, hΦ]`.
- **Hypotheses**: `hΦ` (needed for `(√Φ)² = Φ` in case 2); `hδ1` (needed for `δ ≤ √δ` in case 1); `hrp` (gives `r_p > 0` and, with `hl'`, `3l ≤ 4r_p`); `hl` (cancelling `l`, and nonnegativity of `Φ+δ`); `hl'` (size comparison). No nonnegativity of `δ` is required because `Real.sqrt` truncates (`Real.sq_sqrt'` with `max δ 0`). All are used per inspection of the proof; no Lean minimality experiment was run.
- **Uses from project**: `[]` (all identifiers are mathlib: `min_le_iff`, `mul_div_assoc`, `mul_le_mul_iff_right₀`, `div_le_iff₀`, `Real.le_sqrt_self_iff`, `Real.sqrt_nonneg`, `mul_le_mul_of_nonneg_right`, `nonneg_of_mul_nonneg_right`, `div_nonneg`, `mul_nonneg`, `sq_nonneg`, `le_of_sq_le_sq`, `le_max_left`, `Real.sq_sqrt'`, `Real.sq_sqrt`; tactics `linarith`, `linear_combination`, `positivity`, `norm_num`).
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:582), via `apply index_numeric_bound_aux (Φ := Φ) (l := (l : ℝ)) ...`, with `hmin` supplied by `Roth.min_le_sum_max` chained with the lower/upper index bounds `sum_max_sub_le_index_det` and `index_det_le`. No other uses project-wide (`grep -rn index_numeric_bound_aux Roth/`: lines 531 and 582 only).
- **Visibility**: private
- **Lines**: 531–551 (statement 531–533, proof 534–551), proof length 18 lines
- **Notes**: No docstring (private); a comment line explains the `δ ≤ √δ` trick. The lemma deliberately works over arbitrary reals `rp l`, so the caller casts from `ℕ`. Its role mirrors `Roth.min_le_sum_max` (Roth/Theta.lean:362), which supplies the `min` lower bound.

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: `Roth.index_le_lem6` (Roth/Theta.lean:582), the final step of Lemma 6.
- Wrapper of 1–2 mathlib calls? No. Two-case analysis with cancellation, a squared bound via `linear_combination`, and a square-root comparison; about 18 lines.
- Does mathlib have it? No; it is a bespoke real inequality with Roth-specific constants (`3`, `2`, `4`, `r_p + 1`). `lean_leansearch` is not warranted for such a specific numeric statement; mathlib holds only the generic ingredients used (`Real.le_sqrt_self_iff`, `le_of_sq_le_sq`, `Real.sq_sqrt`).
- Too specific (inline)? Specific to Lemma 6 with one caller, but inlining it would put 18 lines of pure real arithmetic into the already long `index_le_lem6`, which currently reads as the paper's structural argument. Separating the arithmetic is the right factoring.
- Well-chosen? Yes. The statement is stated over plain reals with exactly the hypotheses the caller has at hand, so the caller only needs casts.
- Conclusion: `KEEP` — action: keep as is at Roth/Theta.lean:531–551; no change at the call site Roth/Theta.lean:582.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private

(The name also ends in `_aux`, which independently fires the Step 9a pre-filter. Content is a Roth-specific numerical inequality with no upstream value.)

## Evidence
- `sed -n 500,620p Roth/Theta.lean`: read the declaration, its neighbours and the call site in `index_le_lem6`.
- `sed -n 355,372p Roth/Theta.lean`: read `Roth.min_le_sum_max`, which produces the `hmin` hypothesis at the call site.
- `grep -rn index_numeric_bound_aux Roth/`: Roth/Theta.lean:531 (declaration), Roth/Theta.lean:582 (only use).
- `git log -S index_numeric_bound_aux`: appears in prior overview commits (neighbouring assessments) only as a cross-reference.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP/KEEP; the project builds clean so the lemma compiles as stated).
