from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index');R=Path('/Users/ramin/LEAN/Roth')
s=(D/'project-executed.lean.txt').read_text().replace('convert cost_bound hd hbase hC hx hw using 1 <;> congr 2 <;> ring','convert cost_bound hd hbase hC hx hw using 1\n  congr 2\n  ring')
p=D/'project2-executed.lean.txt';p.write_text(s)
def request(id,p,receipt):
 (D/f'root-requests/{id}.json').write_text(json.dumps({'id':id,'operation':'diagnostics','source':p.name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'receipt':receipt,'arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}},indent=2)+'\n')
request('project02',p,'project02-receipt.json')
main=(R/'Roth/Main.lean').read_text();helper=main[main.index('private lemma abs_prod_pow'):main.index('/-- If `Q` has index')]
caller=(D/'caller-excerpt.lean.txt').read_text()
# full exact caller signature/body; preserve all original premises.
inline=caller.replace('private lemma one_lt_roth_eval_bound_aux','lemma caller_inline')
target=(D/'target-excerpt.lean.txt').read_text().replace('theorem abs_eval_lt_of_le_index','have upper')
inline=inline.replace('  exact (one_le_prod_pow_mul_abs_eval','\n'.join('  '+l for l in target.splitlines())+'\n  exact (one_le_prod_pow_mul_abs_eval').replace('(abs_eval_lt_of_le_index hdmap','(upper hdmap')
generic=caller.replace('private lemma one_lt_roth_eval_bound_aux','lemma caller_generic').replace('abs_eval_lt_of_le_index hdmap hidx_strict.le hq0 hκ0 happ hqr hC','Taylor281Project.original_recovery hdmap hidx_strict.le hq0 hκ0 happ hqr (fun d _ ↦ hC d)')
p=D/'callers-executed.lean.txt';p.write_text(s+'\nnamespace Taylor281Caller\nopen Roth MvPolynomial\n'+helper+inline+'\n'+generic+'''
open Lean Elab Term in
elab "originalCaller281" : term => do
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.Main `Roth.one_lt_roth_eval_bound_aux)
example : @caller_inline = originalCaller281 := Subsingleton.elim _ _
example : @caller_generic = originalCaller281 := Subsingleton.elim _ _
#print axioms Taylor281Caller.caller_inline
#print axioms Taylor281Caller.caller_generic
run_cmd Lean.Elab.Command.liftTermElabM do
  for n in [`Taylor281Caller.caller_inline, `Taylor281Caller.caller_generic] do
    let ci ← Lean.getConstInfo n
    let some v := ci.value? (allowOpaque := true) | throwError "missing value"
    if v.getUsedConstants.contains `Roth.abs_eval_lt_of_le_index then
      throwError "TAY281_CALLER_STILL_USES_TARGET"
    Lean.logInfo m!"TAY281_CALLER_TARGET_FREE: {n}"
end Taylor281Caller
''');request('callers01',p,'callers01-receipt.json')
print('Prepared project02 and full caller inline/generic sources')
