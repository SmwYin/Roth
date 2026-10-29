from pathlib import Path
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
m=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=m.index('/-- Finitely supported degree bounds and a strict');b=m.index('/-- The difference of two distinct members');t=m[m.index('theorem exists_ne_modByMonic_eq'):b].rstrip();m=m[:a]+m[b:]
t=t.replace('theorem exists_ne_modByMonic_eq','have collision',1)
needle="  obtain ⟨W', hW', W'', hW'', hne, hWeq⟩ := exists_ne_modByMonic_eq"
assert m.count(needle)==1
m=m.replace(needle,''.join('  '+l+'\n'for l in t.splitlines())+needle.replace('exists_ne_modByMonic_eq','collision'))
assert 'exists_ne_modByMonic_eq'not in m
extra='''
end Collision249Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  let env ← Lean.getEnv
  let short := `Roth.exists_mem_RSet_le_index_aux
  let oldName := Lean.mkPrivateNameCore `Roth.MainLemma short
  let newSuffix := short.replacePrefix `Roth `Collision249Inline
  let newName := Lean.mkPrivateNameCore env.mainModule newSuffix
  let old ← Lean.getConstInfo oldName
  let new ← Lean.getConstInfo newName
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "COLL249_INLINE_SIGNATURE_CHANGED"
  Lean.logInfo "COLL249_INLINE_SIGNATURE_IDENTICAL"
  let some value := new.value? (allowOpaque := true) | throwError "COLL249_INLINE_NO_VALUE"
  if value.getUsedConstants.contains `Roth.exists_ne_modByMonic_eq then
    throwError "COLL249_INLINE_RETAINS_TARGET"
  Lean.logInfo "COLL249_INLINE_NO_TARGET"
#print axioms Collision249Inline.main_lemma
'''
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Collision249Inline\nopen Roth\n'+m+extra
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s)
print('PASS prepared full original module with exact actual caller inlining; width',max(map(len,s.splitlines())))
