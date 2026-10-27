import pathlib,json,hashlib,subprocess,shutil,re
r=pathlib.Path('/Users/ramin/LEAN/Roth');b=pathlib.Path(__file__).parent
def dump(n,x):(b/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def hashed(p):
 v=p.read_bytes();return {'path':str(p.relative_to(r)) if p.is_relative_to(r) else str(p),'sha256':hashlib.sha256(v).hexdigest(),'bytes':len(v)}
def run(n,args):
 z=subprocess.run(args,cwd=r,text=True,capture_output=True);dump(n,{'request':{'argv':args,'cwd':str(r)},'result':{'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr}})
for n in ['input-manifest.json','baseline-build.txt']:shutil.copyfile(r/'.mathlib-quality/overview/evidence/shared'/n,b/n)
m=json.loads((b/'input-manifest.json').read_text())
checks=[{'path':p,'expected':e['sha256'],'observed':hashed(r/p)['sha256']} for p,e in m['sources_and_pins'].items()]
assert len(checks)==17 and all(x['expected']==x['observed'] for x in checks);dump('baseline-fresh-check.json',checks)
dump('source-hashes.json',[hashed(r/p) for p in ['Roth/HasseDeriv.lean','Roth/Taylor.lean','Roth/MainLemma.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Degrees.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean']])
dump('reference-hashes.json',[hashed(pathlib.Path(p)) for p in ['/Users/ramin/.codex/skills/mathlib-quality/SKILL.md','/Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlib-search.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlibable-verdicts.md','/Users/ramin/.codex/skills/mathlib-quality/references/generalisation-patterns.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlib-review-stages.md',str(r/'.mathlib-quality/references/clean.tex')]])
run('full-name.json',['rg','-n',r'\bhasseDeriv_eq_zero_of_degreeOf_lt\b','.lake/packages/mathlib/Mathlib'])
run('rg-current.json',['rg','-n',r'hasseDeriv_eq_zero|hasseDeriv.*degreeOf|degreeOf.*hasseDeriv','.lake/packages/mathlib/Mathlib'])
run('rg-literature.json',['rg','-n',r'hasseDeriv_eq_zero|natDegree_hasseDeriv|choose_eq_zero','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean'])
run('rg-abstract.json',['rg','-n',r'notMem_support_of_degreeOf_lt|coeff_eq_zero|ext_iff|support.*(subset|disjoint)|restrictSupport','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Data/Finsupp'])
run('callers.json',['rg','-n',r'\bhasseDeriv_eq_zero_of_degreeOf_lt\b','Roth','Roth.lean'])
run('inline-audit.json',['rg','-n',r'notMem_support_of_degreeOf_lt|hasseDeriv.*= 0|coeff_hasseDeriv|hasseCoeff_eq_zero_iff','Roth'])
run('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-5','--format=%H %an %ad %s','--date=short','--','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/Polynomial/HasseDeriv.lean'])
run('literature-local.json',['sed','-n','115,153p;1500,1517p','.mathlib-quality/references/clean.tex'])
for p,lo,hi,dest in [('Roth/HasseDeriv.lean',216,223,'target-source.lean.txt'),('Roth/Taylor.lean',168,174,'caller-taylor-degree.lean.txt'),('Roth/Taylor.lean',192,213,'caller-taylor-box.lean.txt'),('Roth/MainLemma.lean',411,425,'caller-mainlemma.lean.txt')]:
 (b/dest).write_text(''.join((r/p).read_text().splitlines(keepends=True)[lo-1:hi]))
body=''.join((r/'Roth/HasseDeriv.lean').read_text().splitlines(keepends=True)[220:223])
dump('q8-diagnostic.json',{'body':body,'named_object':'hasseDeriv','identifier_occurrences':len(re.findall(r'\bhasseDeriv\b',body)),'named_substring_lines':sum('hasseDeriv' in x for x in body.splitlines()),'subsequent_named_substring_occurrences':0,'fired':True,'abstract_premise':'forall e, Q.coeff e = w e * P.coeff (e+d); forall e, P.coeff (e+d)=0','consequence':'Generic shifted coefficient maps vanish on polynomials whose support avoids the upper cone of d. Coordinate-degree corollary remains canonical API.'})
print('Fresh 17 source/pin hashes match successful reusable baseline. Source/caller/search/reference evidence saved.')
