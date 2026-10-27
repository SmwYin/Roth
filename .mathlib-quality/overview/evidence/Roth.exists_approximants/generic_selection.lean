import Roth.Main

/-! Evidence for `Roth.exists_approximants`.
1. The combinatorial core is a generic "dependent choice with growth" lemma:
   if `f` is unbounded on `S`, then for any `g` one can pick `s : ℕ → α` in `S` with
   `g (f (s k)) < f (s (k + 1))` and `B < f (s 0)`. Proved by `Nat.rec`, as in the project.
2. Mathlib's closest lemma `exists_seq_of_forall_finset_exists` also yields it (all pairs
   `m < n`), showing the selection step is a short composition of a mathlib lemma. -/

open Roth

theorem exists_seq_growth {α : Type*} {S : Set α} (f : α → ℕ)
    (hS : ∀ Q₀ : ℕ, ∃ x ∈ S, Q₀ < f x) (g : ℕ → ℕ) (B : ℕ) :
    ∃ s : ℕ → α, (∀ k, s k ∈ S) ∧ B < f (s 0) ∧ ∀ k, g (f (s k)) < f (s (k + 1)) := by
  choose c hcS hc using hS
  let s : ℕ → α := Nat.rec (c B) fun _ x ↦ c (g (f x))
  exact ⟨s, by rintro (_ | k) <;> exact hcS _, hc _, fun k ↦ hc _⟩

/-- Same content via mathlib's `exists_seq_of_forall_finset_exists` (relation on all pairs). -/
theorem exists_seq_growth' {α : Type*} {S : Set α} (f : α → ℕ)
    (hS : ∀ Q₀ : ℕ, ∃ x ∈ S, Q₀ < f x) (g : ℕ → ℕ) :
    ∃ s : ℕ → α, (∀ k, s k ∈ S) ∧ ∀ m n, m < n → g (f (s m)) < f (s n) := by
  classical
  obtain ⟨s, hs, hr⟩ := exists_seq_of_forall_finset_exists (· ∈ S) (fun x y ↦ g (f x) < f y)
    fun t _ ↦ by
      obtain ⟨y, hy, hlt⟩ := hS (t.sup (g ∘ f))
      exact ⟨y, hy, fun x hx ↦ (Finset.le_sup (f := g ∘ f) hx).trans_lt hlt⟩
  exact ⟨s, hs, hr⟩

/-- `δ` carries no hypothesis: the statement already holds for `δ ≤ 0`
(the growth condition is then implied by `1 < q j`). -/
example {α κ : ℝ} (hα : Irrational α) (hκ : 0 < κ) (hinf : (approxSet α κ).Infinite) :
    ∃ (h : Fin 3 → ℤ) (q : Fin 3 → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ 0 < Real.log (q 0) ∧
      ∀ i j : Fin 3, i.val + 1 = j.val → 2 / (-1 : ℝ) * Real.log (q i) < Real.log (q j) :=
  exists_approximants hα hκ hinf 3 0
