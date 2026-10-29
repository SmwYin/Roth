from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.roth_rat')
meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
N='Roth.roth_rat';x=meta[N];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256']
assert s.replace('theorem roth_rat','theorem replay',1)in(D/'original-executed.lean.txt').read_text()
norm=lambda s:re.sub(r'\s+',' ',s).strip()
shape=(D/'shape2-executed.lean.txt').read_text();body=s.split(':= by\n',1)[1]
# The complete original numerator/denominator injection proof is separated as a generic map lemma.
mapping=body.replace('  refine roth hα halg','  refine',1)
assert norm(mapping)in norm(shape)
assert 'Roth.roth hα halg (rational_to_pairs hinf)'in shape
g=(D/'general2-executed.lean.txt').read_text()
assert 'Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational'in g
assert 'Real.rpow_le_rpow_of_exponent_le'in g
assert 'hR (inferred_irrational hκ.le hinf) halg hinf'in g
m=(D/'modern-executed.lean.txt').read_text();assert 'simp only [eventually_cofinite, not_le]'in m
assert '1 / (x.den : ℝ) ^ κ ≤ |α - x|'in m
for label in ['original','general02','shape02','modern01','edges01']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics',[]));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in ['error','warning']or 'sorryAx'in x['message']or 'PANIC'in x['message']];print(label,q['elapsed_ms'],len(ds))
b=json.loads((D/'file-end-build.json').read_text());assert b['command']==['lake','build']and b['exit_code']==0 and b['warning_count']==0
assert hashlib.sha256((D/b['log']).read_bytes()).hexdigest()==b['log_sha256']
print('PASS root exact original replay/generic rational-pair injection/original endpoint recovery, independently inspected denominator monotonicity/irrationality implication and cofinite complement, actual full file-end build. Final assessment acceptance separate.')
