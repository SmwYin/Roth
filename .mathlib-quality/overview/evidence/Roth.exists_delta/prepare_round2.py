from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
for stem in ['recovery','callers','composition']:
 src=D/(stem+'-executed.lean.txt');s=src.read_text()
 s=s.replace('  simp\nexample {κ', '  rintro ⟨δ, hδ, hlt⟩\n  norm_num at hlt\n  exact hδ.not_ge hlt.le\nexample {κ')
 s=s.replace('  fail_if_success simp\n  fail_if_success aesop','  fail_if_success solve | simp\n  fail_if_success solve | aesop')
 n=stem+'2-executed.lean.txt';(D/n).write_text(s);o=json.loads((D/'root-requests'/(stem+'01.json')).read_text());o.update(id=stem+'02',source=n,source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt=stem+'02-receipt.json');(D/'root-requests'/(stem+'02.json')).write_text(json.dumps(o,indent=2)+'\n');assert max(map(len,s.splitlines()))<=100
# Build consumer audit by retaining current canonical array exactly.
s=(D/'original-executed.lean.txt').read_text();tail=Path('/private/tmp/roth-overview/assess/Roth.exists_m/consumer-scope2-executed.lean.txt').read_text();tail=tail[tail.index('  let deps :='):tail.rindex('end Dimension275Audit')];tail=tail.replace('DIMENSION275','DELTA276')
s=s.replace('end Delta276Audit',tail+'end Delta276Audit');n='scope-executed.lean.txt';(D/n).write_text(s);o=json.loads((D/'root-requests/original01.json').read_text());o.update(id='scope01',source=n,source_sha256=hashlib.sha256(s.encode()).hexdigest(),receipt='scope01-receipt.json');(D/'root-requests/scope01.json').write_text(json.dumps(o,indent=2)+'\n');assert max(map(len,s.splitlines()))<=100
print('PASS prep round2 width/read; rejected sources/receipts unchanged')
