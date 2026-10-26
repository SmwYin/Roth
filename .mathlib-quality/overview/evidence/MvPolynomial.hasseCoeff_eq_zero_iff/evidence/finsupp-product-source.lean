  prod_eq_single _ (fun a ↦ by simp [Subsingleton.elim a default]) h₁

end SumProd

section CommMonoidWithZero
variable [Zero α] [CommMonoidWithZero β] [Nontrivial β] [NoZeroDivisors β]
  {f : ι →₀ α} (a : α) {g : ι → α → β}

@[simp]
lemma prod_eq_zero_iff : f.prod g = 0 ↔ ∃ i ∈ f.support, g i (f i) = 0 := Finset.prod_eq_zero_iff
lemma prod_ne_zero_iff : f.prod g ≠ 0 ↔ ∀ i ∈ f.support, g i (f i) ≠ 0 := Finset.prod_ne_zero_iff

end CommMonoidWithZero
end Finsupp
