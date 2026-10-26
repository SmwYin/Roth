private lemma coeff_taylor_monomial_aux (α : σ → R) (d k : σ →₀ ℕ) (a : R) :
    (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a)) := by
  classical
  induction k using Finsupp.induction generalizing d with
  | zero =>
    obtain rfl | hd := eq_or_ne d 0
    · simp
    · simp [← C_apply, hasseDeriv_C hd, hd.symm]
  | single_add i n k hi _ ih =>
    exact coeff_taylor_monomial_single_add_aux α a n (Finsupp.notMem_support_iff.1 hi) ih d

