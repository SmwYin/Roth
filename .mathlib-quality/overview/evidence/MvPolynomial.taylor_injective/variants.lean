import Roth.Taylor

namespace MvPolynomial

section CommRing

variable {σ A : Type*} [CommRing A]

-- (1) project statement, project proof
example (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) :=
  Function.LeftInverse.injective (taylor_neg_taylor α)

-- (2) Pi-negation spelling of the left inverse gives the same proof
example (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) :=
  Function.LeftInverse.injective (g := taylor (-α)) (taylor_neg_taylor α)

-- (3) via the bundled `AlgEquiv` proposed for `taylor_neg_taylor`
-- (mirrors `Polynomial.taylorEquiv`)
theorem taylor_taylor_neg (α : σ → A) (P : MvPolynomial σ A) : taylor α (taylor (-α) P) = P := by
  simpa using taylor_neg_taylor (-α) P

noncomputable def taylorEquiv (α : σ → A) : MvPolynomial σ A ≃ₐ[A] MvPolynomial σ A :=
  AlgEquiv.ofAlgHom (taylor α) (taylor (-α))
    (AlgHom.ext fun P ↦ taylor_taylor_neg α P) (AlgHom.ext fun P ↦ taylor_neg_taylor α P)

example (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) :=
  (taylorEquiv α).injective

-- (4) the companion `taylor_inj` (mathlib univariate `Polynomial.taylor_inj`, simp)
example (α : σ → A) {P Q : MvPolynomial σ A} : taylor α P = taylor α Q ↔ P = Q :=
  (taylor_injective α).eq_iff

end CommRing

-- (5) `CommRing` cannot be weakened to `CommSemiring`: over `ℕ∞`, translation by `⊤`
-- identifies `X` and `X + 1`.
example : ¬ Function.Injective (taylor (fun _ : Unit ↦ (⊤ : ℕ∞)) : MvPolynomial Unit ℕ∞ → _) := by
  intro h
  have key : taylor (fun _ : Unit ↦ (⊤ : ℕ∞)) (X ()) =
      taylor (fun _ : Unit ↦ (⊤ : ℕ∞)) (X () + C 1) := by
    rw [map_add, taylor_X, taylor_C, add_assoc, ← C_add, top_add]
  have := congrArg constantCoeff (h key)
  simp at this

end MvPolynomial
