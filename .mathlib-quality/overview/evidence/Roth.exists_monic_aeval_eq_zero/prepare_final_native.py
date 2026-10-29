from pathlib import Path
import hashlib,json
D=Path(__file__).resolve().parent
exec((D/'prepare_requests.py').read_text().split("req('original01'")[0])
s=(D/'isolated2-executed.lean.txt').read_text().replace('  simpa [h] using hf','  simp [h] at hf')
(D/'isolated3-executed.lean.txt').write_text(s)
req('isolated03','run_code','isolated3-executed.lean.txt','isolated3-receipt.json')
s=(D/'caller-executed.lean.txt').read_text()+'''
elab "originalParameters272" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.Main `Roth.exists_roth_parameters_aux)
example : originalParameters272 = @Monic272Inline.exists_roth_parameters_aux := Subsingleton.elim _ _
namespace Monic272Inline
open LeanEval.NumberTheory.ThueSiegelRothProblem
'''
meta=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
t=next(x['source'] for x in meta if x['name']=='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth')
s+=t.replace('Roth.roth','Monic272Inline.roth')+'''
#print axioms thueSiegelRoth
end Monic272Inline
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Monic272Inline.thueSiegelRoth := Subsingleton.elim _ _
'''
(D/'caller2-executed.lean.txt').write_text(s)
req('caller02','diagnostics','caller2-executed.lean.txt','caller2-receipt.json',dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
print('prepared final native requests; caller02 maxwidth',max(map(len,s.splitlines())))
