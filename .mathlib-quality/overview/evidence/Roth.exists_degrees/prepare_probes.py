from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
pre=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.exists_degrees\n'
s=pre+(D/'generic-body.lean.txt').read_text().replace('namespace Degrees278Generic','namespace Degrees278Composition').replace('end Degrees278Generic','end Degrees278Composition')
s=s.replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
s+='''
#check @exists_nat_gt
#check @Finset.le_sup'
#check @Nat.le_ceil
#check @Nat.ceil_lt_add_one
#check @Nat.ceil_natCast
#check @tendsto_nat_ceil_mul_div_atTop
#print axioms Degrees278Composition.balanced
#print axioms Degrees278Composition.separated
'''
def req(n,s,op='run_code'):
 assert max(map(len,s.splitlines()))<=100
 p=D/(n+'-executed.lean.txt');p.write_text(s)
 (D/'root-requests'/(n+'01.json')).write_text(json.dumps(dict(id=n+'01',operation=op,source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=n+'01-receipt.json',arguments={}if op=='run_code'else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
req('composition',s)
s=pre+'''
namespace Degrees278Edges
-- At zero error, the strict upper bound contradicts the base coordinate itself.
theorem zero_error : ¬ ∃ r : Fin 1 → ℕ, (r 0 : ℝ) < (1 + (0 : ℝ)) * r 0 := by
  simp
-- Nonnegative weights are insufficient: zero makes the strict upper bound impossible.
theorem zero_weight (ε : ℝ) :
    ¬ ∃ r : Fin 1 → ℕ, (r 0 : ℝ) * 0 < (1 + ε) * (r 0 * 0) := by
  simp
-- A growth margin of one cannot enforce strict adjacent separation when δ=1.
theorem no_margin : ¬ ∃ r : Fin 2 → ℕ,
    (r 0 : ℝ) ≤ r 1 ∧ (r 1 : ℝ) / 1 < r 0 := by
  simp
-- The original denominator assumption cannot simply become q>=1.
theorem denominator_one (δ : ℝ) : ¬ ∃ r : Fin 1 → ℕ,
    (r 0 : ℝ) * Real.log (1 : ℕ) < (1 + δ / 10) * (r 0 * Real.log (1 : ℕ)) := by
  simp
#print axioms zero_error
#print axioms zero_weight
#print axioms no_margin
#print axioms denominator_one
end Degrees278Edges
'''
req('edges',s)
print('Composition absence probe/building-block checks and edges ready')
