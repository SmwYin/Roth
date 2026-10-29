from pathlib import Path
import re
D=Path(__file__).resolve().parent
body='''
#check_failure Roth.exists_nat_mul_isIntegral
namespace NatIntegral268Supplement
-- Existing canonical denominator law, stronger than mere existence.
theorem denominator_normal_form {A : Type*} [CommRing A] (x : A) (n : ℕ) :
    Algebra.natDenominator x ∣ n ↔ IsIntegral ℤ (n • x) :=
  Algebra.natDenominator_dvd_iff
-- A scalar denominator of a polynomial is not a proof its root is integral.
-- Removing algebraicity from integral-multiple existence is false already for Z[X].
theorem no_unconditional_nat :
    ¬ (∀ x : Polynomial ℤ, ∃ n : ℕ, 0 < n ∧ IsIntegral ℤ ((n : Polynomial ℤ) * x)) := by
  intro hall
  obtain ⟨n, hn, hi⟩ := hall Polynomial.X
  apply Polynomial.transcendental_X ℤ
  exact IsAlgebraic.of_smul_isIntegral (y := (n : ℤ))
    (by simpa only [isNilpotent_iff_eq_zero, Int.natCast_eq_zero] using hn.ne')
    (by simpa only [Algebra.smul_def, map_natCast] using hi)
end NatIntegral268Supplement
#print axioms NatIntegral268Supplement.denominator_normal_form
#print axioms NatIntegral268Supplement.no_unconditional_nat
'''
full=(D/'isolated-prefix19.lean.txt').read_text()+body;assert max(map(len,full.splitlines()))<=100
(D/'supplement-executed.lean.txt').write_text(full);print(full)
