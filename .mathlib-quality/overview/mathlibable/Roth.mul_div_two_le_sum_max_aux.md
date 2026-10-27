---
decl: Roth.mul_div_two_le_sum_max_aux
file: Roth/Theta.lean
line: 304
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private case lemma of min_le_sum_max (case l ≤ θr) giving lθ/2 ≤ ∑_{ν<l} max(0, θ - ν/r) via the Gauss sum; used twice in Theta.lean, nothing in mathlib states it, too specific to upstream.
action: Keep as private helper for its call sites Roth/Theta.lean:354 (mul_sq_div_three_le_sum_max_aux) and Roth/Theta.lean:369 (min_le_sum_max); no change needed.
---

# Roth.mul_div_two_le_sum_max_aux

## Inventory entry

### `theorem Roth.mul_div_two_le_sum_max_aux`
- **Type**: `∀ {θ r : ℝ} {l : ℕ}, (l : ℝ) ≤ θ * r → (l : ℝ) * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`
- **What**: If l ≤ θ r, then the truncated arithmetic-progression sum ∑_{ν<l} max(0, θ - ν/r) is at least lθ/2. This is the case "θ r_p ≥ l" of the combined estimate in §5, proof of Lemma 6 of the source (the sum has all l terms, average term ≥ θ/2).
- **How**: Case l = 0 by `simp`. Case θ ≤ 0: the left side is ≤ 0 (`div_nonpos_of_nonpos_of_nonneg`, `mul_nonpos_of_nonneg_of_nonpos`) and the right side is ≥ 0 (`Finset.sum_nonneg`, `le_max_left`). Otherwise r > 0 by `pos_of_mul_pos_right`; drop the `max` with `Finset.sum_le_sum` + `le_max_right`, expand ∑(θ - ν/r) = lθ - (∑ν)/r (`Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_range`, `nsmul_eq_mul`, `Finset.sum_div`), clear denominators (`div_add_div`, `div_le_iff₀`), and close with `linarith only` using the cast of the Gauss identity `Finset.sum_range_id_mul_two l` (∑_{ν<l} ν · 2 = l(l-1)) and l(θr - l) ≥ 0.
- **Hypotheses**: `hl : (l : ℝ) ≤ θ * r`. No sign hypotheses on θ or r (handled by case split: θ ≤ 0 is trivial, θ > 0 forces r > 0 when l > 0).
- **Uses from project**: `[]` (only mathlib lemmas)
- **Used by**: Roth/Theta.lean only (`grep -rn mul_div_two_le_sum_max_aux Roth/`): `mul_sq_div_three_le_sum_max_aux` (private, l.343; use at l.354, boundary case θr = l) and `min_le_sum_max` (public, l.362; use at l.369, case l ≤ θr). Transitively via `min_le_sum_max`: `index_le_lem6` (Roth/Theta.lean:556, use at l.586) and its downstream (Lemma 6).
- **Visibility**: private
- **Lines**: 304–320, proof length 15 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). The hypothesis is stronger than needed: in the θ, r > 0 case the inequality lθ - l(l-1)/(2r) ≥ lθ/2 holds iff l - 1 ≤ θr, so `l ≤ θ * r + 1` would suffice; the stronger form matches the source case split and both call sites, so no change is warranted.

## Junk check (Step 8)
- Used anywhere? Yes, twice: Roth/Theta.lean:354 (`mul_sq_div_three_le_sum_max_aux`) and Roth/Theta.lean:369 (`min_le_sum_max`).
- Wrapper of 1–2 mathlib calls? No: a 15-line proof with a three-way case split, the Gauss sum `Finset.sum_range_id_mul_two`, denominator clearing and `linarith`.
- Does mathlib have it? No. `lean_leansearch` ("lower bound for sum over range of arithmetic progression theta - nu / r, half of l times theta") returns only unrelated lemmas (`Finset.sum_range_le_sum` over ℤ, `Chebyshev.theta`, `Nat.geom_sum_le`); `lean_loogle` `Finset.sum (Finset.range _) (fun _ => max 0 _)` returns no results. Mathlib has the ingredient `Finset.sum_range_id_mul_two` but no truncated arithmetic-progression bound.
- Too specific / inline? It is specific to the Lemma 6 computation, but it has two call sites, and inlining into `min_le_sum_max` and `mul_sq_div_three_le_sum_max_aux` would duplicate 15 lines. The private-helper factoring mirrors the source's case split (θ r_p ≥ l vs θ r_p < l) and is the right granularity.
- Well-chosen? Yes; name follows mathlib conventions (`mul_div_two_le_sum_max`), `_aux` + `private` correctly marks it as internal. Sign hypotheses were deliberately removed via case analysis, keeping call sites clean.
- Conclusion: `KEEP` — action: keep as private helper for Roth/Theta.lean:354 and :369; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:304; the name also ends in `_aux`, so the Step 9a pre-filter would fire independently).

Note: the public parent `Roth.min_le_sum_max` is the natural unit for any upstreaming discussion; this lemma would travel with it as a private helper. It is an elementary real-number estimate specific to Roth's Lemma 6 and has no standard literature form.

## Evidence
- `grep -rn mul_div_two_le_sum_max_aux Roth/`: definition l.304, uses l.354 and l.369.
- `grep -rn min_le_sum_max Roth/`: downstream use in `index_le_lem6` at Roth/Theta.lean:586.
- `lean_leansearch` (query above, 6 results): none relevant.
- `lean_loogle` `Finset.sum (Finset.range _) (fun _ => max 0 _)`: no results.
- No Lean runs and no evidence Lean files (private SKIP; no weakening claimed beyond the hand computation recorded in Notes, which is not acted on; the project builds clean so the lemma compiles as stated).
