"""Read-only, completed-only aggregate preparation; not a final overview acceptance."""
from pathlib import Path
import hashlib,json,re,sys
R=Path('/Users/ramin/LEAN/Roth'); B=Path('/private/tmp/roth-overview'); O=R/'.mathlib-quality/overview'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
p=read(O/'progress.json');order=read(O/'declaration-order.json');meta={x['name']:x for x in read(B/'review/corrected-manifest.json')}
pending_final=None
if '--accepted-final-candidate' in sys.argv:
 assert len(p['completed_declarations'])==292, 'Preintegration final inventory requires exactly292 published assessments'
 n=order[292]['name'];pending_final=B/'assess'/n
 a=read(pending_final/'assessment.json');rr=read(pending_final/'root-review.json')
 assert a['completed'] and not a['unresolved'] and rr['status']=='PASS'
 assert rr['declaration']==a['declaration']==p['next_declaration']==n
 assert rr['report_sha256']==sha(pending_final/'report.md')
 assert all(isinstance(v,str) and (v.startswith('PASS') or v.lower().startswith('n/a')) for v in a['phases'].values())
 p['completed_declarations'].append({'declaration':n,'verdict':a['verdict'],'report':'.mathlib-quality/overview/mathlibable/'+n+'.md','evidence':'.mathlib-quality/overview/evidence/'+n+'/'})
 p['next_declaration']=None
graph=read(B/'final-canonical-direct-dependencies.json');g={x['canonical_name']:x for x in graph['declarations']}
repairs={x['declaration']:x for x in read(B/'final-inventory-type-repair-plan.json')['kind_only_inventory_entries']}
resolutions=read(B/'final-project-dependency-reviewed-resolutions.json')['rows'];resolved={}
for row in resolutions:resolved.setdefault(row['declaration'],[]).append(row)
how_plan=B/'final-inventory-how-clarification-plan.json'
how_repairs={x['declaration']:x for x in read(how_plan)['rows']} if how_plan.exists() else {}
editorial_plan=B/'final-inventory-editorial-clarification-plan.json'
editorial_rows=read(editorial_plan)['rows'] if editorial_plan.exists() else []
base=read(O/'evidence/shared/input-manifest.json')['sources_and_pins']
assert len(base)==17
for path,info in base.items():assert sha(R/path)==info['sha256']
assert graph['provenance_sha256']==sha(B/graph['provenance'])
rows=[]
for i,c in enumerate(p['completed_declarations'],1):
 n=c['declaration'];assert n==order[i-1]['name'];m=meta[n]
 unpublished=pending_final is not None and i==293
 d=pending_final if unpublished else R/c['evidence'];report=d/'report.md' if unpublished else R/c['report']
 accept_path=d/('root-review.json' if unpublished else 'root-acceptance.json');accept=read(accept_path)
 assert accept['status']=='PASS' and sha(report)==accept['report_sha256']
 source='\n'.join((R/m['file']).read_text().splitlines()[m['line']-1:m['end_line']])
 assert hashlib.sha256(source.encode()).hexdigest()==m['sha256']
 e=read(d/'overview-entry.json') if (d/'overview-entry.json').exists() else {}
 if n in repairs:
  sig=repairs[n]['accepted_full_binder_signature'];assert sha(Path(sig['receipt']))==sig['receipt_sha256']
  typ=sig['type'];provenance={'method':'fresh fullbinder native batch','receipt':sig['receipt'],'receipt_sha256':sig['receipt_sha256'],'source':sig['source']}
 elif e:
  typ=e['type'];provenance={'method':'root-reviewed unpublished final candidate' if unpublished else 'accepted overview-entry','path':str(d/'overview-entry.json') if unpublished else str((d/'overview-entry.json').relative_to(R)),'sha256':sha(d/'overview-entry.json')}
 else:
  # Earliest two packages predate overview-entry schema; full native type is retained in report.
  assert n in ['MvPolynomial.hasseCoeff','MvPolynomial.hasseDeriv']
  typ=re.search(r'```lean\n(.*?)\n```',report.read_text(),re.S)[1]
  provenance={'method':'accepted native type displayed in report','path':c['report'],'sha256':sha(report)}
 assert typ and typ not in ['theorem','def','lemma','instance','noncomputable def']
 what=e.get('what',m['what']);how=e.get('how',m['how']);hyp=e.get('hypotheses',m['hypotheses'])
 assert what and how and hyp
 how_provenance={'method':'accepted inventory entry'}
 if n in how_repairs:
  hr=how_repairs[n];assert hr['original_how']==how and hr['source_sha256']==m['sha256'] and hr['accepted_report_sha256']==sha(report)
  assert all(name in source or name.split('.')[-1] in source for name in hr['named_source_ingredients'])
  how=hr['how'];how_provenance={'method':'root exact-source-reviewed final inventory clarification','plan':how_plan.name,'plan_sha256':sha(how_plan),'original_how':hr['original_how'],'named_source_ingredients':hr['named_source_ingredients']}
 editorial_provenance=[]
 for er in [x for x in editorial_rows if x['declaration']==n]:
  assert er['source_sha256']==m['sha256'] and er['accepted_report_sha256']==sha(report)
  assert er['field']=='what' and what==er['original']
  what=er['replacement'];editorial_provenance.append({'field':'what','original':er['original'],'plan':editorial_plan.name,'plan_sha256':sha(editorial_plan)})
 rows.append({'canonical_index':i,'declaration':n,'kind':m['kind'],'visibility':m['visibility'],
  'file':m['file'],'start_line':m['line'],'end_line':m['end_line'],'proof_lines':m['proof_lines'],
  'source_sha256':m['sha256'],'type':typ,'type_provenance':provenance,'what':what,'editorial_provenance':editorial_provenance,'how':how,'how_provenance':how_provenance,'hypotheses':hyp,
  'source_project_body_refs':m['project_body_refs'],'source_project_type_refs':m['project_type_refs'],
  'native_direct_body_dependencies':g[n]['body_dependencies'],'native_direct_type_dependencies':g[n]['type_dependencies'],
  'accepted_explanatory_dependencies':e.get('project_dependencies',m.get('uses_from_project', m['project_body_refs'] + m['project_type_refs'])),
  'historical_dependency_normalization':resolved.get(n,[]),
  'source_callers':m['project_callers'],'notes':m['notes'],'verdict':c['verdict'],
  'report':c['report'],'report_source':str(report),'evidence_source':str(d),'root_reviewed_unpublished_final_candidate':unpublished,
  'report_sha256':sha(report),'acceptance':c['evidence']+'root-acceptance.json','acceptance_source':str(accept_path),'acceptance_sha256':sha(accept_path)})
out={'scope':'COMPLETED-ONLY preparation. Not final overview; unfinished declarations and whole-project semantic-pairwise analysis remain. No tracked documents or historical accepted artifacts changed.',
 'completed_count':len(rows),'published_count':len(rows)-(1 if pending_final else 0),'has_unpublished_final_candidate':pending_final is not None,'total_declarations':293,'next_declaration':p['next_declaration'],
 'type_repairs_count':len([x for x in rows if x['declaration'] in repairs]),
 'how_clarifications_count':len([x for x in rows if x['declaration'] in how_repairs]),
 'dependency_scope':'Source references, native direct references, and explanatory/transitive metadata remain distinct. None claims full opaque/generated/simp/transitive closure.',
 'canonical_native_graph_provenance':{'file':'final-canonical-direct-dependencies.json','sha256':sha(B/'final-canonical-direct-dependencies.json')},'rows':rows}
if pending_final:
 out['scope']='PREINTEGRATION final-inventory preparation:292 published assessments plus the independently root-reviewed unpublished final candidate. Planned tracked paths are not claimed to exist for that candidate. Global synthesis/final acceptance is still separate. No tracked documents changed.'
(B/'final-completed-inventory-preparation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(rows),'completed-only inventory rows, all nonblank fields/full native types,14 fullbinder repairs, accepted report hashes, exact source excerpts, fresh17. No tracked edits.')
