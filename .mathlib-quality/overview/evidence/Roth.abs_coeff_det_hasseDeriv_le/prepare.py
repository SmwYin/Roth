from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.abs_coeff_det_hasseDeriv_le'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rg(tag,args):
 c=['rg']+args;p=subprocess.run(c,cwd=R,text=True,capture_output=True);put('rg-'+tag+'.json',{'command':c,'cwd':str(R),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
for p,n in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/Theta.lean','source-callers.lean.txt'),('Roth/HasseDeriv.lean','source-hasse.lean.txt'),('Roth/Box.lean','source-box.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/p,D/n)
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for p,x in b['sources_and_pins'].items():
 f=R/p;inputs.append({'path':p,'sha256':sha(f),'bytes':f.stat().st_size,'baseline_sha256':x['sha256'],'match':sha(f)==x['sha256']})
put('inputs.json',inputs);put('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
files=['Mathlib/Analysis/Polynomial/Norm.lean','Mathlib/RingTheory/Polynomial/GaussNorm.lean','Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean','Mathlib/Algebra/Polynomial/HasseDeriv.lean','Mathlib/Analysis/Normed/Unbundled/RingSeminorm.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean']
ms=[]
for i,p in enumerate(files):
 f=R/'.lake/packages/mathlib'/p;a=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/a);ms.append({'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'archive':a})
put('mathlib-inputs.json',ms)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-entry.json',order[99]);put('canonical-order.json',{'index':100,'entry':order[99],'source_sha256':sha(R/'.mathlib-quality/overview/declaration-order.json')});put('canonical-snapshot.json',order)
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());cs=p['completed_declarations'];put('accepted-yes-grouping.json',{'completed_count':len(cs),'accepted_yes':[x for x in cs if x['verdict'].startswith('YES') and x['acceptance']=='PASS']})
rg('current',['-n','coeff.*det|det.*coeff|hasseDeriv.*le|le.*hasseDeriv','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix'])
rg('literature',['-n','length|l.1|height|det_le|norm_det|det.*norm','.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean','.lake/packages/mathlib/Mathlib/Analysis/Matrix'])
rg('abstract',['-n','RingSeminorm|gaussNorm_mul|single_eval_le_sum|le_sum_of_subadditive|le_prod_of_submultiplicative_of_nonneg','.lake/packages/mathlib/Mathlib/Analysis/Normed/Unbundled/RingSeminorm.lean','.lake/packages/mathlib/Mathlib/RingTheory/Polynomial/GaussNorm.lean','.lake/packages/mathlib/Mathlib/Algebra/Order'])
rg('full-name',['-n',r'Roth\.abs_coeff_det_hasseDeriv_le|theorem abs_coeff_det_hasseDeriv_le|lemma abs_coeff_det_hasseDeriv_le','.lake/packages/mathlib/Mathlib'])
rg('callers',['-n',r'\babs_coeff_det_hasseDeriv_le\b','Roth','Roth.lean'])
rg('inline',['-n',r'coeff.*det|det.*coeff|normOne_det_le|normOne_hasseDeriv_le','Roth','Roth.lean'])
rg('local-literature',['-n',r'roth:lem3|triangle inequality|Pad the monomial|submultiplicativity|abc\(F\)','.mathlib-quality/references/clean.tex'])
f=R/'.mathlib-quality/references/clean.tex';ls=f.read_text().splitlines();(D/'local-literature-excerpt.txt').write_text('\n'.join(f'{i+1}: {ls[i]}' for i in range(437,500))+'\n')
put('local-literature-source.json',{'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'summary':'Section3 Lemma3 lines438–500: Hasse determinant coefficient estimate via coefficient length, binomial bounds, support box and Leibniz expansion; source formula N^l l! (B2^S)^l.'})
formal=[]
for meth in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  x=json.loads((D/f'{meth}-{form}.json').read_text());formal.append({'tool':meth,'form':form,**x})
put('formal-search.json',formal)
shutil.copyfile('/private/tmp/roth-overview/abs-hasse-reviewer-git.json',D/'reviewer-git.json')
put('callers.json',{'named_count':1,'explicit_occurrences':1,'external_to_file_count':1,'callers':[{'file':'Roth/Theta.lean','line':475,'name':'Roth.index_det_le','usage':'abs_coeff_det_hasseDeriv_le _ R (r := fun _ ↦ r₁) … hR.2.2 d','refactor':'Replace with generic seminorm coefficient bound specialized to intSize; omit redundant nonnegative-B argument; preserve constant-r simplification into lem6M.'}],'inline_audit':'No separate full determinant coefficient estimate rederived inline. normOne_det_le and degreeOf_det_hasseDeriv_le are distinct supporting bounds; Theta hFcoef directly calls target.','native_audit':{'status':'pending'}})
