from pathlib import Path
import json,hashlib
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth')
I=json.loads((B/'final-completed-inventory-preparation.json').read_text())
S=json.loads((B/'final-file-summary-preparation.json').read_text())
assert I['completed_count']==len(I['rows'])
L=['# Inventory rendering preparation','',f"Completed-only: {I['completed_count']}/293. This is a scratch layout preview, not the final overview.",'']
def prose(x):
 if isinstance(x,list):return '; '.join(prose(v)for v in x) or '[]'
 if isinstance(x,dict):return '; '.join(str(k)+': '+prose(v)for k,v in x.items()) or '{}'
 return str(x)
names=lambda xs: ', '.join('\x60'+str(x)+'\x60'for x in xs) or '[]'
for file in S['rows']:
 rows=[x for x in I['rows'] if x['file']==file['file']]
 assert hashlib.sha256((R/file['file']).read_bytes()).hexdigest()==file['source_sha256']
 L += ['## '+file['file'],'',f"Completed assessments: {len(rows)}/{file['written_declarations']}.",'']
 if not rows:
  L += ['No written declarations: this is the aggregate import module.' if not file['written_declarations'] else 'No declaration assessments accepted in this module yet; the summary below is structural source data only.','']
 for x in rows:
  assert hashlib.sha256(Path(x.get('report_source',str(R/x['report']))).read_bytes()).hexdigest()==x['report_sha256']
  L += ['### '+x['kind']+' '+x['declaration'],'','Type:','', '\x60\x60\x60lean', x['type'],'\x60\x60\x60','']
  for label,key in [('What','what'),('How','how'),('Hypotheses','hypotheses')]:
   assert prose(x[key]).strip();L+=['- **'+label+'**: '+prose(x[key])]
  L += ['- **Uses from project (lexical body)**: '+names(x['source_project_body_refs']),'- **Project references in type**: '+names(x['source_project_type_refs']),'- **Native direct body references**: '+names(x['native_direct_body_dependencies']),'- **Native direct type references**: '+names(x['native_direct_type_dependencies'])]
  same=[c['name']for c in x['source_callers'] if c['file']==x['file']]
  other=[c['name']for c in x['source_callers'] if c['file']!=x['file']]
  L+=['- **Used by in file (lexical)**: '+names(same),'- **Used by other files (lexical)**: '+names(other),'- **Visibility**: '+x['visibility'],f"- **Lines**: {x['start_line']}–{x['end_line']}; proof/body length {x['proof_lines']} lines.",'- **Notes**: '+'; '.join(x['notes']),'- **Verdict**: '+x['verdict']+'; [complete report]('+x['report']+').','']
 L+=['### File structural summary','',f"- Written declarations: {file['written_declarations']}; kinds: "+str(file['kind_counts']),'- **Key API (at least three lexical callers)**: '+names([x['declaration']for x in file['key_api_used_by_at_least_three_source_declarations']]),'- **Unused in file (observation)**: '+names(file['unused_in_file']),'- **Proofs over 30 lines**: '+names([x['declaration']for x in file['proofs_over_30_lines']]),'- Source/direct usage observations do not establish external deadness or simp/generated/transitive closure.','']
(B/'FINAL_INVENTORY_PREVIEW.md').write_text('\n'.join(L)+'\n')
print('PASS scratch inventory layout preview:',I['completed_count'],'completed declarations; no tracked edits.')
