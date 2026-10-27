from pathlib import Path
import hashlib, json, re
b = Path(__file__).resolve().parent
v = json.loads((b/'verification.json').read_text())['supplementary_reaim']
code = (b/v['source']).read_text()
assert hashlib.sha256(code.encode()).hexdigest() == v['source_sha256']
z = json.loads((b/v['receipt']).read_text())
assert z['request']['code'] == code
n = z['result']; assert not n.get('isError', False)
out = n.get('structuredContent', n)
assert out['success'] and not out.get('timed_out', False)
assert not re.search(r'^import Roth', code, re.M)
assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b', code)
ds = out.get('diagnostics', [])
assert not any(d['severity'] in ['error','warning'] for d in ds)
for d in ds:
    msg = d.get('message',''); assert 'sorryAx' not in msg
    if 'depends on axioms:' in msg:
        names = re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1)
        assert {s.strip() for s in names.split(',')} <= {'propext','Classical.choice','Quot.sound'}
assert any(v['theorem'] in d.get('message','') for d in ds)
a = json.loads((b/'assessment.json').read_text())
assert a['verdict'] == 'NO-mathlib-has-it' and a['reaim']['verified']
assert a['reaim']['existing_fact'] == v['existing_fact']
print('PASS: explicit parent re-aim, exact native bridge/preservation law, standard axioms')
