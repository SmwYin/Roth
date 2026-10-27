from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.abs_coeff_hasseDeriv_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
for src,dst in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/src,D/dst)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[88]['name']==N
out('canonical-order.json',dict(index=89,total=293,entry=order[88],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths=['Algebra/Polynomial/HasseDeriv.lean','Analysis/Normed/Group/Seminorm.lean','Data/Nat/Choose/Bounds.lean','Algebra/MvPolynomial/Degrees.lean','Analysis/Normed/Group/Basic.lean']
m=[]
for i,p in enumerate(paths):
 f=R/'.lake/packages/mathlib/Mathlib'/p;dest=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'hasseDeriv.*coeff|coeff.*hasseDeriv|abs_coeff_hasseDeriv_le',['.lake/packages/mathlib/Mathlib']),('literature',r'hasseDeriv|Hasse|divided derivative',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/RingTheory/LaurentSeries.lean']),('abstract',r'norm_nsmul_le|map_nsmul_le|scalarBound|choose_le_two_pow|map_add_le_add',['.lake/packages/mathlib/Mathlib/Algebra','.lake/packages/mathlib/Mathlib/Analysis','.lake/packages/mathlib/Mathlib/Data/Nat/Choose/Bounds.lean']),('full-name',r'\babs_coeff_hasseDeriv_le\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\babs_coeff_hasseDeriv_le\b',['Roth','Roth.lean']),('inline',r'hasseCoeff_le_two_pow|coeff_hasseDeriv|normOne_hasseDeriv_le',['Roth','Roth.lean']),('local-literature',r'abc|Hasse|binomial|coefficient',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in list(range(436,500))+list(range(1437,1449))+list(range(1536,1568)))+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,lines=[[437,500],[1438,1449],[1537,1568]]))
f=[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))];assert len(f)==12;out('formal-search.json',f)
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());out('accepted-yes-grouping.json',dict(source_sha256=sha(R/'.mathlib-quality/overview/progress.json'),completed_count=len(p['completed_declarations']),accepted_yes=[x for x in p['completed_declarations'] if x['verdict'].startswith('YES')]))
print('Prepared fresh hashes/source/search evidence')

for p in ['Roth/MainLemma.lean','Roth/HasseDeriv.lean']:
 shutil.copyfile(R/p,D/(Path(p).stem+'-module.lean.txt'))
