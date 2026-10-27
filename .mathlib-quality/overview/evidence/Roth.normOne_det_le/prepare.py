from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.normOne_det_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
for src,dst in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/src,D/dst)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[87]['name']==N
out('canonical-order.json',dict(index=88,total=293,entry=order[87],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths=['LinearAlgebra/Matrix/AbsoluteValue.lean','LinearAlgebra/Matrix/Determinant/Basic.lean','Analysis/Normed/Unbundled/RingSeminorm.lean','Algebra/Order/BigOperators/Ring/Finset.lean','Algebra/Order/BigOperators/Group/Finset.lean']
m=[]
for i,p in enumerate(paths):
 f=R/'.lake/packages/mathlib/Mathlib'/p;dest=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'normOne_det_le|norm_one.*det',['.lake/packages/mathlib/Mathlib']),('literature',r'norm_det|det_norm|det_le|seminorm.*det|det.*seminorm',['.lake/packages/mathlib/Mathlib']),('abstract',r'le_prod_of_submultiplicative|le_sum_of_subadditive|structure RingSeminorm|seminorm_one_eq_one',['.lake/packages/mathlib/Mathlib/Algebra/Order/BigOperators','.lake/packages/mathlib/Mathlib/Analysis/Normed/Unbundled/RingSeminorm.lean']),('full-name',r'\bnormOne_det_le\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_det_le\b',['Roth','Roth.lean']),('inline',r'det_apply|factorial.*\^|normOne.*det',['Roth','Roth.lean']),('local-literature',r'factorial|det|norm|triangle inequality',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,497))+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,lines=[437,497]))
f=[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))];assert len(f)==12;out('formal-search.json',f)
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());out('accepted-yes-grouping.json',dict(source_sha256=sha(R/'.mathlib-quality/overview/progress.json'),completed_count=len(p['completed_declarations']),accepted_yes=[x for x in p['completed_declarations'] if x['verdict'].startswith('YES')]))
print('Prepared fresh hashes/source/search evidence')
