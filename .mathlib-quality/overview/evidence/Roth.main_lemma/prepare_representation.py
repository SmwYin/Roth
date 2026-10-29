from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'isolated-executed.lean.txt').read_text();defs=s[s.index('noncomputable def shift'):s.index('-- These positive')]
t=(R/'Roth/MainLemma.lean').read_text();concl=t[t.index(' : ∃ Q',t.index('theorem main_lemma'))+3:t.index(' := by',t.index('theorem main_lemma'))]
code=(D/'disk-prefix.lean.txt').read_text()+'''\nnamespace Main266Representation
open Roth MvPolynomial
'''+defs+'''
theorem shift_eq {σ : Type*} (x : σ → ℝ) (P : MvPolynomial σ ℝ) :
    shift x P = MvPolynomial.taylor x P := rfl
theorem idx_eq {m : ℕ} (P : MvPolynomial (Fin m) ℝ) (x : Fin m → ℝ)
    (r : Fin m → ℕ) : idx P x r = Roth.index P x r := rfl
theorem coeff_shift {σ : Type*} (x : σ → ℝ) (P : MvPolynomial σ ℝ) (i : σ →₀ ℕ) :
    (shift x P).coeff i = eval x (hasseDeriv i P) := MvPolynomial.coeff_taylor x i P
theorem goal_eq {m : ℕ} [NeZero m] (α δ : ℝ) (f : Polynomial ℤ)
    (r q : Fin m → ℕ) (h : Fin m → ℤ) : goal α δ f r q h ↔
    '''+concl+''' := by
  simp only [goal, idx_eq, coeff_shift, gam, lam, eta, mainCoeffBound]
#print axioms shift_eq
#print axioms idx_eq
#print axioms coeff_shift
#print axioms goal_eq
end Main266Representation
'''
assert max(map(len,code.splitlines()))<=100
(D/'representation-executed.lean.txt').write_text(code)
(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print(code)
