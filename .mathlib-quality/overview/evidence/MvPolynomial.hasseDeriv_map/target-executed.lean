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
    hasseDeriv d (AddMonoidAlgebra.map f P) = AddMonoidAlgebra.map f (hasseDeriv d P) := by
  apply MvPolynomial.ext
  intro e
  simp only [coeff_hasseDeriv, coeff_addMonoidAlgebraMap, ← nsmul_eq_mul, map_nsmul]
theorem abstract (s : (σ →₀ ℕ) → (σ →₀ ℕ)) (w : (σ →₀ ℕ) → ℕ)
    (DR : MvPolynomial σ R → MvPolynomial σ R) (DS : MvPolynomial σ S → MvPolynomial σ S)
    (hR : ∀ P e, (DR P).coeff e = (w e : R) * P.coeff (s e))
    (hS : ∀ P e, (DS P).coeff e = (w e : S) * P.coeff (s e))
    (f : R →+ S) (P : MvPolynomial σ R) :
    DS (AddMonoidAlgebra.map f P) = AddMonoidAlgebra.map f (DR P) := by
  apply MvPolynomial.ext
  intro e
  simp only [hR, hS, coeff_addMonoidAlgebraMap, ← nsmul_eq_mul, map_nsmul]
#check @MvPolynomial.coeff_addMonoidAlgebraMap
#check @AddMonoidHom.map_nsmul
#print axioms additive
#print axioms abstract
end AssessHasseMapAdditive

namespace AssessHasseMapShape
open MvPolynomial
variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]
theorem function_square (f : R →+* S) (d : σ →₀ ℕ) :
    (fun P : MvPolynomial σ R ↦ hasseDeriv d (map f P)) =
      (fun P ↦ map f (hasseDeriv d P)) := by
  funext P
  exact HasseMapAssessment.coefficient_replay f d P
theorem explicit_order (d : σ →₀ ℕ) (P : MvPolynomial σ R) (f : R →+* S) :
    hasseDeriv d (map f P) = map f (hasseDeriv d P) := HasseMapAssessment.coefficient_replay f d P
#print axioms function_square
#print axioms explicit_order
end AssessHasseMapShape
namespace AssessHasseMapWeak
variable {σ R S : Type*} [Semiring R] [Semiring S]
#check_failure (MvPolynomial.hasseDeriv (R := R) (σ := σ))
#check_failure (fun (f : R →+* S) (P : MvPolynomial σ R) ↦ MvPolynomial.map f P)
end AssessHasseMapWeak

namespace AssessHasseMapCallers
open MvPolynomial
variable {σ R S T : Type*} [CommSemiring R] [CommSemiring S]
theorem observe (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R)
    (H : MvPolynomial σ S → T) : H (hasseDeriv d (map f P)) = H (map f (hasseDeriv d P)) :=
  congrArg H (HasseMapAssessment.coefficient_replay f d P)
theorem twice (f : R →+* S) (d k : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv k (map f P)) = map f (hasseDeriv d (hasseDeriv k P)) := by
  rw [HasseMapAssessment.coefficient_replay, HasseMapAssessment.coefficient_replay]
#print axioms observe
#print axioms twice
end AssessHasseMapCallers
