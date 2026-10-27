import Roth.Index

/-! Evidence for the `/overview` assessment of `Roth.index_unique`. -/

open MvPolynomial

namespace Roth

variable {σ : Type*} [Fintype σ]

/-! (1) `hP : P ≠ 0` is superfluous: for `P = 0` both sides are `0`
(`index 0 = sInf ∅ = 0`, `Polynomial.rootMultiplicity_zero`). -/
theorem index_unique_noHP [Unique σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r =
      (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default := by
  rcases eq_or_ne P 0 with rfl | hP
  · simp [index]
  · exact index_unique hP α r

/-! (2) The mathlib building block: root multiplicity is the trailing degree of the
translate `p(X + t)` (= `Polynomial.taylor t p`). -/
example (p : Polynomial ℝ) (t : ℝ) :
    p.rootMultiplicity t = (Polynomial.taylor t p).natTrailingDegree := by
  rw [Polynomial.rootMultiplicity_eq_natTrailingDegree, Polynomial.taylor_apply]

/-! (3) No positivity of `r` is needed: the `r default = 0` case is covered by the
statement itself (both sides `0`). -/
example [Unique σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) :
    index P α (fun _ ↦ 0) = 0 := by
  rw [index_unique_noHP]; simp

end Roth
