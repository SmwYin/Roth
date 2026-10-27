import Roth.Separation

open MvPolynomial Finsupp

namespace Roth.Evidence

variable {τ : Type*} {R : Type*} [CommSemiring R]

-- (1) mathlib's own decomposition: `d = optionElim (d none) d.some`, i.e. `Finsupp.optionElim_some`.
example (d : Option τ →₀ ℕ) : d = d.some.optionElim (d none) := (optionElim_some d).symm

-- (2) the missing glue between the project's spelling and mathlib's `optionElim`,
-- stated for any `AddCommMonoid` (needed by `mapDomain`).
theorem optionElim_eq_mapDomain_add_single {α M : Type*} [AddCommMonoid M] (y : M) (f : α →₀ M) :
    f.optionElim y = f.mapDomain Option.some + single none y := by
  ext o
  cases o <;> simp [mapDomain_of_notMem_range,
    mapDomain_apply_of_injective (Option.some_injective α)]

-- (3) the project lemma follows in one line from (1) + (2).
example (d : Option τ →₀ ℕ) :
    d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none) := by
  rw [← optionElim_eq_mapDomain_add_single, optionElim_some]

-- (4) weakening: the statement holds for any `AddCommMonoid M`, not just `ℕ`.
example {M : Type*} [AddCommMonoid M] (d : Option τ →₀ M) :
    d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none) := by
  ext o
  cases o <;> simp [mapDomain_of_notMem_range,
    mapDomain_apply_of_injective (Option.some_injective τ), some_apply]

-- (5) the only call site (eq_sum_X_none_pow_mul_coeffNone, Separation.lean:107) needs
-- `P.coeff e = (coeffNone P (e none)).coeff e.some`, which is literally mathlib's
-- `MvPolynomial.optionEquivLeft_coeff_some_coeff_none` after unfolding `coeffNone`.
example (P : MvPolynomial (Option τ) R) (e : Option τ →₀ ℕ) :
    P.coeff e = (coeffNone P (e none)).coeff (Finsupp.some e) :=
  (optionEquivLeft_coeff_some_coeff_none R τ e P).symm

-- (6) `coeff_coeffNone` restated against mathlib's `optionElim` is `optionEquivLeft_coeff_coeff`.
example (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (coeffNone P ν).coeff d = P.coeff (d.optionElim ν) :=
  optionEquivLeft_coeff_coeff R P ν d

end Roth.Evidence
