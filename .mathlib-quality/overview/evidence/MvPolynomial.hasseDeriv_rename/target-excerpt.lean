/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

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

private lemma hasseCoeff_mul_hasseCoeff (f d e : σ →₀ ℕ) :
    hasseCoeff d (f + d) * hasseCoeff e (f + d + e) =
      hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e)) := by
