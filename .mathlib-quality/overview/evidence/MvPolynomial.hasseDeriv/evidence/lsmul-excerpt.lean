theorem bijective_compr₂ₛₗ_of_equiv [RingHomInvPair σ₃₄ σ₄₃] [RingHomInvPair σ₄₃ σ₃₄]
    (f : M →ₛₗ[σ₁₃] N →ₛₗ[σ₂₃] P) (g : P ≃ₛₗ[σ₃₄] Q) (hf : Bijective f) :
    Bijective (f.compr₂ₛₗ g.toLinearMap) :=
  ⟨injective_compr₂ₛₗ_of_injective f g.toLinearMap hf.1 g.bijective.1,
  surjective_compr₂ₛₗ_of_equiv f g hf.2⟩

end CommSemiringSemilinear

variable (R M)

/-- Scalar multiplication as a bilinear map `R → M → M`. -/
def lsmul : R →ₗ[R] M →ₗ[R] M :=
  mk₂ R (· • ·) add_smul (fun _ _ _ => mul_smul _ _ _) smul_add fun r s m => by
    simp only [smul_smul, mul_comm]

variable {R}

lemma lsmul_eq_distribSMultoLinearMap (r : R) :
    lsmul R M r = DistribSMul.toLinearMap R M r := rfl
