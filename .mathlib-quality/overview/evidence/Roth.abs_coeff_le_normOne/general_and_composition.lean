import Roth.CoeffNorm
import Mathlib.Analysis.Normed.Ring.Int

/-! Evidence for `Roth.abs_coeff_le_normOne`: the coefficient bound holds for the generalised
ℓ¹ norm `l1Norm` on `MvPolynomial σ R`, `[SeminormedCommRing R]` (parent `Roth.normOne`
verdict), with the project's one-call proof (`Finsupp.single_eval_le_sum`) surviving verbatim
modulo `|·|` ↦ `‖·‖`; plus the `[Norm R]`-only floor and recovery of the project statement. -/

open MvPolynomial

namespace Evidence80

variable {σ R : Type*}

section Seminormed
variable [SeminormedCommRing R]

noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖

/-- General form, verbatim project proof (one mathlib call). -/
theorem norm_coeff_le_l1Norm (p : MvPolynomial σ R) (d : σ →₀ ℕ) :
    ‖p.coeff d‖ ≤ l1Norm p :=
  Finsupp.single_eval_le_sum p.coeff (g := fun z ↦ ‖z‖) (by simp) (fun _ ↦ norm_nonneg _) d

/-- Alternative proof (parent evidence style) via `Finset.single_le_sum`. -/
theorem norm_coeff_le_l1Norm' (p : MvPolynomial σ R) (d : σ →₀ ℕ) :
    ‖p.coeff d‖ ≤ l1Norm p := by
  by_cases hd : d ∈ p.support
  · exact Finset.single_le_sum (f := fun d ↦ ‖p.coeff d‖) (fun _ _ ↦ norm_nonneg _) hd
  · simpa [notMem_support_iff.1 hd, l1Norm] using
      Finset.sum_nonneg fun d (_ : d ∈ p.support) ↦ norm_nonneg (p.coeff d)

/-- Bridge to the project def. -/
theorem l1Norm_int_eq_normOne (P : MvPolynomial σ ℤ) : l1Norm P = Roth.normOne P := by
  simp only [l1Norm, Roth.normOne, Int.norm_eq_abs]

/-- The exact project statement is recovered from the general one for `R = ℤ`. -/
example (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) : |((P.coeff d : ℤ) : ℝ)| ≤ Roth.normOne P := by
  simpa [Int.norm_eq_abs, l1Norm_int_eq_normOne] using norm_coeff_le_l1Norm P d

end Seminormed

/-- Floor: only `[Norm R]` (with `‖0‖ = 0`) is needed by the bound itself; recorded to show
the parent's `[SeminormedCommRing R]` (needed for triangle / submultiplicativity) is the
binding constraint, not this lemma. -/
theorem norm_coeff_le_l1Norm_norm [CommSemiring R] [Norm R] (h0 : ‖(0 : R)‖ = 0)
    (hn : ∀ r : R, 0 ≤ ‖r‖) (p : MvPolynomial σ R) (d : σ →₀ ℕ) :
    ‖p.coeff d‖ ≤ ∑ e ∈ p.support, ‖p.coeff e‖ :=
  Finsupp.single_eval_le_sum p.coeff (g := fun z ↦ ‖z‖) h0 hn d

end Evidence80
