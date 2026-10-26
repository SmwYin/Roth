import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Nat.Choose.Bounds
#check_failure MvPolynomial.hasseDeriv_rename
#check_failure MvPolynomial.hasseDeriv
#check @MvPolynomial.pderiv_rename
#check @MvPolynomial.rename_monomial
#check @MvPolynomial.coeff_rename_mapDomain
#check @Finsupp.prod_mapDomain_index_inj
#check @Finsupp.mapDomain_apply_of_injective
#check @Finsupp.mapDomain_tsub
#check @Finsupp.lsum_single
namespace AssessHasseRenameAbstract
open MvPolynomial
variable {σ τ R : Type*} [CommSemiring R]
theorem natural_monomial (f : σ → τ)
    (D : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (E : MvPolynomial τ R →ₗ[R] MvPolynomial τ R)
    (h : ∀ k a, E (monomial (k.mapDomain f) a) = rename f (D (monomial k a)))
    (P : MvPolynomial σ R) : E (rename f P) = rename f (D P) := by
  induction P using MvPolynomial.induction_on' with
  | monomial k a => simpa only [rename_monomial] using h k a
  | add p q hp hq => simp only [map_add, hp, hq]
#print axioms natural_monomial
end AssessHasseRenameAbstract
