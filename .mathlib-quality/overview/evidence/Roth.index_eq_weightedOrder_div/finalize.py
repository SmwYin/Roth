from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).parent;N='Roth.index_eq_weightedOrder_div'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,o):(D/n).write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
for p in Path('/private/tmp/roth-overview').glob('index-weighted-order-*'):
 if p.is_file() and p.name.endswith(('.json','.lean.txt','.txt')):shutil.copyfile(p,D/p.name)
accepted=[]
def add(label,source,receipt,fmt,start,required):
 accepted.append({'label':label,'source':source,'source_sha256':sha(D/source),'receipt':receipt,'format':fmt,'native_region_start_line':start,'required_info':required})
prefix='index-weighted-order-'
add('original',prefix+'original-executed.lean.txt',prefix+'original-audit-receipt.json','disk',1929,['Roth.index_eq_weightedOrder_div','depends on axioms: [propext, Classical.choice, Quot.sound]'])
add('canonical-audit',prefix+'audit-executed.lean.txt',prefix+'original-audit-receipt.json','disk',1932,['INDEX_WEIGHTED_ORDER143_AUDIT: requested=293; unique=293','INDEX_WEIGHTED_ORDER143_AUDIT_PRESENT: present=293; values=293','INDEX_WEIGHTED_ORDER143_DIRECT_CONSUMER: Roth.index_mul'])
for lab,info in [('mathlib-clean',['IndexWeightedOrder143.weightedOrder_coe']),('scale',['IndexWeightedScale143.scaledMinimum','IndexWeightedScale143.finiteProjection','IndexWeightedScale143.scaledInfDegree']),('exact-probe',['IndexWeightedOrder143.weightedOrder_coe']),('simp-probe',['IndexWeightedOrder143.weightedOrder_coe'])]:add(lab,prefix+lab+'-executed.lean.txt',prefix+lab+'-receipt.json','raw',1,info)
for lab,info in [('target',['IndexWeightedOrderTarget143.replacementNonzero','IndexWeightedOrderTarget143.replacement','IndexWeightedOrderTarget143.fullCaller']),('guards-clean',['IndexWeightedGuards143.mixedZeroIndex','IndexWeightedGuards143.mixedZeroRhs'])]:
 region=lab.replace('-clean','')
 start=int((D/(prefix+region+'-region.txt')).read_text())
 add(lab,prefix+lab+'-executed.lean.txt',prefix+lab+'-receipt.json','disk',start,info)
# Modern specialization will be added once root native evidence is available.
modern=D/(prefix+'modern-clean-executed.lean.txt')
if modern.exists():
 start=int((D/(prefix+'modern-region.txt')).read_text())
 add('modern-specialization',modern.name,prefix+'modern-clean-receipt.json','disk',start,['IndexWeightedModern143.specialization'])
v={'declaration':N,'unresolved':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'accepted':accepted,'rejected':[{'source':prefix+'modern-executed.lean.txt','receipt':prefix+'modern-receipt.json','reason':'Degree function inferred HDiv ℝ ℕ from uncast denominator; corrected explicit cast of natural product to ℝ, clean specialization compiled.'},{'source':prefix+'mathlib-initial-executed.lean.txt','receipt':prefix+'mathlib-initial-receipt.json','reason':'Finset.inf_le degree function was not inferred; clean correction explicit f, no accepted proof uses failed elaboration.'},{'source':prefix+'guards-initial-executed.lean.txt','receipt':prefix+'guards-initial-receipt.json','reason':'support_X normalizer missing, invalid fielddot newline and unused simp argument warnings; corrected guards clean.'}],'audit':{'source':prefix+'audit-executed.lean.txt','receipt':prefix+'original-audit-receipt.json','native_region_start_line':1932,'marker':'INDEX_WEIGHTED_ORDER143'},'caller_source':prefix+'target-executed.lean.txt','modern_specialization_source':prefix+'modern-clean-executed.lean.txt','preparation_only':['mathlib-probe-prep.lean.txt','project-probe-prep.lean.txt','scaled-probe-prep.lean.txt','guard-probe-prep.lean.txt','modern-specialization-prep.lean.txt'],'notes':['Disk sources are exact appended regions with original execution path in raw receipt; required info scoped by actual region, historical diagnostics also checked for errors/warnings.','Raw run_code uses diagnostics and has no partial field. Disk success requires partial=false.','No article/search result bodies stored; exact web request/hash/bytes/status and locators only.']}
put('verification.json',v)
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append({'source':str(p),'destination':dest,'sha256':sha(p),'bytes':p.stat().st_size})
put('copy-manifest.json',{'declaration':N,'files':files})
