from pathlib import Path
import hashlib,json
D=Path('/private/tmp/roth-overview/assess/Roth.roth');R=Path('/Users/ramin/LEAN/Roth')
def save(n,s):
 s='\n'.join(l.rstrip() for l in s.splitlines()).rstrip()+'\n'
 assert max(map(len,s.splitlines()))<=100,(n,max(map(len,s.splitlines())))
 (D/n).write_text(s)
def req(id,src):
 (D/'root-requests'/f'{id}.json').write_text(json.dumps(dict(id=id,operation='diagnostics',source=src,source_sha256=hashlib.sha256((D/src).read_bytes()).hexdigest(),receipt=id+'-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
prefix=(D/'disk-prefix.lean.txt').read_text()
s=prefix+'''
namespace Roth288Shape
open Roth
lemma finite_iff_bound (α : ℝ) :
    (∀ {κ : ℝ}, (approxSet α κ).Infinite → κ ≤ 2) ↔
      ∀ κ : ℝ, 2 < κ → (approxSet α κ).Finite := by
  constructor
  · intro h κ hκ
    exact Set.not_infinite.mp fun hinf ↦ (h hinf).not_gt hκ
  · intro h κ hinf
    exact le_of_not_gt fun hκ ↦ hinf (h κ hκ)
lemma algebraic_finite {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α)
    {κ : ℝ} (hκ : 2 < κ) : (approxSet α κ).Finite :=
  (finite_iff_bound α).mp (Roth.roth hα halg) κ hκ
lemma recover {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 :=
  (finite_iff_bound α).mpr (fun _ hκ ↦ algebraic_finite hα halg hκ) hinf
lemma zero_infinite (κ : ℝ) : (approxSet 0 κ).Infinite := by
  have hi : (Set.Ioi (0 : ℕ)).Infinite := Set.Ioi_infinite 0
  refine (hi.image (f := fun q : ℕ ↦ ((0 : ℤ), q)) (by
    intro a b hab
    exact congrArg Prod.snd hab)).mono ?_
  rintro _ ⟨q, hq, rfl⟩
  exact ⟨hq, by simp only [Int.cast_zero, zero_div, sub_self, abs_zero]; positivity⟩
example : ¬ (∀ {α : ℝ}, IsAlgebraic ℚ α → ∀ {κ : ℝ},
    (approxSet α κ).Infinite → κ ≤ 2) := by
  intro h
  have hh := h (isAlgebraic_zero : IsAlgebraic ℚ (0 : ℝ)) (zero_infinite 3)
  norm_num at hh
#print axioms Roth288Shape.finite_iff_bound
#print axioms Roth288Shape.algebraic_finite
#print axioms Roth288Shape.recover
#print axioms Roth288Shape.zero_infinite
end Roth288Shape
'''
save('shape-executed.lean.txt',s);req('shape01','shape-executed.lean.txt')
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());roth=next(x['source']for x in meta if x['name']=='Roth.roth');rat=next(x['source']for x in meta if x['name']=='Roth.roth_rat')
body=roth.split(':= by\n',1)[1]
inline='''  have roth_inline {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
      (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by
'''+''.join('    '+l+'\n'for l in body.rstrip().splitlines())
rat=rat.replace('theorem roth_rat','theorem rat_inline').replace('  refine roth hα',inline+'  refine roth_inline hα')
s=prefix+'\nnamespace Roth288Callers\nopen Roth\n'+rat+'''
example : @Roth.roth_rat = @rat_inline := Subsingleton.elim _ _
#print axioms Roth288Callers.rat_inline
end Roth288Callers
'''
lean=(R/'Roth/LeanEval.lean').read_text();lean=lean[lean.index('namespace LeanEval.'):].replace('LeanEval.NumberTheory.ThueSiegelRothProblem','Roth288LeanEval')
# Replace the entire target call with the exact original proof as an anonymous theorem term.
lean=lean.replace('(Roth.roth _h_irr (_h_alg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)))','''((by
      intro α hα halg κ hinf
      by_contra! hκ
      obtain ⟨α', κ', hα', hint', hκ', hinf'⟩ := Roth.reduction hα halg hκ hinf
      exact (Roth.roth_of_isIntegral hα' hint' hinf').not_gt hκ' :
      ∀ {α : ℝ}, Irrational α → IsAlgebraic ℚ α →
        ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite → κ ≤ 2)
      _h_irr (_h_alg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)))''')
s+='\n'+lean+'''
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Roth288LeanEval.thueSiegelRoth := Subsingleton.elim _ _
#print axioms Roth288LeanEval.thueSiegelRoth
'''
save('callers-executed.lean.txt',s);req('callers01','callers-executed.lean.txt')
print('Prepared shape01 and both full actual caller proof inlinings')
