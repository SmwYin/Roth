from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
sig=(D/'target-excerpt.lean.txt').read_text().split(':= by',1)[0].replace('theorem exists_ne_modByMonic_eq','theorem noFinite').replace(' [Finite (Function.support r)]','')
finite=(D/'target-excerpt.lean.txt').read_text().split(':= by',1)[1].rstrip()
# Full finite-support branch is the original mathematical proof, not a call to the target.
s=(D/'disk-prefix.lean.txt').read_text()+'''namespace Collision249NoFinite
open Roth MvPolynomial
'''+sig+''' := by
  classical
  by_cases hfin : Finite (Function.support r)
  · let : Finite (Function.support r) := hfin
'''+''.join('  '+line+'\n'for line in finite.splitlines()if line.strip())+'''
  · have : Infinite (Function.support r) := not_finite_iff_infinite.mp hfin
    have hB : 0 < B := by
      by_contra hn
      have hzero : B = 0 := Nat.eq_zero_of_not_pos hn
      simp [hzero] at hcount
    have hX (j : Function.support r) : (X j.1 : MvPolynomial σ ℤ) ∈ boxFamily r B := by
      refine ⟨fun k ↦ ?_, fun d ↦ ?_⟩
      · by_cases hk : k = j.1
        · subst k
          simpa only [degreeOf_X_self] using Nat.pos_of_ne_zero j.2
        · simp only [degreeOf_X, hk, ite_false]
          exact Nat.zero_le _
      · rw [coeff_X]
        split_ifs <;> omega
    let F (j : Function.support r) (p : J × Fin f.natDegree) : Set.Icc (-(C : ℤ)) C :=
      ⟨(diag (hasseDeriv p.1.1 (X j.1)) %ₘ f).coeff p.2,
        abs_le.1 (hC _ (hX j) p.1.1 p.1.2 p.2.1 p.2.2)⟩
    obtain ⟨j, k, hne, he⟩ := Finite.exists_ne_map_eq_of_infinite F
    refine ⟨X j.1, hX j, X k.1, hX k, ?_, fun i hi ↦ ?_⟩
    · exact fun h ↦ hne (Subtype.ext (MvPolynomial.X_injective h))
    · simpa [F, Polynomial.sum_modByMonic_coeff hf Polynomial.degree_le_natDegree] using
        congrArg (fun g ↦ ∑ n : Fin f.natDegree, Polynomial.monomial (n : ℕ)
          (g (⟨i, hi⟩, n) : ℤ)) he
end Collision249NoFinite
#print axioms Collision249NoFinite.noFinite
'''
assert max(map(len,s.splitlines()))<=100
(D/'nofinite-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print(s)
