import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.LinearAlgebra.Dimension.OrzechProperty
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.LinearAlgebra.Vandermonde
import Mathlib.RingTheory.Polynomial.Pochhammer

/-!
# Wronskians of finitely many univariate polynomials

For `φ : Fin l → K[X]` the Wronskian is `det (hasseDeriv μ (φ ν))_{μ ν}` (Hasse derivatives
`(1/μ!) d^μ/dt^μ`). Over a field of characteristic zero it vanishes iff the family is linearly
dependent. Mathlib's `Polynomial.wronskian` only treats two polynomials, so the `l × l`
determinant is set up here.

## Main definitions

* `Roth.wronskianMatrix φ`: the matrix `(hasseDeriv μ (φ ν))_{μ, ν}`.
* `Roth.wronskian φ`: its determinant.

## Main results

* `Roth.det_choose_eq`: the determinant of `(d ν choose μ)_{μ, ν}` is a Vandermonde product
  divided by `∏ μ!`.
* `Roth.wronskian_ne_zero_of_natDegree_injective`: a family of nonzero polynomials of pairwise
  distinct degrees has nonzero Wronskian.
* `Roth.wronskian_eq_zero_iff`: in characteristic zero, the Wronskian vanishes iff the family is
  linearly dependent.

## Implementation notes

The hard direction reduces to the case of distinct degrees by column operations
`φ ν' ↦ φ ν' - c φ ν` (`Roth.wronskian_update_sub_smul`), which preserve linear independence and,
for a suitable `c`, strictly decrease the total degree (`Roth.sum_natDegree_update_lt`). In the
distinct-degree case the coefficient of the top possible degree is computed explicitly
(`Roth.coeff_wronskian_of_natDegree_injective`).

## References

* Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §2 "Wronskians", first lemma
  (`.mathlib-quality/references/clean.tex`).
-/

namespace Roth

open Polynomial

variable {K : Type*} [Field K] {l : ℕ}

/-- The Wronskian matrix `(hasseDeriv μ (φ ν))_{μ, ν}`. Source: §2, definition of `W`. -/
noncomputable def wronskianMatrix (φ : Fin l → K[X]) : Matrix (Fin l) (Fin l) K[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)

/-- The Wronskian `det (hasseDeriv μ (φ ν))_{μ, ν}`. Source: §2, definition of `W`. -/
noncomputable def wronskian (φ : Fin l → K[X]) : K[X] := (wronskianMatrix φ).det

/-- A linearly dependent family has vanishing Wronskian; this holds over any field.
Source: §2, first lemma, easy direction ("Linear dependence gives a nontrivial constant linear
relation between the columns, so the determinant vanishes"). -/
theorem wronskian_eq_zero_of_not_linearIndependent {φ : Fin l → K[X]}
    (h : ¬ LinearIndependent K φ) : wronskian φ = 0 := by
  obtain ⟨g, hg, ν₀, hν₀⟩ := Fintype.not_linearIndependent_iff.1 h
  refine Matrix.exists_mulVec_eq_zero_iff.1 ⟨fun ν => C (g ν), fun h0 => hν₀ ?_, ?_⟩
  · simpa using congrFun h0 ν₀
  · ext1 μ
    simpa [wronskianMatrix, Matrix.mulVec, dotProduct, ← smul_eq_C_mul, mul_comm]
      using congrArg (hasseDeriv (μ : ℕ)) hg

/-- The determinant of the binomial matrix `(d ν choose μ)_{μ, ν}` is the Vandermonde product
`∏_{i<j} (d j - d i)` times `∏ μ, (μ!)⁻¹`.
Source: §2, first lemma ("`det (d_ν choose μ) = ∏_{i<j} (d_j - d_i) / ∏ μ!`: `binom X μ` has
degree `μ` and leading coefficient `1/μ!`, so its evaluation determinant is the Vandermonde
determinant multiplied by `∏ 1/μ!`"). -/
theorem det_choose_eq [CharZero K] (d : Fin l → ℕ) :
    (Matrix.of fun μ ν : Fin l => ((d ν).choose μ : K)).det =
      (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) *
        ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i) := by
  have h1 : (Matrix.of fun μ ν : Fin l => ((d ν).choose μ : K)) =
      Matrix.of fun μ ν : Fin l => ((μ : ℕ).factorial : K)⁻¹ *
        (Matrix.of fun μ' ν' : Fin l => (descPochhammer K μ').eval (d ν' : K)) μ ν := by
    ext μ ν
    simp [Nat.cast_choose_eq_descPochhammer_div, div_eq_inv_mul]
  have h2 : Matrix.transpose (Matrix.of fun μ ν : Fin l => (descPochhammer K μ).eval (d ν : K)) =
      Matrix.of fun i j : Fin l => (descPochhammer K j).eval (d i : K) :=
    rfl
  rw [h1, Matrix.det_mul_column, ← Matrix.det_transpose, h2,
    ← Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde (fun i => (d i : K))
      (fun j => descPochhammer K j) (fun i => descPochhammer_natDegree K _)
      (fun i => monic_descPochhammer K _), Matrix.det_vandermonde]

private lemma sum_range_card_le_sum (S : Finset ℕ) :
    ∑ k ∈ Finset.range S.card, k ≤ ∑ x ∈ S, x := by
  induction S using Finset.induction_on_max with
  | empty => simp
  | insert a s ha ih =>
    have has : a ∉ s := fun h => lt_irrefl a (ha a h)
    have hcard : s.card ≤ a := by
      simpa using Finset.card_le_card
        (fun x hx => Finset.mem_range.2 (ha x hx) : s ⊆ Finset.range a)
    rw [Finset.card_insert_of_notMem has, Finset.sum_range_succ, Finset.sum_insert has]
    lia

private lemma coeff_prod_of_natDegree_le' {ι : Type*} (s : Finset ι) (f : ι → K[X]) (n : ι → ℕ)
    (h : ∀ i ∈ s, (f i).natDegree ≤ n i) :
    (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s has ih =>
    rw [Finset.prod_insert has, Finset.sum_insert has, Finset.prod_insert has,
      coeff_mul_add_eq_of_natDegree_le (h a (Finset.mem_insert_self a s))
        ((natDegree_prod_le _ _).trans
          (Finset.sum_le_sum fun i hi => h i (Finset.mem_insert_of_mem hi))),
      ih fun i hi => h i (Finset.mem_insert_of_mem hi)]

/-- `l` distinct natural numbers sum to at least `0 + 1 + ⋯ + (l - 1)`.
Source: §2, first lemma (`D = ∑ d_ν - l(l-1)/2 ≥ 0` for distinct degrees). -/
theorem sum_range_le_sum_of_injective (d : Fin l → ℕ) (hd : Function.Injective d) :
    ∑ ν : Fin l, (ν : ℕ) ≤ ∑ ν, d ν := by
  classical
  have h := sum_range_card_le_sum (Finset.univ.image d)
  rwa [Finset.card_image_of_injective _ hd, Finset.card_univ, Fintype.card_fin,
    Finset.sum_image fun x _ y _ hxy => hd hxy, ← Fin.sum_univ_eq_sum_range] at h

/-- For a family of pairwise distinct degrees `d ν`, the coefficient of the Wronskian in degree
`∑ d ν - ∑ ν` is `∏ (leading coefficients)` times the binomial determinant `det (d ν choose μ)`.
The hypotheses are not needed for the identity itself, which holds for any family (both sides
may vanish), but they are the setting in which it is used.
Source: §2, first lemma ("The coefficient of `t^D` in the new Wronskian is
`(∏ a_ν) det (d_ν choose μ)`... All other contributions have lower total degree"). -/
theorem coeff_wronskian_of_natDegree_injective {φ : Fin l → K[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν => (φ ν).natDegree) :
    (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      (∏ ν, (φ ν).leadingCoeff) *
        (Matrix.of fun μ ν : Fin l => (((φ ν).natDegree.choose μ : ℕ) : K)).det := by
  classical
  have key : ∀ σ : Equiv.Perm (Fin l),
      (∏ i, hasseDeriv ((σ i : Fin l) : ℕ) (φ i)).coeff
          (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
        ∏ i, (((φ i).natDegree.choose (σ i) : ℕ) : K) * (φ i).leadingCoeff := by
    intro σ
    by_cases h : ∀ i, ((σ i : Fin l) : ℕ) ≤ (φ i).natDegree
    · have hD : ∑ i, ((φ i).natDegree - (σ i : ℕ)) =
          ∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ) := by
        rw [Finset.sum_tsub_distrib _ fun i _ => h i,
          Equiv.sum_comp σ (fun i : Fin l => (i : ℕ))]
      rw [← hD, coeff_prod_of_natDegree_le' _ _ _ fun i _ => natDegree_hasseDeriv_le _ _]
      refine Finset.prod_congr rfl fun i _ => ?_
      rw [hasseDeriv_coeff, Nat.sub_add_cancel (h i), leadingCoeff]
    · push Not at h
      obtain ⟨i, hi⟩ := h
      rw [Finset.prod_eq_zero (Finset.mem_univ i) (hasseDeriv_eq_zero_of_lt_natDegree _ _ hi),
        coeff_zero]
      exact (Finset.prod_eq_zero (Finset.mem_univ i) (by simp [Nat.choose_eq_zero_of_lt hi])).symm
  rw [wronskian, wronskianMatrix, Matrix.det_apply', Matrix.det_apply', finsetSum_coeff,
    Finset.mul_sum]
  refine Finset.sum_congr rfl fun σ _ => ?_
  simp only [Matrix.of_apply, coeff_intCast_mul, key, Finset.prod_mul_distrib]
  ring

/-- In characteristic zero, nonzero polynomials of pairwise distinct degrees have nonzero
Wronskian.
Source: §2, first lemma ("Thus the new Wronskian ... is nonzero" for a family with distinct
degrees). -/
theorem wronskian_ne_zero_of_natDegree_injective [CharZero K] {φ : Fin l → K[X]}
    (hφ : ∀ ν, φ ν ≠ 0) (hd : Function.Injective fun ν => (φ ν).natDegree) :
    wronskian φ ≠ 0 := by
  intro h0
  have h1 := coeff_wronskian_of_natDegree_injective hφ hd
  rw [h0, coeff_zero, det_choose_eq] at h1
  simp [eq_comm (a := (0 : K)), Finset.prod_eq_zero_iff, sub_eq_zero, hφ, Nat.factorial_ne_zero,
    hd.eq_iff] at h1

/-- Subtracting a constant multiple of one member of the family from another does not change
the Wronskian.
Source: §2, first lemma ("By invertible column operations over `ℚ`" — a single column
operation does not change the Wronskian). -/
theorem wronskian_update_sub_smul {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) :
    wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ := by
  have hM : wronskianMatrix (Function.update φ ν' (φ ν' - C c * φ ν)) =
      (wronskianMatrix φ).updateCol ν'
        fun k => wronskianMatrix φ k ν' + (-C c) • wronskianMatrix φ k ν := by
    ext μ ρ
    rcases eq_or_ne ρ ν' with rfl | hρ
    · simp [wronskianMatrix, ← smul_eq_C_mul, sub_eq_add_neg]
    · simp [wronskianMatrix, Matrix.updateCol_ne hρ, Function.update_of_ne hρ]
  rw [wronskian, hM, Matrix.det_updateCol_add_smul_self _ h.symm, wronskian]

private lemma span_range_update_sub_le (φ : Fin l → K[X]) (ν ν' : Fin l) (c : K) :
    Submodule.span K (Set.range (Function.update φ ν' (φ ν' - C c * φ ν))) ≤
      Submodule.span K (Set.range φ) := by
  refine Submodule.span_le.2 (Set.range_subset_iff.2 fun i => ?_)
  rcases eq_or_ne i ν' with rfl | hi
  · rw [Function.update_self, ← smul_eq_C_mul]
    exact sub_mem (Submodule.subset_span ⟨i, rfl⟩)
      (Submodule.smul_mem _ _ (Submodule.subset_span ⟨ν, rfl⟩))
  · rw [Function.update_of_ne hi]
    exact Submodule.subset_span ⟨i, rfl⟩

/-- Subtracting a constant multiple of one member of a linearly independent family from another
gives a linearly independent family.
Source: §2, first lemma ("replace them by a basis `g_0, …, g_{l-1}` of their span": a column
operation preserves linear independence). -/
theorem linearIndependent_update_sub_smul {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K)
    (hφ : LinearIndependent K φ) :
    LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν)) := by
  set ψ := Function.update φ ν' (φ ν' - C c * φ ν)
  have hinv : Function.update ψ ν' (ψ ν' - C (-c) * ψ ν) = φ := by
    simp [ψ, Function.update_of_ne h]
  have hspan : Submodule.span K (Set.range ψ) = Submodule.span K (Set.range φ) :=
    (span_range_update_sub_le φ ν ν' c).antisymm
      ((span_range_update_sub_le ψ ν ν' (-c)).trans_eq' (by rw [hinv]))
  rw [linearIndependent_iff_card_eq_finrank_span] at hφ ⊢
  rw [hφ, Set.finrank, Set.finrank, hspan]

/-- If two members `φ ν`, `φ ν'` of a linearly independent family have the same degree, cancelling
the leading coefficient of `φ ν'` against `φ ν` strictly lowers the total degree.
Source: §2, first lemma ("Such a basis is obtained by eliminating equal leading degrees": a
column operation that cancels a leading coefficient strictly lowers the sum of the degrees; the
difference is nonzero because the family is linearly independent). -/
theorem sum_natDegree_update_lt {φ : Fin l → K[X]} (hφ : LinearIndependent K φ) {ν ν' : Fin l}
    (h : ν ≠ ν') (hdeg : (φ ν).natDegree = (φ ν').natDegree) :
    ∑ ρ, (Function.update φ ν'
        (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree
      < ∑ ρ, (φ ρ).natDegree := by
  set a := (φ ν').leadingCoeff / (φ ν).leadingCoeff
  have h0 : ∀ i, φ i ≠ 0 := hφ.ne_zero
  have hlc : (φ ν).leadingCoeff ≠ 0 := leadingCoeff_ne_zero.2 (h0 ν)
  have ha : a ≠ 0 := div_ne_zero (leadingCoeff_ne_zero.2 (h0 ν')) hlc
  have hne : φ ν' - C a * φ ν ≠ 0 := fun h' =>
    hφ.notMem_span_image (s := {ν}) (Set.mem_singleton_iff.not.2 h.symm) <| by
      rw [Set.image_singleton, Submodule.mem_span_singleton]
      exact ⟨a, by rw [smul_eq_C_mul, ← sub_eq_zero.1 h']⟩
  have hdeg' : degree (φ ν') = degree (C a * φ ν) := by
    rw [degree_C_mul ha, degree_eq_natDegree (h0 ν), degree_eq_natDegree (h0 ν'), hdeg]
  have hlt : (φ ν' - C a * φ ν).natDegree < (φ ν').natDegree :=
    natDegree_lt_natDegree hne (degree_sub_lt_left hdeg' (h0 ν') (by
      rw [leadingCoeff_mul, leadingCoeff_C, div_mul_cancel₀ _ hlc]))
  refine Finset.sum_lt_sum (fun i _ => ?_) ⟨ν', Finset.mem_univ _, by rwa [Function.update_self]⟩
  rcases eq_or_ne i ν' with rfl | hi
  · rw [Function.update_self]
    exact hlt.le
  · rw [Function.update_of_ne hi]

/-- In characteristic zero, a linearly independent family has nonzero Wronskian.
Source: §2, first lemma, hard direction ("Conversely, suppose the polynomials are linearly
independent ... Thus the new Wronskian, and hence the original one, is nonzero"). -/
theorem wronskian_ne_zero_of_linearIndependent [CharZero K] {φ : Fin l → K[X]}
    (h : LinearIndependent K φ) : wronskian φ ≠ 0 := by
  classical
  induction hN : ∑ ρ, (φ ρ).natDegree using Nat.strong_induction_on generalizing φ with
  | _ N ih =>
    by_cases hinj : Function.Injective fun ν => (φ ν).natDegree
    · exact wronskian_ne_zero_of_natDegree_injective h.ne_zero hinj
    obtain ⟨ν, ν', hdeg, hne⟩ := Function.not_injective_iff.1 hinj
    rw [← wronskian_update_sub_smul hne ((φ ν').leadingCoeff / (φ ν).leadingCoeff)]
    exact ih _ (hN ▸ sum_natDegree_update_lt h hne hdeg)
      (linearIndependent_update_sub_smul hne _ h) rfl

/-- In characteristic zero, the Wronskian vanishes iff the family is linearly dependent.
Source: §2, first lemma ("the Wronskian vanishes if and only if they are linearly
dependent"). -/
theorem wronskian_eq_zero_iff [CharZero K] {φ : Fin l → K[X]} :
    wronskian φ = 0 ↔ ¬ LinearIndependent K φ :=
  ⟨fun hw hli => wronskian_ne_zero_of_linearIndependent hli hw,
    wronskian_eq_zero_of_not_linearIndependent⟩

end Roth
