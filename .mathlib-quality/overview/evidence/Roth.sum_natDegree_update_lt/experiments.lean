import Roth.Wronskian
import Mathlib.Algebra.Polynomial.CancelLeads

/-! Evidence for `Roth.sum_natDegree_update_lt`. -/

open Polynomial

/-- (A) The pointwise core, over a division ring, from mathlib's `degree_sub_lt_left`. -/
theorem natDegree_sub_C_div_mul_lt {K : Type*} [DivisionRing K] {p q : K[X]} (hp : p ≠ 0)
    (hdeg : p.natDegree = q.natDegree) (hne : q - C (q.leadingCoeff / p.leadingCoeff) * p ≠ 0) :
    (q - C (q.leadingCoeff / p.leadingCoeff) * p).natDegree < q.natDegree := by
  have hq : q ≠ 0 := by rintro rfl; simp at hne
  have hlc : p.leadingCoeff ≠ 0 := leadingCoeff_ne_zero.2 hp
  have ha : q.leadingCoeff / p.leadingCoeff ≠ 0 := div_ne_zero (leadingCoeff_ne_zero.2 hq) hlc
  exact natDegree_lt_natDegree hne (degree_sub_lt_left
    (by rw [degree_C_mul ha, degree_eq_natDegree hp, degree_eq_natDegree hq, hdeg]) hq
    (by rw [leadingCoeff_mul, leadingCoeff_C, div_mul_cancel₀ _ hlc]))

/-- (B) Weakened sum form: any `Fintype` index, `[DivisionRing K]`, no linear independence,
no `ν ≠ ν'`; only `φ ν ≠ 0` and nonvanishing of the updated member. -/
theorem sum_natDegree_update_lt' {K ι : Type*} [DivisionRing K] [Fintype ι] [DecidableEq ι]
    {φ : ι → K[X]} {ν ν' : ι} (hp : φ ν ≠ 0)
    (hne : φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν ≠ 0)
    (hdeg : (φ ν).natDegree = (φ ν').natDegree) :
    ∑ ρ, (Function.update φ ν'
      (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree
      < ∑ ρ, (φ ρ).natDegree := by
  have hlt := natDegree_sub_C_div_mul_lt hp hdeg hne
  refine Finset.sum_lt_sum (fun i _ ↦ ?_) ⟨ν', Finset.mem_univ _, by simpa⟩
  by_cases hi : i = ν'
  · simpa [hi] using hlt.le
  · simp [Function.update_of_ne hi]

/-- (C) The project statement is a corollary of (B). -/
example {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} (hφ : LinearIndependent K φ)
    {ν ν' : Fin l} (h : ν ≠ ν') (hdeg : (φ ν).natDegree = (φ ν').natDegree) :
    ∑ ρ, (Function.update φ ν'
      (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree
      < ∑ ρ, (φ ρ).natDegree :=
  sum_natDegree_update_lt' (hφ.ne_zero ν)
    (by simpa using (Roth.linearIndependent_update_sub_smul h _ hφ).ne_zero ν') hdeg

/-- (D) Relation to mathlib's division-free `cancelLeads` when degrees agree. -/
example {K : Type*} [Field K] {p q : K[X]} (hp : p ≠ 0) (hdeg : p.natDegree = q.natDegree) :
    q - C (q.leadingCoeff / p.leadingCoeff) * p = C p.leadingCoeff⁻¹ * p.cancelLeads q := by
  have hlc : p.leadingCoeff ≠ 0 := leadingCoeff_ne_zero.2 hp
  rw [cancelLeads, hdeg, Nat.sub_self, pow_zero, mul_one, mul_one, mul_sub, ← mul_assoc,
    ← mul_assoc, ← C_mul, ← C_mul, inv_mul_cancel₀ hlc, C_1, one_mul, div_eq_inv_mul]
