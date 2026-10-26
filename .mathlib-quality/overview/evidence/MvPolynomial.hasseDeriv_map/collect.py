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
commands=[['rg','-n','hasseDeriv_map|\\.hasseDeriv_map','Roth','Roth.lean'],['rg','-n','hasseDeriv.*map|map.*hasseDeriv|coeff_map|coeff_hasseDeriv','Roth','Roth.lean'],['rg','-n','MvPolynomial\\.hasseDeriv_map|theorem hasseDeriv_map|lemma hasseDeriv_map|def hasseDeriv','.lake/packages/mathlib/Mathlib'],['rg','-n','HasseSchmidt|Hasse.Schmidt|higherDeriv|higher_deriv|hasseDeriv|pderiv_map','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial'],['rg','-n','mapDomain_mapRange|mapRange_smul|mapRange_finsetSum|mapRange.addMonoidHom','.lake/packages/mathlib/Mathlib/Data/Finsupp'],['rg','-n','lsum|mapRange|map_nsmul','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean'],['rg','-n','def map|coeff_map|coeff_addMonoidAlgebraMap|map_monomial','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean'],['rg','-n','Hasse|\\\\Delta|derivative','.mathlib-quality/references/clean.tex']]
receipts=[]
for c in commands:
 p=subprocess.run(c,cwd=r,text=True,capture_output=True);receipts.append(dict(request=c,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
save('grep-receipts.json',receipts)
def excerpt(src,start,end,dst):
 (b/dst).write_text('\n'.join((r/src).read_text().splitlines()[start-1:end])+'\n')
excerpt('Roth/HasseDeriv.lean',46,139,'target-excerpt.lean')
for f,a,z in [('Separation',511,537),('Theta',511,529),('Theta',555,590),('MainLemma',394,413),('MainLemma',478,496)]:excerpt('Roth/'+f+'.lean',a,z,'caller-'+f+'-'+str(a)+'.lean')
excerpt('.mathlib-quality/references/clean.tex',117,157,'local-reference-excerpt.tex')
excerpt('.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean',126,136,'mathlib-hasse-excerpt.lean')
excerpt('.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean',325,390,'mathlib-map-excerpt.lean')
excerpt('.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean',450,480,'mathlib-mapDomain-excerpt.lean')
files=sorted((r/'Roth').glob('*.lean'))+[r/'Roth.lean']
save('worker-source-manifest.json',dict(files=[dict(path=str(p.relative_to(r)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in files]))
refs=[r/'.mathlib-quality/references/clean.tex',r/'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean',r/'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean',r/'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean',r/'.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean',r/'.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean',r/'.lake/packages/mathlib/Mathlib/Data/Finsupp/SMulWithZero.lean']
save('reference-source-manifest.json',dict(files=[dict(path=str(p.relative_to(r)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size) for p in refs]))
print('17/17 baseline hashes match; exact search and caller receipts saved')
