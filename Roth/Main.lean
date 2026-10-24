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
  have hspos : (0 : ℝ) < s := (mul_nonneg (by norm_num) (Nat.cast_nonneg n)).trans_lt hs4R
  have hkey : 4 * κ * n < (s : ℝ) * (κ - 2) := by
    apply (div_lt_iff₀ (sub_pos.mpr hκ)).mp
    refine (Nat.le_ceil _).trans_lt ?_
    exact_mod_cast (show ⌈4 * κ * n / (κ - 2)⌉₊ < s by
      dsimp [s]
      lia)
  have hmul : 4 * n * (s : ℝ) < (s : ℝ) ^ 2 := by
    simpa only [pow_two] using mul_lt_mul_of_pos_right hs4R hspos
  refine ⟨s ^ 2, ?_, ?_, ?_⟩
  · simpa only [mul_pow, show (4 : ℕ) ^ 2 = 16 from rfl] using
      Nat.pow_lt_pow_left hs4 (by decide : 2 ≠ 0)
  · simpa only [Nat.cast_pow, Real.sqrt_sq (Nat.cast_nonneg s)] using hmul
  · push_cast
    rw [Real.sqrt_sq (Nat.cast_nonneg _), div_lt_iff₀ (sub_pos.mpr hmul)]
    nlinarith only [mul_lt_mul_of_pos_right hkey hspos]

/-- Given `m` as in `Roth.exists_m`, there is `δ ∈ (0, 1/m)` with
`η(δ, m) + 2 (1 + 3δ) n √m < m / 2` and `m (1 + 4δ) / (γ - η) < κ`.
The parameter `n` may be zero.

Source: §7, eqs. (29), (30), (48), (49) ("For `δ` small enough ... Decreasing `δ` further if
necessary, we also arrange that `2m(1+4δ)/(m - 4(1+3δ) n m^{1/2} - 2η) < κ` ... equivalent to
`m(1+4δ)/(γ - η) < κ`"). -/
theorem exists_delta {n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
    (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ := by
  obtain ⟨δ₀, hδ₀, hδ₀'⟩ := exists_delta_bound hm
  have hc : ContinuousAt (fun δ ↦
      (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m)) 0 :=
    (show ContinuousAt (fun δ : ℝ ↦ (m : ℝ) * (1 + 4 * δ)) 0 from
      continuousAt_const.mul (continuousAt_const.add (continuousAt_const.mul continuousAt_id))).div
      ((show ContinuousAt (fun δ ↦ gam δ n m) 0 from
        (continuousAt_const.sub (((continuousAt_const.mul
          (continuousAt_const.add (continuousAt_const.mul continuousAt_id))).mul
            continuousAt_const).mul continuousAt_const)).div_const 2).sub
        ((Real.continuousAt_rpow_const 0 _ (.inr (by positivity))).const_mul _))
      (sub_pos.mpr ((eta_lt_gam_iff 0 n m).mp (hδ₀' 0 le_rfl hδ₀.le).2)).ne'
  obtain ⟨ε, hε, hbound⟩ := Metric.eventually_nhds_iff.mp
    (hc.eventually_lt continuousAt_const (by
      simpa [gam, lam, eta, Real.zero_rpow (by positivity : (1 / 2 : ℝ) ^ m ≠ 0),
        div_div_eq_mul_div, mul_comm] using h47'))
  obtain ⟨δ, hδ, hlt⟩ := exists_between (lt_min hδ₀ hε)
  obtain ⟨h29, h30⟩ := hδ₀' δ hδ.le (hlt.trans_le (min_le_left _ _)).le
  exact ⟨δ, hδ, h29, h30,
    hbound (y := δ) (by simpa [Real.dist_eq, abs_of_pos hδ] using hlt.trans_le (min_le_right _ _))⟩

/-- One can choose `m` reduced approximations `h_j / q_j ∈ approxSet α κ` with `q_j > 1`,
`log q_1 > L` and `log q_{j+1} > (2 / δ) log q_j`.

Source: §7 ("pick a reduced solution `h_1, q_1` ... such that `q_1` satisfies (32) ... We then
choose solutions `h_2, q_2; …; h_m, q_m` with `gcd(h_j, q_j) = 1` to satisfy (50)"). -/
theorem exists_approximants {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧ ∀ i j : Fin m,
      i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j) := by
  choose g hgmem hglt hgcop using fun Q₀ : ℕ ↦ exists_reduced_approx hα hκ hinf Q₀
  let s : ℕ → ℤ × ℕ := Nat.rec (g (max ⌈Real.exp L⌉₊ 1))
    (fun _ p ↦ g (max ⌈(p.2 : ℝ) ^ (2 / δ)⌉₊ 1))
  have hmem : ∀ k, s k ∈ approxSet α κ ∧ IsCoprime (s k).1 ((s k).2 : ℤ) ∧ 1 < (s k).2 := by
    rintro (_ | k) <;> exact ⟨hgmem _, hgcop _, (le_max_right _ _).trans_lt (hglt _)⟩
  refine ⟨fun j ↦ (s j).1, fun j ↦ (s j).2, fun j ↦ (hmem j).1, fun j ↦ (hmem j).2.1,
    fun j ↦ (hmem j).2.2, ?_, ?_⟩
  · have hlt : Real.exp L < ((g (max ⌈Real.exp L⌉₊ 1)).2 : ℝ) :=
      (Nat.le_ceil _).trans_lt (by exact_mod_cast (le_max_left _ _).trans_lt (hglt _))
    exact (Real.lt_log_iff_exp_lt ((Real.exp_pos L).trans hlt)).2 hlt
  · intro i j hij
    change 2 / δ * Real.log ((s i).2) < Real.log ((s j).2)
    rw [hij.symm]
    apply Real.lt_log_of_rpow_lt (by exact_mod_cast zero_lt_one.trans (hmem i).2.2)
    exact (Nat.le_ceil _).trans_lt (by exact_mod_cast (le_max_left _ _).trans_lt (hglt _))

/-- Given denominators `q_j` with rapidly increasing logarithms, there are positive degrees `r_j`
with `r_j > 10 / δ`, `r_{j+1} / δ < r_j`, and `r_1 log q_1 ≤ r_j log q_j < (1 + δ/10) r_1 log q_1`.

Source: §7, eqs. (51)–(53) and the Lean note ("define `r_j = ⌈r_1 log q_1 / log q_j⌉` for
`j ≥ 2`, and collect positivity, (31), (33) and (53) in one rounding lemma"). -/
theorem exists_degrees {m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) {q : Fin m → ℕ}
    (hq : ∀ j, 1 < q j) (h50 : ∀ i j : Fin m, i.val + 1 = j.val →
      2 / δ * Real.log (q i) ≤ Real.log (q j)) : ∃ r : Fin m → ℕ, (∀ j, 0 < r j) ∧
      (∀ j, 10 / δ < r j) ∧ (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) ∧
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧ ∀ j,
      (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0)) := by
  let ℓ (j) := Real.log (q j)
  have hℓ : ∀ j, 0 < ℓ j := fun j ↦ Real.log_pos (by exact_mod_cast hq j)
  obtain ⟨s, hs⟩ := exists_nat_gt (Finset.univ.sup' Finset.univ_nonempty (10 * ℓ · / (δ * ℓ 0)))
  have hS (j) : 10 * ℓ j < ((s : ℝ) * ℓ 0) * δ := by
    simpa only [mul_assoc, mul_comm δ] using (div_lt_iff₀ (mul_pos hδ0 (hℓ 0))).1
      ((Finset.le_sup' _ (Finset.mem_univ j)).trans_lt hs)
  let r : Fin m → ℕ := fun j ↦ ⌈s * ℓ 0 / ℓ j⌉₊
  have hr0 : r 0 = s := by simp only [r, mul_div_cancel_right₀ _ (hℓ 0).ne', Nat.ceil_natCast]
  have hlow (j) := (div_le_iff₀ (hℓ j)).1 (Nat.le_ceil (s * ℓ 0 / ℓ j))
  have hup (j) : (r j : ℝ) * ℓ j < (1 + δ / 10) * (s * ℓ 0) := by
    refine (mul_lt_mul_of_pos_right (Nat.ceil_lt_add_one (by positivity)) (hℓ j)).trans_le ?_
    rw [add_mul, one_mul, div_mul_cancel₀ _ (hℓ j).ne', add_mul, one_mul]
    refine add_le_add le_rfl ?_
    rw [div_mul_eq_mul_div, le_div_iff₀ (by norm_num : (0 : ℝ) < 10)]
    simpa only [mul_comm] using (hS j).le
  have hlarge (j) : 10 / δ < r j := by
    refine (div_lt_iff₀ hδ0).2 ((mul_lt_mul_iff_left₀ (hℓ j)).1 ?_)
    simpa only [mul_right_comm] using (hS j).trans_le (mul_le_mul_of_nonneg_right (hlow j) hδ0.le)
  refine ⟨r, fun j ↦ ?_, hlarge, fun i j hij ↦ ?_, ?_⟩
  · exact_mod_cast (div_pos (by norm_num : (0 : ℝ) < 10) hδ0).trans (hlarge j)
  · have h : (r j : ℝ) * (2 / δ) < (1 + δ / 10) * r i := by
      apply (mul_lt_mul_iff_left₀ (hℓ i)).1
      simpa only [mul_assoc] using
        (mul_le_mul_of_nonneg_left (h50 i j hij) (Nat.cast_nonneg (r j))).trans_lt
          ((hup j).trans_le (mul_le_mul_of_nonneg_left (hlow i) (by positivity)))
    rw [← mul_div_assoc, mul_comm (r j : ℝ) 2, mul_div_assoc] at h
    exact (mul_lt_mul_iff_right₀ (by norm_num : (0 : ℝ) < 2)).1 <| h.trans_le
      (mul_le_mul_of_nonneg_right ((add_le_add le_rfl
        (div_le_div_of_nonneg_right hδ1 (by norm_num))).trans (by norm_num)) (Nat.cast_nonneg _))
  · simpa only [hr0] using And.intro hlow hup

/-- If an integer polynomial `Q` of multidegree at most `r` does not vanish at `h / q`, then
`∏ q_j^{r_j} |Q(h/q)| ≥ 1`.

Source: §7, eq. (54) ("the number `(∏ q_j^{r_j}) Q(h_1/q_1, …, h_m/q_m)` is a nonzero
integer ... Its absolute value is at least `1`"). -/
theorem one_le_prod_pow_mul_abs_eval {m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : Fin m → ℤ) {q : Fin m → ℕ} (hq : ∀ j, 0 < q j)
    (hne : eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| := by
  have hqR : ∀ j, (0 : ℝ) < q j := fun j ↦ by exact_mod_cast hq j
  have hP : (0 : ℝ) < ∏ j, (q j : ℝ) ^ r j := Finset.prod_pos fun j _ ↦ pow_pos (hqR j) _
  set N : ℤ := ∑ d ∈ Q.support, Q.coeff d * ∏ j, h j ^ d j * (q j : ℤ) ^ (r j - d j) with hN
  have hNeq : (N : ℝ) = (∏ j, (q j : ℝ) ^ r j) *
      eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) := by
    rw [eval_eq', support_map_of_injective _ Int.cast_injective, Finset.mul_sum, hN]
    push_cast
    refine Finset.sum_congr rfl fun d hd ↦ ?_
    rw [coeff_map, mul_left_comm, ← Finset.prod_mul_distrib]
    congr 1
    refine Finset.prod_congr rfl fun j _ ↦ ?_
    rw [← pow_sub_mul_pow (q j : ℝ) ((monomial_le_degreeOf j hd).trans (hQ j)), div_pow]
    rw [mul_assoc, mul_div_cancel₀ _ (pow_ne_zero _ (hqR j).ne'), mul_comm]
  have h1 : (1 : ℝ) ≤ |(N : ℝ)| := by
    rw [← Int.cast_abs]
    exact_mod_cast Int.one_le_abs (Int.cast_ne_zero.mp (hNeq.symm ▸ mul_ne_zero hP.ne' hne))
  rwa [hNeq, abs_mul, abs_of_pos hP] at h1

-- Denominator growth converts coordinate bounds into decay governed by the monomial weight.
private lemma abs_prod_pow_le_rpow_of_le_weight {m : ℕ} [NeZero m] {r q : Fin m → ℕ}
    (hq : ∀ j, 0 < q j) {κ : ℝ} (hκ : 0 ≤ κ) {x : Fin m → ℝ} (hx : ∀ j, |x j| ≤ 1 / (q j : ℝ) ^ κ)
    (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) (d : Fin m →₀ ℕ) {c : ℝ} (hw : c ≤ weight r d)
    : |∏ j, x j ^ d j| ≤ (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
  have hqR : ∀ j, (0 : ℝ) < q j := fun j ↦ by exact_mod_cast hq j
  have hq1 : (1 : ℝ) ≤ q 0 := by exact_mod_cast hq 0
  rw [Finset.abs_prod]
  calc ∏ j, |x j ^ d j|
      ≤ ∏ j, (q j : ℝ) ^ (-κ * d j) := by
        refine Finset.prod_le_prod₀ (fun j _ ↦ abs_nonneg _) fun j _ ↦ ?_
        rw [abs_pow, Real.rpow_mul (hqR j).le, Real.rpow_natCast,
          Real.rpow_neg (hqR j).le, ← one_div]
        exact pow_le_pow_left₀ (abs_nonneg _) (hx j) _
    _ ≤ ∏ j, ((q 0 : ℝ) ^ ((r 0 : ℝ) / r j)) ^ (-κ * d j) := by
        refine Finset.prod_le_prod₀ (fun j _ ↦ by positivity) fun j _ ↦ ?_
        exact Real.rpow_le_rpow_of_nonpos (by positivity) (hqr j)
          (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.2 hκ) (Nat.cast_nonneg _))
    _ = (q 0 : ℝ) ^ (-(r 0 : ℝ) * κ * weight r d) := by
        simp_rw [← Real.rpow_mul (hqR 0).le]
        rw [← Real.rpow_sum_of_pos (hqR 0), weight, Finset.mul_sum]
        exact congrArg _ (Finset.sum_congr rfl fun j _ ↦ by ring)
    _ ≤ (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
        apply Real.rpow_le_rpow_of_exponent_le hq1
        convert mul_le_mul_of_nonpos_left hw
          (neg_nonpos.2 (mul_nonneg (Nat.cast_nonneg (r 0)) hκ)) using 1 <;> ring

/-- If `Q` has index at least `c` at `(α, …, α)`, its Hasse derivatives there are bounded by `C`,
and each `h_j / q_j` approximates `α` to order `κ`, then
`|Q(h/q)| < ∏ (r_j + 1) · C · q_1^{-r_1 c κ}`.

Source: §7 ("By (1) of Lemma 9 the terms with `∑ i_j/r_j < γ - η` vanish. In every other
term ... `|∏ (h_j/q_j - α)^{i_j}| < q_1^{-r_1 (γ-η) κ}` ... By using (3) of Lemma 9 we have
`|Q(h/q)| < (r_1+1) ⋯ (r_m+1) B_1^{1+3δ} q_1^{-r_1(γ-η)κ}`"). -/
theorem abs_eval_lt_of_le_index {m : ℕ} [NeZero m] {Q : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ}
    (hd : ∀ j, degreeOf j Q ≤ r j) {α c : ℝ} (hidx : c ≤ index Q (fun _ ↦ α) r) {h : Fin m → ℤ}
    {q : Fin m → ℕ} (hq : ∀ j, 0 < q j) {κ : ℝ} (hκ : 0 ≤ κ)
    (happ : ∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ)
    (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) {C : ℝ}
    (hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ ↦ α) (hasseDeriv i Q)| < C) :
    |eval (fun j ↦ (h j : ℝ) / q j) Q| < (∏ j, ((r j : ℝ) + 1)) * C *
      (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
  have hT : 0 < (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) :=
    Real.rpow_pos_of_pos (by exact_mod_cast hq 0) _
  rw [eval_eq_sum_box (fun _ ↦ α) (fun j ↦ (h j : ℝ) / q j) r Q hd]
  -- each term of the Taylor expansion is small
  have hterm : ∀ d ∈ box r, |eval (fun _ ↦ α) (hasseDeriv d Q) *
      ∏ j, ((h j : ℝ) / q j - α) ^ d j| < C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by
    intro d _
    by_cases h0 : eval (fun _ ↦ α) (hasseDeriv d Q) = 0
    · rw [h0, zero_mul, abs_zero]
      exact mul_pos (lt_of_le_of_lt (abs_nonneg _) (hC 0)) hT
    rw [abs_mul]
    exact mul_lt_mul_of_lt_of_le_of_nonneg_of_pos (hC d)
      (abs_prod_pow_le_rpow_of_le_weight hq hκ (fun j ↦ by
        simpa only [abs_sub_comm] using happ j) hqr d (hidx.trans (index_le_weight h0)))
      (abs_nonneg _) hT
  refine (Finset.abs_sum_le_sum_abs _ _).trans_lt ?_
  convert Finset.sum_lt_sum_of_nonempty ⟨0, mem_box.2 fun j ↦ Nat.zero_le _⟩ hterm using 1
  rw [Finset.sum_const, card_box, nsmul_eq_mul]
  push_cast
  ring

-- Choose the polynomial, coefficient bound, dimension and delta with compatible constraints.
private lemma exists_roth_parameters_aux {α κ : ℝ} (hint : IsIntegral ℤ α) (hκ : 2 < κ) :
    ∃ (f : Polynomial ℤ) (A : ℝ) (m : ℕ) (δ : ℝ), f.Monic ∧ Polynomial.aeval α f = 0 ∧ 1 ≤ A ∧
      (∀ i, |(f.coeff i : ℝ)| ≤ A) ∧ 2 ≤ m ∧ 0 < δ ∧ δ < 1 / m ∧
      eta δ m + 2 * (1 + 3 * δ) * f.natDegree * √(m : ℝ) < m / 2 ∧
      (m : ℝ) * (1 + 4 * δ) / (gam δ f.natDegree m - eta δ m) < κ := by
  obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint
  -- a bound for the coefficients of `f`
  let A : ℝ := 1 + ∑ i ∈ f.support, |(f.coeff i : ℝ)|
  -- choice of `m` and `δ`
  obtain ⟨m, hm, -, h47'⟩ := exists_m (n := f.natDegree) hκ
  obtain ⟨δ, hδ0, hδm, h30, h49⟩ := exists_delta hm h47'
  refine ⟨f, A, m, δ, hf, hfα, ?_, ?_, ?_, hδ0, hδm, h30, h49⟩
  · exact le_add_of_nonneg_right (Finset.sum_nonneg fun _ _ ↦ abs_nonneg _)
  · intro i
    exact (Finsupp.single_eval_le_sum f.toFinsupp.coeff (g := fun z : ℤ ↦ |(z : ℝ)|)
      (by simp) (fun _ ↦ abs_nonneg _) i).trans (le_add_of_nonneg_left zero_le_one)
  · nlinarith only [hm, hdeg]

-- Choose reduced approximants and balanced positive degrees with compatible growth bounds.
private lemma exists_roth_approximants_aux {α κ : ℝ} (hα : Irrational α) (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1)
    (A : ℝ) : ∃ (h : Fin m → ℤ) (q r : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ (∀ j, 0 < r j) ∧ 3 ≤ r (Fin.rev 0) ∧
      (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) ∧ (∀ j, r j ≤ r 0) ∧
      (2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) < δ ^ 2 * Real.log (q 0)) ∧
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧
      ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0)) := by
  -- the approximants and the degrees
  obtain ⟨h, q, happ, hcop, hq1, hL, h50⟩ := exists_approximants hα hκ hinf m
    ((2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|)) / δ ^ 2)
  obtain ⟨r, hr0, h31a, h31b, h33, h53⟩ := exists_degrees hδ0 hδ1 hq1
    (fun i j hij ↦ (h50 i j hij).le)
  have hranti : Antitone r := by
    obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (NeZero.ne m)
    refine Fin.antitone_iff_succ_le.2 fun i ↦ ?_
    exact_mod_cast (le_div_self (Nat.cast_nonneg _) hδ0 hδ1).trans
      (h31b i.castSucc i.succ rfl).le
  refine ⟨h, q, r, happ, hcop, hq1, hr0, ?_, fun i j hij ↦ (h31b i j hij).le,
    fun j ↦ hranti (Fin.zero_le j), (div_lt_iff₀' (by positivity)).1 hL, h33, h53⟩
  exact_mod_cast (by norm_num : (3 : ℝ) ≤ 10).trans
    ((le_div_self (by norm_num) hδ0 hδ1).trans (h31a (Fin.rev 0)).le)

-- Compare the nonzero integral value from Lemma 9 with its Taylor upper bound.
private lemma one_lt_roth_eval_bound_aux {α κ : ℝ} {f : Polynomial ℤ} (hf : f.Monic)
    (hfα : Polynomial.aeval α f = 0) {A : ℝ} (hA : ∀ i, |(f.coeff i : ℝ)| ≤ A) {m : ℕ} [NeZero m]
    {δ : ℝ} (hδ0 : 0 ≤ δ) (hδm : δ ≤ 1 / m) {r : Fin m → ℕ} (hr0 : ∀ j, 0 < r j)
    (hrlast : 3 ≤ r (Fin.rev 0)) (h31b : ∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i)
    {q : Fin m → ℕ} (hq0 : ∀ j, 0 < q j) (hκ0 : 0 ≤ κ) {h : Fin m → ℤ}
    (happ : ∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ) (hcop : ∀ j, IsCoprime (h j) (q j : ℤ))
    (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤
      δ ^ 2 * Real.log (q 0)) (h33 : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) :
    1 < (∏ j, (q j : ℝ) ^ r j) * ((∏ j, ((r j : ℝ) + 1)) * (B₁ δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ) *
      (q 0 : ℝ) ^ (-(r 0 : ℝ) * (gam δ f.natDegree m - eta δ m) * κ)) := by
  -- Lemma 9
  obtain ⟨Q, -, hQd, hidx_strict, hne, hC⟩ :=
    main_lemma hf hfα hA hδ0 hδm hrlast h31b h32 h33 hcop
  have hqR : ∀ j, (0 : ℝ) < q j := fun j ↦ by exact_mod_cast hq0 j
  -- the upper bound
  have hdmap : ∀ j, degreeOf j (map (Int.castRingHom ℝ) Q) ≤ r j := fun j ↦ by
    rw [degreeOf_eq_sup, support_map_of_injective _ Int.cast_injective, ← degreeOf_eq_sup]
    exact hQd j
  have hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j := fun j ↦ by
    have hrj : (0 : ℝ) < r j := by exact_mod_cast hr0 j
    rw [Real.rpow_le_iff_le_log (hqR 0) (hqR j), div_mul_eq_mul_div, div_le_iff₀ hrj]
    linarith [h33 j]
  exact (one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne).trans_lt
    (mul_lt_mul_of_pos_left (abs_eval_lt_of_le_index hdmap hidx_strict.le hq0 hκ0 happ hqr hC)
      (Finset.prod_pos fun j _ ↦ pow_pos (hqR j) _))

-- Bound the common coefficient scale and the product of degree factors.
private lemma roth_product_bound_aux {m : ℕ} [NeZero m] {α A δ : ℝ} (hδ0 : 0 ≤ δ) (hA : 0 ≤ A)
    {q r : Fin m → ℕ} (hr0 : 0 < r 0) (hr0max : ∀ j, r j ≤ r 0)
    (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤
      δ ^ 2 * Real.log (q 0)) : 0 < (B₁ δ (q 0) (r 0) : ℝ) ∧
      (B₁ δ (q 0) (r 0) : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) ∧
      (∏ j, ((r j : ℝ) + 1)) < (B₁ δ (q 0) (r 0) : ℝ) ^ δ := by
  -- `B` is at most `q_0^{δ r_0}` and `∏ (r_j + 1) < B^δ`
  have hm1 : (1 : ℝ) ≤ m := by exact_mod_cast Nat.one_le_iff_ne_zero.2 (NeZero.ne m)
  have h32' : 3 ≤ δ ^ 2 * Real.log (q 0) := by
    have := mul_nonneg (Nat.cast_nonneg m) (Real.log_nonneg (le_add_of_nonneg_right hA))
    have := mul_nonneg (Nat.cast_nonneg m)
      (Real.log_nonneg (le_add_of_nonneg_right (abs_nonneg α)))
    linarith
  obtain ⟨hsqB, hBX⟩ := sqrt_lt_floor ((by norm_num : (2 : ℝ) ≤ 4).trans
    (four_lt_rpow hδ0 hr0 h32').le)
  refine ⟨(Real.sqrt_nonneg _).trans_lt hsqB, hBX, ?_⟩
  have hprod : ∏ j, (r j + 1) ≤ (2 ^ r 0) ^ m := by
    simpa using Finset.prod_le_pow_card Finset.univ (fun j ↦ r j + 1) (2 ^ r 0)
      (fun j _ ↦ Nat.lt_two_pow_self.trans_le (Nat.pow_le_pow_right (by norm_num) (hr0max j)))
  have hprodR : (∏ j, ((r j : ℝ) + 1)) ≤ (2 : ℝ) ^ (m * r 0) := by
    exact_mod_cast (by simpa [← pow_mul, mul_comm] using hprod)
  exact hprodR.trans_lt (three_small_factors hδ0 hr0 hA h32).1

-- Compare logarithms of the denominator product, degree factors and coefficient scale.
private lemma roth_log_bound_aux {m : ℕ} [NeZero m] (hm2 : 2 ≤ m) {δ G κ B : ℝ} (hδ1 : δ ≤ 1)
    {q r : Fin m → ℕ} (hq1 : ∀ j, 1 < q j)
    (h53 : ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))) (hBpos : 0 < B)
    (hBX : B ≤ (q 0 : ℝ) ^ (δ * r 0)) (hN : (∏ j, ((r j : ℝ) + 1)) < B ^ δ)
    (hone : 1 < (∏ j, (q j : ℝ) ^ r j) * ((∏ j, ((r j : ℝ) + 1)) * B ^ (1 + 3 * δ) *
      (q 0 : ℝ) ^ (-(r 0 : ℝ) * G * κ))) : G * κ < m * (1 + 4 * δ) := by
  have hr0 : 0 < r 0 := Nat.pos_of_ne_zero fun h ↦ by simpa [h] using h53 0
  have hK0 := mul_pos (Nat.cast_pos.2 hr0) (Real.log_pos (Nat.one_lt_cast.2 (hq1 0)))
  have hδ0 : 0 ≤ δ := le_of_lt <|
    (div_pos_iff_of_pos_right (by norm_num : (0 : ℝ) < 10)).mp <|
    (lt_add_iff_pos_right 1).mp <| (mul_lt_mul_iff_left₀ hK0).mp <| by
      simpa only [one_mul] using h53 0
  have hqR : ∀ j, (0 : ℝ) < q j := fun j ↦ Nat.cast_pos.2 (lt_trans zero_lt_one (hq1 j))
  have hN0 : 0 < ∏ j, ((r j : ℝ) + 1) := Finset.prod_pos fun j _ ↦ Nat.cast_add_one_pos _
  -- take logarithms
  have hlog := Real.log_pos hone
  rw [Real.log_mul (Finset.prod_pos fun j _ ↦ pow_pos (hqR j) _).ne'
      ((mul_pos (mul_pos hN0 (Real.rpow_pos_of_pos hBpos _))
        (Real.rpow_pos_of_pos (hqR 0) _)).ne'),
    Real.log_mul (mul_pos hN0 (Real.rpow_pos_of_pos hBpos _)).ne'
      (Real.rpow_pos_of_pos (hqR 0) _).ne',
    Real.log_mul hN0.ne' (Real.rpow_pos_of_pos hBpos _).ne',
    Real.log_rpow hBpos, Real.log_rpow (hqR 0)] at hlog
  have hlogP : Real.log (∏ j, (q j : ℝ) ^ r j) <
      m * ((1 + δ / 10) * (r 0 * Real.log (q 0))) := by
    simp_rw [Real.log_prod (fun j _ ↦ (pow_pos (hqR j) _).ne'), Real.log_pow]
    simpa only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul] using
      Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty (fun j _ ↦ h53 j)
  have hpos : 0 < m * (1 + δ / 10) + (1 + 4 * δ) * δ - G * κ :=
    (mul_pos_iff_of_pos_left hK0).mp <| by
      linarith only [hlog, hlogP, (Real.log_lt_log hN0 hN).trans_eq (Real.log_rpow hBpos δ),
        mul_le_mul_of_nonneg_left (a := 1 + 4 * δ)
          ((Real.log_le_log hBpos hBX).trans_eq (Real.log_rpow (hqR 0) _)) (by positivity)]
  have hmR : (2 : ℝ) ≤ m := by exact_mod_cast hm2
  apply (sub_pos.mp hpos).trans_le
  linarith only [mul_le_mul_of_nonneg_right
    (by linarith only [hδ1, hmR] : 1 + 4 * δ ≤ (39 / 10) * m) hδ0]

/-- Roth's theorem for irrational real algebraic integers: if `approxSet α κ` is infinite,
then `κ ≤ 2`.

Source: §7 ("This contradicts (49) and finishes the proof of the theorem"). -/
theorem roth_of_isIntegral {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by
  by_contra! hκ
  obtain ⟨f, A, m, δ, hf, hfα, hA1, hA, hm2, hδ0, hδm, h30, h49⟩ :=
    exists_roth_parameters_aux hint hκ
  have : NeZero m := ⟨by lia⟩
  have hδ1 : δ ≤ 1 := hδm.le.trans (by
    simpa using one_div_le_one_div_of_le zero_lt_one
      (show (1 : ℝ) ≤ m by exact_mod_cast Nat.one_le_iff_ne_zero.2 (NeZero.ne m)))
  obtain ⟨h, q, r, happ, hcop, hq1, hr0, hrlast, h31b, hr0max, h32, h33, h53⟩ :=
    exists_roth_approximants_aux hα (by linarith) hinf m hδ0 hδ1 A
  obtain ⟨hBpos, hBX, hN⟩ :=
    roth_product_bound_aux hδ0.le (zero_le_one.trans hA1) (hr0 0) hr0max h32.le
  exact ((div_lt_iff₀' (sub_pos.2 ((eta_lt_gam_iff _ _ _).1 h30))).1 h49).not_gt
    (roth_log_bound_aux (κ := κ) hm2 hδ1 hq1 h53 hBpos hBX hN
      (one_lt_roth_eval_bound_aux hf hfα hA hδ0.le hδm.le hr0 hrlast h31b
        (fun j ↦ zero_lt_one.trans (hq1 j)) (by linarith) (fun j ↦ (happ j).2.le) hcop h32.le h33))

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
  refine roth hα halg ((hinf.image (f := fun x : ℚ ↦ (x.num, x.den))
    (fun _ _ _ _ hxy ↦ Rat.ext (congrArg Prod.fst hxy) (congrArg Prod.snd hxy))).mono ?_)
  rintro _ ⟨x, hx, rfl⟩
  exact ⟨x.den_pos, by rwa [← Rat.cast_def]⟩

end Roth
