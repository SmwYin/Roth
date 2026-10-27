from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.diag_eq_sum'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
for src,dst in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/src,D/dst)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[90]['name']==N
out('canonical-order.json',dict(index=91,total=293,entry=order[90],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths=['Algebra/MvPolynomial/Eval.lean','Algebra/Polynomial/Basic.lean','Algebra/MvPolynomial/CommRing.lean','Algebra/BigOperators/Group/Finset/Basic.lean','Data/Finsupp/Defs.lean','Algebra/Polynomial/AlgebraMap.lean']
m=[]
for i,p in enumerate(paths):
 f=R/'.lake/packages/mathlib/Mathlib'/p
 if not f.exists():continue
 dest=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'diag_eq_sum|diag.*sum|aeval.*monomial|monomial.*degree',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),('literature',r'eval₂_eq|aeval_def|degree_apply|C_mul_X_pow_eq_monomial|prod_pow_eq_pow_sum',['.lake/packages/mathlib/Mathlib']),('abstract',r'mapDomain.*single|mapDomain.*sum|lift.*monomial|sum.*mapDomain',['.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']),('full-name',r'\bdiag_eq_sum\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bdiag_eq_sum\b',['Roth','Roth.lean']),('inline',r'prod_pow_eq_pow_sum|eval₂_eq|C_mul_X_pow_eq_monomial|diag_eq_sum',['Roth','Roth.lean']),('local-literature',r'diagonal|replace|same variable|number of terms|coefficients',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();hits=[i for i,s in enumerate(lines) if 'same variable' in s or 'replace' in s and 'x_' in s];sel=set()
for i in hits:
 sel.update(range(max(0,i-5),min(len(lines),i+13)))
(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in sorted(sel))+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,line_numbers=[i+1 for i in sorted(sel)]))
f=[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))];assert len(f)==12;out('formal-search.json',f)
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());out('accepted-yes-grouping.json',dict(source_sha256=sha(R/'.mathlib-quality/overview/progress.json'),completed_count=len(p['completed_declarations']),accepted_yes=[x for x in p['completed_declarations'] if x['verdict'].startswith('YES')]))
print('Fresh preparation complete')
