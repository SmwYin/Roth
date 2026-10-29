from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.roth_rat')
s=(D/'general2-executed.lean.txt').read_text()
s=s[:s.index('lemma generalize')]+'''
lemma rational_finite (a : ℚ) {κ : ℝ} (hκ : 2 ≤ κ) :
    {x : ℚ | |(a : ℝ) - x| < 1 / (x.den : ℝ) ^ κ}.Finite := by
  apply Set.not_infinite.mp
  intro hinf
  exact (inferred_irrational hκ hinf).ne_rat a rfl
lemma sharp {α : ℝ} (hα : Irrational α) :
    {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ (2 : ℝ)}.Infinite := by
  simpa only [Real.rpow_two] using Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational hα
lemma coefficient_le_one
    (hR : ∀ {α : ℝ}, IsAlgebraic ℚ α → ∀ {κ : ℝ},
      {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite → κ ≤ 2)
    {α κ C : ℝ} (halg : IsAlgebraic ℚ α) (hC : C ≤ 1)
    (hinf : {x : ℚ | |α - x| < C / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 := by
  apply hR halg
  refine hinf.mono ?_
  intro x hx
  change |α - (x : ℝ)| < C / (x.den : ℝ) ^ κ at hx
  change |α - (x : ℝ)| < 1 / (x.den : ℝ) ^ κ
  exact hx.trans_le (div_le_div_of_nonneg_right hC (by positivity))
-- The pair representation has infinitely many exact unreduced representatives of zero.
def pairSet (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}
lemma zero_pairs_infinite (κ : ℝ) : (pairSet 0 κ).Infinite := by
  have hi : (Set.Ioi (0 : ℕ)).Infinite := Set.Ioi_infinite 0
  refine (hi.image (f := fun q : ℕ ↦ ((0 : ℤ), q)) (by
    intro a _ b _ hab
    exact congrArg Prod.snd hab)).mono ?_
  rintro _ ⟨q, hq, rfl⟩
  have hq0 : (0 : ℝ) < q := by exact_mod_cast hq
  exact ⟨hq, by simpa using one_div_pos.mpr (Real.rpow_pos_of_pos hq0 κ)⟩
example : ¬ (∀ {α : ℝ}, IsAlgebraic ℚ α → ∀ {κ : ℝ},
    (pairSet α κ).Infinite → κ ≤ 2) := by
  intro h
  have hh := h (isAlgebraic_zero : IsAlgebraic ℚ (0 : ℝ)) (zero_pairs_infinite 3)
  norm_num at hh
#print axioms Roth289General.rational_finite
#print axioms Roth289General.sharp
#print axioms Roth289General.coefficient_le_one
#print axioms Roth289General.zero_pairs_infinite
end Roth289General
'''
assert max(map(len,s.splitlines()))<=100
(D/'edges-executed.lean.txt').write_text(s)
r=dict(id='edges01',operation='run_code',source='edges-executed.lean.txt',source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='edges01-receipt.json',arguments={})
(D/'root-requests/edges01.json').write_text(json.dumps(r,indent=2)+'\n')
print('edges prepared width',max(map(len,s.splitlines())))
