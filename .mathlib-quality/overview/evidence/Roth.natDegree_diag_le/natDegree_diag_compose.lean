import Mathlib.RingTheory.Polynomial.Basic
import Roth.CoeffNorm

/-! Evidence for the `Roth.natDegree_diag_le` mathlibable assessment. -/

open MvPolynomial

namespace NatDegreeDiagEvidence

variable {σ R : Type*} [CommSemiring R]

/-- (1) `totalDegree ≤ ∑ degreeOf` is a composition of three mathlib lemmas
(`totalDegree_le_degrees_card`, `degreeOf_def`, `Multiset.sum_count_eq_card`). -/
theorem totalDegree_le_sum_degreeOf [Fintype σ] (P : MvPolynomial σ R) :
    P.totalDegree ≤ ∑ j, P.degreeOf j := by
  classical
  simpa [degreeOf_def] using P.totalDegree_le_degrees_card

/-- (2) The project statement, over any `CommSemiring R`, re-aimed at the mathlib term
`aeval (fun _ ↦ X)`: one call to `MvPolynomial.aeval_natDegree_le` with `n = 1`. -/
theorem natDegree_aeval_X_le [Fintype σ] (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) :
    (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).natDegree ≤ ∑ j, r j := by
  simpa using aeval_natDegree_le P
    ((totalDegree_le_sum_degreeOf P).trans (Finset.sum_le_sum fun j _ ↦ hP j)) _
    fun _ ↦ Polynomial.natDegree_X_le

/-- (3) The original `ℤ` statement is recovered from (2) by `rfl`-unfolding `Roth.diag`. -/
example [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) :
    (Roth.diag P).natDegree ≤ ∑ j, r j :=
  natDegree_aeval_X_le P hP

/-- (4) The sharper, `Fintype`-free form `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P`
is one call to `aeval_natDegree_le`. -/
example (P : MvPolynomial σ R) :
    (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).natDegree ≤ P.totalDegree := by
  simpa using aeval_natDegree_le P le_rfl _ fun _ ↦ Polynomial.natDegree_X_le

end NatDegreeDiagEvidence
