import Roth.Theta

/-! Probes for `Roth.lem6M` (reducibility / closed-form). -/

open Roth

-- (1) Reducibility probe: the def unfolds by `rfl` (plain semireducible def).
example (p r₁ : ℕ) (B : ℝ) (l : ℕ) :
    lem6M p r₁ B l = ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r₁) := rfl

-- (2) Closed form as a single `l`-th power times `l!`: no mathlib name, but `ring` gives it.
example (p r₁ : ℕ) (B : ℝ) (l : ℕ) :
    lem6M p r₁ B l = l.factorial * (((r₁ : ℝ) + 1) ^ p * B * 2 ^ (p * r₁)) ^ l := by
  rw [lem6M]; ring

-- (3) It is the RHS of mathlib's `Matrix.det_le` shape `n! • x^n` with
--     `x = (r₁+1)^p B 2^{p r₁}`, `n = l` (pure arithmetic restatement).
example (p r₁ : ℕ) (B : ℝ) (l : ℕ) :
    lem6M p r₁ B l = l.factorial • (((r₁ : ℝ) + 1) ^ p * B * 2 ^ (p * r₁)) ^ l := by
  rw [lem6M, nsmul_eq_mul]; ring
