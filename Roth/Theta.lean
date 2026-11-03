/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.RingTheory.Polynomial.GaussLemma

import Roth.CoeffNorm
import Roth.Index
import Roth.Separation

/-!
# The index across sets of polynomials: `Θ_m(B; q; r)` (Lemmas 5, 6, 7)

We define `Θ_m(B; q; r)`, the supremum of the indices of nonzero integer polynomials with
bounded degrees and coefficients at rational points with prescribed denominators, and prove the
three bounds on it (Lemmas 5, 6 and 7 of the source) that feed into the proof of Roth's theorem.

## Main definitions

* `Roth.boundedPolys B r`: the set `ℛ_m(B; r_1, …, r_m)` of nonzero integer polynomials of degree at
  most `r j` in `X j` with coefficients bounded by `B`.
* `Roth.indexSet B q r`: the set of indices of `R ∈ boundedPolys B r` at the points `(h_j / q_j)_j`
  with `gcd (h_j, q_j) = 1`, relative to `r`.
* `Roth.Θ B q r`: the supremum of `Roth.indexSet B q r`.
* `Roth.detCoeffBound`, `Roth.ΘSplit`: the auxiliary quantities `M` and `Φ` of Lemma 6.

## Main results

* `Roth.Θ_nonneg`, `Roth.Θ_le_card`: `0 ≤ Θ_m ≤ m`.
* `Roth.Θ_mono`, `Roth.Θ_equiv`: monotonicity in `B` and invariance under renaming variables.
* `Roth.Θ_unique_le` (Lemma 5): `Θ_1(B; q; r) ≤ log B / (r log q)`.
* `Roth.Θ_option_le` (Lemma 6): a bound on `Θ` in `p` variables (indexed by `Option τ`, where
  `none` is the variable `x_p` of the source) through `Θ` in `p - 1` variables and in one
  variable.
* `Roth.Θ_lt` (Lemma 7): `Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}`.

## References

* R. Takloo-Bighash and S. Yin, *Formalizing Roth's theorem*, §5 "Index across sets of
  polynomials" (`.mathlib-quality/references/clean.tex`).
-/

namespace Polynomial

/-- `a X - b` is primitive when `a` and `b` are relatively prime. -/
theorem isPrimitive_C_mul_X_sub_C_of_isRelPrime {R : Type*} [CommRing R] {a b : R}
    (h : IsRelPrime a b) : (C a * X - C b).IsPrimitive := by
  intro c hc
  rw [C_dvd_iff_dvd_coeff] at hc
  exact h (by simpa using hc 1) (by simpa using hc 0)

/-- Powers of a primitive polynomial are primitive. -/
theorem IsPrimitive.pow {R : Type*} [CommRing R] [NormalizedGCDMonoid R]
    {p : R[X]} (hp : p.IsPrimitive) (t : ℕ) : (p ^ t).IsPrimitive := by
  induction t with
  | zero => exact isPrimitive_one
  | succ t ih => simpa [pow_succ] using ih.mul hp

end Polynomial

namespace Roth

open MvPolynomial

variable {σ : Type*} [Fintype σ]

/-- The set `ℛ_m(B; r)` of nonzero integer polynomials whose degree in each variable `X j` is at
most `r j` and whose coefficients have absolute value at most `B`.
Source: §5 (items (1)–(3) of the definition of `ℛ_m`). -/
def boundedPolys (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ) :=
  {R | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧ ∀ d, |(R.coeff d : ℝ)| ≤ B}

/-- The set of indices `ind(R; h/q; r)` of polynomials `R ∈ ℛ_m(B; r)` at the points
`(h_j / q_j)_j` with each `h_j` coprime to `q_j`; its supremum is `Θ_m(B; q; r)`.
Source: §5, definition of `Θ_m`. -/
def indexSet (B : ℝ) (q r : σ → ℕ) : Set ℝ :=
  {x | ∃ R ∈ boundedPolys B r, ∃ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) ∧
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r = x}

/-- `Θ_m(B; q_1, …, q_m; r_1, …, r_m)` is the supremum of the indices `ind(R; h/q; r)` over
`R ∈ ℛ_m(B; r)` and `h` with each `h_j` coprime to `q_j`. Source: §5, definition of `Θ_m`. -/
noncomputable def Θ (B : ℝ) (q r : σ → ℕ) : ℝ := sSup (indexSet B q r)

omit [Fintype σ] in
/-- If `1 ≤ B`, the constant polynomial `1` lies in `ℛ_m(B; r)`. Source: §5 ("the constant
polynomial `1` with every `h_i = 1` is allowed"). -/
theorem one_mem_boundedPolys {B : ℝ} (hB : 1 ≤ B) (r : σ → ℕ) :
    (1 : MvPolynomial σ ℤ) ∈ boundedPolys B r := by
  classical
  simp [boundedPolys, coeff_one, apply_ite, ite_apply, hB, zero_le_one.trans hB]

/-- If `1 ≤ B`, the set of indices defining `Θ_m(B; q; r)` is nonempty. Source: §5 ("This
supremum is well-defined"). -/
theorem indexSet_nonempty {B : ℝ} (hB : 1 ≤ B) (q r : σ → ℕ) : (indexSet B q r).Nonempty :=
  ⟨_, 1, one_mem_boundedPolys hB r, fun _ ↦ 1, fun _ ↦ isCoprime_one_left, rfl⟩

private lemma card_mem_upperBounds_indexSet_aux (B : ℝ) (q r : σ → ℕ) :
    (Fintype.card σ : ℝ) ∈ upperBounds (indexSet B q r) := by
  rintro _ ⟨R, ⟨-, hRd, -⟩, h, -, rfl⟩
  exact index_le_card
    (fun j ↦ (degreeOf_map_of_injective Int.cast_injective j R).trans_le (hRd j)) _

/-- The indices defining `Θ_m(B; q; r)` are bounded above (by the number `m` of variables).
Source: §5 ("`0 ≤ Θ_m ≤ m`": Taylor's theorem gives a nonzero derivative of weight at most
`m`). -/
theorem indexSet_bddAbove (B : ℝ) (q r : σ → ℕ) : BddAbove (indexSet B q r) :=
  ⟨_, card_mem_upperBounds_indexSet_aux B q r⟩

/-- The index of any `R ∈ ℛ_m(B; r)` at a point `(h_j / q_j)_j` with each `h_j` coprime to `q_j`
is at most `Θ_m(B; q; r)`. Source: §5, definition of `Θ_m` as a supremum, and the Lean note
("lemmas for bounding an individual index"). -/
theorem index_le_Θ {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ} (hR : R ∈ boundedPolys B r)
    {h : σ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r :=
  le_csSup (indexSet_bddAbove B q r) ⟨R, hR, h, hh, rfl⟩

/-- `Θ_m(B; q; r)` is nonnegative for every coefficient bound and weight vector. Source: §5
("`0 ≤ Θ_m`"). -/
theorem Θ_nonneg (B : ℝ) (q r : σ → ℕ) : 0 ≤ Θ B q r := by
  apply Real.sSup_nonneg
  rintro _ ⟨R, _, h, _, rfl⟩
  exact index_nonneg _ _ _

/-- `Θ_m(B; q; r)` is at most the number `m` of variables. Source: §5 ("`Θ_m ≤ m`"). -/
theorem Θ_le_card (B : ℝ) (q r : σ → ℕ) : Θ B q r ≤ Fintype.card σ :=
  Real.sSup_le (card_mem_upperBounds_indexSet_aux B q r) (Nat.cast_nonneg _)

/-- A bound on every index is a bound on `Θ`. Source: §5, Lemma 5 ("Taking the supremum proves
the claim"). -/
theorem Θ_le_of_forall_index_le {B : ℝ} (hB : 1 ≤ B) {q r : σ → ℕ} {c : ℝ}
    (hc : ∀ R ∈ boundedPolys B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) : Θ B q r ≤ c := by
  refine csSup_le (indexSet_nonempty hB q r) ?_
  rintro _ ⟨R, hR, h, hh, rfl⟩
  exact hc R hR h hh

/-- `Θ_m(B; q; r)` is monotone in `B`. Source: §5 ("`Θ_m` is nondecreasing in `B`, since
increasing `B` enlarges the set of allowed polynomials"). -/
theorem Θ_mono {B B' : ℝ} (hBB' : B ≤ B') (q r : σ → ℕ) : Θ B q r ≤ Θ B' q r := by
  refine Real.sSup_le ?_ (Θ_nonneg B' q r)
  rintro _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, rfl⟩
  exact index_le_Θ ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩ hh

private lemma indexSet_comp_subset_aux {τ : Type*} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ) :
    indexSet B (q ∘ e) (r ∘ e) ⊆ indexSet B q r := by
  rintro _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, rfl⟩
  refine ⟨rename e R, ⟨?_, ?_, ?_⟩, h ∘ e.symm, ?_, ?_⟩
  · simpa [rename_eq_zero_iff_of_injective R e.injective] using hR0
  · intro j
    obtain ⟨i, rfl⟩ := e.surjective j
    simpa [degreeOf_rename_of_injective e.injective] using hRd i
  · intro d
    obtain ⟨d, rfl⟩ := Finsupp.mapDomain_surjective e.surjective d
    simpa [coeff_rename_mapDomain _ e.injective] using hRc d
  · intro j
    simpa using hh (e.symm j)
  · simp [map_rename, index_rename e.injective, Function.comp_def]

/-- `Θ` is invariant under renaming the variables. Source: §4, Lean note after Lemma 4-2
("invariance under ... variable renaming"). -/
theorem Θ_equiv {τ : Type*} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ) :
    Θ B (q ∘ e) (r ∘ e) = Θ B q r := by
  apply congrArg sSup
  refine subset_antisymm (indexSet_comp_subset_aux e B q r) ?_
  simpa [Function.comp_def] using indexSet_comp_subset_aux e.symm B (q ∘ e) (r ∘ e)

section Lemma5

/-- If `h` is coprime to `q > 0` and `t` is the multiplicity of `h / q` as a root of a nonzero
`R ∈ ℤ[X]`, then `R = (q X - h)^t Q` for some `Q ∈ ℤ[X]`.
Source: §5, proof of Lemma 5 ("The polynomial `(q_1 x_1 - h_1)^t` is primitive and divides
`R` over `ℚ`. Gauss's lemma therefore gives a nonzero `Q ∈ ℤ[x_1]` with
`R = (q_1 x_1 - h_1)^t Q`"). -/
theorem exists_eq_pow_mul_of_rootMultiplicity {R : Polynomial ℤ} {h : ℤ} {q : ℕ} (hq : 0 < q)
    (hcop : IsCoprime h (q : ℤ)) : ∃ Q : Polynomial ℤ, R =
      (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h) ^
      Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) * Q := by
  set t := Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ))
  have hq' : (q : ℚ) ≠ 0 := by exact_mod_cast hq.ne'
  have hmap : (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h).map (Int.castRingHom ℚ) =
      Polynomial.C (q : ℚ) * (Polynomial.X - Polynomial.C ((h : ℚ) / q)) := by
    rw [mul_sub, ← Polynomial.C_mul, mul_div_cancel₀ _ hq']
    simp
  apply (Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast _ _
    ((Polynomial.isPrimitive_C_mul_X_sub_C_of_isRelPrime hcop.symm.isRelPrime).pow t)).2
  rw [Polynomial.map_pow, hmap, mul_pow, ← Polynomial.C_pow,
    Polynomial.C_mul_dvd (pow_ne_zero _ hq')]
  exact Polynomial.pow_rootMultiplicity_dvd _ _

/-- If the leading coefficient of a nonzero `R ∈ ℤ[X]` has absolute value at most `B` and `h / q`,
with `h` coprime to `q > 0`, is a root of `R` of multiplicity `t`, then `q^t ≤ B`.
Source: §5, proof of Lemma 5 ("Comparing nonzero leading coefficients yields
`B ≥ |lc(R)| = q_1^t |lc(Q)| ≥ q_1^t`"). -/
theorem pow_rootMultiplicity_le {R : Polynomial ℤ} (hR : R ≠ 0) {h : ℤ} {q : ℕ} (hq : 0 < q)
    (hcop : IsCoprime h (q : ℤ)) {B : ℝ} (hB : |(R.leadingCoeff : ℝ)| ≤ B) :
    (q : ℝ) ^ Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) ≤ B := by
  obtain ⟨Q, hQ⟩ := exists_eq_pow_mul_of_rootMultiplicity hq hcop
  set t := Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ))
  have hlc : R.leadingCoeff = (q : ℤ) ^ t * Q.leadingCoeff := by
    rw [hQ, Polynomial.leadingCoeff_mul, Polynomial.leadingCoeff_pow, sub_eq_add_neg,
      ← Polynomial.C_neg, Polynomial.leadingCoeff_linear (by exact_mod_cast hq.ne')]
  have h1 : (1 : ℝ) ≤ |(Q.leadingCoeff : ℝ)| := by
    exact_mod_cast Int.one_le_abs (Polynomial.leadingCoeff_ne_zero.2
      (right_ne_zero_of_mul (hQ ▸ hR)))
  rw [hlc] at hB
  push_cast at hB
  rw [abs_mul, abs_pow, Nat.abs_cast] at hB
  exact (le_mul_of_one_le_right (by positivity) h1).trans hB

private lemma index_unique_le_log_div_aux [Unique σ] {B : ℝ} {q r : σ → ℕ} (hq : 1 < q default)
    {R : MvPolynomial σ ℤ} (hR : R ≠ 0) (hRB : |((uniqueAlgEquiv ℤ σ R).leadingCoeff : ℝ)| ≤ B)
    {h : σ → ℤ} (hh : IsCoprime (h default) (q default : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤
      Real.log B / (r default * Real.log (q default)) := by
  -- pass to the univariate polynomial `R1`; root multiplicities agree over `ℝ` and over `ℚ`
  let R1 : Polynomial ℤ := uniqueAlgEquiv ℤ σ R
  have hmapeq : uniqueAlgEquiv ℝ σ (map (Int.castRingHom ℝ) R) =
      R1.map (Int.castRingHom ℝ) := by
    dsimp only [R1]
    ext n
    rw [coeff_uniqueAlgEquiv, Polynomial.coeff_map, coeff_uniqueAlgEquiv, coeff_map]
  have hmult : Polynomial.rootMultiplicity ((h default : ℝ) / q default)
      (R1.map (Int.castRingHom ℝ)) =
      Polynomial.rootMultiplicity ((h default : ℚ) / q default) (R1.map (Int.castRingHom ℚ)) := by
    rw [Polynomial.eq_rootMultiplicity_map (f := Rat.castHom ℝ) Rat.cast_injective,
      Polynomial.map_map]
    congr 1
    simp
  -- the index is `t / r` (Lemma 4-2); bound `q^t ≤ B` and take logarithms
  rw [index_eq_rootMultiplicity_div, hmapeq, hmult]
  have hlog := Real.log_le_log (by positivity : (0 : ℝ) < (q default : ℝ) ^
    Polynomial.rootMultiplicity ((h default : ℚ) / q default) (R1.map (Int.castRingHom ℚ)))
    (pow_rootMultiplicity_le ((map_ne_zero_iff _ (uniqueAlgEquiv ℤ σ).injective).2 hR)
      (Nat.zero_lt_of_lt hq) hh hRB)
  rw [Real.log_pow] at hlog
  simpa [div_div, mul_comm] using
    div_le_div_of_nonneg_right
      ((le_div_iff₀ (Real.log_pos (by exact_mod_cast hq))).2 hlog) (Nat.cast_nonneg _)

/-- **Lemma 5**: in one variable, if `q > 1` then `Θ_1(B; q; r) ≤ log B / (r log q)`.
Source: §5, Lemma `roth:lem5` ("Suppose additionally that `q_1 > 1`. Then
`Θ_1(B; q_1; r_1) ≤ log B / (r_1 log q_1)`"), for a single variable `σ`. -/
theorem Θ_unique_le [Unique σ] {B : ℝ} (hB : 1 ≤ B) (q r : σ → ℕ) (hq : 1 < q default) :
    Θ B q r ≤ Real.log B / (r default * Real.log (q default)) :=
  Θ_le_of_forall_index_le hB fun _ hR _ hh ↦
    index_unique_le_log_div_aux hq hR.1
      (by simpa only [Polynomial.leadingCoeff, coeff_uniqueAlgEquiv] using hR.2.2 _) (hh default)

end Lemma5

section Lemma6

variable {τ : Type*} [Fintype τ]

/-- The constant `M = (r_1 + 1)^{p l} l! B^l 2^{p l r_1}` of Lemma 6. Source: §5, proof of
Lemma 6, eq. (16). -/
noncomputable def detCoeffBound (p r₁ : ℕ) (B : ℝ) (l : ℕ) : ℝ :=
  ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r₁)

/-- The quantity `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1})` of
Lemma 6. Source: §5, proof of Lemma 6, eq. (15). -/
noncomputable def ΘSplit (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ :=
  Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) + Θ M (q ∘ some) fun j ↦ l * r (some j)

/-- The quantity `Φ` of Lemma 6 is nonnegative. -/
theorem ΘSplit_nonneg (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : 0 ≤ ΘSplit q r M l :=
  add_nonneg (Θ_nonneg _ _ _) (Θ_nonneg _ _ _)

/-- The constant `M` of Lemma 6 is at least `1` when `B` is. Source: §5, proof of Lemma 6. -/
theorem one_le_detCoeffBound (p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) :
    1 ≤ detCoeffBound p r₁ B l := by
  rw [detCoeffBound]
  refine one_le_mul_of_one_le_of_one_le
    (one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le ?_ ?_)
      (one_le_pow₀ hB)) (one_le_pow₀ (by norm_num))
  · exact one_le_pow₀ (le_add_of_nonneg_left (Nat.cast_nonneg r₁))
  · exact_mod_cast Nat.factorial_pos l

private lemma mul_div_two_le_sum_max_aux {θ r : ℝ} (hθ : 0 ≤ θ) {l : ℕ} (hl : (l : ℝ) ≤ θ * r) :
    l * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) := by
  rcases Nat.eq_zero_or_pos l with rfl | hl0
  · simp
  have hr := pos_of_mul_pos_right ((Nat.cast_pos.mpr hl0).trans_le hl) hθ
  have hsum := congrArg (Nat.cast (R := ℝ)) (Finset.sum_range_id_mul_two l)
  push_cast [Nat.cast_sub hl0] at hsum
  refine le_trans ?_ (Finset.sum_le_sum fun ν _ ↦ le_max_right 0 (θ - ν / r))
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul,
    ← Finset.sum_div, le_sub_iff_add_le, div_add_div _ _ (by norm_num) hr.ne',
    div_le_iff₀ (by positivity)]
  linarith only [hsum, (Nat.cast_nonneg l : (0 : ℝ) ≤ l),
    mul_nonneg (Nat.cast_nonneg l) (sub_nonneg.mpr hl)]

private lemma mul_sq_div_three_le_sum_max_of_pos_aux {θ r : ℝ} (hr : 0 < r) (hθ : 0 ≤ θ) {l : ℕ}
    (hl : θ * r < l) : r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) := by
  set n := ⌊θ * r⌋₊
  have hnle : (n : ℝ) ≤ θ * r := Nat.floor_le (mul_nonneg hθ hr.le)
  have hnlt : θ * r < n + 1 := Nat.lt_floor_add_one _
  have hsum := congrArg (Nat.cast (R := ℝ)) (Finset.sum_range_id_mul_two (n + 1))
  push_cast [Nat.add_sub_cancel] at hsum
  have hbound : (θ * r) ^ 2 / 3 ≤ ∑ ν ∈ Finset.range (n + 1), (θ * r - ν) := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    push_cast
    generalize θ * r = a at hnle hnlt ⊢
    linear_combination hsum / 2 + sq_nonneg a / 6 + (le_trans (Nat.cast_nonneg n) hnle) / 2 +
      mul_nonneg (sub_nonneg.mpr hnle) (sub_nonneg.mpr hnlt.le) / 2
  calc
    r * θ ^ 2 / 3 = (θ * r) ^ 2 / 3 / r := (eq_div_iff hr.ne').2 (by ring)
    _ ≤ (∑ ν ∈ Finset.range (n + 1), (θ * r - ν)) / r :=
      (div_le_div_iff_of_pos_right hr).2 hbound
    _ ≤ ∑ ν ∈ Finset.range (n + 1), max 0 (θ - ν / r) := by
      simp only [Finset.sum_div, sub_div, mul_div_cancel_right₀ _ hr.ne']
      exact Finset.sum_le_sum fun ν _ ↦ le_max_right _ _
    _ ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) :=
      Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_subset_range.2
        ((Nat.floor_lt (mul_nonneg hθ hr.le)).2 hl))
        fun _ _ _ ↦ le_max_left _ _

/-- `min(lθ/2, r_p θ²/3) ≤ ∑_{ν<l} max(0, θ - ν/r_p)`.
Source: §5, proof of Lemma 6 ("Combining everything, we obtain
`∑_{ν<l} max(0, θ - ν/r_p) ≥ min(lθ/2, r_p θ²/3)`", the two cases `θ r_p < l` and
`θ r_p ≥ l`), for `θ r_p > 10`.
The inequality also holds without the source's positivity and size assumptions. -/
theorem min_le_sum_max (θ rp : ℝ) (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) := by
  have h0 : 0 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) :=
    Finset.sum_nonneg fun _ _ ↦ le_max_left _ _
  rcases le_or_gt θ 0 with hθ | hθ
  · exact (min_le_left _ _).trans (le_trans (by nlinarith [l.cast_nonneg (α := ℝ)]) h0)
  rcases le_or_gt (l : ℝ) (θ * rp) with hl | hl
  · exact (min_le_left _ _).trans (mul_div_two_le_sum_max_aux hθ.le hl)
  rcases le_or_gt rp 0 with hrp | hrp
  · exact (min_le_right _ _).trans (le_trans (by nlinarith [sq_nonneg θ]) h0)
  exact (min_le_right _ _).trans (mul_sq_div_three_le_sum_max_of_pos_aux hrp hθ.le hl)

/-- The index of the determinant `F = det (∂_{D_μ} ∂_{x_p}^ν R)_{μ,ν}` is at least
`∑_{ν<l} max(0, ind R - ν/r_p) - lδ`, where `δ` bounds the weights of the derivatives `D_μ`.
Source: §5, proof of Lemma 6 ("We have proved `ind(F) ≥ ∑_{ν<l} max(0, θ - ν/r_p) - lδ`"). -/
theorem sum_max_sub_le_index_det {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (hdet : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0) (α : Option τ → ℝ)
    {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ} (hw : ∀ μ, weight (r ∘ some) (D μ) ≤ δ) :
    ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤
      index (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by
  set E : Fin l → Fin l → MvPolynomial (Option τ) ℝ := fun μ ν ↦
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R
  -- each entry `Δ_{D μ + ν e_p} R` has index at least `max(0, ind R - ν/r_p) - δ`
  have hterm : ∀ μ ν : Fin l, E μ ν ≠ 0 →
      max 0 (index R α r - ν / r none) - δ ≤ index (E μ ν) α r := by
    intro μ ν hE
    have h1 := index_sub_weight_le_index_hasseDeriv hE α r
    rw [weight_add, weight_mapDomain, weight_single] at h1
    have h2 := hw μ
    refine sub_le_iff_le_add.2 (max_le ?_ (by linarith))
    linarith [index_nonneg (E μ ν) α r, weight_nonneg (r ∘ some) (D μ)]
  -- expand the determinant: a nonzero sum has index at least a common bound for its nonzero terms
  rw [Matrix.det_apply'] at hdet ⊢
  refine le_index_sum hdet fun s _ hs ↦ ?_
  have hprod : ∏ i, Matrix.of E (s i) i ≠ 0 := (mul_ne_zero_iff.mp hs).2
  have hentry (i : Fin l) : Matrix.of E (s i) i ≠ 0 :=
    (Finset.prod_ne_zero_iff.1 hprod) i (Finset.mem_univ _)
  -- the sign does not change the index, and the index of a product is the sum of the indices
  have hidx : index (((Equiv.Perm.sign s : ℤ) : MvPolynomial (Option τ) ℝ) *
      ∏ i, Matrix.of E (s i) i) α r = index (∏ i, Matrix.of E (s i) i) α r := by
    simpa only [map_intCast] using
      index_C_mul (Int.cast_ne_zero.2 (Units.ne_zero (Equiv.Perm.sign s)))
        (∏ i, Matrix.of E (s i) i) α r
  rw [hidx, index_prod _ (fun i _ ↦ hentry i) α hr,
    ← Fin.sum_univ_eq_sum_range (fun ν : ℕ ↦ max 0 (index R α r - ν / r none)) l]
  have hlδ : (l : ℝ) * δ = ∑ _i : Fin l, δ := by rw [Fin.sum_const, nsmul_eq_mul]
  rw [hlδ, ← Finset.sum_sub_distrib]
  exact Finset.sum_le_sum fun i _ ↦ hterm (s i) i (hentry i)

private lemma index_separated_mul_le_aux {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {q : Option τ → ℕ}
    {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {M : ℝ} {l : ℕ} (hl : 0 < l)
    {U : MvPolynomial τ ℤ} (hU : U ∈ boundedPolys M (fun j ↦ l * r (some j))) {V : Polynomial ℤ}
    (hV : V ≠ 0) (hVd : V.natDegree ≤ l * r none) (hVc : ∀ b, |(V.coeff b : ℝ)| ≤ M) :
    index (map (Int.castRingHom ℝ) (rename some U * V.toMvPolynomial none))
      (fun j ↦ (h j : ℝ) / q j) r ≤ l * ΘSplit q r M l := by
  -- view `V` as a polynomial in the single variable `Unit`, a member of the one-variable `ℛ`
  set V' : MvPolynomial Unit ℤ := (uniqueAlgEquiv ℤ Unit).symm V with hV'
  have hV'0 : V' ≠ 0 := by
    rwa [hV', ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective]
  have hVmem : V' ∈ boundedPolys M (fun _ : Unit ↦ l * r none) := by
    refine ⟨hV'0, fun j ↦ ?_, fun d ↦ ?_⟩
    · rw [Subsingleton.elim j default, hV', degreeOf_uniqueAlgEquiv_symm]
      exact hVd
    · rw [hV', MvPolynomial.coeff_uniqueAlgEquiv_symm]
      exact hVc _
  have hinjV : Function.Injective (fun _ : Unit ↦ (none : Option τ)) :=
    Function.injective_of_subsingleton _
  have hmU : map (Int.castRingHom ℝ) U ≠ 0 :=
    (map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hU.1
  have hmV : map (Int.castRingHom ℝ) V' ≠ 0 :=
    (map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hV'0
  -- the index of the product is the sum of the indices (Lemma 4-1), each computed in its own
  -- variables (Lemma 4-2)
  rw [toMvPolynomial_eq_rename, _root_.map_mul, map_rename, map_rename,
    index_mul ((map_ne_zero_iff (rename (R := ℝ) some)
      (rename_injective _ (Option.some_injective _))).2 hmU)
      ((map_ne_zero_iff (rename (R := ℝ) (fun _ : Unit ↦ (none : Option τ)))
        (rename_injective _ hinjV)).2 hmV) _ hr0,
    index_rename (Option.some_injective _), index_rename hinjV]
  -- bound each factor by the corresponding `Θ`, rescaling the weights by `l`
  have hUΘ := index_le_Θ hU (h := h ∘ some)
    fun j ↦ hh (some j)
  have hVΘ := index_le_Θ hVmem
    (q := fun _ : Unit ↦ q none) (h := fun _ ↦ h none) fun _ ↦ hh none
  rw [index_mul_left_weights] at hUΘ hVΘ
  have hlR : (0 : ℝ) < l := by exact_mod_cast hl
  rw [ΘSplit, mul_add, add_comm]
  exact add_le_add ((div_le_iff₀' hlR).1 hVΘ) ((div_le_iff₀' hlR).1 hUΘ)

/-- If the determinant `F = det (∂_{D_μ} ∂_{x_p}^ν R)_{μ,ν}` factors as
`U(x_1, …, x_{p-1}) V(x_p)` with suitably bounded degrees, then its index at `h/q` is at most
`l Φ`, where `Φ` is formed with the coefficient bound `M` of Lemma 6.
Source: §5, proof of Lemma 6, eq. (17) ("`ind F ≤ l Φ`"). -/
theorem index_det_le {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁)
    {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ}
    (hRd : ∀ j, degreeOf j R ≤ r j) (hRc : ∀ d, |(R.coeff d : ℝ)| ≤ B)
    {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ} (hl : 1 ≤ l)
    {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0)
    (hUd : ∀ j, degreeOf j U ≤ l * r (some j)) (hVd : V.natDegree ≤ l * r none)
    (hF : (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      rename some U * V.toMvPolynomial none) :
    index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)
      (fun j ↦ (h j : ℝ) / q j) r ≤
        l * ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l := by
  -- Step 1: the coefficients of `F` are bounded by `M`.
  have hFcoef (d) : |((Matrix.of fun μ ν : Fin l ↦ hasseDeriv
      ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det.coeff d : ℝ)| ≤
      detCoeffBound (Fintype.card τ + 1) r₁ B l := by
    simpa only [detCoeffBound, Finset.prod_const, Finset.sum_const, Finset.card_univ,
      Fintype.card_option, nsmul_eq_mul, Nat.cast_id, pow_mul, mul_right_comm] using
      abs_coeff_det_hasseDeriv_le _ R (r := fun _ ↦ r₁) (fun j ↦ (hRd j).trans (hr₁ j)) hRc d
  -- Step 2: the coefficients of `U` and `V` are bounded by `M`.
  have hUc : ∀ a, |(U.coeff a : ℝ)| ≤ detCoeffBound (Fintype.card τ + 1) r₁ B l := fun a ↦ by
    have h1 := hFcoef (a.optionElim V.natDegree)
    rw [hF, coeff_rename_mul_toMvPolynomial, Int.cast_mul, abs_mul] at h1
    exact (le_mul_of_one_le_right (abs_nonneg _) (by
      exact_mod_cast Int.one_le_abs (Polynomial.leadingCoeff_ne_zero.2 hV))).trans h1
  have hVc : ∀ b, |(V.coeff b : ℝ)| ≤ detCoeffBound (Fintype.card τ + 1) r₁ B l := fun b ↦ by
    obtain ⟨a₀, ha₀⟩ := MvPolynomial.ne_zero_iff.1 hU
    have h1 := hFcoef (a₀.optionElim b)
    rw [hF, coeff_rename_mul_toMvPolynomial, Int.cast_mul, abs_mul] at h1
    exact (le_mul_of_one_le_left (abs_nonneg _) (by
      exact_mod_cast Int.one_le_abs ha₀)).trans h1
  -- Step 3: Lemma 4-2, the index of the product of polynomials in separate variables.
  rw [hF]
  exact index_separated_mul_le_aux hr0 hh hl ⟨hU, hUd, hUc⟩ hV hVd hVc

private lemma weight_le_delta_aux {δ : ℝ} (hδ : 0 ≤ δ) {r : Option τ → ℕ}
    (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {d : τ →₀ ℕ} (hd : d.degree ≤ r none) :
    weight (r ∘ some) d ≤ δ := by
  by_cases hr : r none = 0
  · rw [(Finsupp.degree_eq_zero_iff d).1 (Nat.eq_zero_of_le_zero (hr ▸ hd))]
    simpa [weight] using hδ
  have hrp : (0 : ℝ) < r none := by exact_mod_cast Nat.pos_of_ne_zero hr
  calc weight (r ∘ some) d = ∑ j, (d j : ℝ) / r (some j) := rfl
    _ ≤ ∑ j, (d j : ℝ) * δ / r none := Finset.sum_le_sum fun j _ ↦ by
        rw [div_le_div_iff₀ (pos_of_mul_pos_right (hrp.trans_le (hratio j)) hδ) hrp, mul_assoc]
        exact mul_le_mul_of_nonneg_left (hratio j) (Nat.cast_nonneg _)
    _ = δ * d.degree / r none := by
        rw [← Finset.sum_div, ← Finset.sum_mul, Finsupp.degree_eq_sum, Nat.cast_sum, mul_comm]
    _ ≤ δ := (div_le_iff₀ hrp).2 (mul_le_mul_of_nonneg_left (by exact_mod_cast hd) hδ)

omit [Fintype τ] in
private lemma mapped_det_ne_zero_aux {R : MvPolynomial (Option τ) ℤ} {l : ℕ} {D : Fin l → (τ →₀ ℕ)}
    {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0)
    (hF : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
        rename some U * V.toMvPolynomial none) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +
      Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det ≠ 0 := by
  have hmapdet : map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +
        Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det := by
    simp [RingHom.map_det, RingHom.mapMatrix_apply, Matrix.map]
  rw [← hmapdet, ne_eq, map_eq_zero_iff _ (map_injective _ Int.cast_injective), hF,
    mul_eq_zero, not_or, map_eq_zero_iff _ (rename_injective _ (Option.some_injective _))]
  exact ⟨hU, (map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective none)).2 hV⟩

private lemma le_two_mul_add_sqrt_add_sqrt_of_min_le_aux {θ Φ δ rp l : ℝ} (hΦ : 0 ≤ Φ)
    (hδ1 : δ ≤ 1) (hrp : 3 ≤ rp) (hl : 0 < l) (hl' : l ≤ rp + 1)
    (hmin : min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ l * (Φ + δ)) :
    θ ≤ 2 * (Φ + √Φ + √δ) := by
  -- the small-index comparison `δ ≤ √δ` also controls the linear bound
  rcases min_le_iff.1 hmin with hk | hk
  · nlinarith [Real.le_sqrt_self_iff.2 hδ1, Real.sqrt_nonneg Φ]
  · have hsq : θ ^ 2 ≤ 4 * (Φ + δ) := by nlinarith [sq_nonneg θ]
    nlinarith [Real.sq_sqrt hΦ, Real.sqrt_nonneg Φ, Real.sqrt_nonneg δ,
      (le_max_left δ 0).trans_eq (Real.sq_sqrt').symm,
      mul_nonneg (Real.sqrt_nonneg Φ) (Real.sqrt_nonneg δ)]

/-- **Lemma 6**, for one polynomial and one point: the index of `R ∈ ℛ_p(B; r)` at `h/q` is at
most `2(Φ + Φ^{1/2} + δ^{1/2})` for some `1 ≤ l ≤ r_p + 1`. Source: §5, Lemma `roth:lem6` and
its proof ("We need to show that the index `ind(R; h/q; r)` is bounded by the right hand side
of (13)"). -/
theorem exists_index_le_two_mul_ΘSplit_add_sqrt {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1)
    {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j))
    {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ}
    {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ boundedPolys B r) {h : Option τ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤
        2 * (ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l +
          √(ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  have hrp0 : (0 : ℝ) < r none := (by norm_num : (0 : ℝ) < 3).trans_le hrp
  have hr0 : ∀ j, 0 < r j := fun j ↦ by
    cases j with
    | none => exact_mod_cast hrp0
    | some j => exact_mod_cast pos_of_mul_pos_right (hrp0.trans_le (hratio j)) hδ0
  obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1
  refine ⟨l, hl, hl', ?_⟩
  let α : Option τ → ℝ := fun j ↦ (h j : ℝ) / q j
  let Φ := ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l
  -- The two bounds for the index of `F`.
  have hlower := sum_max_sub_le_index_det D (mapped_det_ne_zero_aux hU hV hF) α hr0
    (fun μ ↦ weight_le_delta_aux hδ0 hratio ((hD μ).trans (Nat.le_of_lt_succ (μ.2.trans_le hl'))))
  have hupper := index_det_le hr0 hr₁ hR.2.1 hR.2.2 hh hl hU hV hUd hVd hF
  simp only [RingHom.map_det, RingHom.mapMatrix_apply, Matrix.map, Matrix.of_apply] at hupper
  simp only [hasseDeriv_map] at hlower
  -- Both summands of `Φ` are nonnegative.
  apply le_two_mul_add_sqrt_add_sqrt_of_min_le_aux (Φ := Φ) (l := (l : ℝ)) (ΘSplit_nonneg _ _ _ _)
    hδ1 hrp (by exact_mod_cast hl) (by exact_mod_cast hl')
  exact (min_le_sum_max (index (map (Int.castRingHom ℝ) R) α r) (r none) l).trans
    (by simpa only [mul_add] using sub_le_iff_le_add.1 (hlower.trans hupper))

/-- **Lemma 6**: `Θ_p(B; q; r)` is at most twice the maximum of `Φ + Φ^{1/2} + δ^{1/2}` over
`1 ≤ l ≤ r_p + 1`. Source: §5, Lemma `roth:lem6` ("`Θ_p(B; q; r) ≤ 2 max_l (Φ + Φ^{1/2} + δ^{1/2})`,
where the maximum is taken over integers `l` satisfying `1 ≤ l ≤ r_p + 1`"). -/
theorem Θ_option_le {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ))
    (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁)
    (q : Option τ → ℕ) (B : ℝ) :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (Nat.le_add_left 1 _))
      (fun l ↦ ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l +
        √(ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  set f := fun l ↦ ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l +
    √(ΘSplit q r (detCoeffBound (Fintype.card τ + 1) r₁ B l) l) + √δ
  refine Real.sSup_le ?_ ?_
  · rintro _ ⟨R, hR, h, hh, rfl⟩
    obtain ⟨l, hl, hl', hle⟩ := exists_index_le_two_mul_ΘSplit_add_sqrt hδ0 hδ1 hrp hratio hr₁ hR hh
    exact hle.trans (mul_le_mul_of_nonneg_left
      (Finset.le_sup' f (Finset.mem_Icc.2 ⟨hl, hl'⟩)) (by norm_num))
  · have h1 : 0 ≤ f 1 :=
      add_nonneg (add_nonneg (ΘSplit_nonneg _ _ _ _) (Real.sqrt_nonneg _)) (Real.sqrt_nonneg _)
    exact mul_nonneg (by norm_num) (h1.trans (Finset.le_sup' f
      (Finset.left_mem_Icc.2 (Nat.le_add_left 1 _))))

end Lemma6

section Lemma7

private lemma factorial_coefficient_le_two_pow_aux (p r₁ l : ℕ) (hl : l ≤ 2 ^ r₁) :
    (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤ 2 ^ ((2 * p + 1) * r₁ * l) := by
  calc
    (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁)
        ≤ (2 ^ r₁) ^ (p * l) * (2 ^ r₁) ^ l * 2 ^ (p * l * r₁) := by
          gcongr
          · exact Nat.lt_two_pow_self
          · exact (Nat.factorial_le_pow l).trans (Nat.pow_le_pow_left hl _)
    _ = 2 ^ ((2 * p + 1) * r₁ * l) := by ring

private lemma two_pow_lt_rpow_aux {p r₁ l : ℕ} (hp : 0 < p) {δ q : ℝ} (hδ : 0 < δ) (hq : 0 < q)
    (hlog : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q) (hlr : 0 < l * r₁) :
    (2 : ℝ) ^ ((2 * p + 1) * r₁ * l) < q ^ (δ / p * (l * r₁)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp
  have hlog2 : Real.log 2 < 1 :=
    (Real.log_lt_sub_one_of_pos two_pos (by norm_num)).trans_eq (by norm_num)
  have h3 : (2 * p + 1 : ℝ) ≤ Real.log q * (δ / p) := by
    rw [mul_div_assoc', le_div_iff₀ hp0]
    rw [div_le_iff₀ hδ] at hlog
    linarith
  rw [← Real.rpow_natCast, Real.rpow_def_of_pos (by norm_num), Real.rpow_def_of_pos hq,
    Real.exp_lt_exp]
  calc
    Real.log 2 * (((2 * p + 1) * r₁ * l : ℕ) : ℝ)
        = Real.log 2 * (2 * p + 1) * (l * r₁) := by
          push_cast
          ring
    _ < Real.log q * (δ / p) * (l * r₁) :=
      mul_lt_mul_of_pos_right
        ((mul_lt_of_lt_one_left (by positivity) hlog2).trans_le h3) (by exact_mod_cast hlr)
    _ = Real.log q * (δ / p * (l * r₁)) := by ring

/-- For `log q_1 ≥ p (2p + 1) / δ`, `p > 0` and `1 ≤ l ≤ r_1`, the constant `M` of Lemma 6 with
`B = q_1^{δ r_1}` satisfies `M < q_1^{δ (1 + 1/p) l r_1}`.
Source: §5, proof of Lemma 7 ("`M < q_1^{δ_1 l r_1}` with `δ_1 = δ(1 + p⁻¹)`"). -/
theorem detCoeffBound_lt_rpow {p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ q₁ : ℕ}
    (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) :
    detCoeffBound p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp
  have hq1pos : (0 : ℝ) < q₁ := zero_lt_one.trans <|
    (Real.log_pos_iff (Nat.cast_nonneg q₁)).1 <| lt_of_lt_of_le (by positivity) hq₁
  -- the factors other than `B^l` are at most `2^{(2p+1) r₁ l}`
  have hnatR : ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤
      2 ^ ((2 * p + 1) * r₁ * l) := by
    exact_mod_cast factorial_coefficient_le_two_pow_aux p r₁ l (hl'.trans Nat.lt_two_pow_self.le)
  calc
    detCoeffBound p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l = ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial *
        2 ^ (p * l * r₁) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l := by
          rw [detCoeffBound]
          ring
    _ ≤ 2 ^ ((2 * p + 1) * r₁ * l) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l :=
      mul_le_mul_of_nonneg_right hnatR (by positivity)
    _ < (q₁ : ℝ) ^ (δ / p * (l * r₁)) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l :=
      mul_lt_mul_of_pos_right
        (two_pow_lt_rpow_aux hp hδ0 hq1pos hq₁ (Nat.mul_pos (by lia) (by lia))) (by positivity)
    _ = (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by
      rw [← Real.rpow_mul_natCast hq1pos.le, ← Real.rpow_add hq1pos]
      congr 1
      ring

/-- For `p = k + 1 ≥ 2` and `0 < δ ≤ 1`, with `δ_1 = δ (1 + 1/p)`,
`δ_1 + 10^{p-1} δ_1^{(1/2)^{p-1}} < 3 · 10^{p-1} δ^{(1/2)^{p-1}}`.
Source: §5, proof of Lemma 7 ("`Φ < δ_1 + 10^{p-1} δ_1^{(1/2)^{p-1}} < 2δ + 2 · 10^{p-1}
δ^{(1/2)^{p-1}} < 3 · 10^{p-1} δ^{(1/2)^{p-1}}`"). -/
theorem mul_add_pow_mul_rpow_lt {k : ℕ} (hk : 1 ≤ k) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) :
    δ * (1 + 1 / ((k : ℝ) + 1)) + 10 ^ k * (δ * (1 + 1 / ((k : ℝ) + 1))) ^ ((1 / 2 : ℝ) ^ k) <
      3 * 10 ^ k * δ ^ ((1 / 2 : ℝ) ^ k) := by
  set e : ℝ := (1 / 2 : ℝ) ^ k
  have he1 : e ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  have hp : (2 : ℝ) ≤ (k : ℝ) + 1 := by exact_mod_cast Nat.succ_le_succ hk
  have hc1 : 1 ≤ 1 + 1 / ((k : ℝ) + 1) := le_add_of_nonneg_right (by positivity)
  have hc2 : 1 + 1 / ((k : ℝ) + 1) ≤ 3 / 2 := by
    linarith [one_div_le_one_div_of_le (by norm_num : (0 : ℝ) < 2) hp]
  have hδe : δ ≤ δ ^ e := by
    simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1 he1
  have hde0 : 0 < δ ^ e := Real.rpow_pos_of_pos hδ0 e
  have hmul : (δ * (1 + 1 / ((k : ℝ) + 1))) ^ e ≤ δ ^ e * (3 / 2) := by
    rw [Real.mul_rpow hδ0.le (zero_le_one.trans hc1)]
    refine mul_le_mul_of_nonneg_left ?_ hde0.le
    calc (1 + 1 / ((k : ℝ) + 1)) ^ e ≤ (1 + 1 / ((k : ℝ) + 1)) ^ (1 : ℝ) :=
          Real.rpow_le_rpow_of_exponent_le hc1 he1
      _ ≤ 3 / 2 := by simpa using hc2
  linear_combination mul_le_mul hδe hc2 (zero_le_one.trans hc1) hde0.le +
    mul_le_mul_of_nonneg_left hmul (by positivity : (0 : ℝ) ≤ 10 ^ k) +
    (3 / 2) * mul_le_mul_of_nonneg_right
      (le_self_pow₀ (by norm_num : (1 : ℝ) ≤ 10) (by lia : k ≠ 0)) hde0.le +
    (27 / 2) * hde0

/-- If `Φ ≤ 3 · 10^{p-1} δ^{(1/2)^{p-1}}` with `p = k + 1 ≥ 2` and `0 < δ ≤ 1`, then
`2(Φ + Φ^{1/2} + δ^{1/2}) < 10^p δ^{(1/2)^p}`.
The bound also allows negative `Φ` and equality in both upper hypotheses.
Source: §5, proof of Lemma 7 ("Set `a = δ^{2^{-p}}` ... `Θ_p < 2(3·10^{p-1} a² + √3 10^{(p-1)/2}
a + δ^{1/2}) ≤ ... < 10^p a`"). -/
theorem two_mul_add_sqrt_add_sqrt_lt {k : ℕ} (hk : 1 ≤ k) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1)
    {Φ : ℝ} (hΦ : Φ ≤ 3 * 10 ^ k * δ ^ ((1 / 2 : ℝ) ^ k)) :
    2 * (Φ + √Φ + √δ) < 10 ^ (k + 1) * δ ^ ((1 / 2 : ℝ) ^ (k + 1)) := by
  -- with `a = δ^{(1/2)^p}` and `T = 10^{p-1}`: `Φ ≤ 3 T a²`, `√Φ < T a`, `√δ ≤ a` and `a² ≤ a`
  set a := δ ^ ((1 / 2 : ℝ) ^ (k + 1)) with ha
  set T : ℝ := 10 ^ k with hT
  have ha0 : 0 < a := Real.rpow_pos_of_pos hδ0 _
  have ha2 : a ^ 2 = δ ^ ((1 / 2 : ℝ) ^ k) := by
    rw [ha, ← Real.rpow_mul_natCast hδ0.le, pow_succ]
    congr 1
    push_cast
    ring
  have hsqrt : √δ ≤ a := by
    rw [Real.sqrt_eq_rpow, ha]
    refine Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1 ?_
    rw [pow_succ]
    exact mul_le_of_le_one_left (by norm_num) (pow_le_one₀ (by norm_num) (by norm_num))
  have hT10 : (10 : ℝ) ≤ T := le_self_pow₀ (by norm_num) (by lia : k ≠ 0)
  rw [← ha2] at hΦ
  have hsΦ : √Φ < T * a := by
    refine (Real.sqrt_lt' (by positivity)).2 (hΦ.trans_lt ?_)
    rw [mul_pow, pow_two T]
    exact mul_lt_mul_of_pos_right (mul_lt_mul_of_pos_right
      ((by norm_num : (3 : ℝ) < 10).trans_le hT10) (by positivity)) (sq_pos_of_pos ha0)
  have haa : a ^ 2 ≤ a := by
    simpa only [pow_two, mul_one] using mul_le_mul_of_nonneg_left
      (Real.rpow_le_one hδ0.le hδ1 (pow_nonneg (by norm_num) _)) ha0.le
  rw [pow_succ, ← hT, mul_comm T]
  linear_combination 2 * hΦ.trans
    (mul_le_mul_of_nonneg_left haa (by positivity : 0 ≤ 3 * T)) + 2 * hsΦ +
    2 * hsqrt.trans (le_mul_of_one_le_left ha0.le ((by norm_num : (1 : ℝ) ≤ 10).trans hT10))

private lemma Θ_scaled_unique_le_aux {δ M : ℝ} {q₁ q₂ r₁ r₂ l : ℕ} (hq₁ : 1 < q₁) (hr₁ : 0 < r₁)
    (hl : 0 < l) (hqr : (r₁ : ℝ) * Real.log q₁ ≤ r₂ * Real.log q₂) (hM1 : 1 ≤ M)
    (hM : M ≤ (q₁ : ℝ) ^ (δ * (l * r₁))) : Θ M (fun _ : Unit ↦ q₂) (fun _ ↦ l * r₂) ≤ δ := by
  have hδ0 : 0 ≤ δ := by
    have h : (0 : ℝ) ≤ δ * (l * r₁) :=
      (Real.rpow_le_rpow_left_iff (x := (q₁ : ℝ)) (by exact_mod_cast hq₁)).1
        (by simpa using hM1.trans hM)
    exact nonneg_of_mul_nonneg_left h
      (mul_pos (by exact_mod_cast hl : (0 : ℝ) < l)
        (by exact_mod_cast hr₁ : (0 : ℝ) < r₁))
  have hL : (0 : ℝ) < r₂ * Real.log q₂ :=
    (mul_pos (by exact_mod_cast hr₁) (Real.log_pos (by exact_mod_cast hq₁))).trans_le hqr
  have hL₂ : 0 < Real.log (q₂ : ℝ) := pos_of_mul_pos_right hL (Nat.cast_nonneg r₂)
  have hr₂ : 0 < r₂ := by exact_mod_cast pos_of_mul_pos_left hL hL₂.le
  have hq₂ : 1 < q₂ := by
    exact_mod_cast (Real.log_pos_iff (Nat.cast_nonneg q₂)).1 hL₂
  refine (Θ_mono hM _ _).trans ((Θ_unique_le (hM1.trans hM) _ _ hq₂).trans ?_)
  rw [Real.log_rpow (by positivity), div_le_iff₀ (by
    push_cast
    exact mul_pos (mul_pos (by exact_mod_cast hl) (by exact_mod_cast hr₂)) hL₂)]
  push_cast
  nlinarith only [mul_le_mul_of_nonneg_left hqr (mul_nonneg hδ0 (Nat.cast_nonneg l))]

private lemma Θ_prefix_lt_aux {n : ℕ} {δ ε M : ℝ} (hδ0 : 0 < δ) (hδε : δ ≤ ε)
    {r q : Fin (n + 2) → ℕ} (hanti : ∀ j, r (Fin.last (n + 1)) ≤ r j)
    (hrlast : 3 ≤ (r (Fin.last (n + 1)) : ℝ))
    (hratio : ∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc)
    (hq1 : ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0))
    (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) {l : ℕ} (hl : 1 ≤ l)
    (hM : M ≤ (q 0 : ℝ) ^ (ε * (l * r 0)))
    (ih : ∀ {r q : Fin (n + 1) → ℕ}, 3 ≤ (r (Fin.last n) : ℝ) →
      (∀ i : Fin n, (r i.succ : ℝ) ≤ ε * r i.castSucc) →
      ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / ε ≤ Real.log (q 0) →
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) →
      Θ ((q 0 : ℝ) ^ (ε * r 0)) q r < 10 ^ (n + 1) * ε ^ ((1 / 2 : ℝ) ^ (n + 1))) :
    Θ M (fun j : Fin (n + 1) ↦ q j.castSucc) (fun j ↦ l * r j.castSucc) <
      10 ^ (n + 1) * ε ^ ((1 / 2 : ℝ) ^ (n + 1)) := by
  refine (Θ_mono hM _ _).trans_lt ?_
  have hCeq : (q 0 : ℝ) ^ (ε * (l * r 0)) =
      (q (Fin.castSucc 0) : ℝ) ^ (ε * ((l * r (Fin.castSucc 0) : ℕ) : ℝ)) := by
    simp [Nat.cast_mul]
  rw [hCeq]
  have hn : (0 : ℝ) ≤ n + 1 + 1 := by positivity
  refine ih (r := fun j ↦ l * r j.castSucc) (q := fun j ↦ q j.castSucc) ?_ ?_
    ((div_le_div₀ (mul_nonneg hn (add_nonneg (mul_nonneg (by norm_num) hn) zero_le_one)) (by
      linarith only [Nat.cast_nonneg (α := ℝ) n]) hδ0 hδε).trans hq1) ?_
  · have h2 : (r (Fin.last (n + 1)) : ℝ) ≤ r (Fin.castSucc (Fin.last n)) := by
      exact_mod_cast hanti _
    push_cast
    exact hrlast.trans (h2.trans
      (le_mul_of_one_le_left (Nat.cast_nonneg _) (by exact_mod_cast hl)))
  · intro i
    push_cast
    calc
      (l : ℝ) * r (Fin.castSucc i.succ) ≤ l * (δ * r (Fin.castSucc (Fin.castSucc i))) :=
        mul_le_mul_of_nonneg_left (hratio (Fin.castSucc i)) (Nat.cast_nonneg l)
      _ = δ * (l * r (Fin.castSucc (Fin.castSucc i))) := mul_left_comm _ _ _
      _ ≤ ε * (l * r (Fin.castSucc (Fin.castSucc i))) :=
        mul_le_mul_of_nonneg_right hδε (mul_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _))
  · intro j
    push_cast
    simpa only [mul_assoc, Fin.castSucc_zero] using
      mul_le_mul_of_nonneg_left (hqr j.castSucc) (Nat.cast_nonneg l)

private lemma Θ_lt_base_aux {δ : ℝ} (hδ0 : 0 < δ) (hδ : δ ≤ 1) {r q : Fin 1 → ℕ}
    (hrlast : 0 < r 0) (hq1 : 1 < q 0) :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ 1 * δ ^ ((1 / 2 : ℝ) ^ 1) := by
  have h : Θ ((q 0 : ℝ) ^ (δ * r 0)) q r ≤ δ := by
    refine (Θ_unique_le (Real.one_le_rpow (by exact_mod_cast hq1.le) (by positivity)) q r
      hq1).trans_eq ?_
    rw [Subsingleton.elim (default : Fin 1) 0, Real.log_rpow (by positivity)]
    field_simp [ne_of_gt (by exact_mod_cast hrlast : (0 : ℝ) < r 0),
      ne_of_gt (Real.log_pos (by exact_mod_cast hq1 : (1 : ℝ) < q 0))]
  have h1 : δ ≤ δ ^ ((1 / 2 : ℝ) ^ 1) := by
    simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ (by norm_num : (1 / 2 : ℝ) ^ 1 ≤ 1)
  norm_num only [pow_one] at h1 ⊢
  exact h.trans_lt (h1.trans_lt
    (lt_mul_of_one_lt_left (Real.rpow_pos_of_pos hδ0 _) (by norm_num : (1 : ℝ) < 10)))

private lemma one_lt_of_mul_log_le_aux {n : ℕ} {r q : Fin (n + 1) → ℕ} (hrlast : 0 < r 0)
    (hq1 : 0 < Real.log (q 0)) (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j))
    (j : Fin (n + 1)) : 1 < q j := by
  exact_mod_cast (Real.log_pos_iff (Nat.cast_nonneg (q j))).1
    (pos_of_mul_pos_right
      ((mul_pos (by exact_mod_cast hrlast) hq1).trans_le (hqr j)) (Nat.cast_nonneg _))

private lemma Θ_phi_lt_aux {n : ℕ} {δ : ℝ} (hδ0 : 0 < δ)
    (hδ1 : δ < 1) {r q : Fin (n + 2) → ℕ} (hanti : Antitone r)
    (hrlast : 3 ≤ (r (Fin.last (n + 1)) : ℝ))
    (hratio : ∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc)
    (hq1 : ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0))
    (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j))
    (ih : ∀ {δ : ℝ}, 0 < δ → ∀ {r q : Fin (n + 1) → ℕ}, 3 ≤ (r (Fin.last n) : ℝ) →
      (∀ i : Fin n, (r i.succ : ℝ) ≤ δ * r i.castSucc) →
      ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ ≤ Real.log (q 0) →
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) →
      Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))) {l : ℕ}
    (hl : l ∈ Finset.Icc 1 (r (Fin.last (n + 1)) + 1)) :
    let M := detCoeffBound (n + 2) (r 0) ((q 0 : ℝ) ^ (δ * r 0)) l
    let Φ := Θ M (fun _ : Unit ↦ q (Fin.last (n + 1))) (fun _ ↦ l * r (Fin.last (n + 1))) +
      Θ M (fun j : Fin (n + 1) ↦ q j.castSucc) (fun j ↦ l * r j.castSucc)
    Φ + √Φ + √δ < (10 ^ (n + 2) * δ ^ ((1 / 2 : ℝ) ^ (n + 2))) / 2 := by
  dsimp only
  obtain ⟨hl1, hl2⟩ := Finset.mem_Icc.1 hl
  have hr0 : ∀ j, 0 < r j := fun j ↦ by
    have h : (3 : ℝ) ≤ r j := hrlast.trans (by exact_mod_cast hanti (Fin.le_last j))
    exact_mod_cast (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 3) h)
  have hq := one_lt_of_mul_log_le_aux (hr0 0) (lt_of_lt_of_le (by positivity) hq1) hqr 0
  let ε : ℝ := δ * (1 + 1 / ((n : ℝ) + 1 + 1))
  have hε0 : 0 < ε := mul_pos hδ0 (by positivity)
  let M := detCoeffBound (n + 2) (r 0) ((q 0 : ℝ) ^ (δ * r 0)) l
  have hM1 : 1 ≤ M := one_le_detCoeffBound _ _
    (Real.one_le_rpow (by exact_mod_cast hq.le) (mul_nonneg hδ0.le (Nat.cast_nonneg _))) l
  have hM : M < (q 0 : ℝ) ^ (ε * (l * r 0)) := by
    simpa only [ε, Nat.cast_add, Nat.cast_one] using
      detCoeffBound_lt_rpow (p := n + 1 + 1) (Nat.zero_lt_succ _) hδ0
      (by simpa only [Nat.cast_add, Nat.cast_one] using hq1) hl1
      (hl2.trans (Nat.succ_le_of_lt ((hanti (Fin.le_last _)).trans_lt (by
        exact_mod_cast (hratio 0).trans_lt
          (mul_lt_of_lt_one_left (by exact_mod_cast hr0 0) hδ1)))))
  have hb := mul_add_pow_mul_rpow_lt (k := n + 1) (Nat.succ_le_succ (Nat.zero_le n)) hδ0 hδ1.le
  simp only [Nat.cast_add, Nat.cast_one] at hb
  apply (lt_div_iff₀' (by norm_num : (0 : ℝ) < 2)).2
  apply two_mul_add_sqrt_add_sqrt_lt (Nat.succ_le_succ (Nat.zero_le n)) hδ0 hδ1.le
  -- combine
  exact (lt_of_lt_of_le (add_lt_add_of_le_of_lt
    -- the one-variable term
    (Θ_scaled_unique_le_aux hq (hr0 0) hl1
      (hqr (Fin.last (n + 1))) hM1 hM.le)
    -- the `(p - 1)`-variable term, by the induction hypothesis
    (Θ_prefix_lt_aux hδ0
      (le_mul_of_one_le_right hδ0.le (le_add_of_nonneg_right (by positivity)))
      (fun j ↦ hanti (Fin.le_last j)) hrlast hratio hq1 hqr hl1 hM.le (ih hε0))) hb.le).le

private lemma Θ_lt_succ_aux {n : ℕ} {δ : ℝ} (hδ0 : 0 < δ) (hδ : δ ≤ 1 / ((n : ℝ) + 1 + 1))
    {r q : Fin (n + 2) → ℕ} (hrlast : 3 ≤ (r (Fin.last (n + 1)) : ℝ))
    (hratio : ∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc)
    (hq1 : ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0))
    (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j))
    (ih : ∀ {δ : ℝ}, 0 < δ → ∀ {r q : Fin (n + 1) → ℕ}, 3 ≤ (r (Fin.last n) : ℝ) →
      (∀ i : Fin n, (r i.succ : ℝ) ≤ δ * r i.castSucc) →
      ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ ≤ Real.log (q 0) →
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) →
      Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))) :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 2) * δ ^ ((1 / 2 : ℝ) ^ (n + 2)) := by
  have hδ1 : δ < 1 := hδ.trans_lt ((div_lt_one (by positivity)).2
    (by linarith only [Nat.cast_nonneg (α := ℝ) n]))
  have hanti : Antitone r := Fin.antitone_iff_succ_le.2 fun i ↦ by
    exact_mod_cast (hratio i).trans (mul_le_of_le_one_left (Nat.cast_nonneg _) hδ1.le)
  have hratio' : ∀ j : Fin (n + 1),
      (r (Fin.last (n + 1)) : ℝ) ≤ δ * r j.castSucc := fun j ↦ by
    have h := hratio (Fin.last n)
    rw [Fin.succ_last] at h
    exact h.trans (mul_le_mul_of_nonneg_left
      (by exact_mod_cast hanti (Fin.castSucc_le_castSucc_iff.2 (Fin.le_last j))) hδ0.le)
  -- transport to `Option (Fin (n + 1))`
  let e : Fin (n + 2) ≃ Option (Fin (n + 1)) := finSuccEquivLast
  rw [← Θ_equiv e.symm ((q 0 : ℝ) ^ (δ * r 0)) q r]
  refine (Θ_option_le (τ := Fin (n + 1)) hδ0.le hδ1.le (r := r ∘ e.symm)
    (by simpa only [Function.comp_apply, e, finSuccEquivLast_symm_none] using hrlast)
    (fun j ↦ by simpa only [Function.comp_apply, e, finSuccEquivLast_symm_none,
      finSuccEquivLast_symm_some] using hratio' j)
    (r₁ := r 0) (fun j ↦ hanti (Fin.zero_le _)) (q ∘ e.symm) _).trans_lt ?_
  simp only [ΘSplit, e, Function.comp_def, finSuccEquivLast_symm_none,
    finSuccEquivLast_symm_some, Fintype.card_fin]
  rw [← lt_div_iff₀' (by norm_num : (0 : ℝ) < 2), Finset.sup'_lt_iff]
  exact fun l hl ↦ Θ_phi_lt_aux hδ0 hδ1 hanti hrlast hratio hq1 hqr ih hl

private lemma Θ_lt_of_large_delta_aux {n : ℕ} {δ : ℝ} (hδ : 1 / ((n : ℝ) + 1) ≤ δ)
    {r q : Fin (n + 1) → ℕ} :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1)) := by
  have hp : (0 : ℝ) < n + 1 := by positivity
  have hp2 : (n : ℝ) + 1 < (2 : ℝ) ^ (n + 1) := by exact_mod_cast Nat.lt_two_pow_self
  calc
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r ≤ (n : ℝ) + 1 := by
      simpa using Θ_le_card _ q r
    _ < 10 ^ (n + 1) / ((n : ℝ) + 1) :=
      (lt_div_iff₀ hp).2 <| calc
        ((n : ℝ) + 1) * ((n : ℝ) + 1) < (2 : ℝ) ^ (n + 1) * 2 ^ (n + 1) :=
          mul_self_lt_mul_self hp.le hp2
        _ = (4 : ℝ) ^ (n + 1) := by
          rw [← mul_pow]
          norm_num
        _ ≤ (10 : ℝ) ^ (n + 1) := pow_le_pow_left₀ (by norm_num) (by norm_num) _
    _ = 10 ^ (n + 1) * (1 / ((n : ℝ) + 1)) := (mul_one_div _ _).symm
    _ ≤ 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1)) :=
      mul_le_mul_of_nonneg_left
        ((Real.self_le_rpow_of_le_one (by positivity)
          ((div_le_one hp).2 (by linarith only [Nat.cast_nonneg (α := ℝ) n]))
          (pow_le_one₀ (by norm_num : (0 : ℝ) ≤ 1 / 2) (by norm_num))).trans
          (Real.rpow_le_rpow (by positivity) hδ (by positivity))) (by positivity)

/-- **Lemma 7**: under the weak growth and balanced-logarithm conditions on `r` and `q`,
with `δ > 0` and final weight at least `3`,
`Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}`. No upper bound on `δ` is required.
Source: §5, Lemma `roth:lem7` ("`Θ_m(q_1^{δ r_1}; q_1, …, q_m; r_1, …, r_m) <
10^m δ^{(1/2)^m}`" under (19)–(22)), for `m = n + 1` variables indexed by `Fin (n + 1)`;
the hypotheses here allow equality in the growth bounds and derive positivity. -/
theorem Θ_lt (n : ℕ) {δ : ℝ} (hδ0 : 0 < δ) {r q : Fin (n + 1) → ℕ}
    (hrlast : 3 ≤ (r (Fin.last n) : ℝ)) (hratio : ∀ i : Fin n, (r i.succ : ℝ) ≤ δ * r i.castSucc)
    (hq1 : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ ≤ Real.log (q 0))
    (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1)) := by
  induction n generalizing δ with
  | zero =>
    have hr : 0 < r 0 := by
      exact_mod_cast (lt_of_lt_of_le (by norm_num : (0 : ℝ) < 3)
        (by simpa using hrlast : (3 : ℝ) ≤ r 0))
    by_cases hδ : δ ≤ 1
    · exact Θ_lt_base_aux hδ0 hδ hr
        (one_lt_of_mul_log_le_aux hr (lt_of_lt_of_le (by positivity) hq1) hqr 0)
    · exact Θ_lt_of_large_delta_aux (by simpa using (not_le.mp hδ).le)
  | succ n ih =>
    by_cases hδ : δ ≤ 1 / ((n : ℝ) + 1 + 1)
    · exact Θ_lt_succ_aux hδ0 hδ hrlast hratio
        (by simpa only [Nat.cast_add, Nat.cast_one] using hq1) hqr ih
    · exact Θ_lt_of_large_delta_aux
        (by simpa only [Nat.cast_add, Nat.cast_one] using (not_le.mp hδ).le)

end Lemma7

end Roth
