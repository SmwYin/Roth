from pathlib import Path
D=Path('/private/tmp/roth-overview/assess/Roth.four_lt_rpow')
s=(D/'isolated-prefix.lean.txt').read_text()+'''
#check_failure Roth.four_lt_rpow
namespace Four238Isolated
#check @Real.lt_rpow_of_log_lt
#check @Real.lt_rpow_iff_log_lt
#check @Real.rpow_le_rpow_of_exponent_le
#check @Real.log_le_log
#check @Real.quadratic_le_exp_of_nonneg
#check @Real.le_log_one_add_of_nonneg
#check @Real.lt_log_one_add_of_pos
#check @sq_lt_sq₀
#check @Real.exp_lt_iff_lt_log
#check @Real.rpow_def_of_pos

theorem squareTransfer {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {a c d L : K} (hd : 0 ≤ d) (hL : 0 < L) (hc : c ≤ d ^ 2 * L)
    (ha : a ^ 2 < c * L) : a < d * L := by
  by_contra! h
  nlinarith only [mul_self_le_mul_self (mul_nonneg hd hL.le) h,
    mul_le_mul_of_nonneg_right hc hL.le, ha]

theorem powerTransfer {a c d q r : ℝ} (hd : 0 ≤ d) (hq : 1 < q) (hr : 1 ≤ r)
    (hc : c ≤ d ^ 2 * Real.log q) (ha : (Real.log a) ^ 2 < c * Real.log q) :
    a < q ^ (d * r) := by
  have hL := Real.log_pos hq
  have hkey := squareTransfer hd hL hc ha
  apply Real.lt_rpow_of_log_lt (zero_lt_one.trans hq)
  nlinarith only [hkey, le_mul_of_one_le_right (mul_nonneg hd hL.le) hr]

theorem sharper {d q r : ℝ} (hd : 0 ≤ d) (hq : 2 ≤ q) (hr : 1 ≤ r)
    (hc : 4 * Real.log 2 < d ^ 2 * Real.log q) : 4 < q ^ (d * r) := by
  have hL := Real.log_pos (by linarith : 1 < q)
  have hlog : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]
    norm_num
  apply powerTransfer hd (by linarith) hr (le_refl (d ^ 2 * Real.log q))
  have h2 := Real.log_pos (by norm_num : (1 : ℝ) < 2)
  have hq2 := Real.log_le_log (by norm_num : (0 : ℝ) < 2) hq
  have hmul := mul_lt_mul_of_pos_right hc hL
  have hm := mul_le_mul_of_nonneg_left hq2 (by positivity : 0 ≤ 4 * Real.log 2)
  rw [hlog]
  nlinarith only [hm, hmul]

theorem realBase {d q r : ℝ} (hd : 0 ≤ d) (hq : 2 ≤ q) (hr : 1 ≤ r)
    (hc : 3 ≤ d ^ 2 * Real.log q) : 4 < q ^ (d * r) := by
  have hlog2 : Real.log 2 < 3 / 4 := by
    apply (Real.log_lt_iff_lt_exp (by norm_num)).2
    nlinarith only [Real.quadratic_le_exp_of_nonneg (by norm_num : (0 : ℝ) ≤ 3 / 4)]
  exact sharper hd hq hr (lt_of_lt_of_le (by linarith only [hlog2]) hc)

theorem original {d : ℝ} (hd : 0 ≤ d) {q r : ℕ} (hr : 0 < r)
    (hc : 3 ≤ d ^ 2 * Real.log q) : 4 < (q : ℝ) ^ (d * r) := by
  have hL : 0 < Real.log q :=
    pos_of_mul_pos_right (lt_of_lt_of_le (by norm_num) hc) (sq_nonneg d)
  have hq : 2 ≤ q := by exact_mod_cast (Real.log_pos_iff (by positivity)).1 hL
  exact realBase hd (by exact_mod_cast hq) (by exact_mod_cast hr) hc

theorem realDegreeWitness : 4 < (2 : ℝ) ^ (3 * (3 / 2 : ℝ)) := by
  apply realBase (by norm_num) (by norm_num) (by norm_num)
  have h := Real.le_log_one_add_of_nonneg (by norm_num : (0 : ℝ) ≤ 1)
  norm_num at h ⊢
  linarith

theorem endpoint : (2 : ℝ) ^ ((2 : ℝ) * 1) = 4 := by norm_num

theorem sharpBoundary : 4 * Real.log 2 = (2 : ℝ) ^ 2 * Real.log 2 ∧
    ¬4 < (2 : ℝ) ^ ((2 : ℝ) * 1) := by norm_num

theorem zeroDegree {d q : ℝ} : ¬4 < q ^ (d * 0) := by simp

theorem zeroDeltaImpossible {q : ℕ} : ¬3 ≤ (0 : ℝ) ^ 2 * Real.log q := by norm_num

theorem lowBaseImpossible {d : ℝ} {q : ℕ} (hq : q ≤ 1) :
    ¬3 ≤ d ^ 2 * Real.log q := by
  interval_cases q <;> norm_num

theorem negativeDelta : 3 ≤ (-3 : ℝ) ^ 2 * Real.log (2 : ℕ) ∧
    ¬4 < (2 : ℝ) ^ ((-3 : ℝ) * (1 : ℕ)) := by
  have h := Real.le_log_one_add_of_nonneg (by norm_num : (0 : ℝ) ≤ 1)
  norm_num at h ⊢
  constructor
  · linarith
  · norm_num [Real.rpow_neg, Real.rpow_natCast]

theorem realBaseGuard : 1 < Real.exp (1 / 4) ∧
    3 ≤ (4 : ℝ) ^ 2 * Real.log (Real.exp (1 / 4)) ∧
    ¬4 < (Real.exp (1 / 4)) ^ ((4 : ℝ) * 1) := by
  have h2 := Real.lt_log_one_add_of_pos (by norm_num : (0 : ℝ) < 1)
  have hlog4 : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]
    norm_num
  have he : Real.exp 1 < 4 := (Real.exp_lt_iff_lt_log (by norm_num)).2 (by
    norm_num at h2
    linarith only [h2, hlog4])
  refine ⟨by simpa using Real.exp_lt_exp.mpr (by norm_num : (0 : ℝ) < 1 / 4), ?_, ?_⟩
  · norm_num
  · rw [Real.rpow_def_of_pos (Real.exp_pos _), Real.log_exp]
    norm_num
    exact he.le.not_gt

theorem existingTransport {a q z : ℝ} (hq : 0 < q) (h : Real.log a < z * Real.log q) :
    a < q ^ z := Real.lt_rpow_of_log_lt hq h

theorem primitiveProbe {d : ℝ} (hd : 0 ≤ d) {q r : ℕ} (hr : 0 < r)
    (hc : 3 ≤ d ^ 2 * Real.log q) : 4 < (q : ℝ) ^ (d * r) := by
  fail_if_success solve | exact?
  fail_if_success
    solve | exact Real.lt_rpow_of_log_lt (show (0 : ℝ) < q by positivity) hc
  exact original hd hr hc
'''
names=['squareTransfer','powerTransfer','sharper','realBase','original','realDegreeWitness','endpoint','sharpBoundary','zeroDegree','zeroDeltaImpossible','lowBaseImpossible','negativeDelta','realBaseGuard','existingTransport','primitiveProbe']
s+='\n'+'\n'.join('#print axioms '+n for n in names)+'\nend Four238Isolated\n'
assert max(map(len,s.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(s)
print(s)
