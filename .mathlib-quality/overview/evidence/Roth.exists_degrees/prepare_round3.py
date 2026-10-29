from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
oldbody=(D/'generic2-body.lean.txt').read_text()
s=oldbody.replace(' (hδ : 0 < δ)','').replace('ℝ','K')
s=s.replace('namespace Degrees278Generic\n','''namespace Degrees278Generic
variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [FloorRing K]
  [Archimedean K]
''',1)
(D/'generic3-body.lean.txt').write_text(s)
def req(label,source,op):
 assert max(map(len,source.splitlines()))<=100
 p=D/(label+'3-executed.lean.txt');p.write_text(source)
 (D/'root-requests'/(label+'03.json')).write_text(json.dumps(dict(id=label+'03',operation=op,source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=label+'03-receipt.json',arguments={}if op=='run_code'else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
pre=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.exists_degrees\n'
req('generic',pre+s+'\n#print axioms Degrees278Generic.balanced\n#print axioms Degrees278Generic.separated\n','run_code')
for label in ['recovery','callers','composition']:
 old=(D/(label+'2-executed.lean.txt')).read_text()
 if label=='composition':
  ob=oldbody.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
  nb=s.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
 else:ob=oldbody;nb=s
 assert ob in old
 new=old.replace(ob,nb).replace('(div_pos hδ0 (by norm_num)) (div_pos (by norm_num) hδ0) hδ0 (by norm_num)','(div_pos hδ0 (by norm_num)) (div_pos (by norm_num) hδ0) (by norm_num)')
 req(label,new,'run_code'if label=='composition'else'diagnostics')
print('Round3 field/Finite generalization and genuine drop hδ ready')
