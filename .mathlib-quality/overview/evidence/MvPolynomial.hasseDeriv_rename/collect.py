from pathlib import Path
import json,hashlib,subprocess,shutil
b=Path(__file__).resolve().parent;r=Path('/Users/ramin/LEAN/Roth')
def save(n,o):(b/n).write_text(json.dumps(o,indent=2)+'\n')
manifest=json.loads((r/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());checks=[]
for n,e in manifest['sources_and_pins'].items():
 p=r/n;h=hashlib.sha256(p.read_bytes()).hexdigest();checks.append(dict(path=n,sha256=h,expected=e['sha256'],matches=h==e['sha256']))
assert len(checks)==17 and all(x['matches'] for x in checks)
save('source-check.json',dict(checks=checks,matched=17))
for n in ['input-manifest.json','baseline-build.txt']:shutil.copyfile(r/'.mathlib-quality/overview/evidence/shared'/n,b/n)
commands=[['rg','-n','hasseDeriv_rename|\\.hasseDeriv_rename','Roth','Roth.lean'],['rg','-n','hasseDeriv.*rename|rename.*hasseDeriv|prod_mapDomain_index_inj|mapDomain_tsub','Roth','Roth.lean'],['rg','-n','MvPolynomial\\.hasseDeriv_rename|theorem hasseDeriv_rename|lemma hasseDeriv_rename|def hasseDeriv','.lake/packages/mathlib/Mathlib'],['rg','-n','HasseSchmidt|Hasse.Schmidt|higherDeriv|higher_deriv|hasseDeriv|pderiv_rename','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial'],['rg','-n','prod_mapDomain_index_inj|mapDomain_apply_of_injective|mapDomain_tsub','.lake/packages/mathlib/Mathlib/Data/Finsupp'],['rg','-n','lsum|mapDomain','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean'],['rg','-n','coeff_rename_mapDomain|rename_monomial','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Rename.lean'],['rg','-n','Hasse|\\Delta|rename|renam|embedded','.mathlib-quality/references/clean.tex']]
receipts=[]
for c in commands:
 p=subprocess.run(c,cwd=r,text=True,capture_output=True);receipts.append(dict(request=c,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
save('grep-receipts.json',receipts)
def excerpt(src,start,end,dst):
 (b/dst).write_text('\n'.join((r/src).read_text().splitlines()[start-1:end])+'\n')
excerpt('Roth/HasseDeriv.lean',1,155,'target-excerpt.lean')
excerpt('Roth/Separation.lean',129,167,'caller-Separation-146.lean')
excerpt('.mathlib-quality/references/clean.tex',117,157,'local-reference-definition.tex')
excerpt('.mathlib-quality/references/clean.tex',395,435,'local-reference-caller.tex')
excerpt('.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean',143,154,'mathlib-pderiv-excerpt.lean')
excerpt('.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean',407,440,'mathlib-mapDomain-excerpt.lean')
excerpt('.lake/packages/mathlib/Mathlib/Data/Finsupp/Order.lean',295,305,'mathlib-tsub-excerpt.lean')
files=sorted((r/'Roth').glob('*.lean'))+[r/'Roth.lean']
save('worker-source-manifest.json',dict(files=[dict(path=str(p.relative_to(r)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in files]))
refs=[r/'.mathlib-quality/references/clean.tex',r/'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Rename.lean',r/'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean',r/'.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean',r/'.lake/packages/mathlib/Mathlib/Data/Finsupp/Order.lean']
save('reference-source-manifest.json',dict(files=[dict(path=str(p.relative_to(r)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in refs]))
print('17/17 baseline matches; fresh searches/source/caller receipts saved')
