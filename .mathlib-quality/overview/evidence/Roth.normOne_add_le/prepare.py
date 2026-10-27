from pathlib import Path
import json,hashlib,shutil,subprocess
D=Path(__file__).resolve().parent; R=Path('/Users/ramin/LEAN/Roth'); N='Roth.normOne_add_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in base['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=base['baseline_commit']))
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
paths={'source-module.lean.txt':'Roth/CoeffNorm.lean','mathlib-finsupp-basic.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','mathlib-finsupp-order.lean.txt':'.lake/packages/mathlib/Mathlib/Data/Finsupp/Order.lean','mathlib-lp-finsupp.lean.txt':'.lake/packages/mathlib/Mathlib/Analysis/Normed/Lp/Finsupp.lean','mathlib-norm.lean.txt':'.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','mathlib-norm-group.lean.txt':'.lake/packages/mathlib/Mathlib/Analysis/Normed/Group/Basic.lean','mathlib-monoid-algebra.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Defs.lean'}
m=[]
for dest,p in paths.items():
 f=R/p;shutil.copyfile(f,D/dest)
 if p.startswith('.lake/'):m.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'normOne_add_le|norm_one_add',['.lake/packages/mathlib/Mathlib']),('literature',r'norm_add_le|sum.*norm|length|add_le',['.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','.lake/packages/mathlib/Mathlib/Analysis/Normed/Lp/Finsupp.lean']),('abstract',r'sum.*add|add.*sum|sum_le_sum|subadditive',['.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Order.lean']),('full-name',r'\bnormOne_add_le\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_add_le\b',['Roth','Roth.lean']),('inline',r'normOne.*\+|normOne_add|abs_add_le|support_add',['Roth','Roth.lean']),('local-literature',r'triangle inequality|norm|\\\|f\+kg',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
local=R/'.mathlib-quality/references/clean.tex';lines=local.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,497))+'\n');out('local-literature-source.json',dict(path=str(local.relative_to(R)),sha256=sha(local),bytes=local.stat().st_size,lines=[437,497]))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[81]['name']==N;out('canonical-order.json',dict(index=82,total=len(order),entry=order[81],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('formal-search.json',[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))])
# Fresh execution requested; an old audit's canonical name array is only source scaffolding.
old=Path('/private/tmp/roth-overview/assess/Roth.normOne_zero/native-full-audit-executed.lean.txt').read_text()
audit=old[old.index('run_cmd do'):old.rindex('end MvPolynomial.NormZeroConsumers')].replace('Roth.normOne_zero','Roth.normOne_add_le').replace('ZERO_','ADD_')
consumer='''namespace MvPolynomial.NormAddConsumers
open Roth
variable {σ : Type*}
theorem sumBound {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, normOne (f i) :=
  Finset.le_sum_of_subadditive normOne normOne_zero.le NormAddAssessment.direct s f
#print axioms sumBound
'''
(D/'requested-consumers.lean.txt').write_text(consumer+audit+'end MvPolynomial.NormAddConsumers\n')
imports=Path('/private/tmp/roth-overview/diag-raw-executed.lean.txt').read_text().split('#check_failure')[0]
target=(D/'requested-target.lean.txt').read_text();generic=target[target.index('theorem generic'):target.index('#print axioms direct')].replace('[PartialOrder N]','[Preorder N]')
raw=imports+'''#check_failure Roth.normOne_add_le
namespace NormAddRaw
open MvPolynomial
variable {σ : Type*}
noncomputable def replacement (P : MvPolynomial σ ℤ) : ℝ :=
  ∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|
'''+generic+'''theorem direct (P Q : MvPolynomial σ ℤ) :
    replacement (P + Q) ≤ replacement P + replacement Q := by
  exact generic (fun _ (z : ℤ) ↦ |(z : ℝ)|) (by simp)
    (fun _ a b ↦ by simpa using abs_add_le (a : ℝ) (b : ℝ)) P.coeff Q.coeff
theorem finiteTriangle {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    replacement (∑ i ∈ s, f i) ≤ ∑ i ∈ s, replacement (f i) :=
  Finset.le_sum_of_subadditive replacement (by simp [replacement]) direct s f
#check @Finsupp.sum_of_support_subset
#check @Finset.sum_le_sum
#check @abs_add_le
#print axioms generic
#print axioms direct
#print axioms finiteTriangle
end NormAddRaw
'''
(D/'requested-raw.lean.txt').write_text(raw)
print('Fresh82 inputs/searches prepared; native gates pending.')
