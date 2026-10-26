import Roth.Taylor

namespace MvPolynomial
variable {σ R A : Type*} [CommSemiring R] [CommRing A]

-- 1. Does the current simp lemma fire on the Pi-zero form `taylor 0 P`?
--    Expected NO: `simp` makes no progress (the lemma is keyed on `fun _ ↦ 0`, not Pi `0`).
example (P : MvPolynomial σ R) : taylor 0 P = P := by
  fail_if_success simp
  exact taylor_zero P

-- 2. Preferred mathlib-style statement (Pi zero, matching Polynomial.taylor_zero), same proof.
theorem taylor_zero_pi (P : MvPolynomial σ R) : taylor 0 P = P := by
  simp [taylor, aeval_X_left_apply]

-- 3. Bundled companion, matching Polynomial.taylor_zero'.
theorem taylor_zero_pi' : taylor (0 : σ → R) = AlgHom.id R _ :=
  AlgHom.ext taylor_zero_pi

-- 4. Is taylor_zero used implicitly by simp in taylor_neg_taylor?
example (α : σ → A) (P : MvPolynomial σ A) :
    taylor (fun j ↦ -α j) (taylor α P) = P := by
--    Expected YES: without `taylor_zero`, simp leaves `taylor (fun j ↦ 0) P = P`.
  fail_if_success (simp [taylor_taylor, -taylor_zero]; done)
  simp [taylor_taylor]

end MvPolynomial
