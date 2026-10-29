from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=[]
for label,src,rec,fmt,infos,axiom in [
('original','original-executed.lean.txt','original-receipt.json','disk',['DIMENSION275_FULL_TYPE:','DIM275_AUDIT: requested=293; unique=293','DIMENSION275_AUDIT_PRESENT: present=293; values=293'],True),
('callers','callers-executed.lean.txt','callers-receipt.json','disk',["'Dimension275Caller.replay' depends on axioms:"],True),
('consumers','consumer-scope2-executed.lean.txt','consumers2-receipt.json','disk',['DIMENSION275_PROJECT_CLOSURE:','DIMENSION275_TRANSITIVE_PROJECT_CONSUMER:','DIMENSION275_AUDIT_PRESENT: present=293; values=293'],False),
('generic','generic-executed.lean.txt','generic-receipt.json','run_code',["'Dimension275.generic' depends on axioms:","'Dimension275.recovered' depends on axioms:"],True),
('signed','signed-executed.lean.txt','signed-receipt.json','run_code',["'Dimension275Signed.generic' depends on axioms:","'Dimension275Signed.recovered' depends on axioms:","'Dimension275Signed.sharp_gap' depends on axioms:"],True),
('composition','composition2-executed.lean.txt','composition2-receipt.json','run_code',["'Dimension275Composition.checked' depends on axioms:"],True),
('shape','shape-executed.lean.txt','shape-receipt.json','run_code',["'Dimension275Shape.middle' depends on axioms:",'Real.tendsto_sqrt_atTop :'],True),
('replacementcaller','replacement-caller-executed.lean.txt','replacement-caller-receipt.json','disk',["'Dimension275ReplacementCaller.replay' depends on axioms:"],True)]:
 q=rd(rec);a.append({'label':label,'source':src,'receipt':rec,'source_sha256':sha(D/src),'format':fmt,'native_region_start_line':17 if fmt=='disk' else 20,'required_info':infos,'axiom_print_required':axiom,'original_execution_request':q['request'],'elapsed_ms':q['elapsed_ms']})
other=[]
for s,r in [('composition-executed.lean.txt','composition-receipt.json'),('consumer-scope-executed.lean.txt','consumers-receipt.json')]:other.append({'source':s,'receipt':r,'source_sha256':sha(D/s),'status':'rejected'})
v={'declaration':'Roth.exists_m','canonical_index':275,'completed':False,'unresolved':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'native_executor':'root exclusive; worker prepared exact sources and inspected complete raw returned results','accepted':a,'other_executions':other,'attempt_accounting':{'native_executions':10,'accepted':8,'rejected':2},'build_gate':'Reused clean2467job baseline with17freshmatching hashes; no file-boundary build due at275; next289'}
(D/'verification.json').write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
(D/'preparation-notes.json').write_text(json.dumps({'native_failures':['composition01: over-indented copied body parsed as command, recovered sorryAx; rejected and immutable','consumers01: Array.union not available; rejected and immutable'], 'pre_native_only':['original preparation width assertion failed twice, then fixed audit marker width; original declaration width intentionally preserved','shape preparation invocation typo path returned exit2; reran correct path exit0 before root dispatch'],'normalization':'Exact executed sources unchanged. Source snapshots exact. Any numbered blank-line excerpts omit artificial trailing whitespace; none used for execution.','limits':'No raised heartbeats/recursion limits, unsafe, native_decide, new axioms, or accepted partial output'},indent=2)+'\n')
print('verification prepared completedfalse, accepted8 rejected2')
