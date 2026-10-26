import Roth.Index

/-! Isolated caller migration experiment; production sources are unchanged. -/
namespace Roth.ZeroApplyCallerAssessment
open MvPolynomial
variable {σ : Type*} [Fintype σ]
theorem index_eq_zero_replacement {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) :
    index P α r = 0 ↔ eval α P ≠ 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ (index_nonneg P α r).antisymm' ?_⟩
  · obtain ⟨d, hd, hdw⟩ := exists_weight_eq_index hP α r
    rw [h, weight_eq_zero_iff hr] at hdw
    subst hdw
    simpa only [hasseDeriv_zero, LinearMap.id_apply] using hd
  · simpa using index_le_weight (r := r) (d := 0)
      (by simpa only [hasseDeriv_zero, LinearMap.id_apply] using h)
#print axioms index_eq_zero_replacement
end Roth.ZeroApplyCallerAssessment
