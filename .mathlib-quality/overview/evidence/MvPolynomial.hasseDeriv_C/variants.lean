import Roth.HasseDeriv

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- Generalisation: `Δ_d` kills every monomial `X^k` with `d ≰ k`. -/
theorem hasseDeriv_monomial_of_not_le {d k : σ →₀ ℕ} (h : ¬d ≤ k) (a : R) :
    hasseDeriv d (monomial k a) = 0 := by
  simp [(hasseCoeff_eq_zero_iff d k).2 h]

/-- `hasseDeriv_C` as a one-line corollary of the generalisation. -/
example {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 :=
  hasseDeriv_monomial_of_not_le (by simpa using hd) a

/-- The pointwise-alternative proof via the coefficient formula. -/
example {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by
  classical
  ext e
  have he : (0 : σ →₀ ℕ) ≠ e + d := fun h => hd (add_eq_zero.1 h.symm).2
  simp [coeff_hasseDeriv, coeff_C, he]

/-- Mathlib-analogue companion: `hasseDeriv_apply_one`. -/
example {d : σ →₀ ℕ} (hd : d ≠ 0) : hasseDeriv d (1 : MvPolynomial σ R) = 0 := by
  rw [← C_1, hasseDeriv_C hd]

/-- The hypothesis `d ≠ 0` is necessary: `Δ_0 (C 1) = C 1 ≠ 0` over `ℤ`. -/
example : ¬ ∀ (d : Unit →₀ ℕ) (a : ℤ), hasseDeriv d (C a) = (0 : MvPolynomial Unit ℤ) := by
  intro h
  have := h 0 1
  simp at this

end MvPolynomial
