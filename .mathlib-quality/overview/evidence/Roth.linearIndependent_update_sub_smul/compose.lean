import Roth.Wronskian

/-! Evidence for `Roth.linearIndependent_update_sub_smul`. -/

open Polynomial

-- (1) General form (any ring, any module, any index type), as an iff, composed from
-- mathlib's `linearIndependent_add_smul_iff` with `c = Pi.single j (-r)`.
theorem linearIndependent_update_sub_smul_iff {ι R M : Type*} [DecidableEq ι] [Ring R]
    [AddCommGroup M] [Module R M] {v : ι → M} {i j : ι} (hij : i ≠ j) (r : R) :
    LinearIndependent R (Function.update v j (v j - r • v i)) ↔ LinearIndependent R v := by
  convert linearIndependent_add_smul_iff (v := v) (c := Pi.single j (-r)) (i := i)
    (by simp [hij]) using 2
  ext k
  by_cases hk : k = j <;> simp [Pi.single_apply, hk, sub_eq_add_neg]

-- (2) The project statement is a one-line specialisation of (1).
example {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K)
    (hφ : LinearIndependent K φ) :
    LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν)) := by
  simpa [smul_eq_C_mul] using (linearIndependent_update_sub_smul_iff h c).2 hφ

-- (3) The project proof (via `finrank` of the span) works over a division ring only;
-- the statement itself holds over any ring by (1). `ν ≠ ν'` is necessary:
example : ¬ LinearIndependent ℚ (Function.update ![(X : ℚ[X])] 0 (![X] 0 - C 1 * ![X] 0)) := by
  simp
