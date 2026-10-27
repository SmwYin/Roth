from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).parent;N='Roth.index_prod';T=Path('/private/tmp/roth-overview')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
for p in T.glob('index-prod-*'):
 if p.is_file():shutil.copyfile(p,D/p.name)
accepted=[]
def add(label,source,receipt,fmt,start,req,**kw):accepted.append(dict(label=label,source=source,source_sha256=sha(D/source),receipt=receipt,format=fmt,native_region_start_line=start,required_info=req,**kw))
p='index-prod-'
add('original',p+'original-executed.lean.txt',p+'original-audit-receipt.json','disk',2853,['Roth.index_prod','depends on axioms: [propext, Classical.choice, Quot.sound]'],source_layout='whole-document')
add('canonical-audit',p+'audit-executed.lean.txt',p+'original-audit-receipt.json','disk',2857,['INDEX_PROD145_AUDIT: requested=293; unique=293','INDEX_PROD145_AUDIT_PRESENT: present=293; values=293','INDEX_PROD145_DIRECT_CONSUMER: Roth.sum_max_sub_le_index_det'],source_layout='region',source_start_line=2856)
add('target-clean',p+'target-clean-executed.lean.txt',p+'target-clean-receipt.json','disk',3175,['IndexProd145.one','IndexProd145.replacement','IndexProd145.nonzeroGuard'],source_layout='whole-document')
add('callers-composition',p+'callers-composition-executed.lean.txt',p+'callers-composition-receipt.json','disk',3202,['IndexProdCallers145.sum_max_sub_le_index_det','IndexProdComposition145.exactAttempt'],source_layout='whole-document')
add('mathlib-final',p+'mathlib-final-executed.lean.txt',p+'mathlib-final-receipt.json','raw',1,['IndexProdMathlib145.modern','IndexProdMathlib145.polynomial','MvPowerSeries.weightedOrder_prod','MvPolynomial.coeToMvPowerSeries.ringHom'],guard=N)
add('prerequisite-binary','index-mul-target-clean-executed.lean.txt','index-mul-target-clean-receipt.json','disk',2722,['IndexMul144.clearedWeight','IndexMul144.comparison','IndexMul144.replacement'],prerequisite=True,source_layout='whole-document')
add('prerequisite-targetBridge','index-consumers-executed.lean.txt','index-consumers-receipt.json','disk',16522,['IndexConsumers133.targetBridge'],source_layout='region',source_start_line=16522,prerequisite=True)
add('prerequisite-scale','index-weighted-order-scale-executed.lean.txt','index-weighted-order-scale-receipt.json','raw',1,['IndexWeightedScale143.scaledMinimum','IndexWeightedScale143.finiteProjection','IndexWeightedScale143.scaledInfDegree'],guard='Roth.index_eq_weightedOrder_div',prerequisite=True)
for lab,req in [('generic-api-clean',['@MvPolynomial.weightedHomogeneousComponent','MvPolynomial.weightedGradedAlgebra','Unknown constant `AddMonoidAlgebra.infDegree_mul`']),('broader-api',['@MvPolynomial.IsWeightedHomogeneous.mul','MvPolynomial.weightedDecomposition'])]:
 add('prerequisite-'+lab,'index-mul-'+lab+'-executed.lean.txt','index-mul-'+lab+'-receipt.json','raw',1,req,guard='Roth.index_mul',signatures_only=True,prerequisite=True)
if (D/'index-prod-generic-api-receipt.json').exists():
 add('generic-prod-signature','index-prod-generic-api-executed.lean.txt','index-prod-generic-api-receipt.json','raw',1,['@MvPolynomial.IsWeightedHomogeneous.prod'],guard=N,signatures_only=True)
rejected=[]
for lab,reason in [('target-initial','Unused taylor_X simp argument in guard; warning means rejected whole run. Final source removes it.'),('mathlib-initial','Nonexistent MvPolynomial.coe_prod and not-loaded ENat.toNat_sum; recovered sorryAx rejected.'),('mathlib-second','ringHom map_prod rewrite left definitional equality; recovered sorryAx rejected.'),('mathlib-clean','An additional intermediate rejected raw run; final30-line source/receipt supersedes it.')]:
 s=p+lab+'-executed.lean.txt';r=p+lab+'-receipt.json'
 if (D/s).exists() and (D/r).exists():rejected.append(dict(source=s,receipt=r,reason=reason))
put('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,audit=dict(source=p+'audit-executed.lean.txt',receipt=p+'original-audit-receipt.json',native_region_start_line=2857,marker='INDEX_PROD145'),target_source=p+'target-clean-executed.lean.txt',caller_source=p+'callers-composition-executed.lean.txt',composition_source=p+'callers-composition-executed.lean.txt',preparation_only=['project-probe-prep.lean.txt','mathlib-probe-prep.lean.txt','caller-probe-prep.lean.txt','compose-probe-prep.lean.txt','generic-api-probe-prep.lean.txt'],notes=['Accepted145 mathlib-final receipt is clean success=true; earlier raw attempts with sorryAx are rejected only.','Earlier133,143,144 accepted proofs/signatures are explicitly prerequisite evidence, not fresh145 or existing library calls.','Disk documents retain historical info messages; required fresh information scoped to actual native_region_start_line.','Raw run_code uses diagnostics and has no partial field; disk requires partial=false.','Target145 kernel print is complete; historical144 print in persistent receipts has an elision.','ENat.toNat_sum exists in pinned BigOperators source but not stable7 import context.']))
files=[]
for q in sorted(D.iterdir()):
 if not q.is_file() or q.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{N}.md' if q.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{q.name}'
 files.append(dict(source=str(q),destination=dest,sha256=sha(q),bytes=q.stat().st_size))
put('copy-manifest.json',dict(declaration=N,files=files))
