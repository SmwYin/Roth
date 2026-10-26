import Roth.Taylor

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

-- (1) project statement, project proof
example (α β : σ → R) (P : MvPolynomial σ R) :
    taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P := by
  simp [taylor, comp_aeval_apply, add_assoc]

-- (2) plain `simp` does not prove it (not a simp consequence of the existing simp set)
example (α β : σ → R) (P : MvPolynomial σ R) :
    taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P := by
  fail_if_success simp
  simp [taylor, comp_aeval_apply, add_assoc]

-- (3) mathlib-only composition (statement unfolded, no project `taylor`)
example (α β : σ → R) (P : MvPolynomial σ R) :
    aeval (fun j ↦ X j + C (α j)) (aeval (fun j ↦ X j + C (β j)) P) =
      aeval (fun j ↦ X j + C (α j + β j)) P := by
  rw [comp_aeval_apply]; simp [add_assoc]

-- (4) Pi-addition form, mirroring `Polynomial.taylor_taylor : taylor r (taylor s f) = taylor (r + s) f`
theorem taylor_taylor' (α β : σ → R) (P : MvPolynomial σ R) :
    taylor α (taylor β P) = taylor (α + β) P :=
  taylor_taylor α β P

-- (5) bundled AlgHom form
theorem taylor_comp_taylor (α β : σ → R) :
    (taylor α).comp (taylor β) = taylor (α + β) :=
  AlgHom.ext fun P ↦ taylor_taylor α β P

-- (6) translation as a monoid hom `Multiplicative (σ → R) →* End` (modern-idiom probe)
noncomputable def taylorHom : Multiplicative (σ → R) →* (MvPolynomial σ R →ₐ[R] MvPolynomial σ R) where
  toFun α := taylor α.toAdd
  map_one' := AlgHom.ext fun P ↦ taylor_zero P
  map_mul' α β := (taylor_comp_taylor α.toAdd β.toAdd).symm

end MvPolynomial
