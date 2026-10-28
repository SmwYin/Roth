from pathlib import Path
import subprocess,json,hashlib
D=Path(__file__).resolve().parent;R=Path.cwd()
queries={
'current':['rg','-n',r'Roth[.]lam|def lam\b|def rothLambda\b|4 \* \(1 \+ 3 \*',' .lake/packages/mathlib/Mathlib'.strip()],
'standard':['rg','-n','[Rr]oth|[Ss]iegel|auxiliary polynomial','.lake/packages/mathlib/Mathlib/NumberTheory','.lake/packages/mathlib/Mathlib/Combinatorics/Additive'],
'abstract':['rg','-n',r'def sqrt\b|theorem sqrt_mul|theorem mul_self_sqrt|theorem sq_sqrt|continuous_sqrt|continuous_mul_left','.lake/packages/mathlib/Mathlib/Analysis/Real/Sqrt.lean','.lake/packages/mathlib/Mathlib/Topology/Algebra/Ring/Real.lean']}
for form,args in queries.items():
 z=subprocess.run(args,text=True,capture_output=True);(D/('search-'+form+'-rg.json')).write_text(json.dumps(dict(form=form,method='rg',request=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr),ensure_ascii=False,indent=2)+'\n')
paths=['Mathlib/Analysis/Real/Sqrt.lean','Mathlib/Combinatorics/Additive/AP/Three/Defs.lean','Mathlib/NumberTheory/DiophantineApproximation/Basic.lean']
mi=[]
for p in paths:
 f=R/'.lake/packages/mathlib'/p
 if f.exists():
  b=f.read_bytes();n='mathlib-'+p.replace('/','-')+'.txt';(D/n).write_bytes(b);mi.append(dict(path=p,archive=n,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b)))
(D/'mathlib-inputs.json').write_text(json.dumps(mi,indent=2)+'\n')
code=(D/'isolated-prefix.lean.txt').read_text()+'''
namespace Lam229Isolated
#check_failure Roth.lam
#check @Real.sqrt
#check @Real.sqrt_mul
#check @Real.sq_sqrt
#check @HMul.hMul
#check @HAdd.hAdd
#check @Nat.cast
#synth Mul ℝ
#synth Add ℝ
#synth NatCast ℝ
#check_failure (inferInstance : CoeFun ℝ (fun _ : ℝ ↦ ℝ → ℝ))
noncomputable def formula (δ n m : ℝ) : ℝ := 4 * (1 + 3 * δ) * n * √m
noncomputable def scaled (a x : ℝ) : ℝ := 4 * a * √x
def algebraic {R : Type*} [Semiring R] (s : R → R) (δ n m : R) : R :=
  4 * (1 + 3 * δ) * n * s m
theorem originalForm (δ : ℝ) (n m : ℕ) :
    formula δ n m = 4 * (1 + 3 * δ) * n * √(m : ℝ) := rfl
theorem abstractBridge (δ n m : ℝ) : formula δ n m = scaled ((1 + 3 * δ) * n) m := by
  dsimp only [formula, scaled]
  ring
theorem expressionBridge (δ n m : ℝ) : formula δ n m = algebraic Real.sqrt δ n m := rfl
theorem normalForm (δ n m : ℝ) : formula δ n m = (4 + 12 * δ) * n * √m := by
  dsimp only [formula]
  ring
theorem continuousDelta (n m : ℝ) : Continuous (fun δ ↦ formula δ n m) := by
  unfold formula
  fun_prop
theorem scaleCount {a x D N : ℝ} (ha : 0 < a) (hx : 0 < x)
    (hD : D ≤ 2 * √x / scaled a x * N) : a * D ≤ N / 2 := by
  refine (mul_le_mul_of_nonneg_left hD ha.le).trans_eq ?_
  dsimp only [scaled]
  field_simp [ha.ne', (Real.sqrt_pos.mpr hx).ne']
  ring
theorem deltaMatters : formula 0 1 1 ≠ formula 1 1 1 := by norm_num [formula]
theorem degreeMatters : formula 0 1 1 ≠ formula 0 2 1 := by norm_num [formula]
theorem dimensionMatters : formula 0 1 0 ≠ formula 0 1 1 := by norm_num [formula]
theorem signGuard : formula (-1) 1 1 < 0 := by norm_num [formula]
theorem nonnegative (δ : ℝ) (n m : ℕ) (hδ : 0 ≤ δ) : 0 ≤ formula δ n m := by
  unfold formula
  positivity
#print axioms formula
#print axioms scaled
#print axioms algebraic
#print axioms originalForm
#print axioms abstractBridge
#print axioms expressionBridge
#print axioms normalForm
#print axioms continuousDelta
#print axioms scaleCount
#print axioms deltaMatters
#print axioms degreeMatters
#print axioms dimensionMatters
#print axioms signGuard
#print axioms nonnegative
end Lam229Isolated
'''
assert max(map(len,code.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(code)
print(code)
