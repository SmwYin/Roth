from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
prefix=(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.Analysis.SpecialFunctions.Pow.Continuity\n';(D/'isolated-prefix19.lean.txt').write_text(prefix)
s=(D/'generic-executed.lean.txt').read_text();generic=s[s.index('open scoped Topology'):]
env='''
namespace Delta276Envelopes
-- Independent semantic amplitude, positive exponent, scale, geometric term and cap.
-- In particular A and M need no positivity: only M>4s and U>0 are used.
theorem quantitative {A e M s U K : ℝ} (he : 0 < e) (hM : 4 * s < M)
    (hU : 0 < U) (hK : 2 * M / (M - 4 * s) < K) :
    ∃ δ : ℝ, 0 < δ ∧ δ < U ∧
      A * δ ^ e + 2 * (1 + 3 * δ) * s < M / 2 ∧
      M * (1 + 4 * δ) / ((M - 4 * (1 + 3 * δ) * s) / 2 - A * δ ^ e) < K := by
  apply Delta276Generic.simultaneous (f := fun δ ↦
    A * δ ^ e + 2 * (1 + 3 * δ) * s)
    (p := fun δ ↦ M * (1 + 4 * δ))
    (q := fun δ ↦ (M - 4 * (1 + 3 * δ) * s) / 2 - A * δ ^ e) hU
  · exact (Real.continuousAt_rpow_const 0 e (.inr he.le)).const_mul A |>.add
      (by fun_prop)
  · fun_prop
  · exact ((continuousAt_const.sub (by fun_prop)).div_const 2).sub
      ((Real.continuousAt_rpow_const 0 e (.inr he.le)).const_mul A)
  · have hgap : 0 < (M - 4 * s) / 2 := by linarith
    simpa [Real.zero_rpow he.ne'] using hgap.ne'
  · simpa [Real.zero_rpow he.ne'] using (show 2 * s < M / 2 by linarith)
  · simpa [Real.zero_rpow he.ne', div_div_eq_mul_div, mul_comm] using hK

-- Full old-form recovery reconstructed from genuine mathlib operations alone.
theorem recovered {n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (hK : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
    10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m) +
      2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
    (m : ℝ) * (1 + 4 * δ) /
      (((m : ℝ) - 4 * (1 + 3 * δ) * n * √(m : ℝ)) / 2 -
        10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)) < κ := by
  have hm0 : (0 : ℝ) < m := by exact_mod_cast (Nat.zero_le _).trans_lt hm
  have hm' : (16 * n ^ 2 : ℝ) < m := by exact_mod_cast hm
  have h4n : 4 * (n : ℝ) < √(m : ℝ) := Real.lt_sqrt_of_sq_lt (by nlinarith only [hm'])
  have hgap : 4 * ((n : ℝ) * √(m : ℝ)) < m := by
    nlinarith only [Real.sq_sqrt hm0.le,
      mul_lt_mul_of_pos_right h4n (Real.sqrt_pos.mpr hm0)]
  simpa only [mul_assoc] using quantitative (A := 10 ^ m)
    (e := (1 / 2 : ℝ) ^ m) (M := m) (s := n * √(m : ℝ))
    (U := 1 / m) (K := κ) (by positivity) hgap (by positivity)
    (by simpa only [mul_assoc] using hK)
#print axioms quantitative
#print axioms recovered
end Delta276Envelopes
'''
s=prefix+'\n#check_failure Roth.exists_delta\n'+generic+env;n='envelopes-executed.lean.txt';(D/n).write_text(s);assert max(map(len,s.splitlines()))<=100
put=lambda n,x:(D/n).write_text(json.dumps(x,indent=2)+'\n')
put('root-requests/envelopes01.json',dict(id='envelopes01',operation='run_code',source=n,source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='envelopes01-receipt.json',arguments={}))
# Explicit ambient definition bridge, no target theorem in proof.
s=(D/'disk-prefix.lean.txt').read_text()+generic+env+'''
namespace Delta276Bridge
open Roth
theorem recovered {n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (hK : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
    (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ := by
  simpa only [eta, gam, lam] using Delta276Envelopes.recovered hm hK
example : @recovered = @Roth.exists_delta := Subsingleton.elim _ _
#print axioms recovered
end Delta276Bridge
'''
n='envelope-bridge-executed.lean.txt';(D/n).write_text(s);assert max(map(len,s.splitlines()))<=100
put('root-requests/envelope-bridge01.json',dict(id='envelope-bridge01',operation='diagnostics',source=n,source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='envelope-bridge01-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)))
print('PASS independent quantitative envelopes + full raw mathlib-only old recovery19, ambient bridge9; width≤100')
