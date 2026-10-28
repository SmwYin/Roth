from pathlib import Path
import re
D=Path(__file__).resolve().parent;R=Path.cwd()
def transform(s,ns):
 b=s[s.index('namespace Roth'):].replace('namespace Roth','namespace '+ns+'\nopen Roth',1).replace('end Roth','end '+ns)
 if ns=='Eta231Inline':
  b=b.replace('/-- The parameter `η = 10^m δ^{(1/2)^m}`. Source: §6, eq. (36). -/\n','')
  b=b.replace('noncomputable def eta (δ : ℝ) (m : ℕ) : ℝ := 10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)','')
 b=b.replace('eta δ m','(10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m))')
 b=b.replace('[eta, ','[').replace('[eta]','[]').replace(', eta,',',')
 if ns=='Eta231MainInline':
  for n in ['exists_delta_bound','eta_lt_gam_iff','main_lemma']:b=re.sub(r'\b'+n+r'\b','Eta231Inline.'+n,b)
 assert not re.search(r'\beta\b',b)
 return b
body=transform((D/'source-MainLemma.lean.txt').read_text(),'Eta231Inline')
main=transform((D/'source-Main.lean.txt').read_text(),'Eta231MainInline')
checks='''
example : @Roth.exists_delta_bound = @Eta231Inline.exists_delta_bound := rfl
example : @Roth.eta_lt_gam_iff = @Eta231Inline.eta_lt_gam_iff := rfl
example : @Roth.main_lemma = @Eta231Inline.main_lemma := rfl
example : @Roth.exists_delta = @Eta231MainInline.exists_delta := rfl
run_cmd Lean.Elab.Command.liftTermElabM do
'''
for mod,ns,names in [('MainLemma','Eta231Inline',['theta_lt_eta_of_sq_log_bound_aux','exists_auxiliary_polynomial_with_index_gap_aux']),('Main','Eta231MainInline',['exists_roth_parameters_aux','one_lt_roth_eval_bound_aux'])]:
 for n in names:
  checks+='  do\n    let old ← Lean.getConstInfo (Lean.mkPrivateNameCore `Roth.'+mod+'\n      `Roth.'+n+')\n    let new ← Lean.getConstInfo ``'+ns+'.'+n+'\n    unless ← Lean.Meta.isDefEq old.type new.type do\n      throwError "ETA231_INLINE_SIGNATURE_MISMATCH"\n'
checks+='  Lean.logInfo "ETA231_INLINE_ALL8_ORIGINAL_SIGNATURES: PASS"\n'
for ns,names in [('Eta231Inline',['exists_delta_bound','eta_lt_gam_iff','theta_lt_eta_of_sq_log_bound_aux','exists_auxiliary_polynomial_with_index_gap_aux','main_lemma']),('Eta231MainInline',['exists_delta','exists_roth_parameters_aux','one_lt_roth_eval_bound_aux','roth_of_isIntegral'])]:
 checks+='namespace '+ns+'\n'+'\n'.join('#print axioms '+n for n in names)+'\nend '+ns+'\n'
code=(D/'disk-prefix.lean.txt').read_text()+body+'\n'+main+'\n'+checks
lines=[]
for l in code.splitlines():
 while len(l)>100:
  pos=l.rfind(' ',0,99);lines.append(l[:pos]);l='      '+l[pos+1:]
 lines.append(l)
code='\n'.join(lines)+'\n';assert max(map(len,code.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print('Prepared exact full two-module inline replay',len(lines),'lines; eight signatures plus kernel-only consumer replay.')
print('\n'.join(code.splitlines()[-60:]))
