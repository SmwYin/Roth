
variable {R : Type*} [Semiring R] (k : ℕ) (f : R[X])

/-- The `k`th Hasse derivative of a polynomial `∑ a_i X^i` is `∑ (i.choose k) a_i X^(i-k)`.
It satisfies `k! * (hasse_deriv k f) = derivative^[k] f`. -/
def hasseDeriv (k : ℕ) : R[X] →ₗ[R] R[X] :=
  lsum fun i => monomial (i - k) ∘ₗ DistribSMul.toLinearMap R R (i.choose k)

theorem hasseDeriv_apply :
    hasseDeriv k f = f.sum fun i r => monomial (i - k) (↑(i.choose k) * r) := by
  dsimp [hasseDeriv]
  simp

theorem hasseDeriv_coeff (n : ℕ) :
    (hasseDeriv k f).coeff n = (n + k).choose k * f.coeff (n + k) := by
  rw [hasseDeriv_apply, coeff_sum, sum_def, Finset.sum_eq_single (n + k), coeff_monomial]
  · simp
  · #adaptation_note
    /-- Prior to nightly-2025-08-14, this was working as
    `grind [coeff_monomial, Nat.choose_eq_zero_of_lt, Nat.cast_zero, zero_mul]` -/
    intro i _hi hink
    rw [coeff_monomial]
    by_cases hik : i < k
    · simp only [Nat.choose_eq_zero_of_lt hik, ite_self, Nat.cast_zero, zero_mul]
    · grind
  · intro h
    simp only [notMem_support_iff.mp h, monomial_zero_right, mul_zero, coeff_zero]

theorem hasseDeriv_zero' : hasseDeriv 0 f = f := by
  simp only [hasseDeriv_apply, Nat.sub_zero, choose_zero_right, cast_one, one_mul, sum_monomial_eq]

@[simp]
theorem hasseDeriv_zero : @hasseDeriv R _ 0 = LinearMap.id :=
  LinearMap.ext <| hasseDeriv_zero'

theorem hasseDeriv_eq_zero_of_lt_natDegree (p : R[X]) (n : ℕ) (h : p.natDegree < n) :
    hasseDeriv n p = 0 := by
  rw [hasseDeriv_apply, sum_def]
  refine Finset.sum_eq_zero fun x hx => ?_
  simp [Nat.choose_eq_zero_of_lt ((le_natDegree_of_mem_supp _ hx).trans_lt h)]

theorem hasseDeriv_one' : hasseDeriv 1 f = derivative f := by
  simp only [hasseDeriv_apply, derivative_apply, ← C_mul_X_pow_eq_monomial, Nat.choose_one_right,
    (Nat.cast_commute _ _).eq]

@[simp]
theorem hasseDeriv_one : @hasseDeriv R _ 1 = derivative :=
  LinearMap.ext <| hasseDeriv_one'

@[simp]
theorem hasseDeriv_monomial (n : ℕ) (r : R) :
    hasseDeriv k (monomial n r) = monomial (n - k) (↑(n.choose k) * r) := by
  ext i
  simp only [hasseDeriv_coeff, coeff_monomial]
  by_cases hnik : n = i + k
  · grind
  · rw [ite_eq_right hnik, mul_zero]
    by_cases! hkn : k ≤ n
    · rw [← tsub_eq_iff_eq_add_of_le hkn] at hnik
      rw [ite_eq_right hnik]
    · rw [Nat.choose_eq_zero_of_lt hkn, Nat.cast_zero, zero_mul, ite_self]

theorem hasseDeriv_C (r : R) (hk : 0 < k) : hasseDeriv k (C r) = 0 := by
  rw [← monomial_zero_left, hasseDeriv_monomial, Nat.choose_eq_zero_of_lt hk, Nat.cast_zero,
    zero_mul, monomial_zero_right]

theorem hasseDeriv_apply_one (hk : 0 < k) : hasseDeriv k (1 : R[X]) = 0 := by
  rw [← C_1, hasseDeriv_C k _ hk]

theorem hasseDeriv_X (hk : 1 < k) : hasseDeriv k (X : R[X]) = 0 := by
  rw [← monomial_one_one_eq_X, hasseDeriv_monomial, Nat.choose_eq_zero_of_lt hk, Nat.cast_zero,
    zero_mul, monomial_zero_right]

@[simp]
theorem hasseDeriv_map {S : Type*} [Semiring S] (f : R →+* S) (k : ℕ) (p : R[X]) :
    hasseDeriv k (p.map f) = (hasseDeriv k p).map f := by
  ext
  simp [hasseDeriv_coeff]

theorem factorial_smul_hasseDeriv : ⇑(k ! • @hasseDeriv R _ k) = (@derivative R _)^[k] := by
  induction k with
  | zero => rw [hasseDeriv_zero, factorial_zero, iterate_zero, one_smul, LinearMap.id_coe]
  | succ k ih => ?_
  ext f n : 2
  rw [iterate_succ_apply', ← ih]
  simp only [LinearMap.smul_apply, coeff_smul, LinearMap.map_smul_of_tower, coeff_derivative,
    hasseDeriv_coeff, ← @choose_symm_add _ k]
  simp only [nsmul_eq_mul, factorial_succ, mul_assoc, succ_eq_add_one, ← add_assoc,
    add_right_comm n 1 k, ← cast_succ]
  rw [← (cast_commute (n + 1) (f.coeff (n + k + 1))).eq]
  simp only [← mul_assoc]
  norm_cast
  congr 2
  rw [mul_comm (k + 1) _, mul_assoc, mul_assoc]
