import Mathlib.Algebra.MvPolynomial.Polynomial
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

import Roth.Box
import Roth.HasseDeriv

/-!
# Coefficient norms of integer polynomials

For `P : MvPolynomial σ ℤ` we use the ℓ¹ norm `normOne P = ∑ |coeff d P|` of the coefficients
and sup-bounds `∀ d, |coeff d P| ≤ B`.  This file collects the estimates needed for the
coefficient bound of the determinant `F` (Lemma 3) and for the size estimates in Roth's main
lemma (Lemma 9): Hasse derivatives, diagonal substitution `x_1 = ⋯ = x_m = x`, and evaluation.

## Main definitions

* `Roth.normOne P`: the ℓ¹ norm `∑ |a_e|` of the coefficients of `P : MvPolynomial σ ℤ`.
* `Roth.diag P`: the one-variable polynomial `P(x, …, x)`.

## Main results

* `Roth.normOne_mul_le`, `Roth.normOne_det_le`: submultiplicativity of `normOne` and the
  resulting bound `l! C^l` for an `l × l` determinant with entries of norm at most `C`.
* `Roth.normOne_hasseDeriv_le`: a Hasse derivative increases `normOne` by at most `2^{∑ r_j}`.
* `Roth.abs_coeff_det_hasseDeriv_le`: Lemma 3, the coefficient bound for a determinant of Hasse
  derivatives.
* `Roth.abs_coeff_diag_le`, `Roth.abs_eval_le`: coefficient and value bounds used in Lemma 9.

## References

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §3 Lemma 3 (and its Lean implementation
note) and §6 Lemma 9 (`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open MvPolynomial

variable {σ : Type*}

/-- The ℓ¹ norm `‖P‖₁ = ∑ |a_e|` of the coefficients. Source: §3, proof of Lemma 3. -/
noncomputable def normOne (P : MvPolynomial σ ℤ) : ℝ := ∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|

/-- The ℓ¹ norm of the coefficients is nonnegative. -/
theorem normOne_nonneg (P : MvPolynomial σ ℤ) : 0 ≤ normOne P :=
  Finset.sum_nonneg fun _ _ ↦ abs_nonneg _

/-- `normOne P` can be computed over any finite set of exponents containing the support. -/
theorem normOne_eq_sum_of_support_subset {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)}
    (hs : P.support ⊆ s) : normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)| :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]

/-- The ℓ¹ norm of a monomial is the absolute value of its coefficient. -/
theorem normOne_monomial (e : σ →₀ ℕ) (c : ℤ) : normOne (monomial e c) = |(c : ℝ)| := by
  classical
  rw [normOne_eq_sum_of_support_subset support_monomial_subset]
  simp

/-- The zero polynomial has ℓ¹ norm `0`. -/
@[simp]
theorem normOne_zero : normOne (0 : MvPolynomial σ ℤ) = 0 := by
  simp [normOne]

/-- Each coefficient is bounded in absolute value by the ℓ¹ norm.
Source: §3, Lean note ("Prove `abc(f) ≤ ‖f‖₁`"). -/
theorem abs_coeff_le_normOne (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) :
    |((P.coeff d : ℤ) : ℝ)| ≤ normOne P := by
  by_cases hd : d ∈ P.support
  · exact Finset.single_le_sum (f := fun d => |((P.coeff d : ℤ) : ℝ)|)
      (fun _ _ => abs_nonneg _) hd
  · simp [notMem_support_iff.1 hd, normOne_nonneg]

/-- The triangle inequality for `normOne`. Source: §3, proof of Lemma 3 ("The triangle inequality
gives `‖f + k g‖₁ ≤ ‖f‖₁ + |k| ‖g‖₁`"). -/
theorem normOne_add_le (P Q : MvPolynomial σ ℤ) : normOne (P + Q) ≤ normOne P + normOne Q := by
  classical
  rw [normOne_eq_sum_of_support_subset support_add,
    normOne_eq_sum_of_support_subset (s := P.support ∪ Q.support) Finset.subset_union_left,
    normOne_eq_sum_of_support_subset (s := P.support ∪ Q.support) Finset.subset_union_right,
    ← Finset.sum_add_distrib]
  exact Finset.sum_le_sum fun d _ => by simpa using abs_add_le (P.coeff d : ℝ) (Q.coeff d)

/-- `normOne` is invariant under negation. -/
theorem normOne_neg (P : MvPolynomial σ ℤ) : normOne (-P) = normOne P := by
  simp [normOne, support_neg]

/-- The triangle inequality for `normOne` over a finite sum. -/
theorem normOne_sum_le {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, normOne (f i) :=
  Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le s f

/-- `normOne` is submultiplicative.
Source: §3, Lean note ("submultiplicativity for `‖·‖₁`"). -/
theorem normOne_mul_le [DecidableEq σ] (P Q : MvPolynomial σ ℤ) :
    normOne (P * Q) ≤ normOne P * normOne Q := by
  have hPQ : P * Q = ∑ a ∈ P.support, ∑ b ∈ Q.support,
      monomial (a + b) (P.coeff a * Q.coeff b) := by
    conv_lhs => rw [P.as_sum, Q.as_sum]
    rw [Finset.sum_mul_sum]
    simp [monomial_mul_monomial]
  rw [hPQ]
  refine (normOne_sum_le _ _).trans ?_
  rw [normOne, normOne, Finset.sum_mul_sum]
  exact Finset.sum_le_sum fun a _ => (normOne_sum_le _ _).trans_eq <|
    Finset.sum_congr rfl fun b _ => by simp [normOne_monomial, abs_mul]

/-- `normOne` is submultiplicative over a finite product. -/
theorem normOne_prod_le [DecidableEq σ] {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, normOne (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (normOne_monomial (0 : σ →₀ ℕ) 1).le
  | insert a s has ih =>
    rw [Finset.prod_insert has, Finset.prod_insert has]
    exact (normOne_mul_le _ _).trans (mul_le_mul_of_nonneg_left ih (normOne_nonneg _))

/-- A polynomial with coefficients bounded by `B` has `normOne` at most `#support * B`.
Source: §3, proof of Lemma 3 ("Pad the monomial expansion of `R` by zero terms and write
`R = ∑_{i=1}^N α_i`" — a polynomial with `N` terms of size `≤ B` has `‖R‖₁ ≤ N B`). -/
theorem normOne_le_card_mul (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) :
    normOne P ≤ P.support.card * B := by
  rw [normOne, ← nsmul_eq_mul]
  exact Finset.sum_le_card_nsmul _ _ B fun d _ => hB d

/-- The determinant of an `l × l` matrix whose entries have `normOne` at most `C` has `normOne`
at most `l! C^l`. Source: §3, proof of Lemma 3 ("`‖det(...)‖₁ ≤ ∑_σ ‖∏_ν ...‖₁ ≤ l! (B 2^S)^l`"). -/
theorem normOne_det_le [DecidableEq σ] {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ))
    {C : ℝ} (hC : 0 ≤ C) (hM : ∀ μ ν, normOne (M μ ν) ≤ C) :
    normOne M.det ≤ l.factorial * C ^ l := by
  rw [Matrix.det_apply']
  calc _ ≤ ∑ τ : Equiv.Perm (Fin l), normOne (_ * ∏ i, M (τ i) i) := normOne_sum_le _ _
    _ ≤ ∑ _τ : Equiv.Perm (Fin l), C ^ l := Finset.sum_le_sum fun τ _ => ?_
    _ = l.factorial * C ^ l := by simp [Fintype.card_perm]
  rw [show normOne (_ * ∏ i, M (τ i) i) = normOne (∏ i, M (τ i) i) by
    rcases Int.units_eq_one_or (Equiv.Perm.sign τ) with h | h <;> simp [h, normOne_neg]]
  exact (normOne_prod_le _ _).trans <|
    (Finset.prod_le_prod₀ (fun _ _ => normOne_nonneg _) fun i _ => hM _ _).trans_eq (by simp)

/-- Coefficient bound for a Hasse derivative of a polynomial with `deg_{X_j} P ≤ r_j`.
Source: §3, proof of Lemma 3 and §6, proof of Lemma 9 ("`abc(Δ_j W) ≤ 2^{r_1+⋯+r_m} B_1`":
each output coefficient of a fixed Hasse derivative receives at most one input coefficient,
multiplied by a binomial factor at most `2^{∑ r_j}`). -/
theorem abs_coeff_hasseDeriv_le [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) (e : σ →₀ ℕ) :
    |(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B := by
  rw [coeff_hasseDeriv]
  push_cast
  rw [abs_mul, Nat.abs_cast]
  by_cases he : e + d ∈ P.support
  · have hc : (hasseCoeff d (e + d) : ℝ) ≤ 2 ^ (∑ j, r j) := by
      exact_mod_cast hasseCoeff_le_two_pow fun j => (monomial_le_degreeOf j he).trans (hP j)
    exact mul_le_mul hc (hB _) (abs_nonneg _) (by positivity)
  · rw [notMem_support_iff.1 he]
    simpa using mul_nonneg (by positivity : (0 : ℝ) ≤ 2 ^ (∑ j, r j)) ((abs_nonneg _).trans (hB e))

/-- A Hasse derivative of a polynomial with `deg_{X_j} P ≤ r_j` increases `normOne` by at most a
factor `2^{∑ r_j}`. Source: §3, proof of Lemma 3 ("An individual Hasse derivative of such a term
is zero or a monomial whose coefficient has absolute value at most `B 2^S`"). -/
theorem normOne_hasseDeriv_le [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P := by
  classical
  have hsub : (hasseDeriv d P).support.image (· + d) ⊆ P.support :=
    Finset.image_subset_iff.2 fun e he =>
      mem_support_iff.2 (right_ne_zero_of_mul (by rwa [mem_support_iff, coeff_hasseDeriv] at he))
  calc normOne (hasseDeriv d P)
      ≤ ∑ e ∈ (hasseDeriv d P).support, 2 ^ (∑ j, r j) * |((P.coeff (e + d) : ℤ) : ℝ)| := by
        rw [normOne]
        refine Finset.sum_le_sum fun e he => ?_
        rw [coeff_hasseDeriv]
        push_cast
        rw [abs_mul, Nat.abs_cast]
        have he' : e + d ∈ P.support := hsub (Finset.mem_image_of_mem _ he)
        have hc : hasseCoeff d (e + d) ≤ 2 ^ (∑ j, r j) :=
          hasseCoeff_le_two_pow fun j => (monomial_le_degreeOf j he').trans (hP j)
        exact mul_le_mul_of_nonneg_right (by exact_mod_cast hc) (abs_nonneg _)
    _ = 2 ^ (∑ j, r j) * ∑ k ∈ (hasseDeriv d P).support.image (· + d),
          |((P.coeff k : ℤ) : ℝ)| := by
        rw [Finset.mul_sum, Finset.sum_image fun x _ y _ h => add_right_cancel h]
    _ ≤ 2 ^ (∑ j, r j) * normOne P :=
        mul_le_mul_of_nonneg_left (Finset.sum_le_sum_of_subset_of_nonneg hsub
          fun _ _ _ => abs_nonneg _) (by positivity)

/-- Diagonal substitution `P(x, …, x)`. Source: §6, proof of Lemma 9 ("When we replace
`x_1, …, x_m` by the same variable `x`"). -/
noncomputable def diag (P : MvPolynomial σ ℤ) : Polynomial ℤ := aeval (fun _ => Polynomial.X) P

/-- `diag P` collects each monomial `a_k X^k` into `a_k x^{|k|}`. -/
theorem diag_eq_sum (P : MvPolynomial σ ℤ) :
    diag P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k) := by
  conv_lhs => rw [P.as_sum]
  rw [diag, map_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [aeval_monomial, Finsupp.prod, Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply,
    Polynomial.algebraMap_eq, Polynomial.C_mul_X_pow_eq_monomial]

/-- The coefficients of `diag P` are bounded by `#support P` times a bound for those of `P`.
Source: §6, proof of Lemma 9 ("the absolute value of the coefficients of the resulting
polynomial is at most the number of terms of the polynomial ... multiplied by the coefficient
bound"). -/
theorem abs_coeff_diag_le (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B)
    (n : ℕ) : |(((diag P).coeff n : ℤ) : ℝ)| ≤ P.support.card * B := by
  rw [diag_eq_sum, Polynomial.finsetSum_coeff, Int.cast_sum, ← nsmul_eq_mul]
  refine (Finset.abs_sum_le_sum_abs _ _).trans (Finset.sum_le_card_nsmul _ _ B fun k _ => ?_)
  rw [Polynomial.coeff_monomial]
  split_ifs
  · exact hB k
  · simpa using (abs_nonneg _).trans (hB k)

/-- The degree of `diag P` is at most `∑ r_j` when `deg_{X_j} P ≤ r_j`.
Source: §6, proof of Lemma 9 ("`s ≤ ∑ r_j ≤ m r_1`"). -/
theorem natDegree_diag_le [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) : (diag P).natDegree ≤ ∑ j, r j := by
  rw [diag_eq_sum]
  refine Polynomial.natDegree_sum_le_of_forall_le _ _ fun k hk =>
    (Polynomial.natDegree_monomial_le _).trans ?_
  rw [Finsupp.degree_eq_sum]
  exact Finset.sum_le_sum fun j _ => (monomial_le_degreeOf j hk).trans (hP j)

/-- Evaluating `diag P` at `x` is evaluating `P` at the diagonal point `(x, …, x)`.
Source: §6, proof of Lemma 9 ("`Δ_j W^*(x_1, …, x_m)` are zero when `x_1 = ⋯ = x_m = α`"). -/
theorem eval_diag (P : MvPolynomial σ ℤ) (x : ℝ) :
    Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (diag P)) =
      eval (fun _ => x) (map (Int.castRingHom ℝ) P) := by
  induction P using MvPolynomial.induction_on <;> simp_all [diag]

/-- `diag` is additive. -/
theorem diag_sub (P Q : MvPolynomial σ ℤ) : diag (P - Q) = diag P - diag Q :=
  map_sub _ _ _

/-- A truncated geometric sum `∑_{s ≤ r} t^s` is at most `(1 + t)^r` for `0 ≤ t`.
Source: §6, proof of Lemma 9 ("for every `t ≥ 0` and integer `r ≥ 0`, `∑_{j=0}^r t^j ≤
(1+t)^r`, since each binomial coefficient is at least `1`"). -/
theorem geom_sum_le_one_add_pow {t : ℝ} (ht : 0 ≤ t) (r : ℕ) :
    ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r := by
  rw [add_comm (1 : ℝ) t, add_pow]
  refine Finset.sum_le_sum fun m hm => ?_
  rw [one_pow, mul_one]
  refine le_mul_of_one_le_right (pow_nonneg ht m) ?_
  exact_mod_cast Nat.choose_pos (Nat.lt_succ_iff.1 (Finset.mem_range.1 hm))

private lemma sum_box_prod_pow [Fintype σ] [DecidableEq σ] (r : σ → ℕ) (y : σ → ℝ) :
    ∑ k ∈ box r, ∏ j, y j ^ k j = ∏ j, ∑ s ∈ Finset.range (r j + 1), y j ^ s := by
  rw [box, Finset.sum_map, Finset.prod_univ_sum]
  rfl

/-- A value bound for an integer polynomial with bounded coefficients and degrees.
Source: §6, proof of Lemma 9 ("`|(Δ_i Q)(α, …, α)| ≤ abc(Δ_i Q) ∏_j ∑_{s ≤ r_j} |α|^s`",
combined with the geometric-sum bound). -/
theorem abs_eval_le [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j)
    {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (x : σ → ℝ) :
    |eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j := by
  classical
  have hB0 : 0 ≤ B := (abs_nonneg _).trans (hB 0)
  have hbox : P.support ⊆ box r := fun k hk =>
    mem_box.2 fun j => (monomial_le_degreeOf j hk).trans (hP j)
  have heval : eval x (map (Int.castRingHom ℝ) P) =
      ∑ k ∈ P.support, (P.coeff k : ℝ) * ∏ j, x j ^ k j := by
    conv_lhs => rw [P.as_sum]
    rw [map_sum, map_sum]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [map_monomial, eval_monomial, Finsupp.prod_fintype _ _ fun _ => pow_zero _]
    rfl
  rw [heval]
  calc |∑ k ∈ P.support, (P.coeff k : ℝ) * ∏ j, x j ^ k j|
      ≤ ∑ k ∈ P.support, B * ∏ j, |x j| ^ k j := by
        refine (Finset.abs_sum_le_sum_abs _ _).trans (Finset.sum_le_sum fun k _ => ?_)
        rw [abs_mul, Finset.abs_prod]
        simp only [abs_pow]
        exact mul_le_mul_of_nonneg_right (hB k) (by positivity)
    _ ≤ ∑ k ∈ box r, B * ∏ j, |x j| ^ k j :=
        Finset.sum_le_sum_of_subset_of_nonneg hbox fun _ _ _ => by positivity
    _ = B * ∏ j, ∑ s ∈ Finset.range (r j + 1), |x j| ^ s := by
        rw [← Finset.mul_sum, sum_box_prod_pow]
    _ ≤ B * ∏ j, (1 + |x j|) ^ r j :=
        mul_le_mul_of_nonneg_left (Finset.prod_le_prod₀ (fun _ _ => by positivity)
          fun j _ => geom_sum_le_one_add_pow (abs_nonneg _) _) hB0

/-- Degree bound for a determinant of Hasse derivatives of `P`.
Source: §2, end of the proof of Lemma 2 ("Since `F` is a determinant of an `l × l` matrix whose
entries are polynomials of degree at most `r_j` in `x_j`, `F` will be of degree at most `l r_j` in
each variable `x_j`"). -/
theorem degreeOf_det_hasseDeriv_le {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ)
    {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) (j : σ) :
    degreeOf j (Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P).det ≤ l * r j := by
  rw [Matrix.det_apply']
  refine (degreeOf_sum_le _ _ _).trans (Finset.sup_le fun τ _ => ?_)
  refine (degreeOf_mul_le _ _ _).trans ?_
  have hsign : degreeOf j ((Equiv.Perm.sign τ : ℤ) : MvPolynomial σ ℤ) = 0 := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign τ) with h | h <;> simp [h, degreeOf_neg]
  rw [hsign, zero_add]
  refine (degreeOf_prod_le _ _ _).trans ?_
  calc ∑ i, degreeOf j ((Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P) (τ i) i)
      ≤ ∑ _i : Fin l, r j :=
        Finset.sum_le_sum fun i _ => (degreeOf_hasseDeriv_le _ _ _).trans (hP j)
    _ = l * r j := by simp

/-- Lemma 3. Source: §3, Lemma `roth:lem3` ("all the coefficients of `F` have absolute value
bounded by `((r_1 + 1) ⋯ (r_p + 1))^l l! B^l 2^{(r_1 + ⋯ + r_p) l}`"), stated for a determinant
of Hasse derivatives of arbitrary multi-indices. -/
theorem abs_coeff_det_hasseDeriv_le [Fintype σ] [DecidableEq σ] {l : ℕ}
    (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB0 : 0 ≤ B) (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B)
    (d : σ →₀ ℕ) :
    |(((Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤
      (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l) := by
  have hN0 : 0 ≤ ∏ j, ((r j : ℝ) + 1) := by positivity
  have hsupp : (P.support.card : ℝ) ≤ ∏ j, ((r j : ℝ) + 1) := by
    exact_mod_cast card_le_card_box fun d hd j => (monomial_le_degreeOf j hd).trans (hP j)
  have hC0 : 0 ≤ 2 ^ (∑ j, r j) * ((∏ j, ((r j : ℝ) + 1)) * B) :=
    mul_nonneg (by positivity) (mul_nonneg hN0 hB0)
  have hentry : ∀ μ ν, normOne ((Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P) μ ν) ≤
      2 ^ (∑ j, r j) * ((∏ j, ((r j : ℝ) + 1)) * B) := fun μ ν =>
    (normOne_hasseDeriv_le _ P hP).trans (mul_le_mul_of_nonneg_left
      ((normOne_le_card_mul P hB).trans (mul_le_mul_of_nonneg_right hsupp hB0)) (by positivity))
  calc _ ≤ normOne (Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P).det :=
        abs_coeff_le_normOne _ _
    _ ≤ l.factorial * (2 ^ (∑ j, r j) * ((∏ j, ((r j : ℝ) + 1)) * B)) ^ l :=
        normOne_det_le _ hC0 hentry
    _ = _ := by rw [pow_mul]; ring

end Roth
