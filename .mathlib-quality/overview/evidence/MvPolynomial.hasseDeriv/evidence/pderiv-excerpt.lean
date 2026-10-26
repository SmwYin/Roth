
noncomputable section

universe u v

namespace MvPolynomial

open Function Finsupp

variable {R : Type u} {σ : Type v} {a : R} {s : σ →₀ ℕ}

section PDeriv

variable [CommSemiring R]

/-- `pderiv i p` is the partial derivative of `p` with respect to `i` -/
def pderiv (i : σ) : Derivation R (MvPolynomial σ R) (MvPolynomial σ R) :=
  letI := Classical.decEq σ
  mkDerivation R <| Pi.single i 1

theorem pderiv_def [DecidableEq σ] (i : σ) : pderiv i = mkDerivation R (Pi.single i 1) := by
  unfold pderiv; congr!

@[simp]
theorem pderiv_monomial {i : σ} :
    pderiv i (monomial s a) = monomial (s - single i 1) (a * s i) := by
  classical
  simp only [pderiv_def, mkDerivation_monomial, Finsupp.smul_sum, smul_eq_mul, ← smul_mul_assoc,
    ← (monomial _).map_smul]
