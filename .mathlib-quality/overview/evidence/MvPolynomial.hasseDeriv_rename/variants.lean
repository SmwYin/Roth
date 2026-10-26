import Roth.HasseDeriv

/-! Evidence for the `/overview` assessment of `MvPolynomial.hasseDeriv_rename`. -/

open MvPolynomial

variable {σ τ R : Type*} [CommSemiring R]

-- (1) the statement re-proved standalone (same `induction_on'` proof as the project).
example {f : σ → τ} (hf : Function.Injective f) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    simp [rename_monomial, hasseCoeff, Finsupp.prod_mapDomain_index_inj hf,
      Finsupp.mapDomain_apply_of_injective hf, ← Finsupp.mapDomain_tsub hf]
  | add p q hp hq => simp [hp, hq]

-- (2) the univariate-order special case `d = single i n` (Hasse analogue of `pderiv_rename`).
example {f : σ → τ} (hf : Function.Injective f) (i : σ) (n : ℕ) (P : MvPolynomial σ R) :
    hasseDeriv (Finsupp.single (f i) n) (rename f P) =
      rename f (hasseDeriv (Finsupp.single i n) P) := by
  rw [← Finsupp.mapDomain_single, hasseDeriv_rename hf]

-- (3) injectivity cannot be dropped: collapse the two variables of `Fin 2` to one.
-- With `P = X 0 * X 1`, `d = e_0`: LHS is `Δ_{e_*} (X_*^2) = 2 X_*`, RHS is `rename (X 1) = X_*`.
example : ¬ ∀ (P : MvPolynomial (Fin 2) ℤ),
    hasseDeriv ((Finsupp.single (0 : Fin 2) 1).mapDomain (fun _ ↦ ())) (rename (fun _ ↦ ()) P) =
      rename (fun _ ↦ ()) (hasseDeriv (Finsupp.single (0 : Fin 2) 1) P) := by
  intro h
  have hP : (X 0 * X 1 : MvPolynomial (Fin 2) ℤ) =
      monomial (Finsupp.single 0 1 + Finsupp.single 1 1) 1 := by
    simp [X]
  have := congrArg (eval fun _ ↦ (1 : ℤ)) (h (X 0 * X 1))
  rw [hP, rename_monomial, hasseDeriv_monomial, hasseDeriv_monomial, rename_monomial] at this
  simp [hasseCoeff, Finsupp.mapDomain_add, Finsupp.mapDomain_single, eval_monomial] at this
