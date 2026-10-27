from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.index_mul'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,o):(D/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
accepted=[]
def add(label,source,receipt,fmt,start,required,**kwargs):
 accepted.append(dict(label=label,source=source,source_sha256=sha(D/source),receipt=receipt,format=fmt,native_region_start_line=start,required_info=required,**kwargs))
p='index-mul-'
add('original',p+'original-executed.lean.txt',p+'original-audit-receipt.json','disk',2400,['Roth.index_mul','depends on axioms: [propext, Classical.choice, Quot.sound]'],source_layout='whole-document')
add('canonical-audit',p+'audit-executed.lean.txt',p+'original-audit-receipt.json','disk',2404,['INDEX_MUL144_AUDIT: requested=293; unique=293','INDEX_MUL144_AUDIT_PRESENT: present=293; values=293','INDEX_MUL144_DIRECT_CONSUMER: Roth.index_prod','INDEX_MUL144_DIRECT_CONSUMER: _private.Roth.Theta.0.Roth.index_separated_mul_le_aux'],source_layout='region',source_start_line=2403)
for lab,st,req in [('target-clean',2722,['IndexMul144.clearedWeight','IndexMul144.comparison','IndexMul144.replacement','IndexMul144.zeroLeftGuard','IndexMul144.zeroRightGuard']),('callers-clean',2781,['IndexMulCallers144.index_prod','IndexMulCallers144.index_separated_mul_le_aux']),('composition-final',2839,['IndexMulComposition144.exactAttempt'])]:
 add(lab,p+lab+'-executed.lean.txt',p+lab+'-receipt.json','disk',st,req,source_layout='whole-document')
add('mathlib',p+'mathlib-executed.lean.txt',p+'mathlib-receipt.json','raw',1,['IndexMulMathlib144.modern','IndexMulMathlib144.polynomial','IndexMulMathlib144.finiteScale'],guard=N)
for lab,req in [('generic-api-clean',['@MvPolynomial.weightedHomogeneousComponent','MvPolynomial.weightedGradedAlgebra','Unknown constant `AddMonoidAlgebra.infDegree_mul`','Unknown constant `MvPolynomial.weightedTotalDegree_mul`','Unknown constant `MvPolynomial.weightedHomogeneousComponent_mul`']),('broader-api',['@MvPolynomial.IsWeightedHomogeneous.mul','MvPolynomial.weightedDecomposition'])]:
 add(lab,p+lab+'-executed.lean.txt',p+lab+'-receipt.json','raw',1,req,guard=N,signatures_only=True)
add('prerequisite-targetBridge','index-consumers-executed.lean.txt','index-consumers-receipt.json','disk',16522,['IndexConsumers133.targetBridge'],source_layout='region',source_start_line=16522,prerequisite=True)
add('prerequisite-scale','index-weighted-order-scale-executed.lean.txt','index-weighted-order-scale-receipt.json','raw',1,['IndexWeightedScale143.scaledMinimum','IndexWeightedScale143.finiteProjection','IndexWeightedScale143.scaledInfDegree'],guard='Roth.index_eq_weightedOrder_div',prerequisite=True)
rejected=[]
for lab,reason in [('target-initial','Zero-factor guards left type of index0 implicit; corrected explicit Unit polynomial annotation. Nonzero theorem and all-r normalization succeeded, but whole run not accepted.'),('callers-initial','Theta hr0 unused after replacing sole multiplication use; binding renamed _hr0 with hypothesis type/position retained.'),('generic-api-initial','Root executed importless preparation code in isolated run_code; unknown names. Corrected explicit genuine imports and target guard.'),('composition-initial','Offside parsing of exact arguments caused failed elaboration and recovered sorryAx; never accepted.'),('composition-second','Parenthesized exact attempt still offside; recovered sorryAx not accepted.'),('composition-warnings','Bounded simp negative probe had two unused arguments; final exact tested scope simp only[index,map_mul].')]:
 rejected.append(dict(source=p+lab+'-executed.lean.txt',receipt=p+lab+'-receipt.json',reason=reason))
v=dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,audit=dict(source=p+'audit-executed.lean.txt',receipt=p+'original-audit-receipt.json',native_region_start_line=2404,marker='INDEX_MUL144'),caller_source=p+'callers-clean-executed.lean.txt',target_source=p+'target-clean-executed.lean.txt',composition_source=p+'composition-final-executed.lean.txt',preparation_only=['project-probe-prep.lean.txt','mathlib-probe-prep.lean.txt','caller-probe-prep.lean.txt','generic-api-probe-prep.lean.txt','compose-probe-prep.lean.txt'],notes=['New target-specific disk sources preserve entire exact executed document; assertions of required proof information scoped to actual native_region_start_line. Full-file diagnostics remain error/warning/axiom checked.','Canonical audit source is the exact appended region, while same execution full source retained as original-executed; exact293 order equality validated.','Earlier133 targetBridge and143 scaled comparison retained as explicit prerequisite proofs, not existing mathlib calls. Old receipt offsets retained unchanged.','Raw run_code uses diagnostics and has no partial field; disk success requires partial=false.','Broad arbitrary-real polynomial infDegree multiplication is a design proposal only, not accepted proof or unresolved verification request.','Original #print has509character MCP elision; full kernel body not claimed.'])
put('verification.json',v)
files=[]
for q in sorted(D.iterdir()):
 if not q.is_file() or q.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{N}.md' if q.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{q.name}'
 files.append(dict(source=str(q),destination=dest,sha256=sha(q),bytes=q.stat().st_size))
put('copy-manifest.json',dict(declaration=N,files=files))
