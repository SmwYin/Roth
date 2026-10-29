"""Scratch-only rendering of independently reviewed completed-declaration pairs."""
from pathlib import Path
import json,hashlib
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth')
p=B/'final-completed-combined-pairwise-preparation.json';d=json.loads(p.read_text())
I=json.loads((B/'final-completed-inventory-preparation.json').read_text());idx={x['declaration']:x for x in I['rows']}
assert d['completed_count']==I['completed_count']
report_hashes={n:hashlib.sha256(Path(x.get('report_source',str(R/x['report']))).read_bytes()).hexdigest()for n,x in idx.items()}
assert all(report_hashes[n]==x['report_sha256']for n,x in idx.items())
L=['# Completed-declaration pairwise comparison preview','',f"Scratch only: {d['pair_count']} individually reviewed pairs among {d['completed_count']} accepted declarations. Not the final293 analysis, and not evidence that unlisted pairs are inequivalent.",'','| Declaration A | Declaration B | Same statement? | Same proof / mathematical relationship? | Recommended action |','|---|---|---|---|---|']
def cell(s):return str(s).replace('|','\\|').replace('\n','<br>')
seen=set()
for x in d['rows']:
 assert x['a']in idx and x['b']in idx
 k=tuple(sorted([x['a'],x['b']]));assert k not in seen;seen.add(k)
 for v in x['evidence']:
  n=v['declaration'];assert v['report_sha256']==report_hashes[n]==idx[n]['report_sha256']
 L.append('| '+' | '.join(cell(v)for v in [f"`{x['a']}`",f"`{x['b']}`",'yes'if x['same_statement']is True else 'no'if x['same_statement']is False else x['same_statement'],x['same_proof'],x['action']])+' |')
assert len(seen)==d['pair_count']
(B/'FINAL_PAIRWISE_PREVIEW.md').write_text('\n'.join(L)+'\n')
print(f"PASS scratch pairwise table: {len(seen)} unique reviewed pairs, current accepted report hashes verified; no tracked changes.")
