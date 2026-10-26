import Roth.Taylor
#check @MvPolynomial.hasseDeriv_C
#print MvPolynomial.hasseDeriv_C
#print axioms MvPolynomial.hasseDeriv_C
namespace HasseCTargetProbe
open MvPolynomial
variable {σ R : Type*} [CommSemiring R]
theorem original {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by
  rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)]
  simp
theorem unfolded {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by
  have hz : hasseCoeff d 0 = 0 := (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)
  simp [hasseDeriv, C_apply, hz]
theorem caller (α : σ → R) {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) :
    (taylor α (monomial 0 a)).coeff d = eval α (hasseDeriv d (monomial 0 a)) := by
  simp [← C_apply, hasseDeriv_C hd, hd.symm]
theorem caller_inline (α : σ → R) {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) :
    (taylor α (monomial 0 a)).coeff d = eval α (hasseDeriv d (monomial 0 a)) := by
  have hz : hasseCoeff d 0 = 0 := (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)
  simp [← C_apply, hasseDeriv, C_apply, hz, hd.symm]
#print axioms original
#print axioms unfolded
#print axioms caller
#print axioms caller_inline
end HasseCTargetProbe
