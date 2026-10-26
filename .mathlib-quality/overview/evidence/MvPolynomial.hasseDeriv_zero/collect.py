import pathlib,json,hashlib,subprocess
base=pathlib.Path(__file__).resolve().parent
root=pathlib.Path('/Users/ramin/LEAN/Roth')
shared=root/'.mathlib-quality/overview/evidence/shared'
manifest=json.loads((shared/'input-manifest.json').read_text())
checks={p:hashlib.sha256((root/p).read_bytes()).hexdigest()==v['sha256'] for p,v in manifest['sources_and_pins'].items()}
assert len(checks)==17 and all(checks.values())
(base/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(base/'baseline-build.txt').write_bytes((shared/'baseline-build.txt').read_bytes())
(base/'source-check.json').write_text(json.dumps({'matches':checks,'count':17},indent=2)+'\n')
corrected=json.loads(pathlib.Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
target=next(x for x in corrected if x['name']=='MvPolynomial.hasseDeriv_zero')
(base/'corrected-target.json').write_text(json.dumps(target,indent=2)+'\n')
slices=[('target-excerpt.lean','Roth/HasseDeriv.lean',45,122),('caller-excerpt.lean','Roth/Index.lean',85,107),('local-reference-excerpt.tex','.mathlib-quality/references/clean.tex',117,155),('mathlib-hasse-excerpt.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean',40,88),('mathlib-reconstruct-excerpt.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean',960,969),('mathlib-lsum-excerpt.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean',87,133)]
for dest,src,a,b in slices:
 (base/dest).write_text(''.join((root/src).read_text().splitlines(keepends=True)[a-1:b]))
commands=[['rg','-n','hasseDeriv_zero_apply|hasseDeriv_zero', 'Roth','Roth.lean'],['rg','-n','hasseDeriv_zero_apply|hasseDeriv_zero\'|hasseDeriv_zero',' .lake/packages/mathlib/Mathlib'.strip()],['rg','-n','support_sum_monomial_coeff|sum_coeff_single|lsum_symm_apply|lsum_comp_lsingle|coeffLinearEquiv','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra'],['rg','-n','hasseDeriv 0|hasseDeriv.*zero|coeff_hasseDeriv.*hasseCoeff','Roth']]
receipts=[]
for cmd in commands:
 r=subprocess.run(cmd,cwd=root,text=True,capture_output=True)
 receipts.append({'request':cmd,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
(base/'grep-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
print('PASS: 17 source/pin hashes matched; exact slices and searches saved.')
