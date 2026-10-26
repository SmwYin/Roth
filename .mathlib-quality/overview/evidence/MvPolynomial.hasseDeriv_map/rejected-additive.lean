import Roth.Taylor

/-! Current declaration assessment experiments; production sources are unchanged. -/
namespace HasseMapAssessment
open MvPolynomial
variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]
#check @MvPolynomial.hasseDeriv_map
#print axioms MvPolynomial.hasseDeriv_map
theorem coefficient_replay (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (map f P) = map f (hasseDeriv d P) := by
  apply MvPolynomial.ext
  intro e
  simp only [coeff_hasseDeriv, coeff_map, map_mul, map_natCast]
#print axioms coefficient_replay
end HasseMapAssessment

namespace AssessHasseMapAdditive
open MvPolynomial
variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]
theorem additive (f : R →+ S) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (P.map f) = (hasseDeriv d P).map f := by
  apply MvPolynomial.ext
  intro e
  simp only [coeff_hasseDeriv, coeff_addMonoidAlgebraMap, ← nsmul_eq_mul, map_nsmul]
theorem abstract (s : (σ →₀ ℕ) → (σ →₀ ℕ)) (w : (σ →₀ ℕ) → ℕ)
    (DR : MvPolynomial σ R → MvPolynomial σ R) (DS : MvPolynomial σ S → MvPolynomial σ S)
    (hR : ∀ P e, (DR P).coeff e = (w e : R) * P.coeff (s e))
    (hS : ∀ P e, (DS P).coeff e = (w e : S) * P.coeff (s e))
    (f : R →+ S) (P : MvPolynomial σ R) : DS (P.map f) = (DR P).map f := by
  apply MvPolynomial.ext
  intro e
  simp only [hR, hS, coeff_addMonoidAlgebraMap, ← nsmul_eq_mul, map_nsmul]
#check @MvPolynomial.coeff_addMonoidAlgebraMap
#check @AddMonoidHom.map_nsmul
#print axioms additive
#print axioms abstract
end AssessHasseMapAdditive
