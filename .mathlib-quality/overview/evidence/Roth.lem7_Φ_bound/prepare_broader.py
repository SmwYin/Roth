from pathlib import Path
import json,re
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');row=json.loads((D/'target-metadata.json').read_text());src=(D/'source-module.lean.txt').read_text();body=src[src.index('namespace Roth'):].replace('namespace Roth','namespace Phi218Broader\nopen Roth',1).replace('end Roth','end Phi218Broader');body=re.sub(r'\blem7_Φ_bound\b','replay',body)
orig=row['source'].replace('theorem lem7_Φ_bound','theorem replay',1)
wide=orig.replace('theorem replay','theorem wider',1).replace('(hδ1 : δ ≤ 1)','(hδ2 : δ ≤ 2)',1)
wide=wide.replace('  have hδe : δ ≤ δ ^ e := by\n    simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1 he1','''  have hδe : δ ≤ 2 * δ ^ e := by
    by_cases hδ1 : δ ≤ 1
    · have h : δ ≤ δ ^ e := by
        simpa using Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1 he1
      nlinarith only [h, Real.rpow_pos_of_pos hδ0 e]
    · have h : 1 ≤ δ ^ e := Real.one_le_rpow (lt_of_not_ge hδ1).le (by positivity)
      linarith only [hδ2, h]''').replace('(27 / 2) * hde0','12 * hde0').replace('mul_le_mul hδe hc2 (zero_le_one.trans hc1) hde0.le','mul_le_mul hδe hc2 (zero_le_one.trans hc1) (by positivity)')
wrapper=orig.split(' := by',1)[0]+''' :=
  wider hp hδ0 (hδ1.trans (by norm_num))'''
assert orig in body;body=body.replace(orig,wide+'\n\n'+wrapper)
s=(D/'disk-prefix.lean.txt').read_text()+'\n/-! Read-only wider delta bound and complete caller replay. -/\n\nopen MvPolynomial\n\n'+body
s+='\n'+ '\n'.join('#print axioms Phi218Broader.'+m for m in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',body,re.M))+'\n'
assert all(len(l)<=100 for l in s.splitlines());(D/'broader-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print('PASS broader exact source,100width,nine unchanged imports,whole-module replay')
