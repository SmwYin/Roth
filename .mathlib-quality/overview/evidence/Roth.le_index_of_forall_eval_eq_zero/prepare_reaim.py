from pathlib import Path
D=Path(__file__).parent
body='''
namespace Cutoff252Reaim
 theorem abstract_lower {I A L : Type*} [Semiring A] [SemilatticeInf L] [OrderTop L]
    (w : I → L) (P : AddMonoidAlgebra A I) (c : L) :
    c ≤ AddMonoidAlgebra.infDegree w P ↔ ∀ i ∈ P.coeff.support, c ≤ w i :=
  Finset.le_inf_iff
 theorem bounded_support_check {I A L : Type*} [Semiring A] [LinearOrder L] [OrderTop L]
    (w : I → L) (P : AddMonoidAlgebra A I) (T : Set I) (c : L)
    (hs : ∀ i ∈ P.coeff.support, i ∈ T)
    (hv : ∀ i ∈ T, w i < c → P.coeff i = 0) : c ≤ AddMonoidAlgebra.infDegree w P :=
  Finset.le_inf_iff.mpr fun i hi ↦
    le_of_not_gt fun hw ↦ (Finsupp.mem_support_iff.mp hi) (hv i (hs i hi) hw)
 theorem finset_bridge {I : Type*} (s : Finset I) (w : I → ℝ) :
    (s.inf (fun i ↦ (w i : WithTop ℝ))).untopD 0 = sInf (w '' (↑s : Set I)) := by
  classical
  rcases s.eq_empty_or_nonempty with h | h
  · subst s
    simp
  · change (s.inf (WithTop.some ∘ w)).untopD 0 = _
    rw [← Finset.coe_inf' h w, Finset.inf'_eq_csInf_image]
    rfl
 theorem projected_lower {I A : Type*} [Semiring A] (w : I → ℝ)
    (P : AddMonoidAlgebra A I) (hP : P.coeff.support.Nonempty) (c : ℝ) :
    c ≤ (AddMonoidAlgebra.infDegree (fun i ↦ (w i : WithTop ℝ)) P).untopD 0 ↔
      ∀ i, P.coeff i ≠ 0 → c ≤ w i := by
  change c ≤ (P.coeff.support.inf (WithTop.some ∘ w)).untopD 0 ↔ _
  rw [← Finset.coe_inf' hP w]
  simp only [WithTop.untopD_coe]
  simpa only [Finsupp.mem_support_iff] using
    (show c ≤ P.coeff.support.inf' hP w ↔ ∀ i ∈ P.coeff.support, c ≤ w i from
      Finset.le_inf'_iff hP w)
end Cutoff252Reaim
#print axioms Cutoff252Reaim.abstract_lower
#print axioms Cutoff252Reaim.bounded_support_check
#print axioms Cutoff252Reaim.finset_bridge
#print axioms Cutoff252Reaim.projected_lower
'''.replace('\n theorem','\ntheorem')
(D/'reaim-body.lean.txt').write_text(body)
s=(D/'isolated-prefix.lean.txt').read_text()+'''\n#check_failure Roth.le_index_of_forall_eval_eq_zero
#check_failure MvPolynomial.hasseDeriv
#check @AddMonoidAlgebra.infDegree
#check @Finset.le_inf_iff
#check @Finset.le_inf'_iff
'''+body
assert max(map(len,s.splitlines()))<=100
(D/'reaim-executed.lean.txt').write_text(s)
print('PASS reaim prepared; width',max(map(len,s.splitlines())));print(s)
