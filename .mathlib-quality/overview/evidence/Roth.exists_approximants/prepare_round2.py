from pathlib import Path
import hashlib,json
D=Path('/private/tmp/roth-overview/assess/Roth.exists_approximants')
s=(D/'callers-executed.lean.txt').read_text()
q='''(show ∃ (h : Fin m → ℤ) (q : Fin m → ℕ),
      (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧
      (2 * m + 1 + 2 * m * Real.log (1 + A) +
        2 * m * Real.log (1 + |α|)) / δ ^ 2 < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val →
        2 / δ * Real.log (q i) < Real.log (q j) from by'''
s=s.replace('(by\n    let L :=',q+'\n    let L :=')
assert max(map(len,s.splitlines()))<=100
p=D/'callers2-executed.lean.txt';p.write_text(s)
r={'id':'callers02','operation':'diagnostics','source':p.name,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'callers02-receipt.json','arguments':{'file_path':'.lake/roth-overview-session/GenWronskianChecks.lean','timeout_s':45}}
(D/'root-requests/callers02.json').write_text(json.dumps(r,indent=2)+'\n')
print('callers02 prepared explicit full inline result type; width<=100')
