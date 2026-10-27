import Roth.Separation

open Finset

-- (0) signature of the project declaration
#check @Roth.exists_sum_mul_eq_gcd

-- (1) the project statement generalised to any Bézout normalized-GCD ring; one-line from mathlib
example {R ι : Type*} [CommRing R] [IsBezout R] [NormalizedGCDMonoid R]
    (s : Finset ι) (u : ι → R) : ∃ z : ι → R, ∑ i ∈ s, z i * u i = s.gcd u := by
  simpa [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u

-- (2) the only call site (exists_int_eq_of_gcd_eq_one, Separation.lean:446) served directly by
-- mathlib in its own orientation: `s.gcd u = ∑ i ∈ s, u i * z i`
example {ι : Type*} {s : Finset ι} {u : ι → ℤ} (hu : s.gcd u = 1)
    {v : ℚ} (hv : ∀ a ∈ s, ∃ z : ℤ, (u a : ℚ) * v = z) : ∃ z : ℤ, v = z := by
  classical
  obtain ⟨z, hz⟩ := Finset.gcd_eq_sum_mul s u
  rw [hu] at hz
  choose! w hw using hv
  refine ⟨∑ i ∈ s, w i * z i, ?_⟩
  calc v = ((∑ i ∈ s, u i * z i : ℤ) : ℚ) * v := by simp [← hz]
    _ = ((∑ i ∈ s, w i * z i : ℤ) : ℚ) := by
        push_cast
        rw [Finset.sum_mul]
        exact Finset.sum_congr rfl fun i hi ↦ by rw [mul_right_comm, hw i hi]

-- (3) ℤ instances needed by (1) are found
example : IsBezout ℤ := inferInstance
