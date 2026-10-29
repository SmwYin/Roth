from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
s=(D/'disk-prefix.lean.txt').read_text()
a=(D/'original-executed.lean.txt').read_text();a=a[a.index('  let names : Array Lean.Name := #['):a.index('  unless names.size')]
s+='''
#print axioms Roth.eventually_div_rpow_lt
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.eventually_div_rpow_lt
'''+a+'''
  Lean.logInfo m!"DECAY270_SIMP_MEMBER: {← Lean.Meta.isInSimpSet `simp target}"
  let project (n : Lean.Name) := n.toString.startsWith "Roth." ||
    n.toString.startsWith "_private.Roth." || n.toString.startsWith "LeanEval." ||
    n.toString.startsWith "_private.Roth.LeanEval."
  let closure (n : Lean.Name) := Id.run do
    let mut todo := [n]
    let mut seen : List Lean.Name := []
    while !todo.isEmpty do
      let k := todo.head!
      todo := todo.tail!
      unless seen.contains k do
        seen := k :: seen
        if let some ci := env.find? k then
          let deps := ci.type.getUsedConstants.toList ++
            ((ci.value? (allowOpaque := true)).map (·.getUsedConstants.toList)).getD []
          todo := deps.filter project ++ todo
    return seen
  Lean.logInfo m!"DECAY270_PROJECT_CLOSURE: {closure target}"
  for n in names do
    if n != target && (closure n).contains target then
      Lean.logInfo m!"DECAY270_TRANSITIVE_CONSUMER: {n}"
  Lean.logInfo "DECAY270_SCOPE_COMPLETE"
'''
assert max(map(len,s.splitlines()))<=100
(D/'scope-executed.lean.txt').write_text(s)
r=dict(id='scope01',operation='diagnostics',source='scope-executed.lean.txt',source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='scope-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
(D/'root-requests/scope01.json').write_text(json.dumps(r,indent=2)+'\n')
p=json.load(open('.mathlib-quality/overview/progress.json'));(D/'accepted-YES.json').write_text(json.dumps([x for x in p['completed_declarations'] if x['verdict'].startswith('YES')],indent=2)+'\n')
print('Scope exact293 project type+value transitive closure and simp membership prepared')
