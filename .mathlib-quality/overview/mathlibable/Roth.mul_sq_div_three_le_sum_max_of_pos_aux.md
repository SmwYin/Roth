---
decl: Roth.mul_sq_div_three_le_sum_max_of_pos_aux
file: Roth/Theta.lean
line: 322
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private case lemma (θr < l, r > 0) of min_le_sum_max giving rθ²/3 ≤ ∑_{ν<l} max(0, θ - ν/r) via an inline floor/Gauss-sum bound valid for all θr ≥ 0; single call site, nothing in mathlib states it, too specific to upstream.
action: Keep as private helper for its call site Roth/Theta.lean:353 (mul_sq_div_three_le_sum_max_aux); separately remove the now-dead public floor_sq_div_two_le_sum and sq_div_three_lt_floor_sq_div_two (Roth/Theta.lean:289, :300), whose role this lemma's inline hbound took over.
---

# Roth.mul_sq_div_three_le_sum_max_of_pos_aux

## Inventory entry

### `theorem Roth.mul_sq_div_three_le_sum_max_of_pos_aux`
- **Type**: `∀ {θ r : ℝ}, 0 < r → 0 ≤ θ → ∀ {l : ℕ}, θ * r < (l : ℝ) → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`
- **What**: If r > 0, θ ≥ 0 and θ r < l, then the truncated arithmetic-progression sum ∑_{ν<l} max(0, θ - ν/r) is at least r θ²/3. This is the case "θ r_p < l" of the combined estimate in §5, proof of Lemma 6 of the source, but without the source's assumption θ r_p > 10: the inner bound (θr)²/3 ≤ ∑_{ν ≤ ⌊θr⌋} (θr - ν) is proved for every θr ≥ 0, replacing the source's two FACTs (⌊a⌋²/2 ≤ ∑ and a²/3 < ⌊a⌋²/2 for a > 10).
- **How**: Put n = ⌊θ r⌋₊, with `Nat.floor_le` (n ≤ θr) and `Nat.lt_floor_add_one` (θr < n + 1). Cast the Gauss identity `Finset.sum_range_id_mul_two (n + 1)` to ℝ. Inner claim `hbound`: (θr)²/3 ≤ ∑_{ν<n+1} (θr - ν), by expanding the sum (`Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_range`, `nsmul_eq_mul`), generalising θr to a, and a `linear_combination` certificate using the Gauss identity, `sq_nonneg a`, n ≥ 0 and (a - n)(n + 1 - a) ≥ 0. Then a `calc`: rewrite rθ²/3 = (θr)²/3 / r (`eq_div_iff`), divide `hbound` by r (`div_le_div_iff_of_pos_right`), distribute the division (`Finset.sum_div`, `sub_div`, `mul_div_cancel_right₀`) and bound each term by its positive part (`Finset.sum_le_sum`, `le_max_right`), and finally enlarge the index range from n + 1 to l (`Finset.sum_le_sum_of_subset_of_nonneg`, `Finset.range_subset_range`, `Nat.floor_lt`, `le_max_left`).
- **Hypotheses**: `hr : 0 < r` (needed for the division by r; the r ≤ 0 case is handled trivially by the caller), `hθ : 0 ≤ θ` (necessary: for θ < 0 < r the right side is 0 and the left side is positive), `hl : θ * r < l` (strict is needed for ⌊θr⌋ + 1 ≤ l; the equality case θr = l is handled by the caller via `mul_div_two_le_sum_max_aux`).
- **Uses from project**: `[]` (only mathlib lemmas)
- **Used by**: Roth/Theta.lean only (`grep -rn mul_sq_div_three_le_sum_max_of_pos_aux Roth/`): `mul_sq_div_three_le_sum_max_aux` (private, l.347; use at l.353, case θr < l). Transitively: `min_le_sum_max` (public, l.362; use at l.370), then `index_le_lem6` (Roth/Theta.lean:586) and Lemma 6 downstream.
- **Visibility**: private
- **Lines**: 322–345, proof length 22 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). Its inline `hbound` is strictly stronger than the composition of the public `floor_sq_div_two_le_sum` and `sq_div_three_lt_floor_sq_div_two` (no a > 10 needed); those two public theorems are now unused in the project (see their reports, both junk REMOVE). `hbound` could be extracted as a public lemma `sq_div_three_le_sum_range_floor` replacing them, but it has only this one use.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Theta.lean:353 in `mul_sq_div_three_le_sum_max_aux`, which feeds the public `min_le_sum_max`.
- Wrapper of 1–2 mathlib calls? No: a 22-line proof with a floor argument, a cast Gauss identity, a `linear_combination` certificate and a 4-step `calc`.
- Does mathlib have it? No. `lean_leansearch` ("sum over range ... lower bound a squared over three, sum of max 0 (θ - ν / r)", 6 results) returns only unrelated lemmas (`Chebyshev.theta_eq_theta_coe_floor`, `Finset.sum_range_le_sum`, Abel summation, `sum_div_nat_floor_pow_sq_le_div_sq`, `Int.le_floor_add`); `lean_loogle` `Finset.sum (Finset.range _) (fun _ => max 0 _)` returns no results. Mathlib supplies only the ingredients (`Finset.sum_range_id_mul_two`, `Nat.floor_le`, `Nat.lt_floor_add_one`).
- Too specific / inline? Single caller, so inlining into `mul_sq_div_three_le_sum_max_aux` is possible, but it would put a 22-line proof inside one branch of a 3-way case split. The separate private lemma mirrors the source's case split (θr < l vs θr ≥ l) and keeps the caller readable; the split is the right granularity.
- Well-chosen? Yes. Name follows mathlib conventions; `private` plus `_aux` correctly mark it internal; hypotheses are each necessary for this statement (see Inventory). The improvement over the source (no θr > 10) is the reason the old FACT lemmas went dead.
- Conclusion: `KEEP`. Action: keep as private helper for Roth/Theta.lean:353; no change to this lemma. Related cleanup (not this lemma's action item per se): remove dead `floor_sq_div_two_le_sum` and `sq_div_three_lt_floor_sq_div_two`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:322; the name also ends in `_aux`, so the Step 9a pre-filter would fire independently).

Note: the public parent `Roth.min_le_sum_max` is the natural unit for any upstreaming discussion; this lemma would travel with it as a private helper. It is an elementary real estimate specific to Roth's Lemma 6 with no standard literature form.

## Evidence
- `grep -rn mul_sq_div_three_le_sum_max_of_pos_aux Roth/`: definition l.322, single use l.353.
- `grep -rn "floor_sq_div_two_le_sum\|sq_div_three_lt_floor_sq_div_two\|min_le_sum_max" Roth/`: the two FACT lemmas have no uses beyond their definitions; `min_le_sum_max` used at Roth/Theta.lean:586.
- Existing reports read: Roth.mul_div_two_le_sum_max_aux, Roth.floor_sq_div_two_le_sum, Roth.sq_div_three_lt_floor_sq_div_two.
- `lean_leansearch` (query above, 6 results): none relevant. `lean_loogle` `Finset.sum (Finset.range _) (fun _ => max 0 _)`: no results.
- No Lean runs and no evidence Lean files (private SKIP; necessity of hypotheses argued by hand counterexample/caller structure, no weakening claimed; the project builds clean so the lemma compiles as stated).
