from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
s=(D/'controls-executed.lean.txt').read_text()+'''
namespace Cutoff252Positive
open Roth MvPolynomial Cutoff252Project
 theorem positive_cutoff_weaker :
    (∀ d : Unit →₀ ℕ, weight (fun _ ↦ 1) d < 1 → (¬ ∀ j, d j ≤ 1) →
      ∃ j, degreeOf j ((X () : MvPolynomial Unit ℝ) ^ 2) < d j) ∧
    (∀ d : Unit →₀ ℕ, (∀ j, d j ≤ 1) → weight (fun _ ↦ 1) d < 1 →
      eval (fun _ ↦ (0 : ℝ)) (hasseDeriv d ((X () : MvPolynomial Unit ℝ) ^ 2)) = 0) ∧
    ¬ (∀ j : Unit, degreeOf j ((X () : MvPolynomial Unit ℝ) ^ 2) ≤ 1) ∧
    (1 : ℝ) ≤ index ((X () : MvPolynomial Unit ℝ) ^ 2) (fun _ ↦ 0) (fun _ ↦ 1) := by
  have low (d : Unit →₀ ℕ) (hw : weight (fun _ ↦ 1) d < 1) : d = 0 := by
    apply Finsupp.ext
    intro j
    have hR : (d () : ℝ) < 1 := by simpa [weight] using hw
    have hn : d () < 1 := by exact_mod_cast hR
    have hz : d () = 0 := by omega
    simpa using hz
  have hlocal : ∀ d : Unit →₀ ℕ, weight (fun _ ↦ 1) d < 1 → (¬ ∀ j, d j ≤ 1) →
      ∃ j, degreeOf j ((X () : MvPolynomial Unit ℝ) ^ 2) < d j := by
    intro d hw hb
    obtain rfl := low d hw
    simp at hb
  have hvan : ∀ d : Unit →₀ ℕ, (∀ j, d j ≤ 1) → weight (fun _ ↦ 1) d < 1 →
      eval (fun _ ↦ (0 : ℝ)) (hasseDeriv d ((X () : MvPolynomial Unit ℝ) ^ 2)) = 0 := by
    intro d _ hw
    obtain rfl := low d hw
    simp
  refine ⟨hlocal, hvan, ?_, ?_⟩
  · simp
  · exact cutoff_local_degree (pow_ne_zero _ (X_ne_zero ())) (fun _ ↦ 0) (fun _ ↦ 1) 1
      hlocal hvan
end Cutoff252Positive
#print axioms Cutoff252Positive.positive_cutoff_weaker
'''.replace('\n theorem','\ntheorem')
assert max(map(len,s.splitlines()))<=100
(D/'positive-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS positive source prepared; width',max(map(len,s.splitlines())));print(s[s.index('namespace Cutoff252Positive'):])
