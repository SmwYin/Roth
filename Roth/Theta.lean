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

* `Roth.RSet B r`: the set `ℛ_m(B; r_1, …, r_m)` of nonzero integer polynomials of degree at
  most `r j` in `X j` with coefficients bounded by `B`.
* `Roth.indexSet B q r`: the set of indices of `R ∈ RSet B r` at the points `(h_j / q_j)_j`
  with `gcd (h_j, q_j) = 1`, relative to `r`.
* `Roth.Θ B q r`: the supremum of `Roth.indexSet B q r`.
* `Roth.lem6M`, `Roth.lem6Φ`: the auxiliary quantities `M` and `Φ` of Lemma 6.

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

namespace Roth

open MvPolynomial

variable {σ : Type*} [Fintype σ] [DecidableEq σ]

/-- The set `ℛ_m(B; r)` of nonzero integer polynomials whose degree in each variable `X j` is at
most `r j` and whose coefficients have absolute value at most `B`.
Source: §5 (items (1)–(3) of the definition of `ℛ_m`). -/
def RSet (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ) :=
  {R | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧ ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}

/-- The set of indices `ind(R; h/q; r)` of polynomials `R ∈ ℛ_m(B; r)` at the points
`(h_j / q_j)_j` with each `h_j` coprime to `q_j`; its supremum is `Θ_m(B; q; r)`.
Source: §5, definition of `Θ_m`. -/
def indexSet (B : ℝ) (q r : σ → ℕ) : Set ℝ :=
  {x | ∃ R ∈ RSet B r, ∃ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) ∧
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r = x}

/-- `Θ_m(B; q_1, …, q_m; r_1, …, r_m)` is the supremum of the indices `ind(R; h/q; r)` over
`R ∈ ℛ_m(B; r)` and `h` with each `h_j` coprime to `q_j`. Source: §5, definition of `Θ_m`. -/
noncomputable def Θ (B : ℝ) (q r : σ → ℕ) : ℝ := sSup (indexSet B q r)

omit [Fintype σ] [DecidableEq σ] in
/-- If `1 ≤ B`, the constant polynomial `1` lies in `ℛ_m(B; r)`. Source: §5 ("the constant
polynomial `1` with every `h_i = 1` is allowed"). -/
theorem one_mem_RSet {B : ℝ} (hB : 1 ≤ B) (r : σ → ℕ) : (1 : MvPolynomial σ ℤ) ∈ RSet B r := by
  classical
  simp [RSet, coeff_one, apply_ite, ite_apply, hB, zero_le_one.trans hB]

omit [DecidableEq σ] in
/-- If `1 ≤ B`, the set of indices defining `Θ_m(B; q; r)` is nonempty. Source: §5 ("This
supremum is well-defined"). -/
theorem indexSet_nonempty {B : ℝ} (hB : 1 ≤ B) (q r : σ → ℕ) : (indexSet B q r).Nonempty :=
  ⟨_, 1, one_mem_RSet hB r, fun _ ↦ 1, fun _ ↦ isCoprime_one_left, rfl⟩

omit [DecidableEq σ] in
/-- If every `r j` is positive, the indices defining `Θ_m(B; q; r)` are bounded above (by the
number `m` of variables). Source: §5 ("`0 ≤ Θ_m ≤ m`": Taylor's theorem gives a nonzero
derivative of weight at most `m`). -/
theorem indexSet_bddAbove (B : ℝ) (q : σ → ℕ) {r : σ → ℕ} : BddAbove (indexSet B q r) := by
  classical
  refine ⟨Fintype.card σ, ?_⟩
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
    (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
          Int.cast_injective] using hRd) _

omit [DecidableEq σ] in
/-- The index of any `R ∈ ℛ_m(B; r)` at a point `(h_j / q_j)_j` with each `h_j` coprime to `q_j`
is at most `Θ_m(B; q; r)`. Source: §5, definition of `Θ_m` as a supremum, and the Lean note
("lemmas for bounding an individual index"). -/
theorem index_le_Θ {B : ℝ} {q r : σ → ℕ} (hr : ∀ j, 0 < r j) {R : MvPolynomial σ ℤ}
    (hR : R ∈ RSet B r) {h : σ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r :=
  le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩

omit [DecidableEq σ] in
/-- `Θ_m(B; q; r)` is nonnegative when `1 ≤ B` and every `r j` is positive. Source: §5
("`0 ≤ Θ_m`"). -/
theorem Θ_nonneg {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    0 ≤ Θ B q r := by
  apply Real.sSup_nonneg
  rintro _ ⟨R, _, h, _, rfl⟩
  exact index_nonneg _ _ _

omit [DecidableEq σ] in
/-- `Θ_m(B; q; r)` is at most the number `m` of variables. Source: §5 ("`Θ_m ≤ m`"). -/
theorem Θ_le_card {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Fintype.card σ := by
  refine Real.sSup_le ?_ (Nat.cast_nonneg _)
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
    (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
          Int.cast_injective] using hRd) _

omit [DecidableEq σ] in
/-- A bound on every index is a bound on `Θ`. Source: §5, Lemma 5 ("Taking the supremum proves
the claim"). -/
theorem Θ_le_of_forall_index_le {B : ℝ} (hB : 1 ≤ B) {q r : σ → ℕ} {c : ℝ}
    (hc : ∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) : Θ B q r ≤ c := by
  refine csSup_le (indexSet_nonempty hB q r) ?_
  rintro _ ⟨R, hR, h, hh, rfl⟩
  exact hc R hR h hh

omit [DecidableEq σ] in
/-- `Θ_m(B; q; r)` is monotone in `B`. Source: §5 ("`Θ_m` is nondecreasing in `B`, since
increasing `B` enlarges the set of allowed polynomials"). -/
theorem Θ_mono {B B' : ℝ} (hB : 1 ≤ B) (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    Θ B q r ≤ Θ B' q r := by
  refine csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) ?_
  rintro _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, rfl⟩
  exact ⟨R, ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩, h, hh, rfl⟩

omit [DecidableEq σ] in
private lemma indexSet_comp_subset {τ : Type*} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ) :
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

omit [DecidableEq σ] in
/-- `Θ` is invariant under renaming the variables. Source: §4, Lean note after Lemma 4-2
("invariance under ... variable renaming"). -/
theorem Θ_equiv {τ : Type*} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ) :
    Θ B (q ∘ e) (r ∘ e) = Θ B q r := by
  apply congrArg sSup
  refine subset_antisymm (indexSet_comp_subset e B q r) ?_
  simpa [Function.comp_def] using indexSet_comp_subset e.symm B (q ∘ e) (r ∘ e)

section Lemma5

private lemma isPrimitive_linear {h : ℤ} {q : ℕ} (hcop : IsCoprime h (q : ℤ)) :
    (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h).IsPrimitive := by
  intro c hc
  rw [Polynomial.C_dvd_iff_dvd_coeff] at hc
  exact hcop.isUnit_of_dvd' (by simpa using hc 0)
    (by simpa only [Polynomial.coeff_sub, Polynomial.coeff_C_mul, Polynomial.coeff_X_one,
      Polynomial.coeff_C, mul_one, one_ne_zero, ↓reduceIte, sub_zero] using hc 1)

private lemma isPrimitive_pow {p : Polynomial ℤ} (hp : p.IsPrimitive) (t : ℕ) :
    (p ^ t).IsPrimitive :=
  Nat.rec Polynomial.isPrimitive_one (fun t ih ↦ by simpa [pow_succ] using ih.mul hp) t

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
    rw [Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_C, Polynomial.map_X,
      Polynomial.map_C, mul_sub, ← Polynomial.C_mul, mul_div_cancel₀ _ hq']
    simp
  apply (Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast _ _
    (isPrimitive_pow (isPrimitive_linear hcop) t)).2
  rw [Polynomial.map_pow, hmap, mul_pow, ← Polynomial.C_pow,
    Polynomial.C_mul_dvd (pow_ne_zero _ hq')]
  exact Polynomial.pow_rootMultiplicity_dvd _ _

/-- If the coefficients of a nonzero `R ∈ ℤ[X]` are bounded by `B` and `h / q`, with `h` coprime
to `q > 0`, is a root of `R` of multiplicity `t`, then `q^t ≤ B`.
It suffices to bound the absolute value of the leading coefficient.
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

omit [DecidableEq σ] in
private lemma index_unique_le_log_div [Unique σ] {B : ℝ} {q r : σ → ℕ} (hq : 1 < q default)
    {R : MvPolynomial σ ℤ} (hR : R ≠ 0) (hRB : |((uniqueAlgEquiv ℤ σ R).leadingCoeff : ℝ)| ≤ B)
    {h : σ → ℤ} (hh : IsCoprime (h default) (q default : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤
      Real.log B / (r default * Real.log (q default)) := by
  classical
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
  rw [index_unique ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR), hmapeq, hmult]
  have hlog := Real.log_le_log (by positivity : (0 : ℝ) < (q default : ℝ) ^
    Polynomial.rootMultiplicity ((h default : ℚ) / q default) (R1.map (Int.castRingHom ℚ)))
    (pow_rootMultiplicity_le ((map_ne_zero_iff _ (uniqueAlgEquiv ℤ σ).injective).2 hR)
      (Nat.zero_lt_of_lt hq) hh hRB)
  rw [Real.log_pow] at hlog
  simpa [div_div, mul_comm] using
    div_le_div_of_nonneg_right
      ((le_div_iff₀ (Real.log_pos (by exact_mod_cast hq))).2 hlog) (Nat.cast_nonneg _)

omit [DecidableEq σ] in
/-- **Lemma 5**: in one variable, if `q > 1` then `Θ_1(B; q; r) ≤ log B / (r log q)`.
Source: §5, Lemma `roth:lem5` ("Suppose additionally that `q_1 > 1`. Then
`Θ_1(B; q_1; r_1) ≤ log B / (r_1 log q_1)`"), for a single variable `σ`. -/
theorem Θ_unique_le [Unique σ] {B : ℝ} (hB : 1 ≤ B) {q : σ → ℕ} (hq : 1 < q default) {r : σ → ℕ}
    (hr : 0 < r default) : Θ B q r ≤ Real.log B / (r default * Real.log (q default)) :=
  Θ_le_of_forall_index_le hB fun _ hR _ hh ↦
    index_unique_le_log_div hq hR.1
      (by simpa only [Polynomial.leadingCoeff, coeff_uniqueAlgEquiv] using hR.2.2 _) (hh default)

end Lemma5

section Lemma6

variable {τ : Type*} [Fintype τ] [DecidableEq τ]

/-- The constant `M = (r_1 + 1)^{p l} l! B^l 2^{p l r_1}` of Lemma 6. Source: §5, proof of
Lemma 6, eq. (16). -/
noncomputable def lem6M (p r₁ : ℕ) (B : ℝ) (l : ℕ) : ℝ :=
  ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r₁)

/-- The quantity `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1})` of
Lemma 6. Source: §5, proof of Lemma 6, eq. (15). -/
noncomputable def lem6Φ (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ :=
  Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) + Θ M (q ∘ some) fun j ↦ l * r (some j)

/-- The constant `M` of Lemma 6 is at least `1` when `B` is. Source: §5, proof of Lemma 6. -/
theorem one_le_lem6M (p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) : 1 ≤ lem6M p r₁ B l := by
  rw [lem6M]
  refine one_le_mul_of_one_le_of_one_le
    (one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le ?_ ?_)
      (one_le_pow₀ hB)) (one_le_pow₀ (by norm_num))
  · exact one_le_pow₀ (le_add_of_nonneg_left (Nat.cast_nonneg r₁))
  · exact_mod_cast Nat.factorial_pos l

/-- For `a ≥ 0`, `⌊a⌋² / 2 ≤ ∑_{0 ≤ ν ≤ ⌊a⌋} (a - ν)`. Source: §5, proof of Lemma 6, first
FACT ("For any `α ≥ 0` we have `∑_{0 ≤ ν ≤ α} (α - ν) ≥ [α]²/2`"). -/
theorem floor_sq_div_two_le_sum {a : ℝ} (ha : 0 ≤ a) :
    (⌊a⌋₊ : ℝ) ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ν) := by
  have hsum := congrArg (Nat.cast (R := ℝ)) (Finset.sum_range_id_mul_two (⌊a⌋₊ + 1))
  simp only [Nat.add_sub_cancel] at hsum
  push_cast at hsum
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  push_cast
  nlinarith [Nat.floor_le ha]

/-- For `a > 10`, `a² / 3 < ⌊a⌋² / 2`. Source: §5, proof of Lemma 6, second FACT ("If `α > 10`,
then `[α]²/2 > α²/3`"). -/
theorem sq_div_three_lt_floor_sq_div_two {a : ℝ} (ha : 10 < a) :
    a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2 := by
  nlinarith [Nat.lt_floor_add_one a]

private lemma mul_div_two_le_sum_max_aux {θ r : ℝ} {l : ℕ} (hl : (l : ℝ) ≤ θ * r) :
    l * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) := by
  rcases Nat.eq_zero_or_pos l with rfl | hl0
  · simp
  by_cases hθ : θ ≤ 0
  · exact (div_nonpos_of_nonpos_of_nonneg
      (mul_nonpos_of_nonneg_of_nonpos (Nat.cast_nonneg l) hθ) (by norm_num)).trans
        (Finset.sum_nonneg fun _ _ ↦ le_max_left _ _)
  have hr := pos_of_mul_pos_right ((Nat.cast_pos.mpr hl0).trans_le hl) (le_of_not_ge hθ)
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
    linarith only [hsum, (Nat.cast_nonneg n : (0 : ℝ) ≤ n), hnle, sq_nonneg a,
      mul_nonneg (sub_nonneg.mpr hnle) (sub_nonneg.mpr hnlt.le)]
  calc
    r * θ ^ 2 / 3 = (θ * r) ^ 2 / 3 / r := by field_simp
    _ ≤ (∑ ν ∈ Finset.range (n + 1), (θ * r - ν)) / r :=
      (div_le_div_iff_of_pos_right hr).2 hbound
    _ ≤ ∑ ν ∈ Finset.range (n + 1), max 0 (θ - ν / r) := by
      simp only [Finset.sum_div, sub_div, mul_div_cancel_right₀ _ hr.ne']
      exact Finset.sum_le_sum fun ν _ ↦ le_max_right _ _
    _ ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) :=
      Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_subset_range.2
        ((Nat.floor_lt (mul_nonneg hθ hr.le)).2 hl))
        fun _ _ _ ↦ le_max_left _ _

private lemma mul_sq_div_three_le_sum_max_aux {θ r : ℝ} (hθ : 0 ≤ θ) {l : ℕ} (hl : θ * r ≤ l) :
    r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r) := by
  rcases le_or_gt r 0 with hr | hr
  · exact (div_nonpos_of_nonpos_of_nonneg (mul_nonpos_of_nonpos_of_nonneg hr (sq_nonneg θ))
      (by norm_num)).trans (Finset.sum_nonneg fun _ _ ↦ le_max_left _ _)
  rcases lt_or_eq_of_le hl with hl | hl
  · exact mul_sq_div_three_le_sum_max_of_pos_aux hr hθ hl
  · linarith only [mul_div_two_le_sum_max_aux hl.ge, congrArg (· * θ) hl,
      mul_nonneg hr.le (sq_nonneg θ)]

/-- If `θ r_p > 10`, then `min(lθ/2, r_p θ²/3) ≤ ∑_{ν<l} max(0, θ - ν/r_p)`.
Source: §5, proof of Lemma 6 ("Combining everything, we obtain
`∑_{ν<l} max(0, θ - ν/r_p) ≥ min(lθ/2, r_p θ²/3)`", the two cases `θ r_p < l` and
`θ r_p ≥ l`), for `θ r_p > 10`.
The inequality also holds without the source's positivity and size assumptions. -/
theorem min_le_sum_max {θ : ℝ} {rp : ℕ} (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) := by
  by_cases hθ : θ ≤ 0
  · exact (min_le_left _ _).trans ((div_nonpos_of_nonpos_of_nonneg
      (mul_nonpos_of_nonneg_of_nonpos (Nat.cast_nonneg l) hθ) (by norm_num)).trans
        (Finset.sum_nonneg fun _ _ ↦ le_max_left _ _))
  rcases le_or_gt (l : ℝ) (θ * rp) with hl | hl
  · exact (min_le_left _ _).trans (mul_div_two_le_sum_max_aux hl)
  · exact (min_le_right _ _).trans (mul_sq_div_three_le_sum_max_aux (le_of_not_ge hθ) hl.le)

omit [DecidableEq τ] in
/-- The index of the determinant `F = det (∂_{D_μ} ∂_{x_p}^ν R)_{μ,ν}` is at least
`∑_{ν<l} max(0, ind R - ν/r_p) - lδ`, where `δ` bounds the weights of the derivatives `D_μ`.
Source: §5, proof of Lemma 6 ("We have proved `ind(F) ≥ ∑_{ν<l} max(0, θ - ν/r_p) - lδ`"). -/
theorem sum_max_sub_le_index_det {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (hD : ∀ μ, (D μ).degree ≤ μ) (hdet : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0) (α : Option τ → ℝ)
    {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ}
    (hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ) :
    ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤
      index (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by
  classical
  set E : Fin l → Fin l → MvPolynomial (Option τ) ℝ := fun μ ν ↦
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R
  have hterm : ∀ μ ν : Fin l, E μ ν ≠ 0 →
      max 0 (index R α r - ν / r none) - δ ≤ index (E μ ν) α r := by
    intro μ ν hE
    have h1 := index_hasseDeriv_ge hE α r
    rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1
    have h2 := hδ (D μ) ((hD μ).trans (Nat.le_sub_one_of_lt μ.isLt))
    rw [sub_le_iff_le_add]
    exact max_le (add_nonneg (index_nonneg _ _ _) ((weight_nonneg _ _).trans h2))
      (by linarith only [h1, h2])
  rw [Matrix.det_apply'] at hdet ⊢
  refine le_index_sum hdet fun s _ hs ↦ ?_
  have hprod : ∏ i, Matrix.of E (s i) i ≠ 0 := (mul_ne_zero_iff.mp hs).2
  have hidx : index (((Equiv.Perm.sign s : ℤ) : MvPolynomial (Option τ) ℝ) *
      ∏ i, Matrix.of E (s i) i) α r = index (∏ i, Matrix.of E (s i) i) α r := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign s) with h | h <;> simp [h, index_neg]
  rw [hidx, index_prod _ (fun i _ ↦ (Finset.prod_ne_zero_iff.1 hprod) i (Finset.mem_univ _)) α hr,
    ← Fin.sum_univ_eq_sum_range (fun ν : ℕ ↦ max 0 (index R α r - ν / r none)) l]
  have hlδ : (l : ℝ) * δ = ∑ _i : Fin l, δ := by simp
  rw [hlδ, ← Finset.sum_sub_distrib]
  exact Finset.sum_le_sum fun i _ ↦
    hterm (s i) i ((Finset.prod_ne_zero_iff.1 hprod) i (Finset.mem_univ _))

omit [DecidableEq τ] in
private lemma index_separated_mul_le_aux {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {q : Option τ → ℕ}
    {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {M : ℝ} {l : ℕ} (hl : 0 < l)
    {U : MvPolynomial τ ℤ} (hU : U ∈ RSet M (fun j ↦ l * r (some j))) {V : Polynomial ℤ}
    (hV : V ≠ 0) (hVd : V.natDegree ≤ l * r none) (hVc : ∀ b, |(V.coeff b : ℝ)| ≤ M) :
    index (map (Int.castRingHom ℝ)
        (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V))
      (fun j ↦ (h j : ℝ) / q j) r ≤ l * lem6Φ q r M l := by
  classical
  set V' : MvPolynomial Unit ℤ := (uniqueAlgEquiv ℤ Unit).symm V with hV'
  have hV'0 : V' ≠ 0 := by
    rwa [hV', ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective]
  have hVmem : V' ∈ RSet M (fun _ : Unit ↦ l * r none) := by
    refine ⟨hV'0, fun j ↦ ?_, fun d ↦ ?_⟩
    · rw [Subsingleton.elim j default, hV', degreeOf_uniqueAlgEquiv_symm]
      exact hVd
    · rw [hV', MvPolynomial.coeff_uniqueAlgEquiv_symm]
      exact hVc _
  have hinjV : Function.Injective (fun _ : Unit ↦ (none : Option τ)) :=
    fun a b _ ↦ Subsingleton.elim a b
  rw [aeval_X_eq_rename, _root_.map_mul, map_rename, map_rename,
    index_mul ((map_ne_zero_iff _ (rename_injective _ (Option.some_injective _))).2
      ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hU.1))
      ((map_ne_zero_iff _ (rename_injective _ hinjV)).2
        ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hV'0)) _ hr0,
    index_rename (Option.some_injective _), index_rename hinjV]
  have hUΘ := index_le_Θ (fun j ↦ Nat.mul_pos hl (hr0 _)) hU (h := h ∘ some)
    fun j ↦ hh (some j)
  have hVΘ := index_le_Θ (fun _ ↦ Nat.mul_pos hl (hr0 none)) hVmem
    (q := fun _ : Unit ↦ q none) (h := fun _ ↦ h none) fun _ ↦ hh none
  rw [index_mul_left_weights] at hUΘ hVΘ
  have hlR : (0 : ℝ) < l := by exact_mod_cast hl
  simpa only [lem6Φ, mul_add, Function.comp_def, mul_comm _ (l : ℝ), add_comm] using
    add_le_add ((div_le_iff₀ hlR).1 hUΘ) ((div_le_iff₀ hlR).1 hVΘ)

omit [DecidableEq τ] in
/-- If the determinant `F = det (∂_{D_μ} ∂_{x_p}^ν R)_{μ,ν}` factors as
`U(x_1, …, x_{p-1}) V(x_p)` with suitably bounded degrees, then its index at `h/q` is at most
`l Φ`, where `Φ` is formed with the coefficient bound `M` of Lemma 6.
Source: §5, proof of Lemma 6, eq. (17) ("`ind F ≤ l Φ`"). -/
theorem index_det_le {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁)
    {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r)
    {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ} (hl : 1 ≤ l)
    {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0)
    (hUd : ∀ j, degreeOf j U ≤ l * r (some j)) (hVd : V.natDegree ≤ l * r none)
    (hF : (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) :
    index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)
      (fun j ↦ (h j : ℝ) / q j) r ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l := by
  classical
  -- Step 1: the coefficients of `F` are bounded by `M`.
  have hFcoef (d) : |(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv
      ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det.coeff d : ℤ) : ℝ)| ≤
      lem6M (Fintype.card τ + 1) r₁ B l := by
    simpa [lem6M, Finset.prod_const, Finset.sum_const, Fintype.card_option, pow_mul,
      mul_right_comm] using
      abs_coeff_det_hasseDeriv_le _ R (r := fun _ ↦ r₁) (fun j ↦ (hR.2.1 j).trans (hr₁ j))
        ((abs_nonneg ((R.coeff 0 : ℤ) : ℝ)).trans (hR.2.2 0)) hR.2.2 d
  -- Step 2: the coefficients of `U` and `V` are bounded by `M`.
  have hUc : ∀ a, |((U.coeff a : ℤ) : ℝ)| ≤ lem6M (Fintype.card τ + 1) r₁ B l := fun a ↦ by
    have h1 := hFcoef (a.mapDomain some + Finsupp.single none V.natDegree)
    rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1
    exact (le_mul_of_one_le_right (abs_nonneg _) (by
      exact_mod_cast Int.one_le_abs (Polynomial.leadingCoeff_ne_zero.2 hV))).trans h1
  have hVc : ∀ b, |((V.coeff b : ℤ) : ℝ)| ≤ lem6M (Fintype.card τ + 1) r₁ B l := fun b ↦ by
    obtain ⟨a₀, ha₀⟩ := MvPolynomial.ne_zero_iff.1 hU
    have h1 := hFcoef (a₀.mapDomain some + Finsupp.single none b)
    rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1
    exact (le_mul_of_one_le_left (abs_nonneg _) (by
      exact_mod_cast Int.one_le_abs ha₀)).trans h1
  -- Step 3: Lemma 4-2, the index of the product of polynomials in separate variables.
  rw [hF]
  exact index_separated_mul_le_aux hr0 hh hl ⟨hU, hUd, hUc⟩ hV hVd hVc

omit [DecidableEq τ] in
private lemma weight_le_delta_aux {δ : ℝ} (hδ : 0 ≤ δ) {r : Option τ → ℕ}
    (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {d : τ →₀ ℕ} (hd : d.degree ≤ r none) :
    weight (r ∘ some) d ≤ δ := by
  classical
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

omit [Fintype τ] [DecidableEq τ] in
private lemma mapped_det_ne_zero_aux {R : MvPolynomial (Option τ) ℤ} {l : ℕ} {D : Fin l → (τ →₀ ℕ)}
    {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0)
    (hF : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
        rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +
      Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det ≠ 0 := by
  have hmapdet : map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +
        Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det := by
    rw [RingHom.map_det]
    congr 1
    exact Matrix.ext fun μ ν ↦ by simp [hasseDeriv_map]
  rw [← hmapdet]
  refine (map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 ?_
  rw [hF]
  refine mul_ne_zero ((map_ne_zero_iff _ (rename_injective _ (Option.some_injective _))).2 hU) ?_
  rw [aeval_X_eq_rename]
  refine (map_ne_zero_iff _ (rename_injective _ fun a b _ ↦ Subsingleton.elim a b)).2 ?_
  rwa [ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective]

private lemma index_numeric_bound_aux {θ Φ δ rp l : ℝ} (hΦ : 0 ≤ Φ) (hδ1 : δ ≤ 1) (hrp : 3 ≤ rp)
    (hl : 0 < l) (hl' : l ≤ rp + 1) (hmin : min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ l * (Φ + δ)) :
    θ ≤ 2 * (Φ + √Φ + √δ) := by
  -- The small-index comparison `δ ≤ √δ` also controls the linear bound.
  have hsΦ : 0 ≤ √Φ := Real.sqrt_nonneg _
  rcases min_le_iff.1 hmin with hk | hk
  · have hθ : θ ≤ 2 * (Φ + δ) := by
      rwa [mul_div_assoc, mul_le_mul_iff_right₀ hl, div_le_iff₀ (by norm_num), mul_comm] at hk
    linarith only [hθ, Real.le_sqrt_self_iff.2 hδ1, hsΦ]
  · have hsum : 0 ≤ Φ + δ := nonneg_of_mul_nonneg_right
      ((div_nonneg (mul_nonneg (by linarith only [hrp]) (sq_nonneg θ)) (by norm_num)).trans hk) hl
    have hsq : θ ^ 2 ≤ 4 * (Φ + δ) := by
      have h1 : rp * θ ^ 2 ≤ 3 * (rp + 1) * (Φ + δ) := by
        nlinarith only [hk, mul_le_mul_of_nonneg_right hl' hsum]
      nlinarith only [h1, mul_nonneg (sub_nonneg.2 hrp) hsum, hrp]
    have hθ : θ ≤ 2 * (√Φ + √δ) := by
      nlinarith only [hsq, Real.sq_sqrt hΦ, le_max_left δ 0, Real.sq_sqrt' (x := δ), hsΦ,
        Real.sqrt_nonneg δ, mul_nonneg hsΦ (Real.sqrt_nonneg δ)]
    linarith only [hθ, hΦ]

omit [DecidableEq τ] in
/-- **Lemma 6**, for one polynomial and one point: the index of `R ∈ ℛ_p(B; r)` at `h/q` is at
most `2(Φ + Φ^{1/2} + δ^{1/2})` for some `1 ≤ l ≤ r_p + 1`. Source: §5, Lemma `roth:lem6` and
its proof ("We need to show that the index `ind(R; h/q; r)` is bounded by the right hand side
of (13)"). -/
theorem index_le_lem6 {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ}
    (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ}
    {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤
        2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
          √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  classical
  have hr0 : ∀ j, 0 < r j := fun j ↦ by
    cases j with
    | none => exact_mod_cast (by linarith only [hrp] : (0 : ℝ) < r none)
    | some j =>
      exact_mod_cast pos_of_mul_pos_right
        ((by linarith only [hrp] : (0 : ℝ) < r none).trans_le (hratio j)) hδ0
  have hB : 1 ≤ B := by
    obtain ⟨d, hd⟩ := MvPolynomial.ne_zero_iff.1 hR.1
    exact (by exact_mod_cast Int.one_le_abs hd : (1 : ℝ) ≤ |(R.coeff d : ℝ)|).trans (hR.2.2 d)
  obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1
  refine ⟨l, hl, hl', ?_⟩
  let α : Option τ → ℝ := fun j ↦ (h j : ℝ) / q j
  let Φ := lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l
  -- `1 ≤ M` and `0 ≤ Φ`.
  have hM1 := one_le_lem6M (Fintype.card τ + 1) r₁ hB l
  -- The two bounds for the index of `F`.
  have hlower := sum_max_sub_le_index_det D hD (mapped_det_ne_zero_aux hU hV hF) α hr0
    (fun d hd ↦ weight_le_delta_aux hδ0 hratio (by lia))
  have hupper := index_det_le hr0 hr₁ hR hh hl hU hV hUd hVd hF
  simp only [RingHom.map_det, RingHom.mapMatrix_apply, Matrix.map, Matrix.of_apply] at hupper
  simp only [hasseDeriv_map] at hlower
  apply index_numeric_bound_aux (Φ := Φ) (l := (l : ℝ))
    (add_nonneg (Θ_nonneg hM1 _ fun _ ↦ Nat.mul_pos hl (hr0 _))
      (Θ_nonneg hM1 _ fun _ ↦ Nat.mul_pos hl (hr0 _))) hδ1 hrp
    (by exact_mod_cast (show 0 < l from hl))
    (by exact_mod_cast hl')
  exact (min_le_sum_max (θ := index (map (Int.castRingHom ℝ) R) α r) (rp := r none) l).trans
    (by simpa [mul_add] using sub_le_iff_le_add.1 (hlower.trans hupper))

omit [DecidableEq τ] in
/-- **Lemma 6**: `Θ_p(B; q; r)` is at most twice the maximum of `Φ + Φ^{1/2} + δ^{1/2}` over
`1 ≤ l ≤ r_p + 1`. Source: §5, Lemma `roth:lem6` ("`Θ_p(B; q; r) ≤ 2 max_l (Φ + Φ^{1/2} + δ^{1/2})`,
where the maximum is taken over integers `l` satisfying `1 ≤ l ≤ r_p + 1`"). -/
theorem Θ_option_le {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ))
    (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ}
    (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B) :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (by lia))
      (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
        √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  refine Θ_le_of_forall_index_le hB fun R hR h hh ↦ ?_
  obtain ⟨l, hl, hl', hle⟩ := index_le_lem6 hδ0 hδ1 hrp hratio hr₁ hq hR hh
  refine hle.trans (mul_le_mul_of_nonneg_left ?_ (by norm_num))
  exact Finset.le_sup' (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
    √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) (Finset.mem_Icc.2 ⟨hl, hl'⟩)

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
    _ = 2 ^ ((2 * p + 1) * r₁ * l) := by
      rw [← pow_mul, ← pow_mul, ← pow_add, ← pow_add]
      ring_nf

private lemma two_pow_lt_rpow_aux {p r₁ l : ℕ} (hp : 0 < p) {δ q : ℝ} (hδ : 0 < δ) (hq : 0 ≤ q)
    (hlog : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q) (hlr : 0 < l * r₁) :
    (2 : ℝ) ^ ((2 * p + 1) * r₁ * l) < q ^ (δ / p * (l * r₁)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp
  replace hq : 0 < q := zero_lt_one.trans <|
    (Real.log_pos_iff hq).1 <| lt_of_lt_of_le (by positivity) hlog
  have hlog2 : Real.log 2 < 1 := by
    exact (Real.log_lt_sub_one_of_pos (by norm_num : (0 : ℝ) < 2) (by norm_num)).trans_eq
      (by norm_num)
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

/-- For `log q_1 ≥ p (2p + 1) / δ` and `p > 0`, the constant `M` of Lemma 6 with
`B = q_1^{δ r_1}` satisfies `M < q_1^{δ (1 + 1/p) l r_1}`.
Source: §5, proof of Lemma 7 ("`M < q_1^{δ_1 l r_1}` with `δ_1 = δ(1 + p⁻¹)`"). -/
theorem lem6M_lt {p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ q₁ : ℕ}
    (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) :
    lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp
  have hq1pos : (0 : ℝ) < q₁ := zero_lt_one.trans <|
    (Real.log_pos_iff (Nat.cast_nonneg q₁)).1 <| lt_of_lt_of_le (by positivity) hq₁
  -- the factors other than `B^l` are at most `2^{(2p+1) r₁ l}`
  have hnatR : ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤
      2 ^ ((2 * p + 1) * r₁ * l) := by
    exact_mod_cast factorial_coefficient_le_two_pow_aux p r₁ l (hl'.trans Nat.lt_two_pow_self.le)
  calc
    lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l = ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial *
        2 ^ (p * l * r₁) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l := by
          rw [lem6M]
          ring
    _ ≤ 2 ^ ((2 * p + 1) * r₁ * l) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l :=
      mul_le_mul_of_nonneg_right hnatR (by positivity)
    _ < (q₁ : ℝ) ^ (δ / p * (l * r₁)) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l :=
      mul_lt_mul_of_pos_right
        (two_pow_lt_rpow_aux hp hδ0 hq1pos.le hq₁ (Nat.mul_pos (by lia) (by lia))) (by positivity)
    _ = (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by
      rw [← Real.rpow_mul_natCast hq1pos.le, ← Real.rpow_add hq1pos]
      congr 1
      ring

/-- For `p ≥ 2` and `0 < δ ≤ 1`, with `δ_1 = δ (1 + 1/p)`,
`δ_1 + 10^{p-1} δ_1^{(1/2)^{p-1}} < 3 · 10^{p-1} δ^{(1/2)^{p-1}}`.
Source: §5, proof of Lemma 7 ("`Φ < δ_1 + 10^{p-1} δ_1^{(1/2)^{p-1}} < 2δ + 2 · 10^{p-1}
δ^{(1/2)^{p-1}} < 3 · 10^{p-1} δ^{(1/2)^{p-1}}`"). -/
theorem lem7_Φ_bound {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) :
    δ * (1 + 1 / p) + 10 ^ (p - 1) * (δ * (1 + 1 / p)) ^ ((1 / 2 : ℝ) ^ (p - 1)) <
      3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1)) := by
  set e : ℝ := (1 / 2 : ℝ) ^ (p - 1)
  have he1 : e ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  have hp : (2 : ℝ) ≤ p := by exact_mod_cast hp
  have hc1 : 1 ≤ 1 + 1 / (p : ℝ) := le_add_of_nonneg_right (by positivity)
  have hc2 : 1 + 1 / (p : ℝ) ≤ 3 / 2 := by
    have : 1 / (p : ℝ) ≤ 1 / 2 := one_div_le_one_div_of_le (by norm_num) hp
    linarith only [this]
  have hδe : δ ≤ δ ^ e := by
    simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1 he1
  have hde0 : 0 < δ ^ e := Real.rpow_pos_of_pos hδ0 e
  have hmul : (δ * (1 + 1 / p)) ^ e ≤ δ ^ e * (3 / 2) := by
    rw [Real.mul_rpow hδ0.le (by positivity)]
    refine mul_le_mul_of_nonneg_left ?_ hde0.le
    calc (1 + 1 / (p : ℝ)) ^ e ≤ (1 + 1 / (p : ℝ)) ^ (1 : ℝ) :=
          Real.rpow_le_rpow_of_exponent_le hc1 he1
      _ ≤ 3 / 2 := by simpa using hc2
  nlinarith only [mul_le_mul hδe hc2 (zero_le_one.trans hc1) hde0.le,
    mul_le_mul_of_nonneg_left hmul (by positivity : (0 : ℝ) ≤ 10 ^ (p - 1)),
    mul_le_mul_of_nonneg_right
      (le_self_pow₀ (by norm_num : (1 : ℝ) ≤ 10) (by lia : p - 1 ≠ 0)) hde0.le, hde0]

/-- If `0 ≤ Φ < 3 · 10^{p-1} δ^{(1/2)^{p-1}}` with `p ≥ 2` and `0 < δ < 1`, then
`2(Φ + Φ^{1/2} + δ^{1/2}) < 10^p δ^{(1/2)^p}`.
Source: §5, proof of Lemma 7 ("Set `a = δ^{2^{-p}}` ... `Θ_p < 2(3·10^{p-1} a² + √3 10^{(p-1)/2}
a + δ^{1/2}) ≤ ... < 10^p a`"). -/
theorem lem7_numeric {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {Φ : ℝ}
    (hΦ0 : 0 ≤ Φ) (hΦ : Φ < 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))) :
    2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ ((1 / 2 : ℝ) ^ p) := by
  obtain ⟨k, rfl⟩ : ∃ k, p = k + 1 := ⟨p - 1, by omega⟩
  rw [Nat.add_sub_cancel] at hΦ
  set a := δ ^ ((1 / 2 : ℝ) ^ (k + 1)) with ha
  set T : ℝ := 10 ^ k with hT
  have ha0 : 0 < a := Real.rpow_pos_of_pos hδ0 _
  have ha1 : a ≤ 1 := Real.rpow_le_one hδ0.le hδ1.le (by positivity)
  have ha2 : a ^ 2 = δ ^ ((1 / 2 : ℝ) ^ k) := by
    rw [ha, ← Real.rpow_mul_natCast hδ0.le, pow_succ]
    congr 1
    push_cast
    ring
  have hsqrt : √δ ≤ a := by
    rw [Real.sqrt_eq_rpow, ha]
    refine Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1.le ?_
    rw [pow_succ]
    have : (1 / 2 : ℝ) ^ k ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
    linarith
  have hT10 : (10 : ℝ) ≤ T := le_self_pow₀ (by norm_num) (by omega)
  rw [← ha2] at hΦ
  have hsΦ : √Φ < T * a := by
    rw [Real.sqrt_lt' (by positivity)]
    nlinarith
  have hpow : (10 : ℝ) ^ (k + 1) = 10 * T := by rw [pow_succ, hT, mul_comm]
  rw [hpow]
  nlinarith

/-- **Lemma 7**: under the growth conditions (19)–(22) on `r` and `q`,
`Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}`.
Source: §5, Lemma `roth:lem7` ("`Θ_m(q_1^{δ r_1}; q_1, …, q_m; r_1, …, r_m) <
10^m δ^{(1/2)^m}`" under (19)–(22)), for `m = n + 1` variables indexed by `Fin (n + 1)`. -/
theorem Θ_lt (n : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ : δ < 1 / ((n : ℝ) + 1)) {r q : Fin (n + 1) → ℕ}
    (hr0 : ∀ j, 0 < r j) (hrlast : 10 / δ < r (Fin.last n))
    (hratio : ∀ i : Fin n, (r i.succ : ℝ) / δ < r i.castSucc) (hq0 : ∀ j, 0 < q j)
    (hq1 : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ < Real.log (q 0))
    (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1)) := by
  induction n generalizing δ with
  | zero =>
    have : Unique (Fin (0 + 1)) := inferInstanceAs (Unique (Fin 1))
    have hL : 0 < Real.log (q 0) := lt_trans (by positivity) hq1
    have hq : 1 < q 0 := by
      exact_mod_cast (Real.log_pos_iff (Nat.cast_nonneg (q 0))).1 hL
    have hB : (1 : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) :=
      Real.one_le_rpow (by exact_mod_cast hq.le) (by positivity)
    have h := Θ_unique_le (q := q) (r := r) hB (by convert hq; exact Subsingleton.elim _ _) (hr0 _)
    have hr : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0
    have key : ∀ x y : Fin (0 + 1), Θ ((q 0 : ℝ) ^ (δ * r 0)) q r ≤
        Real.log ((q 0 : ℝ) ^ (δ * r 0)) / (r x * Real.log (q y)) →
        Θ ((q 0 : ℝ) ^ (δ * r 0)) q r ≤ δ := fun x y hxy => by
      rw [Subsingleton.elim x 0, Subsingleton.elim y 0, Real.log_rpow (by positivity)] at hxy
      have hδeq : δ * r 0 * Real.log (q 0) / (r 0 * Real.log (q 0)) = δ := by
        field_simp
      rwa [hδeq] at hxy
    replace h := key _ _ h
    have hδ1 : δ < 1 := by simpa using hδ
    have h1 : δ ≤ δ ^ ((1 / 2 : ℝ) ^ (0 + 1)) := by
      simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1.le
        (by norm_num : (1 / 2 : ℝ) ^ (0 + 1) ≤ 1)
    have h2 : 0 < δ ^ ((1 / 2 : ℝ) ^ (0 + 1)) := Real.rpow_pos_of_pos hδ0 _
    have h3 : (10 : ℝ) ^ (0 + 1) = 10 := by norm_num
    rw [h3]
    linarith
  | succ n ih =>
    have hL : 0 < Real.log (q 0) := lt_trans (by positivity) hq1
    have hq0' : 1 < q 0 := by
      exact_mod_cast (Real.log_pos_iff (Nat.cast_nonneg (q 0))).1 hL
    set B : ℝ := (q 0 : ℝ) ^ (δ * r 0)
    have hB : 1 ≤ B := Real.one_le_rpow (by exact_mod_cast hq0'.le) (by positivity)
    have hn2 : (0 : ℝ) < (n : ℝ) + 1 + 1 := by positivity
    set u : ℝ := 1 / ((n : ℝ) + 1 + 1) with hu
    have hu0 : 0 < u := by positivity
    have huP : u * ((n : ℝ) + 1 + 1) = 1 := by rw [hu]; field_simp
    have hδu : δ < u := by
      have := hδ
      push_cast at this
      exact this
    have hδ1 : δ < 1 := by nlinarith
    -- `r` is antitone
    have hanti : Antitone r := Fin.antitone_iff_succ_le.2 fun i => by
      have h1 := hratio i
      have h2 : (r i.succ : ℝ) ≤ r i.succ / δ := le_div_self (Nat.cast_nonneg _) hδ0 hδ1.le
      exact_mod_cast h2.trans h1.le
    have hr₁ : ∀ j, r j ≤ r 0 := fun j => hanti (Fin.zero_le j)
    have hratio' : ∀ j : Fin (n + 1), (r (Fin.last (n + 1)) : ℝ) < δ * r (Fin.castSucc j) :=
      fun j => by
        have h1 := hratio (Fin.last n)
        rw [Fin.succ_last, div_lt_iff₀ hδ0] at h1
        have h2 : (r (Fin.castSucc (Fin.last n)) : ℝ) ≤ r (Fin.castSucc j) := by
          exact_mod_cast hanti (Fin.castSucc_le_castSucc_iff.2 (Fin.le_last j))
        nlinarith
    have hlast_lt0 : r (Fin.last (n + 1)) < r 0 := by
      have h := hratio' 0
      have hr0' : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0
      have : (r (Fin.last (n + 1)) : ℝ) < r 0 := by
        change (r (Fin.last (n + 1)) : ℝ) < δ * r 0 at h
        nlinarith
      exact_mod_cast this
    -- transport to `Option (Fin (n + 1))`
    set e : Fin (n + 2) ≃ Option (Fin (n + 1)) := finSuccEquivLast with he
    rw [← Θ_equiv e.symm B q r]
    set q' := q ∘ e.symm with hq'
    set r' := r ∘ e.symm with hr'
    have hq'n : q' none = q (Fin.last (n + 1)) := by simp [hq', he]
    have hr'n : r' none = r (Fin.last (n + 1)) := by simp [hr', he]
    have hq's : ∀ j, q' (some j) = q (Fin.castSucc j) := fun j => by
      simp [hq', he, finSuccEquivLast_symm_some]
    have hr's : ∀ j, r' (some j) = r (Fin.castSucc j) := fun j => by
      simp [hr', he, finSuccEquivLast_symm_some]
    have hr'0 : ∀ j, 0 < r' j := fun j => hr0 _
    have hr'1 : ∀ j, r' j ≤ r 0 := fun j => hr₁ _
    have hq'0 : ∀ j, 0 < q' j := fun j => hq0 _
    clear_value q' r' e
    have hle := Θ_option_le (τ := Fin (n + 1)) hδ0.le hδ1.le (r := r')
      (by
        rw [hr'n]
        exact (by norm_num : (3 : ℝ) ≤ 10).trans
          ((le_div_self (by norm_num) hδ0 hδ1.le).trans hrlast.le))
      (fun j ↦ by rw [hr'n, hr's]; exact (hratio' j).le)
      (r₁ := r 0) hr'1 (q := q') hq'0 hB
    refine lt_of_le_of_lt hle ?_
    set X : ℝ := 10 ^ (n + 1 + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1 + 1))
    suffices hsup : (Finset.Icc 1 (r' none + 1)).sup' (Finset.nonempty_Icc.2 (by omega))
        (fun l => lem6Φ q' r' (lem6M (Fintype.card (Fin (n + 1)) + 1) (r 0) B l) l +
          √(lem6Φ q' r' (lem6M (Fintype.card (Fin (n + 1)) + 1) (r 0) B l) l) + √δ) < X / 2 by
      linarith
    rw [Finset.sup'_lt_iff]
    intro l hl
    obtain ⟨hl1, hl2⟩ := Finset.mem_Icc.1 hl
    rw [hr'n] at hl2
    have hl'' : l ≤ r 0 := by omega
    rw [Fintype.card_fin]
    set M := lem6M (n + 1 + 1) (r 0) B l
    set δ₁ := δ * (1 + 1 / ((n + 1 + 1 : ℕ) : ℝ)) with hδ₁
    have hδδ₁ : δ ≤ δ₁ := le_mul_of_one_le_right hδ0.le (le_add_of_nonneg_right (by positivity))
    have hδ₁0 : 0 < δ₁ := by positivity
    have hMlt : M < (q 0 : ℝ) ^ (δ₁ * (l * r 0)) :=
      lem6M_lt (p := n + 1 + 1) (by omega) hδ0 (by
        have := hq1
        push_cast at this ⊢
        linarith) hl1 hl''
    have hM1 : 1 ≤ M := one_le_lem6M _ _ hB l
    set C : ℝ := (q 0 : ℝ) ^ (δ₁ * (l * r 0)) with hC
    have hC1 : 1 ≤ C := Real.one_le_rpow (by exact_mod_cast hq0'.le) (by positivity)
    have hlR : (0 : ℝ) < l := by exact_mod_cast hl1
    -- the one-variable term
    have hΘ1 : Θ M (fun _ : Unit => q' none) (fun _ => l * r' none) ≤ δ₁ := by
      rw [hq'n, hr'n]
      have hqr' := hqr (Fin.last (n + 1))
      have hrl : (0 : ℝ) < r (Fin.last (n + 1)) := by exact_mod_cast hr0 _
      have hr0R : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0
      have hLl : 0 < Real.log (q (Fin.last (n + 1))) := by
        by_contra hc
        push Not at hc
        nlinarith
      have hql : 1 < q (Fin.last (n + 1)) := by
        exact_mod_cast (Real.log_pos_iff (Nat.cast_nonneg (q (Fin.last (n + 1))))).1 hLl
      calc Θ M (fun _ : Unit => q (Fin.last (n + 1))) (fun _ => l * r (Fin.last (n + 1)))
          ≤ Θ C (fun _ : Unit => q (Fin.last (n + 1))) (fun _ => l * r (Fin.last (n + 1))) :=
            Θ_mono hM1 hMlt.le _ fun _ => Nat.mul_pos hl1 (hr0 _)
        _ ≤ Real.log C / (((l * r (Fin.last (n + 1)) : ℕ) : ℝ) *
              Real.log (q (Fin.last (n + 1)))) :=
            Θ_unique_le hC1 hql (Nat.mul_pos hl1 (hr0 _))
        _ ≤ δ₁ := by
            rw [hC, Real.log_rpow (by positivity), div_le_iff₀ (by push_cast; positivity)]
            push_cast
            have := mul_le_mul_of_nonneg_left hqr' (by positivity : (0 : ℝ) ≤ δ₁ * l)
            nlinarith
    -- the `(p - 1)`-variable term, by the induction hypothesis
    have hΘ2 : Θ M (q' ∘ some) (fun j => l * r' (some j)) <
        10 ^ (n + 1) * δ₁ ^ ((1 / 2 : ℝ) ^ (n + 1)) := by
      have hfq : q' ∘ some = fun j => q (Fin.castSucc j) := funext hq's
      have hfr : (fun j => l * r' (some j)) = fun j => l * r (Fin.castSucc j) :=
        funext fun j => by rw [hr's]
      rw [hfq, hfr]
      refine lt_of_le_of_lt (Θ_mono hM1 hMlt.le _ fun j => Nat.mul_pos hl1 (hr0 _)) ?_
      have hCeq : C = ((q (Fin.castSucc 0) : ℕ) : ℝ) ^
          (δ₁ * ((l * r (Fin.castSucc 0) : ℕ) : ℝ)) := by
        rw [Nat.cast_mul]
        rfl
      rw [hCeq]
      have hA : δ₁ < 1 / ((n : ℝ) + 1) := by
        have hδ₁u : δ₁ = δ * (1 + u) := by rw [hδ₁, hu]; push_cast; ring
        rw [hδ₁u, lt_div_iff₀ (by positivity)]
        have h1 : u * ((n : ℝ) + 1) = 1 - u := by linarith
        have h2 : u * (1 + u) * ((n : ℝ) + 1) = 1 - u ^ 2 := by
          rw [mul_right_comm, h1]
          ring
        have h3 := mul_lt_mul_of_pos_right hδu (by positivity : (0 : ℝ) < (1 + u) * (n + 1))
        nlinarith
      have hB' : 10 / δ₁ < ((l * r (Fin.castSucc (Fin.last n)) : ℕ) : ℝ) := by
        have h1 : 10 / δ₁ ≤ 10 / δ := div_le_div_of_nonneg_left (by norm_num) hδ0 hδδ₁
        have h2 : (r (Fin.last (n + 1)) : ℝ) ≤ r (Fin.castSucc (Fin.last n)) := by
          exact_mod_cast hanti (Fin.le_last _)
        have h3 : (r (Fin.castSucc (Fin.last n)) : ℝ) ≤ l * r (Fin.castSucc (Fin.last n)) :=
          le_mul_of_one_le_left (Nat.cast_nonneg _) (by exact_mod_cast hl1)
        push_cast
        linarith
      have hC' : ∀ i : Fin n, ((l * r (Fin.castSucc i.succ) : ℕ) : ℝ) / δ₁ <
          ((l * r (Fin.castSucc (Fin.castSucc i)) : ℕ) : ℝ) := by
        intro i
        have h : (r (Fin.castSucc i.succ) : ℝ) / δ < r (Fin.castSucc (Fin.castSucc i)) :=
          hratio (Fin.castSucc i)
        push_cast
        calc (l : ℝ) * r (Fin.castSucc i.succ) / δ₁ ≤ l * r (Fin.castSucc i.succ) / δ :=
              div_le_div_of_nonneg_left (by positivity) hδ0 hδδ₁
          _ = l * (r (Fin.castSucc i.succ) / δ) := by ring
          _ < l * r (Fin.castSucc (Fin.castSucc i)) := mul_lt_mul_of_pos_left h hlR
      have hD' : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ₁ <
          Real.log (q (Fin.castSucc 0)) := by
        calc ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ₁
            ≤ ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ :=
              div_le_div_of_nonneg_left (by positivity) hδ0 hδδ₁
          _ ≤ (((n + 1 : ℕ) : ℝ) + 1) * (2 * (((n + 1 : ℕ) : ℝ) + 1) + 1) / δ := by
              apply div_le_div_of_nonneg_right _ hδ0.le
              push_cast
              nlinarith
          _ < Real.log (q 0) := hq1
      have hE' : ∀ j : Fin (n + 1), ((l * r (Fin.castSucc 0) : ℕ) : ℝ) *
          Real.log (q (Fin.castSucc 0)) ≤
          ((l * r (Fin.castSucc j) : ℕ) : ℝ) * Real.log (q (Fin.castSucc j)) := by
        intro j
        have := hqr (Fin.castSucc j)
        push_cast
        rw [mul_assoc, mul_assoc]
        exact mul_le_mul_of_nonneg_left this (Nat.cast_nonneg l)
      exact ih (r := fun j => l * r (Fin.castSucc j)) (q := fun j => q (Fin.castSucc j)) hδ₁0 hA
        (fun j => Nat.mul_pos hl1 (hr0 _)) hB' hC' (fun j => hq0 _) hD' hE'
    -- combine
    have hΦ0 : 0 ≤ lem6Φ q' r' M l := by
      rw [lem6Φ]
      exact add_nonneg (Θ_nonneg hM1 _ fun _ => Nat.mul_pos hl1 (hr'0 _))
        (Θ_nonneg hM1 _ fun _ => Nat.mul_pos hl1 (hr'0 _))
    have hb := lem7_Φ_bound (p := n + 1 + 1) (by omega) hδ0 hδ1.le
    simp only [Nat.add_sub_cancel] at hb
    have hΦlt : lem6Φ q' r' M l <
        3 * 10 ^ (n + 1 + 1 - 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1 + 1 - 1)) := by
      simp only [Nat.add_sub_cancel]
      rw [lem6Φ]
      linarith
    have hfin := lem7_numeric (p := n + 1 + 1) (by omega) hδ0 hδ1 hΦ0 hΦlt
    linarith

end Lemma7

end Roth
