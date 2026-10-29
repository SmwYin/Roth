from pathlib import Path
D=Path(__file__).parent
m=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=m.index('/-- If `Δ_j');b=m.index('/-- Vanishing of box Hasse');t=m[m.index('theorem eval_hasseDeriv_sub_eq_zero'):b].rstrip()
body=t.split(':= by\n',1)[1]
mi=m[:a]+m[b:]
needle='    fun d hd hw ↦ eval_hasseDeriv_sub_eq_zero hfα (hWeq d (hJ d hd hw))'
inline='    fun d hd hw ↦ by\n      have h := hWeq d (hJ d hd hw)\n'+'\n'.join('    '+x.replace(' j ', ' d ') for x in body.splitlines())
assert mi.count(needle)==1;mi=mi.replace(needle,inline);assert 'eval_hasseDeriv_sub_eq_zero'not in mi
extra='''
end Vanish251Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  let env ← Lean.getEnv
  let short := `Roth.exists_mem_RSet_le_index_aux
  let oldName := Lean.mkPrivateNameCore `Roth.MainLemma short
  let newSuffix := short.replacePrefix `Roth `Vanish251Inline
  let newName := Lean.mkPrivateNameCore env.mainModule newSuffix
  let old ← Lean.getConstInfo oldName
  let new ← Lean.getConstInfo newName
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "VANISH251_INLINE_SIGNATURE_CHANGED"
  Lean.logInfo "VANISH251_INLINE_SIGNATURE_IDENTICAL"
  let some value := new.value? (allowOpaque := true) | throwError "VANISH251_INLINE_NO_VALUE"
  if value.getUsedConstants.contains `Roth.eval_hasseDeriv_sub_eq_zero then
    throwError "VANISH251_INLINE_RETAINS_TARGET"
  Lean.logInfo "VANISH251_INLINE_NO_TARGET"
#print axioms Vanish251Inline.main_lemma
'''
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Vanish251Inline\nopen Roth\n'+mi+extra
assert max(map(len,s.splitlines()))<=100;(D/'inline-executed.lean.txt').write_text(s)
meta=(D/'disk-prefix.lean.txt').read_text()+'''
run_cmd do
  let ci ← Lean.getConstInfo `Roth.eval_hasseDeriv_sub_eq_zero
  Lean.logInfo m!"VANISH251_TYPE_CONSTANTS: {ci.type.getUsedConstants}"
  let some v := ci.value? (allowOpaque := true) | throwError "VANISH251_NO_VALUE"
  Lean.logInfo m!"VANISH251_BODY_CONSTANTS: {v.getUsedConstants}"
#print axioms Roth.eval_hasseDeriv_sub_eq_zero
''';(D/'metadata-executed.lean.txt').write_text(meta)
generic=(D/'isolated-executed.lean.txt').read_text().split('theorem observe',1)[1].split('theorem divisibility',1)[0]
rec=t.split(':= by',1)[0].replace('theorem eval_hasseDeriv_sub_eq_zero','theorem recovery')+''':= by
  let D : MvPolynomial σ ℤ →+ Polynomial ℤ :=
    (aeval (fun _ ↦ Polynomial.X)).toAddMonoidHom.comp (hasseDeriv j).toAddMonoidHom
  have he := observe D (Polynomial.aeval α).toRingHom hfα h
  simpa [D, hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def,
    MvPolynomial.comp_aeval_apply, Polynomial.aeval_X] using he
'''
s=(D/'disk-prefix.lean.txt').read_text()+'''namespace Vanish251Project
open Roth MvPolynomial
variable {R S A : Type*}
'''+ 'theorem observe'+generic+rec+'''
theorem root_needed :
    diag (hasseDeriv (0 : Unit →₀ ℕ) (1 : MvPolynomial Unit ℤ)) %ₘ 1 =
      diag (hasseDeriv (0 : Unit →₀ ℕ) (0 : MvPolynomial Unit ℤ)) %ₘ 1 ∧
    eval (fun _ : Unit ↦ (0 : ℤ))
      (hasseDeriv 0 (map (Int.castRingHom ℤ) ((1 : MvPolynomial Unit ℤ) - 0))) ≠ 0 := by
  simp
theorem equality_needed : Polynomial.aeval (0 : ℤ) (Polynomial.X : Polynomial ℤ) = 0 ∧
    eval (fun _ : Unit ↦ (0 : ℤ))
      (hasseDeriv 0 (map (Int.castRingHom ℤ) ((1 : MvPolynomial Unit ℤ) - 0))) ≠ 0 := by
  simp
end Vanish251Project
#print axioms Vanish251Project.recovery
#print axioms Vanish251Project.root_needed
#print axioms Vanish251Project.equality_needed
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.eval_hasseDeriv_sub_eq_zero
  let new ← Lean.getConstInfo `Vanish251Project.recovery
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "VANISH251_RECOVERY_SIGNATURE_CHANGED"
  Lean.logInfo "VANISH251_RECOVERY_SIGNATURE_IDENTICAL"
'''
assert max(map(len,s.splitlines()))<=100;(D/'recovery-executed.lean.txt').write_text(s)
print('Prepared full module inline with caller signature and continuation, recovery and metadata; width100')
