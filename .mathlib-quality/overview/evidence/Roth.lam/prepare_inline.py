from pathlib import Path
import json,re
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'source-MainLemma.lean.txt').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace Lam229Inline\nopen Roth',1).replace('end Roth','end Lam229Inline')
body=body.replace('noncomputable def lam (δ : ℝ) (n m : ℕ) : ℝ := 4 * (1 + 3 * δ) * n * √(m : ℝ)','')
body=body.replace('lam δ n m','(4 * (1 + 3 * δ) * n * √(m : ℝ))').replace('[gam, lam]','[gam]')
body=body.replace('/-- The parameter `λ = 4(1 + 3δ) n m^{1/2}`. Source: §6, eq. (34). -/\n','')
assert not re.search(r'\blam\b',body)
m=(D/'source-Main.lean.txt').read_text();mbody=m[m.index('namespace Roth'):].replace('namespace Roth','namespace Lam229MainInline\nopen Roth',1).replace('end Roth','end Lam229MainInline')
mbody=mbody.replace('[gam, lam, eta,','[gam, eta,')
mbody=re.sub(r'\bgam\b','Lam229Inline.gam',mbody)
mbody=re.sub(r'\beta_lt_gam_iff\b','Lam229Inline.eta_lt_gam_iff',mbody)
assert not re.search(r'\blam\b',mbody)
checks='''
namespace Lam229Inline
#print axioms gam
#print axioms eta_lt_gam_iff
#print axioms exists_mem_RSet_le_index_of_log_bound_aux
end Lam229Inline
#print axioms Lam229MainInline.exists_delta
example : Roth.gam = Lam229Inline.gam := rfl
example : @Roth.eta_lt_gam_iff = @Lam229Inline.eta_lt_gam_iff := rfl
example : @Roth.exists_delta = @Lam229MainInline.exists_delta := rfl
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo (Lean.mkPrivateNameCore `Roth.MainLemma
    `Roth.exists_mem_RSet_le_index_of_log_bound_aux)
  let new ← Lean.getConstInfo ``Lam229Inline.exists_mem_RSet_le_index_of_log_bound_aux
  unless ← Lean.Meta.isDefEq old.type new.type do
    throwError "LAM229_INLINE_SIGNATURE_MISMATCH"
  Lean.logInfo "LAM229_INLINE_ALL4_ORIGINAL_SIGNATURES: PASS"
'''
code=(D/'disk-prefix.lean.txt').read_text()+body+'\n'+mbody+'\n'+checks
assert max(map(len,code.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print('Prepared full MainLemma and Main inline replay',len(code.splitlines()),'lines; all explicit target references removed; equality checks use original signatures.')
print('\n'.join(code.splitlines()[:30]));print('\n'.join(code.splitlines()[-25:]))
