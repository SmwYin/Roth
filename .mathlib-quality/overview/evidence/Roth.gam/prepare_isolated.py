from pathlib import Path
D=Path(__file__).resolve().parent
code=(D/'isolated-prefix.lean.txt').read_text()+'''
namespace Gam230Isolated
#check_failure Roth.gam
#check_failure Roth.lam
#check @Real.sqrt
#check @sub_div
#check @Continuous.sub
#check @Continuous.div_const
#check @HSub.hSub
#check @HDiv.hDiv
#check @Nat.cast
#synth Sub ℝ
#synth Div ℝ
#synth NatCast ℝ
#check_failure (inferInstance : CoeFun ℝ (fun _ : ℝ ↦ ℝ → ℝ))
noncomputable def formula (δ n m : ℝ) : ℝ := (m - 4 * (1 + 3 * δ) * n * √m) / 2
def halfGap {K : Type*} [Field K] (x l : K) : K := (x - l) / 2
def algebraic {K : Type*} [Field K] (s : K → K) (δ n m : K) : K :=
  (m - 4 * (1 + 3 * δ) * n * s m) / 2
theorem originalForm (δ : ℝ) (n m : ℕ) :
    formula δ n m = ((m : ℝ) - 4 * (1 + 3 * δ) * n * √(m : ℝ)) / 2 := rfl
theorem abstractBridge (δ n m : ℝ) :
    formula δ n m = halfGap m (4 * (1 + 3 * δ) * n * √m) := rfl
theorem expressionBridge (δ n m : ℝ) : formula δ n m = algebraic Real.sqrt δ n m := rfl
theorem normalForm (δ n m : ℝ) : formula δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √m := by
  dsimp only [formula]
  ring
theorem gapComparison (e x l : ℝ) : e + l / 2 < x / 2 ↔ e < halfGap x l := by
  dsimp only [halfGap]
  constructor <;> intro h <;> linarith only [h]
theorem arbitraryCutoff {P : ℝ → Prop} {c g : ℝ} (hg : g ≤ c)
    (hP : ∀ x, x < c → P x) : ∀ x, x < g → P x :=
  fun x hx ↦ hP x (hx.trans_le hg)
theorem continuousDelta (n m : ℝ) : Continuous (fun δ ↦ formula δ n m) := by
  unfold formula
  fun_prop
theorem deltaMatters : formula 0 1 1 ≠ formula 1 1 1 := by norm_num [formula]
theorem degreeMatters : formula 0 1 1 ≠ formula 0 2 1 := by norm_num [formula]
theorem dimensionMatters : formula 0 0 0 ≠ formula 0 0 1 := by norm_num [formula]
theorem signGuard : formula 0 1 1 < 0 := by norm_num [formula]
theorem positiveGap {δ : ℝ} {n m : ℕ}
    (h : 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2) : 0 < formula δ n m := by
  dsimp only [formula]
  linarith only [h]
'''
import re
code+='\n'.join('#print axioms '+n for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',code,re.M))+'\nend Gam230Isolated\n'
assert max(map(len,code.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(code)
print(code)
