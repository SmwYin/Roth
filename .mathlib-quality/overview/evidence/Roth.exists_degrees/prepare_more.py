from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
meta=json.loads((D/'target-metadata.json').read_text());sig=meta['source'].split(':= by\n')[0]
allpos=sig.replace('theorem exists_degrees','theorem all_positive_delta').replace(' (hδ1 : δ ≤ 1)','')+''' := by
  exact Degrees278Generic.separated (0 : Fin m)
    (fun j ↦ Real.log_pos (by exact_mod_cast hq j))
    (div_pos hδ0 (by norm_num)) (div_pos (by norm_num) hδ0) hδ0 (by norm_num)
    (fun i j ↦ i.val + 1 = j.val) h50
'''
# The whitespace before := is harmless; full original signature retained for recovered theorem.
recover=sig.replace('theorem exists_degrees','theorem recovered').replace('(hδ1 : δ ≤ 1)','(_hδ1 : δ ≤ 1)')+''' := by
  exact all_positive_delta hδ0 hq h50
'''
body='namespace Degrees278Recovery\n'+allpos+'\n'+recover+'\nend Degrees278Recovery\n'
(D/'recovery-body.lean.txt').write_text(body)
s=(D/'disk-prefix.lean.txt').read_text()+'\n'+(D/'generic-body.lean.txt').read_text()+'\n'+body+'''
example : @Roth.exists_degrees = @Degrees278Recovery.recovered := Subsingleton.elim _ _
#print axioms Degrees278Recovery.all_positive_delta
#print axioms Degrees278Recovery.recovered
'''
def request(n,s,op='diagnostics'):
 assert max(map(len,s.splitlines()))<=100,[(i,len(l))for i,l in enumerate(s.splitlines(),1)if len(l)>100]
 p=D/(n+'-executed.lean.txt');p.write_text(s)
 q=dict(id=n+'01',operation=op,source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=n+'01-receipt.json',arguments={} if op=='run_code' else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
 (D/'root-requests'/(n+'01.json')).write_text(json.dumps(q,indent=2)+'\n')
request('recovery',s)
r=json.loads((D/'root-requests/local-abstract.json').read_text());r['id']='local-abstract-retry';r['receipt']='formal-abstract-local-retry.json';(D/'root-requests/local-abstract-retry.json').write_text(json.dumps(r,indent=2)+'\n')
print('Recovery and local retry ready')
