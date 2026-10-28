from pathlib import Path
D=Path(__file__).parent
prior=Path('/private/tmp/roth-overview/assess/Roth.mul_log_div_two_lt_log_mainCoeffBound/isolated-executed.lean.txt').read_text()
a=prior.index('theorem rootFloor');b=prior.index('theorem original')
helpers=prior[a:b]
mod=(D/'source-MainLemma.lean.txt').read_text()
a=mod.index('private lemma two_lt_rpow_aux');b=mod.index('/-- For positive `r_1`',a)
two=mod[a:b].replace('private lemma two_lt_rpow_aux','theorem twoPower')
a=mod.index('theorem three_small_factors');b=mod.index('private lemma exists_norm_coeff',a)
target=mod[a:b].replace('theorem three_small_factors','theorem logDomain').replace('(hA : 0 ≤ A)','(hlogA : 0 ≤ Real.log (1 + A))')
target=target.replace('  have hlogA : 0 ≤ Real.log (1 + A) := Real.log_nonneg (le_add_of_nonneg_right hA)\n','')
target=target.replace('mainCoeffBound δ q₁ r₁','⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊').replace('two_lt_rpow_aux','twoPower')
target=target.replace('(sqrt_lt_floor hX).1','(rootFloor hX)').replace('(mul_log_div_two_lt_log_mainCoeffBound hX)','(realPower (Nat.cast_nonneg _) hX)')
# The concrete floor expression must be parenthesized at function arguments.
target=target.replace('(y := ⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊)','(y := (⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊ : ℝ))')
extra='''
theorem floorPower {X t δ : ℝ} {s : ℕ} (hX : 2 ≤ X) (hδ : 0 < δ)
    (h : (s : ℝ) * Real.log t ≤ δ * Real.log X / 2) :
    t ^ s < (⌊X⌋₊ : ℝ) ^ δ := by
  apply Real.lt_rpow_of_log_lt ((Real.sqrt_nonneg X).trans_lt (rootFloor hX))
  rw [Real.log_pow]
  exact h.trans_lt (by nlinarith only [mul_lt_mul_of_pos_left (logFloor hX) hδ])

theorem existingTransport {t B δ : ℝ} {s : ℕ} (hB : 0 < B)
    (h : (s : ℝ) * Real.log t < δ * Real.log B) : t ^ s < B ^ δ :=
  Real.lt_rpow_of_log_lt hB ((Real.log_pow t s).symm ▸ h)

theorem original {δ : ℝ} (hδ : 0 ≤ δ) {m q r : ℕ} (hr : 0 < r) {A α : ℝ}
    (hA : 0 ≤ A) (h : 2 * m + 1 + 2 * m * Real.log (1 + A) +
      2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log q) :
    (2 : ℝ) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + A) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + |α|) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ :=
  logDomain hδ hr (Real.log_nonneg (le_add_of_nonneg_right hA)) h

theorem zeroVariables {δ A α : ℝ} {q r : ℕ} (hδ : 0 ≤ δ) (hr : 0 < r)
    (h : 1 ≤ δ ^ 2 * Real.log q) :
    (2 : ℝ) ^ (0 * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + A) ^ (0 * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + |α|) ^ (0 * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ := by
  simpa only [zero_mul, pow_zero] using
    (original (m := 0) (A := 0) (α := 0) hδ hr le_rfl (by simpa using h))

theorem negativeAAllowed {δ : ℝ} {m q r : ℕ} (hδ : 0 ≤ δ) (hr : 0 < r) {α : ℝ}
    (h : 2 * m + 1 + 2 * m * Real.log (1 + (-2 : ℝ)) +
      2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log q) :
    (2 : ℝ) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + (-2 : ℝ)) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + |α|) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ :=
  logDomain hδ hr (by norm_num) h

theorem noASignGuard :
    0 < 1 + (Real.exp (-2) - 1) ∧
    (2 * (1 : ℕ) + 1 + 2 * (1 : ℕ) * Real.log (1 + (Real.exp (-2) - 1)) +
      2 * (1 : ℕ) * Real.log (1 + |(0 : ℝ)|) ≤ (0 : ℝ) ^ 2 * Real.log (2 : ℕ)) ∧
    ¬ (2 : ℝ) ^ ((1 : ℕ) * 1) < (⌊(2 : ℝ) ^ ((0 : ℝ) * (1 : ℕ))⌋₊ : ℝ) ^ (0 : ℝ) := by
  norm_num
  positivity

theorem noRPositiveGuard :
    1 ≤ (1 : ℝ) ^ 2 * Real.log (⌈Real.exp 1⌉₊ : ℕ) ∧
    ¬ (2 : ℝ) ^ ((0 : ℕ) * 0) <
      (⌊((⌈Real.exp 1⌉₊ : ℕ) : ℝ) ^ ((1 : ℝ) * (0 : ℕ))⌋₊ : ℝ) ^ (1 : ℝ) := by
  constructor
  · simpa using Real.log_le_log (Real.exp_pos 1) (Nat.le_ceil (Real.exp 1))
  · norm_num

theorem noDeltaSignGuard :
    (3 : ℝ) ≤ (-3 : ℝ) ^ 2 * Real.log (2 : ℕ) ∧
    ¬ (2 : ℝ) ^ ((1 : ℕ) * 1) < (⌊(2 : ℝ) ^ ((-3 : ℝ) * (1 : ℕ))⌋₊ : ℝ) ^ (-3 : ℝ) := by
  constructor
  · have h := Real.one_sub_inv_le_log_of_pos (by norm_num : (0 : ℝ) < 2)
    norm_num at h ⊢
    linarith only [h]
  · norm_num [Nat.floor_eq_zero.mpr (by norm_num : (1 / 8 : ℝ) < 1)]

theorem budgetEqualityWitness :
    0 ≤ Real.sqrt (1 / Real.log 2) ∧
      (1 : ℝ) = Real.sqrt (1 / Real.log 2) ^ 2 * Real.log (2 : ℕ) := by
  have hlog : 0 < Real.log 2 := Real.log_pos (by norm_num)
  constructor
  · positivity
  · rw [Real.sq_sqrt (by positivity)]
    norm_num

theorem noSlackGuard :
    (2 * (0 : ℕ) + 2 * (0 : ℕ) * Real.log (1 + (0 : ℝ)) +
      2 * (0 : ℕ) * Real.log (1 + |(0 : ℝ)|) ≤ (0 : ℝ) ^ 2 * Real.log (2 : ℕ)) ∧
      ¬ (2 : ℝ) ^ ((0 : ℕ) * 1) <
        (⌊(2 : ℝ) ^ ((0 : ℝ) * (1 : ℕ))⌋₊ : ℝ) ^ (0 : ℝ) := by norm_num

theorem boundaryStillStrict {δ : ℝ} {m q r : ℕ} {A α : ℝ}
    (hδ : 0 ≤ δ) (hr : 0 < r) (hA : 0 ≤ A)
    (h : 2 * m + 1 + 2 * m * Real.log (1 + A) +
      2 * m * Real.log (1 + |α|) = δ ^ 2 * Real.log q) :
    (2 : ℝ) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + A) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ ∧
      (1 + |α|) ^ (m * r) < (⌊(q : ℝ) ^ (δ * r)⌋₊ : ℝ) ^ δ := original hδ hr hA h.le

theorem primitiveProbe {X t δ : ℝ} {s : ℕ} (hX : 2 ≤ X) (hδ : 0 < δ)
    (h : (s : ℝ) * Real.log t ≤ δ * Real.log X / 2) :
    t ^ s < (⌊X⌋₊ : ℝ) ^ δ := by
  fail_if_success
    exact Real.lt_rpow_of_log_lt zero_lt_one h
  fail_if_success
    exact Real.pow_lt_iff_lt_log zero_lt_one zero_lt_one |>.2 h
  exact floorPower hX hδ h
'''
s=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.three_small_factors\nnamespace Fact241Isolated\n'+helpers+two+target+extra
for n in ['Real.lt_rpow_of_log_lt','Real.log_pow','Real.log_rpow','Nat.floor_le','Nat.lt_floor_add_one','Real.pow_lt_iff_lt_log','Real.log_nonneg','Real.log_lt_sub_one_of_pos']:
 s+='\n#check @'+n
for n in ['rootFloor','logFloor','realPower','twoPower','logDomain','floorPower','existingTransport','original','zeroVariables','negativeAAllowed','noASignGuard','noRPositiveGuard','noDeltaSignGuard','budgetEqualityWitness','noSlackGuard','boundaryStillStrict','primitiveProbe']:
 s+='\n#print axioms '+n
s+='\nend Fact241Isolated\n'
s=s.replace('(hlogA : 0 ≤ Real.log (1 + A)) (h32 :', '(hlogA : 0 ≤ Real.log (1 + A))\n    (h32 :')
s=s.replace('    nlinarith only [mul_le_mul_of_nonneg_left h (Nat.cast_nonneg r₁),', '    nlinarith only [mul_le_mul_of_nonneg_left h (Nat.cast_nonneg r₁),')
for l in s.splitlines():
 if len(l)>100:print(len(l),l)
assert max(map(len,s.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(s)
print('Prepared exact18 isolated source; width100; no project definitions.')
