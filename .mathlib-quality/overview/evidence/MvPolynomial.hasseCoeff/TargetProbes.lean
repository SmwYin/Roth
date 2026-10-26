import Roth.HasseDeriv

set_option pp.universes true
#check @MvPolynomial.hasseCoeff
#print MvPolynomial.hasseCoeff
#print axioms MvPolynomial.hasseCoeff
#check @Finsupp.prod
#check @Nat.choose
#synth CommMonoid ℕ
#synth Zero ℕ

universe u
variable {σ : Type u}
-- Semireducibility, orientation, and equality to the two mathlib primitives.
example (d k : σ →₀ ℕ) : MvPolynomial.hasseCoeff d k =
    Finsupp.prod d (fun j n ↦ Nat.choose (k j) n) := rfl
example (d k : σ →₀ ℕ) :
    Finsupp.prod d (fun j n ↦ Nat.choose (k j) n) = MvPolynomial.hasseCoeff d k := rfl
-- Output has the existing natural-number structure; no new instance target is created.
example (d k : σ →₀ ℕ) : MvPolynomial.hasseCoeff d k * 1 =
    MvPolynomial.hasseCoeff d k := mul_one _
-- The only function coercion is the pre-existing Finsupp coercion.
#synth CoeFun (σ →₀ ℕ) (fun _ ↦ σ → ℕ)
#check fun (d k : σ →₀ ℕ) ↦ (MvPolynomial.hasseCoeff d k : ℤ)
#check fun (d k : σ →₀ ℕ) ↦ (MvPolynomial.hasseCoeff d k : ℕ)
#check fun (d k : ℕ →₀ ℕ) ↦ MvPolynomial.hasseCoeff d k
#check fun (d k : ULift.{1} ℕ →₀ ℕ) ↦ MvPolynomial.hasseCoeff d k
#check fun (d k : σ →₀ ℕ) ↦ MvPolynomial.hasseCoeff d k
-- Mechanically verified weakening: the upper multi-index needs only a function.
def upperFunctionCoeff (d : σ →₀ ℕ) (k : σ → ℕ) : ℕ :=
  Finsupp.prod d (fun j n ↦ Nat.choose (k j) n)
example (d k : σ →₀ ℕ) : upperFunctionCoeff d k = MvPolynomial.hasseCoeff d k := rfl
-- Finite-variable alternative, verified against the actual declaration.
example [Fintype σ] (d k : σ →₀ ℕ) :
    MvPolynomial.hasseCoeff d k = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _)
