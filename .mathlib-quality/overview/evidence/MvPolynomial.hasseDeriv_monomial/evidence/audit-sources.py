"""Run from the repository root; read-only baseline and named-use evidence."""
from pathlib import Path
import hashlib,json,re,subprocess
out=Path(__file__).resolve().parent
manifest=json.loads((out/'input-manifest.json').read_text())
checks=[]
for name,info in manifest['sources_and_pins'].items():
    actual=hashlib.sha256(Path(name).read_bytes()).hexdigest()
    checks.append(dict(path=name,expected=info['sha256'],actual=actual,match=actual==info['sha256']))
(out/'baseline-hash-verification.json').write_text(json.dumps(checks,indent=2))
paths=['Mathlib/Algebra/MvPolynomial/Derivation.lean','Mathlib/Algebra/MvPolynomial/Basic.lean','Mathlib/Algebra/MvPolynomial/PDeriv.lean','Mathlib/Algebra/Polynomial/HasseDeriv.lean','Mathlib/LinearAlgebra/Finsupp/LSum.lean','Mathlib/Algebra/MonoidAlgebra/Module.lean']
records=[]
for rel in paths:
 p=Path('.lake/packages/mathlib')/rel
 records.append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(out/'candidate-source-hashes.json').write_text(json.dumps(records,indent=2))
# Production modules only: do not count copied report snippets or scratch probes.
receipts=[]
for query,paths in [(r'(?<![\w.])(?:MvPolynomial\.)?hasseDeriv_monomial\b',['Roth.lean','Roth']), (r'hasseDeriv_monomial|Hasse|hasseDeriv|hyperderiv',['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial']), (r'simp.*hasseDeriv|lsum_single|prod.*choose|choose.*prod',['Roth'])]:
 args=['rg','--pcre2','-n',query,*paths]
 p=subprocess.run(args,capture_output=True,text=True)
 receipts.append(dict(request=args,exit=p.returncode,stdout=p.stdout,stderr=p.stderr))
(out/'reproduction-grep-receipts.json').write_text(json.dumps(receipts,indent=2))
assert len(checks)==17 and all(x['match'] for x in checks)
print('17/17 baseline hashes match; candidate hashes and untruncated grep receipts saved.')
