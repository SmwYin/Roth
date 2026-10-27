from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.eval_diag'
def put(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rg(tag,args):
 c=['rg']+args;p=subprocess.run(c,cwd=R,text=True,capture_output=True);put('rg-'+tag+'.json',{'command':c,'cwd':str(R),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
for p,n in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/MainLemma.lean','source-inline.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]: shutil.copyfile(R/p,D/n)
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for p,x in b['sources_and_pins'].items():
 f=R/p;inputs.append({'path':p,'sha256':sha(f),'bytes':f.stat().st_size,'baseline_sha256':x['sha256'],'match':sha(f)==x['sha256']})
put('inputs.json',inputs);put('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
files=['Mathlib/Algebra/MvPolynomial/Eval.lean','Mathlib/Algebra/Polynomial/Eval/Defs.lean','Mathlib/Algebra/Polynomial/AlgebraMap.lean']
ms=[]
for i,p in enumerate(files):
 f=R/'.lake/packages/mathlib'/p;a=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/a);ms.append({'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'archive':a})
put('mathlib-inputs.json',ms)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-entry.json',order[93]);put('canonical-order.json',{'index':94,'entry':order[93],'source_sha256':sha(R/'.mathlib-quality/overview/declaration-order.json')});put('canonical-snapshot.json',order)
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());cs=progress['completed_declarations'];put('accepted-yes-grouping.json',{'completed_count':len(cs),'accepted_yes':[x for x in cs if x['verdict'].startswith('YES') and x['acceptance']=='PASS'],'parent_diag':[x for x in cs if x['declaration']=='Roth.diag']})
rg('current',['-n','eval.*diag|diag.*eval|eval_toMvPolynomial','.lake/packages/mathlib/Mathlib'])
rg('literature',['-n','hom_eval₂|eval₂_comp_left|eval₂RingHom_comp_C|eval_map','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Eval/Defs.lean'])
rg('abstract',['-n','comp_aeval|map_aeval|aeval_def|aeval_X','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/AlgebraMap.lean'])
rg('full-name',['-n',r'Roth\.eval_diag|theorem eval_diag|lemma eval_diag','.lake/packages/mathlib/Mathlib'])
rg('callers',['-n',r'\beval_diag\b','Roth','Roth.lean'])
rg('inline',['-n',r'eval_diag|eval_map|aeval.*fun _|diag.*eval|eval.*diag|comp_aeval_apply','Roth','Roth.lean'])
rg('local-literature',['-n',r'diagonal|point evaluation|same variable|x_1 =|zero when','.mathlib-quality/references/clean.tex'])
f=R/'.mathlib-quality/references/clean.tex';put('local-literature-source.json',{'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'line_numbers':[1515,1519,1562],'summary':'Lemma9 identifies vanishing after all variables equal alpha and separates differentiation, diagonal substitution, point evaluation.'})
lines=f.read_text().splitlines();(D/'local-literature-excerpt.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(1502,1522))+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in range(1560,1569))+'\n')
forms=['current']*3+['current']*3+['current']*3+['current']*3
f=[]
for i in range(1,13):
 x=json.loads((D/f'search-{i:02}.json').read_text());x['form']=['current','standard','abstract'][(i-1)%3];f.append(x)
f.append(json.loads((D/'search-13.json').read_text())|{'form':'standard','retry':'rate-limit'})
f.append(json.loads((D/'search-14.json').read_text())|{'form':'standard','retry':'successful-correction'})
put('formal-search.json',f)
