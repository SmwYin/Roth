import Roth.Taylor
import Mathlib.Algebra.MvPolynomial.Monad

namespace MvPolynomial

variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]

-- (1) project proof is import-fragile: with Mathlib.Algebra.MvPolynomial.Monad imported,
-- simp rewrites `aeval` to `bind₁` (simp lemma `aeval_eq_bind₁`) and the project proof fails.
example (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    taylor (fun j ↦ f (α j)) (map f P) = map f (taylor α P) := by
  fail_if_success (simp [taylor, aeval_def, map_eval₂, Function.comp_def]; done)
  exact taylor_map f α P

-- (1b) robust proof via mathlib's map_bind₁
example (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    taylor (fun j ↦ f (α j)) (map f P) = map f (taylor α P) := by
  simp [taylor, map_bind₁]

-- (2) plain simp (without unfolding taylor) does not prove it
example (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    taylor (fun j ↦ f (α j)) (map f P) = map f (taylor α P) := by
  fail_if_success (simp; done)
  exact taylor_map f α P

-- (3) mathlib-only composition: taylor is bind₁ by rfl, then map_bind₁ + simp
example (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    map f (bind₁ (fun j ↦ X j + C (α j)) P) =
      bind₁ (fun j ↦ X j + C (f (α j))) (map f P) := by
  rw [map_bind₁]; simp

example (α : σ → R) (P : MvPolynomial σ R) :
    taylor α P = bind₁ (fun j ↦ X j + C (α j)) P := rfl

-- (4) mathlib-oriented restatement (matches Polynomial.map_taylor), simp-normal direction
@[simp] theorem map_taylor' (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    map f (taylor α P) = taylor (f ∘ α) (map f P) :=
  (taylor_map f α P).symm

-- (5) the simp-lemma (4) fires and closes the project form by itself
example (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    taylor (fun j ↦ f (α j)) (map f P) = map f (taylor α P) := by
  simp [Function.comp_def]

-- (6) bundled ring-hom companion
theorem map_comp_taylor (f : R →+* S) (α : σ → R) :
    (map f).comp (taylor α : MvPolynomial σ R →ₐ[R] MvPolynomial σ R).toRingHom =
      (taylor (f ∘ α) : MvPolynomial σ S →ₐ[S] MvPolynomial σ S).toRingHom.comp (map f) :=
  RingHom.ext fun P ↦ map_taylor' f α P

end MvPolynomial
