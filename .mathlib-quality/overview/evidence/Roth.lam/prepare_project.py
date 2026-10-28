from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
code=(D/'disk-prefix.lean.txt').read_text()+'''
namespace Lam229Project
noncomputable def realFormula (δ n m : ℝ) : ℝ := 4 * (1 + 3 * δ) * n * √m
noncomputable def scaled (a m : ℝ) : ℝ := 4 * a * √m
theorem bridge (δ : ℝ) (n m : ℕ) : Roth.lam δ n m = realFormula δ n m := rfl
theorem unfolding (δ : ℝ) (n m : ℕ) :
    Roth.lam δ n m = 4 * (1 + 3 * δ) * n * √(m : ℝ) := rfl
theorem scaleBridge (δ : ℝ) (n m : ℕ) :
    Roth.lam δ n m = scaled ((1 + 3 * δ) * n) m := by
  dsimp only [Roth.lam, scaled]
  ring
theorem normalForm (δ : ℝ) (n m : ℕ) :
    Roth.lam δ n m = (4 + 12 * δ) * n * √(m : ℝ) := by
  dsimp only [Roth.lam]
  ring
theorem continuousDelta (n m : ℕ) : Continuous (fun δ ↦ Roth.lam δ n m) := by
  unfold Roth.lam
  fun_prop
#print axioms realFormula
#print axioms scaled
#print axioms bridge
#print axioms unfolding
#print axioms scaleBridge
#print axioms normalForm
#print axioms continuousDelta
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.lam
  Lean.logInfo m!"LAM229_UNIVERSE_PARAMETERS: {ci.levelParams}"
  Lean.logInfo m!"LAM229_REAL_FORMULA_BRIDGE: PASS"
end Lam229Project
'''
assert max(map(len,code.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print(code)
