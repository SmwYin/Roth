import Mathlib.Data.Fin.Tuple.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-! Evidence for `Roth.card_filter_box_last`: the general (plain-function, arbitrary
coordinate finsets) form of fibrewise counting over the last coordinate, which is the
natural mathlib-level statement next to `Finset.card_snocEquiv_filter_piFinset`. -/

open Finset Fintype

theorem card_filter_piFinset_eq_sum_snoc {n : ℕ} {α : Type*} [DecidableEq α]
    (S : Fin (n + 1) → Finset α) (P : (Fin (n + 1) → α) → Prop) [DecidablePred P] :
    #{r ∈ piFinset S | P r} =
      ∑ a ∈ S (Fin.last n), #{r ∈ piFinset (Fin.init S) | P (Fin.snoc r a)} := by
  rw [card_eq_sum_card_fiberwise (f := fun r ↦ r (Fin.last n)) (t := S (Fin.last n))
    fun r hr ↦ by simp only [coe_filter, Set.mem_ofPred_eq, mem_piFinset] at hr; exact hr.1 _]
  refine sum_congr rfl fun a ha ↦ ?_
  refine (card_bij' (fun r _ ↦ Fin.snoc r a) (fun r _ ↦ Fin.init r) ?_ ?_ ?_ ?_).symm
  · intro r hr
    simp only [mem_filter, mem_piFinset] at hr ⊢
    refine ⟨⟨fun i ↦ ?_, hr.2⟩, by simp⟩
    refine Fin.lastCases ?_ (fun j ↦ ?_) i
    · simpa using ha
    · rw [Fin.snoc_castSucc]; exact hr.1 j
  · intro r hr
    simp only [mem_filter, mem_piFinset] at hr ⊢
    obtain ⟨⟨h1, h2⟩, h3⟩ := hr
    refine ⟨fun i ↦ h1 _, ?_⟩
    rw [← h3, Fin.snoc_init_self]
    exact h2
  · intro r _
    simp [Fin.init_snoc]
  · intro r hr
    simp only [mem_filter] at hr
    rw [← hr.2, Fin.snoc_init_self]
