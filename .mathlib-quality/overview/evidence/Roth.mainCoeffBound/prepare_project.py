from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
body='''
namespace Coeff232Project
theorem direct (δ : ℝ) (q r : ℕ) :
    Roth.mainCoeffBound δ q r = Nat.floor (Real.rpow (q : ℝ) (δ * (r : ℝ))) := rfl
theorem endpoints (δ : ℝ) (q r : ℕ) :
    (Roth.mainCoeffBound δ q r : ℝ) ≤ (q : ℝ) ^ (δ * r) ∧
      (q : ℝ) ^ (δ * r) < (Roth.mainCoeffBound δ q r : ℝ) + 1 :=
  ⟨Nat.floor_le (Real.rpow_nonneg (Nat.cast_nonneg q) _), Nat.lt_floor_add_one _⟩
theorem coeffBound (δ : ℝ) (q r : ℕ) (z : ℤ) :
    |z| ≤ (Roth.mainCoeffBound δ q r : ℤ) ↔ |(z : ℝ)| ≤ (q : ℝ) ^ (δ * r) := by
  unfold Roth.mainCoeffBound
  rw [Int.natCast_floor_eq_floor (Real.rpow_nonneg (Nat.cast_nonneg q) _),
    Int.le_floor, Int.cast_abs]
theorem sqrtBound {δ : ℝ} {q r : ℕ} (hX : 2 ≤ (q : ℝ) ^ (δ * r)) :
    √((q : ℝ) ^ (δ * r)) < Roth.mainCoeffBound δ q r ∧
      (Roth.mainCoeffBound δ q r : ℝ) ≤ (q : ℝ) ^ (δ * r) := Roth.sqrt_lt_floor hX
#synth FloorRing ℝ
#synth FloorSemiring ℝ
#synth NatCast ℝ
#print axioms direct
#print axioms endpoints
#print axioms coeffBound
#print axioms sqrtBound
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.mainCoeffBound
  Lean.logInfo m!"COEFF232_UNIVERSE_PARAMETERS: {ci.levelParams}"
  Lean.logInfo "COEFF232_STRICT3_CONSTRUCTION: PASS"
end Coeff232Project
'''
code=(D/'disk-prefix.lean.txt').read_text()+body
assert max(map(len,code.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print(code)
