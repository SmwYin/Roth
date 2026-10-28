from pathlib import Path
import json,hashlib,re
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'source-Main.lean.txt').read_text();b=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Gap235Inline\nopen Roth',1).replace('end Roth','end Gap235Inline')
a='((eta_lt_gam_iff 0 n m).mp (hδ₀\' 0 le_rfl hδ₀.le).2)'
c='''(show eta 0 m < gam 0 n m from by
        have h := (hδ₀' 0 le_rfl hδ₀.le).2
        dsimp only [gam, lam]
        linarith only [h])'''
assert a in b;b=b.replace(a,c)
a='((eta_lt_gam_iff _ _ _).1 h30)';c='''(show eta δ m < gam δ f.natDegree m from by
    dsimp only [gam, lam]
    linarith only [h30])'''
assert a in b;b=b.replace(a,c);assert 'eta_lt_gam_iff'not in b
checks='''
example : @Roth.exists_delta = @Gap235Inline.exists_delta := rfl
example : @Roth.roth_of_isIntegral = @Gap235Inline.roth_of_isIntegral := rfl
#print axioms Gap235Inline.exists_delta
#print axioms Gap235Inline.roth_of_isIntegral
run_cmd Lean.Elab.Command.liftTermElabM do
  for n in [``Gap235Inline.exists_delta, ``Gap235Inline.roth_of_isIntegral] do
    let ci ← Lean.getConstInfo n
    let some val := ci.value? (allowOpaque := true) | throwError "GAP235_NO_CALLER_VALUE"
    if val.getUsedConstants.any (fun c ↦ c == `Roth.eta_lt_gam_iff) then
      throwError "GAP235_INLINE_STILL_DIRECT_TARGET"
  Lean.logInfo "GAP235_INLINE: two actual caller proofs; original signatures retained"
'''
whole=(D/'disk-prefix.lean.txt').read_text()+b+'\n'+checks
assert max(map(len,whole.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(whole);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(whole)
rows=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());cs=[]
for name in ['Roth.exists_delta','Roth.roth_of_isIntegral']:
 row=next(x for x in rows if x['name']==name);cs.append(row)
(D/'callers.json').write_text(json.dumps(dict(executable_occurrences=2,distinct_declarations=2,external_to_file_files=1,callers=cs),ensure_ascii=False,indent=2)+'\n')
print('Prepared full original Main module with two actual inline derivations',len(whole.splitlines()))
print('\n'.join(whole.splitlines()[190:212]));print('\n'.join(whole.splitlines()[-54:]))
