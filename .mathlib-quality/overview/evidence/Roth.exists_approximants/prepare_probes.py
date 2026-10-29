from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_approximants')
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
def emit(n,s,op='run_code'):
 assert max(map(len,s.splitlines()))<=100
 p=D/(n+'-executed.lean.txt');p.write_text(s)
 r={'id':n+'01','operation':op,'source':p.name,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':n+'01-receipt.json','arguments':{}}
 if op=='diagnostics':r['arguments']={'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}
 (D/'root-requests'/(n+'01.json')).write_text(json.dumps(r,indent=2)+'\n')
generic='''
namespace Approximants277Generic
-- An arbitrary step threshold, arbitrary objects, and a real height.
theorem sequence {A : Type*} (s : Set A) (height : A → ℝ)
    (hs : ∀ B : ℝ, ∃ a ∈ s, B < height a) (F : ℕ → ℝ → ℝ) (L : ℝ) :
    ∃ f : ℕ → A, (∀ k, f k ∈ s) ∧ (∀ k, 0 < height (f k)) ∧
      L < height (f 0) ∧ ∀ k, F k (height (f k)) < height (f (k + 1)) := by
  choose g hgmem hglt using fun B : ℝ ↦ hs (max B 0)
  let f : ℕ → A := Nat.rec (g L) (fun k a ↦ g (F k (height a)))
  have hf : ∀ k, f k ∈ s ∧ 0 < height (f k) := by
    rintro (_ | k) <;> exact ⟨hgmem _, (le_max_right _ _).trans_lt (hglt _)⟩
  exact ⟨f, fun k ↦ (hf k).1, fun k ↦ (hf k).2,
    (le_max_left _ _).trans_lt (hglt _), fun k ↦ (le_max_left _ _).trans_lt (hglt _)⟩
theorem finite_chain {A : Type*} (s : Set A) (height : A → ℝ)
    (hs : ∀ B : ℝ, ∃ a ∈ s, B < height a) (m : ℕ) [NeZero m]
    (c L : ℝ) : ∃ f : Fin m → A, (∀ j, f j ∈ s) ∧ (∀ j, 0 < height (f j)) ∧
      L < height (f 0) ∧ ∀ i j : Fin m, i.val + 1 = j.val →
        c * height (f i) < height (f j) := by
  obtain ⟨f, hm, hp, hL, hstep⟩ := sequence s height hs (fun _ t ↦ c * t) L
  refine ⟨fun j ↦ f j, fun j ↦ hm j, fun j ↦ hp j, hL, ?_⟩
  intro i j hij
  simpa only [← hij] using hstep i
-- Empty finite chains have no first element; expose the exact no-start form separately.
theorem finite_chain_empty {A : Type*} (s : Set A) (height : A → ℝ) (c : ℝ) :
    ∃ f : Fin 0 → A, (∀ j, f j ∈ s) ∧ ∀ i j : Fin 0,
      i.val + 1 = j.val → c * height (f i) < height (f j) := by
  exact ⟨Fin.elim0, fun j ↦ Fin.elim0 j, fun i ↦ Fin.elim0 i⟩
#print axioms Approximants277Generic.sequence
#print axioms Approximants277Generic.finite_chain
#print axioms Approximants277Generic.finite_chain_empty
end Approximants277Generic
'''
(D/'generic-body.lean.txt').write_text(generic)
emit('generic',(D/'isolated-prefix.lean.txt').read_text()+
 '\n#check_failure Roth.exists_approximants\n'+generic)
recovery='''
namespace Approximants277Recovery
open Roth
-- Cofinality in log height absorbs all representation-specific exp/ceiling operations.
theorem from_selector {α κ : ℝ}
    (hsel : ∀ Q : ℕ, ∃ hq ∈ approxSet α κ, Q < hq.2 ∧
      IsCoprime hq.1 (hq.2 : ℤ)) (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val →
        2 / δ * Real.log (q i) < Real.log (q j) := by
  let s : Set (ℤ × ℕ) := {hq | hq ∈ approxSet α κ ∧
    IsCoprime hq.1 (hq.2 : ℤ) ∧ 1 < hq.2}
  have hs : ∀ B : ℝ, ∃ a ∈ s, B < Real.log a.2 := by
    intro B
    obtain ⟨a, hm, hlt, hc⟩ := hsel (max ⌈Real.exp B⌉₊ 1)
    have he : Real.exp B < (a.2 : ℝ) :=
      (Nat.le_ceil _).trans_lt (by exact_mod_cast (le_max_left _ _).trans_lt hlt)
    exact ⟨a, ⟨hm, hc, (le_max_right _ _).trans_lt hlt⟩,
      (Real.lt_log_iff_exp_lt ((Real.exp_pos B).trans he)).2 he⟩
  obtain ⟨f, hm, -, hL, hstep⟩ := Approximants277Generic.finite_chain
    s (fun a ↦ Real.log a.2) hs m (2 / δ) L
  exact ⟨fun j ↦ (f j).1, fun j ↦ (f j).2, fun j ↦ (hm j).1,
    fun j ↦ (hm j).2.1, fun j ↦ (hm j).2.2, hL, hstep⟩
theorem recovered {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val →
        2 / δ * Real.log (q i) < Real.log (q j) :=
  from_selector (exists_reduced_approx hα hκ hinf) m L
example : @Roth.exists_approximants = @recovered := Subsingleton.elim _ _
#print axioms Approximants277Recovery.from_selector
#print axioms Approximants277Recovery.recovered
end Approximants277Recovery
'''
(D/'recovery-body.lean.txt').write_text(recovery)
emit('recovery',(D/'disk-prefix.lean.txt').read_text()+generic+recovery,'diagnostics')
# Full actual caller, first with original proof inlined, then generic recovery.
caller=next(x for x in meta if x['name']=='Roth.exists_roth_approximants_aux')['source']
(D/'caller-excerpt.lean.txt').write_text(caller+'\n')
target=next(x for x in meta if x['name']=='Roth.exists_approximants')['source']
body=target.split(' := by\n',1)[1]
call='exists_approximants hα hκ hinf m\n    ((2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|)) / δ ^ 2)'
inline='''(by
    let L := (2 * m + 1 + 2 * m * Real.log (1 + A) +
      2 * m * Real.log (1 + |α|)) / δ ^ 2
'''+''.join('  '+l+'\n' for l in body.splitlines())+'  )'
s=(D/'disk-prefix.lean.txt').read_text()+generic+recovery+'\nnamespace Approximants277Callers\nopen Roth\n'
s+=caller.replace('private lemma exists_roth_approximants_aux','theorem inline_caller').replace(call,inline)+'\n'
s+=caller.replace('private lemma exists_roth_approximants_aux','theorem generic_caller').replace('exists_approximants hα hκ hinf m','Approximants277Recovery.recovered hα hκ hinf m')+'\n'
s+='''#print axioms Approximants277Callers.inline_caller
#print axioms Approximants277Callers.generic_caller
end Approximants277Callers
'''
emit('callers',s,'diagnostics')
print('generic01 recovery01 callers01 prepared; all width<=100')
