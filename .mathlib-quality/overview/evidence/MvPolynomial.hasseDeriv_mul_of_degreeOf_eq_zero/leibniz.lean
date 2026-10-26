import Roth.Taylor
import Mathlib.Data.ZMod.Basic

/-! Evidence for the `hasseDeriv_mul_of_degreeOf_eq_zero` overview report. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) `Δ_d P` recovered from the Taylor shift by `X` over `MvPolynomial σ R`. -/
theorem eval_X_coeff_taylor (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (taylor (X : σ → MvPolynomial σ R) (map C P)).coeff d = hasseDeriv d P := by
  rw [coeff_taylor, hasseDeriv_map, eval_map, eval₂_eta]

/-- (2) General Leibniz rule for multivariate Hasse derivatives
(multivariate `Polynomial.hasseDeriv_mul`). -/
theorem hasseDeriv_mul [DecidableEq σ] (d : σ →₀ ℕ) (f g : MvPolynomial σ R) :
    hasseDeriv d (f * g) =
      ∑ x ∈ Finset.antidiagonal d, hasseDeriv x.1 f * hasseDeriv x.2 g := by
  simp_rw [← eval_X_coeff_taylor, map_mul, coeff_mul]

/-- (3) Weakened hypothesis: only needs `Δ_a f = 0` for `0 ≠ a ≤ d`. -/
theorem hasseDeriv_mul_of_hasseDeriv_eq_zero {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ a ≤ d, a ≠ 0 → hasseDeriv a f = 0) :
    hasseDeriv d (f * g) = f * hasseDeriv d g := by
  classical
  rw [hasseDeriv_mul, Finset.sum_eq_single (0, d)]
  · simp
  · rintro ⟨a, b⟩ hab hne
    rw [Finset.mem_antidiagonal] at hab
    have ha : a ≠ 0 := by rintro rfl; simp_all
    simp [hf a (hab ▸ le_self_add) ha]
  · simp

/-- (4) The project statement as a corollary of (3). -/
theorem hasseDeriv_mul_of_degreeOf_eq_zero' {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ j ∈ d.support, degreeOf j f = 0) : hasseDeriv d (f * g) = f * hasseDeriv d g :=
  hasseDeriv_mul_of_hasseDeriv_eq_zero fun a had ha ↦ by
    obtain ⟨j, hj⟩ := Finsupp.support_nonempty_iff.2 ha
    exact hasseDeriv_eq_zero_of_degreeOf_lt <| by
      rw [hf j (Finsupp.support_mono had hj)]
      exact Nat.pos_of_ne_zero (Finsupp.mem_support_iff.1 hj)

/-- (5) Strictness: in characteristic 2, `X^2` commutes with `Δ_{e_0}` although
`degreeOf 0 (X^2) = 2 ≠ 0`. -/
example (g : MvPolynomial Unit (ZMod 2)) :
    hasseDeriv (Finsupp.single () 1) (X () ^ 2 * g) =
      X () ^ 2 * hasseDeriv (Finsupp.single () 1) g := by
  refine hasseDeriv_mul_of_hasseDeriv_eq_zero fun a had ha ↦ ?_
  have : a = Finsupp.single () 1 := by
    have h1 := had ()
    have h0 : a () ≠ 0 := fun h ↦ ha (Finsupp.ext fun v ↦ by cases v; simpa using h)
    refine Finsupp.ext fun v ↦ ?_
    cases v
    simp only [Finsupp.single_eq_same] at h1 ⊢
    change a () = 1
    omega
  subst this
  rw [X_pow_eq_monomial, hasseDeriv_monomial]
  simp [hasseCoeff]
  decide

end MvPolynomial
