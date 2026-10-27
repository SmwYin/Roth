from pathlib import Path
import json,hashlib,shutil,subprocess
D=Path(__file__).resolve().parent; R=Path('/Users/ramin/LEAN/Roth'); N='Roth.normOne_neg'
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
searches=[('current',r'normOne_neg|norm_one_neg',['.lake/packages/mathlib/Mathlib']),('literature',r'norm_neg|sum.*norm|length|neg',['.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','.lake/packages/mathlib/Mathlib/Analysis/Normed/Lp/Finsupp.lean']),('abstract',r'prod_neg_index|sum_neg_index|support_neg|coeff_neg',['.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Order.lean']),('full-name',r'\bnormOne_neg\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_neg\b',['Roth','Roth.lean']),('inline',r'normOne.*\(-|normOne_neg|abs_neg|support_neg',['Roth','Roth.lean']),('local-literature',r'signs|norm|absolute value',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
local=R/'.mathlib-quality/references/clean.tex';lines=local.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,497))+'\n');out('local-literature-source.json',dict(path=str(local.relative_to(R)),sha256=sha(local),bytes=local.stat().st_size,lines=[437,497]))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[82]['name']==N;out('canonical-order.json',dict(index=83,total=len(order),entry=order[82],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('formal-search.json',[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))])
print('Fresh83 source receipts prepared')
