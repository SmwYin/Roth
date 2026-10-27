import Roth.GenWronskian

open Finset

/-! Evidence for `Roth.det_sum_rows`. -/

-- (1) Weakening: `Fin l` replaced by an arbitrary `[Fintype n] [DecidableEq n]` row/column type.
theorem det_sum_rows_gen {A : Type*} [CommRing A] {n : Type*} [Fintype n] [DecidableEq n]
    {ι : Type*} (s : n → Finset ι) (c : n → ι → A) (N : n → ι → n → A) :
    (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det := by
  have h := (Matrix.detRowAlternating (R := A) (n := n)).toMultilinearMap.map_sum_finset
    (fun μ i ↦ c μ i • N μ i) s
  simp_rw [MultilinearMap.map_smul_univ, smul_eq_mul] at h
  simp only [Matrix.det, Finset.sum_fn, Pi.smul_def, smul_eq_mul] at h ⊢
  exact h

-- (2) The original is a specialisation of (1).
example {A : Type*} [CommRing A] {l : ℕ} {ι : Type*} (s : Fin l → Finset ι) (c : Fin l → ι → A)
    (N : Fin l → ι → Fin l → A) :
    (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det :=
  det_sum_rows_gen s c N

-- (3) Composition from mathlib: the matrix-of-vectors version is literally
-- `MultilinearMap.map_sum_finset` for `detRowAlternating`, one call (no scalars).
example {A : Type*} [CommRing A] {n : Type*} [Fintype n] [DecidableEq n]
    {ι : Type*} (s : n → Finset ι) (g : n → ι → n → A) :
    (Matrix.of fun μ ↦ ∑ i ∈ s μ, g μ i).det =
      ∑ f ∈ Fintype.piFinset s, (Matrix.of fun μ ↦ g μ (f μ)).det :=
  (Matrix.detRowAlternating (R := A) (n := n)).toMultilinearMap.map_sum_finset g s
