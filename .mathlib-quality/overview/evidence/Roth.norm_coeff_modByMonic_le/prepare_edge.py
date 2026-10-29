from pathlib import Path
D=Path(__file__).resolve().parent
s=(D/'isolated-executed.lean.txt').read_text();s=s[:s.index('end Rem243Isolated')]+'''
-- The original statement is recovered without any sign or commutativity premise.
theorem original {R : Type*} [SeminormedRing R] {f : Polynomial R} {A : ℝ}
    (hfA : ∀ i, ‖f.coeff i‖ ≤ A) (P : Polynomial R) {C : ℝ}
    (hP : ∀ i, ‖P.coeff i‖ ≤ C) {s : ℕ} (hs : P.natDegree ≤ s) (i : ℕ) :
    ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C :=
  size_remainder norm norm_zero norm_nonneg norm_sub_le norm_mul_le hfA P hP hs i
-- Concrete bound parameters imply nonnegativity even at coefficient zero.
theorem signs {R : Type*} [SeminormedRing R] {f P : Polynomial R} {A C : ℝ}
    (hfA : ∀ i, ‖f.coeff i‖ ≤ A) (hP : ∀ i, ‖P.coeff i‖ ≤ C) : 0 ≤ A ∧ 0 ≤ C :=
  ⟨(norm_nonneg _).trans (hfA 0), (norm_nonneg _).trans (hP 0)⟩
theorem nonmonic {R : Type*} [SeminormedRing R] {f P : Polynomial R}
    (hf : ¬ f.Monic) {C : ℝ} (hP : ∀ i, ‖P.coeff i‖ ≤ C) (i : ℕ) :
    ‖(P %ₘ f).coeff i‖ ≤ C := by
  rw [Polynomial.modByMonic_eq_of_not_monic _ hf]
  exact hP i
theorem f_one {R : Type*} [SeminormedRing R] (P : Polynomial R) (i : ℕ) :
    ‖(P %ₘ 1).coeff i‖ = 0 := by simp
theorem p_zero {R : Type*} [SeminormedRing R] (f : Polynomial R) (i : ℕ) :
    ‖((0 : Polynomial R) %ₘ f).coeff i‖ = 0 := by simp
theorem f_zero {R : Type*} [SeminormedRing R] (P : Polynomial R) : P %ₘ 0 = P := by simp
-- Degree data / submodule membership do not bound archimedean size.
example {R : Type*} [SeminormedRing R] {f : Polynomial R} {A : ℝ}
    (hfA : ∀ i, ‖f.coeff i‖ ≤ A) (P : Polynomial R) {C : ℝ}
    (hP : ∀ i, ‖P.coeff i‖ ≤ C) {s : ℕ} (hs : P.natDegree ≤ s) (i : ℕ) :
    ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C := by
  fail_if_success exact Polynomial.natDegree_modByMonic_le P
  fail_if_success solve | simp only [Polynomial.modByMonic_eq_sub_mul_div]
  exact original hfA P hP hs i
-- Removing the final elimination from the exponent is false already for X modulo X-2.
theorem final_step_needed :
    ¬ ‖(((Polynomial.X : Polynomial ℝ) %ₘ
      (Polynomial.X - Polynomial.C 2)).coeff 0)‖ ≤ 1 := by
  norm_num [Polynomial.modByMonic_X_sub_C_eq_C_eval]
#print axioms original
#print axioms signs
#print axioms nonmonic
#print axioms f_one
#print axioms p_zero
#print axioms f_zero
#print axioms final_step_needed
end Rem243Isolated
'''
assert max(map(len,s.splitlines()))<=100
(D/'edge-executed.lean.txt').write_text(s)
print('Prepared edges plus original recovery and bounded composition failure probes')
