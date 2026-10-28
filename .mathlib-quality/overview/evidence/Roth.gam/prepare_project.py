from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
code=(D/'disk-prefix.lean.txt').read_text()+'''
namespace Gam230Project
noncomputable def formula (δ n m : ℝ) : ℝ := (m - 4 * (1 + 3 * δ) * n * √m) / 2
theorem bridge (δ : ℝ) (n m : ℕ) : Roth.gam δ n m = formula δ n m := rfl
theorem unfolding (δ : ℝ) (n m : ℕ) : Roth.gam δ n m = ((m : ℝ) - Roth.lam δ n m) / 2 := rfl
theorem normalForm (δ : ℝ) (n m : ℕ) :
    Roth.gam δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √(m : ℝ) := by
  dsimp only [Roth.gam, Roth.lam]
  ring
theorem divideSub (δ : ℝ) (n m : ℕ) :
    Roth.gam δ n m = m / 2 - Roth.lam δ n m / 2 := sub_div _ _ _
theorem continuousDelta (n m : ℕ) : Continuous (fun δ ↦ Roth.gam δ n m) := by
  unfold Roth.gam Roth.lam
  fun_prop
#print axioms formula
#print axioms bridge
#print axioms unfolding
#print axioms normalForm
#print axioms divideSub
#print axioms continuousDelta
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.gam
  Lean.logInfo m!"GAM230_UNIVERSE_PARAMETERS: {ci.levelParams}"
  Lean.logInfo m!"GAM230_REAL_FORMULA_BRIDGE: PASS"
end Gam230Project
'''
assert max(map(len,code.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print(code)
