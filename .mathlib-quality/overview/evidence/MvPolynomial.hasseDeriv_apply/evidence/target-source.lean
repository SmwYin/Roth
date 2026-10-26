-/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- The binomial factor `∏ j, (k j).choose (d j)` (a product over the support of `d`). -/
def hasseCoeff (d k : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose

/-- The multivariate Hasse derivative `Δ_d`: the `R`-linear map sending `monomial k a` to
`monomial (k - d) (hasseCoeff d k * a)` (see `hasseDeriv_monomial`). The coefficient
`hasseCoeff d k` vanishes unless `d ≤ k`, so the truncated subtraction `k - d` is harmless.

Source: §1, definition of `Δ_i` on monomials. -/
noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

/-- `Δ_d (a X^k) = hasseCoeff d k * a X^(k - d)`.

Source: §1, definition of `Δ_i` on monomials. -/
@[simp]
theorem hasseDeriv_monomial (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by
  simp [hasseDeriv]

/-- Expansion of `Δ_d P` as a sum over the support of `P`.

Source: §1, definition of `Δ_i` on monomials. -/
theorem hasseDeriv_apply (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  simp [hasseDeriv, sum_def]
