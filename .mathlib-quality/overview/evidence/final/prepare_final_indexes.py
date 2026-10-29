"""Refresh scratch-only final aggregation indexes from accepted completed declarations."""
from pathlib import Path
import json, hashlib, sys
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth')
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,data):(B/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
I=read(B/'final-completed-inventory-preparation.json');rows=I['rows'];idx={x['declaration']:x for x in rows}
P=read(R/'.mathlib-quality/overview/progress.json')
if I.get('has_unpublished_final_candidate',False):
 assert '--accepted-final-candidate' in sys.argv
 assert len(rows)==I['completed_count']==293 and I['published_count']==len(P['completed_declarations'])==292
 assert rows[-1]['root_reviewed_unpublished_final_candidate'] and rows[-1]['declaration']==P['next_declaration']
 assert [x['declaration']for x in rows[:-1]]==[x['declaration']for x in P['completed_declarations']]
else:
 assert len(rows)==I['completed_count']==len(P['completed_declarations'])
 assert [x['declaration']for x in rows]==[x['declaration']for x in P['completed_declarations']]
if '--require-complete' in sys.argv:assert len(rows)==293
for x in rows:assert sha(Path(x.get('report_source',str(R/x['report']))))==x['report_sha256']
pairs=[]
for name in ['final-completed-theta-pairwise-preparation.json','final-completed-cross-module-pairwise-preparation.json']:
 path=B/name;d=read(path);preparation_hash=sha(path)
 for x in d['rows']:
  assert x['a']in idx and x['b']in idx
  evidence=[]
  for n in [x['a'],x['b']]:
   y=idx[n];evidence.append({k:y[k]for k in ['declaration','canonical_index','file','start_line','end_line','source_sha256','report','report_sha256']})
  pairs.append({'a':x['a'],'b':x['b'],'same_statement':x['same_statement'],'same_proof':x['same_proof'],'action':x.get('action',x.get('verdict')),'preparation_source':name,'preparation_sha256':preparation_hash,'evidence':evidence})
assert len({tuple(sorted((x['a'],x['b'])))for x in pairs})==len(pairs)
write('final-completed-combined-pairwise-preparation.json',{'scope':'Completed-only root-reviewed semantic pairs. Partial aggregation, not full293 semantic acceptance or proof that unrelated pairs are inequivalent.','completed_count':len(rows),'pair_count':len(pairs),'rows':pairs})
G=read(B/'final-kernel-graph.json');usage=[]
for x in rows:
 n=x['declaration'];body=[a for a,c in G['body_edges']if c==n];typ=[a for a,c in G['type_edges']if c==n]
 usage.append({'declaration':n,'source_callers':x['source_callers'],'native_direct_body_consumers':body,'native_direct_type_consumers':typ,'source_caller_count':len(x['source_callers']),'native_direct_body_consumer_count':len(body),'native_direct_type_consumer_count':len(typ),'report':x['report'],'report_sha256':x['report_sha256'],'has_no_source_or_direct_body_or_type_consumers':not x['source_callers']and not body and not typ})
usage.sort(key=lambda x:(-x['native_direct_body_consumer_count'],-x['source_caller_count'],x['declaration']))
write('final-completed-api-usage-preparation.json',{'scope':'Completed declarations, source callers and verified whole293 native direct graph. Zero counts do not establish external/simp/generated/opaque/transitive deadness. No deletion decision.','completed_count':len(rows),'kernel_graph_sha256':sha(B/'final-kernel-graph.json'),'rows':usage})
U={x['declaration']:x for x in usage};actions=[];defs=[]
fields=['mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']
for x in rows:
 path=Path(x.get('evidence_source',str(R/'.mathlib-quality/overview/evidence'/x['declaration'])))/'overview-entry.json'
 if path.exists():e=read(path);provenance={'path':str(path) if x.get('root_reviewed_unpublished_final_candidate') else str(path.relative_to(R)),'sha256':sha(path),'root_reviewed_unpublished_final_candidate':x.get('root_reviewed_unpublished_final_candidate',False)}
 else:e={};provenance={'method':'Legacy first2 assessments, complete accepted report authoritative; no summary fabricated.'}
 actions.append({'canonical_index':x['canonical_index'],'declaration':x['declaration'],'verdict':x['verdict'],'report':x['report'],'report_sha256':x['report_sha256'],'overview_metadata_provenance':provenance,'accepted_fields':{k:e.get(k)for k in fields},'usage_observation':{k:U[x['declaration']][k]for k in ['source_caller_count','native_direct_body_consumer_count','native_direct_type_consumer_count']}})
 if x['kind']=='def':
  defs.append({'canonical_index':x['canonical_index'],'declaration':x['declaration'],'visibility':x['visibility'],'verdict':x['verdict'],'type':x['type'],'type_provenance':x['type_provenance'],'what':x['what'],'accepted_api_audit':e.get('mathlib_api_audit'),'accepted_action':e.get('action'),'report':x['report'],'report_sha256':x['report_sha256'],'metadata_provenance':provenance})
write('final-completed-action-buckets-preparation.json',{'scope':'Accepted completed-only action material, not final reconciliation. Historical pending-wording reflects original worker snapshot; current independent root acceptance governs review status. NO-upstream does not mandate local deletion.','completed_count':len(rows),'buckets':{v:[x for x in actions if x['verdict']==v]for v in sorted({x['verdict']for x in actions})}})
write('final-completed-definition-api-index-preparation.json',{'scope':'Completed definition audit/action source material. First2 legacy reports remain authoritative. Not final synthesis.','completed_count':len(rows),'completed_definitions':len(defs),'rows':defs,'interpretation':'Separate local semantic API usefulness from independent upstream contribution verdict.'})
M=read(B/'review/corrected-manifest.json');S=read(B/'final-source-statistics-and-imports-preparation.json');files=[]
for f in S['rows']:
 assert sha(R/f['file'])==f['sha256'];ds=[x for x in M if x['file']==f['file']]
 files.append({'file':f['file'],'source_sha256':f['sha256'],'written_declarations':len(ds),'completed_assessments':sum(x['name']in idx for x in ds),'all_assessments_complete':all(x['name']in idx for x in ds),'kind_counts':f['kind_counts'],'physical_lines':f['physical_lines'],'project_imports':f['project_imports'],'external_imports':f['external_imports'],'key_api_used_by_at_least_three_source_declarations':[{'declaration':x['name'],'source_callers':x['project_callers']}for x in ds if len(x['project_callers'])>=3],'unused_in_file':[x['name']for x in ds if not any(c['file']==f['file']for c in x['project_callers'])],'no_explicit_source_caller':[x['name']for x in ds if not x['project_callers']],'proofs_over_30_lines':[{'declaration':x['name'],'proof_lines':x['proof_lines']}for x in ds if x['proof_lines']>30],'declaration_flags':[{'declaration':x['name'],'notes':x['notes']}for x in ds]})
write('final-file-summary-preparation.json',{'scope':'Whole-source structural inventory with separate completed-assessment counts. No assessment of unfinished declarations claimed. Usage observations do not prove deadness.','completed_count':len(rows),'total_declarations':293,'manifest_sha256':sha(B/'review/corrected-manifest.json'),'rows':files})
groups=read(B/'final-completed-yes-mathematical-groups-preparation.json');assigned=[x['declaration']for g in groups['groups']for x in g['assessments']]
yes={x['declaration']for x in rows if x['verdict'].startswith('YES-')};assert len(assigned)==len(set(assigned))and set(assigned)<=yes
groups['completed_count']=len(rows);groups['accepted_yes_count']=len(yes);groups['unassigned_later_yes']=sorted(yes-set(assigned))
for g in groups['groups']:
 for x in g['assessments']:assert idx[x['declaration']]['report_sha256']==x['report_sha256']
write('final-completed-yes-mathematical-groups-preparation.json',groups)
print('PASS scratch refresh:',len(rows),'completed;',len(pairs),'semantic pairs;',len(defs),'definitions;',len(yes),'YES;',len(groups['unassigned_later_yes']),'unassigned. No tracked edits.')
