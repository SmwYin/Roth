---
decl: Roth.theta_lt_eta_of_sq_log_bound_aux
file: Roth/MainLemma.lean
line: 671
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private adapter restating Lemma 7 (Roth.Θ_lt) in Lemma 9's hypothesis shape (m with NeZero, delta*m le 1, ratio as r_j/delta le r_i, delta^2 log q_1 bound) with conclusion via eta; single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:724 (exists_auxiliary_polynomial_with_index_gap_aux); optionally add a docstring citing Lemma 7 / eqs. (31)-(33); no other change.
---

# Roth.theta_lt_eta_of_sq_log_bound_aux

## Inventory entry

### `theorem Roth.theta_lt_eta_of_sq_log_bound_aux`
- **Type**: `∀ {m : ℕ} [NeZero m] {δ : ℝ}, 0 ≤ δ → δ * (m : ℝ) ≤ 1 → ∀ {r q : Fin m → ℕ}, 3 ≤ r (Fin.rev 0) → (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) → 2 * (m : ℝ) + 1 ≤ δ ^ 2 * Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < eta δ m`
- **What**: For m ≥ 1, 0 ≤ δ with δm ≤ 1, degrees r_1, …, r_m with last degree r_m ≥ 3 and the chain condition r_{j+1}/δ ≤ r_j (paper's (31)), denominators q with 2m + 1 ≤ δ²·log q_1 (the α/A-free part of (32)) and r_1 log q_1 ≤ r_j log q_j (33), the quantity Θ_m(q_1^{δ r_1}; q; r) is strictly below η = 10^m δ^{(1/2)^m}. This is Lemma 7 of the source (`Roth.Θ_lt`) repackaged in the hypothesis form used by Lemma 9 (`main_lemma`).
- **How**: Writes m = n + 1 (`Nat.exists_eq_succ_of_ne_zero`). Derives δ > 0 from hL (if δ = 0 the right side of hL is 0 < 2m+1). Converts δ²·log q_1 ≥ 2m+1 together with δm ≤ 1 into m(2m+1)/δ ≤ log q_1 by cancelling δ² (`mul_le_mul_iff_of_pos_right`, `sq_pos_of_pos`, `mul_le_mul_of_nonneg_right`, then `field_simp`/`ring`). Converts the ratio hypothesis r_j/δ ≤ r_i into r_{i+1} ≤ δ r_i via `div_le_iff₀`, the last-degree bound via `Fin.rev_zero`/`Nat.cast_le`, and concludes by `Roth.Θ_lt` (Roth/Theta.lean:962), unfolding `eta` by `simpa [eta]`.
- **Hypotheses**: `hδ0` (gives δ > 0 together with hL); `hδm` (used to pass from δ² log q_1 ≥ 2m+1 to the Θ_lt log bound); `hrlast` (Θ_lt's last-degree bound); `hratio` (Θ_lt's chain condition after `div_le_iff₀`); `hL` (log bound and δ > 0); `hqr` (passed verbatim). All used.
- **Uses from project**: `Roth.Θ` (Roth/Theta.lean:68), `Roth.eta` (Roth/MainLemma.lean:66), `Roth.Θ_lt` (Roth/Theta.lean:962). Mathlib names used: `Nat.exists_eq_succ_of_ne_zero`, `NeZero.ne`, `mul_le_mul_iff_of_pos_right`, `sq_pos_of_pos`, `mul_le_mul_of_nonneg_right`, `one_mul`, `div_le_iff₀`, `Fin.rev_zero`, `Nat.cast_le`, `Nat.cast_ofNat`, `Real.log`.
- **Used by**: Roth/MainLemma.lean:724 `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (private, l.692), which feeds `Roth.main_lemma` (l.734). `grep -rn theta_lt_eta_of_sq_log_bound_aux Roth/` gives only l.671 (definition) and l.724 (use).
- **Visibility**: private
- **Lines**: 671–689, proof length 13 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. It is also the only call site of the public `Roth.Θ_lt` (grep: Roth/MainLemma.lean:687), so the pair could alternatively be merged by stating `Θ_lt` directly in this form; the current split keeps `Θ_lt` in the induction-friendly `Fin (n+1)` form matching the paper's Lemma 7, which is reasonable.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:724 in `exists_auxiliary_polynomial_with_index_gap_aux`.
- Wrapper of 1–2 mathlib calls? No. It is a wrapper of one project lemma (`Roth.Θ_lt`) plus a 13-line hypothesis translation (m = n+1 reindexing, δ > 0, δ²-cancellation for the log bound, ratio rewriting, `eta` unfolding).
- Does mathlib have it? No. The statement concerns the project-defined `Θ` (supremum of indices over `RSet`) and `eta`; mathlib has no index/Θ machinery for Roth's theorem. A Roth-specific numerical specialisation cannot plausibly be in mathlib.
- Too specific (inline?)? Single call site. Inlining into `exists_auxiliary_polynomial_with_index_gap_aux` (already ~32 lines, which itself already does an m = m'+1 reindex and a δ > 0 derivation) would lengthen it to ~45 lines and mix the Θ-bound arithmetic with the index-gap assembly; keeping it separate keeps the caller's final `linarith` clean. Keep. Minor duplication: the δ > 0 derivation from the log bound appears here (l.680–681) and in the caller (l.708–709).
- Well-chosen statement? Yes: hypotheses are phrased exactly as the caller has them (`hδm` after `le_div_iff₀`, `h31b`, the weakened `h32'`, `h33`), so the call site is a direct application. A docstring citing Lemma 7 would help.
- Conclusion: `KEEP`. Action: keep as private helper of Roth/MainLemma.lean:724; optionally add a docstring.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:671; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the underlying mathematical content (Lemma 7, `Roth.Θ_lt`) is assessed under its own entry (BORDERLINE-needs-human, keep in project).

## Evidence
- `grep -rn theta_lt_eta_of_sq_log_bound_aux Roth/`: definition Roth/MainLemma.lean:671, single use Roth/MainLemma.lean:724.
- `grep -rn Θ_lt Roth/`: `Θ_lt` is used only at Roth/MainLemma.lean:687 (inside this lemma) and mentioned in the Roth/Theta.lean module docstring.
- Read the body (Roth/MainLemma.lean:671–689), `Θ_lt` statement (Roth/Theta.lean:962–966), `Θ` (Roth/Theta.lean:68), `eta` (Roth/MainLemma.lean:66), and the caller (l.692–725).
- Earlier reports consulted: `Roth.Θ_lt.md`, `Roth.exists_auxiliary_polynomial_of_log_bound_aux.md`.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
