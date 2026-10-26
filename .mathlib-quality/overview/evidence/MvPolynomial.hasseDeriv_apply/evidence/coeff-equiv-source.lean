instance : Module R S[M] := fast_instance% coeffAddEquiv.module _

@[to_additive]
instance instIsTorsionFree [IsTorsionFree R S] : IsTorsionFree R S[M] :=
  coeffAddEquiv.moduleIsTorsionFree _

variable (R) in
/-- `MonoidAlgebra.coeff` as a linear equiv. -/
@[to_additive (attr := simps! apply symm_apply)
/-- `MonoidAlgebra.coeff` as a linear equiv. -/]
def coeffLinearEquiv : S[M] ≃ₗ[R] M →₀ S := coeffAddEquiv.linearEquiv _

variable (R S) in
/-- `MonoidAlgebra.mapDomain` as a linear map. -/
@[to_additive /-- `AddMonoidAlgebra.mapDomain` as a linear map. -/]
def mapDomainLinearMap (f : M → N) : S[M] →ₗ[R] S[N] :=
  (coeffLinearEquiv _).symm.toLinearMap ∘ₗ Finsupp.lmapDomain _ _ f ∘ₗ
    (coeffLinearEquiv _).toLinearMap

@[to_additive (attr := simp)]
lemma coeff_mapDomainLinearMap (f : M → N) (x : S[M]) :
