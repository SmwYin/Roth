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

/-- The index of any `R ∈ ℛ_m(B; r)` at a point `(h_j / q_j)_j` with each `h_j` coprime to `q_j`
is at most `Θ_m(B; q; r)`. Source: §5, definition of `Θ_m` as a supremum, and the Lean note
("lemmas for bounding an individual index"). -/
theorem index_le_Θ {B : ℝ} {q r : σ → ℕ} (hr : ∀ j, 0 < r j) {R : MvPolynomial σ ℤ}
    (hR : R ∈ RSet B r) {h : σ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r :=
  le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩

/-- `Θ_m(B; q; r)` is nonnegative when `1 ≤ B` and every `r j` is positive. Source: §5
("`0 ≤ Θ_m`"). -/
theorem Θ_nonneg {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    0 ≤ Θ B q r := by
  apply Real.sSup_nonneg
  rintro _ ⟨R, _, h, _, rfl⟩
  exact index_nonneg _ _ _

/-- `Θ_m(B; q; r)` is at most the number `m` of variables. Source: §5 ("`Θ_m ≤ m`"). -/
theorem Θ_le_card {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    Θ B q r ≤ Fintype.card σ := by
  refine Real.sSup_le ?_ (Nat.cast_nonneg _)
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
    (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
          Int.cast_injective] using hRd) _

/-- A bound on every index is a bound on `Θ`. Source: §5, Lemma 5 ("Taking the supremum proves
the claim"). -/
theorem Θ_le_of_forall_index_le {B : ℝ} (hB : 1 ≤ B) {q r : σ → ℕ} {c : ℝ}
    (hc : ∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) : Θ B q r ≤ c := by
  refine csSup_le (indexSet_nonempty hB q r) ?_
  rintro _ ⟨R, hR, h, hh, rfl⟩
  exact hc R hR h hh

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
  rw [Polynomial.isPrimitive_iff_isUnit_of_C_dvd]
  intro c hc
  rw [Polynomial.C_dvd_iff_dvd_coeff] at hc
  have h1 := hc 1
  have h0 := hc 0
  simp only [Polynomial.coeff_sub, Polynomial.coeff_C_mul, Polynomial.coeff_X_one,
    Polynomial.coeff_X_zero, Polynomial.coeff_C, mul_one, mul_zero, zero_sub, one_ne_zero,
    ↓reduceIte, sub_zero, dvd_neg] at h1 h0
  exact hcop.isUnit_of_dvd' h0 h1

private lemma isPrimitive_pow {p : Polynomial ℤ} (hp : p.IsPrimitive) (t : ℕ) :
    (p ^ t).IsPrimitive := by
  induction t with
  | zero => simp [Polynomial.isPrimitive_one]
  | succ t ih => rw [pow_succ]; exact ih.mul hp

/-- If `h` is coprime to `q > 0` and `t` is the multiplicity of `h / q` as a root of a nonzero
`R ∈ ℤ[X]`, then `R = (q X - h)^t Q` for some `Q ∈ ℤ[X]`.
Source: §5, proof of Lemma 5 ("The polynomial `(q_1 x_1 - h_1)^t` is primitive and divides
`R` over `ℚ`. Gauss's lemma therefore gives a nonzero `Q ∈ ℤ[x_1]` with
`R = (q_1 x_1 - h_1)^t Q`"). -/
theorem exists_eq_pow_mul_of_rootMultiplicity {R : Polynomial ℤ} (hR : R ≠ 0) {h : ℤ} {q : ℕ}
    (hq : 0 < q) (hcop : IsCoprime h (q : ℤ)) :
    ∃ Q : Polynomial ℤ, R = (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h) ^
      Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) * Q := by
  set t := Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ))
  have hprim := isPrimitive_pow (isPrimitive_linear hcop) t
  have hq' : (q : ℚ) ≠ 0 := by exact_mod_cast hq.ne'
  have hmap : (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h).map (Int.castRingHom ℚ) =
      Polynomial.C (q : ℚ) * (Polynomial.X - Polynomial.C ((h : ℚ) / q)) := by
    rw [Polynomial.map_sub, Polynomial.map_mul, Polynomial.map_C, Polynomial.map_X,
      Polynomial.map_C, mul_sub, ← Polynomial.C_mul, mul_div_cancel₀ _ hq']
    simp
  have hdvd : ((Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h) ^ t).map
      (Int.castRingHom ℚ) ∣ R.map (Int.castRingHom ℚ) := by
    rw [Polynomial.map_pow, hmap, mul_pow, ← Polynomial.C_pow,
      Polynomial.C_mul_dvd (pow_ne_zero _ hq')]
    exact Polynomial.pow_rootMultiplicity_dvd _ _
  exact (Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast _ _ hprim).2 hdvd

/-- If the coefficients of a nonzero `R ∈ ℤ[X]` are bounded by `B` and `h / q`, with `h` coprime
to `q > 0`, is a root of `R` of multiplicity `t`, then `q^t ≤ B`.
Source: §5, proof of Lemma 5 ("Comparing nonzero leading coefficients yields
`B ≥ |lc(R)| = q_1^t |lc(Q)| ≥ q_1^t`"). -/
theorem pow_rootMultiplicity_le {R : Polynomial ℤ} (hR : R ≠ 0) {h : ℤ} {q : ℕ} (hq : 0 < q)
    (hcop : IsCoprime h (q : ℤ)) {B : ℝ} (hB : ∀ n, |((R.coeff n : ℤ) : ℝ)| ≤ B) :
    (q : ℝ) ^ Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) ≤ B := by
  obtain ⟨Q, hQ⟩ := exists_eq_pow_mul_of_rootMultiplicity hR hq hcop
  set t := Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ))
  have hQ0 : Q ≠ 0 := right_ne_zero_of_mul (hQ ▸ hR)
  have hlc : R.leadingCoeff = (q : ℤ) ^ t * Q.leadingCoeff := by
    rw [hQ, Polynomial.leadingCoeff_mul, Polynomial.leadingCoeff_pow, sub_eq_add_neg,
      ← Polynomial.C_neg, Polynomial.leadingCoeff_linear (by exact_mod_cast hq.ne')]
  have h1 : (1 : ℝ) ≤ |(Q.leadingCoeff : ℝ)| := by
    exact_mod_cast Int.one_le_abs (Polynomial.leadingCoeff_ne_zero.2 hQ0)
  have h2 := hB R.natDegree
  rw [← Polynomial.leadingCoeff, hlc] at h2
  push_cast at h2
  rw [abs_mul, abs_pow, Nat.abs_cast] at h2
  exact (le_mul_of_one_le_right (by positivity) h1).trans h2

/-- **Lemma 5**: in one variable, if `q > 1` then `Θ_1(B; q; r) ≤ log B / (r log q)`.
Source: §5, Lemma `roth:lem5` ("Suppose additionally that `q_1 > 1`. Then
`Θ_1(B; q_1; r_1) ≤ log B / (r_1 log q_1)`"), for a single variable `σ`. -/
theorem Θ_unique_le [Unique σ] {B : ℝ} (hB : 1 ≤ B) {q : σ → ℕ} (hq : 1 < q default) {r : σ → ℕ}
    (hr : 0 < r default) : Θ B q r ≤ Real.log B / (r default * Real.log (q default)) := by
  have hq0 : 0 < q default := by omega
  have hlogq : 0 < Real.log (q default) := Real.log_pos (by exact_mod_cast hq)
  have hrpos : (0 : ℝ) < r default := by exact_mod_cast hr
  refine Θ_le_of_forall_index_le hB fun R hR h hh => ?_
  obtain ⟨hR0, -, hRB⟩ := hR
  set R1 : Polynomial ℤ := uniqueAlgEquiv ℤ σ R with hR1
  have hR10 : R1 ≠ 0 := by rwa [hR1, ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ σ).injective]
  have hcoef : ∀ n, |((R1.coeff n : ℤ) : ℝ)| ≤ B := fun n => by
    rw [hR1, coeff_uniqueAlgEquiv]
    exact hRB _
  have hpow := pow_rootMultiplicity_le hR10 hq0 (hh default) hcoef
  have hmapeq : uniqueAlgEquiv ℝ σ (map (Int.castRingHom ℝ) R) =
      R1.map (Int.castRingHom ℝ) := by
    ext n
    rw [coeff_uniqueAlgEquiv, Polynomial.coeff_map, hR1, coeff_uniqueAlgEquiv, coeff_map]
  have hmult : Polynomial.rootMultiplicity ((h default : ℝ) / q default)
      (R1.map (Int.castRingHom ℝ)) =
      Polynomial.rootMultiplicity ((h default : ℚ) / q default) (R1.map (Int.castRingHom ℚ)) := by
    rw [Polynomial.eq_rootMultiplicity_map (f := Rat.castHom ℝ) Rat.cast_injective,
      Polynomial.map_map]
    congr 1
    simp
  rw [index_unique ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0), hmapeq, hmult,
    div_le_div_iff₀ hrpos (by positivity)]
  have hlog : (Polynomial.rootMultiplicity ((h default : ℚ) / q default)
      (R1.map (Int.castRingHom ℚ)) : ℝ) * Real.log (q default) ≤ Real.log B := by
    rw [← Real.log_pow]
    exact Real.log_le_log (by positivity) hpow
  nlinarith

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
  Θ M (fun _ : Unit => q none) (fun _ => l * r none) + Θ M (q ∘ some) fun j => l * r (some j)

/-- The constant `M` of Lemma 6 is at least `1` when `B` is. Source: §5, proof of Lemma 6. -/
theorem one_le_lem6M (p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) : 1 ≤ lem6M p r₁ B l := by
  rw [lem6M]
  have h1 : (1 : ℝ) ≤ ((r₁ : ℝ) + 1) ^ (p * l) :=
    one_le_pow₀ (by linarith [(Nat.cast_nonneg r₁ : (0 : ℝ) ≤ r₁)])
  have h2 : (1 : ℝ) ≤ l.factorial := by exact_mod_cast Nat.factorial_pos l
  have h3 : (1 : ℝ) ≤ B ^ l := one_le_pow₀ hB
  have h4 : (1 : ℝ) ≤ 2 ^ (p * l * r₁) := one_le_pow₀ (by norm_num)
  exact one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le
    (one_le_mul_of_one_le_of_one_le h1 h2) h3) h4

/-- For `a ≥ 0`, `⌊a⌋² / 2 ≤ ∑_{0 ≤ ν ≤ ⌊a⌋} (a - ν)`. Source: §5, proof of Lemma 6, first
FACT ("For any `α ≥ 0` we have `∑_{0 ≤ ν ≤ α} (α - ν) ≥ [α]²/2`"). -/
theorem floor_sq_div_two_le_sum {a : ℝ} (ha : 0 ≤ a) :
    (⌊a⌋₊ : ℝ) ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ν) := by
  set n := ⌊a⌋₊
  have hn : (n : ℝ) ≤ a := Nat.floor_le ha
  have h1 := Finset.sum_range_id_mul_two (n + 1)
  simp only [Nat.add_sub_cancel] at h1
  have h2 : (∑ ν ∈ Finset.range (n + 1), (ν : ℝ)) * 2 = ((n : ℝ) + 1) * n := by
    have := congrArg (Nat.cast (R := ℝ)) h1
    push_cast at this
    exact this
  rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  push_cast
  nlinarith

/-- For `a > 10`, `a² / 3 < ⌊a⌋² / 2`. Source: §5, proof of Lemma 6, second FACT ("If `α > 10`,
then `[α]²/2 > α²/3`"). -/
theorem sq_div_three_lt_floor_sq_div_two {a : ℝ} (ha : 10 < a) :
    a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2 := by
  set n := ⌊a⌋₊
  have hlt : a < n + 1 := Nat.lt_floor_add_one a
  have h10 : (10 : ℝ) ≤ n := by
    exact_mod_cast (Nat.le_floor (by norm_num; linarith) : 10 ≤ n)
  nlinarith

/-- If `θ r_p > 10`, then `min(lθ/2, r_p θ²/3) ≤ ∑_{ν<l} max(0, θ - ν/r_p)`.
Source: §5, proof of Lemma 6 ("Combining everything, we obtain
`∑_{ν<l} max(0, θ - ν/r_p) ≥ min(lθ/2, r_p θ²/3)`", the two cases `θ r_p < l` and
`θ r_p ≥ l`), for `θ r_p > 10`. -/
theorem min_le_sum_max {θ : ℝ} {rp : ℕ} (hrp : 0 < rp) (hθ : 10 < θ * rp) (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) := by
  have hrp' : (0 : ℝ) < rp := by exact_mod_cast hrp
  have hθ0 : 0 < θ := pos_of_mul_pos_left (by linarith) hrp'.le
  by_cases hl : (l : ℝ) ≤ θ * rp
  · refine (min_le_left _ _).trans ?_
    have hterm : ∀ ν ∈ Finset.range l, max 0 (θ - ν / rp) = θ - ν / rp := by
      intro ν hν
      apply max_eq_right
      have hν' : (ν : ℝ) < l := by exact_mod_cast Finset.mem_range.1 hν
      rw [sub_nonneg, div_le_iff₀ hrp']
      linarith
    rw [Finset.sum_congr rfl hterm, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range,
      nsmul_eq_mul, ← Finset.sum_div]
    have h1 := Finset.sum_range_id_mul_two l
    have h2 : (∑ ν ∈ Finset.range l, (ν : ℝ)) * 2 = l * ((l : ℝ) - 1) := by
      rcases Nat.eq_zero_or_pos l with rfl | hl0
      · simp
      · have : ((l - 1 : ℕ) : ℝ) = l - 1 := by rw [Nat.cast_sub hl0]; simp
        rw [← this]
        have := congrArg (Nat.cast (R := ℝ)) h1
        push_cast at this
        exact this
    have hl0 : (0 : ℝ) ≤ l := Nat.cast_nonneg l
    rw [le_sub_iff_add_le, div_add_div _ _ (by norm_num) hrp'.ne', div_le_iff₀ (by positivity)]
    nlinarith
  · push Not at hl
    refine (min_le_right _ _).trans ?_
    set n := ⌊θ * rp⌋₊
    have hθr : 0 ≤ θ * rp := by positivity
    have hn : n < l := (Nat.floor_lt hθr).2 hl
    have hnle : (n : ℝ) ≤ θ * rp := Nat.floor_le hθr
    calc (rp : ℝ) * θ ^ 2 / 3 = (θ * rp) ^ 2 / 3 / rp := by field_simp
      _ ≤ (n : ℝ) ^ 2 / 2 / rp :=
          (div_le_div_iff_of_pos_right hrp').2 (sq_div_three_lt_floor_sq_div_two hθ).le
      _ ≤ (∑ ν ∈ Finset.range (n + 1), (θ * rp - ν)) / rp :=
          (div_le_div_iff_of_pos_right hrp').2 (floor_sq_div_two_le_sum hθr)
      _ = ∑ ν ∈ Finset.range (n + 1), max 0 (θ - ν / rp) := by
          rw [Finset.sum_div]
          refine Finset.sum_congr rfl fun ν hν => ?_
          have hν' : (ν : ℝ) ≤ n := by exact_mod_cast Nat.lt_succ_iff.1 (Finset.mem_range.1 hν)
          rw [max_eq_right]
          · field_simp
          · rw [sub_nonneg, div_le_iff₀ hrp']
            linarith
      _ ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) :=
          Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_subset_range.2 hn)
            fun _ _ _ => le_max_left _ _

/-- The index of the determinant `F = det (∂_{D_μ} ∂_{x_p}^ν R)_{μ,ν}` is at least
`∑_{ν<l} max(0, ind R - ν/r_p) - lδ`, where `δ` bounds the weights of the derivatives `D_μ`.
Source: §5, proof of Lemma 6 ("We have proved `ind(F) ≥ ∑_{ν<l} max(0, θ - ν/r_p) - lδ`"). -/
theorem sum_max_sub_le_index_det {R : MvPolynomial (Option τ) ℝ} (hR : R ≠ 0) {l : ℕ}
    (D : Fin l → (τ →₀ ℕ)) (hD : ∀ μ, (D μ).degree ≤ μ)
    (hdet : (Matrix.of fun μ ν : Fin l =>
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0)
    (α : Option τ → ℝ) {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ}
    (hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ) :
    ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤
      index (Matrix.of fun μ ν : Fin l =>
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by
  set E : Fin l → Fin l → MvPolynomial (Option τ) ℝ := fun μ ν =>
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R
  have hterm : ∀ μ ν : Fin l, E μ ν ≠ 0 →
      max 0 (index R α r - ν / r none) - δ ≤ index (E μ ν) α r := by
    intro μ ν hE
    have h1 := index_hasseDeriv_ge hE α r
    rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1
    have h2 := hδ (D μ) ((hD μ).trans (Nat.le_sub_one_of_lt μ.isLt))
    have h3 := index_nonneg (E μ ν) α r
    have h4 := weight_nonneg (r ∘ some) (D μ)
    rw [sub_le_iff_le_add]
    exact max_le (by linarith) (by linarith)
  have hdet' := hdet
  rw [Matrix.det_apply'] at hdet' ⊢
  refine le_index_sum hdet' fun s _ hs => ?_
  have hprod : ∏ i, Matrix.of E (s i) i ≠ 0 := fun h0 => hs (by rw [h0, mul_zero])
  have hidx : index (((Equiv.Perm.sign s : ℤ) : MvPolynomial (Option τ) ℝ) *
      ∏ i, Matrix.of E (s i) i) α r = index (∏ i, Matrix.of E (s i) i) α r := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign s) with h | h <;> simp [h, index_neg]
  rw [hidx, index_prod _ (fun i _ => (Finset.prod_ne_zero_iff.1 hprod) i (Finset.mem_univ _)) α hr,
    ← Fin.sum_univ_eq_sum_range (fun ν : ℕ => max 0 (index R α r - ν / r none)) l]
  have hlδ : (l : ℝ) * δ = ∑ _i : Fin l, δ := by simp
  rw [hlδ, ← Finset.sum_sub_distrib]
  exact Finset.sum_le_sum fun i _ =>
    hterm (s i) i ((Finset.prod_ne_zero_iff.1 hprod) i (Finset.mem_univ _))

/-- If the determinant `F = det (∂_{D_μ} ∂_{x_p}^ν R)_{μ,ν}` factors as
`U(x_1, …, x_{p-1}) V(x_p)` with suitably bounded degrees, then its index at `h/q` is at most
`l Φ`, where `Φ` is formed with the coefficient bound `M` of Lemma 6.
Source: §5, proof of Lemma 6, eq. (17) ("`ind F ≤ l Φ`"). -/
theorem index_det_le {δ : ℝ} {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ} (hB : 1 ≤ B) {R : MvPolynomial (Option τ) ℤ}
    (hR : R ∈ RSet B r) {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ}
    (hl : 1 ≤ l) (hl' : l ≤ r none + 1) {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ}
    {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0) (hUd : ∀ j, degreeOf j U ≤ l * r (some j))
    (hVd : V.natDegree ≤ l * r none)
    (hF : (Matrix.of fun μ ν : Fin l =>
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) (hδ : 0 < δ) :
    index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l =>
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)
      (fun j => (h j : ℝ) / q j) r ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l := by
  set M := lem6M (Fintype.card τ + 1) r₁ B l with hMdef
  set F := (Matrix.of fun μ ν : Fin l =>
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det
  have hB0 : (0 : ℝ) ≤ B := zero_le_one.trans hB
  have hl0 : 0 < l := hl
  -- Step 1: the coefficients of `F` are bounded by `M`.
  have hprod : ∏ j, ((r j : ℝ) + 1) ≤ ((r₁ : ℝ) + 1) ^ (Fintype.card τ + 1) := by
    calc ∏ j, ((r j : ℝ) + 1) ≤ ∏ _j : Option τ, ((r₁ : ℝ) + 1) :=
          Finset.prod_le_prod₀ (fun j _ => by positivity)
            fun j _ => by have := hr₁ j; gcongr
      _ = _ := by rw [Finset.prod_const, Finset.card_univ, Fintype.card_option]
  have hsum : (∑ j, r j) * l ≤ (Fintype.card τ + 1) * l * r₁ := by
    have : ∑ j, r j ≤ (Fintype.card τ + 1) * r₁ := by
      calc ∑ j, r j ≤ ∑ _j : Option τ, r₁ := Finset.sum_le_sum fun j _ => hr₁ j
        _ = _ := by rw [Finset.sum_const, Finset.card_univ, Fintype.card_option, smul_eq_mul]
    calc (∑ j, r j) * l ≤ (Fintype.card τ + 1) * r₁ * l := Nat.mul_le_mul_right _ this
      _ = _ := by ring
  have hFcoef : ∀ d, |((F.coeff d : ℤ) : ℝ)| ≤ M := fun d => by
    refine (abs_coeff_det_hasseDeriv_le (fun μ ν : Fin l => (D μ).mapDomain some +
      Finsupp.single none (ν : ℕ)) R hR.2.1 hB0 hR.2.2 d).trans ?_
    rw [hMdef, lem6M, pow_mul ((r₁ : ℝ) + 1)]
    have h1 : (∏ j, ((r j : ℝ) + 1)) ^ l ≤ (((r₁ : ℝ) + 1) ^ (Fintype.card τ + 1)) ^ l :=
      pow_le_pow_left₀ (by positivity) hprod l
    have h2 : (2 : ℝ) ^ ((∑ j, r j) * l) ≤ 2 ^ ((Fintype.card τ + 1) * l * r₁) :=
      pow_le_pow_right₀ (by norm_num) hsum
    have h4 : (0 : ℝ) ≤ (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l := by positivity
    calc (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)
        ≤ (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l *
            2 ^ ((Fintype.card τ + 1) * l * r₁) := mul_le_mul_of_nonneg_left h2 h4
      _ ≤ (((r₁ : ℝ) + 1) ^ (Fintype.card τ + 1)) ^ l * l.factorial * B ^ l *
            2 ^ ((Fintype.card τ + 1) * l * r₁) := by
          rw [mul_assoc _ (l.factorial : ℝ), mul_assoc _ (l.factorial : ℝ)]
          gcongr
  -- Step 2: the coefficients of `U` and `V` are bounded by `M`.
  obtain ⟨a₀, ha₀⟩ := MvPolynomial.ne_zero_iff.1 hU
  have hb₀ : V.coeff V.natDegree ≠ 0 := Polynomial.leadingCoeff_ne_zero.2 hV
  have hUc : ∀ a, |((U.coeff a : ℤ) : ℝ)| ≤ M := fun a => by
    have h1 := hFcoef (a.mapDomain some + Finsupp.single none V.natDegree)
    rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1
    have h2 : (1 : ℝ) ≤ |((V.coeff V.natDegree : ℤ) : ℝ)| := by
      rw [← Int.cast_abs]
      exact_mod_cast Int.one_le_abs hb₀
    nlinarith [abs_nonneg ((U.coeff a : ℤ) : ℝ)]
  have hVc : ∀ b, |((V.coeff b : ℤ) : ℝ)| ≤ M := fun b => by
    have h1 := hFcoef (a₀.mapDomain some + Finsupp.single none b)
    rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1
    have h2 : (1 : ℝ) ≤ |((U.coeff a₀ : ℤ) : ℝ)| := by
      rw [← Int.cast_abs]
      exact_mod_cast Int.one_le_abs ha₀
    nlinarith [abs_nonneg ((V.coeff b : ℤ) : ℝ)]
  set V' : MvPolynomial Unit ℤ := (uniqueAlgEquiv ℤ Unit).symm V with hV'
  have hV'0 : V' ≠ 0 := by
    rwa [hV', ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective]
  have hUmem : U ∈ RSet M (fun j => l * r (some j)) := ⟨hU, hUd, hUc⟩
  have hVmem : V' ∈ RSet M (fun _ : Unit => l * r none) := by
    refine ⟨hV'0, fun j => ?_, fun d => ?_⟩
    · rw [Subsingleton.elim j default, hV', degreeOf_uniqueAlgEquiv_symm]
      exact hVd
    · rw [hV', MvPolynomial.coeff_uniqueAlgEquiv_symm]
      exact hVc _
  -- Step 3: Lemma 4-2, the index of the product of polynomials in separate variables.
  have hinjU : Function.Injective (some : τ → Option τ) := Option.some_injective _
  have hinjV : Function.Injective (fun _ : Unit => (none : Option τ)) :=
    fun a b _ => Subsingleton.elim a b
  have hmU := (map_ne_zero_iff (map (Int.castRingHom ℝ))
    (map_injective _ Int.cast_injective)).2 hU
  have hmV := (map_ne_zero_iff (map (Int.castRingHom ℝ))
    (map_injective _ Int.cast_injective)).2 hV'0
  have hmapF : map (Int.castRingHom ℝ) F = rename some (map (Int.castRingHom ℝ) U) *
      rename (fun _ : Unit => (none : Option τ)) (map (Int.castRingHom ℝ) V') := by
    rw [hF, aeval_X_eq_rename, _root_.map_mul, map_rename, map_rename]
  have hrU : ∀ j, 0 < l * r (some j) := fun j => Nat.mul_pos hl0 (hr0 _)
  have hrV : ∀ _ : Unit, 0 < l * r none := fun _ => Nat.mul_pos hl0 (hr0 _)
  rw [hmapF, index_mul ((map_ne_zero_iff _ (rename_injective _ hinjU)).2 hmU)
    ((map_ne_zero_iff _ (rename_injective _ hinjV)).2 hmV) _ hr0,
    index_rename hinjU, index_rename hinjV]
  have hlR : (0 : ℝ) < l := by exact_mod_cast hl0
  have hU' : index (map (Int.castRingHom ℝ) U) ((fun j => (h j : ℝ) / q j) ∘ some) (r ∘ some) =
      l * index (map (Int.castRingHom ℝ) U) ((fun j => (h j : ℝ) / q j) ∘ some)
        (fun j => l * (r ∘ some) j) := by
    rw [index_mul_left_weights]
    field_simp
  have hV'' : index (map (Int.castRingHom ℝ) V') ((fun j => (h j : ℝ) / q j) ∘ fun _ => none)
        (r ∘ fun _ => none) =
      l * index (map (Int.castRingHom ℝ) V') ((fun j => (h j : ℝ) / q j) ∘ fun _ => none)
        (fun j => l * (r ∘ fun _ : Unit => none) j) := by
    rw [index_mul_left_weights]
    field_simp
  have hUΘ := index_le_Θ hrU hUmem (h := h ∘ some) fun j => hh (some j)
  have hVΘ := index_le_Θ hrV hVmem (q := fun _ : Unit => q none) (h := fun _ => h none)
    fun _ => hh none
  rw [hU', hV'', lem6Φ, mul_add]
  have := mul_le_mul_of_nonneg_left hUΘ hlR.le
  have := mul_le_mul_of_nonneg_left hVΘ hlR.le
  simp only [Function.comp_def] at *
  linarith

/-- **Lemma 6**, for one polynomial and one point: the index of `R ∈ ℛ_p(B; r)` at `h/q` is at
most `2(Φ + Φ^{1/2} + δ^{1/2})` for some `1 ≤ l ≤ r_p + 1`. Source: §5, Lemma `roth:lem6` and
its proof ("We need to show that the index `ind(R; h/q; r)` is bounded by the right hand side
of (13)"). -/
theorem index_le_lem6 {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j)
    (hrp : 10 / δ < r none) (hratio : ∀ j, (r none : ℝ) < δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B)
    {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧
      index (map (Int.castRingHom ℝ) R) (fun j => (h j : ℝ) / q j) r ≤
        2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
          √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1
  refine ⟨l, hl, hl', ?_⟩
  set α : Option τ → ℝ := fun j => (h j : ℝ) / q j with hα
  set θ := index (map (Int.castRingHom ℝ) R) α r with hθ
  set M := lem6M (Fintype.card τ + 1) r₁ B l with hMdef
  set Φ := lem6Φ q r M l with hΦ
  have hrp0 : (0 : ℝ) < r none := by exact_mod_cast hr0 none
  have hl0 : 0 < l := hl
  have hlR : (0 : ℝ) < l := by exact_mod_cast hl0
  have hθ0 : 0 ≤ θ := index_nonneg _ _ _
  have hδrp : 10 < δ * r none := by
    rw [div_lt_iff₀ hδ0] at hrp
    linarith
  -- `1 ≤ M` and `0 ≤ Φ`.
  have hM1 : 1 ≤ M := one_le_lem6M _ _ hB l
  have hΦ0 : 0 ≤ Φ := add_nonneg (Θ_nonneg hM1 _ fun _ => Nat.mul_pos hl0 (hr0 _))
    (Θ_nonneg hM1 _ fun _ => Nat.mul_pos hl0 (hr0 _))
  have hsδ : δ ≤ √δ := (Real.le_sqrt hδ0.le hδ0.le).2 (by nlinarith)
  have hsΦ := Real.sqrt_nonneg Φ
  by_cases h10 : θ * r none ≤ 10
  · -- small index: `θ ≤ 10 / r_p < δ ≤ √δ`.
    have : θ < δ := by
      by_contra hc
      push Not at hc
      nlinarith
    linarith
  push Not at h10
  -- the two bounds for the index of `F`.
  have hupper := index_det_le hr0 hr₁ hB hR hh hl hl' hU hV hUd hVd hF hδ0
  have hmapR := (map_ne_zero_iff (map (Int.castRingHom ℝ))
    (map_injective _ Int.cast_injective)).2 hR.1
  have hmapdet : map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l =>
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      (Matrix.of fun μ ν : Fin l => hasseDeriv ((D μ).mapDomain some +
        Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det := by
    rw [RingHom.map_det]
    congr 1
    refine Matrix.ext fun μ ν => ?_
    simp [hasseDeriv_map]
  have hFne : (Matrix.of fun μ ν : Fin l => hasseDeriv ((D μ).mapDomain some +
        Finsupp.single none (ν : ℕ)) (map (Int.castRingHom ℝ) R)).det ≠ 0 := by
    rw [← hmapdet]
    refine (map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 ?_
    rw [hF]
    refine mul_ne_zero ((map_ne_zero_iff _ (rename_injective _ (Option.some_injective _))).2 hU) ?_
    rw [aeval_X_eq_rename]
    refine (map_ne_zero_iff _ (rename_injective _ fun a b _ => Subsingleton.elim a b)).2 ?_
    rw [ne_eq, map_eq_zero_iff _ (uniqueAlgEquiv ℤ Unit).symm.injective]
    exact hV
  have hδ' : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ := fun d hd => by
    have hdeg : (d.degree : ℝ) ≤ r none := by exact_mod_cast (by omega : d.degree ≤ r none)
    calc weight (r ∘ some) d = ∑ j, (d j : ℝ) / r (some j) := rfl
      _ ≤ ∑ j, (d j : ℝ) * δ / r none := Finset.sum_le_sum fun j _ => by
          have hj : (0 : ℝ) < r (some j) := by exact_mod_cast hr0 (some j)
          rw [div_le_div_iff₀ hj hrp0]
          have := hratio j
          have hdj : (0 : ℝ) ≤ d j := Nat.cast_nonneg _
          nlinarith
      _ = δ * d.degree / r none := by
          rw [← Finset.sum_div, ← Finset.sum_mul, Finsupp.degree_eq_sum, Nat.cast_sum, mul_comm]
      _ ≤ δ := by
          rw [div_le_iff₀ hrp0]
          nlinarith
  have hlower := sum_max_sub_le_index_det hmapR D hD hFne α hr0 hδ'
  rw [← hmapdet] at hlower
  have hmin := min_le_sum_max (hr0 none) h10 l
  have hkey : min (l * θ / 2) (r none * θ ^ 2 / 3) ≤ l * (Φ + δ) := by
    have := hupper
    simp only [← hα, ← hMdef, ← hΦ] at this
    nlinarith
  rcases min_le_iff.1 hkey with hk | hk
  · have : θ ≤ 2 * (Φ + δ) := by
      rw [div_le_iff₀ (by norm_num : (0 : ℝ) < 2)] at hk
      nlinarith
    linarith
  · have hl'R : (l : ℝ) ≤ r none + 1 := by exact_mod_cast hl'
    have hrp10 : (10 : ℝ) < r none := by nlinarith
    have hθsq : θ ^ 2 < 4 * (Φ + δ) := by
      have h1 : r none * θ ^ 2 ≤ 3 * (r none + 1) * (Φ + δ) := by nlinarith
      nlinarith
    set s := √(Φ + δ)
    have hs0 : 0 ≤ s := Real.sqrt_nonneg _
    have hs2 : s ^ 2 = Φ + δ := Real.sq_sqrt (by linarith)
    have hθs : θ < 2 * s := by nlinarith
    have hsle : s ≤ √Φ + √δ := by
      have h1 := Real.sq_sqrt hΦ0
      have h2 := Real.sq_sqrt hδ0.le
      have h3 := Real.sqrt_nonneg δ
      nlinarith
    linarith

/-- **Lemma 6**: `Θ_p(B; q; r)` is at most twice the maximum of `Φ + Φ^{1/2} + δ^{1/2}` over
`1 ≤ l ≤ r_p + 1`. Source: §5, Lemma `roth:lem6` ("`Θ_p(B; q; r) ≤ 2 max_l (Φ + Φ^{1/2} + δ^{1/2})`,
where the maximum is taken over integers `l` satisfying `1 ≤ l ≤ r_p + 1`"). -/
theorem Θ_option_le {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j)
    (hrp : 10 / δ < r none) (hratio : ∀ j, (r none : ℝ) < δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B) :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (by omega))
      (fun l => lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
        √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by
  refine Θ_le_of_forall_index_le hB fun R hR h hh => ?_
  obtain ⟨l, hl, hl', hle⟩ :=
    index_le_lem6 hδ0 hδ1 hr0 hrp hratio hr₁ hq hB hR hh
  refine hle.trans (mul_le_mul_of_nonneg_left ?_ (by norm_num))
  exact Finset.le_sup' (fun l => lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
    √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) (Finset.mem_Icc.2 ⟨hl, hl'⟩)

end Lemma6

section Lemma7

private lemma one_lt_of_log_pos {x : ℕ} (h : 0 < Real.log x) : 1 < x := by
  by_contra hc
  push Not at hc
  have hx : (x : ℝ) ≤ 1 := by exact_mod_cast hc
  have := Real.log_nonpos (Nat.cast_nonneg x) hx
  linarith

/-- For `log q_1 > p (2p + 1) / δ`, the constant `M` of Lemma 6 with `B = q_1^{δ r_1}` satisfies
`M < q_1^{δ (1 + 1/p) l r_1}`. Source: §5, proof of Lemma 7 ("`M < q_1^{δ_1 l r_1}` with
`δ_1 = δ(1 + p⁻¹)`"). -/
theorem lem6M_lt {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ : ℕ} (hr₁ : 0 < r₁) {q₁ : ℕ}
    (hq₁ : (p : ℝ) * (2 * p + 1) / δ < Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) :
    lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by
  have hp0 : (0 : ℝ) < p := by exact_mod_cast (by omega : 0 < p)
  have hlogq : 0 < Real.log q₁ := lt_trans (by positivity) hq₁
  have hq1pos : (0 : ℝ) < q₁ := by
    rcases Nat.eq_zero_or_pos q₁ with h | h
    · simp [h] at hlogq
    · exact_mod_cast h
  -- the factors other than `B^l` are at most `2^{(2p+1) r₁ l}`
  have hr2 : r₁ + 1 ≤ 2 ^ r₁ := Nat.lt_two_pow_self
  have hlr : l ≤ 2 ^ r₁ := hl'.trans Nat.lt_two_pow_self.le
  have hnat : (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤
      2 ^ ((2 * p + 1) * r₁ * l) := by
    have h1 : (r₁ + 1) ^ (p * l) ≤ (2 ^ r₁) ^ (p * l) := Nat.pow_le_pow_left hr2 _
    have h2 : l.factorial ≤ (2 ^ r₁) ^ l :=
      (Nat.factorial_le_pow l).trans (Nat.pow_le_pow_left hlr _)
    calc (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁)
        ≤ (2 ^ r₁) ^ (p * l) * (2 ^ r₁) ^ l * 2 ^ (p * l * r₁) := by gcongr
      _ = 2 ^ ((2 * p + 1) * r₁ * l) := by
          rw [← pow_mul, ← pow_mul, ← pow_add, ← pow_add]
          ring_nf
  have hnatR : ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤
      2 ^ ((2 * p + 1) * r₁ * l) := by exact_mod_cast hnat
  have hB : ((q₁ : ℝ) ^ (δ * r₁)) ^ l = (q₁ : ℝ) ^ (δ * r₁ * l) :=
    (Real.rpow_mul_natCast hq1pos.le _ _).symm
  have h2N : (2 : ℝ) ^ ((2 * p + 1) * r₁ * l) < (q₁ : ℝ) ^ (δ / p * (l * r₁)) := by
    rw [← Real.rpow_natCast, Real.rpow_def_of_pos (by norm_num), Real.rpow_def_of_pos hq1pos,
      Real.exp_lt_exp]
    have hlog2 : Real.log 2 < 1 := by
      have := Real.log_lt_sub_one_of_pos (by norm_num : (0 : ℝ) < 2) (by norm_num)
      linarith
    have hlr0 : (0 : ℝ) < l * r₁ := mul_pos (by exact_mod_cast hl) (by exact_mod_cast hr₁)
    have h3 : (2 * p + 1 : ℝ) < Real.log q₁ * (δ / p) := by
      rw [mul_div_assoc', lt_div_iff₀ hp0]
      rw [div_lt_iff₀ hδ0] at hq₁
      linarith
    have h4 : Real.log 2 * (2 * p + 1) < Real.log q₁ * (δ / p) :=
      (mul_lt_of_lt_one_left (by positivity) hlog2).trans h3
    calc Real.log 2 * (((2 * p + 1) * r₁ * l : ℕ) : ℝ) = Real.log 2 * (2 * p + 1) * (l * r₁) := by
          push_cast
          ring
      _ < Real.log q₁ * (δ / p) * (l * r₁) := mul_lt_mul_of_pos_right h4 hlr0
      _ = Real.log q₁ * (δ / p * (l * r₁)) := by ring
  calc lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l = ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial *
        2 ^ (p * l * r₁) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l := by
        rw [lem6M]
        ring
    _ ≤ 2 ^ ((2 * p + 1) * r₁ * l) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l :=
        mul_le_mul_of_nonneg_right hnatR (by positivity)
    _ < (q₁ : ℝ) ^ (δ / p * (l * r₁)) * ((q₁ : ℝ) ^ (δ * r₁)) ^ l :=
        mul_lt_mul_of_pos_right h2N (by positivity)
    _ = (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by
        rw [hB, ← Real.rpow_add hq1pos]
        congr 1
        ring

/-- For `p ≥ 2` and `0 < δ < 1`, with `δ_1 = δ (1 + 1/p)`,
`δ_1 + 10^{p-1} δ_1^{(1/2)^{p-1}} < 3 · 10^{p-1} δ^{(1/2)^{p-1}}`.
Source: §5, proof of Lemma 7 ("`Φ < δ_1 + 10^{p-1} δ_1^{(1/2)^{p-1}} < 2δ + 2 · 10^{p-1}
δ^{(1/2)^{p-1}} < 3 · 10^{p-1} δ^{(1/2)^{p-1}}`"). -/
theorem lem7_Φ_bound {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) :
    δ * (1 + 1 / p) + 10 ^ (p - 1) * (δ * (1 + 1 / p)) ^ ((1 / 2 : ℝ) ^ (p - 1)) <
      3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1)) := by
  set e : ℝ := (1 / 2 : ℝ) ^ (p - 1) with he
  have he0 : 0 < e := by positivity
  have he1 : e ≤ 1 := pow_le_one₀ (by norm_num) (by norm_num)
  have hp : (2 : ℝ) ≤ p := by exact_mod_cast hp
  have hc1 : 1 ≤ 1 + 1 / (p : ℝ) := le_add_of_nonneg_right (by positivity)
  have hc2 : 1 + 1 / (p : ℝ) ≤ 3 / 2 := by
    have : 1 / (p : ℝ) ≤ 1 / 2 := one_div_le_one_div_of_le (by norm_num) hp
    linarith
  have hδe : δ ≤ δ ^ e := by
    simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1.le he1
  have hde0 : 0 < δ ^ e := Real.rpow_pos_of_pos hδ0 e
  have hmul : (δ * (1 + 1 / p)) ^ e ≤ δ ^ e * (3 / 2) := by
    rw [Real.mul_rpow hδ0.le (by positivity)]
    refine mul_le_mul_of_nonneg_left ?_ hde0.le
    calc (1 + 1 / (p : ℝ)) ^ e ≤ (1 + 1 / (p : ℝ)) ^ (1 : ℝ) :=
          Real.rpow_le_rpow_of_exponent_le hc1 he1
      _ ≤ 3 / 2 := by rw [Real.rpow_one]; exact hc2
  have hT : (10 : ℝ) ≤ 10 ^ (p - 1) := le_self_pow₀ (by norm_num) (by omega)
  have h1 : δ * (1 + 1 / p) ≤ δ ^ e * (3 / 2) := by nlinarith
  have h2 : (10 : ℝ) ^ (p - 1) * (δ * (1 + 1 / p)) ^ e ≤ 10 ^ (p - 1) * (δ ^ e * (3 / 2)) :=
    mul_le_mul_of_nonneg_left hmul (by positivity)
  nlinarith

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
    have hq : 1 < q 0 := one_lt_of_log_pos hL
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
    have hq0' : 1 < q 0 := one_lt_of_log_pos hL
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
    have hle := Θ_option_le (τ := Fin (n + 1)) hδ0 hδ1 (r := r') hr'0
      (by rw [hr'n]; exact hrlast) (fun j => by rw [hr'n, hr's]; exact hratio' j)
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
      lem6M_lt (p := n + 1 + 1) (by omega) hδ0 (hr0 0) (by
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
      have hql : 1 < q (Fin.last (n + 1)) := one_lt_of_log_pos hLl
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
    have hb := lem7_Φ_bound (p := n + 1 + 1) (by omega) hδ0 hδ1
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
