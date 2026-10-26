end Nat

/-! ### Alternative definitions -/

namespace Finsupp

variable {α : Type*}

/-- Alternative multinomial definition based on a finsupp, using the support
  for the big operations
-/
def multinomial (f : α →₀ ℕ) : ℕ :=
  (f.sum fun _ => id)! / f.prod fun _ n => n !

theorem multinomial_eq (f : α →₀ ℕ) : f.multinomial = Nat.multinomial f.support f :=
  rfl

theorem multinomial_eq_of_support_subset {f : α →₀ ℕ} {s : Finset α} (h : f.support ⊆ s) :
    f.multinomial = Nat.multinomial s f := by
  simp only [Finsupp.multinomial_eq, Nat.multinomial]
  congr 1
  · simp [Finset.sum_subset h]
  · rw [Finset.prod_subset h]
    grind [Nat.factorial_eq_one]

theorem multinomial_update (a : α) (f : α →₀ ℕ) :
    f.multinomial = (f.sum fun _ => id).choose (f a) * (f.update a 0).multinomial := by
  simp only [multinomial_eq]
  classical
    by_cases h : a ∈ f.support
    · rw [← Finset.insert_erase h, Nat.multinomial_insert (Finset.notMem_erase a _),
        Finset.add_sum_erase _ f h, support_update_zero]
      congr 1
      exact Nat.multinomial_congr fun _ h ↦ (Function.update_of_ne (mem_erase.1 h).1 0 f).symm
    rw [notMem_support_iff] at h
    rw [h, Nat.choose_zero_right, one_mul, ← h, update_self]

end Finsupp

