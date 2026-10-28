from pathlib import Path
import re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.four_lt_rpow')
a=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
b=(R/'Roth/Main.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
t=(D/'target-excerpt.lean.txt').read_text().strip()
# Remove only assigned target, retain the rest of both complete modules.
a=a.replace(t,'')
start=a.index('/-- The bound `3 ≤ δ² log q_1`')
end=a.index('/-- If `2 ≤ q_1',start)
a=a[:start]+a[end:]
# Rebind the same statement as a local proof inside each actual caller.
local=t.replace('theorem four_lt_rpow','have numericalBound',1)
local='\n'.join('  '+ln if i<2 else '  '+ln for i,ln in enumerate(local.splitlines()))+'\n'
# The local binder shadows delta/q/r by introducing fresh implicit parameters, as original.
for module,name in [('a','exists_mem_RSet_le_index_of_log_bound_aux'),('b','roth_product_bound_aux')]:
 s=a if module=='a' else b
 start=s.index('private lemma '+name)
 end=s.index(':= by\n',start)+len(':= by\n')
 s=s[:end]+local+s[end:]
 # only original use references remain after deletion of target.
 s=s.replace('four_lt_rpow hδ0','numericalBound hδ0')
 if module=='a':a=s
 else:b=s
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Four238Inline\nopen Roth\n'+a+b+'\nend Four238Inline\n'
# Expose scratch private theorems as public for kernel signature verification.
s=s.replace('private lemma ','lemma ').replace('private theorem ','theorem ')
pairs=[('Roth.MainLemma','Roth.exists_mem_RSet_le_index_of_log_bound_aux'),('Roth.Main','Roth.roth_product_bound_aux')]
s+='\nrun_cmd Lean.Elab.Command.liftTermElabM do\n  let pairs := #[\n'
arr=[]
for mod,nm in pairs:arr.append('    (Lean.mkPrivateNameCore `'+mod+' `'+nm+',\n      `Four238Inline.'+nm.split('.')[-1]+')')
for nm in ['main_lemma','roth_of_isIntegral','roth','roth_rat']:arr.append('    (`Roth.'+nm+', `Four238Inline.'+nm+')')
s+=',\n'.join(arr)+']\n'
s+='''  for (oldName, newName) in pairs do
    let old ← Lean.getConstInfo oldName
    let new ← Lean.getConstInfo newName
    unless ← Lean.Meta.isDefEq old.type new.type do throwError "FOUR238_INLINE_TYPE: {oldName}"
    Lean.logInfo m!"FOUR238_INLINE_SIGNATURE_IDENTICAL: {oldName}"
    if (new.value? (allowOpaque := true)).any (fun e ↦
        e.getUsedConstants.contains `Roth.four_lt_rpow) then
      throwError "FOUR238_INLINE_TARGET_REMAINING: {newName}"
'''
for nm in ['exists_mem_RSet_le_index_of_log_bound_aux','roth_product_bound_aux','main_lemma','roth_of_isIntegral','roth','roth_rat']:s+='#print axioms Four238Inline.'+nm+'\n'
assert 'theorem four_lt_rpow'not in s and 'four_lt_rpow hδ0'not in s
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s)
print('Prepared full two modules; assigned theorem removed, numerical proof inside each caller; width PASS')
