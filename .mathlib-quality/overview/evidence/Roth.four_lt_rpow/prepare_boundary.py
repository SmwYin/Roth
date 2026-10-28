from pathlib import Path
D=Path('/private/tmp/roth-overview/assess/Roth.four_lt_rpow')
s=(D/'isolated-executed.lean.txt').read_text().rsplit('end Four238Isolated',1)[0]+'''
theorem exactThreeBoundary :
    let d := Real.sqrt (3 / Real.log 2)
    d ^ 2 * Real.log 2 = 3 ∧ 4 < (2 : ℝ) ^ (d * (1 : ℕ)) := by
  dsimp only
  have hL := Real.log_pos (by norm_num : (1 : ℝ) < 2)
  have he : (Real.sqrt (3 / Real.log 2)) ^ 2 * Real.log 2 = 3 := by
    rw [Real.sq_sqrt (by positivity), div_mul_cancel₀ _ hL.ne']
  exact ⟨he, realBase (Real.sqrt_nonneg _) (by norm_num) (by norm_num) he.ge⟩

theorem squareTransferSemiring {K : Type*} [CommSemiring K] [LinearOrder K]
    [IsStrictOrderedRing K] {a c d L : K} (hd : 0 ≤ d) (hL : 0 < L)
    (hc : c ≤ d ^ 2 * L) (ha : a ^ 2 < c * L) : a < d * L := by
  by_contra! h
  nlinarith only [mul_self_le_mul_self (mul_nonneg hd hL.le) h,
    mul_le_mul_of_nonneg_right hc hL.le, ha]

theorem rationalSquareWitness : (1 : ℚ) < 2 * 2 :=
  squareTransferSemiring (by norm_num) (by norm_num) (by norm_num : (2 : ℚ) ≤ 2 ^ 2 * 2)
    (by norm_num)
#print axioms exactThreeBoundary
#print axioms squareTransferSemiring
#print axioms rationalSquareWitness
end Four238Isolated
'''
assert max(map(len,s.splitlines()))<=100
(D/'boundary-executed.lean.txt').write_text(s)
print(s[s.index('theorem exactThreeBoundary'):])
