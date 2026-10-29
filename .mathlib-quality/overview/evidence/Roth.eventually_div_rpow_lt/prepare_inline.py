from pathlib import Path
import json,re,hashlib
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.eventually_div_rpow_lt'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
meta=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
def get(n):return next(x for x in meta if x['name']==n)
names=['Roth.reduction','Roth.exists_reduced_approx','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff']
callers=[]
for n in names:
 m=get(n);src=m['source']+'\n';a='caller-'+n+'.lean.txt';(D/a).write_text(src)
 callers.append(dict(name=n,file=m['file'],line=m['line'],end_line=m['end_line'],archive=a,sha256=hashlib.sha256(src.encode()).hexdigest(),target_occurrences=src.count('eventually_div_rpow_lt')))
put('callers.json',dict(source_explicit=callers,source_explicit_count=3,source_call_count=3,external_file_count=1))
orig=get(N)['source'];proof=orig.split(' := by\n',1)[1]
iso=(D/'isolated-executed.lean.txt').read_text();generic=iso[iso.index('theorem eventual_filter'):iso.index('theorem nonpositive')]
allcode=(D/'disk-prefix.lean.txt').read_text()
for route in ['Literal','Generic']:
 ns='Decay270'+route
 allcode+='\nnamespace '+ns+'\nopen Roth Filter\n'
 if route=='Generic':allcode+=generic+'\n'
 allcode+=get('Roth.approxSet_num_den_mem_aux')['source']+'\n'
 # Original private LeanEval helper retained completely, only declaration basename namespace changes.
 h=get('LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux')['source']
 allcode+='open Real\n'+h+'\n'
 for n in names:
  src=get(n)['source'];base=n.split('.')[-1]
  if n.startswith('LeanEval.'):
   src=src.replace('IsDiophantine x','LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x')
  src=src.replace('IsDiophantine x ↔ ∀ {κ : ℝ},','IsDiophantine x ↔\n      ∀ {κ : ℝ},')
  binder="  have bound {M κ κ' : ℝ} (hκ : κ' < κ) :\n      ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by\n"
  if route=='Literal':binder+='\n'.join('  '+line for line in proof.splitlines())+'\n'
  else:binder+='    exact recovery hκ\n'
  src=src.replace(' := by\n',' := by\n'+binder,1).replace('Roth.eventually_div_rpow_lt','bound').replace('eventually_div_rpow_lt','bound')
  allcode+=src+'\n'
  allcode+='example : @'+n+' =\n    @'+base+' := Subsingleton.elim _ _\n#print axioms '+base+'\n'
 allcode+='end '+ns+'\n'
allcode+='''
run_cmd do
  let env ← Lean.getEnv
  let ci ← Lean.getConstInfo `Roth.eventually_div_rpow_lt
  let rootDeps := (ci.value? (allowOpaque := true)).get!.getUsedConstants.toList
  let project := rootDeps.filter fun n ↦ n.toString.startsWith "Roth."
  Lean.logInfo m!"DECAY270_DIRECT_PROJECT_BODY: {project}"
  let projectTy := ci.type.getUsedConstants.toList.filter fun n ↦ n.toString.startsWith "Roth."
  Lean.logInfo m!"DECAY270_DIRECT_PROJECT_TYPE: {projectTy}"
  let targets := #[`Decay270Literal.reduction, `Decay270Literal.exists_reduced_approx,
    `Decay270Literal.isDiophantine_iff, `Decay270Generic.reduction,
    `Decay270Generic.exists_reduced_approx, `Decay270Generic.isDiophantine_iff]
  for n in targets do
    let mut todo := [n]
    let mut seen : List Lean.Name := []
    while !todo.isEmpty do
      let k := todo.head!
      todo := todo.tail!
      unless seen.contains k do
        seen := k :: seen
        if k == `Roth.eventually_div_rpow_lt ||
            k.toString.startsWith "Roth.eventually_div_rpow_lt." then
          throwError "DECAY270_CIRCULAR: {n} via {k}"
        if let some info := env.find? k then
          if let some v := info.value? (allowOpaque := true) then
            let deps := v.getUsedConstants.toList.filter fun d ↦
              d.toString.startsWith "Roth." || d.toString.startsWith "_private.Roth." ||
                (d.toString.splitOn "Decay270").length > 1
            todo := deps ++ todo
    Lean.logInfo m!"DECAY270_INLINE_CLOSURE_NO_TARGET: {n}"
'''
bad=[(i+1,len(l),l)for i,l in enumerate(allcode.splitlines())if len(l)>100]
assert not bad,bad
(D/'inline-executed.lean.txt').write_text(allcode)

import hashlib
r=dict(id='inline01',operation='diagnostics',source='inline-executed.lean.txt',source_sha256=hashlib.sha256(allcode.encode()).hexdigest(),receipt='inline-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
put('root-requests/inline01.json',r)
print('Prepared six fullcaller bodies: literal local proof and own generic route; signatures retained')
