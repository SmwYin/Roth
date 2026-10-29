from pathlib import Path
D=Path(__file__).parent
m=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=m.index('/-- The difference of two distinct members');b=m.index('/-- If `Δ_j');t=m[m.index('theorem sub_mem_RSet'):b].rstrip();m=m[:a]+m[b:]
needle="  have hP := sub_mem_RSet hW' hW'' hne"
assert m.count(needle)==1
body=t.split(':= by\n',1)[1].replace("h'.",'hW\'.').replace("h''.","hW''. ")
# Replace only the proof identifiers in the extracted target, not the canonical name array.
body=t.split(':= by\n',1)[1].replace("(h'.", "(hW'.").replace("(h''.", "(hW''.")
inline="  have hP : W' - W'' ∈ RSet B r := by\n"+'\n'.join('  '+l for l in body.splitlines())
m=m.replace(needle,inline)
assert 'sub_mem_RSet'not in m
extra='''
end Difference250Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  let env ← Lean.getEnv
  let short := `Roth.exists_mem_RSet_le_index_aux
  let oldName := Lean.mkPrivateNameCore `Roth.MainLemma short
  let newSuffix := short.replacePrefix `Roth `Difference250Inline
  let newName := Lean.mkPrivateNameCore env.mainModule newSuffix
  let old ← Lean.getConstInfo oldName
  let new ← Lean.getConstInfo newName
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "DIFF250_INLINE_SIGNATURE_CHANGED"
  Lean.logInfo "DIFF250_INLINE_SIGNATURE_IDENTICAL"
  let some value := new.value? (allowOpaque := true) | throwError "DIFF250_INLINE_NO_VALUE"
  if value.getUsedConstants.contains `Roth.sub_mem_RSet then
    throwError "DIFF250_INLINE_RETAINS_TARGET"
  Lean.logInfo "DIFF250_INLINE_NO_TARGET"
#print axioms Difference250Inline.main_lemma
'''
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Difference250Inline\nopen Roth\n'+m+extra
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s)
meta=(D/'disk-prefix.lean.txt').read_text()+'''
run_cmd do
  let ci ← Lean.getConstInfo `Roth.sub_mem_RSet
  Lean.logInfo m!"DIFF250_TYPE_CONSTANTS: {ci.type.getUsedConstants}"
  let some v := ci.value? (allowOpaque := true) | throwError "DIFF250_NO_VALUE"
  Lean.logInfo m!"DIFF250_BODY_CONSTANTS: {v.getUsedConstants}"
#print axioms Roth.sub_mem_RSet
'''
(D/'metadata-executed.lean.txt').write_text(meta)
generic=(D/'isolated-executed.lean.txt').read_text().split('theorem interval_sub',1)[1].split('theorem integer_recovery',1)[0]
recovery=t.split(':= by',1)[0].replace('theorem sub_mem_RSet','theorem recovery')+''':= by
  obtain ⟨hn, hd, hc⟩ := interval_sub (lb := (0 : ℤ)) (ub := (B : ℤ)) h' h'' hne
  refine ⟨hn, hd, fun d ↦ ?_⟩
  have hc' : |(W' - W'').coeff d| ≤ (B : ℤ) := by
    simpa only [sub_zero] using hc d
  exact_mod_cast hc'
'''
s=(D/'disk-prefix.lean.txt').read_text()+'''namespace Difference250Project
open Roth MvPolynomial
'''+ 'theorem interval_sub'+generic+recovery+'''
end Difference250Project
#print axioms Difference250Project.recovery
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.sub_mem_RSet
  let new ← Lean.getConstInfo `Difference250Project.recovery
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "DIFF250_RECOVERY_SIGNATURE_CHANGED"
  Lean.logInfo "DIFF250_RECOVERY_SIGNATURE_IDENTICAL"
'''
assert max(map(len,s.splitlines()))<=100
(D/'recovery-executed.lean.txt').write_text(s)
print('Prepared full caller inline, direct kernel metadata, original specialization drafts')
