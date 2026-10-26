from pathlib import Path
import json,hashlib,shutil
root=Path.cwd(); out=Path(__file__).resolve().parent
shared=root/'.mathlib-quality/overview/evidence/shared'
base=json.load(open(shared/'input-manifest.json'))
checks=[]
for name,info in base['sources_and_pins'].items():
    actual=hashlib.sha256((root/name).read_bytes()).hexdigest()
    checks.append(dict(file=name,expected=info['sha256'],actual=actual,match=actual==info['sha256']))
assert all(x['match'] for x in checks)
json.dump(dict(passed=len(checks),total=len(checks),checks=checks),open(out/'baseline-hash-verification.json','w'),indent=2)
for name in ['input-manifest.json','baseline-build.txt']: shutil.copyfile(shared/name,out/name)
specs=[('.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Derivation.lean',20,48,'mkDerivation-excerpt.lean'),('.lake/packages/mathlib/Mathlib/LinearAlgebra/BilinearMap.lean',496,514,'lsmul-excerpt.lean'),('Roth/HasseDeriv.lean',45,75,'target-excerpt.lean'),('.mathlib-quality/references/clean.tex',119,155,'local-reference-excerpt.tex'),('.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean',70,96,'mvpolynomial-excerpt.lean'),('.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean',45,68,'polynomial-hasse-excerpt.lean'),('.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean',45,73,'pderiv-excerpt.lean'),('.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean',86,119,'lsum-excerpt.lean'),('.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Module.lean',59,85,'coeffLinearEquiv-excerpt.lean'),('.lake/packages/mathlib/Mathlib/RingTheory/LaurentSeries.lean',105,129,'laurent-hasse-excerpt.lean')]
identities=[]
for name,a,b,dest in specs:
    p=root/name; lines=p.read_text().splitlines()
    (out/dest).write_text('\n'.join(lines[a-1:b])+'\n')
    identities.append(dict(file=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),excerpt=dest,start=a,end=b))
json.dump(identities,open(out/'source-identities.json','w'),indent=2)
print('17/17 baseline hashes match; source excerpts and identities saved')
