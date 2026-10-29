from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_m');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
N='Roth.exists_m';target=src(N);assert target.replace('theorem exists_m','theorem replay',1)in(D/'original-executed.lean.txt').read_text()
caller=src('Roth.exists_roth_parameters_aux').replace('private lemma exists_roth_parameters_aux','theorem replay',1);header,body=caller.split(' := by\n',1);s=(D/'callers-executed.lean.txt').read_text();originalbody=target.split(' := by\n',1)[1];assert '\n'.join('  '+x for x in originalbody.splitlines())in s;assert header+' := by\n'in s;assert body.replace(':= exists_m (n :=',':= dimension_choice (n :=')in s
replacement=(D/'replacement-caller-executed.lean.txt').read_text();assert caller.replace(':= exists_m (n :=',':= Dimension275Signed.recovered (n :=')in replacement
signed=(D/'signed-executed.lean.txt').read_text();core=signed.split('namespace Dimension275Signed\n',1)[1].split('-- No n>0',1)[0];assert core.replace('  fail_if_success exact?\n','').strip()in replacement
assert all(x in meta for x in json.loads((D/'overview-entry.json').read_text())['project_dependencies'])if(D/'overview-entry.json').exists()else True
for label in ['original','callers','generic','signed','composition2','consumers2','replacement-caller','shape']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independently reconstructed exact target/full actual private caller original-proof and signed-generic replacements, original written caller signature,8clean native receipts. No native proof-identity equality claimed. Acceptance separate.')
