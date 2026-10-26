from pathlib import Path
import json, hashlib, subprocess, shutil
b=Path(__file__).resolve().parent;r=Path('/Users/ramin/LEAN/Roth')
def save(n,o):(b/n).write_text(json.dumps(o,indent=2)+'\n')
manifest=json.loads((r/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
checks=[]
for name,data in manifest['sources_and_pins'].items():
 p=r/name;h=hashlib.sha256(p.read_bytes()).hexdigest();checks.append({'path':name,'sha256':h,'expected':data['sha256'],'matches':h==data['sha256']})
assert len(checks)==17 and all(x['matches'] for x in checks)
save('source-check.json',{'checks':checks,'matched':17})
shutil.copyfile(r/'.mathlib-quality/overview/evidence/shared/input-manifest.json',b/'input-manifest.json')
shutil.copyfile(r/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',b/'baseline-build.txt')
# Exact commands, outputs and exit statuses. All-source audit excludes generated evidence.
commands=[['rg','-n','hasseDeriv_C|\\.hasseDeriv_C','Roth','Roth.lean'],['rg','-n','hasseDeriv.*\\(C |hasseDeriv.*C |hasseCoeff_eq_zero_iff|C_apply','Roth','Roth.lean'],['rg','-n','MvPolynomial\\.hasseDeriv_C|theorem hasseDeriv_C|lemma hasseDeriv_C|def hasseDeriv',' .lake/packages/mathlib/Mathlib'.strip()],['rg','-n','HasseSchmidt|Hasse.Schmidt|higherDeriv|higher_deriv|hasseDeriv|derivation_C',' .lake/packages/mathlib/Mathlib/Algebra/MvPolynomial'.strip()],['rg','-n','lsum_single|coeffLinearEquiv|theorem C_apply|def C |def monomial',' .lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean'.strip(),'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/LinearAlgebra.lean'],['rg','-n','Hasse|\\\\Delta|derivative','.mathlib-quality/references/clean.tex']]
receipts=[]
for cmd in commands:
 p=subprocess.run(cmd,cwd=r,text=True,capture_output=True);receipts.append({'request':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
save('grep-receipts.json',receipts)
def excerpt(src,start,end,dst):
 lines=(r/src).read_text().splitlines();(b/dst).write_text('\n'.join(lines[start-1:end])+'\n')
excerpt('Roth/HasseDeriv.lean',46,129,'target-excerpt.lean')
excerpt('Roth/Taylor.lean',120,130,'caller-excerpt.lean')
excerpt('.mathlib-quality/references/clean.tex',117,157,'local-reference-excerpt.tex')
excerpt('.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean',54,147,'mathlib-hasse-excerpt.lean')
excerpt('.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean',83,142,'mathlib-C-excerpt.lean')
excerpt('.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean',88,137,'mathlib-lsum-excerpt.lean')
save('worker-source-manifest.json',{'files':[{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted((r/'Roth').glob('*.lean'))]+[{'path':'Roth.lean','sha256':hashlib.sha256((r/'Roth.lean').read_bytes()).hexdigest(),'bytes':(r/'Roth.lean').stat().st_size}]})
print('17/17 baseline hashes match; source receipts saved')
