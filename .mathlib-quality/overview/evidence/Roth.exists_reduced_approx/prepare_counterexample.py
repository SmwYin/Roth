from pathlib import Path
import hashlib,json
D=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx')
s=(D/'isolated-prefix.lean.txt').read_text()+'''
#check_failure Roth.exists_reduced_approx
namespace Reduced274Counterexample
def S (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}
theorem infinite_zero_pairs : (S 0 3).Infinite := by
  refine (Set.infinite_range_of_injective (f := fun n : ℕ ↦ ((0 : ℤ), n + 1))
    (fun _ _ h ↦ Nat.add_right_cancel (congrArg Prod.snd h))).mono ?_
  rintro _ ⟨n, rfl⟩
  refine ⟨by omega, ?_⟩
  simp only [Int.cast_zero, zero_div, sub_zero, abs_zero]
  positivity

theorem no_large_reduced : ¬ ∃ hq ∈ S 0 3, 1 < hq.2 ∧
    IsCoprime hq.1 (hq.2 : ℤ) := by
  rintro ⟨⟨h,q⟩, ⟨hq, happ⟩, hq1, hcop⟩
  have hqR : (1 : ℝ) < q := by exact_mod_cast hq1
  have hzero : h = 0 := by
    by_contra hn
    have h1 : (1 : ℝ) ≤ |(h : ℝ)| := by
      exact_mod_cast Int.one_le_abs hn
    have hqpos : (0 : ℝ) < q := by positivity
    have hbound : |(h : ℝ)| < 1 / (q : ℝ) ^ (2 : ℕ) := by
      have ht : |(h : ℝ)| / q < 1 / (q : ℝ) ^ (3 : ℕ) := by
        simpa [abs_div, abs_of_pos hqpos, Real.rpow_ofNat] using happ
      rw [div_lt_iff₀ hqpos] at ht
      convert ht using 1 <;> field_simp <;> ring
    have : 1 / (q : ℝ) ^ (2 : ℕ) < 1 := by
      rw [div_lt_one (by positivity)]
      nlinarith
    linarith
  subst h
  have : q = 1 := by simpa [Int.isCoprime_iff_gcd_eq_one] using hcop
  omega
#print axioms Reduced274Counterexample.infinite_zero_pairs
#print axioms Reduced274Counterexample.no_large_reduced
end Reduced274Counterexample
'''
(D/'counterexample-executed.lean.txt').write_text(s)
x={'id':'counterexample01','operation':'run_code','source':'counterexample-executed.lean.txt','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'counterexample-receipt.json','arguments':{}}
(D/'root-requests/counterexample01.json').write_text(json.dumps(x,indent=2)+'\n')
assert max(map(len,s.splitlines()))<=100
