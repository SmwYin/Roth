from pathlib import Path
D=Path(__file__).resolve().parent
body='''
#check_failure Roth.eta
#check_failure Roth.lam
#check @Real.rpow
#check @Real.rpow_mul
#check @Real.sqrt_eq_rpow
#check_failure Real.continuousAt_rpow_const
#check @NNReal.coe_rpow
#check @Real.rpow_def_of_neg
namespace Eta231Isolated
noncomputable def formula (C b δ : ℝ) (m : ℕ) : ℝ := C ^ m * δ ^ (b ^ m)
noncomputable def rootIter (δ : ℝ) : ℕ → ℝ
  | 0 => δ
  | n + 1 => √(rootIter δ n)
theorem direct (δ : ℝ) (m : ℕ) :
    formula 10 (1 / 2) δ m = (10 : ℝ) ^ m * Real.rpow δ ((1 / 2 : ℝ) ^ m) := rfl
theorem rootIter_eq (δ : ℝ) (hδ : 0 ≤ δ) (m : ℕ) :
    rootIter δ m = δ ^ ((1 / 2 : ℝ) ^ m) := by
  induction m with
  | zero => simp [rootIter]
  | succ n ih =>
    rw [rootIter, ih, Real.sqrt_eq_rpow, ← Real.rpow_mul hδ, pow_succ]
theorem rootForm (δ : ℝ) (hδ : 0 ≤ δ) (m : ℕ) :
    formula 10 (1 / 2) δ m = 10 ^ m * rootIter δ m :=
  congrArg (fun x : ℝ ↦ 10 ^ m * x) (rootIter_eq δ hδ m).symm
theorem atZero (C b : ℝ) (hb : 0 < b) (m : ℕ) : formula C b 0 m = 0 := by
  simp only [formula, Real.zero_rpow (pow_pos hb m).ne', mul_zero]
theorem dimensionZero (C b δ : ℝ) : formula C b δ 0 = δ := by simp [formula]
theorem negativeGuard : formula 10 (1 / 2) (-1) 0 = -1 := dimensionZero _ _ _
theorem positive (C b δ : ℝ) (hC : 0 < C) (hδ : 0 < δ) (m : ℕ) :
    0 < formula C b δ m := mul_pos (pow_pos hC m) (Real.rpow_pos_of_pos hδ _)
noncomputable def typed (δ : NNReal) (m : ℕ) : NNReal := 10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)
theorem typedBridge (δ : NNReal) (m : ℕ) :
    (typed δ m : ℝ) = formula 10 (1 / 2) δ m := by
  simp only [typed, formula, NNReal.coe_mul, NNReal.coe_pow, NNReal.coe_ofNat,
    NNReal.coe_rpow]
#check_failure (inferInstance : CoeFun ℝ (fun _ : ℝ ↦ ℝ → ℝ))
#print axioms formula
#print axioms rootIter
#print axioms direct
#print axioms rootIter_eq
#print axioms rootForm
#print axioms atZero
#print axioms dimensionZero
#print axioms negativeGuard
#print axioms positive
#print axioms typedBridge
end Eta231Isolated
'''
code=(D/'isolated-prefix.lean.txt').read_text()+body
assert max(map(len,code.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(code)
print(code)
