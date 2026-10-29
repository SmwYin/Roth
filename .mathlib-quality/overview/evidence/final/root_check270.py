from pathlib import Path
import json,re,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.eventually_div_rpow_lt');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def source(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
N='Roth.eventually_div_rpow_lt';target=source(N);orig=(D/'original-executed.lean.txt').read_text();assert target.replace('theorem eventually_div_rpow_lt','theorem replay',1)in orig
proof=target.split(' := by\n',1)[1];iso=(D/'isolated3-executed.lean.txt').read_text();gen=iso[iso.index('theorem eventual_filter'):iso.index('theorem nonpositive')].strip();actual=(D/'inline2-executed.lean.txt').read_text();names=['Roth.reduction','Roth.exists_reduced_approx','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff']
for route in ['Literal','Generic']:
 ns='Decay270'+route;block=actual.split('namespace '+ns+'\n',1)[1].split('end '+ns+'\n',1)[0]
 for helper in ['Roth.approxSet_num_den_mem_aux','LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux']:assert source(helper)in block
 if route=='Generic':assert gen in block
 for n in names:
  s=source(n)
  if n.startswith('LeanEval.'):s=s.replace('IsDiophantine x','LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x').replace('IsDiophantine x ↔ ∀ {κ : ℝ},','IsDiophantine x ↔\n      ∀ {κ : ℝ},')
  bound="  have bound {M κ κ' : ℝ} (hκ : κ' < κ) :\n      ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by\n"
  bound+=('\n'.join('  '+l for l in proof.splitlines())+'\n')if route=='Literal'else'    exact recovery hκ\n'
  s=s.replace(' := by\n',' := by\n'+bound,1).replace('Roth.eventually_div_rpow_lt','bound').replace('eventually_div_rpow_lt','bound');assert s in block,(route,n)
  assert 'example : @'+n+' =\n    @'+n.split('.')[-1]+' := Subsingleton.elim _ _'in block
for label in ['original','isolated3','inline2','supplement3','scope3']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independently reconstructed focused original/full6callers/helpers/generic proofs; five clean root-native receipts. Final root acceptance separate.')
