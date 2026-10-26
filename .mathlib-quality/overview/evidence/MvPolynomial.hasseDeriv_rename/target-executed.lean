import Roth.Taylor

/-! Injective variable-renaming assessment experiments. -/
#check @MvPolynomial.hasseDeriv_rename
#print axioms MvPolynomial.hasseDeriv_rename
namespace AssessHasseRename
open MvPolynomial
variable {σ τ R : Type*} [CommSemiring R]
theorem replay {f : σ → τ} (hf : Function.Injective f) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) :
    hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    simp only [rename_monomial, hasseDeriv_monomial, hasseCoeff,
      Finsupp.prod_mapDomain_index_inj hf, Finsupp.mapDomain_apply_of_injective hf,
      ← Finsupp.mapDomain_tsub hf]
  | add p q hp hq => simp only [map_add, hp, hq]
theorem square {f : σ → τ} (hf : Function.Injective f) (d : σ →₀ ℕ) :
    (hasseDeriv (R := R) (d.mapDomain f)).comp (rename f).toLinearMap =
      (rename f).toLinearMap.comp (hasseDeriv d) := by
  apply LinearMap.ext
  intro P
  exact replay hf d P
theorem embedding (f : σ ↪ τ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) :=
  replay f.injective d P
theorem observe {B : Type*} (g : MvPolynomial (Option σ) R → B) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) :
    g (hasseDeriv (d.mapDomain some) (rename some P)) =
      g (rename some (hasseDeriv d P)) := congrArg g (replay (Option.some_injective σ) d P)
theorem collision_lhs : hasseDeriv ((Finsupp.single (0 : Fin 2) 1).mapDomain (fun _ ↦ ()))
    (rename (fun _ : Fin 2 ↦ ()) (X (1 : Fin 2) : MvPolynomial (Fin 2) ℕ)) = 1 := by
  simp [X, rename_monomial, hasseDeriv_monomial, hasseCoeff]
theorem collision_rhs : rename (fun _ : Fin 2 ↦ ())
    (hasseDeriv (Finsupp.single (0 : Fin 2) 1) (X (1 : Fin 2) : MvPolynomial (Fin 2) ℕ)) = 0 := by
  simp [X, hasseDeriv_monomial, hasseCoeff]
#print axioms collision_lhs
#print axioms collision_rhs
section Weaken
variable {A : Type*} [Semiring A]
#check_failure (hasseDeriv (R := A) (0 : σ →₀ ℕ))
#check_failure (rename (R := A) (fun x : σ ↦ x))
end Weaken
#print axioms replay
#print axioms square
#print axioms embedding
#print axioms observe
end AssessHasseRename
