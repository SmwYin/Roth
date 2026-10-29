from pathlib import Path
import json,hashlib,re
D=Path('/private/tmp/roth-overview/assess/Roth.sub_mem_RSet');R=Path('/Users/ramin/LEAN/Roth')
s=(R/'Roth/MainLemma.lean').read_text();m=s.split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
prefix=(D/'disk-prefix.lean.txt').read_text()
orig=(D/'original-executed.lean.txt').read_text()
expected=prefix+'namespace Difference250Original\nopen Roth\n'+m.replace('sub_mem_RSet','replay')
assert orig.startswith(expected+'\nend Difference250Original\n')
a=m.index('/-- The difference of two distinct members'); b=m.index('/-- If `Δ_j'); t=m[m.index('theorem sub_mem_RSet'):b].rstrip()
body=t.split(':= by\n',1)[1].replace("(h'.", "(hW'.").replace("(h''.", "(hW''.")
inline=m[:a]+m[b:];needle="  have hP := sub_mem_RSet hW' hW'' hne";assert inline.count(needle)==1
inline=inline.replace(needle,"  have hP : W' - W'' ∈ RSet B r := by\n"+'\n'.join('  '+l for l in body.splitlines()))
assert (D/'inline-executed.lean.txt').read_text().startswith(prefix+'namespace Difference250Inline\nopen Roth\n'+inline+'\nend Difference250Inline\n')
v=json.loads((D/'verification.json').read_text())
for e in v['accepted']:
 r=json.loads((D/e['receipt']).read_text());z=r['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'))
 assert z['success'] and not z.get('partial',False)
 print(e['label'],r['elapsed_ms'],'ms',len(ds),'messages',len([d for d in ds if 'depends on axioms' in d['message']]),'axiom prints')
print('PASS independently reconstructed whole original and whole sole-caller inline modules')
