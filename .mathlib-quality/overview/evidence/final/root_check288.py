from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.roth')
meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
def norm(s):return re.sub(r'\s+',' ',s).strip()
target=src('Roth.roth');original=(D/'original-executed.lean.txt').read_text();callers=(D/'callers-executed.lean.txt').read_text()
assert norm(target.replace('theorem roth','theorem replay',1))in norm(original)
inline='\n'.join('  '+x for x in target.replace('theorem roth','have roth_inline',1).splitlines())
rat=src('Roth.roth_rat').replace('theorem roth_rat','theorem rat_inline',1).replace(' := by\n',' := by\n'+inline+'\n',1).replace('refine roth hα','refine roth_inline hα',1)
assert norm(rat)in norm(callers)
ev=(R/'Roth/LeanEval.lean').read_text();ev=ev[ev.index('namespace LeanEval.NumberTheory.ThueSiegelRothProblem'):].replace('namespace LeanEval.NumberTheory.ThueSiegelRothProblem','namespace Roth288LeanEval',1).replace('end LeanEval.NumberTheory.ThueSiegelRothProblem','end Roth288LeanEval')
start=ev.index('theorem thueSiegelRoth');assert norm(ev[:start])in norm(callers)
endpoint=src('LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth');lhs=endpoint.split(':=',1)[0];assert norm(lhs)in norm(callers)
proof=target.split(':= by\n',1)[1].replace(':= reduction',':= Roth.reduction').replace('(roth_of_isIntegral','(Roth.roth_of_isIntegral')
assert norm(proof)in norm(callers)
for label in ['original','callers01','modern02','shape02','callers02']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics',[]));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in ['error','warning']or 'sorryAx'in x['message']];print(label,q['elapsed_ms'],len(ds))
print('PASS root reconstructed exact original target, full rational caller literal inline, entire pre-endpoint LeanEval module and endpoint original signature with actual Roth proof body inlined. Native/report acceptance separate.')
