import Roth.GenWronskian
import Mathlib.Combinatorics.Additive.AP.Three.Behrend

/-! Evidence for `Roth.kroneckerExp_injOn` (overview Step 9, re-aimed at `Behrend.map_injOn`). -/

namespace Evidence

variable {σ : Type*} [Fintype σ]

/-- 1. Reindexing identity: `kroneckerExp k = Behrend.map k ∘ (· ∘ e.symm)`. -/
theorem kroneckerExp_eq_comp (k : ℕ) :
    Roth.kroneckerExp (σ := σ) k =
      Behrend.map k ∘ fun d i ↦ d ((Fintype.equivFin σ).symm i) := by
  ext d
  simp [Behrend.map_apply, Roth.kroneckerExp,
    ← (Fintype.equivFin σ).symm.sum_comp fun j ↦ d j * k ^ (Fintype.equivFin σ j : ℕ)]

/-- 2. Composition: the project lemma (without `1 < k`) is `Behrend.map_injOn` composed with
the injective reindexing, via `Set.InjOn.comp`. -/
theorem kroneckerExp_injOn' {k : ℕ} :
    Set.InjOn (Roth.kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by
  rw [kroneckerExp_eq_comp]
  refine Behrend.map_injOn.comp (fun d _ d' _ h ↦ ?_) fun d hd i ↦ hd _
  ext j; simpa using congrFun h (Fintype.equivFin σ j)

end Evidence
