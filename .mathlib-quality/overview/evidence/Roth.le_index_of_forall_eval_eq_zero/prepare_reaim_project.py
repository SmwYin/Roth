from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
s=(D/'disk-prefix.lean.txt').read_text()+(D/'reaim-body.lean.txt').read_text()+'''
namespace Cutoff252ReaimProject
open Roth MvPolynomial
 theorem index_inf_bridge {σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ)
    (α : σ → ℝ) (r : σ → ℕ) : index P α r =
      (AddMonoidAlgebra.infDegree (fun d ↦ (weight r d : WithTop ℝ)) (taylor α P)).untopD 0 :=
  (Cutoff252Reaim.finset_bridge (taylor α P).support (weight r)).symm
 theorem boxed_support {σ A : Type*} [CommSemiring A] {P : MvPolynomial σ A}
    {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → A) :
    ∀ d ∈ (taylor α P).coeff.support, ∀ j, d j ≤ r j := by
  intro d he j
  exact (monomial_le_degreeOf j he).trans ((degreeOf_taylor_le α j P).trans (hd j))
 theorem recovery {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0)
    {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) {c : ℝ}
    (hin : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) :
    c ≤ index P α r := by
  have hf : (taylor α P).coeff ≠ 0 := by
    intro h
    apply hP
    apply (taylor_eq_zero_iff α P).1
    apply AddMonoidAlgebra.coeff_injective
    simpa using h
  rw [index_inf_bridge]
  apply (Cutoff252Reaim.projected_lower (weight r) (taylor α P)
    (Finsupp.support_nonempty_iff.2 hf) c).2
  intro d he
  apply le_of_not_gt
  intro hw
  apply he
  rw [coeff_taylor]
  exact hin d (boxed_support hd α d (Finsupp.mem_support_iff.2 he)) hw
end Cutoff252ReaimProject
#print axioms Cutoff252ReaimProject.index_inf_bridge
#print axioms Cutoff252ReaimProject.boxed_support
#print axioms Cutoff252ReaimProject.recovery
run_cmd Lean.Elab.Command.liftTermElabM do
  let old ← Lean.getConstInfo `Roth.le_index_of_forall_eval_eq_zero
  let new ← Lean.getConstInfo `Cutoff252ReaimProject.recovery
  unless ← Lean.Meta.isDefEq old.type new.type do throwError "CUTOFF252_REAIM_TYPE_CHANGED"
  Lean.logInfo "CUTOFF252_REAIM_EXACT_RECOVERY"
'''.replace('\n theorem','\ntheorem')
assert max(map(len,s.splitlines()))<=100
(D/'reaim-project-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print('PASS reaim actual source; width',max(map(len,s.splitlines())));print(s)
