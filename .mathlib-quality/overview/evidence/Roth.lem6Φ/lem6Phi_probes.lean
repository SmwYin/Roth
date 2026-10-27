import Roth.Theta

open Roth

-- (1) `lem6Φ` unfolds by `rfl` to the sum of two mathlib-free `Θ` terms (the paper's eq. (15)).
example {τ : Type*} [Fintype τ] (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) :
    lem6Φ q r M l =
      Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) + Θ M (q ∘ some) (fun j ↦ l * r (some j)) :=
  rfl

-- (2) `[Fintype τ]` is essential: `Θ` itself takes `[Fintype σ]` (dropping it fails with
-- `failed to synthesize Fintype τ`, checked once and removed). `[DecidableEq τ]` is not taken
-- (see the `#check` below).

-- (3) signatures.
#check @lem6Φ
#check @Θ
