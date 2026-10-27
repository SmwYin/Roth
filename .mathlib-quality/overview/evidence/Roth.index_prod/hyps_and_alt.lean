import Roth.Index
import Mathlib.Data.ENat.BigOperators

/-! Evidence for `Roth.index_prod`. -/

open MvPolynomial

namespace Roth.Evidence

/-- (1) `hf` is necessary: with `s = univ : Finset Bool`, `f false = 0`, `f true = X true`,
`α = 0`, `r = 1`, the left side is `index 0 = 0` while the right side is `0 + 1 = 1`. -/
example : index (∏ i : Bool, (if i then X true else 0 : MvPolynomial Bool ℝ))
      (fun _ ↦ 0) (fun _ ↦ 1) ≠
    ∑ i : Bool, index (if i then X true else 0 : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) := by
  have h1 : index (X true : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 1 := by
    rw [index, taylor_zero, support_X]
    simp [weight, Finsupp.single_apply]
  have h0 : index (0 : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 0 := by simp [index]
  simp [h0, h1]

/-- (2) Induction-free alternative proof through `MvPowerSeries.weightedOrder_prod`. -/
example {σ : Type*} [Fintype σ] {ι : Type*} (s : Finset ι) {f : ι → MvPolynomial σ ℝ}
    (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r := by
  rw [index_eq_weightedOrder_div (Finset.prod_ne_zero_iff.2 hf) hr, map_prod,
    ← MvPolynomial.coeToMvPowerSeries.ringHom_apply, map_prod,
    MvPowerSeries.weightedOrder_prod,
    ENat.toNat_sum fun i hi ↦ by simp [hf i hi], Nat.cast_sum, Finset.sum_div]
  exact Finset.sum_congr rfl fun i hi ↦ (index_eq_weightedOrder_div (hf i hi) hr α).symm

end Roth.Evidence
