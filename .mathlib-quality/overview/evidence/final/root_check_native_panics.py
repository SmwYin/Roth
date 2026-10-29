"""Read-only supplemental audit: no interpreter PANIC may be accepted as native evidence."""
from pathlib import Path
import json,hashlib,sys
R=Path('/Users/ramin/LEAN/Roth');B=Path('/private/tmp/roth-overview');O=R/'.mathlib-quality/overview'
read=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=read(O/'progress.json');count=len(p['completed_declarations']);roots=[O/'evidence']
if '--accepted-final-candidate'in sys.argv:
 assert count==292
 d=B/'assess'/p['next_declaration'];a=read(d/'assessment.json');r=read(d/'root-review.json')
 assert a['completed']and r['status']=='PASS'and r['report_sha256']==H(d/'report.md')
 roots.append(d);count+=1
scanned=0;findings=[]
for root in roots:
 for f in root.rglob('*.json'):
  if '_validation-layout'in f.parts:continue
  try:q=read(f)
  except (ValueError,UnicodeError):continue
  if not isinstance(q,dict):continue
  result=q.get('result');result=result if isinstance(result,dict)else q
  z=result.get('structuredContent',result)
  if not isinstance(z,dict):continue
  z=z.get('result',z)
  if not isinstance(z,dict):continue
  ds=z.get('items',z.get('diagnostics',[]))
  if not isinstance(ds,list)or not any(isinstance(x,dict)and 'message'in x for x in ds):continue
  scanned+=1
  n=sum('PANIC'in str(x.get('message',''))for x in ds if isinstance(x,dict))
  if not n:continue
  # All observed panics are preserved explicitly rejected attempts, not successful evidence.
  v=f.parent/'verification.json';assert v.is_file(),f
  rejected=read(v).get('rejected',[]);assert f.name in json.dumps(rejected),f
  findings.append(dict(receipt=str(f),receipt_sha256=H(f),diagnostic_count=n,tool_success=z.get('success'),verification=str(v),verification_sha256=H(v),disposition='explicitly rejected in declaration verification ledger'))
base=read(O/'evidence/shared/input-manifest.json')['sources_and_pins'];assert len(base)==17
for f,x in base.items():assert H(R/f)==x['sha256']
out=dict(status='PASS',completed_declaration_count=count,native_diagnostic_envelopes_scanned=scanned,panic_records=findings,accepted_panic_records=0,scope='Supplemental raw structured diagnostic audit; preserved rejected failures are not counted as accepted proofs. Does not replace per-declaration validators, kernel axioms or mathematical review.',command=['python3',str(Path(__file__).resolve()),*sys.argv[1:]],script_sha256=H(Path(__file__)))
(B/'final-native-panic-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',count,'completed scopes;',scanned,'diagnostic envelopes;',len(findings),'explicitly rejected PANIC records; zero accepted')
