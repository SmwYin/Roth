from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.exists_approximants')
s=(D/'signed-executed.lean.txt').read_text()
base='''
namespace Approximants277Edges
open Approximants277SignedSelector
'''
meta=json.loads((D/'target-metadata.json').read_text())['source'];sig=meta.split(' := by',1)[0]
sig=sig.replace('theorem exists_approximants','theorem old_from_unrestricted').replace('(hκ : 0 < κ)','(_hκ : 0 < κ)')
base+=sig+' :=\n  Approximants277Signed.unrestricted hα hinf m L\n'
for label,delta in [('zero','0'),('negative','-1')]:
 sig2=sig.replace('old_from_unrestricted',label).replace(' (_hκ : 0 < κ)','').replace('{δ : ℝ}','').replace('2 / δ','2 / ('+delta+' : ℝ)')
 base+=sig2+' :=\n  Approximants277Signed.unrestricted (δ := '+delta+') hα hinf m L\n'
base+='''#print axioms Approximants277Edges.old_from_unrestricted
#print axioms Approximants277Edges.zero
#print axioms Approximants277Edges.negative
end Approximants277Edges
'''
s+=base
assert max(map(len,s.splitlines()))<=100
p=D/'edges-executed.lean.txt';p.write_text(s);r={'id':'edges01','operation':'run_code','source':p.name,'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'receipt':'edges01-receipt.json','arguments':{}};(D/'root-requests/edges01.json').write_text(json.dumps(r,indent=2)+'\n')
print('edges01 approved19: full old signature through unrestricted theorem; δ0,-1; width<=100')
