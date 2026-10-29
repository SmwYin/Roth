from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
old=(D/'generic4-body.lean.txt').read_text();new=old.replace('let K := max','let A := max').replace('K * ℓ','A * ℓ')
(D/'generic5-body.lean.txt').write_text(new)
for label in ['generic','recovery','callers','composition']:
 source=(D/(label+'4-executed.lean.txt')).read_text()
 if label=='composition':
  ob=old.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
  nb=new.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
 else:ob=old;nb=new
 assert ob in source;source=source.replace(ob,nb)
 assert max(map(len,source.splitlines()))<=100
 p=D/(label+'5-executed.lean.txt');p.write_text(source);op='run_code'if label in ['generic','composition']else'diagnostics'
 (D/'root-requests'/(label+'05.json')).write_text(json.dumps(dict(id=label+'05',operation=op,source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=label+'05-receipt.json',arguments={}if op=='run_code'else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
print('Round5 local scale renamed A to avoid shadowing field K; immutable05 ready')
