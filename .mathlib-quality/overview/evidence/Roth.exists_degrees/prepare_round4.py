from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
oldbody=(D/'generic3-body.lean.txt').read_text();s=oldbody.replace('\n  [Archimedean K]','')
(D/'generic4-body.lean.txt').write_text(s)
def req(label,source,op):
 assert max(map(len,source.splitlines()))<=100
 p=D/(label+'4-executed.lean.txt');p.write_text(source)
 (D/'root-requests'/(label+'04.json')).write_text(json.dumps(dict(id=label+'04',operation=op,source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=label+'04-receipt.json',arguments={}if op=='run_code'else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
pre=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.exists_degrees\n'
req('generic',pre+s+'\n#check @FloorRing.archimedean\n#print axioms Degrees278Generic.balanced\n#print axioms Degrees278Generic.separated\n','run_code')
for label in ['recovery','callers','composition']:
 old=(D/(label+'3-executed.lean.txt')).read_text()
 if label=='composition':
  ob=oldbody.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
  nb=s.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
 else:ob=oldbody;nb=s
 assert ob in old
 new=old.replace(ob,nb)
 if label=='composition':new+='\n#check @Nat.ceil_lt_mul\n#check @Nat.ceil_le_mul\n'
 req(label,new,'run_code'if label=='composition'else'diagnostics')
print('Final04 no redundant Archimedean; candidate checks added composition04')
