from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
abstract='''
namespace Cutoff252Abstract
 theorem support_lower_iff {I A L : Type*} [Zero A] [ConditionallyCompleteLinearOrder L]
    (f : I →₀ A) (hf : f ≠ 0) (w : I → L) (c : L) :
    c ≤ sInf (w '' (↑f.support : Set I)) ↔ ∀ i, w i < c → f i = 0 := by
  constructor
  · intro hc i hi
    by_contra hfi
    exact (not_le_of_gt hi) (hc.trans (csInf_le (f.support.finite_toSet.image w).bddBelow
      (Set.mem_image_of_mem w (Finsupp.mem_support_iff.2 hfi))))
  · intro h
    refine le_csInf ((Finsupp.support_nonempty_iff.2 hf).to_set.image w) ?_
    rintro _ ⟨i, hi, rfl⟩
    exact le_of_not_gt fun hwi ↦ (Finsupp.mem_support_iff.1 hi) (h i hwi)
 theorem support_lower_of_checks {I A L : Type*} [Zero A]
    [ConditionallyCompleteLinearOrder L] (f : I →₀ A) (hf : f ≠ 0) (w : I → L) (c : L)
    (T : Set I) (hout : ∀ i, w i < c → i ∉ T → f i = 0)
    (hin : ∀ i ∈ T, w i < c → f i = 0) : c ≤ sInf (w '' (↑f.support : Set I)) := by
  apply (support_lower_iff f hf w c).2
  intro i hi
  by_cases hT : i ∈ T
  · exact hin i hT hi
  · exact hout i hi hT
end Cutoff252Abstract
'''.replace('\n theorem','\ntheorem')
(D/'abstract-body.lean.txt').write_text(abstract)
isolated=(D/'isolated-prefix.lean.txt').read_text()+'''
#check_failure Roth.le_index_of_forall_eval_eq_zero
#check_failure MvPolynomial.hasseDeriv
#check_failure MvPolynomial.taylor
#check @le_of_not_gt
#check @le_csInf
#check @le_csInf_iff
#check @MvPowerSeries.nat_le_weightedOrder
#check @MvPowerSeries.le_weightedOrder
#check @MvPowerSeries.coeff_eq_zero_of_lt_weightedOrder
#check @Polynomial.hasseDeriv_eq_zero_of_lt_natDegree
'''+abstract+'''
namespace Cutoff252Existing
 theorem scalar_order {L : Type*} [LinearOrder L] {c w : L} (h : ¬ w < c) : c ≤ w := by
  exact?
 theorem powerSeries_criterion {σ A : Type*} [Semiring A] (w : σ → ℕ)
    (F : MvPowerSeries σ A) (n : ℕ) (h : ∀ d, Finsupp.weight w d < n →
      MvPowerSeries.coeff d F = 0) : (n : ℕ∞) ≤ F.weightedOrder w :=
  MvPowerSeries.nat_le_weightedOrder w h
 noncomputable def translated {σ A : Type*} [CommSemiring A] (α : σ → A)
    (P : MvPolynomial σ A) : MvPolynomial σ A :=
  MvPolynomial.eval₂Hom MvPolynomial.C (fun j ↦ MvPolynomial.X j + MvPolynomial.C (α j)) P
 theorem translated_weighted {σ A : Type*} [CommSemiring A] (α : σ → A)
    (P : MvPolynomial σ A) (w : σ → ℕ) (n : ℕ)
    (h : ∀ d, Finsupp.weight w d < n → (translated α P).coeff d = 0) :
    (n : ℕ∞) ≤ (translated α P : MvPowerSeries σ A).weightedOrder w :=
  MvPowerSeries.nat_le_weightedOrder w (by simpa only [MvPolynomial.coeff_coe] using h)
end Cutoff252Existing
#print axioms Cutoff252Abstract.support_lower_iff
#print axioms Cutoff252Abstract.support_lower_of_checks
#print axioms Cutoff252Existing.scalar_order
#print axioms Cutoff252Existing.powerSeries_criterion
#print axioms Cutoff252Existing.translated_weighted
'''.replace('\n theorem','\ntheorem').replace('\n noncomputable','\nnoncomputable')
assert max(map(len,isolated.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(isolated)
print('PASS isolated source prepared, stable18, width',max(map(len,isolated.splitlines())))
