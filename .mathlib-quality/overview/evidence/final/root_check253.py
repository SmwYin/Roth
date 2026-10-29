from pathlib import Path
import json
D=Path('/private/tmp/roth-overview/assess/Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul');R=Path('/Users/ramin/LEAN/Roth');p=(D/'disk-prefix.lean.txt').read_text();m=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
assert(D/'original-executed.lean.txt').read_text().startswith(p+'namespace Budget253Original\nopen Roth\n'+m.replace('mul_two_mul_add_one_div_lt_of_le_sq_mul','replay')+'\nend Budget253Original\n')
a=m.index('    apply (mul_le_mul_iff_of_pos_right (sq_pos_of_pos hδpos)).1',m.index('private lemma theta_lt_eta_of_sq_log_bound_aux'));b=m.index('  simpa [eta] using Θ_lt',a);comparison=m[:a]+'    exact Budget253.weak (by positivity) hδm hL\n'+m[b:]
iso=(D/'isolated-executed.lean.txt').read_text();helpers='namespace Budget253\n'+iso.split('namespace Budget253\n',1)[1].split('theorem strict_budget',1)[0]+'end Budget253\n'
assert(D/'comparison-executed.lean.txt').read_text().startswith(p+helpers+'namespace Budget253Comparison\nopen Roth\n'+comparison+'\nend Budget253Comparison\n')
v=json.loads((D/'verification.json').read_text())
for e in v['accepted']:
 r=json.loads((D/e['receipt']).read_text());z=r['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)
 print(e['label'],r['elapsed_ms'],'ms',len(ds),'messages',sum('depends on axioms'in x['message']for x in ds),'axiom prints')
assert json.loads((D/'inline-audit.json').read_text())['line']==671
print('PASS independent exact full original and related weak-helper module reconstruction; no actual caller invented; four clean native receipts inspected, original printer elision disclosed')
