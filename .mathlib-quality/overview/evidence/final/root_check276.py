from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_delta');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
def norm(s):return re.sub(r'\s+',' ',s).strip()
N='Roth.exists_delta';target=src(N);assert target.replace('theorem exists_delta','theorem replay',1)in(D/'original-executed.lean.txt').read_text()
caller=src('Roth.exists_roth_parameters_aux').replace('private lemma exists_roth_parameters_aux','theorem replay',1);header,body=caller.split(' := by\n',1);s=(D/'inline-executed.lean.txt').read_text();helper=target.replace('theorem exists_delta','have delta_choice',1);assert norm(helper)in norm(s);assert header+' := by\n'in s;assert body.replace(':= exists_delta hm',':= delta_choice hm')in s
s=(D/'callers2-executed.lean.txt').read_text()
for n,x in meta.items():
 if x['file']=='Roth/Main.lean'and x['line']>=410:
  expected=src(n).replace('private lemma','lemma',1)
  if n=='Roth.exists_roth_parameters_aux':expected=expected.replace(':= exists_delta hm',':= Delta276Recovery.recovered hm')
  assert expected in s,n
recovery=(D/'recovery2-executed.lean.txt').read_text();a=recovery.split('namespace Delta276Recovery\n',1)[1].split('example : @recovered',1)[0];assert a.strip()in s
if(D/'overview-entry.json').exists():assert all(x in meta for x in json.loads((D/'overview-entry.json').read_text())['project_dependencies'])
for label in ['original','inline01','generic01','recovery02','callers02','composition02','scope01','shape02','envelope-bridge01','envelopes01']:
 file=label+'-receipt.json';q=json.loads((D/file).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independently reconstructed exact original, complete actual privatecaller inline proof, exact full Main410-end continuation with generic recovery,10clean receipts including quantitative isolated envelope/fulloldbridge. Final acceptance separate.')
