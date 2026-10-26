  | add p q hp hq => simp [hp, hq, mul_add]

/-- Over a finite set of variables, `hasseCoeff d k` is the full product
`∏ j, (k j).choose (d j)`.

Source: §1, Lean implementation note. -/
theorem hasseCoeff_eq_prod [Fintype σ] (d k : σ →₀ ℕ) : hasseCoeff d k = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _

/-- `Δ_0` is the identity, pointwise version of `hasseDeriv_zero`.
