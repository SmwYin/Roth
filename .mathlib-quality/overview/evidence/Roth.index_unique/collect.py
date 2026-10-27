from pathlib import Path
import subprocess,json,hashlib,shutil,re
D=Path('/private/tmp/roth-overview/assess/Roth.index_unique');R=Path('/Users/ramin/LEAN/Roth')
def j(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,cmd):
 r=subprocess.run(cmd,cwd=R,text=True,capture_output=True);j(n,dict(command=cmd,cwd=str(R),exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));return r
for a,b in [('input-manifest.json','.mathlib-quality/overview/evidence/shared/input-manifest.json'),('baseline-build.txt','.mathlib-quality/overview/evidence/shared/baseline-build.txt'),('canonical-order.json','.mathlib-quality/overview/declaration-order.json'),('progress-snapshot.json','.mathlib-quality/overview/progress.json')]:shutil.copyfile(R/b,D/a)
inputs=[]
for p,v in json.loads((D/'input-manifest.json').read_text())['sources_and_pins'].items():
 f=R/p;inputs.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,expected_sha256=v['sha256'],match=sha(f)==v['sha256']))
assert len(inputs)==17 and all(x['match'] for x in inputs);j('inputs.json',inputs)
order=json.loads((D/'canonical-order.json').read_text());j('canonical-target.json',order[150]);assert order[150]['name']=='Roth.index_unique'
files=sorted({x['file'] for x in order});lex=[]
for p in files:
 s=(R/p).read_text();occ=[dict(line=i,text=l) for i,l in enumerate(s.splitlines(),1) if re.search(r'(?<![\w])(?:Roth\.)?index_unique\b',l)]
 lex.append(dict(path=p,sha256=sha(R/p),occurrences=occ))
j('lexical-enumeration.json',dict(files=lex,proof_body_applications=1,statement_applications=0,applications=1))
run('caller-rg.json',['rg','-n','--no-ignore',r'\bindex_unique\b','Roth','Roth.lean'])
run('caller-git-grep.json',['git','grep','-n','-w','index_unique','--','Roth','Roth.lean'])
run('rg-current.json',['rg','-n',r'index_unique|uniqueAlgEquiv.*rootMultiplicity|rootMultiplicity.*uniqueAlgEquiv','.lake/packages/mathlib/Mathlib'])
run('rg-literature.json',['rg','-n',r'rootMultiplicity_eq_natTrailingDegree|natTrailingDegree_eq_support_min|taylor_apply','.lake/packages/mathlib/Mathlib/Algebra/Polynomial'])
run('rg-abstract.json',['rg','-n',r'infDegree|trailingDegree|natTrailingDegree','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Degree/TrailingDegree.lean'])
run('rg-inline.json',['rg','-n','--no-ignore',r'rootMultiplicity|natTrailingDegree|uniqueAlgEquiv','Roth','Roth.lean'])
run('local-literature-search.json',['rg','-n',r'multiplicity|Taylor|ind\(|index|r_1|r_\{1\}','.mathlib-quality/references/clean.tex'])
s=(R/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-index-excerpt.tex.txt').write_text('\n'.join(s[529:680])+'\n')
source_links={}
for p in ['Roth/Index.lean','Roth/Theta.lean','Roth/Box.lean','Roth/Taylor.lean']:
 n=p.replace('/','-')+'.txt';shutil.copyfile(R/p,D/n);source_links[p]=n
j('source-links.json',source_links)
mathlib=[]
for p in ['Algebra/Polynomial/RingDivision.lean','Algebra/Polynomial/Div.lean','Algebra/Polynomial/Taylor.lean','Algebra/Polynomial/Degree/TrailingDegree.lean','Algebra/MonoidAlgebra/Degree.lean','Algebra/MvPolynomial/Equiv.lean','Data/Finsupp/Weight.lean','Order/ConditionallyCompleteLattice/Finset.lean']:
 p='.lake/packages/mathlib/Mathlib/'+p;f=R/p;n='Mathlib-'+p.split('/Mathlib/')[1].replace('/','-')+'.txt';shutil.copyfile(f,D/n);mathlib.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size,archive=n))
j('mathlib-inputs.json',mathlib)
s=(R/'Roth/Theta.lean').read_text();a=s.index('private lemma index_unique_le_log_div');b=s.index('\nomit [DecidableEq σ] in',a)
j('callers.json',[dict(name='Roth.index_unique_le_log_div',file='Roth/Theta.lean',visibility='private',line=223,application_line=242,kind='proof body',source=s[a:b],plan='Replace rw[index_unique nonzeroProof] by all-polynomial bridge, then use Polynomial.rootMultiplicity_eq_natTrailingDegree in univariate normal form; full actual caller replay proves drop of proof argument.')])
for suffix in ['original-executed.lean.txt','original-audit-receipt.json','original-region.txt','audit-executed.lean.txt','audit-region.txt','target-executed.lean.txt','target-receipt.json']:
 f=Path('/private/tmp/roth-overview/index-unique-'+suffix)
 if f.exists():shutil.copyfile(f,D/('index-unique-'+suffix))
