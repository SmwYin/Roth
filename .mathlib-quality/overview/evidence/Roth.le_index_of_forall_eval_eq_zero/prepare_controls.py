from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
s=(D/'project-executed.lean.txt').read_text()+'''
namespace Cutoff252Controls
open Roth MvPolynomial Cutoff252Project
theorem local_degree_of_global {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ}
    {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (c : ℝ) :
    ∀ d, weight r d < c → (¬ ∀ j, d j ≤ r j) → ∃ j, degreeOf j P < d j := by
  intro d _ hb
  obtain ⟨j, hj⟩ : ∃ j, r j < d j := by simpa only [not_forall, not_le] using hb
  exact ⟨j, (hd j).trans_lt hj⟩
theorem local_strictly_weaker :
    (∀ d : Unit →₀ ℕ, weight (fun _ ↦ 0) d < 0 → (¬ ∀ j, d j ≤ 0) →
      ∃ j, degreeOf j (X () : MvPolynomial Unit ℝ) < d j) ∧
    ¬ (∀ j : Unit, degreeOf j (X () : MvPolynomial Unit ℝ) ≤ 0) := by
  constructor
  · intro d hw
    exact (not_lt_of_ge (weight_nonneg _ d) hw).elim
  · simp
theorem missing_degree_guard :
    (X () : MvPolynomial Unit ℝ) ≠ 0 ∧
    (∀ d : Unit →₀ ℕ, (∀ j, d j ≤ 0) → weight (fun _ ↦ 0) d < 1 →
      eval (fun _ ↦ (0 : ℝ)) (hasseDeriv d (X () : MvPolynomial Unit ℝ)) = 0) ∧
    ¬ (1 : ℝ) ≤ index (X () : MvPolynomial Unit ℝ) (fun _ ↦ 0) (fun _ ↦ 0) := by
  refine ⟨X_ne_zero (), ?_, ?_⟩
  · intro d hd _
    have hz : d = 0 := Finsupp.ext fun j ↦ Nat.eq_zero_of_le_zero (hd j)
    subst d
    simp
  · rw [all_zero_weights]
    norm_num
theorem composition_check {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) {c : ℝ}
    (hin : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) :
    c ≤ index P α r := by
  fail_if_success
    exact MvPowerSeries.nat_le_weightedOrder (fun j ↦ r j) hin
  fail_if_success
    solve | simp only [index]
  exact recovery hP hd α hin
end Cutoff252Controls
#print axioms Cutoff252Controls.local_degree_of_global
#print axioms Cutoff252Controls.local_strictly_weaker
#print axioms Cutoff252Controls.missing_degree_guard
#print axioms Cutoff252Controls.composition_check
'''
assert max(map(len,s.splitlines()))<=100
(D/'controls-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS controls prepared; width',max(map(len,s.splitlines())))
