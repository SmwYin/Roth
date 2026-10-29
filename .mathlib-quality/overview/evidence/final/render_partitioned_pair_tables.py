"""Render readable pair tables beside complete JSON evidence; scratch only until final293."""
from pathlib import Path
import json,hashlib,sys
D=Path('/private/tmp/roth-overview/final-pairwise-partitions');p=D/'index.json';m=json.loads(p.read_text());n=m['accepted_declaration_count']
if '--require-complete'in sys.argv:assert n==293 and m['complete_project_pair_coverage']
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def cell(x):return str(x).replace('|','\\|').replace('\n','<br>')
records=[];index=['# Semantic pairwise comparisons','',f'{n}/293 accepted declaration assessments; {m["pair_count"]} unique comparisons. '+('Complete project pair coverage.'if n==293 else 'Completed prefix only; unfinished declarations excluded.'),'','These are source-and-report-based mathematical judgments, not formal proofs of inequivalence. Each table preserves the full comparison and recommended action; adjacent JSON retains source/report hashes and review provenance.','', '| Modules | Pairs | Comparison table | Supporting evidence |','|---|---:|---|---|']
for a in m['artifacts']:
 j=D/a['path'];assert H(j)==a['sha256'];d=json.loads(j.read_text());name=j.with_suffix('.md').name
 lines=['# '+' / '.join(a['files']),'',f'{len(d["rows"])} comparisons among the {n} accepted declarations. [Source hashes and review provenance]('+j.name+').','', '| Declaration A | Declaration B | Same statement? | Same proof / mathematical relationship? | Recommended action |','|---|---|---|---|---|']
 for row in d['rows']:
  same=row['same_statement'];same='yes'if same is True else'no'if same is False else same
  lines.append('| '+' | '.join(cell(x)for x in ['`'+row['a']+'`','`'+row['b']+'`',same,row['same_proof'],row.get('action',row.get('verdict'))])+' |')
 out=D/name;out.write_text('\n'.join(lines)+'\n');assert out.stat().st_size<50_000_000
 records.append(dict(path=name,json_source=j.name,json_source_sha256=H(j),pair_count=len(d['rows']),sha256=H(out),bytes=out.stat().st_size))
 index.append('| '+' / '.join(a['files'])+' | '+str(a['pair_count'])+' | [table]('+name+') | [JSON]('+j.name+') |')
(D/'README.md').write_text('\n'.join(index)+'\n');m['markdown_artifacts']=records;m['markdown_index']={'path':'README.md','sha256':H(D/'README.md'),'bytes':(D/'README.md').stat().st_size};p.write_text(json.dumps(m,indent=2,ensure_ascii=False)+'\n')
print('PASS scratch readable module-pair tables:',len(records),'tables;',sum(x['pair_count']for x in records),'comparisons; largest',max(x['bytes']for x in records),'bytes')
