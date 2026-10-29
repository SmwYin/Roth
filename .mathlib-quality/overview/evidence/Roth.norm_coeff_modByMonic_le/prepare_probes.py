from pathlib import Path
import re
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'source-MainLemma.lean.txt').read_text()
b=s[s.index('private lemma exists_norm_coeff_reduction_aux'):s.index('/-- Integer polynomials with coordinate')]
b=re.sub(r'/--.*?-/', '', b, flags=re.S)
b=b.replace('private lemma exists_norm_coeff_reduction_aux','private lemma reduction')
b=b.replace('exists_norm_coeff_reduction_aux','reduction').replace('theorem norm_coeff_modByMonic_le','theorem size_remainder')
b=b.replace('[SeminormedRing R]', '''[Ring R] (v : R → ℝ)
    (v0 : v 0 = 0) (vn : ∀ x, 0 ≤ v x)
    (vsub : ∀ x y, v (x - y) ≤ v x + v y)
    (vmul : ∀ x y, v (x * y) ≤ v x * v y)''')
b=re.sub('‖([^‖]+)‖',r'v (\1)',b)
b=b.replace('norm_nonneg','vn').replace('norm_sub_le','vsub').replace('norm_mul_le','vmul')
b=b.replace('simp [hQ0]','simp [hQ0]').replace('simpa using mul_nonneg','simpa [v0] using mul_nonneg')
b=b.replace('simpa [hf1]','simpa [hf1, v0]').replace('reduction hfA','reduction v v0 vn vsub vmul hfA')
pre=(D/'isolated-prefix.lean.txt').read_text()
code=pre+'''\n#check_failure Roth.norm_coeff_modByMonic_le
namespace Rem243Isolated
'''+b+'''
#print axioms size_remainder
#check @Polynomial.div_wf_lemma
#check @Polynomial.modByMonic_eq_of_not_monic
#check @Polynomial.modByMonic_eq_self_iff
#check @Polynomial.coeff_mul_X_pow'
-- A degree bound alone provides no coefficient norm bound.
theorem degree_not_size : ¬ (∀ p : Polynomial ℝ, p.natDegree ≤ 0 → ‖p.coeff 0‖ ≤ 1) := by
  intro h
  have hh := h (Polynomial.C 2) (by simp)
  norm_num at hh
-- Natural subtraction must saturate at zero.
theorem saturation (s n : ℕ) (h : s + 1 ≤ n) (A C : ℝ) :
    (1 + A) ^ (s + 1 - n) * C = C := by simp [Nat.sub_eq_zero_of_le h]
#print axioms degree_not_size
#print axioms saturation
end Rem243Isolated
'''
code=code.replace('(hs : P.natDegree ≤ s) (i : ℕ) : v', '(hs : P.natDegree ≤ s) (i : ℕ) :\n    v')
for line in code.splitlines():
 if len(line)>100: print(len(line),line)
assert max(map(len,code.splitlines()))<=100
(D/'isolated-executed.lean.txt').write_text(code)
print(code[len(pre):])
