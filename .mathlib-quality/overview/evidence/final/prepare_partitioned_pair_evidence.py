"""Preserve all completed semantic comparisons in bounded module-pair artifacts.
Scratch preparation only; no Git/production changes. Final293 acceptance is separate.
"""
from pathlib import Path
import json,hashlib,itertools,collections,sys,shutil
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');OUT=B/'final-pairwise-partitions';OUT.mkdir(exist_ok=True);H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
I=json.loads((B/'final-completed-inventory-preparation.json').read_text());idx={x['declaration']:x for x in I['rows']};count=len(idx);assert count==I['completed_count']
if '--require-complete'in sys.argv:assert count==293
records=[];inputs=[]
for fn in['final-completed-cross-module-pairwise-preparation.json','final-completed-theta-pairwise-preparation.json']:
 p=B/fn;source_hash=H(p);d=json.loads(p.read_text());inputs.append({'historical_preparation_identifier':fn,'sha256':source_hash,'rows':len(d['rows']),'note':'Exact semantic rows preserved below; source JSON whitespace/monolithic layout is not a mathematical input.'})
 for row in d['rows']:records.append((row,fn,source_hash))
keys=[tuple(sorted((x['a'],x['b'])))for x,_,_ in records];expected={tuple(sorted(p))for p in itertools.combinations(idx,2)};assert len(keys)==len(set(keys))==len(expected)and set(keys)==expected
report_hashes={n:H(Path(x.get('report_source',str(R/x['report']))))for n,x in idx.items()};assert all(report_hashes[n]==x['report_sha256']for n,x in idx.items())
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())['sources_and_pins'];source_hashes={f:H(R/f)for f in{z['file']for z in idx.values()}};assert all(source_hashes[f]==base[f]['sha256']for f in source_hashes)
groups=collections.defaultdict(list);specs={}
for row,fn,srcsha in records:
 a,b=row['a'],row['b'];new=dict(row);new['historical_preparation']={'identifier':fn,'sha256':srcsha};evidence=[]
 for n in[a,b]:
  z=idx[n];evidence.append({'declaration':n,'canonical_index':z['canonical_index'],'file':z['file'],'start_line':z['start_line'],'end_line':z['end_line'],'source_excerpt_sha256':z['source_sha256'],'source_file_sha256':source_hashes[z['file']],'report':z['report'],'report_sha256':report_hashes[n]})
 new['evidence']=evidence
 if row.get('review_specification'):
  p=Path(row['review_specification']);assert p.is_file()and H(p)==row['review_specification_sha256'];specs[p.name]=p;new['review_specification']='specifications/'+p.name
 group=tuple(sorted((idx[a]['file'],idx[b]['file'])));groups[group].append(new)
for p in OUT.glob('*.json'):p.unlink()
(OUT/'specifications').mkdir(exist_ok=True)
for name,p in specs.items():shutil.copyfile(p,OUT/'specifications'/name)
artifacts=[]
for files,rows in sorted(groups.items()):
 name='--'.join(Path(f).stem for f in files)+'.json';rows.sort(key=lambda x:tuple(sorted((idx[x['a']]['canonical_index'],idx[x['b']]['canonical_index']))))
 d={'scope':'All semantic pairs in this module-pair block among accepted declarations1-'+str(count)+'. Remaining declarations excluded; final293 acceptance separate.','files':list(files),'accepted_declaration_count':count,'pair_count':len(rows),'rows':rows};p=OUT/name;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');assert p.stat().st_size<50_000_000
 artifacts.append({'path':name,'files':list(files),'pair_count':len(rows),'sha256':H(p),'bytes':p.stat().st_size})
manifest={'status':'PASS-completed-only','accepted_declaration_count':count,'total_project_declarations':293,'complete_project_pair_coverage':count==293,'pair_count':len(records),'expected_pairs':count*(count-1)//2,'all_pairs_unique_and_present':True,'historical_inputs':inputs,'inventory_sha256':H(B/'final-completed-inventory-preparation.json'),'artifacts':artifacts,'specifications':[{'path':'specifications/'+n,'sha256':H(OUT/'specifications'/n)}for n in sorted(specs)],'interpretation':'Pairwise mathematical comparisons are source/report-based judgments, not formal proofs of inequivalence. Related mechanisms and possible common APIs are recorded explicitly; detailed per-declaration proof/search evidence remains authoritative.'};(OUT/'index.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('PASS partitioned semantic evidence:',count,'accepted;',len(records),'unique pairs;',len(artifacts),'bounded module-pair files; largest',max(x['bytes']for x in artifacts),'bytes. Scratch only.')
