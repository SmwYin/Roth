from pathlib import Path
import hashlib,json,shutil,subprocess,re
D=Path(__file__).parent;ROOT=Path('/Users/ramin/LEAN/Roth'); TMP=D.parents[1]
def save(n,x): (D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p in TMP.glob('le-index-iff-*'):
 if p.is_file() and p.suffix in ['.txt','.json']:shutil.copy2(p,D/p.name)
P=ROOT/'.mathlib-quality/overview/evidence/Roth.index'
for n in ['index-expanded-mathlib-executed.lean.txt','index-expanded-mathlib-receipt.json','index-consumers-executed.lean.txt','index-consumers-receipt.json','index-expanded-bridge-executed.lean.txt','index-expanded-bridge-receipt.json']:shutil.copy2(P/n,D/n)
shared=ROOT/'.mathlib-quality/overview/evidence/shared'
for n in ['baseline-build.txt','input-manifest.json']:shutil.copy2(shared/n,D/n)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());save('canonical-order.json',order);save('canonical-entry.json',next(e for e in order if e['name']=='Roth.le_index_iff'))
manifest=json.loads((shared/'input-manifest.json').read_text());inputs=[]
for n,e in manifest['sources_and_pins'].items():
 p=ROOT/n;h=sha(p);inputs.append({'path':n,'sha256':h,'expected_sha256':e['sha256'],'bytes':p.stat().st_size,'match':h==e['sha256']})
save('inputs.json',inputs);save('input-hash-check.json',{'all_pass':all(e['match'] for e in inputs),'count':len(inputs)})
sources={'Roth/Index.lean':'Index.lean.txt','Roth/MainLemma.lean':'MainLemma.lean.txt','.mathlib-quality/references/clean.tex':'clean.tex.txt'}
for n,d in sources.items():shutil.copy2(ROOT/n,D/d)
save('source-links.json',sources)
s=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-excerpt.tex.txt').write_text('\n'.join(s[529:556])+'\n')
ml=['Mathlib/Algebra/MonoidAlgebra/Degree.lean','Mathlib/Data/Finset/Lattice/Fold.lean','Mathlib/Order/ConditionallyCompleteLattice/Finset.lean','Mathlib/Order/ConditionallyCompleteLattice/Basic.lean','Mathlib/RingTheory/MvPowerSeries/Order.lean']
save('mathlib-inputs.json',[{'path':'.lake/packages/mathlib/'+n,'sha256':sha(ROOT/'.lake/packages/mathlib'/n),'bytes':(ROOT/'.lake/packages/mathlib'/n).stat().st_size} for n in ml])
def run(n,args):
 r=subprocess.run(args,cwd=ROOT,capture_output=True,text=True);x={'argv':args,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr};save(n,x);return x
inventory=sorted({e['file'] for e in order}|{'Roth.lean'});search=[]
search.append(run('caller-rg.json',['rg','--no-ignore','-n',r'\ble_index_iff\b',*inventory]))
search.append(run('caller-git-grep.json',['git','grep','-n','-E',r'\ble_index_iff\b','--',*inventory]))
save('complete-caller-search.json',{'canonical_source_inventory':inventory,'searches':search})
for form,pat,paths in [('current',r'le_index_iff|index_le_weight',['Roth','Roth.lean']),('literature',r'theorem (le_weightedOrder|nat_le_weightedOrder)|weightedOrder_le',['.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean']),('abstract',r'le_inf_iff|le_inf\x27_iff|le_csInf_iff|abbrev infDegree',['.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/ConditionallyCompleteLattice/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean']),('inline',r'le_csInf|le_inf|weight r d < c|hasseDeriv.*= 0',['Roth/Index.lean','Roth/MainLemma.lean'])]:run('rg-'+form+'.json',['rg','--no-ignore','-n',pat,*paths])
run('local-literature-search.json',['rg','-n','index|minimum|infimum','.mathlib-quality/references/clean.tex'])
callers=[]
for name,file,lines,plan in [('Roth.le_index_sum','Roth/Index.lean',[121,125],'Use generic lower-bound iff on the translated sum for .2; on the chosen nonzero summand for .1. Keep map_sum, witness selection and nonzero argument.'),('Roth.index_eq_weightedOrder_div','Roth/Index.lean',[154],'Apply generic lower-bound iff .2 to Taylor support and retain the weight denominator rewrite and weightedOrder_le estimate.'),('Roth.index_unique','Roth/Index.lean',[248],'Apply generic lower-bound iff .2; retain univariate coefficient key, natTrailingDegree bound and division inequality.'),('Roth.le_index_of_forall_eval_eq_zero','Roth/MainLemma.lean',[423],'Apply generic lower-bound iff .2; retain contradiction from sub-cutoff vanishing, box restriction and degree-bound zero derivative.')]:
 text=(ROOT/file).read_text();bare=name.split('.')[-1];a=text.index('theorem '+bare);b=text.find('\n/--',a);b=len(text) if b<0 else b
 callers.append({'declaration':name,'file':file,'reference_lines':lines,'identifier_occurrences':len(lines),'source_sha256':sha(ROOT/file),'source_fragment':text[a:b].rstrip(),'plan':plan})
save('callers.json',callers);save('direct-consumers.json',{'count':4,'consumers':[c['declaration'] for c in callers]})
save('literature-summary.json',{'chatgpt_math':'n/a: ask_chatgpt_math unavailable','local':'clean.tex lines530-556: minimum nonvanishing Hasse weights; manuscript zero=+infinity versus project zero=0','general':'Roth index is a weighted vanishing order, its lower bounds are precisely common lower bounds of the supported weights. Abstractly this is the finite meet universal property.','nlab':'meet page gives greatest-lower-bound characterization and top for empty meets; direct open failed unsupported XHTML but search returned mathematical content','ncatlab':'two explicit /ncatlab mathematical queries returned nLab pages, no namespace-local hit; not absence evidence','stacks':'02MB section10.121 describes length-defined orders on1-dimensional local Noetherian rings, adjacent not exact weighted finite support law','mathoverflow':'449959 on leadable monomials and weighted lexicographic orders concerns extremal support, not the lower-bound iff','arxiv':'after2021-10-27 queries returned Kim2604.18465 quasi-monomial valuations computing invariants, adjacent recent context not exact elementary iff','access_failures':['nLab direct application/xhtml+xml unsupported','ICM1958 PDF content length74705952 too large'],'history':'Roth ICM1958 p206 defines index via least nonvanishing derivative; Min Ru notes p3 Definition1 use normalized derivatives and coefficient weights. Modern finite meet organization isolates the order law from differential algebra.'})
