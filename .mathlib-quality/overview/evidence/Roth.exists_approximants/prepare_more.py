from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_approximants')
def emit(n,s,op='run_code'):
 assert max(map(len,s.splitlines()))<=100
 p=D/(n+'-executed.lean.txt');p.write_text(s)
 r={'id':n+'01','operation':op,'source':p.name,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':n+'01-receipt.json','arguments':{}}
 if op=='diagnostics':r['arguments']={'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}
 (D/'root-requests'/(n+'01.json')).write_text(json.dumps(r,indent=2)+'\n')
g=(D/'generic-body.lean.txt').read_text()
s=(D/'isolated-prefix.lean.txt').read_text()+'\n#check_failure Roth.exists_approximants\n'+g+'''
#check @Set.seq_of_forall_finite_exists
#check @Nat.exists_strictMono_subsequence
#check @Filter.extraction_forall_of_frequently
#check @not_bddAbove_iff
#check @Real.lt_log_of_rpow_lt
namespace Approximants277Composition
example {A : Type*} (s : Set A) (height : A → ℝ)
    (hs : ∀ B : ℝ, ∃ a ∈ s, B < height a) (m : ℕ) [NeZero m] (c L : ℝ) :
    ∃ f : Fin m → A, (∀ j, f j ∈ s) ∧ (∀ j, 0 < height (f j)) ∧
      L < height (f 0) ∧ ∀ i j : Fin m, i.val + 1 = j.val →
        c * height (f i) < height (f j) := by
  fail_if_success solve | simp
  fail_if_success solve | exact?
  exact Approximants277Generic.finite_chain s height hs m c L
-- Explicitly verify the cofinality normal form rather than equating it to infinitude.
example {A : Type*} (s : Set A) (height : A → ℝ) :
    (∀ B : ℝ, ∃ a ∈ s, B < height a) ↔ ¬ BddAbove (height '' s) := by
  simp only [not_bddAbove_iff, Set.mem_image, exists_exists_and_eq_and]
end Approximants277Composition
'''
emit('composition',s)
# Fresh stable18 rational obstruction, using the prior proof only as a template.
t=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx/counterexample2-executed.lean.txt').read_text()
t=t[t.index('namespace Reduced274Counterexample'):].replace('Reduced274Counterexample','Approximants277Counterexample')
t=t.replace('end Approximants277Counterexample','''theorem no_chain : ¬ ∃ (h : Fin 1 → ℤ) (q : Fin 1 → ℕ),
    (∀ j, (h j, q j) ∈ S 0 3) ∧ (∀ j, IsCoprime (h j) (q j : ℤ)) ∧
      (∀ j, 1 < q j) ∧ (0 : ℝ) < Real.log (q 0) ∧
      ∀ i j : Fin 1, i.val + 1 = j.val →
        (2 / (1 : ℝ)) * Real.log (q i) < Real.log (q j) := by
  rintro ⟨h, q, hm, hc, hq, -⟩
  exact no_large_reduced ⟨(h 0, q 0), hm 0, hq 0, hc 0⟩
#print axioms Approximants277Counterexample.no_chain
end Approximants277Counterexample''')
emit('counterexample',(D/'isolated-prefix.lean.txt').read_text()+'\n'+t)
# Approved19: independent re-elaboration of prior274 own proofs, then full current signedκ chain.
a=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx/isolated2-executed.lean.txt').read_text()
a=a[a.index('namespace Reduced274'):].replace('Reduced274','Approximants277SignedSelector')
# Current isolated recovery body uses our freshly copied approxSet, not project constants.
r=(D/'recovery-body.lean.txt').read_text().replace('Approximants277Recovery','Approximants277Signed')
r=r.replace('open Roth','open Approximants277SignedSelector')
r=r.replace('from_selector (exists_reduced_approx hα hκ hinf) m L','from_selector (positive hα hκ hinf) m L')
r=r.replace('example : @Roth.exists_approximants = @recovered := Subsingleton.elim _ _\n','')
r=r.replace('end Approximants277Signed','''theorem unrestricted {α : ℝ} (hα : Irrational α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val →
        2 / δ * Real.log (q i) < Real.log (q j) :=
  from_selector (Approximants277SignedSelector.unrestricted hα hinf) m L
theorem subcritical {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : κ ≤ 2)
    (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val →
        2 / δ * Real.log (q i) < Real.log (q j) :=
  from_selector (Approximants277SignedSelector.subcritical hα hκ) m L
#print axioms Approximants277Signed.unrestricted
#print axioms Approximants277Signed.subcritical
end Approximants277Signed''')
s=(D/'isolated-prefix.lean.txt').read_text()+\
 'import Mathlib.NumberTheory.DiophantineApproximation.Basic\n'+\
 '\n#check_failure Roth.exists_approximants\n'+g+a+r
emit('signed',s)
print('composition01 counterexample01 stable18 and signed01 approved19 ready width<=100')
