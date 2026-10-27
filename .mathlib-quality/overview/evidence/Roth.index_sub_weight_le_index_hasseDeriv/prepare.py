from pathlib import Path
import re,json,hashlib,subprocess,shutil
D=Path('/private/tmp/roth-overview/assess/Roth.index_sub_weight_le_index_hasseDeriv');R=Path('/Users/ramin/LEAN/Roth');P=R/'.mathlib-quality/overview/evidence/Roth.index_eq_zero_iff';NAME='Roth.index_sub_weight_le_index_hasseDeriv'
def write(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['baseline-build.txt','input-manifest.json','canonical-order.json']:
 shutil.copy2(P/n,D/n)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());write('canonical-entry.json',next(x for x in order if x['name']==NAME))
inputs=json.loads((P/'inputs.json').read_text())
for x in inputs:
 p=R/x['path'];x.update(sha256=sha(p),bytes=p.stat().st_size);x['match']=x['sha256']==x['expected_sha256']
write('inputs.json',inputs);write('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
links={}
for f in ['Index','Box','Taylor','HasseDeriv','Theta','MainLemma']:
 src='Roth/'+f+'.lean';dst=f+'.lean.txt';shutil.copy2(R/src,D/dst);links[src]=dst
write('source-links.json',links)
s=(R/'.mathlib-quality/references/clean.tex').read_text();(D/'clean-excerpt.tex.txt').write_text('\n'.join(s.splitlines()[529:592])+'\n')
def run(n,argv):
 z=subprocess.run(argv,cwd=R,text=True,capture_output=True);v={'argv':argv,'exit_code':z.returncode,'stdout':z.stdout,'stderr':z.stderr};write(n,v);return v
search=[run('caller-rg.json',['rg','--no-ignore','-n',r'\bindex_sub_weight_le_index_hasseDeriv\b','Roth','Roth.lean']),run('caller-git-grep.json',['git','grep','-n','-w','index_sub_weight_le_index_hasseDeriv','--','Roth/*.lean','Roth.lean'])]
write('complete-caller-search.json',{'canonical_source_inventory':sorted({x['file'] for x in order}|{'Roth.lean'}),'searches':search})
roots=['Roth','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/PDeriv.lean']
for form,pattern in [('current',r'index_sub_weight|hasseDeriv.*(index|order)|index.*hasseDeriv'),('literature',r'weightedOrder|[tT]railingDegree.*hasse|hasse.*[tT]railingDegree|natDegree_hasseDeriv_le'),('abstract',r'infDegree|inf.*(deriv|shift)|deriv.*inf|of_mem_support_derivative'),('inline',r'index.*-.*weight|index_sub_weight|hasseDeriv_hasseDeriv')]:
 run('rg-'+form+'.json',['rg','--no-ignore','-n',pattern,*(roots if form!='inline' else ['Roth','Roth.lean'])])
run('local-literature-search.json',['rg','-n','index-of-derivative|ind\(P\)|Hasse|derivative','.mathlib-quality/references/clean.tex'])
write('mathlib-inputs.json',[{'path':p,'sha256':sha(R/p),'bytes':(R/p).stat().st_size} for p in roots[1:]])
callers=[]
for file,decl,start,end,line in [('Theta','Roth.sum_max_sub_le_index_det','theorem sum_max_sub_le_index_det','omit [DecidableEq τ] in',390),('MainLemma','Roth.exists_hasseDeriv_index_eval_bound_aux','private lemma exists_hasseDeriv_index_eval_bound_aux','private lemma abs_coeff_diag_hasseDeriv_modByMonic_le_aux',494)]:
 src='Roth/'+file+'.lean';s=(R/src).read_text();i=s.index(start);j=s.index(end,i+len(start));fragment=s[i:j]
 callers.append({'file':src,'declaration':decl,'reference_lines':[line],'identifier_occurrences':1,'source_sha256':sha(R/src),'source_fragment':fragment,'plan':'Retain the local wrapper; replace its sole application with IndexShiftTarget140.replacement at the identical arguments. A future infDegree API migration requires the explicit minimum/projection bridge and the new derivative shift theorem; generic infDegree sum/product laws do not replace this call.'})
write('callers.json',callers)
write('direct-consumers.json',{'count':2,'consumers':['Roth.sum_max_sub_le_index_det','_private.Roth.MainLemma.0.Roth.exists_hasseDeriv_index_eval_bound_aux'],'scope':'canonical direct kernel-value consumers, separate from source/simp/transitive closure'})
s='namespace IndexShiftReplay140\nopen Roth MvPolynomial\nopen scoped Pointwise\nvariable {τ : Type*} [Fintype τ]\n\n'
for c in callers:s+=c['source_fragment'].replace('private lemma','theorem').replace('index_sub_weight_le_index_hasseDeriv','IndexShiftTarget140.replacement')+'\n'
s+='#print axioms sum_max_sub_le_index_det\n#print axioms exists_hasseDeriv_index_eval_bound_aux\nend IndexShiftReplay140\n';(D/'callers-prepared.lean.txt').write_text(s)
write('literature-summary.json',{'chatgpt_math':'n/a: ask_chatgpt_math unavailable','standard_form':'A Hasse derivative of multi-order k lowers weighted order by at most the additive weight of k; over arbitrary characteristic cancellation of binomial factors is unnecessary.','history':'Roth ICM1958 p206 introduces weighted derivative minimum; normalized classical partial derivatives become Hasse coefficient operators over arbitrary characteristic.','source':'clean.tex lines574-591 and Milojevic Claim3.1 p4 provide exact derivative bound.','generality':'CommSemiring coefficients and arbitrary variable type with finite support; shift-additive real degree function. Verified weakening requires expanded parent representation, not dropping Fintype from fixed Roth.index.','zero_convention':'Projected real minimum0 at zero requires nonzero derivative; WithTop formulation can retain infinity.','ncatlab':'Explicit site:ncatlab.org/ncatlab query returned off-namespace nLab; no exact hit.','recent':'2021-10-27 through2026-10-27; arXiv2402.18717 uses Hasse derivatives and arbitrary characteristic but not exact weighted estimate;2103.07239 excluded from recent window.'})
