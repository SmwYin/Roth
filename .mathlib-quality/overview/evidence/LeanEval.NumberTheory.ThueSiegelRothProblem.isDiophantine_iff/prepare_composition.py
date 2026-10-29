from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
s=(D/'modern-executed.lean.txt').read_text();prefix=s[:s.index('#check_failure')]
c=prefix+'''#check_failure LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff
#check_failure Roth.approxSet
namespace Equivalence292Composition
open Real
'''+s[s.index('def UniformBound'):s.index('example (_x')]+s[s.index('def pairSet'):s.index('theorem pairSet_den')]+'''-- These probes precede every authored equivalence/helper theorem.
example (x : ℝ) (hx : Irrational x) : True := by
  fail_if_success
    have : UniformBound 2 x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ 2 := by
      exact?
  fail_if_success
    have : UniformBound 2 x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ 2 := by
      simp only [UniformBound, pairSet]
  exact True.intro
example (t x : ℝ) : True := by
  fail_if_success
    have : UniformBound t x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t := by
      exact?
  fail_if_success
    have : UniformBound t x ↔
        Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t := by
      exact?
  trivial
#check @Set.exists_min_image
#check @LiouvilleWith.frequently_lt_rpow_neg
#check @Set.Infinite.sdiff
#check @Real.tendsto_rpow_atTop
end Equivalence292Composition
'''
# Ensure hx is actually mentioned without supplying the desired equivalence.
c=c.replace('  exact True.intro','  have : x ≠ 0 := hx.ne_int 0\n  exact True.intro')
# Instead omit unused hypothesis warning by syntactic use in a true proposition.
c=c.replace('  have : x ≠ 0 := hx.ne_int 0\n  exact True.intro','  exact (show True from (fun (_ : Irrational x) ↦ True.intro) hx)')
assert max(map(len,c.splitlines()))<=100
(D/'composition-executed.lean.txt').write_text(c.rstrip()+'\n')
r=dict(id='composition01',operation='run_code',source='composition-executed.lean.txt',source_sha256=hashlib.sha256((D/'composition-executed.lean.txt').read_bytes()).hexdigest(),receipt='composition01-receipt.json',arguments={})
(D/'root-requests/composition01.json').write_text(json.dumps(r,indent=2)+'\n')
print(c)
