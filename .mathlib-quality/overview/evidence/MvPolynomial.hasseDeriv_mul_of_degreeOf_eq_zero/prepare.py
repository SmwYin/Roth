import pathlib,json,hashlib,subprocess,shutil,re
r=pathlib.Path('/Users/ramin/LEAN/Roth');b=pathlib.Path(__file__).parent
def dump(n,x):(b/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def hashed(p):
 v=p.read_bytes();return {'path':str(p.relative_to(r)) if p.is_relative_to(r) else str(p),'sha256':hashlib.sha256(v).hexdigest(),'bytes':len(v)}
def run(n,args):
 z=subprocess.run(args,cwd=r,text=True,capture_output=True);dump(n,{'request':{'argv':args,'cwd':str(r)},'result':{'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr}})
for n in ['input-manifest.json','baseline-build.txt']:shutil.copyfile(r/'.mathlib-quality/overview/evidence/shared'/n,b/n)
m=json.loads((b/'input-manifest.json').read_text());checks=[{'path':p,'expected':e['sha256'],'observed':hashed(r/p)['sha256']} for p,e in m['sources_and_pins'].items()]
assert len(checks)==17 and all(x['expected']==x['observed'] for x in checks);dump('baseline-fresh-check.json',checks)
dump('source-hashes.json',[hashed(r/p) for p in ['Roth/HasseDeriv.lean','Roth/Separation.lean','Roth/Taylor.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Variables.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/Algebra/Algebra/Basic.lean']])
dump('reference-hashes.json',[hashed(pathlib.Path(p)) for p in ['/Users/ramin/.codex/skills/mathlib-quality/SKILL.md','/Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlib-search.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlibable-verdicts.md','/Users/ramin/.codex/skills/mathlib-quality/references/generalisation-patterns.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlib-review-stages.md',str(r/'.mathlib-quality/references/clean.tex')]])
run('full-name.json',['rg','-n',r'\bhasseDeriv_mul_of_degreeOf_eq_zero\b','.lake/packages/mathlib/Mathlib'])
run('rg-current.json',['rg','-n',r'hasseDeriv.*mul|hasseDeriv.*degreeOf|degreeOf.*hasseDeriv','.lake/packages/mathlib/Mathlib'])
run('rg-literature.json',['rg','-n',r'hasseDeriv_mul|Hasse.Schmidt|higher.derivation|pderiv_mul','.lake/packages/mathlib/Mathlib/Algebra','.lake/packages/mathlib/Mathlib/RingTheory'])
run('rg-abstract.json',['rg','-n',r'map_mul_algebraMap|map_smul|linearMap_ext|mem_vars_iff_degreeOf_ne_zero|mem_support_notMem_vars_zero','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Algebra/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/Module/LinearMap/Defs.lean'])
run('callers.json',['rg','-n',r'\bhasseDeriv_mul_of_degreeOf_eq_zero\b','Roth','Roth.lean'])
run('inline-audit.json',['rg','-n',r'hasseDeriv.*mul|mul.*hasseDeriv|hasseDeriv_monomial_mul|degreeOf.*= 0','Roth'])
run('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-7','--format=%H %an %ad %s','--date=short','--','Mathlib/Algebra/MvPolynomial/PDeriv.lean','Mathlib/Algebra/Polynomial/HasseDeriv.lean','Mathlib/Algebra/MvPolynomial/Variables.lean'])
run('literature-local.json',['sed','-n','115,153p;350,435p','.mathlib-quality/references/clean.tex'])
for p,lo,hi,dest in [('Roth/HasseDeriv.lean',225,247,'target-source.lean.txt'),('Roth/Separation.lean',143,166,'caller-separated.lean.txt')]:
 (b/dest).write_text(''.join((r/p).read_text().splitlines(keepends=True)[lo-1:hi]))
body=''.join((r/'Roth/HasseDeriv.lean').read_text().splitlines(keepends=True)[244:247])
dump('q8-diagnostic.json',{'body':body,'named_object':'hasseDeriv','exact_identifier_occurrences':len(re.findall(r'\bhasseDeriv\b',body)),'named_substring_lines':sum('hasseDeriv' in x for x in body.splitlines()),'fired':True,'abstract_premise':'Any R-linear map T commuting with multiplication by all monomials occurring in f commutes with multiplication by f. Hasse needs substantive monomial normalization.','consequence':'Finite sum/map_sum reduction abstracts, but it does not prove the monomial compatibility; no existing abstract R-linear map API supplies it for nonconstant f.'})
print('PASS: fresh 17 baseline inputs and all source/reference/search/caller evidence')
