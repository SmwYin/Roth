import Roth.Taylor

namespace MvPolynomial

section CommRing

variable {σ A : Type*} [CommRing A]

-- (1) project statement, project proof
example (α : σ → A) (P : MvPolynomial σ A) : taylor (fun j ↦ -α j) (taylor α P) = P := by
  simp [taylor_taylor]

-- (2) plain `simp` (without `taylor_taylor`) does not prove it
example (α : σ → A) (P : MvPolynomial σ A) : taylor (fun j ↦ -α j) (taylor α P) = P := by
  fail_if_success simp
  simp [taylor_taylor]

-- (3) Pi-negation form, definitionally the project statement
theorem taylor_neg_taylor' (α : σ → A) (P : MvPolynomial σ A) : taylor (-α) (taylor α P) = P :=
  taylor_neg_taylor α P

-- (4) the missing right inverse (surjectivity direction)
theorem taylor_taylor_neg (α : σ → A) (P : MvPolynomial σ A) : taylor α (taylor (-α) P) = P := by
  simpa using taylor_neg_taylor (-α) P

-- (5) packaging as an `AlgEquiv`, mirroring `Polynomial.taylorEquiv`
noncomputable def taylorEquiv (α : σ → A) : MvPolynomial σ A ≃ₐ[A] MvPolynomial σ A :=
  AlgEquiv.ofAlgHom (taylor α) (taylor (-α))
    (AlgHom.ext fun P ↦ taylor_taylor_neg α P) (AlgHom.ext fun P ↦ taylor_neg_taylor α P)

@[simp] theorem coe_taylorEquiv (α : σ → A) : (taylorEquiv α : _ → _) = taylor α := rfl

@[simp] theorem taylorEquiv_symm (α : σ → A) : (taylorEquiv α).symm = taylorEquiv (-α) := by
  ext P : 1
  rfl

-- (6) downstream project lemmas become AlgEquiv one-liners
example (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) :=
  (taylorEquiv α).injective
example (α : σ → A) : Function.Surjective (taylor α : MvPolynomial σ A → _) :=
  (taylorEquiv α).surjective
example (α : σ → A) (P : MvPolynomial σ A) : taylor α P = 0 ↔ P = 0 :=
  map_eq_zero_iff (taylorEquiv α) (taylorEquiv α).injective

end CommRing

section CommSemiring

variable {σ R : Type*} [CommSemiring R]

-- (7) semiring form with an additive-inverse hypothesis
-- (strictly more general, no mathlib precedent)
example (α β : σ → R) (h : β + α = 0) (P : MvPolynomial σ R) : taylor β (taylor α P) = P := by
  rw [taylor_taylor]
  exact (congrArg (taylor · P) h).trans (taylor_zero P)

end CommSemiring

end MvPolynomial
