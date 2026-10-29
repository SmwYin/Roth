from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
pfx=(D/'isolated-executed.lean.txt').read_text().split('#check_failure')[0]
s=pfx+'''#check_failure Roth.reduction
namespace Reduction271Scope
'''
meta=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
def src(n):return next(x['source'] for x in meta if x['name']==n)
s+=src('Roth.approxSet')+'\n'
# Exact composition probe before any same-result scratch theorem is in environment.
s+=src('Roth.reduction').replace('theorem reduction','theorem composition',1).replace(':= by', ''' := by
  fail_if_success solve | exact?
  fail_if_success solve | simp [approxSet]
  fail_if_success exact LiouvilleWith.nat_mul
  have exists_nat_mul_isIntegral := @IsAlgebraic.exists_integral_multiple
''',1) if False else ''
# Build original proof with local prerequisite have-blocks after automation attempts.
t=src('Roth.reduction');head,body=t.split(':= by',1)
s+=head.replace('theorem reduction','theorem composition',1)+''' := by
  fail_if_success solve | exact?
  fail_if_success solve | simp [approxSet]
  fail_if_success exact LiouvilleWith.nat_mul
'''
for n in ['Roth.exists_nat_mul_isIntegral','Roth.approxSet_den_le_finite','Roth.eventually_div_rpow_lt']:
 h,b=src(n).split(':= by',1);h=h.replace('theorem ','have ',1)
 s+='  '+h.strip()+' := by\n'+'\n'.join('  '+line for line in b.strip('\n').splitlines())+'\n'
s+=body+'\n'
s+='''example : ((0 : ℤ), (1 : ℕ)) ∈ approxSet (3 / 4) 0 ∧
    ¬ ((0 : ℤ), (1 : ℕ)) ∈ approxSet (2 * (3 / 4)) 0 := by
  norm_num [approxSet, Real.rpow_zero]
example (t : ℝ) : ¬ (t < (t + t) / 2) := by linarith
example : LiouvilleWith 1 (0 : ℝ) := liouvilleWith_one 0
#print axioms composition
end Reduction271Scope
'''
p=D/'scope-executed.lean.txt';p.write_text(s);print(max(map(len,s.splitlines())))
r=dict(id='scope01',operation='run_code',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='scope-receipt.json',arguments={});(D/'root-requests/scope01.json').write_text(json.dumps(r,indent=2))
# Direct project dependency extraction avoids original kernel pretty-printer elision.
s=(D/'disk-prefix.lean.txt').read_text()+'''run_cmd do
  let env ← Lean.getEnv
  let some ci := env.find? `Roth.reduction | throwError "missing target"
  let some v := ci.value? (allowOpaque := true) | throwError "missing value"
  let project := v.getUsedConstants.toList.filter (fun n ↦
    n.toString.startsWith "Roth." || n.toString.startsWith "_private.Roth.")
  Lean.logInfo m!"RED271_EXACT_PROJECT_DEPS: {project}"
'''
p=D/'dependencies-executed.lean.txt';p.write_text(s)
r=dict(id='dependencies01',operation='diagnostics',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='dependencies-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45));(D/'root-requests/dependencies01.json').write_text(json.dumps(r,indent=2))
