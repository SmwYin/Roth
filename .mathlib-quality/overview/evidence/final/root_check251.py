from pathlib import Path
import json,hashlib,re
D=Path('/private/tmp/roth-overview/assess/Roth.eval_hasseDeriv_sub_eq_zero');R=Path('/Users/ramin/LEAN/Roth')
m=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0];p=(D/'disk-prefix.lean.txt').read_text()
orig=(D/'original-executed.lean.txt').read_text();assert orig.startswith(p+'namespace Vanish251Original\nopen Roth\n'+m.replace('eval_hasseDeriv_sub_eq_zero','replay')+'\nend Vanish251Original\n')
a=m.index('/-- If `Δ_j');b=m.index('/-- Vanishing of box Hasse');body=m[m.index('theorem eval_hasseDeriv_sub_eq_zero'):b].rstrip().split(':= by\n',1)[1];mi=m[:a]+m[b:]
needle='    fun d hd hw ↦ eval_hasseDeriv_sub_eq_zero hfα (hWeq d (hJ d hd hw))';assert mi.count(needle)==1
replacement='    fun d hd hw ↦ by\n      have h := hWeq d (hJ d hd hw)\n'+'\n'.join('    '+x.replace(' j ',' d ')for x in body.splitlines());mi=mi.replace(needle,replacement)
assert (D/'inline-executed.lean.txt').read_text().startswith(p+'namespace Vanish251Inline\nopen Roth\n'+mi+'\nend Vanish251Inline\n')
v=json.loads((D/'verification.json').read_text())
for e in v['accepted']:
 r=json.loads((D/e['receipt']).read_text());z=r['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)
 print(e['label'],r['elapsed_ms'],'ms',len(ds),'messages',sum('depends on axioms'in x['message']for x in ds),'axiom prints')
print('PASS independent full original and sole-caller inline module reconstruction; six clean actual receipts inspected')
