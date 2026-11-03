/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

import Mathlib.Algebra.MvPolynomial.NoZeroDivisors
import Mathlib.Algebra.MvPolynomial.Polynomial
import Mathlib.Algebra.Polynomial.Eval.Subring

import Roth.CoeffNorm
import Roth.GenWronskian
import Roth.Primitive

/-!
# Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2)

We single out one variable by working with polynomials in `Option τ` variables: `none` is the
distinguished variable (`x_p` in the source) and `some j`, `j : τ`, are the remaining ones.
Lemma 2 of the source produces, for a nonzero integer polynomial `R`, an integer `l` and Hasse
operators `Δ_{D μ}` in the variables `τ` of orders `≤ μ` such that the determinant
`det (Δ_{D μ} Δ^{(none)}_ν R)` factors as `U(x_τ) V(x_none)` with `U, V` nonzero integer
polynomials of controlled degrees.

## Main results

* `Roth.exists_separated_representation`: over a field, `P = ∑ ν, φ_ν(x_none) ψ_ν(x_τ)` with
  both families linearly independent.
* `Roth.det_hasseDeriv_separated`: the determinant of Hasse derivatives of such a sum is
  `genWronskian D ψ · wronskian φ`.
* `Roth.exists_int_factors`: a rational factorisation `U' V'` of an integer polynomial can be
  rescaled to an integral one.
* `Roth.exists_det_eq_mul`: Lemma 2 of the source.

## References

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §2, Lemma 2 (`roth:lem2`)
(`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open MvPolynomial

variable {τ : Type*}

section General

variable {R : Type*} [CommSemiring R]

/-- The coefficient of `x_τ^a x_none^b` in `U(x_τ) V(x_none)` is `U_a V_b`.
Source: §2, proof of Lemma 2 ("the variables of the two factors are disjoint": the
coefficients of `U(x_τ) V(x_none)` are the products of coefficients). -/
theorem coeff_rename_mul_toMvPolynomial (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ)
    (b : ℕ) : (rename some U * V.toMvPolynomial none).coeff (a.optionElim b) =
      U.coeff a * V.coeff b := by
  have h : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom := by
    ext i
    simp
  rw [← optionEquivLeft_coeff_coeff, map_mul,
    (show optionEquivLeft R τ (rename some U) = Polynomial.C U from AlgHom.congr_fun h U),
    Polynomial.toMvPolynomial, ← Polynomial.aeval_algHom_apply, optionEquivLeft_X_none,
    Polynomial.aeval_X_left_eq_map, Polynomial.coeff_C_mul, Polynomial.coeff_map, algebraMap_eq,
    mul_comm U, coeff_C_mul, mul_comm]

/-- A univariate polynomial in the variable `X i`, as the renaming of a one-variable
`MvPolynomial`; the applied form of `Polynomial.toMvPolynomial_eq_rename_comp`.
Source: §4, Lemma 4-2 ("the index of the embedded `Q` is its one-variable index"). -/
theorem toMvPolynomial_eq_rename {σ : Type*} (i : σ) (f : Polynomial R) :
    f.toMvPolynomial i = rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f) :=
  AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f

/-- Change of coefficients along an injective ring hom does not change the degree in any
variable. -/
theorem degreeOf_map_of_injective {σ S : Type*} [CommSemiring S] {f : R →+* S}
    (hf : Function.Injective f) (i : σ) (p : MvPolynomial σ R) :
    degreeOf i (map f p) = degreeOf i p := by
  rw [degreeOf_eq_sup, support_map_of_injective _ hf, ← degreeOf_eq_sup]

/-- A variable outside the range of a renaming has degree `0` in the renamed polynomial. -/
theorem degreeOf_rename_of_notMem_range {σ : Type*} {f : σ → τ} {i : τ} (hi : i ∉ Set.range f)
    (p : MvPolynomial σ R) : degreeOf i (rename f p) = 0 := by
  classical
  rw [degreeOf_def, Multiset.count_eq_zero]
  exact fun h ↦ hi <| (Multiset.mem_map.1 (degrees_rename f p h)).imp fun _ ha ↦ ha.2

private lemma optionElim_eq_mapDomain_add_single_aux (d : τ →₀ ℕ) (ν : ℕ) :
    d.optionElim ν = d.mapDomain some + Finsupp.single none ν := by
  ext (_ | j) <;> simp [Finsupp.mapDomain_of_notMem_range,
    Finsupp.mapDomain_apply_of_injective (Option.some_injective τ)]

/-- A Hasse derivative `Δ_{d + ν e_none}` of a separated product `U(x_τ) V(x_none)` acts
factorwise. Source: §2, proof of Lemma 2 ("`Δ_μ (1/ν!) ∂^ν_{x_p} (φ_ρ(x_p) ψ_ρ(x_1, …, x_{p-1}))
= (Δ_μ ψ_ρ) ((1/ν!) ∂^ν φ_ρ)`", the entries of `A Bᵀ`). -/
theorem hasseDeriv_rename_mul_toMvPolynomial (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R)
    (V : Polynomial R) : hasseDeriv (d.optionElim ν) (rename some U * V.toMvPolynomial none) =
      rename some (hasseDeriv d U) * (Polynomial.hasseDeriv ν V).toMvPolynomial none := by
  classical
  have hnone : ∀ {o : Option τ}, o ∈ (d.mapDomain some).support → o ≠ none := by
    simp
  have hdisj : Disjoint (d.mapDomain some).support (Finsupp.single none ν).support :=
    Finset.disjoint_left.2 fun _ ho ho' ↦
      hnone ho (Finset.mem_singleton.1 (Finsupp.support_single_subset ho'))
  -- split `Δ_{d + ν e_none} = Δ_d ∘ Δ_{ν e_none}`; each factor passes through the operator in
  -- the variables it does not involve
  rw [optionElim_eq_mapDomain_add_single_aux, ← hasseDeriv_hasseDeriv_of_disjoint hdisj,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      rw [Finset.mem_singleton.1 (Finsupp.support_single_subset hj)]
      exact degreeOf_rename_of_notMem_range (by simp) U,
    hasseDeriv_single_toMvPolynomial, mul_comm,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      rw [toMvPolynomial_eq_rename]
      exact degreeOf_rename_of_notMem_range (by rintro ⟨_, rfl⟩; exact hnone hj rfl) _,
    hasseDeriv_rename (Option.some_injective τ), mul_comm]

/-- The degree of a univariate polynomial viewed as a one-variable `MvPolynomial`. -/
theorem degreeOf_uniqueAlgEquiv_symm {σ : Type*} [Unique σ] (f : Polynomial R) :
    degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree := by
  apply le_antisymm
  · rw [degreeOf_le_iff]
    intro e he
    rw [mem_support_iff, MvPolynomial.coeff_uniqueAlgEquiv_symm] at he
    exact Polynomial.le_natDegree_of_ne_zero he
  · refine Polynomial.natDegree_le_iff_coeff_eq_zero.2 fun n hn ↦ ?_
    simpa only [mem_support_iff, MvPolynomial.coeff_uniqueAlgEquiv_symm,
      Finsupp.single_eq_same, not_not] using
      (notMem_support_of_degreeOf_lt (p := (uniqueAlgEquiv R σ).symm f) (i := default)
        (s := Finsupp.single default n) (by simpa only [Finsupp.single_eq_same] using hn))

end General

section Domain

variable {R : Type*} [CommSemiring R] [NoZeroDivisors R]

/-- For `V ≠ 0`, the degree of `U(x_τ) V(x_none)` in `x_j` is the degree of `U` in `x_j`.
Source: §2, end of the proof of Lemma 2 ("since the variables are disjoint and both factors are
nonzero, the individual degrees of `U, V` equal the corresponding degrees of `F`"). -/
theorem degreeOf_some_rename_mul_toMvPolynomial (U : MvPolynomial τ R) {V : Polynomial R}
    (hV : V ≠ 0) (j : τ) :
    degreeOf (some j) (rename some U * V.toMvPolynomial none) = degreeOf j U := by
  by_cases hU : U = 0
  · simp [hU]
  rw [degreeOf_mul_eq ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      ((map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective none)).2 hV),
    degreeOf_rename_of_injective (Option.some_injective τ), toMvPolynomial_eq_rename, add_eq_left]
  exact degreeOf_rename_of_notMem_range (by simp) _

/-- For `U ≠ 0`, the degree of `U(x_τ) V(x_none)` in `x_none` is the degree of `V`.
Source: §2, end of the proof of Lemma 2. -/
theorem degreeOf_none_rename_mul_toMvPolynomial {U : MvPolynomial τ R} (hU : U ≠ 0)
    (V : Polynomial R) : degreeOf none (rename some U * V.toMvPolynomial none) = V.natDegree := by
  by_cases hV : V = 0
  · simp [hV]
  rw [degreeOf_mul_eq ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      ((map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective none)).2 hV),
    (show degreeOf none (rename some U) = 0 from degreeOf_rename_of_notMem_range (by simp) U),
    zero_add, toMvPolynomial_eq_rename]
  exact (degreeOf_rename_of_injective (f := fun _ : Unit ↦ (none : Option τ))
    (Function.injective_of_subsingleton _) ()).trans (degreeOf_uniqueAlgEquiv_symm V)

end Domain

section Field

variable {K : Type*} [Field K]

private lemma linearIndependent_coordinate_polynomials_aux {R M : Type*} [CommRing R]
    [AddCommMonoid M] [Module R M] {n l : ℕ} (v : Fin (n + 1) → M)
    (b : Module.Basis (Fin l) R (Submodule.span R (Set.range v))) :
    LinearIndependent R (fun ρ ↦ ∑ ν : Fin (n + 1),
      Polynomial.C (b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ)) := by
  let a := fun ν ρ ↦ b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ
  rw [Fintype.linearIndependent_iff]
  intro g hg ρ₀
  -- compare the coefficients of `X ^ ν` in the vanishing linear combination
  have hcoeff : ∀ ν : Fin (n + 1), ∑ ρ, g ρ * a ν ρ = 0 := fun ν ↦ by
    simpa [Fin.val_inj] using congrArg (fun p : Polynomial R ↦ p.coeff ν) hg
  -- the functional `∑ ρ, g ρ • b.coord ρ` vanishes on the spanning set, hence on the span
  let f : Submodule.span R (Set.range v) →ₗ[R] R := ∑ ρ, g ρ • b.coord ρ
  have hf : f = 0 := LinearMap.ext_on Submodule.span_span_coe_preimage fun x hx ↦ by
    obtain ⟨ν, hν⟩ := hx
    obtain rfl : x = ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ := Subtype.ext hν.symm
    simpa only [f, a, LinearMap.sum_apply, LinearMap.smul_apply, smul_eq_mul,
      Module.Basis.coord_apply, LinearMap.zero_apply] using hcoeff ν
  -- evaluating it at the basis vector `b ρ₀` gives `g ρ₀ = 0`
  simpa only [f, LinearMap.sum_apply, LinearMap.smul_apply, Module.Basis.coord_apply,
    Module.Basis.repr_self, Finsupp.single_apply, smul_eq_mul, mul_ite, mul_one, mul_zero,
    Finset.sum_ite_eq, Finset.mem_univ, ite_true, LinearMap.zero_apply] using
    LinearMap.congr_fun hf (b ρ₀)

private lemma eq_sum_toMvPolynomial_basis_aux {R : Type*} [CommSemiring R]
    {P : MvPolynomial (Option τ) R} {n l : ℕ} (hP : P = ∑ ν : Fin (n + 1),
      X none ^ (ν : ℕ) * rename some ((optionEquivLeft R τ P).coeff ν))
    (b : Module.Basis (Fin l) R
      (Submodule.span R (Set.range fun ν : Fin (n + 1) ↦ (optionEquivLeft R τ P).coeff ν))) :
    P = ∑ ρ, (∑ ν : Fin (n + 1),
        Polynomial.C (b.repr ⟨(optionEquivLeft R τ P).coeff ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) *
          Polynomial.X ^ (ν : ℕ)).toMvPolynomial none * rename some (b ρ : MvPolynomial τ R) := by
  -- name the coordinates `a ν ρ` of the coefficient polynomials in the basis `b`
  obtain ⟨a, ha⟩ : ∃ a : Fin (n + 1) → Fin l → R, ∀ (ν : Fin (n + 1)) (ρ : Fin l),
      b.repr ⟨(optionEquivLeft R τ P).coeff ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ = a ν ρ :=
    ⟨_, fun _ _ ↦ rfl⟩
  -- expand each coefficient polynomial in the basis `b`
  have hexp : ∀ ν : Fin (n + 1),
      (optionEquivLeft R τ P).coeff ν = ∑ ρ, a ν ρ • (b ρ : MvPolynomial τ R) := fun ν ↦ by
    have h := congrArg Subtype.val
      (b.sum_repr ⟨(optionEquivLeft R τ P).coeff ν, Submodule.subset_span ⟨ν, rfl⟩⟩)
    simpa only [Submodule.coe_sum, Submodule.coe_smul, ha] using h.symm
  simp_rw [ha]
  conv_lhs => rw [hP]
  simp_rw [hexp, map_sum, Finset.mul_sum]
  -- swap the two sums
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun ρ _ ↦ ?_
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun ν _ ↦ ?_
  rw [map_smul, smul_eq_C_mul, map_mul, Polynomial.toMvPolynomial_C, map_pow,
    Polynomial.toMvPolynomial_X]
  ring

private lemma exists_basis_span_coeff_aux {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ}
    (hP' : P = ∑ ν : Fin (n + 1),
      X none ^ (ν : ℕ) * rename some ((optionEquivLeft K τ P).coeff ν)) :
    ∃ l, ∃ _ : Module.Basis (Fin l) K
      (Submodule.span K (Set.range fun ν : Fin (n + 1) ↦ (optionEquivLeft K τ P).coeff ν)),
      1 ≤ l ∧ l ≤ n + 1 := by
  let v : Fin (n + 1) → MvPolynomial τ K := fun ν ↦ (optionEquivLeft K τ P).coeff ν
  let V := Submodule.span K (Set.range v)
  have : FiniteDimensional K V := FiniteDimensional.span_of_finite K (Set.finite_range v)
  have hl1 : 1 ≤ Module.finrank K V := by
    obtain ⟨ν, hν⟩ : ∃ ν, v ν ≠ 0 := by
      by_contra! h
      apply hP
      change P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (v ν) at hP'
      rw [hP']
      simp [h]
    exact Module.finrank_pos_iff_exists_ne_zero.2
      ⟨⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩, fun h ↦ hν (congrArg Subtype.val h)⟩
  exact ⟨Module.finrank K V, Module.finBasis K V, hl1,
    (finrank_range_le_card (R := K) v).trans_eq (Fintype.card_fin _)⟩

/-- Over a field, a nonzero `P` of degree at most `n` in `x_none` can be written as
`∑_{ν < l} φ_ν(x_none) ψ_ν(x_τ)` with `1 ≤ l ≤ n + 1` and both families linearly independent.
Source: §2, proof of Lemma 2 and its Lean implementation note ("Construct the separated
decomposition over `ℚ` from a basis of the span of the coefficient polynomials of `R` in
`x_p`"). -/
theorem exists_separated_representation {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ}
    (hn : degreeOf none P ≤ n) :
    ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
      LinearIndependent K φ ∧ LinearIndependent K ψ ∧
      P = ∑ ν, (φ ν).toMvPolynomial none * rename some (ψ ν) := by
  -- expand `P` in powers of `x_none`, with coefficients `v ν` in the remaining variables
  let v : Fin (n + 1) → MvPolynomial τ K := fun ν ↦ (optionEquivLeft K τ P).coeff ν
  have hP' : P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (v ν) := by
    rw [Fin.sum_univ_eq_sum_range
      (fun ν ↦ X none ^ ν * rename some ((optionEquivLeft K τ P).coeff ν))]
    conv_lhs => rw [← (optionEquivLeft K τ).symm_apply_apply P, optionEquivLeft_symm_apply]
    exact (Polynomial.eval₂_eq_sum_range' _ ((natDegree_optionEquivLeft K P).trans_lt
      (Nat.lt_succ_of_le hn)) _).trans (Finset.sum_congr rfl fun _ _ ↦ mul_comm _ _)
  -- a basis `b` of the span of the `v ν`: the `ψ_ρ` are the basis vectors and the `φ_ρ` collect
  -- the `ρ`-th coordinates of the `v ν`
  obtain ⟨l, b, hl1, hl2⟩ := exists_basis_span_coeff_aux hP hP'
  exact ⟨l, hl1, hl2, fun ρ ↦ ∑ ν : Fin (n + 1),
      Polynomial.C (b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ),
    fun ρ ↦ (b ρ : MvPolynomial τ K), linearIndependent_coordinate_polynomials_aux v b,
    b.linearIndependent.map' (Submodule.span K (Set.range v)).subtype
      (Submodule.ker_subtype _), eq_sum_toMvPolynomial_basis_aux hP' b⟩

end Field

section CommRing

variable {R : Type*} [CommRing R]

/-- The determinant of Hasse derivatives of a separated sum `∑ φ_ρ(x_none) ψ_ρ(x_τ)` is the
product of the generalised Wronskian of `ψ` and the Wronskian of `φ`.
Source: §2, proof of Lemma 2 ("Explicitly, we obtain `GW = det (...)`"). -/
theorem det_hasseDeriv_separated {l : ℕ} (D : Fin l → (τ →₀ ℕ)) (φ : Fin l → Polynomial R)
    (ψ : Fin l → MvPolynomial τ R) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).optionElim (ν : ℕ))
        (∑ ρ, (φ ρ).toMvPolynomial none * rename some (ψ ρ))).det =
      rename some (genWronskian D ψ) * (wronskian φ).toMvPolynomial none := by
  -- the matrix of Hasse derivatives is `A * Bᵀ` with `A = (Δ_{D μ} ψ_ρ)` and `B = (Δ_ν φ_ρ)`, so
  -- its determinant is `det A * det B` by multiplicativity and invariance under transpose
  rw [rename_genWronskian (Option.some_injective τ), genWronskian, wronskian, AlgHom.map_det,
    ← Matrix.det_transpose
      ((Polynomial.toMvPolynomial none).mapMatrix
        (Matrix.of fun μ ν : Fin l ↦ Polynomial.hasseDeriv μ (φ ν))),
    ← Matrix.det_mul]
  congr 1
  ext μ ν
  simp [Matrix.mul_apply, hasseDeriv_rename_mul_toMvPolynomial,
    ← hasseDeriv_rename (Option.some_injective τ), mul_comm]

end CommRing

private lemma rescale_separated_factor_aux {K : Type*} [Field K] {U' U : MvPolynomial τ K}
    {V' : Polynomial K} {F : MvPolynomial (Option τ) K} {g : K} (hg : g ≠ 0) (hUmap : U = g • U')
    (hF : F = rename some U' * V'.toMvPolynomial none) :
    F = rename some U * (Polynomial.C g⁻¹ * V').toMvPolynomial none := by
  rw [hF, hUmap, map_mul, Polynomial.toMvPolynomial_C, smul_eq_C_mul, map_mul, rename_C,
    mul_mul_mul_comm, ← C_mul, mul_inv_cancel₀ hg, C_1, one_mul]

private lemma exists_int_polynomial_of_primitive_factor_aux {U : MvPolynomial τ ℤ}
    {V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ} (hgcd : U.support.gcd U.coeff = 1)
    (hF : map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) *
      V'.toMvPolynomial none) :
    ∃ V : Polynomial ℤ, V.map (Int.castRingHom ℚ) = V' := by
  apply (Polynomial.mem_map_range (Int.castRingHom ℚ)).2
  intro b
  obtain ⟨z, hz⟩ := exists_int_eq_of_gcd_eq_one hgcd fun a _ ↦
    ⟨F.coeff (a.optionElim b), by
      have h := congrArg (fun P ↦ P.coeff (a.optionElim b)) hF
      simp only [coeff_rename_mul_toMvPolynomial, coeff_map] at h
      simpa using h.symm⟩
  exact ⟨z, hz.symm⟩

/-- If an integer polynomial `F` factors over `ℚ` as `U'(x_τ) V'(x_none)` with nonzero factors,
then it factors over `ℤ` as `U(x_τ) V(x_none)` with nonzero factors.
Source: §2, proof of Lemma 2 ("Thus `U, V` are integral and nonzero, as required"). -/
theorem exists_int_factors {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) ℤ} (hF : map (Int.castRingHom ℚ) F =
      rename some U' * V'.toMvPolynomial none) :
    ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * V.toMvPolynomial none := by
  obtain ⟨g, U, hg, hUmap, hgcd⟩ := exists_primitive_smul_eq hU
  have hF' := rescale_separated_factor_aux hg hUmap hF
  obtain ⟨V, hVmap⟩ := exists_int_polynomial_of_primitive_factor_aux hgcd hF'
  refine ⟨U, V, ?_, ?_, ?_⟩
  · exact fun h ↦ smul_ne_zero hg hU (by simpa [h] using hUmap.symm)
  · exact fun h ↦ mul_ne_zero (Polynomial.C_ne_zero.2 (inv_ne_zero hg)) hV
      (by simpa [h] using hVmap.symm)
  · apply MvPolynomial.map_injective (Int.castRingHom ℚ) Int.cast_injective
    rw [hF', map_mul (map (Int.castRingHom ℚ)), map_rename]
    simp only [Polynomial.toMvPolynomial]
    rw [Polynomial.map_aeval_eq_aeval_map (φ := Int.castRingHom ℚ) (Subsingleton.elim _ _), map_X,
      hVmap]

private lemma exists_rat_factors_det_hasseDeriv_aux {P : MvPolynomial (Option τ) ℤ}
    (hP : P ≠ 0) {n : ℕ} (hn : degreeOf none P ≤ n) : ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧
      ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℚ) (V : Polynomial ℚ),
        U ≠ 0 ∧ V ≠ 0 ∧ map (Int.castRingHom ℚ) (Matrix.of fun μ ν : Fin l ↦
          hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *
          V.toMvPolynomial none := by
  classical
  set PQ := map (Int.castRingHom ℚ) P
  have hdeg : degreeOf none PQ ≤ n :=
    (degreeOf_map_of_injective Int.cast_injective none P).trans_le hn
  obtain ⟨l, hl1, hl2, φ, ψ, hφ, hψ, hPQ⟩ :=
    exists_separated_representation (fun h ↦
      hP (MvPolynomial.map_injective _ Int.cast_injective (h.trans (map_zero _).symm))) hdeg
  obtain ⟨D, hD, hG⟩ := exists_genWronskian_ne_zero hψ
  set F := (Matrix.of fun μ ν : Fin l ↦
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det with hFdef
  have hFmap : map (Int.castRingHom ℚ) F = rename some (genWronskian D ψ) *
      (wronskian φ).toMvPolynomial none := by
    rw [hFdef, RingHom.map_det, ← det_hasseDeriv_separated D φ ψ, ← hPQ]
    congr 1
    refine Matrix.ext fun μ ν ↦ ?_
    rw [RingHom.mapMatrix_apply, Matrix.map_apply, Matrix.of_apply, Matrix.of_apply,
      hasseDeriv_map, optionElim_eq_mapDomain_add_single_aux]
  exact ⟨l, hl1, hl2, D, hD, _, _, hG, wronskian_ne_zero_of_linearIndependent hφ, hFmap⟩

/-- Lemma 2. Source: §2, Lemma `roth:lem2` ("there is an integer `l` satisfying `1 ≤ l ≤ r_p + 1`
and there are differential operators `Δ_0, …, Δ_{l-1}` on the variables `x_1, …, x_{p-1}` of
orders at most `0, …, l-1` such that ... `F = U(x_1, …, x_{p-1}) V(x_p)` where `U, V` are nonzero,
have integral coefficients, `U` is of degree at most `l r_j` in `x_j` ... and `V` is of degree
at most `l r_p`"). -/
theorem exists_det_eq_mul {P : MvPolynomial (Option τ) ℤ} (hP : P ≠ 0) {r : Option τ → ℕ}
    (hr : ∀ j, degreeOf j P ≤ r j) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ),
      (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
        (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧
        (Matrix.of fun μ ν : Fin l ↦
            hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *
          V.toMvPolynomial none := by
  obtain ⟨l, hl1, hl2, D, hD, U', V', hU', hV', hFmap⟩ :=
    exists_rat_factors_det_hasseDeriv_aux hP (hr none)
  obtain ⟨U, V, hU, hV, hFUV⟩ := exists_int_factors hU' hV' hFmap
  have key := degreeOf_det_hasseDeriv_le
    (fun μ ν : Fin l ↦ (D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P hr
  refine ⟨l, hl1, hl2, D, hD, U, V, hU, hV, fun j ↦ ?_, ?_, hFUV⟩
  · rw [← degreeOf_some_rename_mul_toMvPolynomial U hV j, ← hFUV]
    exact key (some j)
  · rw [← degreeOf_none_rename_mul_toMvPolynomial hU V, ← hFUV]
    exact key none

end Roth
