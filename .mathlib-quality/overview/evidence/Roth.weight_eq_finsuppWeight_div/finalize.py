from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.weight_eq_finsuppWeight_div'
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
accepted=[]
def add(label,stem,source=None,region=1,required=[],fmt='raw'):
 s=source or f'weight-eq-finsupp-{stem}-executed.lean.txt';accepted.append(dict(label=label,source=s,source_sha256=sha(D/s),receipt=f'weight-eq-finsupp-{stem}-receipt.json',format=fmt,native_region_start_line=region,required_info=required,guard=N if fmt=='raw' else None))
add('original-and-audit','original-audit','weight-eq-finsupp-original-executed.lean.txt',1525,['Roth.weight_eq_finsuppWeight_div','WEIGHT_EQ_FINSUPP142_AUDIT: requested=293; unique=293','WEIGHT_EQ_FINSUPP142_AUDIT_PRESENT: present=293; values=293'],fmt='disk')
add('mathlib-only-generic-map-cast-scale-clearing','mathlib-final',required=["'WeightDiv142.mapWeight' depends on axioms:","'WeightDiv142.castWeight' depends on axioms:","'WeightDiv142.scaleWeight' depends on axioms:","'WeightDiv142.clear' depends on axioms:"])
add('support-local-CharZero-and-zero-guards','extra-initial',required=["'WeightDiv142Extra.supportClear' depends on axioms:","'WeightDiv142Extra.mixedZero' depends on axioms:","'WeightDiv142Extra.zeroIndex' depends on axioms:"])
add('strong-support-local-arbitrary-characteristic','strong',required=["'WeightDivStrong142.supportClear' depends on axioms:"])
add('actual-original-replacement-and-entire-sole-caller','target',region=1847,required=["'WeightDivTarget142.replacement' depends on axioms:","'WeightDivTarget142.caller' depends on axioms:"],fmt='disk')
rejected=[dict(source=f'weight-eq-finsupp-mathlib-{s}-executed.lean.txt',receipt=f'weight-eq-finsupp-mathlib-{s}-receipt.json',reason=r) for s,r in [('initial','Unused CharZero helper section-variable linter warnings and parser failure at nested exact_mod_cast term; recovered sorryAx, rejected.'),('second','congr1 left LinearMap equality rather than generator function equality; rejected.')]]
dump('verification.json',dict(declaration=N,accepted=accepted,rejected=rejected,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],audit=dict(source='weight-eq-finsupp-audit-executed.lean.txt',receipt='weight-eq-finsupp-original-audit-receipt.json',native_region_start_line=1528),caller_source='weight-eq-finsupp-target-executed.lean.txt',execution_paths=dict(disk='.lake/roth-overview-session/GenWronskianChecks.lean',isolated='lean_run_code stable7-import virtual context'),preparation_only=['probe.lean.txt','extra-probe.lean.txt','strong-probe.lean.txt','target-probe.lean.txt'],rejected_recovered_sorryAx_never_accepted=True))
dump('direct-consumers.json',dict(count=1,consumers=['Roth.index_eq_weightedOrder_div']))
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
dump('copy-manifest.json',dict(declaration=N,files=files))
