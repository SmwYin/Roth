import Roth.Separation

open MvPolynomial

section
variable {R : Type*} [CommSemiring R] {τ : Type*}

-- (0) signature of the project lemma (section Fintype/DecidableEq are omitted)
#check @Roth.coeff_coeffNone

-- (1) re-aimed statement (optionElim spelling) is literally mathlib's lemma, no proof needed
example (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (Roth.coeffNone P ν).coeff d = P.coeff (d.optionElim ν) :=
  optionEquivLeft_coeff_coeff R P ν d

-- (2) the only gap between the two spellings: a Finsupp identity absent from mathlib
theorem mapDomain_some_add_single_none (d : τ →₀ ℕ) (ν : ℕ) :
    d.mapDomain some + Finsupp.single none ν = d.optionElim ν := by
  ext o
  cases o <;> simp [Finsupp.mapDomain_of_notMem_range,
    Finsupp.mapDomain_apply_of_injective (Option.some_injective τ)]

-- (3) the project's exact statement from mathlib in one line given (2)
example (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (Roth.coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν) := by
  rw [mapDomain_some_add_single_none]; exact optionEquivLeft_coeff_coeff R P ν d

-- (4) call site 107 closes without coeff_coeffNone (via optionEquivLeft_coeff_some_coeff_none)
example (P : MvPolynomial (Option τ) R) (e : Option τ →₀ ℕ) :
    (Roth.coeffNone P (e none)).coeff (Finsupp.some e) = P.coeff e :=
  optionEquivLeft_coeff_some_coeff_none R τ e P
end
