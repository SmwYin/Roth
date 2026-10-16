import Roth.Box
import Roth.HasseDeriv

/-!
# Taylor expansion of multivariate polynomials

`MvPolynomial.taylor α P = P(X + α)` is the translation of `P` by `α`.  Its coefficient at the
multi-index `d` is the value `(Δ_d P)(α)` of the Hasse derivative, which is the content of
Taylor's theorem for polynomials in several variables.

## Main definitions

* `MvPolynomial.taylor α`: the `R`-algebra endomorphism `P ↦ P(X + α)`.

## Main results

* `MvPolynomial.coeff_taylor`: the coefficient of `P(X + α)` at `d` is `(Δ_d P)(α)`.
* `MvPolynomial.eq_sum_box_hasseDeriv`: Taylor's expansion
  `P = ∑_{d ≤ r} (Δ_d P)(α) ∏ (X_j - α_j)^{d_j}` when `deg_{X_j} P ≤ r_j`.
* `MvPolynomial.eval_eq_sum_box`: the evaluated form of Taylor's expansion.

## References

 Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §4 "Index", Theorem (Taylor's
expansion for polynomials in several variables) and the Lean implementation note following the
definition of the index (`.mathlib-quality/references/clean.tex`).
-/

namespace MvPolynomial

section CommSemiring

variable {σ R : Type*} [CommSemiring R]

/-- Translation `P ↦ P(X + α)`. Source: §4, Lean implementation note ("Let `P_α(X) = P(X+α)`"). -/
noncomputable def taylor (α : σ → R) : MvPolynomial σ R →ₐ[R] MvPolynomial σ R :=
  aeval fun j ↦ X j + C (α j)

/-- `taylor α` is evaluation at `X + α`. -/
theorem taylor_apply (α : σ → R) (P : MvPolynomial σ R) :
    taylor α P = aeval (fun j ↦ X j + C (α j)) P := rfl

/-- `taylor α` sends the variable `X j` to `X j + α j`. -/
@[simp]
theorem taylor_X (α : σ → R) (j : σ) : taylor α (X j) = X j + C (α j) := by
  simp [taylor]

/-- `taylor α` fixes constants. -/
@[simp]
theorem taylor_C (α : σ → R) (a : R) : taylor α (C a) = C a := by
  simp [taylor]

/-- The translate of a monomial is a product of powers of the translated variables.
Source: §4, proof of Taylor's theorem ("it suffices to prove the theorem for monomials"). -/
theorem taylor_monomial (α : σ → R) (k : σ →₀ ℕ) (a : R) :
    taylor α (monomial k a) = C a * k.prod fun j n => (X j + C (α j)) ^ n := by
  simp [taylor, aeval_monomial, algebraMap_eq]

private lemma coeff_aeval_X_mul (i : σ) (f : Polynomial R) (B : MvPolynomial σ R)
    (hB : ∀ e ∈ B.support, e i = 0) (d : σ →₀ ℕ) :
    (Polynomial.aeval (X i : MvPolynomial σ R) f * B).coeff d =
      f.coeff (d i) * B.coeff (d.erase i) := by
  classical
  have hA : Polynomial.aeval (X i : MvPolynomial σ R) f =
      ∑ m ∈ f.support, monomial (Finsupp.single i m) (f.coeff m) := by
    conv_lhs => rw [f.as_sum_support]
    simp [Polynomial.aeval_monomial, X_pow_eq_monomial, C_mul_monomial, algebraMap_eq]
  have herase : d - Finsupp.single i (d i) = d.erase i := by
    ext j
    obtain rfl | hj := eq_or_ne j i <;> simp [*, Finsupp.erase_ne]
  rw [hA, Finset.sum_mul, coeff_sum]
  simp_rw [coeff_monomial_mul']
  rw [Finset.sum_eq_single (d i)]
  · simp [herase]
  · intro m _ hne
    split_ifs with hle
    · have hlt : m < d i := (Finsupp.single_le_iff.1 hle).lt_of_ne hne
      rw [notMem_support_iff.1 fun h => by simpa [Nat.sub_eq_zero_iff_le, hlt.not_ge] using hB _ h,
        mul_zero]
    · rfl
  · intro hnot
    simp [Polynomial.notMem_support_iff.1 hnot]

private lemma hasseCoeff_single_add_eq {i : σ} {n : ℕ} {k' : σ →₀ ℕ}
    (hi : k' i = 0) (d : σ →₀ ℕ) :
    hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k' := by
  classical
  simp only [hasseCoeff]
  have hdisj : Disjoint (Finsupp.single i (d i)).support (d.erase i).support :=
    Finset.disjoint_left.2 fun j hj => by
      simp [Finset.mem_singleton.1 (Finsupp.support_single_subset hj)]
  conv_lhs => rw [← Finsupp.single_add_erase i d]
  rw [Finsupp.prod_add_index_of_disjoint hdisj, Finsupp.prod_single_index (by simp)]
  congr 1
  · simp [hi]
  · refine Finsupp.prod_congr fun j hj => ?_
    obtain rfl | hj' := eq_or_ne j i
    · simp at hj
    · simp [Finsupp.single_eq_of_ne hj']

private lemma prod_pow_single_add_tsub (α : σ → R) {i : σ} {n : ℕ} {k' : σ →₀ ℕ}
    (hi : k' i = 0) (d : σ →₀ ℕ) :
    ((Finsupp.single i n + k') - d).prod (fun j e => α j ^ e) =
      α i ^ (n - d i) * (k' - d.erase i).prod (fun j e => α j ^ e) := by
  classical
  have h : Finsupp.single i n + k' - d = Finsupp.single i (n - d i) + (k' - d.erase i) := by
    ext j
    obtain rfl | hj := eq_or_ne j i <;> simp [*, Finsupp.erase_ne]
  rw [h, Finsupp.prod_add_index' (fun _ => pow_zero _) (fun _ _ _ => pow_add _ _ _)]
  congr 1
  exact Finsupp.prod_single_index (pow_zero _)

/-- Taylor's theorem, coefficient form. Source: §4, Lean implementation note ("`P_α(X) = P(X+α)`,
whose coefficient at `d` is `(Δ_d P)(α)`"), proved as in the Theorem (Taylor's expansion) by
linearity and the one-variable binomial expansion on monomials. -/
theorem coeff_taylor (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (taylor α P).coeff d = eval α (hasseDeriv d P) := by
  classical
  induction P using MvPolynomial.induction_on' generalizing d with
  | add p q hp hq => simp [hp, hq]
  | monomial k a =>
    induction k using Finsupp.induction generalizing d with
    | zero =>
      rw [← C_apply, taylor_C, coeff_C, C_apply, hasseDeriv_monomial, eval_monomial]
      obtain rfl | hd := eq_or_ne d 0
      · simp [hasseCoeff]
      · have : hasseCoeff d 0 = 0 := (hasseCoeff_eq_zero_iff d 0).2 fun h => hd (le_zero_iff.1 h)
        simp [this, hd.symm]
    | single_add i n k' hi hn ih =>
      have hi' : k' i = 0 := Finsupp.notMem_support_iff.1 hi
      have hXC : (X i + C (α i) : MvPolynomial σ R) ^ n =
          Polynomial.aeval (X i) ((Polynomial.X + Polynomial.C (α i)) ^ n) := by
        simp [algebraMap_eq]
      have hsupp : ∀ e ∈ (taylor α (monomial k' a)).support, e i = 0 := by
        intro e he
        rw [mem_support_iff, ih e, hasseDeriv_monomial] at he
        by_contra h
        have : hasseCoeff e k' = 0 := (hasseCoeff_eq_zero_iff e k').2 fun hle => by
          have := hle i
          lia
        simp [this] at he
      have htay : taylor α (monomial (Finsupp.single i n + k') a) =
          Polynomial.aeval (X i) ((Polynomial.X + Polynomial.C (α i)) ^ n) *
            taylor α (monomial k' a) := by
        rw [monomial_single_add, map_mul, map_pow, taylor_X, hXC]
      rw [htay, coeff_aeval_X_mul i _ _ hsupp, ih, Polynomial.coeff_X_add_C_pow,
        hasseDeriv_monomial, hasseDeriv_monomial, eval_monomial, eval_monomial,
        hasseCoeff_single_add_eq hi', prod_pow_single_add_tsub α hi']
      push_cast
      ring

/-- Evaluating `P(X + α)` at `x` is evaluating `P` at `x + α`. -/
theorem eval_taylor (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j => x j + α j) P := by
  induction P using MvPolynomial.induction_on <;> simp_all

/-- Translations compose additively. -/
theorem taylor_taylor (α β : σ → R) (P : MvPolynomial σ R) :
    taylor α (taylor β P) = taylor (fun j => α j + β j) P := by
  induction P using MvPolynomial.induction_on <;> simp_all [add_assoc]

/-- Translation by `0` is the identity. -/
@[simp]
theorem taylor_zero (P : MvPolynomial σ R) : taylor (fun _ => (0 : R)) P = P := by
  induction P using MvPolynomial.induction_on <;> simp_all

/-- Translation commutes with changing the coefficient ring along `f`.
Source: §1, Lean implementation note ("compatibility with coefficient maps"). -/
theorem taylor_map {S : Type*} [CommSemiring S] (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    taylor (fun j => f (α j)) (map f P) = map f (taylor α P) := by
  induction P using MvPolynomial.induction_on <;> simp_all

/-- Translation commutes with renaming variables.
Source: §4, Lemma 4-2 ("When `P` is embedded into the larger polynomial ring, its translated
monomials have zero exponent in `x_p`"). -/
theorem taylor_rename {τ : Type*} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by
  induction P using MvPolynomial.induction_on <;> simp_all

/-- Translation does not increase the degree in any variable.
Source: §5 ("Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`"). -/
theorem degreeOf_taylor_le (α : σ → R) (j : σ) (P : MvPolynomial σ R) :
    degreeOf j (taylor α P) ≤ degreeOf j P := by
  refine degreeOf_le_iff.2 fun e he => not_lt.1 fun h => ?_
  rw [mem_support_iff, coeff_taylor, hasseDeriv_eq_zero_of_degreeOf_lt h, map_zero] at he
  exact he rfl

end CommSemiring

section CommRing

variable {σ A : Type*} [CommRing A]

/-- Translation by `-α` undoes translation by `α`. -/
theorem taylor_neg_taylor (α : σ → A) (P : MvPolynomial σ A) :
    taylor (fun j => -α j) (taylor α P) = P := by
  simp [taylor_taylor]

/-- Over a ring, translation is injective, since translation by `-α` is a left inverse. -/
theorem taylor_injective (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) :=
  Function.LeftInverse.injective (taylor_neg_taylor α)

/-- A polynomial vanishes iff its translate does. -/
@[simp]
theorem taylor_eq_zero_iff (α : σ → A) (P : MvPolynomial σ A) : taylor α P = 0 ↔ P = 0 :=
  (taylor_injective α).eq_iff' (map_zero _)

/-- Taylor's theorem, polynomial form. Source: §4, Theorem (Taylor's expansion for polynomials in
several variables): `P = ∑_{i ≤ d} (Δ_i P)(α) ∏ (x_j - α_j)^{i_j}` when `d_i ≥ r_i`. -/
theorem eq_sum_box_hasseDeriv [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by
  have h1 : taylor α P = ∑ d ∈ Roth.box r, monomial d (eval α (hasseDeriv d P)) := by
    ext e
    rw [coeff_taylor, coeff_sum]
    simp only [coeff_monomial, Finset.sum_ite_eq']
    split_ifs with he
    · rfl
    · obtain ⟨j, hj⟩ : ∃ j, r j < e j := by
        simpa [Roth.mem_box] using he
      rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hP j).trans_lt hj), map_zero]
  calc P = taylor (fun j => -α j) (taylor α P) := (taylor_neg_taylor α P).symm
    _ = _ := by
      rw [h1, map_sum]
      refine Finset.sum_congr rfl fun d _ => ?_
      rw [taylor_monomial, Finsupp.prod_fintype _ _ fun _ => pow_zero _]
      simp [sub_eq_add_neg]

/-- Taylor's theorem, evaluation form. Source: §7 ("`Q(h_1/q_1, …) = ∑ Δ_i Q(α,…,α) ∏ (h_j/q_j -
α)^{i_j}`"). -/
theorem eval_eq_sum_box [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by
  conv_lhs => rw [eq_sum_box_hasseDeriv α r P hP]
  simp

end CommRing

end MvPolynomial
