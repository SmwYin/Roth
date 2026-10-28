from pathlib import Path
import json,subprocess,hashlib,re
D=Path(__file__).resolve().parent;R=Path.cwd()
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for form,pat in [('current',r'eta_lt_gam|eta.*gam|2.*4.*div'),('standard',r'lt_sub_iff_add_lt|add_lt_iff_lt_sub|sub_pos'),('abstract',r'theorem (sub_div|div_sub_div_same)|mul_div_cancel_left₀|lt_div_iff₀')]:
 args=['rg','-n',pat,'.lake/packages/mathlib/Mathlib/Algebra'];z=subprocess.run(args,text=True,capture_output=True);put('search-'+form+'-rg.json',dict(form=form,method='rg',command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
mods=['Mathlib/Algebra/Field/Basic.lean','Mathlib/Algebra/Order/Group/Unbundled/Basic.lean','Mathlib/Algebra/GroupWithZero/Units/Basic.lean']
xs=[]
for mod in mods:
 p=R/'.lake/packages/mathlib'/mod;a='mathlib-'+mod.replace('/','-')+'.txt';(D/a).write_bytes(p.read_bytes());xs.append(dict(path=mod,archive=a,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
put('mathlib-inputs.json',xs)
code=(D/'isolated-prefix.lean.txt').read_text()+'''
#check_failure Roth.eta_lt_gam_iff
#check_failure Roth.eta
#check_failure Roth.gam
#check_failure Roth.lam
namespace Gap235Isolated
#check @lt_sub_iff_add_lt
#check @sub_div
#check @div_sub_div_same
#check @mul_div_cancel_left₀
#check @lt_div_iff₀
-- Exactly three existing theorem calls; no arithmetic normalization tactic.
theorem three_calls (a b c d : ℝ) (hd : d ≠ 0) :
    a + b < c / d ↔ a < (c - d * b) / d := by
  rw [← div_sub_div_same, mul_div_cancel_left₀ b hd, lt_sub_iff_add_lt]
theorem three_term (a b c d : ℝ) (hd : d ≠ 0) :
    a + b < c / d ↔ a < (c - d * b) / d :=
  Eq.ndrec (motive := fun z ↦ a + b < c / d ↔ a < z)
    (Eq.ndrec (motive := fun z ↦ a + b < c / d ↔ a < c / d - z)
      (show a + b < c / d ↔ a < c / d - b from lt_sub_iff_add_lt.symm)
      (mul_div_cancel_left₀ b hd).symm) (div_sub_div_same c (d * b) d)
-- Removing coefficient normalization gives an existing abstract translation law.
theorem additive {G : Type*} [AddGroup G] [LT G] [AddRightStrictMono G] (a b c : G) :
    a + b < c ↔ a < c - b := lt_sub_iff_add_lt.symm
-- This is a new generic proof with arithmetic normalization, not an existing replacement.
theorem generic {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (a b c : K) : a + 2 * b < c / 2 ↔ a < (c - 4 * b) / 2 := by
  grind
-- Actual original arithmetic with every project definition expanded.
theorem expanded (δ : ℝ) (n m : ℕ) :
    10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m) + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔
      10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m) <
        ((m : ℝ) - 4 * (1 + 3 * δ) * n * √(m : ℝ)) / 2 := by
  fail_if_success
    exact three_calls _ _ _ (2 : ℝ) two_ne_zero
  fail_if_success
    exact lt_sub_iff_add_lt.symm
  grind
-- Strictness is preserved; no positivity of a, b, c or the original δ is used.
theorem weak (a b c : ℝ) : a + 2 * b ≤ c / 2 ↔ a ≤ (c - 4 * b) / 2 := by
  constructor <;> intro h <;> linarith
-- The coefficient relation matters: replacing 4 with 2 is false.
theorem false_coefficient : ¬ ((0 : ℝ) + 2 * 1 < (3 : ℝ) / 2 ↔ 0 < ((3 : ℝ) - 2 * 1) / 2) := by
  norm_num
-- Division by a negative d does not invalidate translation once no scaling step is used.
theorem negative_d (a b c : ℝ) : a + b < c / (-1) ↔ a < (c - (-1) * b) / (-1) :=
  three_calls a b c (-1) (by norm_num)
end Gap235Isolated
#print axioms Gap235Isolated.three_term
#print axioms Gap235Isolated.three_calls
#print axioms Gap235Isolated.additive
#print axioms Gap235Isolated.generic
#print axioms Gap235Isolated.expanded
#print axioms Gap235Isolated.weak
#print axioms Gap235Isolated.false_coefficient
#print axioms Gap235Isolated.negative_d
'''
assert max(map(len,code.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(code)
print(code)
