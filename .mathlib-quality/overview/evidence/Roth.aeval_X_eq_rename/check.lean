import Roth.Separation

open MvPolynomial

-- (0) signature
#check @Roth.aeval_X_eq_rename

variable {R σ : Type*} [CommSemiring R]

-- (1) the statement is the applied form of mathlib's lemma (toMvPolynomial unfolds by defeq)
example (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f) :=
  AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f

-- (2) `aeval (X i)` and `toMvPolynomial i` are defeq
example (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f = f.toMvPolynomial i := rfl

-- (3) direct `rw` with the mathlib lemma does not fire on the `aeval (X i)` spelling
example (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f) := by
  fail_if_success rw [Polynomial.toMvPolynomial_eq_rename_comp]
  rw [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]; rfl

-- (4) simp closes it with the mathlib lemma after unfolding the def
example (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f) := by
  simp [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]
