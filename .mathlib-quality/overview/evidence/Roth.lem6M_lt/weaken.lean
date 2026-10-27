import Roth.Theta

/-! Evidence for `Roth.lem6M_lt`: weakened statement with
(a) real `q₁ ≥ 0` instead of a natural number,
(b) `l ≤ 2 ^ r₁` and `0 < l * r₁` instead of `1 ≤ l ≤ r₁`.
The private aux lemmas of Theta.lean are inaccessible here, so their proofs are inlined. -/

open Roth

theorem lem6M_lt_weak {p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ l : ℕ} {q₁ : ℝ}
    (hq0 : 0 ≤ q₁) (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁)
    (hlr : 0 < l * r₁) (hl' : l ≤ 2 ^ r₁) :
    lem6M p r₁ (q₁ ^ (δ * r₁)) l < q₁ ^ (δ * (1 + 1 / p) * (l * r₁)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp
  have hq : 0 < q₁ := zero_lt_one.trans <|
    (Real.log_pos_iff hq0).1 <| lt_of_lt_of_le (by positivity) hq₁
  have hnat : (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤
      2 ^ ((2 * p + 1) * r₁ * l) := by
    calc
      (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁)
          ≤ (2 ^ r₁) ^ (p * l) * (2 ^ r₁) ^ l * 2 ^ (p * l * r₁) := by
            gcongr
            · exact Nat.lt_two_pow_self
            · exact (Nat.factorial_le_pow l).trans (Nat.pow_le_pow_left hl' _)
      _ = 2 ^ ((2 * p + 1) * r₁ * l) := by
        rw [← pow_mul, ← pow_mul, ← pow_add, ← pow_add]
        ring_nf
  have hnatR : ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤
      2 ^ ((2 * p + 1) * r₁ * l) := by exact_mod_cast hnat
  have hlog2 : Real.log 2 < 1 :=
    (Real.log_lt_sub_one_of_pos (by norm_num : (0 : ℝ) < 2) (by norm_num)).trans_eq
      (by norm_num)
  have h3 : (2 * p + 1 : ℝ) ≤ Real.log q₁ * (δ / p) := by
    rw [mul_div_assoc', le_div_iff₀ hp0]
    rw [div_le_iff₀ hδ0] at hq₁
    linarith
  have h2 : (2 : ℝ) ^ ((2 * p + 1) * r₁ * l) < q₁ ^ (δ / p * (l * r₁)) := by
    rw [← Real.rpow_natCast, Real.rpow_def_of_pos (by norm_num), Real.rpow_def_of_pos hq,
      Real.exp_lt_exp]
    calc
      Real.log 2 * (((2 * p + 1) * r₁ * l : ℕ) : ℝ)
          = Real.log 2 * (2 * p + 1) * (l * r₁) := by push_cast; ring
      _ < Real.log q₁ * (δ / p) * (l * r₁) :=
        mul_lt_mul_of_pos_right
          ((mul_lt_of_lt_one_left (by positivity) hlog2).trans_le h3) (by exact_mod_cast hlr)
      _ = Real.log q₁ * (δ / p * (l * r₁)) := by ring
  calc
    lem6M p r₁ (q₁ ^ (δ * r₁)) l = ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial *
        2 ^ (p * l * r₁) * (q₁ ^ (δ * r₁)) ^ l := by rw [lem6M]; ring
    _ ≤ 2 ^ ((2 * p + 1) * r₁ * l) * (q₁ ^ (δ * r₁)) ^ l :=
      mul_le_mul_of_nonneg_right hnatR (by positivity)
    _ < q₁ ^ (δ / p * (l * r₁)) * (q₁ ^ (δ * r₁)) ^ l :=
      mul_lt_mul_of_pos_right h2 (by positivity)
    _ = q₁ ^ (δ * (1 + 1 / p) * (l * r₁)) := by
      rw [← Real.rpow_mul_natCast hq.le, ← Real.rpow_add hq]
      congr 1
      ring

/-- The original follows from the weakened form. -/
example {p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ q₁ : ℕ}
    (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) :
    lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) :=
  lem6M_lt_weak hp hδ0 (Nat.cast_nonneg _) hq₁ (Nat.mul_pos (by lia) (by lia))
    (hl'.trans Nat.lt_two_pow_self.le)

/-- `hl : 1 ≤ l` cannot simply be dropped: at `l = 0` both sides are `1`. -/
example (p r₁ : ℕ) (q₁ : ℝ) (δ : ℝ) :
    lem6M p r₁ (q₁ ^ (δ * r₁)) 0 = 1 ∧ q₁ ^ (δ * (1 + 1 / p) * ((0 : ℕ) * r₁)) = 1 := by
  simp [lem6M]
