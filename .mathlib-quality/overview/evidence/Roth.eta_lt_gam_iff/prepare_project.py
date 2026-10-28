from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
code=(D/'disk-prefix.lean.txt').read_text()+'''
namespace Gap235Project
open Roth
theorem arbitrary_eta (e δ : ℝ) (n m : ℕ) :
    e + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ e < gam δ n m := by
  grind [gam, lam]
theorem bridge (δ : ℝ) (n m : ℕ) :
    gam δ n m = (m : ℝ) / 2 - 2 * (1 + 3 * δ) * n * √(m : ℝ) := by
  dsimp only [gam, lam]
  ring
theorem original_via_new_generic (δ : ℝ) (n m : ℕ) :
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ eta δ m < gam δ n m :=
  arbitrary_eta (eta δ m) δ n m
theorem explicit_existing_translation (δ : ℝ) (n m : ℕ) :
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔
      eta δ m < (m : ℝ) / 2 - 2 * (1 + 3 * δ) * n * √(m : ℝ) :=
  lt_sub_iff_add_lt.symm
theorem original_normalized (δ : ℝ) (n m : ℕ) :
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ eta δ m < gam δ n m := by
  rw [bridge]
  exact lt_sub_iff_add_lt.symm
end Gap235Project
#print axioms Gap235Project.arbitrary_eta
#print axioms Gap235Project.bridge
#print axioms Gap235Project.original_via_new_generic
#print axioms Gap235Project.explicit_existing_translation
#print axioms Gap235Project.original_normalized
run_cmd Lean.Elab.Command.liftTermElabM do
  let mut todo := [`Roth.eta_lt_gam_iff]
  let mut seen : List Lean.Name := []
  while !todo.isEmpty do
    let n := todo.head!
    todo := todo.tail!
    if !seen.contains n then
      seen := n :: seen
      let ci ← Lean.getConstInfo n
      let deps := (ci.value? (allowOpaque := true)).map (·.getUsedConstants.toList)
      let project := deps.getD [] |>.filter (fun c ↦ c.toString.startsWith "Roth.")
      Lean.logInfo m!"GAP235_PROJECT_BODY_EDGE: {n} -> {project}"
      todo := project ++ todo
  Lean.logInfo "GAP235_PROJECT: arbitrary eta, normalization bridge, explicit existing law verified"
'''
assert max(map(len,code.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print(code)
