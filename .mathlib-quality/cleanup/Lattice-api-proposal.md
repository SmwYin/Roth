# Compiled proposal: `sqrt_one_sub_inv_lt` hypothesis

Closed proposal; **not applied**. Owner decision: preserve the paper/API formulation; the sole caller already has `2 ≤ m`, so this weakening has no current practical benefit. No pending approval remains.

Replace `hm : 2 ≤ m` by `hm : 1 ≤ m`. The following independent declaration compiled with native `lean_run_code` (`success: true`, `timed_out: false`, `diagnostics: []`) on 2026-10-16:

```lean
import Roth.Box
import Mathlib.Analysis.SpecialFunctions.Sqrt

theorem probe {m : ℕ} (hm : 1 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2 := by
  have hm' : (1 : ℝ) ≤ m := by exact_mod_cast hm
  have hsq : 4 * (m : ℝ) < lam ^ 2 := by
    nlinarith [Real.sqrt_nonneg (m : ℝ), Real.sq_sqrt (Nat.cast_nonneg m)]
  have hu : lam⁻¹ ^ 2 < 1 / m / 4 := by
    rw [inv_pow, div_div, ← one_div]
    exact one_div_lt_one_div_of_lt (by positivity) (by linarith)
  rw [Real.sqrt_lt' (by linarith [one_div_le_one_div_of_le zero_lt_one hm'])]
  nlinarith [sq_nonneg (lam⁻¹ ^ 2)]
```

Caller audit: `rg -n 'sqrt_one_sub_inv_lt' Roth` found only the declaration and one use in `Roth/Lattice.lean` inside `sum_inv_lt`: `(sqrt_one_sub_inv_lt hm hlam)`. There `hm : 2 ≤ m`; after this proposal it would need `(sqrt_one_sub_inv_lt (by lia) hlam)`. No cross-file uses were found. This is a concrete argument-type change requiring owner/user decision, with little immediate downstream benefit; current cleanup retains the original API.

The source proof of Lemma 8 discusses `m ≥ 2` in this step. Its stronger bound is useful for the following harmonic estimate; this standalone square-root comparison itself works at `m = 1`.
