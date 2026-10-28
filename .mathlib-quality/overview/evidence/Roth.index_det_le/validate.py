#!/usr/bin/env python3
"""Portable read-only validator for current scratch or integrated evidence."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
O=R/'.mathlib-quality/overview'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(cond,what):
 assert cond,what
 print('PASS',what)
a=load('assessment.json');N=a['declaration'];row=load('target-metadata.json')
gate(N=='Roth.index_det_le' and a['canonical_index']==209 and a['completed'] and a['allphases']=='PASS' and not a['unresolved'],'completed209')
gate(a['verdict']=='BORDERLINE-needs-human' and a['root_acceptance'] in ['pending','PASS'] and not a['production_edits'],'disposition')
gate(set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and all(v=='PASS'for v in a['phases'].values()),'all mandatory phases')
ph=load('phase-evidence.json')
for key,n in [('literature_channels',10),('modern_nine',9),('strategy_five',5),('shape_three',3),('infra_six',6)]:gate(len(ph[key])==n and all(ph[key]),key)
gate(1<=len(ph['questions'])<=5 and ph['composition'] and ph['reaim'],'verdict questions and synthesis')
callers=load('callers.json')
gate(len(callers)==1 and callers[0]['name']=='Roth.index_le_lem6','complete actual caller inventory')
for x in [row]+callers:
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])
 gate(s==x['source'] and hashlib.sha256(s.encode()).hexdigest()==x['sha256'],'current declaration '+x['name'])
gate((D/'source-module.lean.txt').read_bytes()==(R/row['file']).read_bytes(),'whole declaring source')
gate((D/'target-excerpt.lean.txt').read_text()==row['source']+'\n','exact target excerpt')
b=load('input-manifest.json')['sources_and_pins'];checks=load('inputs.json')
gate(len(checks)==len(b)==17,'17 inputs')
for x in checks:
 p=R/x['path'];assert x['match'] and sha(p)==x['sha256']==x['baseline_sha256']==b[x['path']]['sha256'] and p.stat().st_size==x['bytes']
gate('2467 jobs'in(D/'baseline-build.txt').read_text(),'unchanged clean baseline')
v=load('verification.json');gate(v['declaration']==N and not v['unresolved'],'verification ledger')
gate(set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'},'exact standard axiom allowlist')
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256']
 assert all(len(l)<=100 for l in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rr=load(x['receipt']);assert rr['request']==x['original_execution_request'] and rr['elapsed_ms']>=0
 r=rr['result'];assert not r.get('isError',False)
 z=r['structuredContent'];z=z if x['format']=='raw' else z['result']
 assert z['success'] and not z.get('timed_out') and not z.get('failed_dependencies')
 if x['format']=='disk':assert z['partial']is False and s.splitlines()[:9]==(D/'disk-prefix.lean.txt').read_text().splitlines()
 else:
  assert rr['request']['code']==s
  assert s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len([l for l in s.splitlines()if l.startswith('import ')])==18
  assert not re.search(r'^import Roth',s,re.M) and '#check_failure Roth.index_det_le'in s
 items=z['diagnostics'] if x['format']=='raw' else z['items']
 assert not any(y['severity']in ['error','warning'] or y.get('category')=='sorry'for y in items)
 msgs='\n'.join(y['message']for y in items)
 assert not any(t in msgs for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msgs):assert {t.strip()for t in ax.split(',')if t.strip()}<=set(v['standard_axioms'])
 fresh='\n'.join(y['message']for y in items if y['line']>=x['native_region_start_line'])
 assert all(t in fresh for t in x['required_info'])
 gate(True,'exact complete native '+x['label'])
for x in v['rejected']:assert not x['accepted'] and (D/x['source']).exists() and (D/x['receipt']).exists()
gate(len(v['rejected'])==2,'rejected evidence separately excluded')
orig=(D/'original-executed.lean.txt').read_text();source=(R/'Roth/Theta.lean').read_text();expected=source[source.index('namespace Roth'):].replace('namespace Roth','namespace DetUpper209\nopen Roth',1).replace('end Roth','end DetUpper209');expected=re.sub(r'\bindex_det_le\b','replay',expected)
gate(expected in orig,'whole original module replay with only namespace/target rename')
rr=load('original-receipt.json')['result']['structuredContent']['result'];items=rr['items'];msg='\n'.join(y['message']for y in items if y['line']>=16)
type_msg=next(y['message']for y in items if y['message'].startswith('theorem Roth.index_det_le.'))
typ=type_msg.split(' : ',1)[1].split(' :=\n',1)[0]
gate(typ==load('native-type.json')['type']==load('overview-entry.json')['type'],'full original elaborated type')
for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',expected,re.M):assert "'DetUpper209."+n+"' depends on axioms:" in msg
gate(True,'all public original module axiom checks')
order=json.loads((O/'declaration-order.json').read_text())
gate(len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[208],'canonical snapshot exact order')
terms=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',orig,re.S);assert len(arr)==1
actual=[]
for t in arr[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:
  assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
gate(actual==terms and len(set(actual))==293,'canonical source exact293 unique names')
gate('DETUPPER209_AUDIT: requested=293; unique=293'in msg and 'DETUPPER209_AUDIT_PRESENT: present=293; values=293'in msg,'runtime canonical293 present/value audit')
gate(re.findall('DETUPPER209_DIRECT_CONSUMER: ([^\n]+)',msg)==load('canonical-consumers.json')==['Roth.index_le_lem6'],'direct kernel consumers')
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+form+'-'+method+'.json')
  assert x['method']==method and x['form']==form
  if method=='rg':assert x['command'][0]=='rg' and x['exit_code']in[0,1]and not x['stderr']
  else:assert x['request']['query'] and 'result'in x
for method in ['leanfinder','loogle','leansearch','rg','local_search']:
 x=load('reaim-'+method+'.json');assert x['method']==method and x['form']=='parent re-aim'
gate(True,'15 actual search cells plus5 parent reaim cells')
for name in ['web-specific','web-general','web-aliases','nlab','ncatlab','stacks','mathoverflow','arxiv','primary']:
 x=load(name+'.json');assert x['request']and x['summary'] and re.fullmatch('[0-9a-f]{64}',x['raw_response_sha256']) and x['raw_response_bytes']>0 and x['status']
gate('site:ncatlab.org/ncatlab'in load('ncatlab.json')['request']['search_query'][0]['q'],'distinct nCatLab namespace')
query=load('arxiv.json')['request']['search_query'][0]['q'];gate('after:2021-10-28'in query and 'before:2026-10-29'in query,'recent literature exact window')
for n in ['source-search.json','tracked-source-search.json','inline-audit.json']:
 x=load(n);assert x['exit_code']==0 and not x['stderr']
e=load('overview-entry.json');keys=['type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'];gate(all(k in e for k in keys),'exact required overview keys')
gate(isinstance(e['junk'],str) and bool(e['junk'].strip()),'explanatory nonblank junk field')
deps=e['project_dependencies'];canonical={x['name']for x in order}
gate(isinstance(deps,list)and len(deps)==len(set(deps)) and set(deps)<=canonical and set(deps)==set(row['project_body_refs']+row['project_type_refs']),'canonical dependency names only')
gate(all(n in e['how']for n in ['abs_coeff_det_hasseDeriv_le','coeff_rename_mul_aeval','index_separated_mul_le_aux']),'connected How names actual three source stages')
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md'
m=load('copy-manifest.json');gate(m['completed']and m['declaration']==N,'current copy manifest')
for x in m['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json','root-review.json'}
gate({p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'},'current manifest complete artifact coverage')
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS COMPLETE FROZEN candidate',N,'all phases, exact native proofs, canonical293,20search cells,17inputs,current manifest')
