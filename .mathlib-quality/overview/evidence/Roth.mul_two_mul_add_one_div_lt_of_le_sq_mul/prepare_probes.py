from pathlib import Path
D=Path(__file__).parent
b='''
#check_failure Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul
#check @mul_lt_of_lt_one_left
#check @mul_lt_mul_iff_of_pos_right
#check @sq_pos_of_ne_zero
#check @mul_le_mul_of_nonneg_right
namespace Budget253
variable {K : Type*} [Semifield K] [LinearOrder K] [IsStrictOrderedRing K]
  [ExistsAddOfLE K]
theorem generic {δ m a L : K} (ha : 0 < a) (hδm : δ * m < 1)
    (hbudget : a ≤ δ ^ 2 * L) : m * a / δ < L := by
  have hδ : δ ≠ 0 := by
    rintro rfl
    simpa using ha.trans_le hbudget
  apply (mul_lt_mul_iff_of_pos_right (sq_pos_of_ne_zero hδ)).1
  calc
    _ = (δ * m) * a := by field_simp
    _ < a := mul_lt_of_lt_one_left ha hδm
    _ ≤ L * δ ^ 2 := hbudget.trans_eq (mul_comm _ _)
theorem recovery {δ m L : K} (hm : 0 < 2 * m + 1) (hδm : δ * m < 1)
    (h32 : 2 * m + 1 ≤ δ ^ 2 * L) : m * (2 * m + 1) / δ < L :=
  generic hm hδm h32
theorem weak {δ m a L : K} (ha : 0 < a) (hδm : δ * m ≤ 1)
    (hbudget : a ≤ δ ^ 2 * L) : m * a / δ ≤ L := by
  have hδ : δ ≠ 0 := by
    rintro rfl
    simpa using ha.trans_le hbudget
  apply (mul_le_mul_iff_of_pos_right (sq_pos_of_ne_zero hδ)).1
  calc
    _ = (δ * m) * a := by field_simp
    _ ≤ a := by simpa using mul_le_mul_of_nonneg_right hδm ha.le
    _ ≤ L * δ ^ 2 := hbudget.trans_eq (mul_comm _ _)
theorem strict_budget {δ m a L : K} (ha : 0 < a) (hδm : δ * m ≤ 1)
    (hbudget : a < δ ^ 2 * L) : m * a / δ < L := by
  have hδ : δ ≠ 0 := by
    rintro rfl
    simpa using ha.trans hbudget
  apply (mul_lt_mul_iff_of_pos_right (sq_pos_of_ne_zero hδ)).1
  calc
    _ = (δ * m) * a := by field_simp
    _ ≤ a := by simpa using mul_le_mul_of_nonneg_right hδm ha.le
    _ < L * δ ^ 2 := hbudget.trans_eq (mul_comm _ _)
omit [IsStrictOrderedRing K] [ExistsAddOfLE K] in
theorem delta_nonzero {δ a L : K} (ha : 0 < a) (h : a ≤ δ ^ 2 * L) : δ ≠ 0 := by
  rintro rfl
  simpa using ha.trans_le h
example {δ m L : K} (hm : 0 < 2 * m + 1) (hδm : δ * m < 1)
    (h32 : 2 * m + 1 ≤ δ ^ 2 * L) : m * (2 * m + 1) / δ < L := by
  fail_if_success exact mul_lt_of_lt_one_left hm hδm
  fail_if_success exact (mul_lt_mul_iff_of_pos_right hm).1 hδm
  exact recovery hm hδm h32
-- The original allows a negative delta and a negative m.
theorem negative_delta :
    (0 : ℚ) < 2 * (1 : ℚ) + 1 ∧ (-1 : ℚ) * 1 < 1 ∧
    2 * (1 : ℚ) + 1 ≤ (-1 : ℚ) ^ 2 * 3 ∧ 1 * (2 * 1 + 1) / (-1 : ℚ) < 3 := by
  norm_num
theorem negative_m :
    (0 : ℚ) < 2 * (-1 / 4 : ℚ) + 1 ∧ (1 : ℚ) * (-1 / 4) < 1 ∧
    2 * (-1 / 4 : ℚ) + 1 ≤ (1 : ℚ) ^ 2 * (1 / 2) ∧
    (-1 / 4 : ℚ) * (2 * (-1 / 4) + 1) / 1 < 1 / 2 := by
  norm_num
theorem zero_m : (0 : ℚ) < 2 * 0 + 1 ∧ (1 : ℚ) * 0 < 1 ∧
    2 * (0 : ℚ) + 1 ≤ (1 : ℚ) ^ 2 * 1 ∧ 0 * (2 * 0 + 1) / (1 : ℚ) < 1 := by
  norm_num
-- Scale positivity cannot be dropped: a=0, delta=0, L=0.
theorem zero_scale_counterexample : (0 : ℚ) * 1 < 1 ∧
    (0 : ℚ) ≤ 0 ^ 2 * 0 ∧ ¬ ((1 : ℚ) * 0 / 0 < 0) := by norm_num
-- Even delta nonzero does not repair a negative scale.
theorem negative_scale_counterexample : (1 : ℚ) * (-2) < 1 ∧
    (-1 : ℚ) ≤ 1 ^ 2 * (-1) ∧ ¬ ((-2 : ℚ) * (-1) / 1 < -1) := by norm_num
-- Equality at both bounds only gives the weak conclusion.
theorem strictness_counterexample : (0 : ℚ) < 2 * 1 + 1 ∧ (1 : ℚ) * 1 ≤ 1 ∧
    2 * (1 : ℚ) + 1 ≤ 1 ^ 2 * 3 ∧ ¬ ((1 : ℚ) * (2 * 1 + 1) / 1 < 3) := by
  norm_num
theorem budget_needed : (0 : ℚ) < 2 * 1 + 1 ∧ (1 / 2 : ℚ) * 1 < 1 ∧
    ¬ ((1 : ℚ) * (2 * 1 + 1) / (1 / 2) < 0) := by norm_num
end Budget253
#print axioms Budget253.generic
#print axioms Budget253.recovery
#print axioms Budget253.weak
#print axioms Budget253.strict_budget
#print axioms Budget253.delta_nonzero
#print axioms Budget253.negative_delta
#print axioms Budget253.negative_m
#print axioms Budget253.zero_m
#print axioms Budget253.zero_scale_counterexample
#print axioms Budget253.negative_scale_counterexample
#print axioms Budget253.strictness_counterexample
#print axioms Budget253.budget_needed
'''
s=(D/'isolated-prefix.lean.txt').read_text()+b
assert max(map(len,s.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(s)
print('PASS isolated positive-scale, recovery, weak/strict budget and boundary probes prepared')
