import pathlib,json,hashlib,subprocess
base=pathlib.Path(__file__).resolve().parent
root=pathlib.Path('/Users/ramin/LEAN/Roth')
commands=[['rg','-n','hasseCoeff_eq_prod|\\.hasseCoeff_eq_prod','Roth','Roth.lean'],['rg','-n','prod_fintype|prod_of_support_subset|choose_zero_right','Roth'],['rg','-n','hasseCoeff_eq_prod|hasseCoeff|theorem prod_fintype|prod_of_support_subset','.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean'],['rg','-n','MvPolynomial\\.hasseCoeff_eq_prod|hasseCoeff_eq_prod','.lake/packages/mathlib/Mathlib']]
receipts=[]
for cmd in commands:
 p=subprocess.run(cmd,cwd=root,text=True,capture_output=True)
 receipts.append({'command':cmd,'cwd':str(root),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'untruncated':True})
(base/'grep-receipts.json').write_text(json.dumps(receipts,indent=2))
paths=['Roth/HasseDeriv.lean','Roth/Taylor.lean','Roth/GenWronskian.lean','.mathlib-quality/references/clean.tex','.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Data/Nat/Choose/Basic.lean','lean-toolchain','lake-manifest.json','lakefile.toml']
(base/'source-evidence.json').write_text(json.dumps({'sources':{p:{'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest(),'bytes':(root/p).stat().st_size} for p in paths},'caller_audit':{'target':'MvPolynomial.hasseCoeff_eq_prod','total_explicit_invocations':1,'same_file':1,'excluding_declaring_file':0,'external_files':0,'callers':[{'name':'MvPolynomial.hasseCoeff_le_two_pow','declaration_line':276,'usage_line':278,'file':'Roth/HasseDeriv.lean','pattern':'rw [hasseCoeff_eq_prod, ← Finset.prod_pow_eq_pow_sum]'}],'exact_inline_duplicates':[],'related_generic_routes':['Roth/HasseDeriv.lean:159–163 (support-superset binomial products)','Roth/Taylor.lean:212 (power product)','Roth/GenWronskian.lean:62 (power product)'],'scope':'All 14 production Lean sources, target short/qualified/dot variants and generic factor/support patterns; explicit source callers only, no opaque metaprogram/kernel dependency closure claim.'}},indent=2))
for name,a,b,out in [('Roth/HasseDeriv.lean',100,109,'target-excerpt.lean'),('.lake/packages/mathlib/Mathlib/Algebra/BigOperators/Finsupp/Basic.lean',40,67,'mathlib-prod-excerpt.lean'),('.lake/packages/mathlib/Mathlib/Data/Nat/Choose/Basic.lean',50,59,'mathlib-choose-excerpt.lean'),('Roth/HasseDeriv.lean',272,282,'caller-excerpt.lean'),('.mathlib-quality/references/clean.tex',119,155,'local-reference-excerpt.tex')]:
 (base/out).write_text('\n'.join((root/name).read_text().splitlines()[a-1:b])+'\n')
(base/'input-manifest.json').write_bytes((root/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_bytes())
(base/'baseline-build.txt').write_bytes((root/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_bytes())
