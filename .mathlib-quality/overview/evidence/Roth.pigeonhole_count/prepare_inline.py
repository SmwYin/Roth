from pathlib import Path
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
m=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=m.index('/-- For positive real `B`');b=m.index('/-- Finitely supported degree bounds and a strict');t=m[m.index('theorem pigeonhole_count'):b].rstrip();m=m[:a]+m[b:]
t=t.replace('theorem pigeonhole_count','have countBound',1)
needle='  exact exists_mem_RSet_le_index_aux hf hfα r B Cn J'
assert m.count(needle)==1
m=m.replace(needle,''.join('  '+l+'\n'for l in t.splitlines())+needle)
m=m.replace('(pigeonhole_count (Nat.cast_pos.2 hB)','(countBound (Nat.cast_pos.2 hB)')
assert 'pigeonhole_count'not in m
extra='''
end Count248Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  let env ← Lean.getEnv
  let short := `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux
  let oldName := Lean.mkPrivateNameCore `Roth.MainLemma short
  let newSuffix := short.replacePrefix `Roth `Count248Inline
  let newName := Lean.mkPrivateNameCore env.mainModule newSuffix
  let old ← Lean.getConstInfo oldName
  let new ← Lean.getConstInfo newName
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "COUNT248_INLINE_SIGNATURE_CHANGED"
  Lean.logInfo "COUNT248_INLINE_SIGNATURE_IDENTICAL"
  let some value := new.value? (allowOpaque := true)
    | throwError "COUNT248_INLINE_NO_VALUE"
  if value.getUsedConstants.contains `Roth.pigeonhole_count then
    throwError "COUNT248_INLINE_RETAINS_TARGET"
  Lean.logInfo "COUNT248_INLINE_NO_TARGET"
#print axioms Count248Inline.main_lemma
'''
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Count248Inline\nopen Roth\n'+m+extra
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS full actual caller inlining; width',max(map(len,s.splitlines())))
