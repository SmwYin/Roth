import Roth.GenWronskian
import Mathlib.Algebra.Polynomial.Derivation

/-! Evidence for `Roth.derivative_aeval`.
1. The multivariate chain rule for an arbitrary derivation `D : Derivation R A M`
   (multivariate analogue of mathlib's `Derivation.map_aeval`).
2. The project lemma, over any commutative semiring, as a corollary of 1 with
   `D = Polynomial.derivative'`.
3. The project proof itself works verbatim with `[CommSemiring R]` in place of `[Field K]`. -/

open MvPolynomial

-- 1. general chain rule
theorem Derivation.map_mvPolynomial_aeval {σ R A M : Type*} [Fintype σ] [CommSemiring R]
    [CommSemiring A] [Algebra R A] [AddCommMonoid M] [Module A M] [Module R M]
    [IsScalarTower R A M] (D : Derivation R A M) (f : σ → A) (P : MvPolynomial σ R) :
    D (aeval f P) = ∑ i, aeval f (pderiv i P) • D (f i) := by
  classical
  induction P using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq, Finset.sum_add_distrib, add_smul]
  | mul_X p j hp =>
    simp [hp, Finset.sum_add_distrib, add_smul, Finset.smul_sum, mul_smul, Pi.single_apply,
      apply_ite (aeval f), ite_smul]

-- 2. project lemma as a corollary, over a commutative semiring
example {σ R : Type*} [Fintype σ] [CommSemiring R] (γ : σ → Polynomial R)
    (P : MvPolynomial σ R) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) := by
  simpa [mul_comm] using Derivation.map_mvPolynomial_aeval Polynomial.derivative' γ P

-- 3. project proof under `CommSemiring`
example {σ R : Type*} [Fintype σ] [CommSemiring R] (γ : σ → Polynomial R)
    (P : MvPolynomial σ R) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) := by
  classical
  induction P using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq, Finset.sum_add_distrib, mul_add]
  | mul_X p j hp =>
    simp [hp, Finset.sum_add_distrib, ← Finset.mul_sum, add_mul, mul_assoc, mul_comm,
      Pi.single_apply, apply_ite (aeval γ)]

-- 4. the project statement is recovered verbatim
example {K σ : Type*} [Field K] [Fintype σ] (γ : σ → Polynomial K) (P : MvPolynomial σ K) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) :=
  Roth.derivative_aeval γ P
