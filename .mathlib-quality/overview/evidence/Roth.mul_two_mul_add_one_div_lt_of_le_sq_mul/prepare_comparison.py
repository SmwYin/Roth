from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
src=(D/'source-MainLemma.lean.txt').read_text();m=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=m.index('    apply (mul_le_mul_iff_of_pos_right (sq_pos_of_pos hδpos)).1',m.index('private lemma theta_lt_eta_of_sq_log_bound_aux'))
z=m.index('  simpa [eta] using Θ_lt',a)
m=m[:a]+'''    exact Budget253.weak (by positivity) hδm hL
'''+m[z:]
# This is a related nonconsumer; compile its full module with a NEW weak helper.
helpers=(D/'isolated-executed.lean.txt').read_text().split('namespace Budget253\n',1)[1].split('theorem strict_budget',1)[0]
helpers='namespace Budget253\n'+helpers+'end Budget253\n'
s=(D/'disk-prefix.lean.txt').read_text()+helpers+'namespace Budget253Comparison\nopen Roth\n'+m+'''
end Budget253Comparison
#print axioms Budget253Comparison.main_lemma
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
  let new ← Lean.getConstInfo `Budget253.recovery
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "BUDGET253_RECOVERY_TYPE_CHANGED"
  Lean.logInfo "BUDGET253_EXACT_RECOVERY"
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.main_lemma
  let new ← Lean.getConstInfo `Budget253Comparison.main_lemma
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "BUDGET253_MAIN_TYPE_CHANGED"
  Lean.logInfo "BUDGET253_COMPARISON_MAIN_SIGNATURE_IDENTICAL"
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Budget253.generic
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"BUDGET253_GENERIC_TYPE: {ci.type}"
'''
# In full copied module the renamed definition mainCoeffBound etc. can differ definitionally only.
assert max(map(len,s.splitlines()))<=100
(D/'comparison-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS full related nonconsumer module prepared; weak bound uses new scratch helper')
