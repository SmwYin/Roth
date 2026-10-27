import Roth.Index

/-! Evidence for `Roth.index_C_mul`. -/

open MvPolynomial

namespace Roth.Evidence

/-- (1) `hc : c ≠ 0` is necessary: with `c = 0`, `P = X true`, `α = 0`, `r = 1`, the left side
is `index 0 = 0` while the right side is `1`. -/
example : index (C (0 : ℝ) * (X true : MvPolynomial Bool ℝ)) (fun _ ↦ 0) (fun _ ↦ 1) ≠
    index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) := by
  have h1 : index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 1 := by
    rw [index, taylor_zero, support_X]
    simp [weight, Finsupp.single_apply]
  rw [h1, C_0, zero_mul]
  simp [index]

/-- (2) The `•` form, equally short (Theta.lean's caller has an integer cast, not `C`). -/
example {σ : Type*} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ)
    (r : σ → ℕ) : index (c • P) α r = index P α r := by
  rw [index, index, map_smul, support_smul_eq hc]

/-- (3) Right-multiplication variant follows by `mul_comm`. -/
example {σ : Type*} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ)
    (r : σ → ℕ) : index (P * C c) α r = index P α r := by
  rw [mul_comm]; exact index_C_mul hc P α r

/-- (4) The current proof, reproduced (composition of `map_mul`, `taylor_C`,
`smul_eq_C_mul`, `support_smul_eq`). -/
example {σ : Type*} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ)
    (r : σ → ℕ) : index (C c * P) α r = index P α r := by
  rw [index, index, map_mul, MvPolynomial.taylor_C, ← smul_eq_C_mul, support_smul_eq hc]

/-- (5) Mathlib gap check: the weighted-order analogue `weightedOrder (a • f) = weightedOrder f`
for `a ≠ 0` over a domain is not stated in mathlib (only `le_weightedOrder_smul`), but it is a
two-step composition of `weightedOrder_mul` and `weightedOrder_monomial_of_ne_zero`. -/
example {σ : Type*} (w : σ → ℕ) {a : ℝ} (ha : a ≠ 0) (f : MvPowerSeries σ ℝ) :
    (a • f).weightedOrder w = f.weightedOrder w := by
  rw [MvPowerSeries.smul_eq_C_mul, MvPowerSeries.weightedOrder_mul,
    ← MvPowerSeries.monomial_zero_eq_C_apply,
    MvPowerSeries.weightedOrder_monomial_of_ne_zero w ha]
  simp

end Roth.Evidence
