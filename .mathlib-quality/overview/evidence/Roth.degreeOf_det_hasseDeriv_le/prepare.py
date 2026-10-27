from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.degreeOf_det_hasseDeriv_le'
def put(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rg(tag,args):
 c=['rg']+args;p=subprocess.run(c,cwd=R,text=True,capture_output=True);put('rg-'+tag+'.json',{'command':c,'cwd':str(R),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
for p,n in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/Separation.lean','source-callers.lean.txt'),('Roth/HasseDeriv.lean','source-hasse.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/p,D/n)
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for p,x in b['sources_and_pins'].items():
 f=R/p;inputs.append({'path':p,'sha256':sha(f),'bytes':f.stat().st_size,'baseline_sha256':x['sha256'],'match':sha(f)==x['sha256']})
put('inputs.json',inputs);put('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
files=['Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean','Mathlib/LinearAlgebra/Matrix/Polynomial.lean','Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean']
ms=[]
for i,p in enumerate(files):
 f=R/'.lake/packages/mathlib'/p;a=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/a);ms.append({'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'archive':a})
put('mathlib-inputs.json',ms)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-entry.json',order[98]);put('canonical-order.json',{'index':99,'entry':order[98],'source_sha256':sha(R/'.mathlib-quality/overview/declaration-order.json')});put('canonical-snapshot.json',order)
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());cs=progress['completed_declarations'];put('accepted-yes-grouping.json',{'completed_count':len(cs),'accepted_yes':[x for x in cs if x['verdict'].startswith('YES') and x['acceptance']=='PASS']})
rg('current',['-n','degreeOf.*det|det.*degreeOf','.lake/packages/mathlib/Mathlib'])
rg('literature',['-n','natDegree.*det|det.*natDegree|column.*degree|degree.*column','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix'])
rg('abstract',['-n','degreeOf_(sum|prod|C_mul)_le|det_apply|det_le|natDegree_det_X_add_C_le','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Degrees.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix'])
rg('full-name',['-n',r'Roth\.degreeOf_det_hasseDeriv_le|theorem degreeOf_det_hasseDeriv_le|lemma degreeOf_det_hasseDeriv_le','.lake/packages/mathlib/Mathlib'])
rg('callers',['-n',r'\bdegreeOf_det_hasseDeriv_le\b','Roth','Roth.lean'])
rg('inline',['-n',r'degreeOf.*det|det.*degreeOf|degreeOf_sum_le|degreeOf_prod_le|natDegree.*det|det.*natDegree','Roth','Roth.lean'])
rg('local-literature',['-n',r'degree at most|degree.*determinant|determinant.*degree|degree.*r_j|degree.*r_',' .mathlib-quality/references/clean.tex'.strip()])
f=R/'.mathlib-quality/references/clean.tex';lines=f.read_text().splitlines();hits=[i for i,l in enumerate(lines) if 'Since $F$ is a determinant' in l or 'Since \\(F' in l];put('local-literature-source.json',{'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'summary':'End proof Lemma2: determinant entries have partial degree at most r_j, determinant partial degree at most l r_j. Lemma3 handles a distinct coefficient bound.'})
# Exact local source excerpt anchored by visible determinant-degree sentence.
ix=[i for i,l in enumerate(lines) if 'determinant' in l and ('degree' in l or 'matrix' in l)];selected=set()
for i in ix:
 if 400<i<1000:selected.update(range(max(0,i-3),min(len(lines),i+5)))
(D/'local-literature-excerpt.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in sorted(selected))+'\n')
put('formal-search.json',[json.loads((D/f'search-{i:02}.json').read_text()) for i in range(1,13)])
shutil.copyfile('/private/tmp/roth-overview/det-degree-reviewer-git.json',D/'reviewer-git.json')
