from pathlib import Path
import json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_monic_aeval_eq_zero');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
N='Roth.exists_monic_aeval_eq_zero';original=(D/'original-executed.lean.txt').read_text();assert src(N).replace('theorem exists_monic_aeval_eq_zero','theorem replay',1)in original
s=(D/'caller2-executed.lean.txt').read_text();t=src('Roth.exists_roth_parameters_aux').replace('private lemma','theorem',1)
old='  obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint'
new='''  obtain ⟨p, hp, hp0⟩ := hint
  let f := p * Polynomial.X ^ 2
  have hf : f.Monic := hp.mul (Polynomial.monic_X_pow 2)
  have hfα : Polynomial.aeval α f = 0 := by
    rw [map_mul, Polynomial.aeval_def, hp0, zero_mul]
  have hdeg : 2 ≤ f.natDegree := by simp [f, hp.ne_zero]'''
assert t.count(old)==1 and t.replace(old,new)in s
for n in ['Roth.exists_roth_approximants_aux','Roth.one_lt_roth_eval_bound_aux','Roth.roth_product_bound_aux','Roth.roth_log_bound_aux']:
 assert src(n).replace('private lemma','theorem',1)in s,n
for n in ['Roth.roth_of_isIntegral','Roth.roth','Roth.roth_rat']:assert src(n)in s,n
final=src('LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth').replace('(Roth.roth _h_irr','(Monic272Inline.roth _h_irr');assert final in s
for label in ['original','isolated3','caller2','composition','consumer-scope']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS independent root original/directprivatecaller/fourhelpercopies/threeMain+LeanEvalfullbodies reconstructed;5clean root-native receipts inspected. Root acceptance separate.')
