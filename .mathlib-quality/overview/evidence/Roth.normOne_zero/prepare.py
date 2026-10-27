from pathlib import Path
import json,hashlib,shutil,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.normOne_zero'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in base['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=base['baseline_commit']))
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
m=[]
for dest,p in {'source-module.lean.txt':'Roth/CoeffNorm.lean','mathlib-finsupp-basic.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','mathlib-mvpolynomial-basic.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean','mathlib-polynomial-basic.lean.txt':'.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Basic.lean','mathlib-norm.lean.txt':'.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean'}.items():
 f=R/p;shutil.copyfile(f,D/dest)
 if p.startswith('.lake/'):m.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'normOne_zero|norm_one_zero',['.lake/packages/mathlib/Mathlib']),('literature',r'sum_zero_index|supNorm_zero|gaussNorm_zero|norm_zero',['.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Basic.lean','.lake/packages/mathlib/Mathlib/Analysis/Polynomial/Norm.lean','.lake/packages/mathlib/Mathlib/RingTheory/Polynomial/GaussNorm.lean']),('abstract',r'prod_zero_index|sum_zero_index|support_zero',['.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean']),('full-name',r'\bnormOne_zero\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_zero\b',['Roth','Roth.lean']),('inline',r'normOne.*0|simp.*normOne|sum_zero_index|support_zero',['Roth','Roth.lean']),('local-literature',r'zero|norm|triangle inequality',['.mathlib-quality/references/clean.tex'])]
for tag,pat,paths in searches:
 args=['rg','-n',pat,*paths];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
local=R/'.mathlib-quality/references/clean.tex';lines=local.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,497))+'\n');out('local-literature-source.json',dict(path=str(local.relative_to(R)),sha256=sha(local),bytes=local.stat().st_size,lines=[437,497]))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[79]['name']==N;out('canonical-order.json',dict(index=80,total=len(order),entry=order[79],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('formal-search.json',[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))])
x=json.loads((D/'web-5.json').read_text());x['summaries']=['Houben–Streng2022 PDFpage4 lines252–253 defines coefficient absolute sum for complex univariate polynomials, with estimates in Lemma3.4. Search for textual1-norm returned no match because notation is symbolic. This confirms broad coefficient domain, not a separate named zero theorem.'];out('web-5.json',x)
print('Prepared base80; native receipts, report and final gates outstanding.')
