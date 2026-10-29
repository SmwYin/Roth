from pathlib import Path
import json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.exists_reduced_approx');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
N='Roth.exists_reduced_approx';assert all(x in meta for x in json.loads((D/'overview-entry.json').read_text())['project_dependencies']);target=src(N);helper=src('Roth.approxSet_num_den_mem_aux').replace('private theorem','theorem',1);s=(D/'original-executed.lean.txt').read_text();assert target.replace('theorem exists_reduced_approx','theorem replay',1)in s;assert helper in s
caller=src('Roth.exists_approximants').replace('theorem exists_approximants','theorem replay',1);old='  choose g hgmem hglt hgcop using fun Q₀ : ℕ ↦ exists_reduced_approx hα hκ hinf Q₀';assert caller.count(old)==1
body=target.split(' := by\n',1)[1];replacement='  have reduced : ∀ Q₀ : ℕ, ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧\n      IsCoprime hq.1 (hq.2 : ℤ) := by\n    intro Q₀\n'+'\n'.join('  '+x for x in body.splitlines())+'\n  choose g hgmem hglt hgcop using reduced'
full=(D/'callers-executed.lean.txt').read_text();assert caller.replace(old,replacement)in full;assert helper in full;assert 'example : @Roth.exists_approximants = @Reduced274Caller.replay := Subsingleton.elim _ _'in full
for label in ['original','callers','consumers2','isolated2','generic','composition','counterexample2']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS independent root exact original/privatehelper/full actual caller proof replacement and exact signature reconstructed;7 clean native receipts inspected. Root acceptance separate.')
