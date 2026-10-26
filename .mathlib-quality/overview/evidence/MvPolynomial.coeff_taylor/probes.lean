import Roth.Taylor
import Mathlib.Algebra.Polynomial.Taylor

/-! Evidence for the /overview mathlibable assessment of `MvPolynomial.coeff_taylor`. -/

open MvPolynomial

-- (1) Weakening `[CommSemiring R]` to `[Semiring R]` is impossible: `MvPolynomial σ R` itself
-- does not elaborate (expected: `#check_failure` succeeds, i.e. an info/failure message).
section
variable {R : Type} [Semiring R]
#check_failure (MvPolynomial ℕ R)
end

-- (2) The statement is already universe-polymorphic in `σ` and works for any `σ`, `α`.
example {σ : Type 3} {R : Type} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) : (taylor α P).coeff d = eval α (hasseDeriv d P) :=
  coeff_taylor α d P

-- (3) Composition check: unfolding to mathlib primitives (`aeval`, `coeff_sum`,
-- `coeff_monomial`) plus `hasseDeriv_apply` and closing with `simp` fails (simp makes
-- progress but leaves a goal); the statement is a
-- genuine theorem (binomial expansion per variable), not a ≤3-call composition.
example {σ R : Type} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (taylor α P).coeff d = eval α (hasseDeriv d P) := by
  fail_if_success (simp [taylor_apply, hasseDeriv_apply, coeff_sum, coeff_monomial, aeval_def,
    eval₂_eq, map_sum]; done)
  exact coeff_taylor α d P

-- (4) Univariate specialisation sanity check: mathlib's `Polynomial.taylor_coeff` is the
-- one-variable analogue (stated over `Semiring`, which `MvPolynomial` cannot reach).
#check @Polynomial.taylor_coeff
