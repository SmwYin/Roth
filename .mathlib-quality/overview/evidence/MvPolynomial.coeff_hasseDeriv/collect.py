import pathlib,json,hashlib,subprocess,shutil
base=pathlib.Path(__file__).parent
root=pathlib.Path('/Users/ramin/LEAN/Roth')
ev=base/'evidence'
def run(label,args):
 p=subprocess.run(args,cwd=root,capture_output=True,text=True)
 out={'command':args,'cwd':str(root),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 (ev/(label+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 return out
run('branch',['git','branch','--show-current'])
run('full-name-search',['rg','-n','coeff_hasseDeriv|hasseDeriv_coeff', '.lake/packages/mathlib/Mathlib','--glob','*.lean'])
run('grep-current',['rg','-n','hasseDeriv|Hasse|hasse', '.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','--glob','*.lean'])
run('grep-literature',['rg','-n','taylor|Taylor|hasseDeriv_coeff', '.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','--glob','*.lean'])
run('grep-abstract',['rg','-n','lsum_apply|sum_eq_single|comapDomain_apply|mapDomain_apply_of_injective|linearCombination_apply', '.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp','.lake/packages/mathlib/Mathlib/Data/Finsupp','--glob','*.lean'])
run('caller-search',['rg','-n',r'\b(MvPolynomial\.)?coeff_hasseDeriv\b','Roth','Roth.lean','--glob','*.lean'])
run('inline-search',['rg','-n','hasseDeriv|hasseCoeff|tsub_eq_iff_eq_add_of_le|choose_eq_zero_iff','Roth','--glob','*.lean'])
run('local-literature',['rg','-n','Hasse|coefficient identity|surviving monomials|coefficients.*merge', '.mathlib-quality/references/clean.tex'])
manifest=json.loads((root/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
checks=[]
for name,record in manifest['sources_and_pins'].items():
 data=(root/name).read_bytes(); actual=hashlib.sha256(data).hexdigest()
 checks.append({'path':name,'expected':record['sha256'],'actual':actual,'match':actual==record['sha256']})
(ev/'baseline-hash-verification.json').write_text(json.dumps({'checks':checks,'all_match':all(x['match'] for x in checks),'count':len(checks)},indent=2)+'\n')
shutil.copyfile(root/'.mathlib-quality/overview/evidence/shared/input-manifest.json',ev/'input-manifest.json')
source=(root/'Roth/HasseDeriv.lean').read_text().splitlines()
(ev/'target-excerpt.lean').write_text('\n'.join(source[84:102])+'\n')
(ev/'local-manuscript.txt').write_text('\n'.join((root/'.mathlib-quality/references/clean.tex').read_text().splitlines()[119:155])+'\n')
paths=['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Finsupp/LSum.lean','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Module.lean']
(ev/'pinned-sources.json').write_text(json.dumps([{'path':p,'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest(),'bytes':(root/p).stat().st_size} for p in paths],indent=2)+'\n')
print('Collected read-only search and hash evidence; all 17 baseline hashes match:',all(x['match'] for x in checks))
