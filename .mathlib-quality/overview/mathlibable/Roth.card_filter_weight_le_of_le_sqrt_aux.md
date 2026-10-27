---
decl: Roth.card_filter_weight_le_of_le_sqrt_aux
file: Roth/Lattice.lean
line: 158
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private trivial-range case of Lemma 8 (lam at most 2 sqrt m) where the bound exceeds the full box size; a 3-step calc from Finset.card_filter_le, card_box and le_mul_of_one_le_left, used once in card_filter_weight_le.
action: Keep as private helper for its sole use in Roth.card_filter_weight_le (Roth/Lattice.lean:212); optionally inline it there, nothing to upstream.
---

# Roth.card_filter_weight_le_of_le_sqrt_aux

## Inventory entry

### `theorem Roth.card_filter_weight_le_of_le_sqrt_aux`
- **Type**: `∀ (m : ℕ) (r : Fin m → ℕ) {lam : ℝ}, 0 < lam → lam ≤ 2 * √(m : ℝ) → (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1)` (declared `private lemma`).
- **What**: The easy case of Lemma 8 (lattice count estimate): when `0 < λ ≤ 2√m`, the claimed bound `2√m λ⁻¹ ∏ (r_j + 1)` is at least the total number `∏ (r_j + 1)` of points of the box, so the filtered count is trivially below it.
- **How**: A three-step `calc`: filtered card ≤ `(box r).card` by `Finset.card_filter_le` (cast with `exact_mod_cast`); `(box r).card = ∏ (r j + 1)` by `simp [card_box]`; then `le_mul_of_one_le_left` with nonnegativity from `positivity` and `1 ≤ 2√m / λ` from `(one_le_div hlam).2 h`.
- **Hypotheses**: `hlam : 0 < lam` (used in `one_le_div`) and `h : lam ≤ 2 * √m` (the case condition) are both needed for `1 ≤ 2√m/λ`. The filter predicate (weight bound) is never used: the statement holds for any decidable predicate, the weight only appears to match the shape of `card_filter_weight_le`.
- **Uses from project**: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71, statement only), `Roth.card_box` (Roth/Box.lean:57).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_weight_le` only (l.212, the `lam ≤ 2 * √(n+1)` branch of the `succ` case). `grep -rn card_filter_weight_le_of_le_sqrt Roth/` returns only the definition (l.158) and this use.
- **Visibility**: private
- **Lines**: 158–164, proof length 4 lines (161–164)
- **Notes**: Name ends in `_aux`; would also be caught by the Step 9a pre-filter. `m` is explicit although determined by `r`; harmless for a private helper (the caller passes `(n + 1)`).

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.card_filter_weight_le` (l.212), the trivial branch of the `by_cases h : lam ≤ 2 * √(n+1)`.
- Wrapper of 1–2 mathlib calls? Essentially a short composition of three facts (`Finset.card_filter_le`, `Roth.card_box`, `le_mul_of_one_le_left` + `one_le_div`); not a single-call wrapper.
- Does mathlib have it? No as such: it is specific to the project's `box`/`weight` and the Lemma 8 constant. The general content (card of a filter ≤ card of the set; `b ≤ a * b` for `1 ≤ a`) is already mathlib (`Mathlib/Data/Finset/Card.lean:278`, `Mathlib/Algebra/Order/GroupWithZero/Basic.lean:364`, `Mathlib/Algebra/Order/Field/Basic.lean:41`).
- Too specific / inline? Single use and only 4 proof lines, so inlining into the `by_cases` branch of `card_filter_weight_le` is feasible. Keeping it separate mirrors the paper's case split (trivial case vs. the inductive `card_filter_weight_le_succ_aux` case) and keeps the main induction readable, so either choice is acceptable; no pressure to change.
- Well-chosen? Yes for its role; it could be stated for an arbitrary predicate, but there is no second consumer to justify that.
- Conclusion: `KEEP`. Action: none required; optional inline at Roth/Lattice.lean:212.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:158); additionally the name ends in `_aux`.

Side note: the upstream-relevant statement, if any, is the public `Roth.card_filter_weight_le` (Lemma 8), assessed separately.

## Evidence
- `grep -rn card_filter_weight_le_of_le_sqrt Roth/`: definition l.158, sole use l.212 (`card_filter_weight_le`).
- `grep -rn` for `card_box`, `box`, `weight`, `weight_nonneg` definitions in Roth/: Roth/Box.lean:47, 57, 71, 75.
- `grep` in `.lake/packages/mathlib/Mathlib/`: `Finset.card_filter_le` (Data/Finset/Card.lean:278), `le_mul_of_one_le_left` (Algebra/Order/GroupWithZero/Basic.lean:364), `one_le_div` (Algebra/Order/Field/Basic.lean:41).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
