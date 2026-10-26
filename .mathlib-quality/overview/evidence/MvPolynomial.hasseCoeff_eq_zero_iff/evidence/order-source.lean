
variable [CanonicallyOrderedAdd α]

@[simp]
theorem add_eq_zero_iff (f g : ι →₀ α) : f + g = 0 ↔ f = 0 ∧ g = 0 := by
  simp [DFunLike.ext_iff, forall_and]

theorem le_iff' (f g : ι →₀ α) {s : Finset ι} (hf : f.support ⊆ s) :
    f ≤ g ↔ ∀ i ∈ s, f i ≤ g i := by
  refine ⟨fun h s _ ↦ h s, fun h s ↦ ?_⟩
  by_cases H : s ∈ f.support
  · exact h s (hf H)
  · exact notMem_support_iff.1 H ▸ zero_le

theorem le_iff (f g : ι →₀ α) : f ≤ g ↔ ∀ i ∈ f.support, f i ≤ g i :=
  le_iff' f g <| Subset.refl _

lemma support_monotone : Monotone (support (α := ι) (M := α)) :=
