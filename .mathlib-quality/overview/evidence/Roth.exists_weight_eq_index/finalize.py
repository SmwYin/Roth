from pathlib import Path
import json,hashlib,re
D=Path(__file__).resolve().parent
N='Roth.exists_weight_eq_index'
def save(n,x):D.joinpath(n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
save('assessment.json',dict(declaration=N,kind='theorem',canonical_index=136,verdict='NO-mathlib-has-it',completed=True,allphases='PASS',unresolved=[],root_acceptance='pending',phases={x:'PASS' for x in ph}))
entries=[]
def add(label,stem,required,region=0,fmt='disk',guard=None,receipt=None):
 source=stem+'-executed.lean.txt';receipt=receipt or stem+'-receipt.json'
 entries.append(dict(label=label,source=source,source_sha256=sha(D/source),receipt=receipt,required_info=required,native_region_start_line=region,format=fmt,**({'guard':guard} if guard else {})))
add('original-and-audit','exists-weight-eq-index-original',["'Roth.exists_weight_eq_index' depends on axioms:",'EXISTS_WEIGHT_EQ_INDEX_AUDIT: requested=293; unique=293','EXISTS_WEIGHT_EQ_INDEX_AUDIT_PRESENT: present=293; values=293'],1619,receipt='exists-weight-eq-index-original-audit-receipt.json')
add('mathlib-reaim-and-generality','exists-weight-eq-index-mathlib-clean',["'ExistsWeightEqIndex136."+x+"' depends on axioms:" for x in ['abstractLaw','projectedLaw']],fmt='raw',guard=N)
add('fresh-original-replacement','exists-weight-eq-index-target',["'ExistsWeightEqIndex136.originalReplacement' depends on axioms:"],1940)
add('fresh-all-callers','exists-weight-eq-index-callers',["'IndexReplay136."+x+"' depends on axioms:" for x in ['replacement','index_eq_zero_iff','index_sub_weight_le_index_hasseDeriv','index_le_card']]+["'IndexMainLemmaReplay136.exists_hasseDeriv_eval_ne_zero' depends on axioms:"],1958)
add('independently-inspected-parent-mathlib-bridge','index-expanded-mathlib',["'IndexMathlibOnly133."+x+"' depends on axioms:" for x in ['finsetBridge','genericBridge','denominatorBridge']],fmt='raw',guard='Roth.index')
# Parent context bridges retained unchanged; full native diagnostic and axiom checks still required.
for stem,region,ns,names in [('index-consumers',401,'IndexConsumers133',['targetBridge','indexSetBridge']),('index-expanded-bridge',429,'IndexExpanded133',['weightBridge','fullyExpandedBridge'])]:
 # Use actual archived receipt regions, not assumed historical positions.
 r=json.loads((D/(stem+'-receipt.json')).read_text())['result']['structuredContent']['result']
 matches=[x['line'] for x in r['items'] if any("'"+ns+'.'+n+"' depends on axioms:" in x['message'] for n in names)]
 assert matches
 add('independently-inspected-parent-'+stem,stem,["'"+ns+'.'+x+"' depends on axioms:" for x in names],min(matches))
v=dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=entries,rejected=[{'source':'exists-weight-eq-index-mathlib-initial-executed.lean.txt','receipt':'exists-weight-eq-index-mathlib-initial-receipt.json','reason':'rw did not delta infDegree; rejected projected proof, recovered proof not accepted; explicit change to coeff.support.inf fixes normalization'}],inputs='inputs.json',mathlib_inputs='mathlib-inputs.json',audit={'source':'exists-weight-eq-index-audit-executed.lean.txt','receipt':'exists-weight-eq-index-original-audit-receipt.json','native_region_start_line':1622,'exact_order_source':'canonical-order.json','requested':293,'unique':293,'present':293,'values':293,'direct_consumers':4},preparation_only=['mathlib-prep.lean.txt','target-prep.lean.txt','caller-prep.lean.txt'],notes=['Disk snippets were appended at the recorded lines in .lake/roth-overview-session/GenWronskianChecks.lean with original whole-project imports.','Historical parent bridges are complete unchanged sources/receipts independently inspected. Fresh probes verify this dependent analogous law and its actual spelling/consumers.','Fresh replacement uses no original target or downstream index theorem.'])
save('verification.json',v)
r=json.loads((D/'exists-weight-eq-index-original-audit-receipt.json').read_text())['result']['structuredContent']['result'];ds=[x for x in r['items'] if x['line']>=1619]
cons=[x['message'].split(': ',1)[1] for x in ds if x['message'].startswith('EXISTS_WEIGHT_EQ_INDEX_DIRECT_CONSUMER:')]
save('direct-consumers.json',dict(count=len(cons),consumers=cons,native_region_start_line=1622))
type_=next(x['message'] for x in ds if x['message'].startswith(N+'.'))
save('overview-entry.json',dict(declaration=N,kind='theorem',type=type_,what='A nonzero polynomial has an evaluated Hasse derivative whose weight attains its index.',how='Set.Nonempty.csInf_mem on finite nonempty weighted Taylor support, then private coefficient/support equivalence.',hypotheses=['σ : Type u with Fintype σ','P : MvPolynomial σ ℝ with P≠0','α : σ→ℝ','r : σ→ℕ, allowing zeros; no positivity assumption'],project_dependencies=['Roth.index','Roth.weight','MvPolynomial.taylor','MvPolynomial.taylor_eq_zero_iff','MvPolynomial.hasseDeriv','MvPolynomial.coeff_taylor','private Roth.mem_support_taylor_iff'],caller_summary={'explicit_declarations':4,'occurrences':4,'within_module':3,'outside_module':1,'kernel_direct_consumers':4,'files':['Roth/Index.lean','Roth/MainLemma.lean']},mathlib_api_audit={'verdict':'NO-mathlib-has-it','reaim_parent':'AddMonoidAlgebra.infDegree','analogous_law':'Finset.exists_mem_eq_inf','premise':'nonempty coefficient support','verified_native':True},moral_duplications=['Attainment of a finite nonempty support infimum in a linear order is already Finset.exists_mem_eq_inf.','MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder provides the standard natural-weight analogue.'],generalization='Verified Semiring coefficients, arbitrary ambient support type with no Fintype, arbitrary degree map into any LinearOrder/OrderTop target with independent universes; separately verified real default-zero projection.',missing_api='No missing generic attained-minimum law. Parent finite-sInf/infDegree bridge and Taylor coefficient conversion are real normalization and separately justified project API.',junk=False,action='Retain locally for manuscript vocabulary or migrate parent to projected infDegree and replace all four applications using existing Finset attainment. Delete this wrapper after replacing those calls; complete consumer replay verified. No upstream PR.'))
# Manifest is current, includes all package artifacts except itself; integration-only acceptance allowed.
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dest='.mathlib-quality/overview/mathlibable/'+N+'.md' if p.name=='report.md' else '.mathlib-quality/overview/evidence/'+N+'/'+p.name
 files.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
save('copy-manifest.json',dict(declaration=N,files=files))
