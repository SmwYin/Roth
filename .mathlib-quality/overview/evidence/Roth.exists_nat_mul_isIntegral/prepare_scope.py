from pathlib import Path
D=Path(__file__).resolve().parent
# Retain exact successful caller proofs, replace verbose audit with compact assertions.
s=(D/'inline-executed.lean.txt').read_text();s=s[:s.index('run_cmd Lean.Elab.Command.liftTermElabM')]+'''run_cmd Lean.Elab.Command.liftTermElabM do
  let target := `Roth.exists_nat_mul_isIntegral
  let ci ← Lean.getConstInfo target
  let some val := ci.value? (allowOpaque := true) | throwError "NAT268_NO_BODY"
  let project := val.getUsedConstants.toList.filter fun n ↦ n.toString.startsWith "Roth."
  Lean.logInfo m!"NAT268_DIRECT_PROJECT_BODY: {project}"
  let types := ci.type.getUsedConstants.toList.filter fun n ↦ n.toString.startsWith "Roth."
  Lean.logInfo m!"NAT268_DIRECT_PROJECT_TYPE: {types}"
  for n in #[`NatIntegral268Inline.manual_reduction, `NatIntegral268Inline.closure_reduction] do
    let ci ← Lean.getConstInfo n
    let some val := ci.value? (allowOpaque := true) | throwError "NAT268_NO_INLINE_BODY"
    if val.getUsedConstants.any (fun c ↦ c == target ||
        c.toString.startsWith "Roth.exists_nat_mul_isIntegral.") then
      throwError "NAT268_CIRCULAR_INLINE: {n}"
    Lean.logInfo m!"NAT268_INLINE_NO_TARGET: {n}"
    let project := val.getUsedConstants.toList.filter fun c ↦ c.toString.startsWith "Roth."
    Lean.logInfo m!"NAT268_CALLER_PROJECT_REFS: {n}: {project}"
'''
assert max(map(len,s.splitlines()))<=100
(D/'scope-executed.lean.txt').write_text(s)
Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print(s[s.index('run_cmd'):])
