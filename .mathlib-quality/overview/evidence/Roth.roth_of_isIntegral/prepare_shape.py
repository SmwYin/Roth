from pathlib import Path
import hashlib,json
D=Path('/private/tmp/roth-overview/assess/Roth.roth_of_isIntegral');R=Path('/Users/ramin/LEAN/Roth')
def save(n,s):
 assert max(map(len,s.splitlines()))<=100,(n,max(map(len,s.splitlines())))
 assert all(x==x.rstrip()for x in s.splitlines()) and s.endswith('\n') and not s.endswith('\n\n')
 (D/n).write_text(s)
def req(id,src,receipt):
 (D/'root-requests'/f'{id}.json').write_text(json.dumps(dict(id=id,operation='diagnostics',source=src,source_sha256=hashlib.sha256((D/src).read_bytes()).hexdigest(),receipt=receipt,arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
prefix=(D/'disk-prefix.lean.txt').read_text()
shape=prefix+'''
namespace Integral287Shape
open Roth
lemma finite_iff_bound (α : ℝ) :
    (∀ {κ : ℝ}, (approxSet α κ).Infinite → κ ≤ 2) ↔
      ∀ κ : ℝ, 2 < κ → (approxSet α κ).Finite := by
  constructor
  · intro h κ hκ
    exact Set.not_infinite.mp fun hinf ↦ (h hinf).not_gt hκ
  · intro h κ hinf
    exact le_of_not_gt fun hκ ↦ hinf (h κ hκ)
lemma integral_finite {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α)
    {κ : ℝ} (hκ : 2 < κ) : (approxSet α κ).Finite :=
  (finite_iff_bound α).mp (Roth.roth_of_isIntegral hα hint) κ hκ
lemma recover_integral {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 :=
  (finite_iff_bound α).mpr (fun _ hκ ↦ integral_finite hα hint hκ) hinf
lemma zero_infinite (κ : ℝ) : (approxSet 0 κ).Infinite := by
  have hi : (Set.Ioi (0 : ℕ)).Infinite := Set.Ioi_infinite 0
  refine (hi.image (f := fun q : ℕ ↦ ((0 : ℤ), q)) (by
    intro a b hab
    exact congrArg Prod.snd hab)).mono ?_
  rintro _ ⟨q, hq, rfl⟩
  exact ⟨hq, by simp only [Int.cast_zero, zero_div, sub_self, abs_zero]; positivity⟩
example : ¬ (∀ {α : ℝ}, IsIntegral ℤ α → ∀ {κ : ℝ},
    (approxSet α κ).Infinite → κ ≤ 2) := by
  intro h
  have hh := h (isIntegral_zero : IsIntegral ℤ (0 : ℝ)) (zero_infinite 3)
  norm_num at hh
example {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by
  fail_if_success exact hint
  exact Roth.roth_of_isIntegral hα hint hinf
#print axioms Integral287Shape.finite_iff_bound
#print axioms Integral287Shape.integral_finite
#print axioms Integral287Shape.recover_integral
#print axioms Integral287Shape.zero_infinite
end Integral287Shape
'''
save('shape-executed.lean.txt',shape);req('shape01','shape-executed.lean.txt','shape01-receipt.json')
main=(R/'Roth/Main.lean').read_text();target=json.loads((D/'target-metadata.json').read_text())['source'];body=target.split(':= by\n',1)[1]
closure=main[main.index('-- Choose the polynomial, coefficient bound'):main.index('/-- Roth\'s theorem for irrational real algebraic integers')]
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text());roth=next(x['source']for x in meta if x['name']=='Roth.roth');rat=next(x['source']for x in meta if x['name']=='Roth.roth_rat')
inline='''  have integral_inline {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
      (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by
'''+''.join('    '+l+'\n' for l in body.rstrip().splitlines())
caller=roth.replace('theorem roth ','theorem roth_inline ').replace('  by_contra! hκ\n',inline+'  by_contra! hκ\n').replace('roth_of_isIntegral hα\' hint\' hinf\'','integral_inline hα\' hint\' hinf\'')
rat=rat.replace('theorem roth_rat','theorem roth_rat_replay').replace('refine roth hα','refine roth_inline hα')
s=prefix+'\nnamespace Integral287Callers\nopen Roth MvPolynomial\n'+closure+caller+'\n\n'+rat+'''
example : @Roth.roth = @roth_inline := Subsingleton.elim _ _
example : @Roth.roth_rat = @roth_rat_replay := Subsingleton.elim _ _
#print axioms Integral287Callers.roth_inline
#print axioms Integral287Callers.roth_rat_replay
end Integral287Callers
'''
lean=(R/'Roth/LeanEval.lean').read_text();lean=lean[lean.index('namespace LeanEval.'):].replace('LeanEval.NumberTheory.ThueSiegelRothProblem','Integral287LeanEval').replace('Roth.roth _h_irr','Integral287Callers.roth_inline _h_irr')
s+='\n'+lean+'''
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Integral287LeanEval.thueSiegelRoth := Subsingleton.elim _ _
#print axioms Integral287LeanEval.thueSiegelRoth
'''
# indenting the exact original proof makes its longest lines wider; wrap only lines at safe tokens.
s=s.replace('      (one_lt_roth_eval_bound_aux hf hfα hA hδ0.le hδm.le hr0 hrlast h31b', '      (one_lt_roth_eval_bound_aux hf hfα hA hδ0.le hδm.le hr0 hrlast h31b')
s=s.replace('(Integral287Callers.roth_inline _h_irr (_h_alg.extendScalars', '(Integral287Callers.roth_inline _h_irr\n      (_h_alg.extendScalars')
# Original proof copied with indentation preserved; split only trailing full application arguments.
lines=[]
for l in s.splitlines():
 if len(l)>100:
  candidates=[i for i in range(70,min(99,len(l)))if l[i]==' ']

  pos=candidates[-1];lines.extend([l[:pos], ' '* (len(l)-len(l.lstrip())+2)+l[pos+1:]])
 else:lines.append(l)
s='\n'.join(lines)+'\n';save('callers-executed.lean.txt',s);req('callers01','callers-executed.lean.txt','callers01-receipt.json')
print('Prepared shape01 and full caller inlining plus full downstream rat/LeanEval bodies')
