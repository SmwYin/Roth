from pathlib import Path
import json,re
D=Path(__file__).resolve().parent;R=Path.cwd()
def transform(s,ns):
 b=s[s.index('namespace Roth'):].replace('namespace Roth','namespace '+ns+'\nopen Roth',1).replace('end Roth','end '+ns)
 if ns=='Gam230Inline':
  b=b.replace('/-- The parameter `γ = (m - λ)/2`. Source: §6, eq. (35). -/\n','')
  b=b.replace('noncomputable def gam (δ : ℝ) (n m : ℕ) : ℝ := ((m : ℝ) - lam δ n m) / 2','')
 for n in ['f.natDegree','n']:
  b=b.replace('gam δ '+n+' m','(((m : ℝ) - lam δ '+n+' m) / 2)')
 b=b.replace('[gam, lam]','[lam]').replace('[gam, lam, eta,','[lam, eta,')
 if ns=='Gam230MainInline':
  for n in ['eta_lt_gam_iff','main_lemma']:b=re.sub(r'\b'+n+r'\b','Gam230Inline.'+n,b)
 assert not re.search(r'\bgam\b',b)
 return b
body=transform((D/'source-MainLemma.lean.txt').read_text(),'Gam230Inline')
main=transform((D/'source-Main.lean.txt').read_text(),'Gam230MainInline')
checks='''
example : @Roth.eta_lt_gam_iff = @Gam230Inline.eta_lt_gam_iff := rfl
example : @Roth.main_lemma = @Gam230Inline.main_lemma := rfl
example : @Roth.exists_delta = @Gam230MainInline.exists_delta := rfl
run_cmd Lean.Elab.Command.liftTermElabM do
'''
for mod,ns,names in [('MainLemma','Gam230Inline',['exists_mem_RSet_le_index_of_log_bound_aux','exists_auxiliary_polynomial_of_log_bound_aux','exists_auxiliary_polynomial_with_index_gap_aux']),('Main','Gam230MainInline',['exists_roth_parameters_aux','one_lt_roth_eval_bound_aux'])]:
 for n in names:
  checks+='  do\n    let old ← Lean.getConstInfo (Lean.mkPrivateNameCore `Roth.'+mod+'\n      `Roth.'+n+')\n    let new ← Lean.getConstInfo ``'+ns+'.'+n+'\n    unless ← Lean.Meta.isDefEq old.type new.type do\n      throwError "GAM230_INLINE_SIGNATURE_MISMATCH"\n'
checks+='  Lean.logInfo "GAM230_INLINE_ALL8_ORIGINAL_SIGNATURES: PASS"\n'
for ns,names in [('Gam230Inline',['eta_lt_gam_iff','exists_mem_RSet_le_index_of_log_bound_aux','exists_auxiliary_polynomial_of_log_bound_aux','exists_auxiliary_polynomial_with_index_gap_aux','main_lemma']),('Gam230MainInline',['exists_delta','exists_roth_parameters_aux','one_lt_roth_eval_bound_aux'])]:
 checks+='namespace '+ns+'\n'+'\n'.join('#print axioms '+n for n in names)+'\nend '+ns+'\n'
code=(D/'disk-prefix.lean.txt').read_text()+body+'\n'+main+'\n'+checks
assert max(map(len,code.splitlines()))<=135
# Expanded arithmetic occasionally needs line wrapping; whitespace only, no source proof changes.
code=code.replace('(((m : ℝ) - lam δ f.natDegree m) / 2)','((m - lam δ f.natDegree m) / 2)')
# wrap only at safe spaces after fixed commas or arithmetic term boundaries
lines=[]
for l in code.splitlines():
 while len(l)>100:
  pos=l.rfind(' ',0,99);lines.append(l[:pos]);l='      '+l[pos+1:]
 lines.append(l)
code='\n'.join(lines)+'\n'
assert max(map(len,code.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print('Prepared full two-module inline replay',len(lines),'lines; removed all gam tokens; eight signature checks.')
print('\n'.join(code.splitlines()[-65:]))
