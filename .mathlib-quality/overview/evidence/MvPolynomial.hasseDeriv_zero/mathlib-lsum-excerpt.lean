
variable (S)
variable [Module S N] [SMulCommClass R₂ S N]

set_option backward.isDefEq.respectTransparency false in
/-- Lift a family of linear maps `M →ₗ[R] N` indexed by `x : α` to a linear map from `α →₀ M` to
`N` using `Finsupp.sum`. This is an upgraded version of `Finsupp.liftAddHom`.

See note [bundled maps over different rings] for why separate `R` and `S` semirings are used.
-/
def lsum : (α → M →ₛₗ[σ] N) ≃ₗ[S] (α →₀ M) →ₛₗ[σ] N where
  toFun F :=
    { toFun := fun d => d.sum fun i => F i
      map_add' := (liftAddHom (α := α) (M := M) (N := N) fun x => (F x).toAddMonoidHom).map_add
      map_smul' := fun c f => by simp [sum_smul_index', smul_sum] }
  invFun F x := F.comp (lsingle x)
  left_inv F := by
    ext x y
    simp
  right_inv F := by
    ext x y
    simp
  map_add' F G := by
    ext x y
    simp
  map_smul' F G := by
    ext x y
    simp

@[simp]
theorem coe_lsum (f : α → M →ₛₗ[σ] N) : (lsum S f : (α →₀ M) → N) = fun d => d.sum fun i => f i :=
  rfl

theorem lsum_apply (f : α → M →ₛₗ[σ] N) (l : α →₀ M) : Finsupp.lsum S f l = l.sum fun b => f b :=
  rfl

theorem lsum_single (f : α → M →ₛₗ[σ] N) (i : α) (m : M) :
    Finsupp.lsum S f (Finsupp.single i m) = f i m :=
  Finsupp.sum_single_index (f i).map_zero

@[simp] theorem lsum_comp_lsingle (f : α → M →ₛₗ[σ] N) (i : α) :
    Finsupp.lsum S f ∘ₛₗ lsingle i = f i := by ext; simp

theorem lsum_symm_apply (f : (α →₀ M) →ₛₗ[σ] N) (x : α) : (lsum S).symm f x = f.comp (lsingle x) :=
  rfl

end LSum
