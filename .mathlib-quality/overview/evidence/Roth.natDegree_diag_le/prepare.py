from pathlib import Path
import json,hashlib,subprocess,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.natDegree_diag_le'
def put(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rg(tag,args):
 c=['rg']+args;p=subprocess.run(c,cwd=R,text=True,capture_output=True);put('rg-'+tag+'.json',{'command':c,'cwd':str(R),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
for lab in ['original','raw','existing','consumers']:
 for s,t in [('executed.lean.txt','executed.lean.txt'),('receipt.json','success.json')]:
  shutil.copyfile('/private/tmp/roth-overview/degree-diag-'+lab+'-'+s,D/('native-'+lab+'-'+t))
for p,n in [('Roth/CoeffNorm.lean','source-module.lean.txt'),('Roth/MainLemma.lean','source-callers.lean.txt'),('.mathlib-quality/overview/evidence/shared/baseline-build.txt','baseline-build.txt')]: shutil.copyfile(R/p,D/n)
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for p,x in b['sources_and_pins'].items():
 f=R/p;inputs.append({'path':p,'sha256':sha(f),'bytes':f.stat().st_size,'baseline_sha256':x['sha256'],'match':sha(f)==x['sha256']})
put('inputs.json',inputs);put('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
files=['Mathlib/RingTheory/Polynomial/Basic.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/MvPolynomial/Equiv.lean','Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean','Mathlib/Algebra/Polynomial/Degree/Operations.lean']
ms=[]
for i,p in enumerate(files):
 f=R/'.lake/packages/mathlib'/p;a=f'mathlib-source-{i}.lean.txt';shutil.copyfile(f,D/a);ms.append({'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'archive':a})
put('mathlib-inputs.json',ms)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-entry.json',order[92]);put('canonical-order.json',{'index':93,'entry':order[92],'source_sha256':sha(R/'.mathlib-quality/overview/declaration-order.json')});put('canonical-snapshot.json',order)
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());cs=progress['completed_declarations'];put('accepted-yes-grouping.json',{'completed_count':len(cs),'accepted_yes':[x for x in cs if x['verdict'].startswith('YES') and x['acceptance']=='PASS'],'parent_diag':[x for x in cs if x['declaration']=='Roth.diag']})
rg('current',['-n','natDegree.*diag|natDegree.*aeval|aeval.*natDegree','.lake/packages/mathlib/Mathlib'])
rg('literature',['-n','aeval_natDegree_le|totalDegree_le_degrees_card|totalDegree_rename_le|sum_count_eq_card','.lake/packages/mathlib/Mathlib'])
rg('abstract',['-n','natDegree.*totalDegree|totalDegree.*natDegree|totalDegree_le.*sum|sum.*degreeOf','.lake/packages/mathlib/Mathlib'])
rg('full-name',['-n',r'Roth\.natDegree_diag_le|theorem natDegree_diag_le|lemma natDegree_diag_le','.lake/packages/mathlib/Mathlib'])
rg('callers',['-n',r'\bnatDegree_diag_le\b','Roth','Roth.lean'])
rg('inline',['-n',r'natDegree_sum_le_of_forall_le|aeval_natDegree_le|totalDegree_le_degrees_card|natDegree.*diag|diag.*natDegree','Roth','Roth.lean'])
rg('local-literature',['-n',r's\\leq\\sum_jr_j|same variable|degree|total degree','.mathlib-quality/references/clean.tex'])
f=R/'.mathlib-quality/references/clean.tex';put('local-literature-source.json',{'path':str(f.relative_to(R)),'sha256':sha(f),'bytes':f.stat().st_size,'line_numbers':[1407,1449,1455,1468],'summary':'Lemma9 uses diagonal monomial expansion then s <= sum_j r_j <= m*r_1 in the remainder bound.'})
lines=f.read_text().splitlines();(D/'local-literature-excerpt.txt').write_text('\n'.join(f'{i+1}: {lines[i]}' for i in range(1403,1472))+'\n')
put('callers.json',{'named_count':1,'explicit_occurrences':1,'external_to_file_count':1,'callers':[{'file':'Roth/MainLemma.lean','line':513,'declaration':'_private.Roth.MainLemma.0.Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux','usage':'(natDegree_diag_le _ hdP)','refactor':'Supply totalDegree bound for hasseDeriv j P, then specialize aeval_natDegree_le at constant X and n=1; consumer replay verifies this using the new experimental generic helper, which is not an existing block.'}],'inline_derivations':[],'native_audit':{'status':'PASS','requested':293,'present':293,'values':293,'unique':293},'scope':'Explicit source calls plus direct proof constants in canonical 293 values; not transitive opaque/simp closure.'})
put('formal-search.json',[json.loads((D/f'search-{i:02}.json').read_text())|{'form':['current','standard','abstract'][(i-1)%3]} for i in range(1,13)])
put('verification.json',{'declaration':N,'production_unchanged':True,'unresolved':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'accepted':[{'label':lab,'source':'native-'+lab+'-executed.lean.txt','source_sha256':sha(D/('native-'+lab+'-executed.lean.txt')),'receipt':'native-'+lab+'-success.json','expected_axiom_declarations':{'original':[N],'raw':['MvPolynomial.DegreeDiagRaw.total','MvPolynomial.DegreeDiagRaw.generic'],'existing':['MvPolynomial.DegreeDiagExisting.total','MvPolynomial.DegreeDiagExisting.total_bound','MvPolynomial.DegreeDiagExisting.generic'],'consumers':['MvPolynomial.DegreeDiagConsumers.specialization','MvPolynomial.DegreeDiagConsumers.abs_coeff_diag_hasseDeriv_modByMonic_le_aux_replay']}[lab]} for lab in ['original','raw','existing','consumers']],'rejected':[],'unexecuted':['probe-composition.lean.txt'],'preexecution_correction':'Root corrected proposed no-Fintype total proof before first execution: use definitional change k.sum ... and le_totalDegree, not Finsupp.degree_eq_sum requiring Fintype. No rejected native attempt resulted.','negative_search_limit':'No failed exact? absence claim. Optional proposed probe was declined; actual positive compositions are verified. No <=3-call old-form term established; nonexistence is not claimed.'})
