from pathlib import Path
import re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.mul_log_div_two_lt_log_mainCoeffBound')
mod=(D/'source-MainLemma.lean.txt').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
start=mod.index('/-- If `2 ≤ q_1');end=mod.index('private lemma two_lt_rpow_aux',start)
target=mod[start:end];proof="""  have hpow : 0 < (q₁ : ℝ) ^ (δ * r₁) := lt_of_lt_of_le (by norm_num) hX
  have hq : 0 < (q₁ : ℝ) :=
    ((Real.one_lt_rpow_iff (Nat.cast_nonneg q₁)).1
      (lt_of_lt_of_le (by norm_num) hX)).elim (fun h ↦ zero_lt_one.trans h.1) And.left
  simpa only [mainCoeffBound, Real.log_sqrt hpow.le, Real.log_rpow hq] using
    Real.log_lt_log (Real.sqrt_pos.mpr hpow) (sqrt_lt_floor hX).1"""
mod=mod[:start]+mod[end:]
needle='  have hX := (two_lt_rpow_aux hδ0 hr₁ (hlog2.trans_le h1)).le\n'
insert='  have logBound : δ * r₁ * Real.log q₁ / 2 < Real.log (mainCoeffBound δ q₁ r₁) := by\n'+''.join('  '+l+'\n'for l in proof.splitlines())
assert mod.count(needle)==1
mod=mod.replace(needle,needle+insert).replace('(mul_log_div_two_lt_log_mainCoeffBound hX)','logBound')
assert 'mul_log_div_two_lt_log_mainCoeffBound'not in mod
extra='''
end Log239Inline
run_cmd Lean.Elab.Command.liftTermElabM do
  for (oldName, newName) in
      [(`Roth.three_small_factors, `Log239Inline.three_small_factors),
       (`Roth.main_lemma, `Log239Inline.main_lemma)] do
    let old ← Lean.getConstInfo oldName
    let new ← Lean.getConstInfo newName
    unless ← Lean.Meta.isDefEq old.type new.type do
      throwError "LOG239_INLINE_SIGNATURE_CHANGED: {oldName}"
    Lean.logInfo m!"LOG239_INLINE_SIGNATURE_IDENTICAL: {oldName}"
    let some value := new.value? (allowOpaque := true)
      | throwError "LOG239_INLINE_NO_VALUE: {newName}"
    if value.getUsedConstants.contains `Roth.mul_log_div_two_lt_log_mainCoeffBound then
      throwError "LOG239_INLINE_RETAINS_TARGET: {newName}"
    Lean.logInfo m!"LOG239_INLINE_NO_TARGET: {newName}"
#print axioms Log239Inline.three_small_factors
#print axioms Log239Inline.main_lemma
'''
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Log239Inline\nopen Roth\n'+mod+extra
assert max(map(len,s.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(s)
print('Prepared exact full MainLemma module; target omitted and sole caller proof inlined; width100.')
print(s[s.index('theorem three_small_factors'):s.index('private lemma exists_norm_coeff')])
