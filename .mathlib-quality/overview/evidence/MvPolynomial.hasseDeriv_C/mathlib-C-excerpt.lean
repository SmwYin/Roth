  AddMonoidAlgebra R (σ →₀ ℕ)

namespace MvPolynomial

variable {σ : Type*} {a a' a₁ a₂ : R} {e : ℕ} {n m : σ} {s : σ →₀ ℕ}

section CommSemiring
variable [CommSemiring R] [CommSemiring S₁] {p q : MvPolynomial σ R}

/-- `monomial s a` is the monomial with coefficient `a` and exponents given by `s` -/
def monomial (s : σ →₀ ℕ) : R →ₗ[R] MvPolynomial σ R :=
  AddMonoidAlgebra.lsingle s

theorem one_def : (1 : MvPolynomial σ R) = monomial 0 1 := rfl

theorem single_eq_monomial (s : σ →₀ ℕ) (a : R) : .single s a = monomial s a :=
  rfl

theorem mul_def : p * q = p.coeff.sum fun m a => q.coeff.sum fun n b => monomial (m + n) (a * b) :=
  AddMonoidAlgebra.mul_def ..

/-- `C a` is the constant polynomial with value `a` -/
def C : R →+* MvPolynomial σ R :=
  { singleZeroRingHom with toFun := monomial 0 }

variable (R σ)

@[simp, polynomial_post]
theorem algebraMap_eq : algebraMap R (MvPolynomial σ R) = C :=
  rfl

@[polynomial_pre]
theorem C_eq_algebraMap : MvPolynomial.C = algebraMap R (MvPolynomial σ R) :=
  rfl

variable {R σ}

@[simp]
theorem algebraMap_apply [Algebra R S₁] (r : R) :
    algebraMap R (MvPolynomial σ S₁) r = C (algebraMap R S₁ r) :=
  rfl

/-- `X n` is the degree `1` monomial $X_n$. -/
def X (n : σ) : MvPolynomial σ R :=
  monomial (Finsupp.single n 1) 1

theorem monomial_left_injective {r : R} (hr : r ≠ 0) :
    Function.Injective fun s : σ →₀ ℕ => monomial s r :=
  single_left_injective hr

@[simp]
theorem monomial_left_inj {s t : σ →₀ ℕ} {r : R} (hr : r ≠ 0) :
    monomial s r = monomial t r ↔ s = t :=
  single_left_inj hr

theorem C_apply : (C a : MvPolynomial σ R) = monomial 0 a :=
  rfl

@[simp]
theorem C_0 : C 0 = (0 : MvPolynomial σ R) := map_zero _
