from pathlib import Path
import re,json
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(R/'Roth/Main.lean').read_text();b=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Main266Inline\nopen Roth',1).replace('end Roth','end Main266Inline')
t=(R/'Roth/MainLemma.lean').read_text();body=t[t.index(' := by',t.index('theorem main_lemma'))+7:t.rindex('\nend Roth')].strip('\n')
body=body.replace('exists_auxiliary_polynomial_with_index_gap_aux','auxgap266').replace('exists_hasseDeriv_index_eval_bound_aux','selectInline266').replace('hW hh','hW hcop')
# The exact expected existential type is supplied by the actual obtain command.
concl=t[t.index(' : ∃ Q',t.index('theorem main_lemma'))+3:t.index(' := by',t.index('theorem main_lemma'))]
new='show '+concl+' from by\n'+'\n'.join('    '+l for l in body.splitlines())
a='main_lemma hf hfα hA hδ0 hδm hrlast h31b h32 h33 hcop';assert b.count(a)==1
b=b.replace(a,new)
setup='''
open Lean Elab Term in
elab "auxgap266" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.exists_auxiliary_polynomial_with_index_gap_aux)
open Lean Elab Term in
elab "selectInline266" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.exists_hasseDeriv_index_eval_bound_aux)
'''
b=b.replace('open Roth\n','open Roth\n'+setup,1)
checks='''
namespace Main266Inline
#print axioms one_lt_roth_eval_bound_aux
#print axioms roth_of_isIntegral
example : @Roth.roth_of_isIntegral = @roth_of_isIntegral := rfl
run_cmd Lean.Elab.Command.liftTermElabM do
  let original := Lean.mkPrivateNameCore `Roth.Main `Roth.one_lt_roth_eval_bound_aux
  let ci ← Lean.getConstInfo ``one_lt_roth_eval_bound_aux
  let src ← Lean.getConstInfo original
  unless ← Lean.Meta.isDefEq ci.type src.type do
    throwError "MAIN266_CALLER_SIGNATURE_CHANGED"
  let some val := ci.value? (allowOpaque := true) | throwError "MAIN266_NO_CALLER_BODY"
  if val.getUsedConstants.any (fun c ↦ c == `Roth.main_lemma) then
    throwError "MAIN266_INLINE_STILL_CALLS_TARGET"
  Lean.logInfo "MAIN266_INLINE: full actual caller body inlined; original signatures retained"
end Main266Inline
'''
whole=(D/'disk-prefix.lean.txt').read_text()+b+'\n'+checks
assert max(map(len,whole.splitlines()))<=100,[(i,len(l),l)for i,l in enumerate(whole.splitlines(),1)if len(l)>100]
(D/'inline-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
print('Prepared',len(whole.splitlines()),'lines, width',max(map(len,whole.splitlines())))
print('\n'.join(whole.splitlines()[475:510]));print(checks)
