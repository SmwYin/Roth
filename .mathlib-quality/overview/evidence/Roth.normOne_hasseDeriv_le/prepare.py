from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.normOne_hasseDeriv_le'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for p,v in b['sources_and_pins'].items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,baseline_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
out('inputs.json',rows);out('input-hash-check.json',dict(all_pass=True,count=17,baseline_commit=b['baseline_commit']))
for src,dst in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/HasseDeriv.lean','HasseDeriv-module.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]:shutil.copyfile(R/src,D/dst)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order[89]['name']==N
out('canonical-order.json',dict(index=90,total=293,entry=order[89],source_sha256=sha(R/'.mathlib-quality/overview/declaration-order.json')))
out('canonical-entry.json',next(x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text()) if x['name']==N))
paths=['Algebra/Polynomial/HasseDeriv.lean','Analysis/Normed/Group/Seminorm.lean','Data/Nat/Choose/Bounds.lean','Data/Finsupp/Basic.lean','Data/Finset/Order.lean','Analysis/Normed/Lp/Finsupp.lean','Analysis/Polynomial/Norm.lean']
m=[]
for i,p in enumerate(paths):
 f=R/'.lake/packages/mathlib/Mathlib'/p
 if not f.exists(): continue
 dest=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/dest);m.append(dict(path=str(f.relative_to(R)),sha256=sha(f),bytes=f.stat().st_size,archive=dest))
out('mathlib-inputs.json',m)
searches=[('current',r'normOne_hasseDeriv_le|hasseDeriv.*norm|norm.*hasseDeriv',['.lake/packages/mathlib/Mathlib']),('literature',r'hasseDeriv|Hasse|divided derivative',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/Analysis/Polynomial']),('abstract',r'sum.*[Ss]eminorm|[Ss]eminorm.*sum|norm_sum_le|sum_le_sum_index|le_sum_of_subadditive|choose_le_two_pow',['.lake/packages/mathlib/Mathlib']),('full-name',r'\bnormOne_hasseDeriv_le\b',['Roth','Roth.lean','.lake/packages/mathlib/Mathlib']),('callers',r'\bnormOne_hasseDeriv_le\b',['Roth','Roth.lean']),('inline',r'hasseCoeff_le_two_pow|hasseDeriv_apply|normOne_hasseDeriv_le',['Roth','Roth.lean']),('local-literature',r'norm|triangle|Hasse|monomial|coefficient',['.mathlib-quality/references/clean.tex'])]
for tag,pat,ps in searches:
 args=['rg','-n',pat,*ps];p=subprocess.run(args,cwd=R,text=True,capture_output=True);out('rg-'+tag+'.json',dict(command=args,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
l=R/'.mathlib-quality/references/clean.tex';lines=l.read_text().splitlines();(D/'local-literature.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(436,500))+'\n');out('local-literature-source.json',dict(path=str(l.relative_to(R)),sha256=sha(l),bytes=l.stat().st_size,lines=[[437,500]]))
f=[json.loads(p.read_text()) for p in sorted(D.glob('lean_*.json'))];assert len(f)==12;out('formal-search.json',f)
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());out('accepted-yes-grouping.json',dict(source_sha256=sha(R/'.mathlib-quality/overview/progress.json'),completed_count=len(p['completed_declarations']),accepted_yes=[x for x in p['completed_declarations'] if x['verdict'].startswith('YES')]))
# Only read-only git history for reviewer selection.
a=['git','log','-8','--format=%h %an %ad %s','--date=short','--','Mathlib/Algebra/Polynomial/HasseDeriv.lean','Mathlib/Analysis/Normed/Lp/Finsupp.lean'];p=subprocess.run(a,cwd=R/'.lake/packages/mathlib',text=True,capture_output=True);out('reviewer-git.json',dict(command=a,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
print('Fresh source/search preparation passed')
