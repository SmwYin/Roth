import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Nat.Choose.Bounds
#check_failure MvPolynomial.hasseDeriv_map
#check_failure MvPolynomial.hasseDeriv
#check @Polynomial.hasseDeriv_map
#check @MvPolynomial.pderiv_map
#check @Finsupp.mapDomain_mapRange
#check @Finsupp.mapRange_smul
#check @MvPolynomial.coeff_map
#check @MvPolynomial.coeff_addMonoidAlgebraMap
namespace AssessHasseMapIsolated
variable {R S : Type*} [Semiring R] [Semiring S]
theorem cast_preserved (f : R →+* S) (n : ℕ) : f (n : R) = (n : S) := map_natCast f n
theorem cast_weight (f : R →+* S) (n : ℕ) (a : R) :
    f ((n : R) * a) = (n : S) * f a := by
  rw [map_mul, map_natCast]
theorem additive_weight (f : R →+ S) (n : ℕ) (a : R) :
    f ((n : R) * a) = (n : S) * f a := by
  simpa only [nsmul_eq_mul] using f.map_nsmul n a
end AssessHasseMapIsolated
namespace AssessHasseMapGeneric
open MvPolynomial
variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]
theorem natural (s : (σ →₀ ℕ) → (σ →₀ ℕ)) (w : (σ →₀ ℕ) → ℕ)
    (DR : MvPolynomial σ R → MvPolynomial σ R) (DS : MvPolynomial σ S → MvPolynomial σ S)
    (hR : ∀ P e, (DR P).coeff e = (w e : R) * P.coeff (s e))
    (hS : ∀ P e, (DS P).coeff e = (w e : S) * P.coeff (s e))
    (f : R →+ S) (P : MvPolynomial σ R) :
    DS (AddMonoidAlgebra.map f P) = AddMonoidAlgebra.map f (DR P) := by
  apply MvPolynomial.ext
  intro e
  simp only [hR, hS, coeff_addMonoidAlgebraMap, ← nsmul_eq_mul, map_nsmul]
theorem zero_not_ringhom : (0 : ℕ →+ ℕ) 1 ≠ 1 := by decide
#print axioms natural
#print axioms zero_not_ringhom
#print axioms AssessHasseMapIsolated.cast_preserved
#print axioms AssessHasseMapIsolated.cast_weight
#print axioms AssessHasseMapIsolated.additive_weight
end AssessHasseMapGeneric
