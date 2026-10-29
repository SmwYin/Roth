from pathlib import Path
import json,hashlib,re
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');N='LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth';D=B/'assess'/N
order=json.loads((B/'review/corrected-manifest.json').read_text());x=next(x for x in order if x['name']==N)
target='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(target.encode()).hexdigest()==x['sha256']
assert target in (D/'original-executed.lean.txt').read_text()
assert x['line']==61 and x['end_line']==64 and not x['project_callers']
g=(D/'generality2-executed.lean.txt').read_text()
for s in ['IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ','theorem endpoint_rat','theorem endpoint_finite','theorem endpoint_weak','lemma rational_counterexample','theorem recovered']:
 assert s in g,s
m=(D/'project-modern-executed.lean.txt').read_text()
for s in ['lemma algebraic_family','lemma algebraic_not_liouville','lemma family_recovery','lemma liouville_counterexample','lemma no_irrational_free_uniform','Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ 2']:
 assert s in m,s
assert '(_h_alg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ))' in m
assert 'IsAlgebraic ℚ x' in m and '¬ LiouvilleWith p x' in m
assert '(h.irrational (by linarith))' in m
assert 'hx.irrational, hx.transcendental, liouville_not_uniform hx' in m
for label in ['original01','modern01','generality02','composition01','projectmodern01']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics',[]))
 assert z['success'] and not z.get('partial',False) and not z.get('timed_out',False)
 assert not [d for d in ds if d['severity'] in ['error','warning'] or 'PANIC' in d['message'] or 'sorryAx' in d['message']]
 if label=='projectmodern01':assert q['executor']['worker_request']['context']=='project_endpoint293' and q['executor']['preexecution_audit']['scope'].startswith('Explicit root-approved')
 print(label,q['elapsed_ms'],len(ds))
print('PASS root exact final theorem replay/fulltype/original-signature recovery, Q/Z equivalence, finite/weak bounds and rational necessity, generic isolated bridge plus explicitly PROJECT-CONTEXT actual Roth-to-Liouville endpoint and full uniform recovery. No existing mathlib Roth theorem inferred; report/global acceptance separate.')
