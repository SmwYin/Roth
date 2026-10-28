from pathlib import Path
D=Path(__file__).resolve().parent
body='''
#check_failure Roth.mainCoeffBound
#check_failure Roth.sqrt_lt_floor
#check @Nat.floor
#check @Real.rpow
#check @Nat.floor_le
#check @Nat.lt_floor_add_one
#check @Nat.floor_pos
#check @Nat.le_floor_iff
#check @FloorSemiring.gc_floor
#check @Int.natCast_floor_eq_floor
#check @Int.le_floor
#check @Real.zero_rpow
#check @Real.rpow_lt_one_of_one_lt_of_neg
namespace Coeff232Isolated
noncomputable def formula (δ : ℝ) (q r : ℕ) : ℕ :=
  Nat.floor (Real.rpow (q : ℝ) (δ * (r : ℝ)))
noncomputable def floorPower (q e : ℝ) : ℕ := ⌊q ^ e⌋₊
theorem direct (δ : ℝ) (q r : ℕ) :
    formula δ q r = Nat.floor (Real.rpow (q : ℝ) (δ * (r : ℝ))) := rfl
theorem expanded (δ : ℝ) (q r : ℕ) : formula δ q r = floorPower q (δ * r) := rfl
theorem endpoints (q e : ℝ) (hq : 0 ≤ q) :
    (floorPower q e : ℝ) ≤ q ^ e ∧ q ^ e < (floorPower q e : ℝ) + 1 :=
  ⟨Nat.floor_le (Real.rpow_nonneg hq e), Nat.lt_floor_add_one _⟩
theorem coefficientInterval (X : ℝ) (hX : 0 ≤ X) (z : ℤ) :
    |z| ≤ (⌊X⌋₊ : ℤ) ↔ |(z : ℝ)| ≤ X := by
  rw [Int.natCast_floor_eq_floor hX, Int.le_floor, Int.cast_abs]
theorem positive (δ : ℝ) (q r : ℕ) :
    0 < formula δ q r ↔ 1 ≤ (q : ℝ) ^ (δ * r) := Nat.floor_pos
theorem zeroExponent (q : ℝ) : floorPower q 0 = 1 := by simp [floorPower]
theorem deltaZero (q r : ℕ) : formula 0 q r = 1 := by simp [formula]
theorem degreeZero (δ : ℝ) (q : ℕ) : formula δ q 0 = 1 := by simp [formula]
theorem baseOne (δ : ℝ) (r : ℕ) : formula δ 1 r = 1 := by simp [formula]
theorem baseZero (δ : ℝ) (r : ℕ) :
    formula δ 0 r = if δ * (r : ℝ) = 0 then 1 else 0 := by
  by_cases h : δ * (r : ℝ) = 0
  · simp [formula, h]
  · simp [formula, Real.zero_rpow h, h]
theorem negativeDelta (δ : ℝ) (q r : ℕ) (hδ : δ < 0) (hq : 1 < q) (hr : 0 < r) :
    formula δ q r = 0 := by
  apply Nat.floor_eq_zero.2
  exact Real.rpow_lt_one_of_one_lt_of_neg (by exact_mod_cast hq)
    (mul_neg_of_neg_of_pos hδ (by exact_mod_cast hr))
theorem negativeExample : formula (-1) 2 1 = 0 := negativeDelta _ _ _ (by norm_num)
  (by norm_num) (by norm_num)
theorem natExponent (q r : ℕ) : formula 1 q r = q ^ r := by
  unfold formula
  rw [one_mul, Real.rpow_eq_pow, Real.rpow_natCast, ← Nat.cast_pow, Nat.floor_natCast]
theorem integerEndpoint : (formula 1 2 1 : ℝ) = (2 : ℝ) ^ (1 * (1 : ℕ)) := by
  norm_num [natExponent]
theorem sqrtLower {X : ℝ} (hX : 2 ≤ X) : √X < ⌊X⌋₊ := by
  have hf : (2 : ℝ) ≤ ⌊X⌋₊ := by exact_mod_cast Nat.le_floor hX
  exact (Real.sqrt_lt' (by positivity)).2
    (by nlinarith only [Nat.lt_floor_add_one X, hf])
theorem abstractFloor {K : Type*} [Semiring K] [PartialOrder K] [FloorSemiring K]
    {x : K} (hx : 0 ≤ x) (n : ℕ) : n ≤ ⌊x⌋₊ ↔ (n : K) ≤ x := Nat.le_floor_iff hx
#check_failure (inferInstance : CoeFun ℕ (fun _ : ℕ ↦ ℝ → ℝ))
'''
import re
body+='\n'.join('#print axioms '+n for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))
body+='\nend Coeff232Isolated\n'
code=(D/'isolated-prefix.lean.txt').read_text()+body
assert max(map(len,code.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(code)
print(code)
