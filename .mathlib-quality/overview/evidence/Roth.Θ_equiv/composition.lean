import Roth.Theta

/-! Evidence for the Roth.Θ_equiv assessment. -/

open MvPolynomial

namespace Roth

-- (1) signature: only `[Fintype σ]`, `[Fintype τ]`; `B` arbitrary (no `1 ≤ B`).
#check @Θ_equiv

-- (2) the inverse direction is a one-line corollary (no separate lemma needed).
example {σ τ : Type*} [Fintype σ] [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : σ → ℕ) :
    Θ B (q ∘ e.symm) (r ∘ e.symm) = Θ B q r := Θ_equiv e.symm B q r

-- (3) the call-site pattern (Theta.lean:919): `Fin (n+2)` versus `Option (Fin (n+1))`.
example (n : ℕ) (B : ℝ) (q r : Fin (n + 2) → ℕ) :
    Θ B (q ∘ (finSuccEquivLast (n := n + 1)).symm) (r ∘ (finSuccEquivLast (n := n + 1)).symm) =
      Θ B q r :=
  Θ_equiv _ B q r

-- (4) mathlib building blocks for the abstract content.
#check @Equiv.iSup_comp
#check @Equiv.iSup_congr
#check @MvPolynomial.renameEquiv
#check @index_rename

end Roth
