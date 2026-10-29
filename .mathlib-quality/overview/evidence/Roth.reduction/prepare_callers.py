from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
meta=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
def src(n):return next(x['source'] for x in meta if x['name']==n)
prefix=(D/'disk-prefix.lean.txt').read_text()
target=src('Roth.reduction');caller=src('Roth.roth')
s=prefix+'''namespace Reduction271Inline
open Roth
'''+target+ '\n'+caller+'''
#print axioms roth
end Reduction271Inline
namespace Reduction271Replacement
open Roth
'''
gen=target.replace('theorem reduction','theorem threshold',1).replace('{κ : ℝ} (hκ : 2 < κ)','{t κ : ℝ} (hκ : t < κ)').replace('∧ 2 < κ\' ∧','∧ t < κ\' ∧').replace('(κ + 2)','(κ + t)')
s+=gen+'\n'+target[:target.index(':= by')]+''' := by
  exact threshold hα halg hκ hinf
'''+caller+'''
#print axioms threshold
#print axioms reduction
#print axioms roth
end Reduction271Replacement
run_cmd do
  let env ← Lean.getEnv
  for n in #[`Reduction271Inline.roth, `Reduction271Replacement.roth,
      `Reduction271Replacement.threshold] do
    let mut todo : List Lean.Name := [n]
    let mut seen : List Lean.Name := []
    while !todo.isEmpty do
      let c := todo.head!
      todo := todo.tail!
      if !seen.contains c then
        seen := c :: seen
        if c == `Roth.reduction || c == `Roth.roth then
          throwError "RED271_CIRCULAR: {n} reaches {c}"
        if let some ci := env.find? c then
          if let some v := ci.value? (allowOpaque := true) then
            todo := v.getUsedConstants.toList ++ todo
    Lean.logInfo m!"RED271_NONCIRCULAR: {n}; checked={seen.length}"
'''
p=D/'caller-executed.lean.txt';p.write_text(s)
assert max(map(len,s.splitlines()))<=100
r=dict(id='caller01',operation='diagnostics',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='caller-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
(D/'root-requests/caller01.json').write_text(json.dumps(r,indent=2));(D/'caller-Roth.roth.lean.txt').write_text(caller)
print('Full original caller tested twice: exact reduction body inline; arbitrary threshold specialization')
