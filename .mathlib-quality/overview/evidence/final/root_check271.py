from pathlib import Path
import json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.reduction');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
target=src('Roth.reduction');caller=src('Roth.roth');original=(D/'original-executed.lean.txt').read_text();assert target.replace('theorem reduction','theorem replay',1)in original
s=(D/'caller3-executed.lean.txt').read_text();a=s.split('namespace Reduction271Inline\n',1)[1].split('end Reduction271Inline',1)[0];b=s.split('namespace Reduction271Replacement\n',1)[1].split('end Reduction271Replacement',1)[0];assert target in a and caller in a and caller in b
g=target.replace('theorem reduction','theorem threshold',1).replace('{κ : ℝ} (hκ : 2 < κ)','{t κ : ℝ} (hκ : t < κ)').replace("∧ 2 < κ' ∧","∧ t < κ' ∧").replace('(κ + 2)','(κ + t)');assert g in b
for name in ['Reduction271Inline.roth','Reduction271Replacement.roth']:assert 'example : @Roth.roth = @'+name+' := Subsingleton.elim _ _'in s
assert 'example : @Roth.reduction = @Reduction271Replacement.reduction := Subsingleton.elim _ _'in s
iso=(D/'isolated-executed.lean.txt').read_text()
for n in ['Roth.approxSet','Roth.exists_nat_mul_isIntegral','Roth.approxSet_den_le_finite','Roth.eventually_div_rpow_lt']:assert src(n)in iso,n
for label in ['original','isolated','caller3','dependencies','scope2','consumer-scope']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independent original/fullcaller2routes/weakerthreshold exact reconstruction, prerequisite source copies, six clean root-native receipts. Final root acceptance separate.')
