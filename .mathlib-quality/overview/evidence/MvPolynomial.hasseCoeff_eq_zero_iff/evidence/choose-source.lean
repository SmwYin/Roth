    choose n k = choose (n - 1) (k - 1) + choose (n - 1) k := by
  obtain ⟨l, rfl⟩ : ∃ l, k = l + 1 := Nat.exists_eq_add_of_le' hk
  rw [choose_succ_right _ _ hn, Nat.add_one_sub_one]

@[grind <=]
theorem choose_eq_zero_of_lt : ∀ {n k}, n < k → choose n k = 0
  | _, 0, hk => absurd hk (Nat.not_lt_zero _)
  | 0, _ + 1, _ => choose_zero_succ _
  | n + 1, k + 1, hk => by
    have hnk : n < k := lt_of_succ_lt_succ hk
    have hnk1 : n < k + 1 := lt_of_succ_lt hk
    rw [choose_succ_succ, choose_eq_zero_of_lt hnk, choose_eq_zero_of_lt hnk1]

@[simp]
theorem choose_self (n : ℕ) : choose n n = 1 := by
  induction n <;> grind

@[simp]
theorem choose_succ_self (n : ℕ) : choose n (succ n) = 0 :=
  choose_eq_zero_of_lt (lt_succ_self _)

@[simp]
lemma choose_one_right (n : ℕ) : choose n 1 = n := by induction n <;> simp [*, choose, Nat.add_comm]

-- The `n + 1`-st triangle number is `n` more than the `n`-th triangle number
theorem triangle_succ (n : ℕ) : (n + 1) * (n + 1 - 1) / 2 = n * (n - 1) / 2 + n := by
  rw [← add_mul_div_left, Nat.mul_comm 2 n, ← Nat.mul_add, Nat.add_sub_cancel, Nat.mul_comm]
  cases n <;> rfl; apply zero_lt_succ

/-- `choose n 2` is the `n`-th triangle number. -/
theorem choose_two_right (n : ℕ) : choose n 2 = n * (n - 1) / 2 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [triangle_succ n, choose, ih]
    simp [Nat.add_comm]

theorem choose_pos : ∀ {n k}, k ≤ n → 0 < choose n k
  | 0, _, hk => by rw [Nat.eq_zero_of_le_zero hk]; decide
  | n + 1, 0, _ => by simp
  | _ + 1, _ + 1, hk => Nat.add_pos_left (choose_pos (le_of_succ_le_succ hk)) _

theorem choose_eq_zero_iff {n k : ℕ} : n.choose k = 0 ↔ n < k :=
  ⟨fun h => lt_of_not_ge (mt Nat.choose_pos h.symm.not_lt), Nat.choose_eq_zero_of_lt⟩

theorem choose_ne_zero_iff {n k : ℕ} : n.choose k ≠ 0 ↔ k ≤ n :=
  not_iff_not.1 <| by simp [choose_eq_zero_iff]

lemma choose_ne_zero {n k : ℕ} (h : k ≤ n) : n.choose k ≠ 0 :=
  (choose_pos h).ne'

