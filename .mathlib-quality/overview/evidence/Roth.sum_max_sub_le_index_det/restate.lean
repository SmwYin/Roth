import Roth.Theta

/-! Evidence for `Roth.sum_max_sub_le_index_det`.
(1) Restatement: the two hypotheses `hD` (degree of `D μ` at most `μ`) and `hδ` (weight bound
    for every `d` of degree `≤ l - 1`) are only used through their consequence
    `∀ μ, weight (r ∘ some) (D μ) ≤ δ`. The restated lemma with that single hypothesis compiles
    with the same proof, and the original is a one-line corollary. -/

namespace Roth
open MvPolynomial

variable {τ : Type*} [Fintype τ]

theorem sum_max_sub_le_index_det' {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (hdet : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0) (α : Option τ → ℝ)
    {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ}
    (hw : ∀ μ, weight (r ∘ some) (D μ) ≤ δ) :
    ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤
      index (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by
  classical
  set E : Fin l → Fin l → MvPolynomial (Option τ) ℝ := fun μ ν ↦
    hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R
  have hterm : ∀ μ ν : Fin l, E μ ν ≠ 0 →
      max 0 (index R α r - ν / r none) - δ ≤ index (E μ ν) α r := by
    intro μ ν hE
    have h1 := index_sub_weight_le_index_hasseDeriv hE α r
    rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1
    have h2 := hw μ
    rw [← sub_sub, sub_right_comm] at h1
    rw [sub_le_iff_le_add]
    exact max_le (add_nonneg (index_nonneg _ _ _) ((weight_nonneg _ _).trans h2))
      ((sub_le_iff_le_add).1 ((sub_le_sub_left h2 _).trans h1))
  rw [Matrix.det_apply'] at hdet ⊢
  refine le_index_sum hdet fun s _ hs ↦ ?_
  have hprod : ∏ i, Matrix.of E (s i) i ≠ 0 := (mul_ne_zero_iff.mp hs).2
  have hentry (i : Fin l) : Matrix.of E (s i) i ≠ 0 :=
    (Finset.prod_ne_zero_iff.1 hprod) i (Finset.mem_univ _)
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

variable [DecidableEq τ]

/-- The original statement follows in one line from the restated one. -/
example {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (hD : ∀ μ, (D μ).degree ≤ μ) (hdet : (Matrix.of fun μ ν : Fin l ↦
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0) (α : Option τ → ℝ)
    {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ}
    (hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ) :
    ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤
      index (Matrix.of fun μ ν : Fin l ↦
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r :=
  sum_max_sub_le_index_det' D hdet α hr fun μ ↦ hδ _ ((hD μ).trans (Nat.le_sub_one_of_lt μ.isLt))

end Roth
