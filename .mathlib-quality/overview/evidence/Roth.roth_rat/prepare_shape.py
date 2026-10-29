from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.roth_rat')
s=(D/'disk-prefix.lean.txt').read_text()+'''
namespace Roth289Shape
open Roth
-- Adapted finite/bound proof syntax from accepted287 shape2; rational domain is new here.
lemma finite_iff_bound (α : ℝ) :
    (∀ {κ : ℝ}, {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite → κ ≤ 2) ↔
      ∀ κ : ℝ, 2 < κ → {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Finite := by
  constructor
  · intro h κ hκ
    exact Set.not_infinite.mp fun hinf ↦ (h hinf).not_gt hκ
  · intro h κ hinf
    exact le_of_not_gt fun hκ ↦ hinf (h κ hκ)
lemma rational_finite {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α)
    {κ : ℝ} (hκ : 2 < κ) : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Finite :=
  (finite_iff_bound α).mp (Roth.roth_rat hα halg) κ hκ
lemma recover {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 :=
  (finite_iff_bound α).mpr (fun _ hκ ↦ rational_finite hα halg hκ) hinf
lemma rational_to_pairs {α κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) :
    (approxSet α κ).Infinite := by
  refine ((hinf.image (f := fun x : ℚ ↦ (x.num, x.den))
    (fun _ _ _ _ hxy ↦ Rat.ext (congrArg Prod.fst hxy) (congrArg Prod.snd hxy))).mono ?_)
  rintro _ ⟨x, hx, rfl⟩
  exact ⟨x.den_pos, by rwa [← Rat.cast_def]⟩
-- This re-elaboration is the endpoint construction, with no dependency on roth_rat.
lemma inline_endpoint {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 :=
  Roth.roth hα halg (rational_to_pairs hinf)
example : @Roth.roth_rat = @inline_endpoint := Subsingleton.elim _ _
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth289Shape.inline_endpoint
  unless !(ci.value! .getUsedConstants.contains `Roth.roth_rat) do
    throwError "ROTH289_INLINE_NOT_TARGET_FREE"
  Lean.logInfo "ROTH289_INLINE_TARGET_FREE"
#print axioms Roth289Shape.finite_iff_bound
#print axioms Roth289Shape.rational_finite
#print axioms Roth289Shape.recover
#print axioms Roth289Shape.rational_to_pairs
#print axioms Roth289Shape.inline_endpoint
end Roth289Shape
'''
s=s.replace('ci.value! .getUsedConstants','(ci.value!).getUsedConstants')
assert max(map(len,s.splitlines()))<=100
(D/'shape-executed.lean.txt').write_text(s)
r=dict(id='shape01',operation='diagnostics',source='shape-executed.lean.txt',source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='shape01-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
(D/'root-requests/shape01.json').write_text(json.dumps(r,indent=2)+'\n')
print('Prepared shape01 exit0 maxwidth',max(map(len,s.splitlines())))
