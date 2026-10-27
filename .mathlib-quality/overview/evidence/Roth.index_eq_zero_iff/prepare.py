from pathlib import Path
import re,json,hashlib,subprocess,shutil
D=Path('/private/tmp/roth-overview/assess/Roth.index_eq_zero_iff');R=Path('/Users/ramin/LEAN/Roth');P=R/'.mathlib-quality/overview/evidence/Roth.index_nonneg'
def write(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=True)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['baseline-build.txt','input-manifest.json','canonical-order.json','clean.tex.txt','clean-excerpt.tex.txt','index-consumers-executed.lean.txt','index-consumers-receipt.json','index-expanded-bridge-executed.lean.txt','index-expanded-bridge-receipt.json','index-expanded-mathlib-executed.lean.txt','index-expanded-mathlib-receipt.json']:
 shutil.copy2(P/n,D/n)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());write('canonical-entry.json',next(x for x in order if x['name']=='Roth.index_eq_zero_iff'))
inputs=json.loads((P/'inputs.json').read_text())
for x in inputs:
 p=R/x['path'];x.update(sha256=sha(p),bytes=p.stat().st_size);x['match']=x['sha256']==x['expected_sha256']
write('inputs.json',inputs);write('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
shutil.copy2(R/'Roth/Index.lean',D/'Index.lean.txt');shutil.copy2(R/'Roth/Box.lean',D/'Box.lean.txt');write('source-links.json',{'Roth/Index.lean':'Index.lean.txt','Roth/Box.lean':'Box.lean.txt'})
def run(n,argv):
 z=subprocess.run(argv,cwd=R,text=True,capture_output=True);v={'argv':argv,'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr};write(n,v);return v
search=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_eq_zero_iff\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','-w','index_eq_zero_iff','--','Roth/*.lean','Roth.lean'])]
write('complete-caller-search.json',{'canonical_source_inventory':sorted({x['file'] for x in order}|{'Roth.lean'}),'searches':search})
roots=['Roth','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean']
for form,pattern in [('current',r'index_eq_zero_iff|weight_eq_zero_iff'),('literature',r'weightedOrder_eq_nat|weightedOrder_eq_zero|constantCoeff'),('abstract',r'inf_eq_bot_iff|sup_eq_top_iff|infDegree|inf_le_iff'),('inline',r'index.*= 0|index_eq_zero_iff|eval.*≠ 0')]:
 run('rg-'+form+'.json',['rg','--no-ignore','-n',pattern,*(roots if form!='inline' else ['Roth','Roth.lean'])])
run('local-literature-search.json',['rg','-n','index|ind\(P\)|nonzero|vanish','.mathlib-quality/references/clean.tex'])
write('mathlib-inputs.json',[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size} for p in roots[1:]])
s=(R/'Roth/Index.lean').read_text();start=s.index('theorem index_prod');end=s.index('/-- Source: §5',start)
write('callers.json',[{'file':'Roth/Index.lean','declaration':'Roth.index_prod','reference_lines':[182],'identifier_occurrences':1,'source_sha256':sha(R/'Roth/Index.lean'),'source_fragment':s[start:end],'plan':'In the empty-product base case replace the iff .2 application with originalReplacement or, after shared parent/nonnegative recoding bridges, Finset.inf_eq_bot_iff using degree zero only at exponent0; the evaluation of1 remains simp. The nonempty inductive branch is unchanged.'}])
write('direct-consumers.json',{'count':1,'consumers':['Roth.index_prod'],'scope':'canonical direct kernel-value consumers, separate from source/simp/transitive closure'})
write('literature-summary.json',{'chatgpt_math':'n/a: ask_chatgpt_math unavailable','standard_form':'Strictly positive weighted finite-support order is zero iff the constant coefficient is nonzero; after translation this is evaluation at the center.','generality':'Finite support arbitrary semiring coefficients, arbitrary support carrier and degree map into a bounded linear order, requiring bottom exactly at the distinguished exponent; real signed degrees need nonnegativity and zero-only-at-exponent0.','history':'Classical normalized derivative minimum; Hasse coefficient formulation extends to positive characteristic.','zero_convention':'Local manuscript sets index0=infinity; project defaults0, so hP is essential for original iff.','ncatlab':'Actual namespace query returned only off-path nLab material; no exact hit, not absence proof.','recent':'2021-10-27 through2026-10-27; 2609.03451 Taylor/monomial valuations adjacent; Roth additive-combinatorial hits rejected.'})
