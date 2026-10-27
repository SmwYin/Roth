import Roth.Index

open MvPolynomial

namespace Roth

/-! (1) `hf` is necessary: collapsing `Bool → Unit` kills `X true - X false`. -/
example : ¬ (index (rename (fun _ : Bool ↦ ()) (X true - X false : MvPolynomial Bool ℝ))
    (fun _ ↦ 0) (fun _ ↦ 1) =
    index (X true - X false : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1)) := by
  have hP : (X true - X false : MvPolynomial Bool ℝ) ≠ 0 := by
    intro h
    have := congrArg (eval (fun b : Bool ↦ if b then (1 : ℝ) else 0)) h
    simp at this
  have hR : rename (fun _ : Bool ↦ ()) (X true - X false : MvPolynomial Bool ℝ) = 0 := by simp
  have h0 : index (0 : MvPolynomial Unit ℝ) (fun _ ↦ 0) (fun _ ↦ 1) = 0 := by simp [index]
  have h1 : index (X true - X false : MvPolynomial Bool ℝ) (fun _ ↦ 0) (fun _ ↦ 1) ≠ 0 := by
    rw [Ne, index_eq_zero_iff hP (fun _ ↦ Nat.one_pos)]
    simp
  rw [hR, h0]
  exact fun h ↦ h1 h.symm

/-! (2) Composition: the proof using only mathlib's `support_rename_of_injective`,
`Finsupp.sum_mapDomain_index_inj` and the project's `taylor_rename` (no `weight_mapDomain`). -/
example {σ τ : Type*} [Fintype σ] [Fintype τ] {f : σ → τ} (hf : Function.Injective f)
    (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) :
    index (rename f P) α r = index P (α ∘ f) (r ∘ f) := by
  classical
  rw [index, index, taylor_rename, support_rename_of_injective hf, Finset.coe_image,
    Set.image_image]
  refine congrArg sInf (Set.image_congr fun d _ ↦ ?_)
  simpa [Finsupp.sum_fintype, weight] using
    Finsupp.sum_mapDomain_index_inj (s := d) (h := fun j n ↦ (n : ℝ) / r j) hf

/-! (3) `[Fintype σ]` cannot be dropped: `index` on `σ` needs it. (Recorded, no code.) -/

end Roth
