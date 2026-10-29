from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd();s=(D/'source-MainLemma.lean.txt').read_text();b=s[s.index('namespace Roth'):]
a=b.index('/-- For polynomials over a seminormed ring');e=b.index('/-- Integer polynomials with coordinate',a);b=b[:a]+b[e:]
b=b.replace('    norm_coeff_modByMonic_le (by simpa','''    Rem243Generic.size_remainder norm norm_zero norm_nonneg norm_sub_le norm_mul_le
      (by simpa''')
b=b.replace('namespace Roth','namespace Rem243Project\nopen Roth',1).replace('end Roth','end Rem243Project')
g=(D/'isolated-executed.lean.txt').read_text().split('namespace Rem243Isolated\n',1)[1].split('#print axioms size_remainder',1)[0]
checks='''
elab "oldCaller243" : term => do
  Lean.Meta.mkConstWithFreshMVarLevels (Lean.mkPrivateNameCore `Roth.MainLemma
    `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux)
example : oldCaller243 = @Rem243Project.abs_coeff_diag_hasseDeriv_modByMonic_le_aux := rfl
#print axioms Rem243Project.abs_coeff_diag_hasseDeriv_modByMonic_le_aux
#print axioms Rem243Project.main_lemma
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo ``Rem243Project.abs_coeff_diag_hasseDeriv_modByMonic_le_aux
  let some v := ci.value? (allowOpaque := true) | throwError "REM243_MISSING_CALLER"
  if v.getUsedConstants.any (fun c ↦ c == `Roth.norm_coeff_modByMonic_le) then
    throwError "REM243_TARGET_NOT_REPLACED"
  Lean.logInfo "REM243_PROJECT: actual caller re-aimed; original signature retained"
'''
whole=(D/'disk-prefix.lean.txt').read_text()+'namespace Rem243Generic\n'+g+'end Rem243Generic\n'+b+checks
assert max(map(len,whole.splitlines()))<=100
(D/'project-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
print('Prepared exact fullmodule caller with generic size replacement')
