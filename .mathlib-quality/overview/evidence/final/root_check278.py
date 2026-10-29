from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_degrees');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
def norm(s):return re.sub(r'\s+',' ',s).strip()
N='Roth.exists_degrees';target=src(N);assert target.replace('theorem exists_degrees','theorem replay',1)in(D/'original-executed.lean.txt').read_text()
caller=src('Roth.exists_roth_approximants_aux');s=(D/'callers5-executed.lean.txt').read_text()
replaced=caller.replace('private lemma exists_roth_approximants_aux','theorem replaced',1).replace('exists_degrees hδ0 hδ1 hq1','Degrees278Recovery.all_positive_delta hδ0 hq1')
assert replaced in s
header=caller.split(' := by\n',1)[0].replace('private lemma exists_roth_approximants_aux','theorem inlined',1);assert header+' := by\n'in s
body=target.split(' := by\n',1)[1];assert norm(body)in norm(s)
remaining='  have hranti : Antitone r := by'+caller.split('  have hranti : Antitone r := by',1)[1];assert s.count(remaining)==2
assert 'Subsingleton.elim _ _'in s
for label in ['original','generic05','recovery05','callers05','composition06','edges01','candidate06']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independently reconstructs exact original, full actual caller using generalized all-positive delta, full literal target proof in otherwise identical caller; seven clean native receipts. Equality checks establish same proposition types by proof irrelevance, not identical proof terms. Final acceptance separate.')
