from pathlib import Path
p=Path('/private/tmp/roth-overview/assess/Roth.index_unique')
s=Path('Roth/Index.lean').read_text()
b=s[s.index('theorem index_unique'):s.index('\nend Roth')]
b=b.replace('theorem index_unique','theorem independentNonzero',1)
out='namespace IndexUniqueAssessment151\nopen MvPolynomial Roth\nuniverse u\nvariable {σ : Type u} [Fintype σ]\n'+b+'\n'
out+='''theorem allPolynomials [Unique σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r =
      (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default := by
  by_cases hP : P = 0
  · subst P
    simp [index]
  · exact independentNonzero hP α r

theorem noAutomaticClosure [Unique σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r =
      (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default := by
  fail_if_success rfl
  fail_if_success simp only [index]
  exact allPolynomials P α r

theorem zeroDenominator [Unique σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) :
    index P α (fun _ ↦ 0) = 0 := by
  rw [allPolynomials]
  simp

#check @Roth.index_unique
#print Roth.index_unique
#print axioms Roth.index_unique
#print axioms independentNonzero
#print axioms allPolynomials
#print axioms noAutomaticClosure
#print axioms zeroDenominator
end IndexUniqueAssessment151
'''
(p/'target-probe-prep.lean.txt').write_text(out)
