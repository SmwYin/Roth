from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
s=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=s.index('/-- If the index of `P ≠ 0`');b=s.index('private lemma abs_eval_iterated_hasseDeriv_lt_aux');s=s[:a]+s[b:]
s=s.replace('private lemma exists_hasseDeriv_index_eval_bound_aux','theorem caller_inline').replace('exists_hasseDeriv_index_eval_bound_aux','caller_inline')
a=s.index('  obtain ⟨k, hkw, hkev⟩ := exists_hasseDeriv_eval_ne_zero');b=s.index('  have hQev',a)
s=s[:a]+'''  have hPN : map (Int.castRingHom ℝ) P ≠ 0 :=
    (map_ne_zero_iff _ (MvPolynomial.map_injective _ Int.cast_injective)).2 hP
  have hn : (taylor z (map (Int.castRingHom ℝ) P)).support.Nonempty := by simpa using hPN
  have hcut : (taylor z (map (Int.castRingHom ℝ) P)).support.inf' hn (weight r) < c := by
    rw [Finset.inf'_eq_csInf_image]
    exact hz
  obtain ⟨k, hk, hkw⟩ := (Finset.inf'_lt_iff hn).mp hcut
  have hkev : eval z (hasseDeriv k (map (Int.castRingHom ℝ) P)) ≠ 0 := by
    rwa [mem_support_iff, coeff_taylor] at hk
'''+s[b:]
assert 'exists_hasseDeriv_eval_ne_zero'not in s
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Witness254Inline\nopen Roth\n'+s+'''
end Witness254Inline
#print axioms Witness254Inline.caller_inline
#print axioms Witness254Inline.main_lemma
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo (Lean.mkPrivateNameCore `Roth.MainLemma
    `Roth.exists_hasseDeriv_index_eval_bound_aux)
  let new ← Lean.getConstInfo `Witness254Inline.caller_inline
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "WITNESS254_CALLER_TYPE_CHANGED"
  let oldMain ← Lean.getConstInfo `Roth.main_lemma
  let newMain ← Lean.getConstInfo `Witness254Inline.main_lemma
  unless ← Lean.Meta.isDefEq oldMain.type newMain.type do
    throwError "WITNESS254_MAIN_TYPE_CHANGED"
  for ci in [new, newMain] do
    let val := (ci.value? (allowOpaque := true)).get!
    if val.getUsedConstants.contains `Roth.exists_hasseDeriv_eval_ne_zero then
      throwError "WITNESS254_INLINE_REFERENCES_TARGET"
  Lean.logInfo "WITNESS254_FULL_CALLER_AND_MAIN_SIGNATURES_IDENTICAL_NO_DIRECT_TARGET"
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.exists_hasseDeriv_eval_ne_zero
  for n in [target, `Witness254Inline.caller_inline] do
    let ci := env.find? n |>.get!
    let project (c : Lean.Name) := c.toString.startsWith "Roth." ||
      c.toString.startsWith "MvPolynomial.hasseDeriv"
    Lean.logInfo m!"WITNESS254_TYPE_CONSTANTS {n}: {ci.type.getUsedConstants.filter project}"
    let val := (ci.value? (allowOpaque := true)).get!
    Lean.logInfo m!"WITNESS254_BODY_CONSTANTS {n}: {val.getUsedConstants.filter project}"
'''
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS full original module target removed, one caller inlined, main continuation preserved')
