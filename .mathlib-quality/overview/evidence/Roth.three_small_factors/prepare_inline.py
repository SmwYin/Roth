from pathlib import Path
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
mod=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
target=mod[mod.index('theorem three_small_factors'):mod.index('private lemma exists_norm_coeff')]
sig,proof=target.rstrip().split(' := by\n',1)
mod=mod[:mod.index('/-- For positive `r_1`')]+mod[mod.index('private lemma exists_norm_coeff'):]
# Each actual call receives the original argument-taking theorem body in situ.
# Fully typed local signature supports the original implicit argument flow.
local=sig.replace('theorem three_small_factors','have factorBounds',1)+' := by\n'+proof+'\n'
needle='  obtain ⟨_, hTA, _⟩ := three_small_factors'
assert mod.count(needle)==1
mod=mod.replace(needle,''.join('  '+l+'\n' for l in local.splitlines())+needle.replace('three_small_factors','factorBounds'))
needle='  obtain ⟨h2, _, hα⟩ := three_small_factors'
assert mod.count(needle)==1
mod=mod.replace(needle,''.join('  '+l+'\n' for l in local.splitlines())+needle.replace('three_small_factors','factorBounds'))
main=(D/'source-Main.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
needle='  exact hprodR.trans_lt (three_small_factors hδ0 hr0 hA h32).1'
assert main.count(needle)==1
main=main.replace(needle,''.join('  '+l+'\n' for l in local.splitlines())+needle.replace('three_small_factors','factorBounds'))
assert 'three_small_factors'not in mod+main
extra='''
end Fact241Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  for (oldName, newName) in
      [(Lean.mkPrivateNameCore `Roth.MainLemma `Roth.exists_mem_RSet_le_index_of_log_bound_aux,
        Lean.mkPrivateNameCore `«GenWronskianChecks»
          `Fact241Inline.exists_mem_RSet_le_index_of_log_bound_aux)] do
    let _ := oldName
    let _ := newName
'''
# Scratch module name is obtained at runtime; this avoids guessing its private prefix.
extra='''
end Fact241Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  let env ← Lean.getEnv
  for (oldModule, short) in
      [(`Roth.MainLemma, `Roth.exists_mem_RSet_le_index_of_log_bound_aux),
       (`Roth.MainLemma, `Roth.exists_auxiliary_polynomial_of_log_bound_aux),
       (`Roth.Main, `Roth.roth_product_bound_aux)] do
    let oldName := Lean.mkPrivateNameCore oldModule short
    let newSuffix := short.replacePrefix `Roth `Fact241Inline
    let newName := Lean.mkPrivateNameCore env.mainModule newSuffix
    let old ← Lean.getConstInfo oldName
    let new ← Lean.getConstInfo newName
    unless ← Lean.Meta.isDefEq old.type new.type do
      throwError "FACT241_INLINE_SIGNATURE_CHANGED: {oldName}"
    Lean.logInfo m!"FACT241_INLINE_SIGNATURE_IDENTICAL: {oldName}"
    let some value := new.value? (allowOpaque := true)
      | throwError "FACT241_INLINE_NO_VALUE: {newName}"
    if value.getUsedConstants.contains `Roth.three_small_factors then
      throwError "FACT241_INLINE_RETAINS_TARGET: {newName}"
    Lean.logInfo m!"FACT241_INLINE_NO_TARGET: {newSuffix}"
#print axioms Fact241Inline.main_lemma
#print axioms Fact241Inline.roth
'''
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Fact241Inline\nopen Roth\n'+mod+main+extra
# Original100-width theorem, nested2 spaces: wrap only the two long signature lines.
s=s.replace('  '+sig.splitlines()[0], '  '+sig.splitlines()[0])
(D/'inline-executed.lean.txt').write_text(s)
print('Prepared3 actual call-site inline bodies; max width',max(map(len,s.splitlines())))
