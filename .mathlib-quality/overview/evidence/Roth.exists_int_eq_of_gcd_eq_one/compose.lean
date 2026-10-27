import Roth.Separation

open Finset

-- (0) signature of the project declaration
#check @Roth.exists_int_eq_of_gcd_eq_one

-- (1) bridge: finset gcd = 1 gives `Ideal.span (u '' s) = ⊤` in any Bézout normalized-GCD ring
theorem span_image_eq_top_of_gcd_eq_one {R ι : Type*} [CommRing R] [IsBezout R]
    [NormalizedGCDMonoid R] {s : Finset ι} {u : ι → R} (hu : s.gcd u = 1) :
    Ideal.span (u '' s) = ⊤ := by
  obtain ⟨g, hg⟩ := Finset.gcd_eq_sum_mul s u
  rw [Ideal.eq_top_iff_one, ← hu, hg]
  exact Ideal.sum_mem _ fun i hi ↦
    Ideal.mul_mem_right _ _ (Ideal.subset_span ⟨i, hi, rfl⟩)

-- (2) general form: submodule membership test, any module over a Bézout normalized-GCD ring
theorem Submodule.mem_of_gcd_eq_one_of_smul_mem {R M ι : Type*} [CommRing R] [IsBezout R]
    [NormalizedGCDMonoid R] [AddCommGroup M] [Module R M] (N : Submodule R M)
    {s : Finset ι} {u : ι → R} (hu : s.gcd u = 1) {x : M} (hx : ∀ a ∈ s, u a • x ∈ N) :
    x ∈ N :=
  N.mem_of_span_top_of_smul_mem _ (span_image_eq_top_of_gcd_eq_one hu) x
    fun ⟨_, a, ha, h⟩ ↦ h ▸ hx a ha

-- (3) the project statement as a specialisation of (2) with R = ℤ, M = ℚ, N = 1
example {ι : Type*} {s : Finset ι} {u : ι → ℤ} (hu : s.gcd u = 1)
    {v : ℚ} (hv : ∀ a ∈ s, ∃ z : ℤ, (u a : ℚ) * v = z) : ∃ z : ℤ, v = z := by
  have := (1 : Submodule ℤ ℚ).mem_of_gcd_eq_one_of_smul_mem hu (x := v) fun a ha ↦ by
    obtain ⟨z, hz⟩ := hv a ha
    exact Submodule.mem_one.2 ⟨z, by simp [zsmul_eq_mul, hz]⟩
  obtain ⟨z, hz⟩ := Submodule.mem_one.1 this
  exact ⟨z, by simpa using hz.symm⟩

-- (4) direct composition from mathlib only (no new lemma), as at the call site
example {ι : Type*} {s : Finset ι} {u : ι → ℤ} (hu : s.gcd u = 1)
    {v : ℚ} (hv : ∀ a ∈ s, ∃ z : ℤ, (u a : ℚ) * v = z) : ∃ z : ℤ, v = z := by
  have hs : Ideal.span (u '' s) = ⊤ := by
    obtain ⟨g, hg⟩ := Finset.gcd_eq_sum_mul s u
    rw [Ideal.eq_top_iff_one, ← hu, hg]
    exact Ideal.sum_mem _ fun i hi ↦ Ideal.mul_mem_right _ _ (Ideal.subset_span ⟨i, hi, rfl⟩)
  obtain ⟨z, hz⟩ := Submodule.mem_one.1 <|
    (1 : Submodule ℤ ℚ).mem_of_span_top_of_smul_mem _ hs v fun ⟨_, a, ha, h⟩ ↦ by
      obtain ⟨z, hz⟩ := hv a ha
      exact h ▸ Submodule.mem_one.2 ⟨z, by simp [zsmul_eq_mul, hz]⟩
  exact ⟨z, by simpa using hz.symm⟩
