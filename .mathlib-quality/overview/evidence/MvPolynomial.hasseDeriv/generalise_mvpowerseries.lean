import Roth.HasseDeriv
import Mathlib.RingTheory.MvPowerSeries.Basic

/-! Evidence for `MvPolynomial.hasseDeriv`:
1. A coefficientwise multivariate Hasse derivative on `MvPowerSeries σ R` elaborates over a
   plain `Semiring R` (no commutativity), and agrees with `MvPolynomial.hasseDeriv` under the
   coercion `MvPolynomial σ R → MvPowerSeries σ R` (for `CommSemiring R`).
2. `MvPolynomial.hasseDeriv` restated with the coefficient spelled `Finsupp.choose k d`
   (top index first) is definitionally the project definition. -/

namespace Finsupp
variable {σ : Type*}
/-- Multi-index binomial coefficient `binom(k, d)`. -/
def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
end Finsupp

namespace MvPowerSeries

variable {σ R : Type*} [Semiring R]

/-- Coefficientwise multivariate Hasse derivative on power series:
`[X^e] Δ_d f = binom(e + d, d) * [X^(e + d)] f`. Only needs `Semiring R`. -/
noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPowerSeries σ R →ₗ[R] MvPowerSeries σ R where
  toFun f e := ((e + d).choose d : R) * f (e + d)
  map_add' _ _ := funext fun _ ↦ mul_add _ _ _
  map_smul' c _ := funext fun _ ↦ (Nat.cast_commute _ c).left_comm _

theorem coeff_hasseDeriv (d e : σ →₀ ℕ) (f : MvPowerSeries σ R) :
    coeff e (hasseDeriv d f) = ((e + d).choose d : R) * coeff (e + d) f := rfl

end MvPowerSeries

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- The project's `hasseDeriv` is the restriction of the power-series version. -/
theorem coe_hasseDeriv (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    ((hasseDeriv d P : MvPolynomial σ R) : MvPowerSeries σ R) =
      MvPowerSeries.hasseDeriv d (P : MvPowerSeries σ R) := by
  ext e
  rw [coeff_coe, coeff_hasseDeriv, MvPowerSeries.coeff_hasseDeriv, coeff_coe]
  rfl

/-- Restatement using `Finsupp.choose` (top index first); definitionally the same map. -/
noncomputable def hasseDeriv' (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (k.choose d : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

example (d : σ →₀ ℕ) : hasseDeriv' (R := R) d = hasseDeriv d := rfl

end MvPolynomial
