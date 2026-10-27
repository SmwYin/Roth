from pathlib import Path
import json,hashlib,subprocess,shutil,re
D=Path(__file__).parent; R=Path('/Users/ramin/LEAN/Roth'); N='Roth.index_eq_weightedOrder_div'
def put(n,o): (D/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def command(n,args):
 x=subprocess.run(args,cwd=R,text=True,capture_output=True); put(n,{'argv':args,'cwd':str(R),'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr}); return x
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());put('input-manifest.json',base)
put('inputs.json',[{'path':p,'sha256':sha(R/p),'expected_sha256':q['sha256'],'bytes':(R/p).stat().st_size,'match':sha(R/p)==q['sha256']} for p,q in base['sources_and_pins'].items()])
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[142])
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
paths=['Roth/Index.lean','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Basic.lean','.lake/packages/mathlib/Mathlib/Order/ConditionallyCompleteLattice/Finset.lean']
links={p:Path(p).name+'.txt' for p in paths}
for p,n in links.items():shutil.copyfile(R/p,D/n)
put('source-links.json',links);put('mathlib-inputs.json',[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size} for p in paths if p.startswith('.lake')])
(D/'clean-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:558])+'\n')
command('local-literature-search.json',['rg','-n','index|weightedOrder|natural weights|P_\\\\alpha','.mathlib-quality/references/clean.tex'])
searches=[]
for args in [['rg','--no-ignore','-n',r'\bindex_eq_weightedOrder_div\b','Roth','Roth.lean'],['git','grep','-n','-w','index_eq_weightedOrder_div','--','Roth/*.lean','Roth.lean']]:
 x=subprocess.run(args,cwd=R,text=True,capture_output=True);searches.append({'argv':args,'exit_code':x.returncode,'stdout':x.stdout,'stderr':x.stderr})
put('complete-caller-search.json',{'searches':searches,'canonical_source_inventory':sorted({x['file'] for x in order})})
fs=[]
for p in sorted({x['file'] for x in order}):
 occ=[]
 for i,line in enumerate((R/p).read_text().splitlines(),1):
  for m in re.finditer(r'\bindex_eq_weightedOrder_div\b',line):occ.append({'line':i,'kind':'docstring' if i==38 else 'declaration' if i==143 else 'proof-body application','text':line})
 fs.append({'path':p,'sha256':sha(R/p),'occurrences':occ})
put('lexical-enumeration.json',{'files':fs,'applications':3,'proof_body_applications':3,'statement_applications':0})
s=(R/'Roth/Index.lean').read_text(); fragment=s[s.index('theorem index_mul'):s.index('/-- The index is additive on finite products')]
put('callers.json',[{'declaration':'Roth.index_mul','file':'Roth/Index.lean','source_sha256':sha(R/'Roth/Index.lean'),'identifier_occurrences':3,'reference_lines':[164,165],'source_fragment':fragment,'plan':'After replacing the local comparison by its checked hP-free form, rewrite each factor and product using replacement P hr α, replacement Q hr α, replacement (P*Q) hr α; retain hP/hQ to prove ENat.toNat_add finiteness. Generic upstream coe comparison plus denominator bridge and scaled finite projection reconstructs the same rewrite equality.'}])
put('direct-consumers.json',{'count':1,'consumers':['Roth.index_mul']})
for n,pat in [('current','index_eq_weightedOrder_div|weightedOrder.*div|div.*weightedOrder'),('literature','weightedOrder|weightedTotalDegree|infDegree'),('abstract','weightedOrder.*infDegree|infDegree.*weightedOrder|theorem.*infDegree|theorem.*weightedOrder')]:command('rg-'+n+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
command('rg-inline.json',['rg','--no-ignore','-n','weightedOrder|toNat_add|weight_eq_finsuppWeight_div|sInf','Roth','Roth.lean'])
command('recent-commits.json',['git','-C','.lake/packages/mathlib','log','-12','--format=%h %ad %an %s','--date=short','--','Mathlib/RingTheory/MvPowerSeries/Order.lean','Mathlib/Algebra/MonoidAlgebra/Degree.lean'])
accepted=[]
pr=json.loads((R/'.mathlib-quality/overview/progress.json').read_text())
put('progress-snapshot.json',pr)
