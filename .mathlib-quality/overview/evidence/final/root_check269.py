from pathlib import Path
import json,re,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.approxSet_den_le_finite');prefix=(D/'disk-prefix.lean.txt').read_text();meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def source(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
N='Roth.approxSet_den_le_finite';target=source(N);replay='namespace Bounded269Original\nopen Roth\n'+target.replace('theorem approxSet_den_le_finite','theorem replay',1)+'\nend Bounded269Original\n';assert(D/'original-executed.lean.txt').read_text().startswith(prefix+replay)
proof=target.split(' := by\n',1)[1];iso=(D/'isolated-executed.lean.txt').read_text();generic=iso[iso.index('theorem bounded_den_finite'):iso.index('theorem finite_radius')];expected=prefix
names=['Roth.reduction','Roth.exists_reduced_approx','LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff']
for route in ['Literal','Generic']:
 ns='Bounded269'+route;expected+='\nnamespace '+ns+'\nopen Roth\n'
 if route=='Generic':expected+=generic+'\n'
 expected+=source('Roth.approxSet_num_den_mem_aux')+'\nopen Real\n'+source('LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux')+'\n'
 for n in names:
  s=source(n)
  if n.startswith('LeanEval.'):s=s.replace('IsDiophantine x','LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x')
  s=s.replace('IsDiophantine x ↔ ∀ {κ : ℝ},','IsDiophantine x ↔\n      ∀ {κ : ℝ},')
  bound='  have bound (α κ : ℝ) (Q₀ : ℕ) : {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite := by\n'
  bound+=('\n'.join('  '+l for l in proof.splitlines())+'\n')if route=='Literal'else'    exact bounded_den_finite α (fun q ↦ 1 / (q : ℝ) ^ κ) Q₀\n'
  s=s.replace(' := by\n',' := by\n'+bound,1).replace('Roth.approxSet_den_le_finite','bound').replace('approxSet_den_le_finite','bound')
  base=n.split('.')[-1];expected+=s+'\nexample : @'+n+' =\n    @'+base+' := Subsingleton.elim _ _\n#print axioms '+base+'\n'
 expected+='end '+ns+'\n'
actual=(D/'inline-executed.lean.txt').read_text();assert actual.startswith(expected)and actual.count('Subsingleton.elim _ _')==6;assert(D/'scope-executed.lean.txt').read_text().startswith(actual)
for label in ['original','isolated','inline','supplement','supplement2','scope']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']];assert not any('sorryAx'in x['message']for x in ds)
 print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root exact focused original and all6 fullcaller body/helper replacements reconstructed;6 raw clean receipts read. Root acceptance separate.')
