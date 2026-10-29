from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');src=(R/'Roth/MainLemma.lean').read_text()
m=src.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
a=m.index('/-- Vanishing of box Hasse');b=m.index('/-- The bound `m(2m');m=m[:a]+m[b:]
a=m.index('  exact le_index_of_forall_eval_eq_zero');b=m.index('\nprivate lemma mul_card_filter_weight_le_aux',a)
m=m[:a]+'''  have hn : map (Int.castRingHom ℝ) (W' - W'') ≠ 0 :=
    ((map_ne_zero_iff _ (MvPolynomial.map_injective _ Int.cast_injective)).2 hP.1)
  have hdP : ∀ j, degreeOf j (map (Int.castRingHom ℝ) (W' - W'')) ≤ r j := by
    simpa only [degreeOf,
      degrees_map_of_injective _ (f := Int.castRingHom ℝ) Int.cast_injective] using hP.2.1
  refine (le_index_iff hn).2 fun d he ↦ le_of_not_gt fun hw ↦ ?_
  have hd : ∀ j, d j ≤ r j := by
    intro j
    by_contra! hj
    exact he <| by rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hdP j).trans_lt hj), map_zero]
  exact he (eval_hasseDeriv_sub_eq_zero hfα (hWeq d (hJ d hd hw)))
''' +m[b:]
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Cutoff252Inline\nopen Roth\n'+m+'''
end Cutoff252Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  let env ← Lean.getEnv
  let short := `Roth.exists_mem_RSet_le_index_aux
  let oldName := Lean.mkPrivateNameCore `Roth.MainLemma short
  let newSuffix := short.replacePrefix `Roth `Cutoff252Inline
  let newName := Lean.mkPrivateNameCore env.mainModule newSuffix
  let old ← Lean.getConstInfo oldName
  let new ← Lean.getConstInfo newName
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "CUTOFF252_INLINE_SIGNATURE_CHANGED"
  Lean.logInfo "CUTOFF252_INLINE_SIGNATURE_IDENTICAL"
  let some value := new.value? (allowOpaque := true) | throwError "CUTOFF252_INLINE_NO_VALUE"
  if value.getUsedConstants.contains `Roth.le_index_of_forall_eval_eq_zero then
    throwError "CUTOFF252_INLINE_RETAINS_TARGET"
  Lean.logInfo "CUTOFF252_INLINE_NO_TARGET"
#print axioms Cutoff252Inline.main_lemma
'''
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS full module inline, width',max(map(len,s.splitlines())))
