from pathlib import Path
import json
D=Path(__file__).resolve().parent;s=(D/'broader-executed.lean.txt').read_text();s+='''
namespace Theta228Broad
theorem bridge {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) :
    Θ B q r = Roth.Θ B q r := rfl
'''
row=json.load(open(D/'target-metadata.json'));sig=row['signature'].replace('theorem Θ_lt','theorem positiveLast').replace('(hrlast : 3 ≤ (r (Fin.last n) : ℝ))','(hrlast : 0 < r (Fin.last n))');s+=sig+''' := by
  exact replay n hδ0 (by exact_mod_cast hrlast) hratio hq1 hqr
'''
s+='''
theorem oneVariable {δ : ℝ} (hδ0 : 0 < δ) {r q : Fin 1 → ℕ}
    (hr : 0 < r 0) (hq : 1 < q 0) :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ 1 * δ ^ ((1 / 2 : ℝ) ^ 1) := by
  by_cases hδ : δ ≤ 1
  · exact theta_lt_base_aux hδ0 hδ hr hq
  · exact theta_lt_of_large_delta_aux (by simpa using (not_le.mp hδ).le)
theorem deltaZeroGuard :
    ¬Θ ((1 : ℝ) ^ ((0 : ℝ) * 3)) (fun _ : Fin 1 ↦ 1) (fun _ ↦ 3) <
      10 ^ 1 * (0 : ℝ) ^ ((1 / 2 : ℝ) ^ 1) := by
  norm_num
  exact Θ_nonneg _
'''
sig=row['signature'].replace('theorem Θ_lt','theorem pointwise');sig=sig[:sig.index(' :\n    Θ')];sig=sig.replace('(hrlast : 3 ≤ (r (Fin.last n) : ℝ))','(hrlast : 0 < r (Fin.last n))');s+=sig+'''
    {P : MvPolynomial (Fin (n + 1)) ℤ} (hP : P ∈ RSet ((q 0 : ℝ) ^ (δ * r 0)) r)
    {h : Fin (n + 1) → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    Roth.index (MvPolynomial.map (Int.castRingHom ℝ) P) (fun j ↦ (h j : ℝ) / q j) r <
      10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1)) :=
  (index_le_Θ hP hh).trans_lt (positiveLast n hδ0 hrlast hratio hq1 hqr)
#print axioms bridge
#print axioms positiveLast
#print axioms oneVariable
#print axioms deltaZeroGuard
#print axioms pointwise
end Theta228Broad
'''
assert all(len(l)<=100 for l in s.splitlines());(D/'shapes-executed.lean.txt').write_text(s);Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print('prepared shape,pointwise,base-case andδzero guards',len(s.splitlines()))
