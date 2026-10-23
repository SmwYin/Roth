import Mathlib.NumberTheory.Real.Irrational
import Mathlib.RingTheory.Algebraic.Integral

import Roth.MainLemma

/-!
# Roth's theorem

If `α` is an irrational real algebraic number and `κ` is a real number such that
`|α - h/q| < 1/q^κ` for infinitely many pairs of integers `(h, q)` with `q > 0`, then `κ ≤ 2`.

## Main results

* `Roth.roth`: Roth's theorem, stated with the set `Roth.approxSet α κ` of pairs `(h, q)`.
* `Roth.roth_rat`: the same statement for rational numbers `x` and their denominators `x.den`.
* `Roth.roth_of_isIntegral`: Roth's theorem for irrational real algebraic integers.

## Proof outline

1. *Reduction* (`Roth.reduction`): replacing `α` by `Mα` for a suitable positive integer `M` and
   `κ` by any `κ' ∈ (2, κ)`, it suffices to treat irrational real algebraic integers.
2. *Parameters*: suppose `κ > 2` and let `f` be a monic integer polynomial of degree `n ≥ 2`
   vanishing at `α`. Choose `m` (`Roth.exists_m`) and then `δ` (`Roth.exists_delta`) satisfying the
   numerical constraints of Roth's argument.
3. *Approximants and degrees*: pick reduced approximations `h_j / q_j` with rapidly increasing
   denominators (`Roth.exists_approximants`) and degrees `r_j` with `r_j log q_j ≈ r_1 log q_1`
   (`Roth.exists_degrees`).
4. *Main lemma*: Roth's Lemma 9 (`Roth.main_lemma`) yields an integer polynomial `Q` of index at
   least `γ - η` at `(α, …, α)`, not vanishing at `(h_1/q_1, …, h_m/q_m)`, with small Hasse
   derivatives at `(α, …, α)`.
5. *Contradiction*: the value `Q(h/q)` is bounded below by `∏ q_j^{-r_j}`
   (`Roth.one_le_prod_pow_mul_abs_eval`) and above via a Taylor expansion at `(α, …, α)`
   (`Roth.abs_eval_lt_of_le_index`); comparing logarithms contradicts the choice of `δ`.

## References

* R. Takloo-Bighash and S. Yin, *Formalizing Roth's theorem*, §6 (Theorem (Roth) and the reduction
  to algebraic integers) and §7 "The proof of Roth's theorem"
  (`.mathlib-quality/references/clean.tex`).
* K. F. Roth, *Rational approximations to algebraic numbers*, Mathematika **2** (1955), 1–20.
-/

namespace Roth

open MvPolynomial

/-- The set of pairs `(h, q)` with `q > 0` and `|α - h/q| < 1/q^κ`, i.e. the approximations of `α`
of quality `κ`. Source: §6, eq. (1). -/
def approxSet (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}

/-- Every real algebraic number has a positive integer multiple that is an algebraic integer.

Source: §6, Lemma ("If `α` is an algebraic number, there is an integer `M > 0` such that `Mα`
is an algebraic integer"). -/
theorem exists_nat_mul_isIntegral {α : ℝ} (hα : IsAlgebraic ℚ α) :
    ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α) := by
  obtain ⟨y, hy, hint⟩ := ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα).exists_integral_multiple
  refine ⟨y.natAbs, Int.natAbs_pos.2 hy, ?_⟩
  simpa [zsmul_eq_mul, ← mul_assoc, ← Int.cast_mul, Int.sign_mul_self] using hint.zsmul y.sign

/-- There are only finitely many approximations `(h, q) ∈ approxSet α κ` with bounded
denominator `q ≤ Q₀`.

Source: §6 ("For a fixed upper bound on `q`, there are only finitely many possible integers
`h` satisfying the approximation inequality"). -/
theorem approxSet_den_le_finite (α κ : ℝ) (Q₀ : ℕ) : {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite := by
  set S : ℝ := ∑ q ∈ Finset.Icc 1 Q₀, 1 / (q : ℝ) ^ κ
  set K : ℤ := ⌈(Q₀ : ℝ) * (|α| + S)⌉
  refine (Finset.finite_toSet (Finset.Icc (-K) K ×ˢ Finset.Icc 1 Q₀)).subset ?_
  rintro ⟨h, q⟩ ⟨⟨hq0, happ⟩, hqQ⟩
  simp only at hq0 happ hqQ
  have hqR : (0 : ℝ) < q := by exact_mod_cast hq0
  have hdiv : |(h : ℝ) / q| ≤ |α| + S := by
    rw [abs_sub_comm] at happ
    linarith only [happ, abs_sub_abs_le_abs_sub ((h : ℝ) / q) α,
      Finset.single_le_sum (f := fun q : ℕ ↦ 1 / (q : ℝ) ^ κ) (fun i _ ↦ by positivity)
        (Finset.mem_Icc.2 ⟨hq0, hqQ⟩)]
  have habs : |(h : ℝ)| ≤ Q₀ * (|α| + S) := by
    have hqQR : (q : ℝ) ≤ Q₀ := by exact_mod_cast hqQ
    have hh : |(h : ℝ)| / q ≤ |α| + S := by simpa [abs_div] using hdiv
    simpa [mul_comm] using ((div_le_iff₀ hqR).1 hh).trans
      (mul_le_mul_of_nonneg_left hqQR ((abs_nonneg _).trans hdiv))
  have hK' : |h| ≤ K := by
    have : ((|h| : ℤ) : ℝ) ≤ K := by
      rw [Int.cast_abs]
      exact habs.trans (Int.le_ceil _)
    exact_mod_cast this
  simp only [Finset.coe_product, Set.mem_prod, Finset.coe_Icc, Set.mem_Icc]
  exact ⟨abs_le.1 hK', hq0, hqQ⟩

/-- If `κ' < κ`, then any fixed real factor `M` can be absorbed into the exponent gap:
`M / q^κ < 1 / q^κ'` for all sufficiently large natural numbers `q`.

Source: §6 ("Pick any `κ'` such that `2 < κ' < κ`. Then for `q` large enough,
`M/q^κ < 1/q^{κ'}`"). -/
theorem eventually_div_rpow_lt {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by
  obtain ⟨N, hN⟩ := Filter.eventually_atTop.1
    (((tendsto_rpow_atTop (sub_pos.2 hκ)).comp tendsto_natCast_atTop_atTop).eventually_gt_atTop M)
  refine ⟨N, fun q hq ↦ ?_⟩
  have hq0 : (0 : ℝ) < q := by exact_mod_cast (Nat.zero_le N).trans_lt hq
  rw [div_lt_iff₀ (Real.rpow_pos_of_pos hq0 κ), one_div_mul_eq_div, ← Real.rpow_sub hq0]
  exact hN q hq.le

/-- A counterexample to Roth's theorem for an irrational real algebraic number yields one for an
irrational real algebraic integer.
The returned exponent may be smaller than the original one.

Source: §6, Lemma ("If the theorem fails, then it also fails for an irrational real algebraic
integer"). -/
theorem reduction {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hκ : 2 < κ)
    (hinf : (approxSet α κ).Infinite) : ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧
    (approxSet α' κ').Infinite := by
  obtain ⟨M, hM0, hMint⟩ := exists_nat_mul_isIntegral halg
  obtain ⟨Q₀, hQ₀⟩ := eventually_div_rpow_lt (M := M) (show (κ + 2) / 2 < κ by linarith)
  refine ⟨M * α, (κ + 2) / 2, hα.natCast_mul hM0.ne', hMint, by linarith, ?_⟩
  refine ((hinf.sdiff (approxSet_den_le_finite α κ Q₀)).image
    ((mul_right_injective₀ (by exact_mod_cast hM0.ne' : (M : ℤ) ≠ 0)).prodMap
      Function.injective_id).injOn).mono ?_
  rintro _ ⟨⟨h, q⟩, ⟨⟨hq0, happ⟩, hnot⟩, rfl⟩
  refine ⟨hq0, ?_⟩
  dsimp only [Prod.map, id]
  push_cast
  rw [mul_div_assoc, ← mul_sub, abs_mul, Nat.abs_cast]
  calc (M : ℝ) * |α - h / q| < M / (q : ℝ) ^ κ := by
        simpa only [mul_one_div] using mul_lt_mul_of_pos_left happ (by positivity : (0 : ℝ) < M)
    _ < 1 / (q : ℝ) ^ ((κ + 2) / 2) := hQ₀ q (not_le.1 fun hc ↦ hnot ⟨⟨hq0, happ⟩, hc⟩)

/-- An algebraic integer is a root of a monic integer polynomial of degree at least `2`.
The witness may be reducible and have larger degree than the minimal polynomial.

Source: §6 ("Since `α` is an algebraic integer, by definition, there is a polynomial
`f(x) = x^n + a_1 x^{n-1} + ⋯ + a_n` with integral coefficients such that `f(α) = 0`. Its degree
`n` is at least `2`, since `α` is irrational"). -/
theorem exists_monic_aeval_eq_zero {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree := by
  obtain ⟨f, hf, hf0⟩ := hint
  refine ⟨f * Polynomial.X ^ 2, hf.mul (Polynomial.monic_X_pow 2), ?_, ?_⟩
  · rw [map_mul, Polynomial.aeval_def, hf0, zero_mul]
  · simp [hf.ne_zero]

private theorem approxSet_num_den_mem_aux {α κ : ℝ} (hκ : 0 ≤ κ) {h : ℤ} {q : ℕ}
    (hq : (h, q) ∈ approxSet α κ) : (((h : ℚ) / q).num, ((h : ℚ) / q).den) ∈ approxSet α κ := by
  set x : ℚ := (h : ℚ) / q
  have hden : x.den ≤ q := Nat.le_of_dvd hq.1 <| Int.natCast_dvd_natCast.1 <| by
    simpa [x, Rat.divInt_eq_div] using Rat.den_dvd h q
  refine ⟨x.den_pos, ?_⟩
  rw [← Rat.cast_def, Rat.cast_div, Rat.cast_intCast, Rat.cast_natCast]
  exact hq.2.trans_le (by gcongr)

/-- If `α` is irrational and `approxSet α κ` is infinite (with `κ > 0`), then it contains reduced
approximations `h / q` with arbitrarily large denominators, supplying coprimality for choosing
successive approximants rather than merely bounding unreduced pairs.

Source: §7, first paragraph ("There are therefore infinitely many distinct reduced solutions
... the reduced denominators are unbounded as well"). -/
theorem exists_reduced_approx {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) : ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧
    IsCoprime hq.1 (hq.2 : ℤ) := by
  by_contra! hcon
  set ρ : ℤ × ℕ → ℚ := fun hq ↦ (hq.1 : ℚ) / hq.2
  have hV : (ρ '' approxSet α κ).Finite := by
    refine ((approxSet_den_le_finite α κ Q₀).image ρ).subset ?_
    rintro _ ⟨hq, hmem, rfl⟩
    -- the reduced form of a solution is a reduced solution
    have hm : ((ρ hq).num, (ρ hq).den) ∈ approxSet α κ :=
      approxSet_num_den_mem_aux hκ.le hmem
    refine ⟨((ρ hq).num, (ρ hq).den), ⟨hm, ?_⟩, ?_⟩
    · by_contra! hc
      exact hcon _ hm hc (Int.isCoprime_iff_gcd_eq_one.2 (ρ hq).reduced)
    · exact Rat.num_div_den (ρ hq)
  have hfib : ∀ x ∈ ρ '' approxSet α κ, {hq ∈ approxSet α κ | ρ hq = x}.Finite := by
    intro x _
    obtain ⟨N, hN⟩ := eventually_div_rpow_lt (M := 1 / |α - (x : ℝ)|) hκ
    refine (approxSet_den_le_finite α κ N).subset ?_
    rintro ⟨h, q⟩ ⟨hm, hρx⟩
    refine ⟨hm, le_of_not_gt fun hq ↦ ?_⟩
    have hbound := hN q hq
    rw [Real.rpow_zero, div_one, div_right_comm,
      div_lt_iff₀ (abs_pos.2 (sub_ne_zero.2 (hα.ne_rat x))), one_mul] at hbound
    exact not_lt_of_gt hbound <| by simpa [← hρx, ρ] using hm.2
  exact hinf (Set.Finite.of_finite_fibers ρ hV hfib)

/-- For `κ > 2` there is a positive integer `m > 16 n²` with `4 n √m < m` and
`2m / (m - 4 n √m) < κ`. The parameter `n` may be zero.

Source: §7, eq. (47) ("We choose a positive integer `m` large enough that `m > 4n m^{1/2}`
and `2m/(m - 4n m^{1/2}) < κ`, which is possible as `κ > 2`"), together with `m > 16n²`. -/
theorem exists_m {n : ℕ} {κ : ℝ} (hκ : 2 < κ) : ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧
    2 * m / (m - 4 * n * √(m : ℝ)) < κ := by
  let s := ⌈4 * κ * n / (κ - 2)⌉₊ + 4 * n + 1
  have hs4 : 4 * n < s := by
    dsimp [s]
    lia
  have hs4R : (4 * n : ℝ) < s := by exact_mod_cast hs4
  have hspos : (0 : ℝ) < s := lt_of_le_of_lt (by positivity) hs4R
  have hkey : 4 * κ * n < (s : ℝ) * (κ - 2) := by
    apply (div_lt_iff₀ (sub_pos.mpr hκ)).mp
    refine (Nat.le_ceil _).trans_lt ?_
    exact_mod_cast (show ⌈4 * κ * n / (κ - 2)⌉₊ < s by
      dsimp [s]
      lia)
  have hmul : 4 * n * (s : ℝ) < (s : ℝ) ^ 2 := by
    simpa [pow_two] using mul_lt_mul_of_pos_right hs4R hspos
  refine ⟨s ^ 2, by nlinarith only [hs4], ?_, ?_⟩
  · simpa using hmul
  · push_cast
    rw [Real.sqrt_sq (Nat.cast_nonneg _), div_lt_iff₀ (sub_pos.mpr hmul)]
    nlinarith only [mul_lt_mul_of_pos_right hkey hspos]

/-- If `δ < c ^ 2 ^ m`, then `η(δ, m) < 10 ^ m * c`. -/
private lemma eta_lt_of_lt {δ c : ℝ} (hδ0 : 0 < δ) (hc : 0 < c) (m : ℕ) (h : δ < c ^ (2 ^ m)) :
    eta δ m < 10 ^ m * c := by
  have hz : (0 : ℝ) < (1 / 2 : ℝ) ^ m := by positivity
  have hpow := Real.rpow_lt_rpow hδ0.le h hz
  rw [← Real.rpow_natCast c (2 ^ m), ← Real.rpow_mul hc.le, Nat.cast_pow, Nat.cast_ofNat,
    ← mul_pow, show (2 : ℝ) * (1 / 2) = 1 by norm_num, one_pow, Real.rpow_one] at hpow
  rw [eta]
  exact mul_lt_mul_of_pos_left hpow (by positivity)

/-- Given `m` as in `Roth.exists_m`, there is `δ ∈ (0, 1/m)` with
`η(δ, m) + 2 (1 + 3δ) n √m < m / 2` and `m (1 + 4δ) / (γ - η) < κ`.

Source: §7, eqs. (29), (30), (48), (49) ("For `δ` small enough ... Decreasing `δ` further if
necessary, we also arrange that `2m(1+4δ)/(m - 4(1+3δ) n m^{1/2} - 2η) < κ` ... equivalent to
`m(1+4δ)/(γ - η) < κ`"). -/
theorem exists_delta {n m : ℕ} (hn : 0 < n) (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (h47 : 4 * n * √(m : ℝ) < m)
    (h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) :
    ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
      (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ := by
  have hm0 : 0 < m := by
    have : 0 < 16 * n ^ 2 := by positivity
    omega
  have hmR : (0 : ℝ) < m := by exact_mod_cast hm0
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hsm : 0 < √(m : ℝ) := Real.sqrt_pos.2 hmR
  have hG : 0 < (m : ℝ) - 4 * n * √(m : ℝ) := by linarith
  have hκ0 : 0 < κ := lt_trans (by positivity) h47'
  set E := κ * (((m : ℝ) - 4 * n * √(m : ℝ)) / 2) - m with hEdef
  have hE : 0 < E := by
    rw [div_lt_iff₀ hG] at h47'
    rw [hEdef]
    linarith
  obtain ⟨δ₀, hδ₀, hδ₀'⟩ := exists_delta_bound hm
  set c : ℝ := E / (3 * κ * 10 ^ m) with hc
  have hc0 : 0 < c := by positivity
  set μ := min δ₀ (min (E / (12 * m)) (min (E / (18 * κ * n * √(m : ℝ))) (c ^ (2 ^ m))))
    with hμ
  have hμ0 : 0 < μ := by
    simp only [hμ, lt_min_iff]
    exact ⟨hδ₀, by positivity, by positivity, by positivity⟩
  have hδ0 : 0 < μ / 2 := by positivity
  have hδlt : μ / 2 < μ := by linarith
  have hδlt' := hδlt
  simp only [hμ, lt_min_iff] at hδlt'
  obtain ⟨h1, h2, h3, h4⟩ := hδlt'
  obtain ⟨h29, h30⟩ := hδ₀' (μ / 2) hδ0.le h1.le
  refine ⟨μ / 2, hδ0, h29, h30, ?_⟩
  set δ := μ / 2
  have hgam := (eta_lt_gam_iff δ n m).1 h30
  have hceq : (10 : ℝ) ^ m * c = E / (3 * κ) := by rw [hc]; field_simp
  have heta := (eta_lt_of_lt hδ0 hc0 m h4).trans_eq hceq
  have a1 : 12 * m * δ < E := by rwa [lt_div_iff₀ (by positivity), mul_comm] at h2
  have a2 : 18 * κ * n * √(m : ℝ) * δ < E := by rwa [lt_div_iff₀ (by positivity), mul_comm] at h3
  have a3 : eta δ m * (3 * κ) < E := by rwa [lt_div_iff₀ (by positivity)] at heta
  rw [div_lt_iff₀ (by linarith)]
  rw [gam, lam]
  rw [hEdef] at a1 a2 a3
  linarith only [a1, a2, a3]

/-- One can choose `m` reduced approximations `h_j / q_j ∈ approxSet α κ` with `q_j > 1`,
`log q_1 > L` and `log q_{j+1} > (2 / δ) log q_j`.

Source: §7 ("pick a reduced solution `h_1, q_1` ... such that `q_1` satisfies (32) ... We then
choose solutions `h_2, q_2; …; h_m, q_m` with `gcd(h_j, q_j) = 1` to satisfy (50)"). -/
theorem exists_approximants {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (hδ : 0 < δ) (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j) := by
  choose g hgmem hglt hgcop using fun Q₀ : ℕ => exists_reduced_approx hα hκ hinf Q₀
  let s : ℕ → ℤ × ℕ := fun k => Nat.rec (g (max ⌈Real.exp L⌉₊ 1))
    (fun _ p => g (max ⌈((p.2 : ℕ) : ℝ) ^ (2 / δ)⌉₊ 1)) k
  have hs0 : s 0 = g (max ⌈Real.exp L⌉₊ 1) := rfl
  have hsS : ∀ k, s (k + 1) = g (max ⌈((s k).2 : ℝ) ^ (2 / δ)⌉₊ 1) := fun k => rfl
  have hmem : ∀ k, s k ∈ approxSet α κ ∧ IsCoprime (s k).1 ((s k).2 : ℤ) ∧ 1 < (s k).2 := by
    rintro (_ | k) <;> exact ⟨hgmem _, hgcop _, (le_max_right _ _).trans_lt (hglt _)⟩
  refine ⟨fun j => (s j).1, fun j => (s j).2, fun j => (hmem j).1, fun j => (hmem j).2.1,
    fun j => (hmem j).2.2, ?_, ?_⟩
  · have hlt : Real.exp L < ((s 0).2 : ℝ) := by
      rw [hs0]
      exact (Nat.le_ceil _).trans_lt (by exact_mod_cast (le_max_left _ _).trans_lt (hglt _))
    have hpos : (0 : ℝ) < ((s 0).2 : ℝ) := lt_trans (Real.exp_pos L) hlt
    exact (Real.lt_log_iff_exp_lt hpos).2 hlt
  · intro i j hij
    simp only
    have hj : (j : ℕ) = (i : ℕ) + 1 := hij.symm
    rw [hj, hsS]
    have hqi : (1 : ℝ) < ((s i).2 : ℝ) := by exact_mod_cast (hmem i).2.2
    have hlt : ((s i).2 : ℝ) ^ (2 / δ) < ((g (max ⌈((s i).2 : ℝ) ^ (2 / δ)⌉₊ 1)).2 : ℝ) :=
      (Nat.le_ceil _).trans_lt (by exact_mod_cast (le_max_left _ _).trans_lt (hglt _))
    have h1 := Real.log_lt_log (by positivity) hlt
    rwa [Real.log_rpow (by linarith)] at h1

/-- Given denominators `q_j` with rapidly increasing logarithms, there are positive degrees `r_j`
with `r_j > 10 / δ`, `r_{j+1} / δ < r_j`, and `r_1 log q_1 ≤ r_j log q_j < (1 + δ/10) r_1 log q_1`.

Source: §7, eqs. (51)–(53) and the Lean note ("define `r_j = ⌈r_1 log q_1 / log q_j⌉` for
`j ≥ 2`, and collect positivity, (31), (33) and (53) in one rounding lemma"). -/
theorem exists_degrees {m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {q : Fin m → ℕ}
    (hq : ∀ j, 1 < q j)
    (h50 : ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j)) :
    ∃ r : Fin m → ℕ, (∀ j, 0 < r j) ∧ (∀ j, 10 / δ < r j) ∧
      (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) ∧
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧
      ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0)) := by
  have hℓ : ∀ j, 0 < Real.log (q j) := fun j => Real.log_pos (by exact_mod_cast hq j)
  set ℓmax := Finset.univ.sup' Finset.univ_nonempty fun j => Real.log (q j)
  have hle : ∀ j, Real.log (q j) ≤ ℓmax := fun j =>
    Finset.le_sup' (fun j => Real.log (q j)) (Finset.mem_univ j)
  set r₀ : ℕ := ⌈10 * ℓmax / (δ * Real.log (q 0))⌉₊ + 1 with hr₀
  have hr₀R : 10 * ℓmax / (δ * Real.log (q 0)) < r₀ := by
    rw [hr₀]
    push_cast
    linarith [Nat.le_ceil (10 * ℓmax / (δ * Real.log (q 0)))]
  have hr₀' : 10 * ℓmax < δ * (r₀ * Real.log (q 0)) := by
    rw [div_lt_iff₀ (mul_pos hδ0 (hℓ 0))] at hr₀R
    linarith
  set r : Fin m → ℕ := fun j => ⌈r₀ * Real.log (q 0) / Real.log (q j)⌉₊ with hr
  have hr0 : r 0 = r₀ := by
    simp only [hr]
    rw [mul_div_assoc, div_self (hℓ 0).ne', mul_one, Nat.ceil_natCast]
  have hlow : ∀ j, (r₀ : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j) := fun j => by
    rw [← div_le_iff₀ (hℓ j)]
    exact Nat.le_ceil _
  have hup : ∀ j, (r j : ℝ) * Real.log (q j) < r₀ * Real.log (q 0) + Real.log (q j) := fun j => by
    have := Nat.ceil_lt_add_one (by positivity : (0 : ℝ) ≤ r₀ * Real.log (q 0) / Real.log (q j))
    have h2 := mul_lt_mul_of_pos_right this (hℓ j)
    rwa [add_mul, one_mul, div_mul_cancel₀ _ (hℓ j).ne'] at h2
  have h53 : ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r₀ * Real.log (q 0)) := fun j => by
    have := hup j
    have := hle j
    linarith
  have h31a : ∀ j, 10 / δ < r j := fun j => by
    rw [div_lt_iff₀ hδ0]
    have h1 := hlow j
    have h2 := hle j
    have h3 : (0 : ℝ) ≤ r j := Nat.cast_nonneg _
    by_contra! hc
    have h4 : (r j : ℝ) * Real.log (q j) ≤ r j * ℓmax := mul_le_mul_of_nonneg_left h2 h3
    have hℓm : 0 ≤ ℓmax := (hℓ 0).le.trans (hle 0)
    have h5 := mul_le_mul_of_nonneg_right hc hℓm
    have h6 := mul_le_mul_of_nonneg_left (h1.trans h4) hδ0.le
    nlinarith
  refine ⟨r, fun j => ?_, h31a, fun i j hij => ?_, fun j => by rw [hr0]; exact hlow j,
    fun j => by rw [hr0]; exact h53 j⟩
  · have := h31a j
    have : (0 : ℝ) < r j := lt_trans (by positivity) this
    exact_mod_cast this
  · have A := h53 j
    have B := hlow i
    have C := h50 i j hij
    have hrj : (0 : ℝ) ≤ r j := Nat.cast_nonneg _
    have hri : (0 : ℝ) ≤ r i := Nat.cast_nonneg _
    have D : 2 * ((r j : ℝ) / δ) * Real.log (q i) ≤ r j * Real.log (q j) := by
      have : 2 * ((r j : ℝ) / δ) * Real.log (q i) = r j * (2 / δ * Real.log (q i)) := by
        field_simp
      rw [this]
      exact mul_le_mul_of_nonneg_left C.le hrj
    have E : 2 * ((r j : ℝ) / δ) < (1 + δ / 10) * r i := by
      by_contra! hc
      have := mul_le_mul_of_nonneg_right hc (hℓ i).le
      nlinarith
    nlinarith

/-- If an integer polynomial `Q` of multidegree at most `r` does not vanish at `h / q`, then
`∏ q_j^{r_j} |Q(h/q)| ≥ 1`.

Source: §7, eq. (54) ("the number `(∏ q_j^{r_j}) Q(h_1/q_1, …, h_m/q_m)` is a nonzero
integer ... Its absolute value is at least `1`"). -/
theorem one_le_prod_pow_mul_abs_eval {m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : Fin m → ℤ) {q : Fin m → ℕ} (hq : ∀ j, 0 < q j)
    (hne : eval (fun j => (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j => (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| := by
  have hqR : ∀ j, (0 : ℝ) < q j := fun j => by exact_mod_cast hq j
  have hP : (0 : ℝ) < ∏ j, (q j : ℝ) ^ r j := Finset.prod_pos fun j _ => pow_pos (hqR j) _
  set N : ℤ := ∑ d ∈ Q.support, Q.coeff d * ∏ j, h j ^ d j * (q j : ℤ) ^ (r j - d j) with hN
  have hNeq : (N : ℝ) = (∏ j, (q j : ℝ) ^ r j) *
      eval (fun j => (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) := by
    rw [eval_eq', support_map_of_injective _ Int.cast_injective, Finset.mul_sum, hN]
    push_cast
    refine Finset.sum_congr rfl fun d hd => ?_
    rw [coeff_map, mul_left_comm, ← Finset.prod_mul_distrib]
    congr 1
    refine Finset.prod_congr rfl fun j _ => ?_
    have hdj : d j ≤ r j := (monomial_le_degreeOf j hd).trans (hQ j)
    rw [← pow_sub_mul_pow (q j : ℝ) hdj, div_pow]
    have := (hqR j).ne'
    field_simp
  have hN0 : N ≠ 0 := by
    intro h0
    rw [h0, Int.cast_zero, eq_comm, mul_eq_zero] at hNeq
    rcases hNeq with h1 | h1
    · exact hP.ne' h1
    · exact hne h1
  have h1 : (1 : ℝ) ≤ |(N : ℝ)| := by
    rw [← Int.cast_abs]
    exact_mod_cast Int.one_le_abs hN0
  rwa [hNeq, abs_mul, abs_of_pos hP] at h1

/-- If `Q` has index at least `c` at `(α, …, α)`, its Hasse derivatives there are bounded by `C`,
and each `h_j / q_j` approximates `α` to order `κ`, then
`|Q(h/q)| < ∏ (r_j + 1) · C · q_1^{-r_1 c κ}`.

Source: §7 ("By (1) of Lemma 9 the terms with `∑ i_j/r_j < γ - η` vanish. In every other
term ... `|∏ (h_j/q_j - α)^{i_j}| < q_1^{-r_1 (γ-η) κ}` ... By using (3) of Lemma 9 we have
`|Q(h/q)| < (r_1+1) ⋯ (r_m+1) B_1^{1+3δ} q_1^{-r_1(γ-η)κ}`"). -/
theorem abs_eval_lt_of_le_index {m : ℕ} [NeZero m] {Q : MvPolynomial (Fin m) ℝ} (hQ : Q ≠ 0)
    {r : Fin m → ℕ} (hr : ∀ j, 0 < r j) (hd : ∀ j, degreeOf j Q ≤ r j) {α : ℝ} {c : ℝ} (hc : 0 < c)
    (hidx : c ≤ index Q (fun _ => α) r) {h : Fin m → ℤ} {q : Fin m → ℕ} (hq : ∀ j, 0 < q j)
    {κ : ℝ} (hκ : 0 < κ) (happ : ∀ j, |α - (h j : ℝ) / q j| < 1 / (q j : ℝ) ^ κ)
    (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) {C : ℝ}
    (hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ => α) (hasseDeriv i Q)| < C) :
    |eval (fun j => (h j : ℝ) / q j) Q| <
      (∏ j, ((r j : ℝ) + 1)) * C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
  have hqR : ∀ j, (0 : ℝ) < q j := fun j => by exact_mod_cast hq j
  have hq1 : (1 : ℝ) ≤ q 0 := by exact_mod_cast hq 0
  have hT : 0 < (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := Real.rpow_pos_of_pos (hqR 0) _
  rw [eval_eq_sum_box (fun _ => α) (fun j => (h j : ℝ) / q j) r Q hd]
  -- each term of the Taylor expansion is small
  have hterm : ∀ d ∈ box r, |eval (fun _ => α) (hasseDeriv d Q) *
      ∏ j, ((h j : ℝ) / q j - α) ^ d j| < C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
    intro d _
    by_cases h0 : eval (fun _ => α) (hasseDeriv d Q) = 0
    · rw [h0, zero_mul, abs_zero]
      exact mul_pos (lt_of_le_of_lt (abs_nonneg _) (hC 0)) hT
    have hw : c ≤ weight r d := hidx.trans (index_le_weight h0)
    rw [abs_mul, Finset.abs_prod]
    refine mul_lt_mul_of_lt_of_le_of_nonneg_of_pos (hC d) ?_ (abs_nonneg _) hT
    calc ∏ j, |((h j : ℝ) / q j - α) ^ d j|
        ≤ ∏ j, (q j : ℝ) ^ (-κ * d j) := by
          refine Finset.prod_le_prod₀ (fun j _ => abs_nonneg _) fun j _ => ?_
          rw [abs_pow, abs_sub_comm, Real.rpow_mul (hqR j).le, Real.rpow_natCast,
            Real.rpow_neg (hqR j).le, ← one_div]
          exact pow_le_pow_left₀ (abs_nonneg _) (happ j).le _
      _ ≤ ∏ j, ((q 0 : ℝ) ^ ((r 0 : ℝ) / r j)) ^ (-κ * d j) := by
          refine Finset.prod_le_prod₀ (fun j _ => by positivity) fun j _ => ?_
          exact Real.rpow_le_rpow_of_nonpos (by positivity) (hqr j)
            (by nlinarith [(Nat.cast_nonneg (d j) : (0 : ℝ) ≤ d j)])
      _ = (q 0 : ℝ) ^ (-(r 0 : ℝ) * κ * weight r d) := by
          have hr' : ∀ j, (0 : ℝ) < r j := fun j => by exact_mod_cast hr j
          simp_rw [← Real.rpow_mul (hqR 0).le]
          rw [← Real.rpow_sum_of_pos (hqR 0), weight, Finset.mul_sum]
          refine congrArg _ (Finset.sum_congr rfl fun j _ => ?_)
          field_simp
      _ ≤ (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
          apply Real.rpow_le_rpow_of_exponent_le hq1
          have : (0 : ℝ) ≤ r 0 * κ := by positivity
          nlinarith
  calc |∑ d ∈ box r, eval (fun _ => α) (hasseDeriv d Q) * ∏ j, ((h j : ℝ) / q j - α) ^ d j|
      ≤ ∑ d ∈ box r, |eval (fun _ => α) (hasseDeriv d Q) * ∏ j, ((h j : ℝ) / q j - α) ^ d j| :=
        Finset.abs_sum_le_sum_abs _ _
    _ < ∑ _d ∈ box r, C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) :=
        Finset.sum_lt_sum_of_nonempty ⟨0, mem_box.2 fun j => Nat.zero_le _⟩ hterm
    _ = (∏ j, ((r j : ℝ) + 1)) * C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
        rw [Finset.sum_const, card_box, nsmul_eq_mul]
        push_cast
        ring

/-- Roth's theorem for irrational real algebraic integers: if `approxSet α κ` is infinite,
then `κ ≤ 2`.

Source: §7 ("This contradicts (49) and finishes the proof of the theorem"). -/
theorem roth_of_isIntegral {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by
  by_contra! hκ
  have hκ0 : 0 < κ := by linarith
  obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint
  set n := f.natDegree
  -- a bound for the coefficients of `f`
  set A : ℝ := 1 + ∑ i ∈ f.support, |((f.coeff i : ℤ) : ℝ)| with hAdef
  have hsum0 : 0 ≤ ∑ i ∈ f.support, |((f.coeff i : ℤ) : ℝ)| :=
    Finset.sum_nonneg fun _ _ => abs_nonneg _
  have hA1 : 1 ≤ A := by linarith
  have hA : ∀ i, |((f.coeff i : ℤ) : ℝ)| ≤ A := fun i => by
    by_cases hi : i ∈ f.support
    · linarith [Finset.single_le_sum (f := fun i => |((f.coeff i : ℤ) : ℝ)|)
        (fun _ _ => abs_nonneg _) hi]
    · simpa [Polynomial.notMem_support_iff.1 hi] using zero_le_one.trans hA1
  -- choice of `m` and `δ`
  obtain ⟨m, hm, h47, h47'⟩ := exists_m (n := n) hκ
  obtain ⟨δ, hδ0, hδm, h30, h49⟩ := exists_delta (by omega : 0 < n) hm h47 h47'
  have hm2 : 2 ≤ m := by
    have : 4 ≤ n ^ 2 := by nlinarith
    omega
  have : NeZero m := ⟨by omega⟩
  have hmR : (2 : ℝ) ≤ m := by exact_mod_cast hm2
  have hδ1 : δ < 1 := hδm.trans_le (by rw [div_le_one (by linarith)]; linarith)
  -- the approximants and the degrees
  obtain ⟨h, q, happ, hcop, hq1, hL, h50⟩ := exists_approximants hα hκ0 hinf m hδ0
    ((2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|)) / δ ^ 2)
  have h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) <
      δ ^ 2 * Real.log (q 0) := by
    rw [div_lt_iff₀ (by positivity)] at hL
    linarith
  obtain ⟨r, hr0, h31a, h31b, h33, h53⟩ := exists_degrees hδ0 hδ1 hq1 h50
  have hq0 : ∀ j, 0 < q j := fun j => lt_trans zero_lt_one (hq1 j)
  -- Lemma 9
  obtain ⟨Q, hQ0, hQd, hidx_strict, hne, hC⟩ := main_lemma hf hfα hA hδ0.le hδm.le (by
      have hj : (3 : ℝ) ≤ r (Fin.rev 0) := (by norm_num : (3 : ℝ) ≤ 10).trans
        ((le_div_self (by norm_num) hδ0 hδ1.le).trans (h31a (Fin.rev 0)).le)
      exact_mod_cast hj)
    (fun i j hij ↦ (h31b i j hij).le) h32.le h33 hcop
  have hidx := hidx_strict.le
  set G := gam δ n m - eta δ m
  have hG0 : 0 < G := by
    have := (eta_lt_gam_iff δ n m).1 h30
    linarith
  set B := B₁ δ (q 0) (r 0)
  have hqR : ∀ j, (0 : ℝ) < q j := fun j => by exact_mod_cast hq0 j
  have hℓ : ∀ j, 0 < Real.log (q j) := fun j => Real.log_pos (by exact_mod_cast hq1 j)
  have hr0R : (0 : ℝ) < r 0 := by exact_mod_cast hr0 0
  -- `B` is at most `q_0^{δ r_0}` and `∏ (r_j + 1) < B^δ`
  have hlogA : 0 ≤ Real.log (1 + A) := Real.log_nonneg (by linarith)
  have hlogα : 0 ≤ Real.log (1 + |α|) := Real.log_nonneg (by linarith [abs_nonneg α])
  have hm1 : 1 ≤ m := by omega
  have hmR' : (0 : ℝ) ≤ m := by positivity
  have h32' : (2 * (m : ℝ) + 1) < δ ^ 2 * Real.log (q 0) := by
    have := mul_nonneg hmR' hlogA
    have := mul_nonneg hmR' hlogα
    linarith
  have hX := four_lt_rpow hδ0.le (hr0 0) (by
    linarith only [h32', show (1 : ℝ) ≤ m by exact_mod_cast hm1])
  obtain ⟨hsqB, hBX⟩ := sqrt_lt_floor (hX.le.trans' (by norm_num))
  change √((q 0 : ℝ) ^ (δ * r 0)) < (B : ℝ) at hsqB
  change (B : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) at hBX
  have hBpos : (0 : ℝ) < B := lt_of_le_of_lt (Real.sqrt_nonneg _) hsqB
  obtain ⟨hT2, -, -⟩ := three_small_factors hδ0.le (hr0 0) (zero_le_one.trans hA1) h32.le
  have hstep : ∀ i j : Fin m, i.val + 1 = j.val → r j ≤ r i := fun i j hij => by
    exact_mod_cast (le_div_self (Nat.cast_nonneg _) hδ0 hδ1.le).trans (h31b i j hij).le
  have hr0max : ∀ j, r j ≤ r 0 := by
    have key : ∀ k (hk : k < m), r ⟨k, hk⟩ ≤ r 0 := by
      intro k
      induction k with
      | zero => intro hk; exact (congrArg r (Fin.ext (by simp))).le
      | succ k ih => intro hk; exact (hstep ⟨k, by omega⟩ ⟨k + 1, hk⟩ rfl).trans (ih (by omega))
    exact fun j => key j.val j.isLt
  have hsumr : ∑ j, r j ≤ m * r 0 :=
    (Finset.sum_le_sum fun j _ => hr0max j).trans_eq (by simp)
  have hN : (∏ j, ((r j : ℝ) + 1)) < (B : ℝ) ^ δ := by
    have h1 : ∏ j, (r j + 1) ≤ 2 ^ (∑ j, r j) := by
      rw [← Finset.prod_pow_eq_pow_sum]
      exact Finset.prod_le_prod fun j _ => Nat.lt_two_pow_self
    have h2 : (∏ j, ((r j : ℝ) + 1)) ≤ 2 ^ (∑ j, r j) := by exact_mod_cast h1
    have h3 : (2 : ℝ) ^ (∑ j, r j) ≤ 2 ^ (m * r 0) := pow_le_pow_right₀ (by norm_num) hsumr
    exact lt_of_le_of_lt (h2.trans h3) hT2
  -- the upper bound
  have hmapQ : map (Int.castRingHom ℝ) Q ≠ 0 := fun h0 =>
    hQ0 (MvPolynomial.map_injective _ Int.cast_injective (h0.trans (map_zero _).symm))
  have hdmap : ∀ j, degreeOf j (map (Int.castRingHom ℝ) Q) ≤ r j := fun j => by
    rw [degreeOf_eq_sup, support_map_of_injective _ Int.cast_injective, ← degreeOf_eq_sup]
    exact hQd j
  have hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j := fun j => by
    have hrj : (0 : ℝ) < r j := by exact_mod_cast hr0 j
    rw [← Real.exp_log (hqR j), Real.rpow_def_of_pos (hqR 0), Real.exp_le_exp, mul_div_assoc',
      div_le_iff₀ hrj]
    linarith [h33 j]
  have hupper := abs_eval_lt_of_le_index hmapQ hr0 hdmap hG0 hidx hq0 hκ0
    (fun j => (happ j).2) hqr hC
  have hlower := one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne
  -- take logarithms
  set P := ∏ j, (q j : ℝ) ^ r j with hP
  have hP0 : 0 < P := Finset.prod_pos fun j _ => pow_pos (hqR j) _
  set N' := ∏ j, ((r j : ℝ) + 1)
  have hN'0 : 0 < N' := Finset.prod_pos fun j _ => by positivity
  set T := (q 0 : ℝ) ^ (-(r 0 : ℝ) * G * κ)
  have hT0 : 0 < T := Real.rpow_pos_of_pos (hqR 0) _
  have hBc0 : 0 < (B : ℝ) ^ (1 + 3 * δ) := Real.rpow_pos_of_pos hBpos _
  have hone : 1 < P * (N' * (B : ℝ) ^ (1 + 3 * δ) * T) :=
    lt_of_le_of_lt hlower (mul_lt_mul_of_pos_left hupper hP0)
  have hlog := Real.log_pos hone
  rw [Real.log_mul hP0.ne' (by positivity), Real.log_mul (by positivity) hT0.ne',
    Real.log_mul hN'0.ne' hBc0.ne'] at hlog
  have hlogP : Real.log P < m * ((1 + δ / 10) * (r 0 * Real.log (q 0))) := by
    rw [hP, Real.log_prod (fun j _ => (pow_pos (hqR j) _).ne')]
    simp only [Real.log_pow]
    calc ∑ j, (r j : ℝ) * Real.log (q j) < ∑ _j : Fin m, (1 + δ / 10) * (r 0 * Real.log (q 0)) :=
          Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty fun j _ => h53 j
      _ = m * ((1 + δ / 10) * (r 0 * Real.log (q 0))) := by simp
  have hlogN : Real.log N' < δ * Real.log B := by
    rw [← Real.log_rpow hBpos]
    exact Real.log_lt_log hN'0 hN
  have hlogB : Real.log B ≤ δ * r 0 * Real.log (q 0) := by
    rw [← Real.log_rpow (hqR 0)]
    exact Real.log_le_log hBpos hBX
  rw [Real.log_rpow hBpos, Real.log_rpow (hqR 0)] at hlog
  have hK0 : 0 < (r 0 : ℝ) * Real.log (q 0) := mul_pos hr0R (hℓ 0)
  have hkey : 0 < ((r 0 : ℝ) * Real.log (q 0)) *
      (m * (1 + δ / 10) + (1 + 4 * δ) * δ - G * κ) := by
    have h1 : (1 + 4 * δ) * Real.log B ≤ (1 + 4 * δ) * (δ * r 0 * Real.log (q 0)) :=
      mul_le_mul_of_nonneg_left hlogB (by positivity)
    linarith
  have hpos : 0 < m * (1 + δ / 10) + (1 + 4 * δ) * δ - G * κ := pos_of_mul_pos_right hkey hK0.le
  rw [div_lt_iff₀ hG0] at h49
  have h2 : (1 + 4 * δ) * δ ≤ (39 / 10) * m * δ :=
    mul_le_mul_of_nonneg_right (by linarith) hδ0.le
  linarith

/-- **Roth's theorem.** If `α` is an irrational real algebraic number and `|α - h/q| < 1/q^κ` has
infinitely many solutions `(h, q)` with `q > 0`, then `κ ≤ 2`.

This is the main theorem of the project.

Source: §6, Theorem (Roth) ("Let `α` be an irrational real algebraic number
and let `κ ∈ ℝ`. Suppose there are infinitely many pairs of integers `h, q` with `q > 0` such that
`|α - h/q| < 1/q^κ`. Then `κ ≤ 2`"). -/
theorem roth {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by
  by_contra! hκ
  obtain ⟨α', κ', hα', hint', hκ', hinf'⟩ := reduction hα halg hκ hinf
  exact (roth_of_isIntegral hα' hint' hinf').not_gt hκ'

/-- Roth's theorem for rational approximations: if `|α - x| < 1 / x.den ^ κ` for infinitely many
rationals `x`, where `α` is an irrational real algebraic number, then `κ ≤ 2`. -/
theorem roth_rat {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 := by
  have hinj : Function.Injective fun x : ℚ => (x.num, x.den) := fun x y hxy =>
    Rat.ext (congrArg Prod.fst hxy) (congrArg Prod.snd hxy)
  refine roth hα halg ((hinf.image hinj.injOn).mono ?_)
  rintro _ ⟨x, hx, rfl⟩
  exact ⟨x.den_pos, by rwa [← Rat.cast_def]⟩

end Roth
