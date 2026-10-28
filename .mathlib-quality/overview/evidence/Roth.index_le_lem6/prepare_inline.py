from pathlib import Path
import json
D=Path(__file__).resolve().parent;s=(D/'noq-executed.lean.txt').read_text();s=s[:s.index('\n#check @LemSix213NoQ.replay')]
row=json.load(open(D/'target-metadata.json'));caller=json.load(open(D/'callers.json'))[0]['source'];body=row['body'][3:];body=body.replace('  -- Retain the paper\'s positive-denominator setting.\n','')
caller=caller.replace('theorem Θ_option_le','theorem inlineCaller').replace('(hq : ∀ j, 0 < q j)','(_hq : ∀ j, 0 < q j)')
line='  obtain ⟨l, hl, hl\', hle⟩ := index_le_lem6 hδ0 hδ1 hrp hratio hr₁ hq hR hh'
replacement='  obtain ⟨l, hl, hl\', hle⟩ : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧\n      index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤\n        2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +\n          √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by\n'
replacement+='\n'.join('  '+l for l in body.splitlines())
assert line in caller;caller=caller.replace(line,replacement)
s+='\nnamespace LemSix213NoQ\nopen Roth MvPolynomial\nvariable {τ : Type*} [Fintype τ]\n'+caller+'\nend LemSix213NoQ\n#print axioms LemSix213NoQ.inlineCaller\n'
assert all(len(l)<=100 for l in s.splitlines());(D/'inline-executed.lean.txt').write_text(s);Path('.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s);print('inline prepared',len(s.splitlines()))
