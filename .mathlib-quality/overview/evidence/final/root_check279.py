from pathlib import Path
import json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.one_le_prod_pow_mul_abs_eval');meta={x['name']:x for x in json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())}
def src(n):
 x=meta[n];s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert hashlib.sha256(s.encode()).hexdigest()==x['sha256'];return s
def norm(s):return re.sub(r'\s+',' ',s).strip()
N='Roth.one_le_prod_pow_mul_abs_eval';target=src(N);assert target.replace('theorem one_le_prod_pow_mul_abs_eval','theorem replay',1)in(D/'original-executed.lean.txt').read_text()
main=(R/'Roth/Main.lean').read_text();main=main[main.index('namespace Roth'):].replace('namespace Roth','namespace Integer279Full\nopen Roth',1).replace('end Roth','end Integer279Full')
assert main.count(target)==1;main=main.replace(target,'')
a=main.index('/-- If an integer polynomial `Q`');b=main.index('-/',a)+2;main=main[:a]+main[b:]
body=target.split(':= by',1)[1].strip('\n').replace('hQ j','hQd j').replace('hq j','hq0 j')
call='(one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne)';assert main.count(call)==1
typ='1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)|'
replacement='(show '+typ+' from by\n'+'\n'.join('  '+l for l in body.splitlines())+')'
expected=(D/'disk-prefix.lean.txt').read_text()+'\n'+main.replace(call,replacement)+'\n#print axioms Integer279Full.roth_rat\n'
assert norm(expected)==norm((D/'callers3-executed.lean.txt').read_text())
for label in ['original','generic01','signed01','recovery01','edges01','clearing03','composition03','callers03','shape02','generic-clearing01']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)and not z.get('timed_out',False);assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'];assert not any('sorryAx'in x['message']for x in ds);assert q['executor']['owner']=='root';print(label,q['elapsed_ms'],'ms',len(ds),'messages','elision',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds))
print('PASS root independently reconstructs exact original and full original Main namespace replay with target declaration and its orphan doc removed, sole full actual caller receives original proof inlining with local hQ/hq substitutions and line wrapping only. Ten actual clean native receipts; final acceptance separate.')
