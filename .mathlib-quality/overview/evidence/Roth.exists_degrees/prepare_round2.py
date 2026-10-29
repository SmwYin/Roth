from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
s=(D/'generic-body.lean.txt').read_text().replace('[Fintype ι]','[Finite ι]')
s=s.replace('  classical\n','  classical\n  let : Fintype ι := Fintype.ofFinite ι\n',1)
s=s.replace('Nat.ceil_lt_add_one (by positivity)','Nat.ceil_lt_add_one\n      (div_nonneg (mul_nonneg (Nat.cast_nonneg _) (hℓ b).le) (hℓ j).le)')
s=s.replace('exact add_lt_add_left (hsmall j) _','linarith only [hsmall j]')
s=s.replace("    rw [mul_div_assoc, mul_comm (r j : ℝ) c, mul_div_assoc] at h'", "    have hm : (r j : ℝ) * (c / δ) = c * (r j / δ) := by ring\n    rw [hm] at h'")
s=s.replace('  · exact mul_le_mul_of_nonneg_right (add_le_add_left (min_le_left _ _) 1) (by positivity)', '''  · exact mul_le_mul_of_nonneg_right (add_le_add le_rfl (min_le_left _ _))
      (mul_nonneg (Nat.cast_nonneg _) (hℓ b).le)''')
# newly split ceil line still too wide? formatting checked below.
(D/'generic2-body.lean.txt').write_text(s)
def req(label,source,op):
 assert max(map(len,source.splitlines()))<=100,[(i,len(l))for i,l in enumerate(source.splitlines(),1)if len(l)>100]
 p=D/(label+'2-executed.lean.txt');p.write_text(source)
 (D/'root-requests'/(label+'02.json')).write_text(json.dumps(dict(id=label+'02',operation=op,source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=label+'02-receipt.json',arguments={}if op=='run_code'else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
pre=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.exists_degrees\n'
req('generic',pre+s+'\n#print axioms Degrees278Generic.balanced\n#print axioms Degrees278Generic.separated\n','run_code')
for label in ['recovery','callers','composition']:
 old=(D/(label+'-executed.lean.txt')).read_text()
 oldbody=(D/'generic-body.lean.txt').read_text()
 if label=='composition':
  oldbody=oldbody.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
  newbody=s.replace('Degrees278Generic','Degrees278Composition').replace('  classical\n','  fail_if_success solve | simp\n  fail_if_success solve | exact?\n  classical\n',1)
 else:newbody=s
 assert oldbody in old
 req(label,old.replace(oldbody,newbody),'run_code'if label=='composition'else'diagnostics')
print('Immutable round2: generic02, recovery02, callers02, composition02')
