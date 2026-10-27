import Roth.Index

/-! Evidence for `Roth.le_index_of_forall_eval_eq_zero` (Roth/MainLemma.lean:419). -/

open MvPolynomial Roth

-- (1) Composition: the statement is `le_index_iff.2` plus the project lemma
-- `hasseDeriv_eq_zero_of_degreeOf_lt` (re-proof outside MainLemma, importing only Roth.Index).
example {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) {c : ℝ}
    (hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) :
    c ≤ index P α r := by
  refine (le_index_iff hP).2 fun d he ↦ le_of_not_gt fun hw ↦ he (hvan d (fun j ↦ ?_) hw)
  by_contra! hj
  exact he <| by rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hd j).trans_lt hj), map_zero]

-- (2) `hP` is necessary: for `P = 0` all hypotheses hold but `1 ≤ index 0 α r` fails.
example : ¬ ∀ (P : MvPolynomial Unit ℝ), (∀ j, degreeOf j P ≤ 0) →
    (∀ d : Unit →₀ ℕ, (∀ j, d j ≤ 0) → weight (fun _ ↦ 0) d < 1 →
      eval (fun _ ↦ 0) (hasseDeriv d P) = 0) →
    (1 : ℝ) ≤ index P (fun _ ↦ 0) (fun _ ↦ 0) := by
  intro h
  have := h 0 (by simp) (by simp)
  norm_num [index] at this

-- (3) `hd` is necessary: `P = X^2` in one variable, `r = 1`, `α = 0`, `c = 3`.
-- Every box derivative (d ≤ 1) vanishes at 0, but `index ≤ weight (single () 2) = 2 < 3`.
example : ¬ ∀ (P : MvPolynomial Unit ℝ), P ≠ 0 →
    (∀ d : Unit →₀ ℕ, (∀ j, d j ≤ 1) → weight (fun _ ↦ 1) d < 3 →
      eval (fun _ ↦ 0) (hasseDeriv d P) = 0) →
    (3 : ℝ) ≤ index P (fun _ ↦ 0) (fun _ ↦ 1) := by
  intro h
  have hX : (X () ^ 2 : MvPolynomial Unit ℝ) = monomial (Finsupp.single () 2) 1 := by
    simp [X_pow_eq_monomial]
  have h3 := h (X () ^ 2) (by simp) fun d hd _ ↦ by
    have hd1 := hd ()
    rw [hX, hasseDeriv_monomial, eval_monomial, Finsupp.prod_pow]
    simp only [mul_one, Finset.univ_unique, PUnit.default_eq_unit, Finsupp.coe_tsub, Pi.sub_apply,
      Finsupp.single_eq_same, Finset.prod_singleton, mul_eq_zero, Nat.cast_eq_zero,
      pow_eq_zero_iff', ne_eq, true_and]
    exact Or.inr (by have := hd PUnit.unit; omega)
  have hle : index (X () ^ 2 : MvPolynomial Unit ℝ) (fun _ ↦ 0) (fun _ ↦ 1) ≤
      weight (fun _ ↦ 1) (Finsupp.single () 2) := index_le_weight (by
    rw [hX, hasseDeriv_monomial]
    simp [hasseCoeff])
  have hw : weight (fun _ ↦ 1) (Finsupp.single () 2) = 2 := by
    simp [weight]
  linarith
