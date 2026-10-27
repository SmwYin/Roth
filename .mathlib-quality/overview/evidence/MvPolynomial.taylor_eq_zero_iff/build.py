from pathlib import Path
import hashlib,json,shutil,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='MvPolynomial.taylor_eq_zero_iff'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for label,pattern,paths in [
 ('current',r'taylor_eq_zero|taylor.*zero|zero.*taylor',['.lake/packages/mathlib/Mathlib/Algebra']),
 ('literature',r'leadingCoeff_taylor|taylor_eq_zero|comp_X_add_C_eq_zero_iff',['.lake/packages/mathlib/Mathlib/Algebra/Polynomial']),
 ('abstract',r'map_eq_zero_iff|eq_iff.|ker_eq_bot|comp_aeval|aeval_X_left',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Algebra/Equiv.lean']),
 ('full-name',r'MvPolynomial\.taylor_eq_zero_iff|\b(theorem|lemma)\s+taylor_eq_zero_iff\b',['.lake/packages/mathlib/Mathlib']),
 ('callers',r'\btaylor_eq_zero_iff\b',['Roth.lean','Roth']),
 ('inline',r'taylor.*zero|zero.*taylor|map_eq_zero_iff|eq_iff.',['Roth.lean','Roth']),
 ('local-literature',r'Taylor|P_\\alpha|x_i-\\alpha_i|x_j - \\alpha_j',['.mathlib-quality/references/clean.tex'])]:
 args=['rg','-n',pattern,*paths];r=subprocess.run(args,cwd=R,capture_output=True);out('rg-'+label+'.json',dict(args=args,exit_code=r.returncode,stdout=r.stdout.decode(),stderr=r.stderr.decode()))
manifest=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for p,x in manifest['sources_and_pins'].items():
 f=R/p;inputs.append(dict(path=p,sha256=sha(f),baseline_sha256=x['sha256'],bytes=f.stat().st_size,match=sha(f)==x['sha256']))
assert len(inputs)==17 and all(x['match'] for x in inputs)
out('inputs.json',inputs);out('input-hash-check.json',dict(all_pass=True,count=17))
shutil.copy(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
entries=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());out('canonical-entry.json',next(x for x in entries if x['name']==N))
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
if isinstance(order,dict):order=order.get('declarations',order.get('order',[]))
out('order-entry.json',next(x for x in order if x['name']==N))
links={'Roth/Taylor.lean':'Taylor-module.lean.txt','Roth/Index.lean':'Index-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean':'MvPolynomial-Eval-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean':'MvPolynomial-Basic-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean':'Polynomial-Taylor-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/AlgebraMap.lean':'Polynomial-AlgebraMap-module.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Algebra/Equiv.lean':'AlgEquiv-module.lean.txt','/Users/ramin/.elan/toolchains/leanprover--lean4---v4.34.0/src/lean/Init/Data/Function.lean':'Function-module.lean.txt','.lake/packages/mathlib/Mathlib/RingTheory/AlgebraicIndependent/Basic.lean':'AlgebraicIndependent-Basic.lean.txt','.lake/packages/mathlib/Mathlib/RingTheory/AlgebraicIndependent/Defs.lean':'AlgebraicIndependent-Defs.lean.txt'}
mi=[]
for p,n in links.items():
 shutil.copy(R/p,D/n)
 if p.startswith('.lake'):mi.append(dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size))
out('mathlib-inputs.json',mi)
clean=R/'.mathlib-quality/references/clean.tex';out('local-literature.json',dict(path=str(clean.relative_to(R)),sha256=sha(clean),bytes=clean.stat().st_size,locator='Section4 Index, lines500–548',role='Finite real-coordinate Taylor expansion and undoing the constant shift. Inverse substitution is immediate context, not separately named theorem.'))
(D/'clean-excerpts.tex.txt').write_text('\n'.join(clean.read_text().splitlines()[499:549])+'\n')
