---
decl: Roth.mul_sq_div_three_le_sum_max_aux
file: Roth/Theta.lean
line: 347
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: INLINE
rationale: Private 9-line case-dispatch lemma (r ≤ 0 / θr < l / θr = l) for the rθ²/3 branch of min_le_sum_max; its sole caller passes a strict θ rp < l so the equality branch is dead, and inlining into min_le_sum_max compiles (evidence file).
action: Inline into min_le_sum_max (Roth/Theta.lean:370) as an rp = 0 split plus a direct call to mul_sq_div_three_le_sum_max_of_pos_aux, delete this lemma (removing the mul_div_two_le_sum_max_aux use at Roth/Theta.lean:354); proof in evidence/Roth.mul_sq_div_three_le_sum_max_aux/inline_into_min_le_sum_max.lean.
---

# Roth.mul_sq_div_three_le_sum_max_aux

## Inventory entry

### `theorem Roth.mul_sq_div_three_le_sum_max_aux`
- **Type**: `∀ {θ r : ℝ}, 0 ≤ θ → ∀ {l : ℕ}, θ * r ≤ (l : ℝ) → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`
- **What**: If θ ≥ 0 and θ r ≤ l, then the truncated arithmetic-progression sum ∑_{ν<l} max(0, θ - ν/r) is at least r θ²/3. This is the case "θ r_p < l" of the combined estimate in §5, proof of Lemma 6 of the source ("∑_{ν<l} max(0, θ - ν/r_p) ≥ min(lθ/2, r_p θ²/3)"), extended to the closed case θ r ≤ l and to arbitrary real r, with no θ r_p > 10 assumption.
- **How**: Three-way case dispatch. (i) r ≤ 0: left side ≤ 0 (`div_nonpos_of_nonpos_of_nonneg`, `mul_nonpos_of_nonpos_of_nonneg`, `sq_nonneg`) and right side ≥ 0 (`Finset.sum_nonneg`, `le_max_left`). (ii) θ r < l (via `lt_or_eq_of_le`): the private `mul_sq_div_three_le_sum_max_of_pos_aux`. (iii) θ r = l: from the private `mul_div_two_le_sum_max_aux` (lθ/2 ≤ ∑) and lθ = rθ² (`congrArg (· * θ) hl`), rθ²/3 ≤ rθ²/2 = lθ/2, closed by `linarith only` with `mul_nonneg hr.le (sq_nonneg θ)`.
- **Hypotheses**: `hθ : 0 ≤ θ` (necessary: for θ < 0 < r with l = 0 the right side is 0 and the left side is positive), `hl : θ * r ≤ l` (closed form; the only caller actually has the strict form). No sign hypothesis on r (case r ≤ 0 is trivial).
- **Uses from project**: `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` (private, Roth/Theta.lean:322), `Roth.mul_div_two_le_sum_max_aux` (private, Roth/Theta.lean:304)
- **Used by**: Roth/Theta.lean only (`grep -rn mul_sq_div_three_le_sum_max_aux Roth/`): `min_le_sum_max` (public, l.362; single use at l.370, case θ ≤ 0 excluded and l > θ rp strict, passed as `hl.le`). Transitively: `index_le_lem6` (Roth/Theta.lean:556, use at l.586) and Lemma 6 downstream.
- **Visibility**: private
- **Lines**: 347–355, proof length 7 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). The only call site supplies `hl.le` from a strict `θ * rp < l`, so branch (iii) (and with it the use of `mul_div_two_le_sum_max_aux` at l.354) is never exercised from the project; branch (i) is exercised only when rp = 0 (rp : ℕ at the call site).

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: Roth/Theta.lean:370 in `min_le_sum_max`.
- Wrapper of 1–2 mathlib calls? No, but it is a thin dispatcher: two project lemmas plus a trivial sign case.
- Does mathlib have it? No. `lean_leansearch` ("r * θ^2 / 3 ≤ sum over range l of max 0 (θ - ν / r) when θ * r ≤ l", 6 results) returns only unrelated lemmas (`sum_div_pow_sq_le_div_sq`, `Finset.sum_le_sum_range`, `Finset.sum_range_le_sum`, `Finset.le_sum_schlomilch`, `Real.tsum_le_of_sum_range_le`, a geometric bound). The sibling reports for `mul_div_two_le_sum_max_aux` and `mul_sq_div_three_le_sum_max_of_pos_aux` record that `lean_loogle` `Finset.sum (Finset.range _) (fun _ => max 0 _)` returns nothing.
- Too specific / inline? Yes. Single caller, and the caller has the strict hypothesis, so a third of the proof (the θr = l branch) is dead. Inlining into `min_le_sum_max` replaces it with an `rp = 0` split (`Nat.eq_zero_or_pos`; then `min_le_right` and `simpa` with the sum's nonnegativity) and a direct call to `mul_sq_div_three_le_sum_max_of_pos_aux (by exact_mod_cast hrp) (le_of_not_ge hθ) hl`. This was compiled clean (evidence file below, `min_le_sum_max'`, same statement as `min_le_sum_max`).
- Well-chosen? The closed-form statement (θ r ≤ l) is mathematically tidy, but it has no second consumer, and the generality is paid for by a dead branch. Name and `private`/`_aux` are fine.
- Conclusion: `INLINE`. Action: in Roth/Theta.lean replace the last line of `min_le_sum_max` (l.370) with the `rp = 0` split plus the direct `mul_sq_div_three_le_sum_max_of_pos_aux` call (verbatim in the evidence file), delete `mul_sq_div_three_le_sum_max_aux` (l.347–355). Side effect: `mul_div_two_le_sum_max_aux` drops to one use (l.369), and `mul_sq_div_three_le_sum_max_of_pos_aux`'s call site moves to `min_le_sum_max`. Low priority (saves about 6 lines); KEEP is also acceptable if the closed-form helper is wanted.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:347; the name also ends in `_aux`, so the Step 9a pre-filter would fire independently).

Note: the public parent `Roth.min_le_sum_max` is the natural unit for any upstreaming discussion; this is an elementary real-number estimate specific to Roth's Lemma 6 with no standard literature form.

## Evidence
- `grep -rn mul_sq_div_three_le_sum_max_aux Roth/`: definition l.347, single use l.370 (`min_le_sum_max`).
- `grep` for `min_le_sum_max` and `mul_div_two_le_sum_max_aux`: definitions l.362 and l.304; uses l.586 (`index_le_lem6`), l.354 and l.369.
- `lean_leansearch` (query above, 6 results): none relevant.
- Evidence file `.mathlib-quality/overview/evidence/Roth.mul_sq_div_three_le_sum_max_aux/inline_into_min_le_sum_max.lean` (`import Roth.Theta`; copies the two private helpers verbatim under namespace `RothEvidence`, then proves `min_le_sum_max'`, the statement of `min_le_sum_max`, without this lemma). `lake env lean` on it: compiles with no errors or warnings (about 38 s). A first attempt with `import Mathlib.Analysis.SpecialFunctions.Pow.Real` failed only because `Finset.sum_div` was not in scope; the file was switched to `import Roth.Theta`, and the final file is the one that compiles.
