from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
s=(D/'recovery2-executed.lean.txt').read_text()+'''
namespace Delta276Shape
open Roth
theorem expanded {n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (h47 : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) :
    ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
      eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
      2 * (m : ℝ) * (1 + 4 * δ) /
        (m - 4 * (1 + 3 * δ) * n * √(m : ℝ) - 2 * eta δ m) < κ := by
  obtain ⟨δ, hδ, hcap, hbound, hquot⟩ := Delta276Recovery.recovered hm h47
  refine ⟨δ, hδ, hcap, hbound, ?_⟩
  have heq : gam δ n m - eta δ m =
      ((m : ℝ) - 4 * (1 + 3 * δ) * n * √(m : ℝ) - 2 * eta δ m) / 2 := by
    unfold gam lam
    ring
  rw [heq, div_div_eq_mul_div] at hquot
  convert hquot using 1 <;> ring
-- h47 cannot be discarded: a positive numerator divided by the positive gap is positive.
theorem no_zero_upper_bound : ¬ ∃ δ : ℝ, 0 < δ ∧ δ < 1 ∧
    eta δ 1 < 1 / 2 ∧ (1 + 4 * δ) / (1 / 2 - eta δ 1) < 0 := by
  rintro ⟨δ, hδ, _, he, hq⟩
  exact (div_pos (by linarith) (sub_pos.mpr he)).not_gt hq
-- Denominator nonzero is a substantive generic continuity hypothesis.
example : ((1 : ℝ) / 0) = 0 := by simp
example : (0 : ℝ) ^ (1 : ℝ) = 0 := by norm_num
example : (0 : ℝ) ^ (0 : ℝ) = 1 := by norm_num
#print axioms expanded
#print axioms no_zero_upper_bound
end Delta276Shape
'''
p=D/'shape-executed.lean.txt';p.write_text(s);assert max(map(len,s.splitlines()))<=100
o=dict(id='shape01',operation='diagnostics',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='shape01-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45));(D/'root-requests/shape01.json').write_text(json.dumps(o,indent=2)+'\n');print('Prepared shape01 width PASS')
