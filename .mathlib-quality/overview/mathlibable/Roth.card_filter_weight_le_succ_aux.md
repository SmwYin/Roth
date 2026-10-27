---
decl: Roth.card_filter_weight_le_succ_aux
file: Roth/Lattice.lean
line: 166
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private inductive step (m = n+1 with n at least 1 and lam above 2 sqrt(n+1)) of Lemma 8 card_filter_weight_le; combines card_filter_box_last, card_filter_fiber_eq, the induction hypothesis and sum_inv_lt in a 4-step calc, so it is project-specific Roth combinatorics with no mathlib counterpart.
action: Keep as private helper for its sole use in card_filter_weight_le (Roth/Lattice.lean:218); no upstream action (the public Lemma 8 statement is assessed separately).
---

# Roth.card_filter_weight_le_succ_aux

## Inventory entry

### `theorem Roth.card_filter_weight_le_succ_aux`
- **Type**: `∀ {n : ℕ} (r : Fin (n + 1) → ℕ), 0 < r (Fin.last n) → 0 < n → ∀ {lam : ℝ}, 2 * √((n + 1 : ℕ) : ℝ) < lam → (∀ {t : ℝ}, 0 < t → (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight (r ∘ Fin.castSucc) d ≤ ((n : ℝ) - t) / 2).card : ℝ) ≤ 2 * √(n : ℝ) / t * ∏ j, (((r ∘ Fin.castSucc) j : ℝ) + 1)) → (((box r).filter fun d ↦ weight r d ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √((n + 1 : ℕ) : ℝ) / lam * ∏ j, ((r j : ℝ) + 1)` (declared `private lemma`).
- **What**: The inductive step of Lemma 8 (lattice count estimate) in the nontrivial regime: assuming the Lemma 8 bound in dimension `n` for the truncated box `r ∘ castSucc` and all `t > 0`, it holds in dimension `n + 1` for every `lam > 2 √(n+1)`, provided `n ≥ 1` and the last side `r_last ≥ 1`. Mathematically: split the count by the value `i ∈ [0, r_last]` of the last coordinate; the fibre over `i` is the `n`-dimensional count with `lam` replaced by `lam - 1 + 2i/r_last`; apply the hypothesis to each fibre and bound the resulting harmonic-type sum `∑_i (lam - 1 + 2i/r_last)⁻¹` by `lam⁻¹ √((n+1)/n) (r_last + 1)`.
- **How**: `sum_inv_lt` (with `m := n + 1`, using `hr` and `Nat.succ_le_succ hn`), simplified by `push_cast [add_sub_cancel_right]`; rewrite the count with `card_filter_box_last`, `Nat.cast_sum`, and `Finset.sum_congr` with `card_filter_fiber_eq`; then a 4-step calc: (1) `Finset.sum_le_sum` with `ih`, positivity of `lam - 1 + 2i/R` via `Real.one_le_sqrt` and `linarith`; (2) factor out with `Finset.mul_sum` and `ring`; (3) `mul_le_mul_of_nonneg_left hs.le` with `positivity`; (4) `Fin.prod_univ_castSucc`, `push_cast`, `field_simp`, `simp [R]`.
- **Hypotheses**: `hr` (feeds `sum_inv_lt`'s `1 ≤ r` and the division by `R`), `hn` (feeds `sum_inv_lt`'s `2 ≤ m`; also needed since `√n` is inverted), `hlam` (feeds `sum_inv_lt` and positivity of the shifted parameters), `ih` (the per-fibre bound). All used; none removable.
- **Uses from project**: `Roth.box` (Roth/Box.lean), `Roth.weight` (Roth/Box.lean:71), `Roth.sum_inv_lt` (Roth/Lattice.lean:68), `Roth.card_filter_box_last` (Roth/Lattice.lean:131), `Roth.card_filter_fiber_eq` (Roth/Lattice.lean:148).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_weight_le` only (l.218, the `succ n` case with `lam > 2 √(n+1)` and `n > 0`). `grep -rn card_filter_weight_le_succ_aux Roth/` returns only the definition (l.166) and this use.
- **Visibility**: private
- **Lines**: 166–199, proof length 27 lines (173–199)
- **Notes**: Name ends in `_aux`; would also be caught by the Step 9a pre-filter. The `ih` hypothesis is stated with an implicit-binder `∀ {t : ℝ}`, matching how `card_filter_weight_le`'s `induction ... generalizing lam` hypothesis is supplied.

## Junk check (Step 8)
- Used anywhere? Yes, once: the main inductive case of the public `Roth.card_filter_weight_le` (Lemma 8), l.218.
- Wrapper of 1–2 mathlib calls? No: a 27-line calc combining three project lemmas (`card_filter_box_last`, `card_filter_fiber_eq`, `sum_inv_lt`) with the induction hypothesis and real arithmetic.
- Does mathlib have it? No. It is a statement about the project-specific `Roth.box` / `Roth.weight` and the specific bound `2 √m / λ · ∏ (r_j + 1)` from Roth's theorem (Lemma 8 of the source); no mathlib result counts weighted lattice points in a box. A `grep -rln` of `.lake/packages/mathlib/Mathlib/` for `card_filter.*weight` and `weight.*≤.*box` returns no hits; the ingredients it uses from mathlib (`Finset.sum_le_sum`, `Finset.mul_sum`, `Fin.prod_univ_castSucc`, `mul_le_mul_of_nonneg_left`, `Real.one_le_sqrt`) are generic.
- Too specific / inline? It could be inlined into the `succ` branch of `card_filter_weight_le`, but that would put a 27-line calc inside an `induction` branch already containing two case splits; as a separate lemma it isolates the inductive step cleanly, and the sibling `card_filter_weight_le_of_le_sqrt_aux` handles the complementary case the same way. Keeping it separate is the better style.
- Well-chosen? Yes; hypotheses are exactly those of the regime in which it is applied, and all are used.
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:166); additionally the name ends in `_aux`.

Side note: any upstreamable content would be the public Lemma 8 `Roth.card_filter_weight_le` and the numeric `Roth.sum_inv_lt`, assessed separately (the latter as BORDERLINE/keep-in-project).

## Evidence
- `grep -rn card_filter_weight_le_succ_aux Roth/`: definition l.166, sole use l.218 (`card_filter_weight_le`).
- Read Roth/Lattice.lean l.60–219 (`sum_inv_lt`, `card_filter_box_fiber_aux`, `card_filter_box_last`, `filter_weight_le_eq_empty`, `card_filter_fiber_eq`, `card_filter_weight_le_of_le_sqrt_aux`, this lemma, `card_filter_weight_le`) to confirm the uses-from-project list and the hypothesis usage.
- `grep -rn` over Roth/ for `weight`, `card_box`, `weight_add`, `weight_single`, `weight_mapDomain`, `sum_inv_lt` to locate dependencies (Roth/Box.lean:57–127, Roth/Lattice.lean:68).
- Consulted sibling reports `Roth.sum_inv_lt.md`, `Roth.card_filter_weight_le_of_le_sqrt_aux.md`, `Roth.card_filter_box_fiber_aux.md` for consistency.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
