import Roth.Taylor
import Mathlib.Algebra.MvPolynomial.Monad

namespace MvPolynomial

variable {σ τ R : Type*} [CommSemiring R]

-- (1) project proof is import-fragile: with Mathlib.Algebra.MvPolynomial.Monad imported,
-- simp rewrites `aeval` to `bind₁` (simp lemma `aeval_eq_bind₁`) and the project proof fails.
example (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by
  fail_if_success (simp [taylor, rename_eq_aeval, comp_aeval_apply]; done)
  exact taylor_rename f α P

-- (1b) robust one-line proof via mathlib's bind₁_rename / rename_bind₁
example (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by
  simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]

-- (2) plain simp (without unfolding taylor) does not prove it
example (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by
  fail_if_success (simp; done)
  exact taylor_rename f α P

-- (3) mathlib-only composition on the unfolded (bind₁) form
example (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    bind₁ (fun j ↦ X j + C (α j)) (rename f P) =
      rename f (bind₁ (fun j ↦ X j + C (α (f j))) P) := by
  rw [bind₁_rename, rename_bind₁]; simp [Function.comp_def]

-- (3b) alternative robust proof through bind₁
example (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by
  change bind₁ _ (rename f P) = rename f (bind₁ _ P)
  rw [bind₁_rename, rename_bind₁]; simp [Function.comp_def]

-- (4) mathlib orientation (rename outermost on LHS, like map_taylor / rename_bind₁)
theorem rename_taylor' (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    rename f (taylor (α ∘ f) P) = taylor α (rename f P) :=
  (taylor_rename f α P).symm

-- (5) bundled AlgHom form
theorem taylor_comp_rename (f : σ → τ) (α : τ → R) :
    (taylor α).comp (rename f) = (rename f).comp (taylor (α ∘ f)) :=
  AlgHom.ext fun P ↦ taylor_rename f α P

-- (6) no CommRing / injectivity / Fintype needed: the statement holds for any f
example (α : ℕ → R) (P : MvPolynomial (Fin 3) R) :
    taylor α (rename (fun _ ↦ 0) P) = rename (fun _ ↦ 0) (taylor (α ∘ fun _ ↦ 0) P) :=
  taylor_rename _ α P

end MvPolynomial
