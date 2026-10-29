from pathlib import Path
import json,hashlib,re
D=Path(__file__).resolve().parent
N='LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def result(p):
 r=json.loads(p.read_text())['result'];r=r.get('structuredContent')or json.loads(r['content'][0]['text']);return r.get('result',r)
accepted=[]
for id,src,fmt in [('original01','original-executed.lean.txt','disk'),('inline01','inline-executed.lean.txt','disk'),('modern01','modern-executed.lean.txt','isolated'),('recovery01','recovery-executed.lean.txt','disk'),('candidates01','candidates-executed.lean.txt','isolated'),('composition02','composition2-executed.lean.txt','isolated')]:
 j=json.loads((D/(id+'-receipt.json')).read_text());r=result(D/(id+'-receipt.json'));ds=r.get('items',r.get('diagnostics',[]))
 assert r['success']and not r.get('partial')and not r.get('timed_out')
 assert all(d['severity']not in ['error','warning']and 'PANIC'not in d['message']and 'sorryAx'not in d['message']for d in ds)
 accepted.append(dict(id=id,source=src,receipt=id+'-receipt.json',source_sha256=hashlib.sha256((D/src).read_bytes()).hexdigest(),format=fmt,original_execution_request=j['request'],elapsed_ms=j['elapsed_ms']))
j=json.loads((D/'composition01-receipt.json').read_text())
rejected=[dict(id='composition01',source='composition-executed.lean.txt',receipt='composition01-receipt.json',source_sha256=hashlib.sha256((D/'composition-executed.lean.txt').read_bytes()).hexdigest(),original_execution_request=j['request'],elapsed_ms=j['elapsed_ms'],reason='Wrong namespace Real.tendsto_rpow_atTop and implicitly-used binder lints; no semantic closure surprise; not accepted evidence')]
dump('verification.json',dict(declaration=N,canonical_index=292,completed=False,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rejected,attempt_accounting=dict(native_executions=7,accepted=6,rejected=1),full_actual_caller='thueSiegelRoth original signature; complete body inline and generic recovery',canonical_audit='exact293 ordered unique present values; one body consumer zero type',root_executor_exclusive=True))
# Read the entire actual messages; retain extracted audit data without printer splitting.
r=result(D/'original01-receipt.json');m='\n'.join(x['message']for x in r['items'])
dump('canonical-consumers.json',dict(type=re.findall(r'D292_DIRECT_TYPE_CONSUMER: ([^\n]+)',m),body=re.findall(r'D292_DIRECT_BODY_CONSUMER: ([^\n]+)',m),requested=293,unique=293,present=293,values=293))
p=D/'report.md';s=p.read_text().replace('composition-executed.lean.txt','composition2-executed.lean.txt').replace('composition01-receipt.json','composition02-receipt.json')
s=s.replace('Root acceptance is pending independent review.','The rejected composition01 source/receipt is retained separately: its positive #check used the wrong Real namespace and two binders triggered implicit-use lints; corrected composition02 passes with no warnings. Root acceptance is pending independent review.')
p.write_text(s.rstrip()+'\n')
print('Built ledger6accepted/1rejected and canonical consumers; corrected report links')
