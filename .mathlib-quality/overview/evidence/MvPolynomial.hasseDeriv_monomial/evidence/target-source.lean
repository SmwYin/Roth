theorem hasseDeriv_monomial (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by
  simp [hasseDeriv]
