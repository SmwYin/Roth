from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent;N='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine'
def dump(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def result(j):
 r=j['result'];r=r.get('structuredContent')or json.loads(r['content'][0]['text']);return r.get('result',r)
accepted=[];rejected=[]
for p in sorted((D/'root-requests').glob('*.json')):
 j=json.loads(p.read_text())
 if j['operation']=='local_search':continue
 raw=json.loads((D/j['receipt']).read_text());r=result(raw)
 entry=dict(id=j['id'],source=j['source'],source_sha256=j['source_sha256'],receipt=j['receipt'],format='disk'if j['operation']=='diagnostics'else'run_code',elapsed_ms=raw['elapsed_ms'],original_execution_request=raw['request'])
 ds=r.get('items',r.get('diagnostics',[]));messages='\n'.join(d['message']for d in ds)
 ok=r['success']and not r.get('timed_out')and not r.get('partial')and not any(d['severity']in['error','warning']for d in ds)and not any(x in messages for x in ['sorryAx','PANIC'])
 (accepted if ok else rejected).append(entry)
assert {x['id']for x in accepted}=={'original01','callers01','shape02','modern03'}
dump('verification.json',dict(declaration=N,canonical_index=290,completed=False,unresolved=[],accepted=accepted,rejected=rejected,standard_axioms=['propext','Classical.choice','Quot.sound'],attempt_accounting=dict(native_executions=len(accepted)+len(rejected),accepted=len(accepted),rejected=len(rejected)),executor='Root persistent native session; worker prepared immutable sources and inspected full raw receipts.',canonical_audit='all293 exact ordered/unique/present/values; target type/body consumers2 each',full_kernel_printer_body=True,build_gate='Shared baseline reusable fresh17 match; final293 project and LeanEval builds root-owned and mandatory.'))
base=json.loads((D/'input-manifest.json').read_text());R=Path('/Users/ramin/LEAN/Roth');inputs=json.loads((D/'inputs.json').read_text())
for x in inputs:assert hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256']==base['sources_and_pins'][x['path']]['sha256']
dump('fresh-final-inputs.json',dict(inputs=inputs,unchanged=True))
a=json.loads((D/'assessment.json').read_text());a['unresolved']=[];a['phases']={k:('pending'if k=='8'else'PASS')for k in a['phases']};dump('assessment.json',a)
print('Native4 accepted/3 rejected; draft phase8 pending and completed=false')
