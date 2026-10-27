from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');NAME='Roth.le_index_sum'
P=R/'.mathlib-quality/overview/evidence/Roth.index';Q=R/'.mathlib-quality/overview/evidence/Roth.le_index_iff'
def write(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,argv):
 z=subprocess.run(argv,cwd=R,text=True,capture_output=True);v={'argv':argv,'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr};write(n,v);return v
for n in ['baseline-build.txt','input-manifest.json','canonical-order.json']:shutil.copy2((Q if n=='input-manifest.json' else P)/n,D/n)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());write('canonical-entry.json',next(x for x in order if x['name']==NAME))
inputs=json.loads((Q/'inputs.json').read_text())
for x in inputs:
 p=R/x['path'];x.update(sha256=sha(p),bytes=p.stat().st_size);x['match']=x['sha256']==x['expected_sha256']
write('inputs.json',inputs);write('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
links={}
for file in ['Index','Theta','Box','Taylor','HasseDeriv']:
 src='Roth/'+file+'.lean';dst=file+'.lean.txt';shutil.copy2(R/src,D/dst);links[src]=dst
write('source-links.json',links)
s=(R/'.mathlib-quality/references/clean.tex').read_text();(D/'clean-excerpt.tex.txt').write_text('\n'.join(s.splitlines()[529:618])+'\n')
search=[run('caller-rg.json',['rg','--no-ignore','-n',r'\ble_index_sum\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','-w','le_index_sum','--','Roth/*.lean','Roth.lean'])]
write('complete-caller-search.json',{'canonical_source_inventory':sorted({x['file'] for x in order}|{'Roth.lean'}),'searches':search})
roots=['Roth','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean']
for form,pattern in [('current',r'le_index_sum|index.*sum|sum.*index'),('literature',r'min_weightedOrder_le_add|weightedOrder.*sum|sum.*weightedOrder'),('abstract',r'supDegree_sum_le|infDegree|le_inf_iff|coe_untopD_le'),('inline',r'le_index_sum|exists_ne_zero_of_sum_ne_zero|index.*sum|sum.*index')]:
 run('rg-'+form+'.json',['rg','--no-ignore','-n',pattern,*(roots if form!='inline' else ['Roth','Roth.lean'])])
run('local-literature-search.json',['rg','-n','roth:lem4-1|ind\(P\+Q\)|smaller|determinant|sum','.mathlib-quality/references/clean.tex'])
write('mathlib-inputs.json',[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size} for p in roots[1:]])
s=(R/'Roth/Theta.lean').read_text();i=s.index('theorem sum_max_sub_le_index_det');j=s.index('omit [DecidableEq τ] in',i+1);fragment=s[i:j]
write('callers.json',[{'file':'Roth/Theta.lean','declaration':'Roth.sum_max_sub_le_index_det','reference_lines':[398],'identifier_occurrences':1,'source_sha256':sha(R/'Roth/Theta.lean'),'source_fragment':fragment,'plan':'At the determinant expansion, replace le_index_sum hdet with the checked replacement hs hf; after parent migration apply finiteInfLaw using the common lower bound via Finset.le_inf_iff and projection normalization. Retain the nonzero determinant, term/product nonvanishing, sign invariance, product-index and entry lower-bound steps.'}])
write('direct-consumers.json',{'count':1,'consumers':['Roth.sum_max_sub_le_index_det'],'scope':'direct canonical kernel-value consumers, not simp/transitive closure'})
for n in ['index-mathlib-infdegree-final-executed.lean.txt','index-mathlib-infdegree-final-receipt.json','index-consumers-executed.lean.txt','index-consumers-receipt.json','index-expanded-bridge-executed.lean.txt','index-expanded-bridge-receipt.json','index-expanded-mathlib-executed.lean.txt','index-expanded-mathlib-receipt.json']:
 shutil.copy2(P/n,D/n)
for p in Path('/private/tmp/roth-overview').glob('le-index-sum-*'):
 if p.is_file():shutil.copy2(p,D/p.name)
write('literature-summary.json',{'chatgpt_math':'n/a: ask_chatgpt_math unavailable','standard_form':'Weighted order of a finite sum is at least the minimum of the orders of its summands; equivalently every common lower bound persists. The index is the minimum support weight after Taylor translation.','history':'Roth ICM1958 p206 derivative index; Min Ru Roth notes Definition1 pp2–3 states additive min inequality. Hasse/Taylor wording identifies the same characteristic-zero quantity.','local':'clean.tex530–618 defines zero as infinity and proves addition via coefficient vanishing below smaller index; finite summation is its iteration.','ncatlab':'Actual explicit site:ncatlab.org/ncatlab queries returned nLab or other same-host pages; no exact namespace hit.','recent':'2021-10-27 through2026-10-27; refined recent query returned Kim2604.18465 and Dutta–Ghosh2609.03451 monomial-valuation context. No abstract claims exact finite-sum novelty.','direct_access':'Min Ru PDF and Stacks00I8 open successfully; nLab direct open unsupported XHTML, indexed text inspected.','false_generalization':'Cancellation can make nonzero summands sum to zero. Old real0 convention requires hs; unprojected top-valued infDegree does not. No domain, positive weights or multiplicative valuation structure is needed for sum inequality.'})
