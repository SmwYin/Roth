from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_approximants');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
def norm(s):return re.sub(r'\s+',' ',s).strip()
N='Roth.exists_approximants';target=src(N);assert target.replace('theorem exists_approximants','theorem replay',1)in(D/'original-executed.lean.txt').read_text()
caller=src('Roth.exists_roth_approximants_aux');s=(D/'callers2-executed.lean.txt').read_text();assert caller.replace('private lemma exists_roth_approximants_aux','theorem generic_caller',1).replace(':= exists_approximants hα hκ hinf m',':= Approximants277Recovery.recovered hα hκ hinf m')in s
header=caller.split(' := by\n',1)[0].replace('private lemma exists_roth_approximants_aux','theorem inline_caller',1);assert header+' := by\n'in s
body=target.split(' := by\n',1)[1];assert norm(body)in norm(s)
remaining='  obtain ⟨r, hr0, h31a, h31b, h33, h53⟩ :='+caller.split('  obtain ⟨r, hr0, h31a, h31b, h33, h53⟩ :=',1)[1];assert s.count(remaining)==2
if(D/'overview-entry.json').exists():assert all(x in meta for x in json.loads((D/'overview-entry.json').read_text())['project_dependencies'])
for label in ['original','recovery01','callers02','generic01','composition02','counterexample02','scope01','signed01','edges02']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independently reconstructs exact original/full actual private caller generic substitution and full literal target body, otherwise identical caller tail/signature;9clean rawnative receipts. Final acceptance separate.')
