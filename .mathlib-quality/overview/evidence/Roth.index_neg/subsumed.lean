import Roth.Index

open MvPolynomial

/-- `index_neg` is the `c = -1` case of `Roth.index_C_mul`. -/
example {σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    Roth.index (-P) α r = Roth.index P α r := by
  rw [show -P = C (-1) * P by simp]
  exact Roth.index_C_mul (by norm_num) P α r

/-- Direct proof, as in the project. -/
example {σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    Roth.index (-P) α r = Roth.index P α r := by
  simp [Roth.index, support_neg]
