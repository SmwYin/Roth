from pathlib import Path
import json,re
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');src=(D/'source-module.lean.txt').read_text();row=json.loads((D/'target-metadata.json').read_text());original=row['source'];prefix=(D/'disk-prefix.lean.txt').read_text()
body=src[src.index('namespace Roth'):].replace('namespace Roth','namespace Numeric219Broader\nopen Roth',1).replace('end Roth','end Numeric219Broader')
ind=(D/'isolated-body.lean.txt').read_text();generic=ind[ind.index('theorem envelope'):ind.index('theorem directProbe')]
wrapper=original.split(' := by',1)[0]+''' := by
  apply wider hp hδ0 hδ1
  exact hΦ.trans (mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_right (by norm_num : (3 : ℝ) ≤ 4) (by positivity)) (by positivity))'''
assert original in body;body=body.replace(original,generic+wrapper)
s=prefix+'\n/-! Verified coefficient4 weakening and original downstream statements. -/\n\nopen MvPolynomial\n\n'+body+'\n'+'\n'.join('#print axioms Numeric219Broader.'+m for m in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))+'\n';assert all(len(l)<=100 for l in s.splitlines());(D/'broader-executed.lean.txt').write_text(s)
body=src[src.index('namespace Roth'):].replace('namespace Roth','namespace Numeric219Inline\nopen Roth',1).replace('end Roth','end Numeric219Inline')
assert original in body;body=body.replace(original,'')
local='  '+original.replace('theorem lem7_numeric','have numeric',1).replace('\n','\n  ')
i=body.index('private lemma theta_phi_lt_aux');j=body.index('private lemma theta_lt_succ_aux',i);part=body[i:j];part=part.replace('  dsimp only',''+local+'\n  dsimp only',1).replace('apply lem7_numeric hp','apply numeric hp');body=body[:i]+part+body[j:]
a=body.index('/-- If `Φ ≤ 3');b=body.index('private lemma theta_scaled_unique_le_aux',a);body=body[:a]+body[b:]
s=prefix+'\n/-! Complete sole caller with the numerical proof local, then downstream replay. -/\n\nopen MvPolynomial\n\n'+body+'\n'+'\n'.join('#print axioms Numeric219Inline.'+m for m in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))+'\n';assert all(len(l)<=100 for l in s.splitlines());(D/'inline-executed.lean.txt').write_text(s)
(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text((D/'broader-executed.lean.txt').read_text());print('PASS variants prepared, allwidth100, nineimports fixed, wrote broader; no canonical arrays')
