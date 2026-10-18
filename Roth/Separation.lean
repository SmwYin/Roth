import Mathlib.Algebra.GCDMonoid.Finset
import Mathlib.Algebra.MvPolynomial.NoZeroDivisors
import Mathlib.Algebra.MvPolynomial.Polynomial
import Mathlib.Tactic.LinearCombination

import Roth.CoeffNorm
import Roth.GenWronskian

/-!
# Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2)

We single out one variable by working with polynomials in `Option τ` variables: `none` is the
distinguished variable (`x_p` in the source) and `some j`, `j : τ`, are the remaining ones.
Lemma 2 of the source produces, for a nonzero integer polynomial `R`, an integer `l` and Hasse
operators `Δ_{D μ}` in the variables `τ` of orders `≤ μ` such that the determinant
`det (Δ_{D μ} Δ^{(none)}_ν R)` factors as `U(x_τ) V(x_none)` with `U, V` nonzero integer
polynomials of controlled degrees.

## Main definitions

* `Roth.coeffNone P ν`: the coefficient of `X none ^ ν` in `P`, a polynomial in the variables `τ`.

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

variable {τ : Type*} [Fintype τ] [DecidableEq τ]

section General

variable {R : Type*} [CommSemiring R]

omit [Fintype τ] [DecidableEq τ] in
/-- Every multi-index on `Option τ` is `(its restriction to τ) + (d none) e_none`. -/
theorem eq_mapDomain_some_add_single (d : Option τ →₀ ℕ) :
    d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none) := by
  ext o
  cases o <;> simp [Finsupp.mapDomain_of_notMem_range,
    Finsupp.mapDomain_apply_of_injective (Option.some_injective τ), Finsupp.some_apply]

omit [Fintype τ] [DecidableEq τ] in
private lemma coeff_X_none_pow_mul_rename (ν : ℕ) (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ) :
    (X none ^ ν * rename some Q).coeff e = if e none = ν then Q.coeff (Finsupp.some e) else 0 := by
  classical
  have h : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom := by
    ext i
    simp
  have hQ : optionEquivLeft R τ (rename some Q) = Polynomial.C Q := AlgHom.congr_fun h Q
  rw [← optionEquivLeft_coeff_some_coeff_none R τ e, map_mul, map_pow,
    optionEquivLeft_X_none, hQ, Polynomial.X_pow_mul_C,
    Polynomial.C_mul_X_pow_eq_monomial, Polynomial.coeff_monomial]
  by_cases he : e none = ν
  · simp [he]
  · simp [he, Ne.symm he]

/-- The coefficient of `X none ^ ν` in `P`, a polynomial in the variables `τ`.
Source: §2, proof of Lemma 2 ("collecting the terms in terms of the powers of `x_p`"). -/
noncomputable def coeffNone (P : MvPolynomial (Option τ) R) (ν : ℕ) : MvPolynomial τ R :=
  (optionEquivLeft R τ P).coeff ν

omit [Fintype τ] [DecidableEq τ] in
/-- The coefficient of `x_τ^d` in `coeffNone P ν` is the coefficient of `x_τ^d x_none^ν` in `P`. -/
theorem coeff_coeffNone (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν) := by
  rw [coeffNone, optionEquivLeft_coeff_coeff]
  congr 1
  ext o
  cases o <;> simp [Finsupp.mapDomain_of_notMem_range,
    Finsupp.mapDomain_apply_of_injective (Option.some_injective τ)]

omit [Fintype τ] [DecidableEq τ] in
/-- Expansion of `P` in powers of the distinguished variable: if `P` has degree at most `n` in
`x_none`, then `P = ∑_{ν ≤ n} x_none^ν · coeffNone P ν`.
Source: §2, proof of Lemma 2 ("we can let `l - 1 = r_p` and `φ_ν(x_p) = x_p^ν` by collecting
the terms in terms of the powers of `x_p`"). -/
theorem eq_sum_X_none_pow_mul_coeffNone (P : MvPolynomial (Option τ) R) {n : ℕ}
    (hn : degreeOf none P ≤ n) :
    P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (coeffNone P ν) := by
  classical
  ext e
  rw [coeff_sum]
  simp_rw [coeff_X_none_pow_mul_rename]
  rw [Finset.sum_ite_eq]
  split_ifs with he
  · rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]
  · exact notMem_support_iff.1 fun h ↦
      he (Finset.mem_range.2 (Nat.lt_succ_of_le ((monomial_le_degreeOf none h).trans hn)))

omit [Fintype τ] [DecidableEq τ] in
/-- Taking the coefficient of a power of `x_none` does not increase the degree in `x_j`.
Source: §2, proof of Lemma 2 ("the `ψ_ν`'s of degree at most `r_j` in `x_j`"). -/
theorem degreeOf_coeffNone_le (P : MvPolynomial (Option τ) R) (ν : ℕ) (j : τ) :
    degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P := by
  refine degreeOf_le_iff.2 fun d hd ↦ ?_
  simpa using monomial_le_degreeOf (some j) ((mem_support_coeff_optionEquivLeft R).1 hd)

omit [Fintype τ] [DecidableEq τ] in
/-- The coefficient of `x_τ^a x_none^b` in `U(x_τ) V(x_none)` is `U_a V_b`.
Source: §2, proof of Lemma 2 ("the variables of the two factors are disjoint": the
coefficients of `U(x_τ) V(x_none)` are the products of coefficients). -/
theorem coeff_rename_mul_aeval (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ) :
    (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V).coeff
        (a.mapDomain some + Finsupp.single none b) = U.coeff a * V.coeff b := by
  have h : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom := by
    ext i
    simp
  rw [← coeff_coeffNone, coeffNone, map_mul,
    (show optionEquivLeft R τ (rename some U) = Polynomial.C U from AlgHom.congr_fun h U),
    ← Polynomial.aeval_algHom_apply, optionEquivLeft_X_none, Polynomial.aeval_X_left_eq_map,
    Polynomial.coeff_C_mul, Polynomial.coeff_map, algebraMap_eq, mul_comm U, coeff_C_mul, mul_comm]

/-- A univariate polynomial in the variable `X i`, as the renaming of a one-variable
`MvPolynomial`. Source: §4, Lemma 4-2 ("the index of the embedded `Q` is its one-variable
index"). -/
theorem aeval_X_eq_rename {σ : Type*} (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit => i) ((uniqueAlgEquiv R Unit).symm f) :=
  AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f

omit [Fintype τ] [DecidableEq τ] in
/-- A Hasse derivative `Δ_{d + ν e_none}` of a separated product `U(x_τ) V(x_none)` acts
factorwise. Source: §2, proof of Lemma 2 ("`Δ_μ (1/ν!) ∂^ν_{x_p} (φ_ρ(x_p) ψ_ρ(x_1, …, x_{p-1}))
= (Δ_μ ψ_ρ) ((1/ν!) ∂^ν φ_ρ)`", the entries of `A Bᵀ`). -/
theorem hasseDeriv_rename_mul_aeval (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R) (V : Polynomial R) :
    hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval
      (X none : MvPolynomial (Option τ) R) V) = rename some (hasseDeriv d U) * Polynomial.aeval
      (X none : MvPolynomial (Option τ) R) (Polynomial.hasseDeriv ν V) := by
  classical
  have hnone : ∀ {o : Option τ}, o ∈ (d.mapDomain some).support → o ≠ none := by
    simp
  have hdisj : Disjoint (d.mapDomain some).support (Finsupp.single none ν).support :=
    Finset.disjoint_left.2 fun _ ho ho' ↦
      hnone ho (Finset.mem_singleton.1 (Finsupp.support_single_subset ho'))
  rw [← hasseDeriv_hasseDeriv_of_disjoint hdisj,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      rw [Finset.mem_singleton.1 (Finsupp.support_single_subset hj)]
      simp [degreeOf, degrees_rename_of_injective (Option.some_injective τ)],
    hasseDeriv_single_aeval_X, mul_comm,
    hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by
      simp [aeval_X_eq_rename, degreeOf,
        degrees_rename_of_injective (Function.injective_of_subsingleton _), Multiset.mem_replicate,
        hnone hj],
    hasseDeriv_rename (Option.some_injective τ), mul_comm]

/-- Source: §5, proof of Lemma 6 ("`V(x_p) ∈ ℛ_1(M; l r_p)`"): the coefficients of a univariate
polynomial viewed as a one-variable `MvPolynomial`. -/
theorem coeff_uniqueAlgEquiv_symm {σ : Type*} [Unique σ] (f : Polynomial R) (n : ℕ) :
    ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n := by
  rw [MvPolynomial.coeff_uniqueAlgEquiv_symm, Finsupp.single_eq_same]

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

variable {R : Type*} [CommRing R] [IsDomain R]

omit [Fintype τ] [DecidableEq τ] in
/-- For `V ≠ 0`, the degree of `U(x_τ) V(x_none)` in `x_j` is the degree of `U` in `x_j`.
Source: §2, end of the proof of Lemma 2 ("since the variables are disjoint and both factors are
nonzero, the individual degrees of `U, V` equal the corresponding degrees of `F`"). -/
theorem degreeOf_rename_mul_aeval (U : MvPolynomial τ R) {V : Polynomial R} (hV : V ≠ 0) (j : τ) :
    degreeOf (some j) (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      degreeOf j U := by
  classical
  by_cases hU : U = 0
  · simp [hU]
  rw [degreeOf_mul_eq ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      ((map_ne_zero_iff (Polynomial.aeval (X none))
        (Polynomial.toMvPolynomial_injective none)).2 hV),
    degreeOf_rename_of_injective (Option.some_injective τ)]
  simp [aeval_X_eq_rename, degreeOf,
    degrees_rename_of_injective (Function.injective_of_subsingleton _), Multiset.mem_replicate]

omit [Fintype τ] [DecidableEq τ] in
/-- For `U ≠ 0`, the degree of `U(x_τ) V(x_none)` in `x_none` is the degree of `V`.
Source: §2, end of the proof of Lemma 2. -/
theorem degreeOf_none_rename_mul_aeval {U : MvPolynomial τ R} (hU : U ≠ 0) (V : Polynomial R) :
    degreeOf none (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      V.natDegree := by
  classical
  by_cases hV : V = 0
  · simp [hV]
  rw [degreeOf_mul_eq ((rename_eq_zero_iff_of_injective U (Option.some_injective τ)).not.mpr hU)
      ((map_ne_zero_iff (Polynomial.aeval (X none))
        (Polynomial.toMvPolynomial_injective none)).2 hV),
    (show degreeOf none (rename some U) = 0 by
      simp [degreeOf, degrees_rename_of_injective (Option.some_injective τ)]),
    zero_add, aeval_X_eq_rename]
  exact (degreeOf_rename_of_injective (f := fun _ : Unit => (none : Option τ))
    (fun _ _ _ => rfl) ()).trans (degreeOf_uniqueAlgEquiv_symm V)

end Domain

section Field

variable {K : Type*} [Field K]

omit [Fintype τ] [DecidableEq τ] in
private lemma linearIndependent_coordinate_polynomials_aux {R M : Type*} [CommRing R]
    [AddCommMonoid M] [Module R M] {n l : ℕ} (v : Fin (n + 1) → M)
    (b : Module.Basis (Fin l) R (Submodule.span R (Set.range v))) :
    LinearIndependent R (fun ρ ↦ ∑ ν : Fin (n + 1),
      Polynomial.C (b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ)) := by
  classical
  let a := fun ν ρ ↦ b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ
  rw [Fintype.linearIndependent_iff]
  intro g hg ρ₀
  have hcoeff : ∀ ν : Fin (n + 1), ∑ ρ, g ρ * a ν ρ = 0 := by
    intro ν
    have h1 := congrArg (fun p : Polynomial R ↦ p.coeff ν) hg
    simp only [Polynomial.finsetSum_coeff, Polynomial.coeff_smul, smul_eq_mul,
      Polynomial.coeff_C_mul_X_pow, Polynomial.coeff_zero] at h1
    rw [← h1]
    refine Finset.sum_congr rfl fun ρ _ ↦ ?_
    rw [Finset.sum_eq_single ν (fun ν' _ hν' ↦ ite_eq_right fun h ↦ hν' (Fin.ext h).symm)
      (fun h ↦ absurd (Finset.mem_univ ν) h), ite_eq_left rfl]
  let f : Submodule.span R (Set.range v) →ₗ[R] R := ∑ ρ, g ρ • b.coord ρ
  have hf : f = 0 := LinearMap.ext_on Submodule.span_span_coe_preimage fun x hx ↦ by
    obtain ⟨ν, hν⟩ := hx
    obtain rfl : x = ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ := Subtype.ext hν.symm
    simpa only [f, a, LinearMap.sum_apply, LinearMap.smul_apply, smul_eq_mul,
      Module.Basis.coord_apply, LinearMap.zero_apply] using hcoeff ν
  simpa only [f, LinearMap.sum_apply, LinearMap.smul_apply, Module.Basis.coord_apply,
    Module.Basis.repr_self, Finsupp.single_apply, smul_eq_mul, mul_ite, mul_one, mul_zero,
    Finset.sum_ite_eq, Finset.mem_univ, ite_true, LinearMap.zero_apply] using
    LinearMap.congr_fun hf (b ρ₀)

omit [Fintype τ] [DecidableEq τ] in
private lemma eq_sum_aeval_basis_coeffNone_aux {R : Type*} [CommSemiring R]
    {P : MvPolynomial (Option τ) R} {n l : ℕ}
    (hP : P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (coeffNone P ν))
    (b : Module.Basis (Fin l) R
      (Submodule.span R (Set.range (fun ν : Fin (n + 1) ↦ coeffNone P ν)))) :
    P = ∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R) (∑ ν : Fin (n + 1),
        Polynomial.C (b.repr ⟨coeffNone P ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) *
          Polynomial.X ^ (ν : ℕ)) * rename some (b ρ : MvPolynomial τ R) := by
  let a := fun (ν : Fin (n + 1)) ρ ↦ b.repr ⟨coeffNone P ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ
  have hexp : ∀ ν : Fin (n + 1), coeffNone P ν = ∑ ρ, a ν ρ • (b ρ : MvPolynomial τ R) := fun ν ↦ by
    have h := congrArg Subtype.val (b.sum_repr ⟨coeffNone P ν, Submodule.subset_span ⟨ν, rfl⟩⟩)
    simpa only [Submodule.coe_sum, Submodule.coe_smul] using h.symm
  change P = ∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R)
    (∑ ν : Fin (n + 1), Polynomial.C (a ν ρ) * Polynomial.X ^ (ν : ℕ)) *
      rename some (b ρ : MvPolynomial τ R)
  conv_lhs => rw [hP]
  simp_rw [hexp, map_sum, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun ρ _ ↦ ?_
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun ν _ ↦ ?_
  rw [map_smul, smul_eq_C_mul, map_mul, Polynomial.aeval_C, algebraMap_eq, map_pow,
    Polynomial.aeval_X]
  ac_rfl

omit [Fintype τ] [DecidableEq τ] in
private lemma exists_coeffNone_basis_aux {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ}
    (hP' : P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (coeffNone P ν)) :
    ∃ l, ∃ b : Module.Basis (Fin l) K
      (Submodule.span K (Set.range (fun ν : Fin (n + 1) ↦ coeffNone P ν))),
      1 ≤ l ∧ l ≤ n + 1 ∧ ∀ ρ j, degreeOf j (b ρ : MvPolynomial τ K) ≤ degreeOf (some j) P := by
  classical
  let v : Fin (n + 1) → MvPolynomial τ K := fun ν ↦ coeffNone P ν
  let V := Submodule.span K (Set.range v)
  have : FiniteDimensional K V := FiniteDimensional.span_of_finite K (Set.finite_range v)
  let b := Module.finBasis K V
  have hl1 : 1 ≤ Module.finrank K V := by
    obtain ⟨ν, hν⟩ : ∃ ν, v ν ≠ 0 := by
      by_contra! h
      apply hP
      change P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (v ν) at hP'
      rw [hP']
      simp [h]
    exact Module.finrank_pos_iff_exists_ne_zero.2
      ⟨⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩, fun h ↦ hν (congrArg Subtype.val h)⟩
  have hdegree : V ≤ restrictSupport K {d | ∀ j, d j ≤ degreeOf (some j) P} :=
    Submodule.span_le.2 (Set.range_subset_iff.2 fun (ν : Fin (n + 1)) d hd j ↦ by
      simpa using monomial_le_degreeOf (some j)
        ((mem_support_coeff_optionEquivLeft K).1 hd))
  exact ⟨Module.finrank K V, b, hl1,
    (finrank_range_le_card (R := K) v).trans_eq (Fintype.card_fin _),
    fun ρ j ↦ degreeOf_le_iff.2 fun d hd ↦ hdegree (b ρ).2 hd j⟩

omit [Fintype τ] [DecidableEq τ] in
/-- Over a field, a nonzero `P` of degree at most `n` in `x_none` can be written as
`∑_{ν < l} φ_ν(x_none) ψ_ν(x_τ)` with `1 ≤ l ≤ n + 1`, both families linearly independent,
`deg φ_ν ≤ n`, and each `ψ_ν` of degree in `x_j` at most that of `P`.
Source: §2, proof of Lemma 2 and its Lean implementation note ("Construct the separated
decomposition over `ℚ` from a basis of the span of the coefficient polynomials of `R` in `x_p`";
the `φ_ν` and `ψ_ν` are linearly independent). -/
theorem exists_separated_representation {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ}
    (hn : degreeOf none P ≤ n) :
    ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
      LinearIndependent K φ ∧ LinearIndependent K ψ ∧ (∀ ν, (φ ν).natDegree ≤ n) ∧
      (∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P) ∧
      P = ∑ ν, Polynomial.aeval (X none : MvPolynomial (Option τ) K) (φ ν) * rename some (ψ ν) := by
  classical
  let v : Fin (n + 1) → MvPolynomial τ K := fun ν ↦ coeffNone P ν
  have hP' : P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (v ν) := by
    rw [Fin.sum_univ_eq_sum_range (fun ν ↦ X none ^ ν * rename some (coeffNone P ν))]
    exact eq_sum_X_none_pow_mul_coeffNone P hn
  obtain ⟨l, b, hl1, hl2, hdegree⟩ := exists_coeffNone_basis_aux hP hP'
  refine ⟨l, hl1, hl2, fun ρ ↦ ∑ ν : Fin (n + 1),
      Polynomial.C (b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ),
    fun ρ ↦ (b ρ : MvPolynomial τ K), linearIndependent_coordinate_polynomials_aux v b,
    b.linearIndependent.map' (Submodule.span K (Set.range v)).subtype
      (Submodule.ker_subtype _), ?_, hdegree,
    eq_sum_aeval_basis_coeffNone_aux hP' b⟩
  exact fun ρ ↦ Polynomial.natDegree_sum_le_of_forall_le _ _ fun ν _ ↦
    (Polynomial.natDegree_C_mul_X_pow_le _ _).trans (Nat.lt_succ_iff.1 ν.2)

omit [Fintype τ] [DecidableEq τ] in
/-- The determinant of Hasse derivatives of a separated sum `∑ φ_ρ(x_none) ψ_ρ(x_τ)` is the
product of the generalised Wronskian of `ψ` and the Wronskian of `φ`.
Source: §2, proof of Lemma 2 ("The matrix defining `F` is `A Bᵀ`, so `F = det A det B` by
multiplicativity and invariance under transpose. Explicitly, we obtain `GW = det (...)`"). -/
theorem det_hasseDeriv_separated {l : ℕ} (D : Fin l → (τ →₀ ℕ)) (φ : Fin l → Polynomial K)
    (ψ : Fin l → MvPolynomial τ K) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ))
        (∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) K) (φ ρ) *
          rename some (ψ ρ))).det = rename some (genWronskian D ψ) *
      Polynomial.aeval (X none : MvPolynomial (Option τ) K) (wronskian φ) := by
  rw [genWronskian, wronskian, AlgHom.map_det, AlgHom.map_det,
    ← Matrix.det_transpose ((Polynomial.aeval (X none)).mapMatrix (wronskianMatrix φ)),
    ← Matrix.det_mul]
  congr 1
  refine Matrix.ext fun μ ν ↦ ?_
  rw [Matrix.of_apply, map_sum, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun ρ _ ↦ ?_
  rw [mul_comm (Polynomial.aeval (X none : MvPolynomial (Option τ) K) (φ ρ)),
    hasseDeriv_rename_mul_aeval]
  rfl

end Field

section Integrality

/-- Bézout's identity for a finite family of integers. Source: §2, Lean implementation note
("if integer coefficients `u_a` have gcd `1` ... by a Bézout relation"). -/
theorem exists_sum_mul_eq_gcd {ι : Type*} (s : Finset ι) (u : ι → ℤ) :
    ∃ z : ι → ℤ, ∑ i ∈ s, z i * u i = s.gcd u := by
  simpa [eq_comm, mul_comm] using Finset.gcd_eq_sum_mul s u

/-- A rational polynomial becomes integral after multiplication by a positive integer.
Source: §2, proof of Lemma 2 ("clearing denominators"). -/
theorem exists_nat_smul_eq_map {σ : Type*} (G : MvPolynomial σ ℚ) :
    ∃ (N : ℕ) (U : MvPolynomial σ ℤ), 0 < N ∧ map (Int.castRingHom ℚ) U = (N : ℚ) • G := by
  classical
  set N := ∏ d ∈ G.support, (G.coeff d).den with hN
  have hint : ∀ d, ∃ z : ℤ, (N : ℚ) * G.coeff d = z := by
    intro d
    by_cases hd : d ∈ G.support
    · obtain ⟨k, hk⟩ := Finset.dvd_prod_of_mem (fun d ↦ (G.coeff d).den) hd
      refine ⟨k * (G.coeff d).num, ?_⟩
      rw [hN, hk]
      push_cast
      rw [mul_comm ((G.coeff d).den : ℚ) k, mul_assoc, Rat.den_mul_eq_num]
    · exact ⟨0, by simp [notMem_support_iff.1 hd]⟩
  choose c hc using hint
  refine ⟨N, ∑ d ∈ G.support, monomial d (c d), Finset.prod_pos fun _ _ ↦ Rat.den_pos _, ?_⟩
  ext e
  rw [coeff_map, coeff_sum, coeff_smul, smul_eq_mul, hc e]
  simp only [coeff_monomial, Finset.sum_ite_eq']
  split_ifs with he
  · simp
  · simpa [notMem_support_iff.1 he] using hc e

/-- Every nonzero rational polynomial has a nonzero rational multiple that is an integral
polynomial with coprime coefficients.
Source: §2, proof of Lemma 2 ("Choose `g ∈ ℚ×` so that `U = gG` is an integral primitive
polynomial, by clearing denominators and then dividing by the gcd of its coefficients"). -/
theorem exists_primitive_smul_eq {σ : Type*} {G : MvPolynomial σ ℚ} (hG : G ≠ 0) :
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧
      U.support.gcd (fun d ↦ U.coeff d) = 1 := by
  classical
  obtain ⟨N, U0, hN, hU0⟩ := exists_nat_smul_eq_map G
  have hne : U0.support.Nonempty := support_nonempty.mpr fun h ↦ by
    simpa [h, smul_eq_zero, hN.ne', hG] using hU0.symm
  obtain ⟨g', hg', hg1⟩ := Finset.extract_gcd (fun d ↦ U0.coeff d) hne
  set g0 := U0.support.gcd (fun d ↦ U0.coeff d) with hg0def
  have hg0 : g0 ≠ 0 := by
    obtain ⟨d, hd⟩ := hne
    rw [hg0def, Ne, Finset.gcd_eq_zero_iff]
    exact fun h ↦ mem_support_iff.1 hd (h d hd)
  set U := ∑ d ∈ U0.support, monomial d (g' d) with hUdef
  have hUcoeff : ∀ d, U.coeff d = if d ∈ U0.support then g' d else 0 := by
    simp [hUdef, coeff_monomial, Finset.sum_ite_eq']
  have hU0coeff : ∀ d, U0.coeff d = g0 * U.coeff d := by
    intro d
    by_cases hd : d ∈ U0.support
    · simpa [hUcoeff, hd] using hg' d hd
    · simp [hUcoeff, hd, notMem_support_iff.1 hd]
  refine ⟨N / g0, U, div_ne_zero (by exact_mod_cast hN.ne') (by exact_mod_cast hg0), ?_, ?_⟩
  · ext d
    have h1 := congrArg (fun P ↦ P.coeff d) hU0
    simp only [coeff_map, coeff_smul, smul_eq_mul, eq_intCast] at h1 ⊢
    rw [hU0coeff] at h1
    push_cast at h1
    rwa [div_mul_eq_mul_div, eq_div_iff (by exact_mod_cast hg0), mul_comm]
  · have hsupp : U.support = U0.support := by
      ext d
      simp [mem_support_iff, hU0coeff d, hg0]
    rw [hsupp, ← hg1]
    exact Finset.gcd_congr rfl fun d hd ↦ by rw [hUcoeff, ite_eq_left hd]

/-- If integers `u_a` have gcd `1` and every `u_a v` is an integer, then `v` is an integer.
Source: §2, proof of Lemma 2 ("Primitivity gives a finite integral linear combination
`∑ z_a u_a = 1`, so `v_b = ∑ z_a (u_a v_b)` is an integer"). -/
theorem exists_int_eq_of_gcd_eq_one {ι : Type*} {s : Finset ι} {u : ι → ℤ} (hu : s.gcd u = 1)
    {v : ℚ} (hv : ∀ a ∈ s, ∃ z : ℤ, (u a : ℚ) * v = z) : ∃ z : ℤ, v = z := by
  classical
  obtain ⟨z, hz⟩ := exists_sum_mul_eq_gcd s u
  rw [hu] at hz
  choose! w hw using hv
  refine ⟨∑ i ∈ s, z i * w i, ?_⟩
  calc v = ((∑ i ∈ s, z i * u i : ℤ) : ℚ) * v := by simp [hz]
    _ = ((∑ i ∈ s, z i * w i : ℤ) : ℚ) := by
        push_cast
        rw [Finset.sum_mul]
        exact Finset.sum_congr rfl fun i hi ↦ by rw [mul_assoc, hw i hi]

private lemma degreeOf_map_intCast {σ : Type*} (U : MvPolynomial σ ℤ) (j : σ) :
    degreeOf j (map (Int.castRingHom ℚ) U) = degreeOf j U := by
  rw [degreeOf_eq_sup, degreeOf_eq_sup, support_map_of_injective _ Int.cast_injective]

/-- If an integer polynomial `F` factors over `ℚ` as `U'(x_τ) V'(x_none)` with nonzero factors,
then it factors over `ℤ` as `U(x_τ) V(x_none)` with the same partial degrees.
Source: §2, proof of Lemma 2 ("Thus `U, V` are integral and nonzero, as required"), together
with the degree comparison at the end of the proof. -/
theorem exists_int_factors {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) ℤ}
    (hF : map (Int.castRingHom ℚ) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :
    ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree := by
  classical
  obtain ⟨g, U, hg, hUmap, hgcd⟩ := exists_primitive_smul_eq hU
  set V'' : Polynomial ℚ := Polynomial.C g⁻¹ * V' with hV''
  have hF' : map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) *
      Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V'' := by
    rw [hF, hUmap, hV'', map_mul, Polynomial.aeval_C, algebraMap_eq, smul_eq_C_mul, map_mul,
      rename_C]
    have : C g * C g⁻¹ = (1 : MvPolynomial (Option τ) ℚ) := by
      rw [← C_mul, mul_inv_cancel₀ hg, C_1]
    linear_combination (rename some U' * Polynomial.aeval (X none) V') * this.symm
  have hint : ∀ b, ∃ z : ℤ, V''.coeff b = z := fun b =>
    exists_int_eq_of_gcd_eq_one hgcd fun a _ =>
      ⟨F.coeff (a.mapDomain some + Finsupp.single none b), by
        have h1 := congrArg (fun P => P.coeff (a.mapDomain some + Finsupp.single none b)) hF'
        simp only [coeff_rename_mul_aeval, coeff_map] at h1
        simpa using h1.symm⟩
  choose w hw using hint
  set V : Polynomial ℤ := ∑ b ∈ V''.support, Polynomial.monomial b (w b) with hVdef
  have hVmap : V.map (Int.castRingHom ℚ) = V'' := by
    ext b
    rw [Polynomial.coeff_map, hVdef, Polynomial.finsetSum_coeff]
    simp only [Polynomial.coeff_monomial, Finset.sum_ite_eq']
    split_ifs with hb
    · rw [hw b]
      rfl
    · rw [Polynomial.notMem_support_iff.1 hb]
      simp
  have hV''ne : V'' ≠ 0 := mul_ne_zero (Polynomial.C_ne_zero.2 (inv_ne_zero hg)) hV
  have hUne : U ≠ 0 := by
    rintro rfl
    rw [map_zero] at hUmap
    exact hU ((smul_eq_zero.1 hUmap.symm).resolve_left hg)
  have hVne : V ≠ 0 := by
    intro h
    rw [h, Polynomial.map_zero] at hVmap
    exact hV''ne hVmap.symm
  refine ⟨U, V, hUne, hVne, ?_, fun j => ?_, ?_⟩
  · apply MvPolynomial.map_injective (Int.castRingHom ℚ) Int.cast_injective
    rw [hF', map_mul (map (Int.castRingHom ℚ)), map_rename,
      Polynomial.map_aeval_eq_aeval_map (φ := Int.castRingHom ℚ) (Subsingleton.elim _ _), map_X,
      hVmap]
  · rw [← degreeOf_map_intCast, hUmap, smul_eq_C_mul,
      degreeOf_C_mul j g (mem_nonZeroDivisors_of_ne_zero hg)]
  · rw [← Polynomial.natDegree_map_eq_of_injective (f := Int.castRingHom ℚ)
      (RingHom.injective_int _), hVmap, hV'',
      Polynomial.natDegree_C_mul (inv_ne_zero hg)]

end Integrality

/-- Lemma 2. Source: §2, Lemma `roth:lem2` ("there is an integer `l` satisfying `1 ≤ l ≤ r_p + 1`
and there are differential operators `Δ_0, …, Δ_{l-1}` on the variables `x_1, …, x_{p-1}` of
orders at most `0, …, l-1` such that ... `F = U(x_1, …, x_{p-1}) V(x_p)` where `U, V` are nonzero,
have integral coefficients, `U` is of degree at most `l r_j` in `x_j` ... and `V` is of degree
at most `l r_p`"). -/
theorem exists_det_eq_mul {P : MvPolynomial (Option τ) ℤ} (hP : P ≠ 0) {r : Option τ → ℕ}
    (hr : ∀ j, degreeOf j P ≤ r j) :
    ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧
      ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
        (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧
        (Matrix.of fun μ ν : Fin l =>
            hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =
          rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V := by
  classical
  set PQ := map (Int.castRingHom ℚ) P with hPQdef
  have hPQ0 : PQ ≠ 0 := fun h =>
    hP (MvPolynomial.map_injective _ Int.cast_injective (h.trans (map_zero _).symm))
  have hdeg : degreeOf none PQ ≤ r none := (degreeOf_map_intCast P none).trans_le (hr none)
  obtain ⟨l, hl1, hl2, φ, ψ, hφ, hψ, -, -, hPQ⟩ := exists_separated_representation hPQ0 hdeg
  have hW := wronskian_ne_zero_of_linearIndependent hφ
  obtain ⟨D, hD, hG⟩ := exists_genWronskian_ne_zero hψ
  set F := (Matrix.of fun μ ν : Fin l =>
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det with hFdef
  have hFmap : map (Int.castRingHom ℚ) F = rename some (genWronskian D ψ) *
      Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) (wronskian φ) := by
    rw [hFdef, RingHom.map_det, ← det_hasseDeriv_separated D φ ψ, ← hPQ]
    congr 1
    refine Matrix.ext fun μ ν => ?_
    rw [RingHom.mapMatrix_apply, Matrix.map_apply, Matrix.of_apply, Matrix.of_apply,
      hPQdef, hasseDeriv_map]
  obtain ⟨U, V, hU, hV, hFUV, -, -⟩ := exists_int_factors hG hW hFmap
  refine ⟨l, hl1, hl2, D, hD, U, V, hU, hV, fun j => ?_, ?_, hFUV⟩
  · have h1 := degreeOf_det_hasseDeriv_le
      (fun μ ν : Fin l => (D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P hr (some j)
    rwa [← hFdef, hFUV, degreeOf_rename_mul_aeval U hV j] at h1
  · have h1 := degreeOf_det_hasseDeriv_le
      (fun μ ν : Fin l => (D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P hr none
    rwa [← hFdef, hFUV, degreeOf_none_rename_mul_aeval hU V] at h1

end Roth
