import Mathlib.RingTheory.Polynomial.Content

/-! Evidence for `Roth.isPrimitive_pow` (Roth/Theta.lean:175).
Mathlib (v4.34.0) has `Polynomial.IsPrimitive.mul` but no `IsPrimitive.pow` / `IsPrimitive.prod`
and no `content_pow`. These checks record: the project statement, its general form, and two
alternative one-line proofs. -/

open Polynomial

-- (1) project statement, project proof verbatim
example {p : Polynomial ℤ} (hp : p.IsPrimitive) (t : ℕ) : (p ^ t).IsPrimitive :=
  Nat.rec Polynomial.isPrimitive_one (fun t ih ↦ by simpa [pow_succ] using ih.mul hp) t

-- (2) general form over any CommRing with NormalizedGCDMonoid (the context of IsPrimitive.mul)
theorem isPrimitive_pow_general {R : Type*} [CommRing R] [NormalizedGCDMonoid R] {p : R[X]}
    (hp : p.IsPrimitive) (t : ℕ) : (p ^ t).IsPrimitive := by
  induction t with
  | zero => simp
  | succ n ih => simpa [pow_succ] using ih.mul hp

-- (3) content route: content is multiplicative over ℤ (StrongNormalizedGCDMonoid)
example {p : Polynomial ℤ} (hp : p.IsPrimitive) (t : ℕ) : (p ^ t).IsPrimitive := by
  rw [isPrimitive_iff_content_eq_one]
  induction t with
  | zero => simp
  | succ n ih => rw [pow_succ, content_mul, ih, hp.content_eq_one, one_mul]
