from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.abs_coeff_diag_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
for src,dst in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/MainLemma.lean','source-callers.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/src,D/dst)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[91]['name']==N
out('canonical-order.json',dict(index=92,total=293,entry=order[91],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths=['Algebra/MvPolynomial/Eval.lean','Algebra/Polynomial/Basic.lean','Algebra/Order/BigOperators/Group/Finset.lean','Analysis/Normed/Group/Seminorm.lean','Data/Finset/Card.lean','Algebra/Polynomial/Coeff.lean','Data/Finsupp/Weight.lean','Algebra/BigOperators/Group/Finset/Basic.lean','Algebra/Polynomial/AlgebraMap.lean']
m=[]
for i,p in enumerate(paths):
 f=R/'.lake/packages/mathlib/Mathlib'/p
 if not f.exists():continue
 dest=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'coeff.*(aeval|eval₂)|diag|coeff.*(abs|norm).*le',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial']),('literature',r'abs_sum_le_sum_abs|sum_le_card_nsmul|finsetSum_coeff|coeff_monomial',['.lake/packages/mathlib/Mathlib']),('abstract',r'le_sum_of_subadditive|mapDomain.*(norm|sum)|seminorm.*sum|sum_le.*seminorm',['.lake/packages/mathlib/Mathlib']),('full-name',r'\babs_coeff_diag_le\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\babs_coeff_diag_le\b',['Roth','Roth.lean']),('inline',r'abs_sum_le_sum_abs|sum_le_card_nsmul|diag.*coeff|coeff.*diag',['Roth','Roth.lean']),('local-literature',r'diagonal|replace|same variable|number of terms|coefficients',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();sel=list(range(1438,1467));(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in sel)+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,line_numbers=[i+1 for i in sel]))
out('formal-search.json',[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))])
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());out('accepted-yes-grouping.json',dict(source_sha256=sha(R/'.mathlib-quality/overview/progress.json'),completed_count=len(p['completed_declarations']),accepted_yes=[x for x in p['completed_declarations'] if x['verdict'].startswith('YES')]))
for tag in ['original','raw']:
 for src,dst in [('executed.lean.txt',f'native-{tag}-executed.lean.txt'),('receipt.json',f'native-{tag}-success.json')]:shutil.copyfile(Path('/private/tmp/roth-overview')/f'coeff-diag-{tag}-{src}',D/dst)
print('Fresh17 hash check; source/pin/search archives prepared')
