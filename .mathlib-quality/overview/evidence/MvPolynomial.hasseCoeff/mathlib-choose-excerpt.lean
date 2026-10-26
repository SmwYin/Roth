
/-- `choose n k` is the number of `k`-element subsets in an `n`-element set. Also known as binomial
coefficients. For the fact that this is the number of `k`-element-subsets of an `n`-element
set, see `Finset.card_powersetCard`. -/
def choose : ℕ → ℕ → ℕ
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => choose n k + choose n (k + 1)

@[simp, grind =]
theorem choose_zero_right (n : ℕ) : choose n 0 = 1 := by cases n <;> rfl

@[simp, grind =]
theorem choose_zero_succ (k : ℕ) : choose 0 (succ k) = 0 :=
