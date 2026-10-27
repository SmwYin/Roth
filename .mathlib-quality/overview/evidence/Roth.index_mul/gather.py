from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).parent; R=Path('/Users/ramin/LEAN/Roth'); N='Roth.index_mul'
def put(n,o): (D/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def command(n,args):
 x=subprocess.run(args,cwd=R,text=True,capture_output=True); put(n,{'argv':args,'cwd':str(R),'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr}); return x
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',base)
put('inputs.json',[{'path':p,'sha256':sha(R/p),'expected_sha256':q['sha256'],'bytes':(R/p).stat().st_size,'match':sha(R/p)==q['sha256']} for p,q in base['sources_and_pins'].items()])
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[143])
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
paths=['Roth/Index.lean','Roth/Theta.lean','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Basic.lean','.lake/packages/mathlib/Mathlib/Order/ConditionallyCompleteLattice/Finset.lean']
links={p:Path(p).name+'.txt' for p in paths}
for p,n in links.items():shutil.copyfile(R/p,D/n)
put('source-links.json',links);put('mathlib-inputs.json',[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size} for p in paths if p.startswith('.lake')])
(D/'clean-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:558])+'\n')
command('local-literature-search.json',['rg','-n','index|weightedOrder|natural weights|P_\\\\alpha','.mathlib-quality/references/clean.tex'])
searches=[]
for args in [['rg','--no-ignore','-n',r'\bindex_mul\b','Roth','Roth.lean'],['git','grep','-n','-w','index_mul','--','Roth/*.lean','Roth.lean']]:
 x=subprocess.run(args,cwd=R,text=True,capture_output=True);searches.append({'argv':args,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr})
put('complete-caller-search.json',{'searches':searches,'canonical_source_inventory':sorted({x['file'] for x in order})})
fs=[]
for p in sorted({x['file'] for x in order}):
 occ=[]
 for i,line in enumerate((R/p).read_text().splitlines(),1):
  for m in re.finditer(r'\bindex_mul\b',line):occ.append({'line':i,'kind':'docstring' if i==37 and p=='Roth/Index.lean' else 'declaration' if i==162 and p=='Roth/Index.lean' else 'proof-body application','text':line})
 fs.append({'path':p,'sha256':sha(R/p),'occurrences':occ})
put('lexical-enumeration.json',{'files':fs,'applications':2,'proof_body_applications':2,'statement_applications':0})

callers=[]
for file,name,start,end,line in [('Roth/Index.lean','Roth.index_prod','theorem index_prod','/-- Source: §5, proof of Lemma 6',185),('Roth/Theta.lean','Roth.index_separated_mul_le_aux','private lemma index_separated_mul_le_aux','\nomit [DecidableEq τ] in',438)]:
 s=(R/file).read_text();a=s.index(start);b=s.index(end,a);frag=s[a:b]
 callers.append({'declaration':name,'file':file,'source_sha256':sha(R/file),'identifier_occurrences':1,'reference_lines':[line],'source_fragment':frag,'plan':'Retain the factor nonvanishing certificates; replace index_mul by independently proved IndexMul144.replacement with explicit r and omit hr argument. Entire caller replay compiled. For upstream migration use projected infDegree with the natural-weight coe/scaling bridge; do not count these new bridge proofs as existing library calls.'})
put('callers.json',callers)
put('direct-consumers.json',{'count':2,'consumers':['Roth.index_prod','Roth.index_separated_mul_le_aux'],'second_is_private':True})
for n,pat in [('current','index_mul|weightedOrder_mul'),('literature','weightedOrder_mul|weightedTotalDegree.*mul|initial.*mul'),('abstract','infDegree.*mul|supDegree_mul|weightedHomogeneousComponent.*mul|weightedGradedAlgebra')]: command('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
command('rg-inline.json',['rg','--no-ignore','-n','weightedOrder_mul|index_mul|toNat_add|infDegree.*mul','Roth','Roth.lean'])
command('rg-graded.json',['rg','-n','mul.*(degree|support)|degree.*mul|sup.*mul|inf.*mul','.lake/packages/mathlib/Mathlib/Algebra/DirectSum','.lake/packages/mathlib/Mathlib/RingTheory/GradedAlgebra','.lake/packages/mathlib/Mathlib/Algebra/GradedMonoid.lean'])
command('recent-commits.json',['git','-C','.lake/packages/mathlib','log','-12','--format=%h %ad %an %s','--date=short','--','Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean','Mathlib/Algebra/MonoidAlgebra/Degree.lean'])
put('progress-snapshot.json',json.loads((R/'.mathlib-quality/overview/progress.json').read_text()))
