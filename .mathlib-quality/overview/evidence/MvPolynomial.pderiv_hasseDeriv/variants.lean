import Roth.HasseDeriv

/-! Evidence for the overview assessment of `MvPolynomial.pderiv_hasseDeriv`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-! (1) Missing basic API, analogue of `Polynomial.hasseDeriv_one'`: `Δ_{e_j} = ∂_j`. -/
theorem hasseDeriv_single_one_apply (j : σ) (P : MvPolynomial σ R) :
    hasseDeriv (Finsupp.single j 1) P = pderiv j P := by
  simpa using factorial_smul_hasseDeriv_single j 1 P

/-! (1') The same, proved directly from coefficients (no dependence on `pderiv_hasseDeriv`, so it
can come first in an upstream file, as `Polynomial.hasseDeriv_one'` does). -/
example (j : σ) (P : MvPolynomial σ R) :
    hasseDeriv (Finsupp.single j 1) P = pderiv j P := by
  ext e
  simp [coeff_hasseDeriv, coeff_pderiv, hasseCoeff, Finsupp.prod_single_index, mul_comm]

/-! (2) `pderiv_hasseDeriv` recovered from (1) + `hasseDeriv_hasseDeriv` (the mathlib-style route,
as `Polynomial.factorial_smul_hasseDeriv` is downstream of `hasseDeriv_one`/`hasseDeriv_comp`). -/
example (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P := by
  classical
  rw [← hasseDeriv_single_one_apply, hasseDeriv_hasseDeriv, add_comm (Finsupp.single j 1) d]
  congr 2
  simp [hasseCoeff, Finsupp.prod_single_index, add_comm]

/-! (3) Operator form in the normal form of `Polynomial.hasseDeriv_comp` (`∘ₗ`, `ℕ`-smul). -/
example (j : σ) (d : σ →₀ ℕ) :
    (pderiv (R := R) j).toLinearMap ∘ₗ hasseDeriv d =
      (d j + 1) • hasseDeriv (d + Finsupp.single j 1) := by
  refine LinearMap.ext fun P ↦ ?_
  rw [LinearMap.comp_apply, LinearMap.smul_apply, Derivation.coeFn_coe,
    pderiv_hasseDeriv, Nat.cast_smul_eq_nsmul]

/-! (4) Not closed by the coefficient API alone. -/
example (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P := by
  ext e
  fail_if_success (simp [coeff_pderiv, coeff_hasseDeriv, hasseCoeff]; done)
  rw [pderiv_hasseDeriv]

end MvPolynomial
