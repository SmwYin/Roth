from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx')
s=(D/'original-executed.lean.txt').read_text();s=s[s.index('namespace Reduced274Audit'):]
s=s.replace('  Lean.logInfo m!"REDUCED274_AUDIT_PRESENT: present={present}; values={values}"','''  Lean.logInfo m!"REDUCED274_AUDIT_PRESENT: present={present}; values={values}"
  -- Traversal is restricted to this explicit project inventory; no all-mathlib traversal.
  let deps := fun (n : Lean.Name) => Id.run do
    let mut out : Array Lean.Name := #[]
    if let some ci := env.find? n then
      let mut used := ci.type.getUsedConstants
      if let some val := ci.value? (allowOpaque := true) then
        used := used.union val.getUsedConstants
      for k in used.toList do
        if names.contains k then out := out.push k
    return out
  let closure := fun (start : Lean.Name) => Id.run do
    let mut seen : Array Lean.Name := #[]
    let mut todo : Array Lean.Name := #[start]
    for _ in [:294] do
      let mut next : Array Lean.Name := #[]
      for n in todo do
        if !seen.contains n then
          seen := seen.push n
          next := next ++ deps n
      todo := next
    return seen
  Lean.logInfo m!"REDUCED274_PROJECT_CLOSURE: {closure target}"
  for n in names do
    if n != target && (closure n).contains target then
      Lean.logInfo m!"REDUCED274_TRANSITIVE_PROJECT_CONSUMER: {n}"
''')
s=(D/'disk-prefix.lean.txt').read_text()+'\n'+s
(D/'consumer-scope-executed.lean.txt').write_text(s)
q={'id':'consumers01','operation':'diagnostics','source':'consumer-scope-executed.lean.txt','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'consumers-receipt.json','original_audit':True,'arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}}
(D/'root-requests/consumers01.json').write_text(json.dumps(q,indent=2)+'\n')
assert max(map(len,s.splitlines()))<=100
