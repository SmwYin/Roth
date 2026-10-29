from pathlib import Path
import json, hashlib, re
B=Path('/private/tmp/roth-overview'); R=Path('/Users/ramin/LEAN/Roth')
N='LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff'; D=B/'assess'/N
order=json.loads((B/'review/corrected-manifest.json').read_text()); x=next(x for x in order if x['name']==N)
lines=(R/x['file']).read_text().splitlines(); target='\n'.join(lines[x['line']-1:x['end_line']])
assert hashlib.sha256(target.encode()).hexdigest()==x['sha256']
original=(D/'original-executed.lean.txt').read_text(); assert target in original
helper='\n'.join(lines[19:39]); assert helper in original
norm=lambda s: re.sub(r'\s+',' ',s).strip()
caller='\n'.join(lines[60:64]); inline=(D/'inline-executed.lean.txt').read_text()
body=target.split(':= by\n',1)[1]
assert norm(body) in norm(inline) and helper in inline
assert norm(caller.split(':=',1)[0]) in norm(inline)
assert 'D292_INLINE_TARGET_FREE' in inline
m=(D/'modern-executed.lean.txt').read_text(); rec=(D/'recovery-executed.lean.txt').read_text()
for token in ['lemma rational_pair_infinite','lemma pair_bound_irrational','lemma uniform_pair_iff_all_real','lemma pair_liouville_iff_all_real','lemma weak_uniform_iff','lemma rational_not_pair_bound','lemma liouville_not_uniform','lemma add_rat_iff','lemma mul_rat_iff']:
 assert token in m, token
assert 'Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t' in m
assert 'theorem all_real {x : ℝ}' in rec and 'D292_RECOVERY_CALLER_TARGET_FREE' in rec
assert norm(caller.split(':=',1)[0]) in norm(rec)
for label in ['original01','inline01','modern01','recovery01','candidates01']:
 q=json.loads((D/(label+'-receipt.json')).read_text()); z=q['result']['structuredContent']; z=z.get('result',z)
 ds=z.get('items',z.get('diagnostics',[])); assert z['success'] and not z.get('partial',False) and not z.get('timed_out',False)
 assert not [a for a in ds if a['severity'] in ['error','warning'] or 'PANIC' in a['message'] or 'sorryAx' in a['message']]
 print(label,q['elapsed_ms'],len(ds))
print('PASS independent exact original/helper/full caller body inlining; all-real generic pair equivalence and fixed2 project recovery, irrational Liouville conjunction, rational exact-multiple guard, strict/weak positive constant equivalence. Report/gates acceptance remains separate.')
