from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'composition-executed.lean.txt').read_text()+'''
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.boxFamily_finite
  for n in ci.type.getUsedConstants do
    if n.toString.startsWith "Roth." || n.toString.startsWith "_private.Roth." then
      Lean.logInfo m!"BOX245_TARGET_KERNEL_TYPE: {n}"
  let some v := ci.value? (allowOpaque := true) | throwError "BOX245_NO_TARGET_BODY"
  for n in v.getUsedConstants do
    if n.toString.startsWith "Roth." || n.toString.startsWith "_private.Roth." then
      Lean.logInfo m!"BOX245_TARGET_KERNEL_BODY: {n}"
  Lean.logInfo m!"BOX245_TARGET_COMPACT_BODY: {← Lean.Meta.ppExpr v}"
'''
assert max(map(len,s.splitlines()))<=100
(D/'dependencies-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('\n'.join(s.splitlines()[-13:]))
