import Mathlib.Algebra.MvPolynomial.Equiv

open MvPolynomial

/-! The project lemma is the `d := Finsupp.single default n` instance of mathlib's
`MvPolynomial.coeff_uniqueAlgEquiv_symm`; it closes by one `rw` of the mathlib lemma plus
`Finsupp.single_eq_same` (plain `simp` unfolds `symm` first and fails, so the rw is needed). -/

example {R σ : Type*} [CommSemiring R] [Unique σ] (f : Polynomial R) (n : ℕ) :
    ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n := by
  rw [MvPolynomial.coeff_uniqueAlgEquiv_symm, Finsupp.single_eq_same]

example {R σ : Type*} [CommSemiring R] [Unique σ] (f : Polynomial R) (n : ℕ) :
    ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n :=
  (MvPolynomial.coeff_uniqueAlgEquiv_symm R f _).trans (by rw [Finsupp.single_eq_same])
