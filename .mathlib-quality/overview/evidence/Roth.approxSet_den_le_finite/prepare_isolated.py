from pathlib import Path
import re
D=Path(__file__).resolve().parent
prefix=(D/'isolated-prefix.lean.txt').read_text()
prior=Path('.mathlib-quality/overview/evidence/Roth.approxSet/isolated-executed.lean.txt').read_text()
template=prior[prior.index('theorem bounded_den_finite'):prior.index('theorem infinite_iff_frequently')]
template=template.replace('approxWith α ψ','{hq : ℤ × ℕ | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < ψ hq.2}')
# Reflow only the long expanded statement.
template=template.replace('    {hq ∈ {hq : ℤ × ℕ | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < ψ hq.2} | hq.2 ≤ Q₀}.Finite',
 '    {hq : ℤ × ℕ | (0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < ψ hq.2) ∧\n      hq.2 ≤ Q₀}.Finite')
s=prefix+'''\n#check_failure Roth.approxSet_den_le_finite
#check @Set.Finite.of_finite_fibers
#check @Set.Finite.biUnion
#check @Set.finite_Icc
#check @Int.ceil_le
#check @Int.le_floor
namespace Bounded269Isolated
'''+template+'''
theorem finite_radius {ι : Type*} (s : Set ι) (hs : s.Finite) (c r : ι → ℝ) :
    {p : ℤ × ι | p.2 ∈ s ∧ |(p.1 : ℝ) - c p.2| ≤ r p.2}.Finite := by
  refine (hs.biUnion fun i _ ↦
    (Set.finite_Icc ⌈c i - r i⌉ ⌊c i + r i⌋).prod (Set.finite_singleton i)).subset ?_
  rintro ⟨h, i⟩ ⟨hi, hb⟩
  have hb' := abs_le.mp hb
  have hlo : c i - r i ≤ (h : ℝ) := by linarith only [hb'.1]
  have hhi : (h : ℝ) ≤ c i + r i := by linarith only [hb'.2]
  simp only [Set.mem_iUnion, Set.mem_prod, Set.mem_Icc, Set.mem_singleton_iff]
  exact ⟨i, hi, ⟨Int.ceil_le.mpr hlo, Int.le_floor.mpr hhi⟩, rfl⟩
theorem old_form (α κ : ℝ) (Q : ℕ) :
    {p : ℤ × ℕ | (0 < p.2 ∧ |α - (p.1 : ℝ) / p.2| < 1 / (p.2 : ℝ) ^ κ) ∧
      p.2 ≤ Q}.Finite := bounded_den_finite α (fun q ↦ 1 / (q : ℝ) ^ κ) Q
theorem zero_bound (α : ℝ) (ψ : ℕ → ℝ) :
    {p : ℤ × ℕ | (0 < p.2 ∧ |α - (p.1 : ℝ) / p.2| < ψ p.2) ∧ p.2 ≤ 0} = ∅ := by
  ext p
  simp only [Set.mem_ofPred_eq, Set.mem_empty_iff_false, iff_false, not_and]
  omega
theorem negative_exponent (Q : ℕ) :
    {p : ℤ × ℕ | (0 < p.2 ∧ |(-1000000 : ℝ) - (p.1 : ℝ) / p.2| <
      1 / (p.2 : ℝ) ^ (-3 : ℝ)) ∧ p.2 ≤ Q}.Finite := old_form _ _ Q
theorem rational_center (Q : ℕ) :
    {p : ℤ × ℕ | (0 < p.2 ∧ |(3 / 7 : ℝ) - (p.1 : ℝ) / p.2| <
      1 / (p.2 : ℝ) ^ (9 : ℝ)) ∧ p.2 ≤ Q}.Finite := old_form _ _ Q
theorem closed_endpoint (s : Set ℕ) (hs : s.Finite) (r : ℕ → ℝ) :
    {p : ℤ × ℕ | p.2 ∈ s ∧ |(p.1 : ℝ) - 17| ≤ r p.2}.Finite :=
  finite_radius s hs (fun _ ↦ 17) r
theorem negative_radius_empty (c : ℝ) : {h : ℤ | |(h : ℝ) - c| < -1} = ∅ := by
  ext h
  simp only [Set.mem_ofPred_eq, Set.mem_empty_iff_false, iff_false]
  linarith only [abs_nonneg ((h : ℝ) - c)]
theorem zero_pairs_infinite (κ : ℝ) :
    {p : ℤ × ℕ | 0 < p.2 ∧ |(0 : ℝ) - (p.1 : ℝ) / p.2| <
      1 / (p.2 : ℝ) ^ κ}.Infinite := by
  refine (Set.infinite_range_of_injective (f := fun n : ℕ ↦ ((0 : ℤ), n + 1)) ?_).mono ?_
  · intro a b hab
    exact Nat.add_right_cancel (congrArg Prod.snd hab)
  · rintro _ ⟨n, rfl⟩
    refine ⟨Nat.succ_pos _, ?_⟩
    simp only [Int.cast_zero, zero_div, sub_zero, abs_zero]
    positivity
-- A fresh default-resource closure probe; the arithmetic bridge is not supplied.
example (α κ : ℝ) (Q : ℕ) :
    {p : ℤ × ℕ | (0 < p.2 ∧ |α - (p.1 : ℝ) / p.2| < 1 / (p.2 : ℝ) ^ κ) ∧
      p.2 ≤ Q}.Finite := by
  fail_if_success exact Set.Finite.of_finite_fibers Prod.snd (Set.finite_Iic Q)
  exact old_form α κ Q
end Bounded269Isolated
#print axioms Bounded269Isolated.bounded_den_finite
#print axioms Bounded269Isolated.finite_radius
#print axioms Bounded269Isolated.old_form
#print axioms Bounded269Isolated.zero_bound
#print axioms Bounded269Isolated.negative_exponent
#print axioms Bounded269Isolated.rational_center
#print axioms Bounded269Isolated.closed_endpoint
#print axioms Bounded269Isolated.negative_radius_empty
#print axioms Bounded269Isolated.zero_pairs_infinite
'''
assert max(map(len,s.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(s)
print('Prepared isolated shared18; credited267 template + new finite-radius proof and endpoints')
