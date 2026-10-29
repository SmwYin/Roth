from pathlib import Path
import subprocess,json,hashlib
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
b=(D/'target-excerpt.lean.txt').read_text().replace('mul_two_mul_add_one_div_lt_of_le_sq_mul','absence_probe').replace(':= by\n',':= by\n  fail_if_success exact?\n',1)
s=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul\nnamespace Budget253Controls\n'+b+'''
#print axioms absence_probe
example {K : Type*} [Semifield K] [LinearOrder K] [IsStrictOrderedRing K] : True := by
  fail_if_success have : ExistsAddOfLE K := inferInstance
  trivial
end Budget253Controls
'''
assert max(map(len,s.splitlines()))<=100;(D/'controls-executed.lean.txt').write_text(s)
for f,pat in [('current','mul_two_mul_add_one_div_lt_of_le_sq_mul'),('standard','mul_lt_of_lt_one_left|sq_pos_of_ne_zero|div_lt.*sq|sq.*div_lt'),('abstract','mul_lt_mul_iff_of_pos_right|mul_le_mul_iff_of_pos_right')]:
 cmd=['rg','-n',pat,'.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);(D/('search-'+f+'-rg.json')).write_text(json.dumps(dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)),indent=2))
cmd=['rg','-n','mul_two_mul_add_one_div_lt_of_le_sq_mul','.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);(D/'full-name-search.json').write_text(json.dumps(dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)),indent=2))
paths=['Mathlib/Algebra/Order/GroupWithZero/Defs.lean','Mathlib/Algebra/Order/GroupWithZero/Basic.lean','Mathlib/Algebra/Order/Ring/Unbundled/Basic.lean']
rows=[]
for path in paths:
 p=R/'.lake/packages/mathlib'/path;n='mathlib-'+path.replace('/','-')+'.txt';(D/n).write_bytes(p.read_bytes());rows.append(dict(path=path,archive=n,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'mathlib-inputs.json').write_text(json.dumps(rows,indent=2));print('PASS controls and pinned rg searches prepared')
