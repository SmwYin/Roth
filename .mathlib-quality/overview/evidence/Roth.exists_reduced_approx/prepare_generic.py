from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx');R=Path('/Users/ramin/LEAN/Roth');meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
s=(D/'isolated-prefix.lean.txt').read_text()+'''
#check_failure Roth.exists_reduced_approx
namespace Reduced274Generic
-- Canonicalization plus local finiteness and finite value fibers.
theorem unbounded_canonical {A B : Type*} (s : Set A) (f : A → B) (r : A → A)
    (height : A → ℕ) (good : A → Prop) (hs : s.Infinite)
    (hcut : ∀ Q : ℕ, {x ∈ s | height x ≤ Q}.Finite)
    (hfib : ∀ b ∈ f '' s, {x ∈ s | f x = b}.Finite)
    (hrmem : ∀ x ∈ s, r x ∈ s) (hrval : ∀ x ∈ s, f (r x) = f x)
    (hrgood : ∀ x ∈ s, good (r x)) (Q : ℕ) :
    ∃ x ∈ s, Q < height x ∧ good x := by
  by_contra! hc
  apply hs
  refine Set.Finite.of_finite_fibers f ?_ hfib
  refine ((hcut Q).image f).subset ?_
  rintro _ ⟨x, hx, rfl⟩
  refine ⟨r x, ⟨hrmem x hx, ?_⟩, hrval x hx⟩
  exact le_of_not_gt fun hh ↦ hc (r x) (hrmem x hx) hh (hrgood x hx)
'''
for nm in ['approxSet','approxSet_den_le_finite','eventually_div_rpow_lt','approxSet_num_den_mem_aux']:
 s+='\n'+next(x for x in meta if x['name']=='Roth.'+nm)['source'].replace('private theorem','theorem')+'\n'
s+='''
-- The complete original arithmetic statement follows from this own new generic theorem.
theorem recovered {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) :
    ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ) := by
  let ρ : ℤ × ℕ → ℚ := fun hq ↦ (hq.1 : ℚ) / hq.2
  let r : ℤ × ℕ → ℤ × ℕ := fun hq ↦ ((ρ hq).num, (ρ hq).den)
  refine unbounded_canonical (approxSet α κ) ρ r Prod.snd
    (fun hq ↦ IsCoprime hq.1 (hq.2 : ℤ)) hinf
    (approxSet_den_le_finite α κ) ?_ ?_ ?_ ?_ Q₀
  · intro x _
    obtain ⟨N, hN⟩ := eventually_div_rpow_lt (M := 1 / |α - (x : ℝ)|) hκ
    refine (approxSet_den_le_finite α κ N).subset ?_
    rintro ⟨h, q⟩ ⟨hm, hρx⟩
    refine ⟨hm, le_of_not_gt fun hq ↦ ?_⟩
    have hbound := hN q hq
    rw [Real.rpow_zero, div_one, div_right_comm,
      div_lt_iff₀ (abs_pos.2 (sub_ne_zero.2 (hα.ne_rat x))), one_mul] at hbound
    exact not_lt_of_gt hbound <| by simpa [← hρx, ρ] using hm.2
  · intro x hx
    exact approxSet_num_den_mem_aux hκ.le hx
  · intro x _
    exact Rat.num_div_den (ρ x)
  · intro x _
    exact Int.isCoprime_iff_gcd_eq_one.2 (ρ x).reduced
#print axioms Reduced274Generic.unbounded_canonical
#print axioms Reduced274Generic.recovered
end Reduced274Generic
'''
(D/'generic-executed.lean.txt').write_text(s)
x={'id':'generic01','operation':'run_code','source':'generic-executed.lean.txt','source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'generic-receipt.json','arguments':{}}
(D/'root-requests/generic01.json').write_text(json.dumps(x,indent=2)+'\n');assert max(map(len,s.splitlines()))<=100
