
@[simp]
theorem hasseDeriv_map {S : Type*} [Semiring S] (f : R →+* S) (k : ℕ) (p : R[X]) :
    hasseDeriv k (p.map f) = (hasseDeriv k p).map f := by
  ext
  simp [hasseDeriv_coeff]

theorem factorial_smul_hasseDeriv : ⇑(k ! • @hasseDeriv R _ k) = (@derivative R _)^[k] := by
  induction k with
  | zero => rw [hasseDeriv_zero, factorial_zero, iterate_zero, one_smul, LinearMap.id_coe]
  | succ k ih => ?_
