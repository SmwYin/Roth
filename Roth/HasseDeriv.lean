import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.MvPolynomial.Degrees
import Mathlib.Algebra.MvPolynomial.Equiv
import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Data.Finsupp.Weight
import Mathlib.Data.Nat.Choose.Bounds
import Mathlib.Tactic.Ring

/-!
# Multivariate Hasse derivatives

For a multi-index `d : σ →₀ ℕ` the *Hasse derivative* `Δ_d` is the `R`-linear map acting on
monomials by `Δ_d (X ^ k) = (∏ j, (k j).choose (d j)) • X ^ (k - d)`; it vanishes unless
`d ≤ k`, because the binomial coefficients vanish.  Over a `ℚ`-algebra it agrees with
`(∏ j, (d j)!)⁻¹ • ∏ j, ∂_j ^ (d j)`.

## Main definitions

* `MvPolynomial.hasseCoeff d k`: the binomial factor `∏ j, (k j).choose (d j)`.
* `MvPolynomial.hasseDeriv d`: the multivariate Hasse derivative `Δ_d`.

## Main results

* `MvPolynomial.coeff_hasseDeriv`: `[X^e] Δ_d P = hasseCoeff d (e + d) * [X^(e + d)] P`.
* `MvPolynomial.hasseDeriv_hasseDeriv`: the composition rule
  `Δ_d Δ_e = hasseCoeff d (d + e) • Δ_{d + e}`.
* `MvPolynomial.pderiv_hasseDeriv`: `∂_j Δ_d = (d j + 1) • Δ_{d + e_j}`.
* `MvPolynomial.factorial_smul_hasseDeriv_single`: `n! • Δ_{n e_j} = ∂_j ^ n`.
* `MvPolynomial.hasseDeriv_single_aeval_X`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`:
  compatibility with the univariate `Polynomial.hasseDeriv`.

## References

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §1 "Derivatives"
(`.mathlib-quality/references/clean.tex`).
-/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- The binomial factor `∏ j, (k j).choose (d j)` (a product over the support of `d`). -/
def hasseCoeff (d k : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose

/-- The multivariate Hasse derivative `Δ_d`: the `R`-linear map sending `monomial k a` to
`monomial (k - d) (hasseCoeff d k * a)` (see `hasseDeriv_monomial`). The coefficient
`hasseCoeff d k` vanishes unless `d ≤ k`, so the truncated subtraction `k - d` is harmless.

Source: §1, definition of `Δ_i` on monomials. -/
noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

/-- `Δ_d (a X^k) = hasseCoeff d k * a X^(k - d)`.

Source: §1, definition of `Δ_i` on monomials. -/
@[simp]
theorem hasseDeriv_monomial (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by
  simp [hasseDeriv]

/-- Expansion of `Δ_d P` as a sum over the support of `P`.

Source: §1, definition of `Δ_i` on monomials. -/
theorem hasseDeriv_apply (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by
  simp [hasseDeriv, sum_def]

/-- The binomial factor `hasseCoeff d k` vanishes exactly when `d ≰ k`.

Source: §1, "`0` otherwise" case of the definition of `Δ_i`. -/
theorem hasseCoeff_eq_zero_iff (d k : σ →₀ ℕ) : hasseCoeff d k = 0 ↔ ¬d ≤ k := by
  simp [hasseCoeff, Finsupp.prod, Finset.prod_eq_zero_iff, Nat.choose_eq_zero_iff, Finsupp.le_iff,
    not_forall]

/-- The coefficient identity `[X^e] Δ_d P = hasseCoeff d (e + d) * [X^(e + d)] P`. This is the
main computational interface to `hasseDeriv`; most identities below are proved by `ext` followed
by rewriting with it.

Source: §1, Lean implementation note. -/
theorem coeff_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    rw [hasseDeriv_monomial, coeff_monomial, coeff_monomial]
    by_cases hk : k = e + d
    · simp [hk]
    by_cases hdk : d ≤ k
    · simp [hk, tsub_eq_iff_eq_add_of_le hdk]
    · simp [hk, (hasseCoeff_eq_zero_iff d k).2 hdk]
  | add p q hp hq => simp [hp, hq, mul_add]

/-- Over a finite set of variables, `hasseCoeff d k` is the full product
`∏ j, (k j).choose (d j)`.

Source: §1, Lean implementation note. -/
theorem hasseCoeff_eq_prod [Fintype σ] (d k : σ →₀ ℕ) : hasseCoeff d k = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _

/-- `Δ_0` is the identity, pointwise version of `hasseDeriv_zero`.

Source: §1. -/
theorem hasseDeriv_zero_apply (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by
  ext e
  simp [coeff_hasseDeriv, hasseCoeff]

/-- `Δ_0` is the identity, since all binomial coefficients `(k j).choose 0` equal `1`.

Source: §1. -/
@[simp]
theorem hasseDeriv_zero : hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] _) :=
  LinearMap.ext hasseDeriv_zero_apply

/-- A Hasse derivative of nonzero order kills constants.

Source: §1. -/
theorem hasseDeriv_C {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by
  rw [C_apply, hasseDeriv_monomial, (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)]
  simp

/-- `hasseDeriv` commutes with change of coefficients along a ring hom; used to pass between
`ℤ`, `ℚ` and `ℝ`.

Source: §1, Lean implementation note. -/
theorem hasseDeriv_map {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) : hasseDeriv d (map f P) = map f (hasseDeriv d P) := by
  ext e
  simp [coeff_hasseDeriv, coeff_map]

/-- `hasseDeriv` commutes with renaming variables along an injective map, provided the
multi-index is transported along the same map.

Source: §4, Lean implementation note after Lemma 4-2. -/
theorem hasseDeriv_rename {τ : Type*} {f : σ → τ} (hf : Function.Injective f) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) :
    hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial k a =>
    simp [rename_monomial, hasseCoeff, Finsupp.prod_mapDomain_index_inj hf,
      Finsupp.mapDomain_apply_of_injective hf, ← Finsupp.mapDomain_tsub hf]
  | add p q hp hq => simp [hp, hq]

private lemma choose_mul_choose_eq (f d e : ℕ) :
    (f + d).choose d * (f + d + e).choose e = (d + e).choose d * (f + d + e).choose (d + e) := by
  simpa [mul_comm, ← Nat.choose_symm_add (a := d) (b := e)] using
    (Nat.choose_mul (n := f + d + e) (k := d + e) (s := e) (Nat.le_add_left e d)).symm

private lemma hasseCoeff_mul_hasseCoeff (f d e : σ →₀ ℕ) :
    hasseCoeff d (f + d) * hasseCoeff e (f + d + e) =
      hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e)) := by
  classical
  simp only [hasseCoeff]
  have hd : d.support ⊆ d.support ∪ e.support := Finset.subset_union_left
  rw [Finsupp.prod_of_support_subset _ hd _ fun _ _ ↦ Nat.choose_zero_right _,
    Finsupp.prod_of_support_subset _ Finset.subset_union_right _
      fun _ _ ↦ Nat.choose_zero_right _,
    Finsupp.prod_of_support_subset _ hd _ fun _ _ ↦ Nat.choose_zero_right _,
    Finsupp.prod_of_support_subset _ Finsupp.support_add _ fun _ _ ↦ Nat.choose_zero_right _,
    ← Finset.prod_mul_distrib, ← Finset.prod_mul_distrib]
  exact Finset.prod_congr rfl fun i _ ↦ by
    simpa [← add_assoc] using choose_mul_choose_eq (f i) (d i) (e i)

/-- The composition rule `Δ_d Δ_e P = hasseCoeff d (d + e) • Δ_{d + e} P`, where
`hasseCoeff d (d + e) = ∏ j, (d j + e j).choose (d j)`. See
`hasseDeriv_hasseDeriv_of_disjoint` for the case where the factor is `1`.

Source: §4, proof of Lemma `index-of-derivative`. -/
theorem hasseDeriv_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by
  ext f
  rw [coeff_smul, coeff_hasseDeriv, coeff_hasseDeriv, coeff_hasseDeriv, smul_eq_mul, ← mul_assoc,
    ← mul_assoc, ← Nat.cast_mul, ← Nat.cast_mul, hasseCoeff_mul_hasseCoeff, add_assoc]

/-- The composition rule `Δ_d Δ_e = Δ_{d + e}` when `d` and `e` have disjoint supports, so that
the binomial factor in `hasseDeriv_hasseDeriv` is `1`.

Source: §4, proof of Lemma `index-of-derivative`. -/
theorem hasseDeriv_hasseDeriv_of_disjoint {d e : σ →₀ ℕ} (h : Disjoint d.support e.support)
    (P : MvPolynomial σ R) : hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := by
  rw [hasseDeriv_hasseDeriv, show hasseCoeff d (d + e) = 1 from
    Finset.prod_eq_one fun i hi ↦ by
      simp [Finsupp.notMem_support_iff.1 (Finset.disjoint_left.1 h hi)], Nat.cast_one, one_smul]

private lemma hasseCoeff_mul_succ (j : σ) (d e : σ →₀ ℕ) :
    hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) =
      (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d) := by
  simpa [hasseCoeff, add_comm, add_left_comm, add_assoc, mul_comm] using
    hasseCoeff_mul_hasseCoeff e (Finsupp.single j 1) d

/-- A partial derivative of a Hasse derivative: `∂_j Δ_d = (d j + 1) • Δ_{d + e_j}`.

Source: §2, proof of Lemma 1. -/
theorem pderiv_hasseDeriv (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P := by
  ext e
  rw [coeff_pderiv, coeff_smul, coeff_hasseDeriv, coeff_hasseDeriv, smul_eq_mul,
    ← add_assoc e d, add_right_comm e d, mul_right_comm, ← Nat.cast_add_one, ← Nat.cast_mul,
    hasseCoeff_mul_succ, Nat.cast_mul, mul_assoc]

/-- Hasse derivatives do not increase the degree in any variable.

Source: §2, proof of Lemma 2. -/
theorem degreeOf_hasseDeriv_le (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P := by
  refine degreeOf_le_iff.2 fun m hm ↦ ?_
  rw [mem_support_iff, coeff_hasseDeriv] at hm
  exact (monomial_le_degreeOf j (mem_support_iff.2 (right_ne_zero_of_mul hm))).trans' (by simp)

/-- `Δ_d P = 0` as soon as `d j` exceeds the degree of `P` in some variable `j`.

Source: §6, proof of Lemma 9. -/
theorem hasseDeriv_eq_zero_of_degreeOf_lt {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : degreeOf j P < d j) : hasseDeriv d P = 0 := by
  ext e
  simp [coeff_hasseDeriv, notMem_support_iff.1
    (notMem_support_of_degreeOf_lt j (s := e + d) (h.trans_le (by simp)))]

private lemma hasseDeriv_monomial_mul {d a : σ →₀ ℕ} (ha : ∀ j ∈ d.support, a j = 0) (c : R)
    (g : MvPolynomial σ R) : hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g := by
  classical
  induction g using MvPolynomial.induction_on' with
  | monomial b c' =>
    have hc : hasseCoeff d (a + b) = hasseCoeff d b :=
      Finset.prod_congr rfl fun j hj => by simp [ha j hj]
    have hs : a + b - d = a + (b - d) := by
      ext j
      by_cases hj : j ∈ d.support
      · simp [ha j hj]
      · simp [Finsupp.notMem_support_iff.1 hj]
    simp only [monomial_mul_monomial, hasseDeriv_monomial, hc, hs]
    ring_nf
  | add p q hp hq => simp [mul_add, hp, hq]

/-- A factor `f` not involving any variable in the support of `d` passes through `Δ_d`:
`Δ_d (f * g) = f * Δ_d g`.

Source: §2, proof of Lemma 2. -/
theorem hasseDeriv_mul_of_degreeOf_eq_zero {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ j ∈ d.support, degreeOf j f = 0) : hasseDeriv d (f * g) = f * hasseDeriv d g := by
  have ha : ∀ a ∈ f.support, ∀ j ∈ d.support, a j = 0 := fun a ha j hj =>
    Nat.eq_zero_of_le_zero (hf j hj ▸ monomial_le_degreeOf j ha)
  rw [f.as_sum, Finset.sum_mul, Finset.sum_mul, map_sum]
  exact Finset.sum_congr rfl fun a haf => hasseDeriv_monomial_mul (ha a haf) _ _

/-- The operator `Δ_{n e_j}` restricted to polynomials in the single variable `X j` is the
univariate Hasse derivative `Polynomial.hasseDeriv n`.

Source: §1. -/
theorem hasseDeriv_single_aeval_X (j : σ) (n : ℕ) (f : Polynomial R) :
    hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) =
      Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv n f) := by
  induction f using Polynomial.induction_on' with
  | add p q hp hq => simp only [map_add, hp, hq]
  | monomial m a =>
    have hc : hasseCoeff (Finsupp.single j n) (Finsupp.single j m) = m.choose n := by
      simp [hasseCoeff, Finsupp.prod_single_index]
    simp only [Polynomial.hasseDeriv_monomial, Polynomial.aeval_monomial, algebraMap_eq,
      X_pow_eq_monomial, C_mul_monomial, mul_one, hasseDeriv_monomial, hc, Finsupp.single_tsub]

/-- For a single variable, `hasseDeriv` corresponds to `Polynomial.hasseDeriv` under
`MvPolynomial.uniqueAlgEquiv`.

Source: §1. -/
theorem uniqueAlgEquiv_hasseDeriv [Unique σ] (n : ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv (R := R) (Finsupp.single (default : σ) n) P) =
      Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P) := by
  obtain ⟨f, rfl⟩ := (uniqueAlgEquiv R σ).symm.surjective P
  have hX : ∀ g : Polynomial R, (uniqueAlgEquiv R σ).symm g = Polynomial.aeval (X default) g :=
    fun g => by rw [Polynomial.aeval_def]; rfl
  rw [AlgEquiv.apply_symm_apply, hX, hasseDeriv_single_aeval_X, ← hX, AlgEquiv.apply_symm_apply]

/-- The binomial factor of a Hasse derivative is at most `2 ^ (∑ j, r j)` on the box `k ≤ r`.

Source: §3, proof of Lemma 3. -/
theorem hasseCoeff_le_two_pow [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ} (hk : ∀ j, k j ≤ r j) :
    hasseCoeff d k ≤ 2 ^ (∑ j, r j) := by
  rw [hasseCoeff_eq_prod, ← Finset.prod_pow_eq_pow_sum]
  exact Finset.prod_le_prod fun j _ =>
    (Nat.choose_le_two_pow _ _).trans (Nat.pow_le_pow_right two_pos (hk j))

/-- `n! • Δ_{n e_j} = ∂_j ^ n`; as for `Polynomial.factorial_smul_hasseDeriv`, this holds over
any commutative semiring. Over a `ℚ`-algebra it identifies `Δ_{n e_j}` with `(1 / n!) ∂_j ^ n`.

Source: §1. -/
theorem factorial_smul_hasseDeriv_single (j : σ) (n : ℕ) (P : MvPolynomial σ R) :
    (n.factorial : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv (R := R) j))^[n] P := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply', ← ih, Derivation.map_smul, pderiv_hasseDeriv, smul_smul,
      Finsupp.single_eq_same, ← Finsupp.single_add, Nat.factorial_succ]
    push_cast
    ring_nf

end MvPolynomial
