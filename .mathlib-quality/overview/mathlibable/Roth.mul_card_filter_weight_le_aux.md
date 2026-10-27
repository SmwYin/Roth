---
decl: Roth.mul_card_filter_weight_le_aux
file: Roth/MainLemma.lean
line: 569
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 9-line arithmetic repackaging of Lemma 8 (card_filter_weight_le with lam = 4a sqrt m, multiplied by a, with the a le 0 case handled) into the counting inequality hD of Lemma 9; single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:612 (exists_mem_RSet_le_index_of_rpow_bound_aux); optional one-line docstring citing Lemma 8/9; no other change.
---

# Roth.mul_card_filter_weight_le_aux

## Inventory entry

### `theorem Roth.mul_card_filter_weight_le_aux`
- **Type**: `∀ {m : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∀ (a : ℝ), a * (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - 4 * a * √(m : ℝ)) / 2).card : ℝ) ≤ ((∏ j, (r j + 1) : ℕ) : ℝ) / 2`
- **What**: For m ≥ 1, positive r_1, …, r_m and any real a, let N(a) be the number of multi-indices d with 0 ≤ d_j ≤ r_j and weight ∑ d_j/r_j ≤ (m − 4a√m)/2. Then a · N(a) ≤ ½ ∏ (r_j + 1). For a > 0 this is Lemma 8 of §6 (N ≤ 2√m λ⁻¹ ∏(r_j+1)) with λ = 4a√m, multiplied through by a; for a ≤ 0 the left side is ≤ 0. In the caller a = c·deg f, and the inequality is the counting input "c · deg f · |J| ≤ ½ ∏(r_j+1)" of the Siegel-lemma step of Lemma 9.
- **How**: Case split on `0 < a`. Positive case: `mul_le_mul_of_nonneg_left` applied to `Roth.card_filter_weight_le m r hr (lam := 4 * a * √m)` (positivity of λ by `positivity`), then `trans_eq` and the identity a · (2√m/(4a√m)) · ∏(r_j+1) = ∏(r_j+1)/2 closed by `push_cast`, `field_simp` (using `ha.ne'` and `Real.sqrt_pos`/`Nat.cast_pos` from `hm` for √m ≠ 0) and `ring`. Nonpositive case: `mul_nonpos_of_nonpos_of_nonneg` (with `le_of_not_gt ha`, `Nat.cast_nonneg`) then `positivity` for the right side.
- **Hypotheses**: `hm : 0 < m` (needed: makes √m ≠ 0 for `field_simp`; the statement is false for m = 0, since then the filter is {0} (card 1) while the right side is 1/2, so a = 1 fails); `hr : ∀ j, 0 < r j` (passed to `card_filter_weight_le`, whose report records a compiled counterexample without it); `a` arbitrary real (the a ≤ 0 branch makes the caller not need a positivity side condition).
- **Uses from project**: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71), `Roth.card_filter_weight_le` (Roth/Lattice.lean:202). Mathlib names used: `mul_le_mul_of_nonneg_left`, `Real.sqrt_pos`, `Nat.cast_pos`, `mul_nonpos_of_nonpos_of_nonneg`, `le_of_not_gt`, `Nat.cast_nonneg`, tactics `push_cast`, `field_simp`, `ring`, `positivity`.
- **Used by**: Roth/MainLemma.lean:612 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (private, l.581), to produce `hD : c * f.natDegree * J.card ≤ (∏ (r j + 1) : ℕ) / 2` with a := c * f.natDegree (via `simpa [J, mul_assoc]`), which is fed to `pigeonhole_count`. Transitively: → `exists_mem_RSet_le_index_of_log_bound_aux` → … → `main_lemma`. `grep -rn mul_card_filter_weight_le_aux Roth/` gives only l.569 (definition) and l.612 (use).
- **Visibility**: private
- **Lines**: 569–579, proof length 9 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. Specialised to `Fin m` because `card_filter_weight_le` is.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:612 inside `exists_mem_RSet_le_index_of_rpow_bound_aux`.
- Wrapper of 1–2 mathlib calls? No. It wraps one project lemma (`card_filter_weight_le`) plus a case split and field arithmetic; it is not a thin wrapper of mathlib.
- Does mathlib have it? No. It is stated in terms of the project-local `box`/`weight` and is a rescaling of Roth's Lemma 8, which mathlib does not have (see `Roth.card_filter_weight_le.md`: not in mathlib, not composable). No mathlib search beyond that is meaningful for a parameter substitution of a project lemma.
- Too specific (inline?)? Single call site, 9 lines; inlining into the ~35-line caller is possible but would add a case split and a `field_simp` block to an already long proof. The factoring isolates the "Lemma 8 with λ = 4a√m" arithmetic cleanly, and handling all real a (not only a > 0) spares the caller a positivity proof of c · deg f. Keep factored.
- Well-chosen statement? Yes; hypotheses are exactly those needed (hm and hr both necessary, see Inventory). The output shape `((∏ (r j + 1) : ℕ) : ℝ) / 2` matches what `pigeonhole_count` consumes. A docstring citing §6 Lemma 8/9 would be a small optional improvement.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site Roth/MainLemma.lean:612; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:569; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the substantive ingredient, `Roth.card_filter_weight_le` (Lemma 8), is assessed under its own entry (BORDERLINE-needs-human).

## Evidence
- `grep -rn mul_card_filter_weight_le_aux Roth/`: definition Roth/MainLemma.lean:569, single use Roth/MainLemma.lean:612.
- Read the body (Roth/MainLemma.lean:569–579), the caller (l.581–616) and the statement of `card_filter_weight_le` (Roth/Lattice.lean:202–204); located `box` (Roth/Box.lean:47) and `weight` (Roth/Box.lean:71) by grep.
- Earlier reports consulted: `Roth.card_filter_weight_le.md` (mathlib absence, necessity of hr), `Roth.exists_mem_RSet_le_index_aux.md` (format).
- Necessity of `hm` argued by hand (m = 0 counterexample with a = 1: left side 1, right side 1/2); no Lean runs and no evidence Lean files, as a private SKIP needs no weakening experiments and the project builds clean.
