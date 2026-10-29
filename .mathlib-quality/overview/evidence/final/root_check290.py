from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine')
meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
N='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine';x=meta[N]
s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256']
assert s in(D/'original-executed.lean.txt').read_text()
norm=lambda s:re.sub(r'\s+',' ',s).strip()
ev=(R/'Roth/LeanEval.lean').read_text();ev=ev[ev.index('namespace LeanEval.NumberTheory.ThueSiegelRothProblem'):].replace('namespace LeanEval.NumberTheory.ThueSiegelRothProblem','namespace Diophantine290Callers',1).replace('end LeanEval.NumberTheory.ThueSiegelRothProblem','end Diophantine290Callers')
assert norm(ev)in norm((D/'callers-executed.lean.txt').read_text())
m=(D/'modern3-executed.lean.txt').read_text()
assert 'UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t'in m
assert 'UniformBound 2 x ↔'in m and 'lemma liouville_not_uniform'in m
for t in ['lemma cutoff_mono','lemma add_rat_iff','lemma mul_rat_iff','lemma rational_cutoff','lemma uniform_irrational','lemma finite_uniform']:assert t in m
shape=(D/'shape2-executed.lean.txt').read_text()
for t in ['lemma natural_den','lemma weak_bound','lemma signed_den','lemma rational_den']:assert t in shape
for label in ['original01','callers01','shape02','modern03']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics',[]));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in ['error','warning']or 'sorryAx'in x['message']or 'PANIC'in x['message']];print(label,q['elapsed_ms'],len(ds))
print('PASS root reconstructed original exact definition and entire namespace-only caller module; read full generic cutoff/irrational-conjunct equivalence, fixed2 recovery/affine consequences/falseguards and four original fixed2 statement-shape equivalences. Final report/assessment acceptance separate.')
