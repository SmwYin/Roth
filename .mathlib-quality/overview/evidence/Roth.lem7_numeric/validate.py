#!/usr/bin/env python3
"""Portable, read-only219 package validator; current manifest always authoritative."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
O=R/'.mathlib-quality/overview';N='Roth.lem7_numeric'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(ok,label):
 assert ok,label
 print('PASS',label)
a=load('assessment.json')
gate(a['declaration']==N and a['canonical_index']==219 and a['completed'] and not a['unresolved'] and a['root_acceptance'] in ['pending','PASS'] and not a['production_edits'],'completed read-only219')
required=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8','parent_reaim','chatgpt_math']
gate(a['verdict']=='BORDERLINE-needs-human' and set(a['phases'])==set(required) and all(x=='PASS' or x.startswith('n/a:')for x in a['phases'].values()),'all mandatory phases')
gate(load('phase-ledger.json')['phases']==a['phases'],'phase ledger agrees')
base=load('input-manifest.json')['sources_and_pins'];inputs=load('inputs.json');assert len(inputs)==len(base)==17
for x in inputs:
 p=R/x['path'];assert x['match'] and p.stat().st_size==x['bytes'] and sha(p)==x['sha256']==x['baseline_sha256']==base[x['path']]['sha256']
gate('2467 jobs' in (D/'baseline-build.txt').read_text(),'fresh17 baseline hashes')
for x in load('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256'] and (R/x['path']).stat().st_size==x['bytes']
x=load('literature-source.json');assert sha(R/x['path'])==x['sha256']
row=load('target-metadata.json');src=(R/row['file']).read_text();assert (D/'source-module.lean.txt').read_text()==src
for x in [row]+load('callers.json'):
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert s==x['source'] and hashlib.sha256(s.encode()).hexdigest()==x['sha256']
gate(True,'declaring module/full caller/source hashes')
v=load('verification.json');allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed and v['declaration']==N and not v['unresolved']
labels=['original','isolated','broader','inline','shape'];assert [x['label']for x in v['accepted']]==labels
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256'] and all(len(l)<=100 for l in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rr=load(x['receipt']);assert rr['request']==x['original_execution_request'] and rr['elapsed_ms']>=0
 raw=rr['result'];assert not raw.get('isError',False);z=raw['structuredContent'];z=z if x['format']=='raw' else z['result'];assert z['success'] and not z.get('timed_out') and not z.get('failed_dependencies')
 if x['format']=='disk':
  assert z['partial'] is False and s.splitlines()[:9]==(D/'disk-prefix.lean.txt').read_text().splitlines()
  assert rr['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
 else:
  assert rr['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len([l for l in s.splitlines()if l.startswith('import ')])==18 and not re.search(r'^import Roth',s,re.M)
  assert '#check_failure Roth.lem7_numeric' in s
 items=z['diagnostics'] if x['format']=='raw' else z['items'];assert not any(y['severity'] in ['error','warning'] or y.get('category')=='sorry' for y in items)
 msg='\n'.join(y['message']for y in items);assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip()for t in ax.split(',')if t.strip()}<=allowed
 fresh='\n'.join(y['message']for y in items if y['line']>=x['native_region_start_line']);assert all(t in fresh for t in x['required_info'])
 if x['label'] in ['original','broader','inline']:
  ns={'original':'Numeric219','broader':'Numeric219Broader','inline':'Numeric219Inline'}[x['label']]
  for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',s,re.M):assert "'"+ns+'.'+n+"' depends on axioms:" in fresh
 gate(True,'exact clean native '+x['label'])
assert len(v['rejected'])==2
for x in v['rejected']+v['supplementary']:
 assert (D/x['source']).is_file() and (D/x['receipt']).is_file() and x['reason'];rr=load(x['receipt']);assert rr['elapsed_ms']>=0
 if 'code'in rr['request']:assert rr['request']['code']==(D/x['source']).read_text()
s=(D/'original-executed.lean.txt').read_text();expected=src[src.index('namespace Roth'):].replace('namespace Roth','namespace Numeric219\nopen Roth',1).replace('end Roth','end Numeric219');expected=re.sub(r'\blem7_numeric\b','replay',expected)
gate(expected in s,'entire exact module replay')
items=load('original-receipt.json')['result']['structuredContent']['result']['items'];msg='\n'.join(x['message']for x in items);printed=next(x['message']for x in items if x['message'].startswith('theorem '+N+' :'));typ=printed.split(' : ',1)[1].split(' :=\n',1)[0]
gate('elided'not in typ and typ==load('native-type.json')['type']==load('overview-entry.json')['type'],'complete fresh native type')
order=json.loads((O/'declaration-order.json').read_text());assert len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[218]
terms=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order];arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1;actual=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
gate(actual==terms and len(set(actual))==293,'exact293 ordered private-aware canonical array')
pre=load('canonical-preflight.json');assert pre['exit_code']==0 and not pre['stderr']
assert 'NUMERIC219_AUDIT: requested=293; unique=293'in msg and 'NUMERIC219_AUDIT_PRESENT: present=293; values=293'in msg
gate(re.findall(r'NUMERIC219_DIRECT_CONSUMER: ([^\n]+)',msg)==load('canonical-consumers.json')==['_private.Roth.Theta.0.Roth.theta_phi_lt_aux'],'runtime293 and sole direct canonical consumer')
b=(D/'broader-executed.lean.txt').read_text();assert '(hΦ : Φ ≤ 4 * 10 ^ (p - 1)'in b and 'theorem wider'in b and 'apply wider hp hδ0 hδ1'in b
inline=(D/'inline-executed.lean.txt').read_text();part=inline[inline.index('private lemma theta_phi_lt_aux'):inline.index('private lemma theta_lt_succ_aux')]
assert 'have numeric'in part and 'apply numeric hp'in part and 'theorem lem7_numeric'not in inline and 'apply lem7_numeric'not in part
for c in ['private lemma theta_phi_lt_aux','private lemma theta_lt_succ_aux','theorem Θ_lt']:
 for z in [b,inline]:assert src[src.index(c):].split(' := by',1)[0]==z[z.index(c):].split(' := by',1)[0]
gate(True,'coefficient4 with delta<=1,unchanged full caller/downstream signatures,local inline')
c=(D/'isolated-executed.lean.txt').read_text();assert 'fail_if_success exact?'in c and 'solve\n    | simp only [Real.sqrt_eq_rpow]'in c
for n in ['envelope','wider','directProbe','zeroDelta','dimensionOne','largeDelta']:assert 'theorem '+n in c
shape=(D/'shape-executed.lean.txt').read_text()
for n in ['divided','successor','negativePhi','equalityUpper','noPhiCap']:assert 'theorem '+n in shape
gate(True,'generic/composition/counterexample/shape/negativePhi/equality probes')
assert load('concrete-diagnostic.json')['named_object_diagnostic']=={'Θ':0,'lem6Φ':0,'lem7_numeric':0}
x=load('pinned-candidate-locators.json');assert x['exit_code']==0 and not x['stderr']
x=load('completion-input-refresh.json');assert x['source_pin_count']==17 and x['all_current_hashes_match']
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+form+'-'+method+'.json');assert x['form']==form and x['method']==method
  if method=='rg':assert x['command'][0]=='rg'and x['exit_code']in[0,1]and not x['stderr']
  else:assert x['request']['query']and not x['result'].get('isError',False)
gate(True,'15 actual formal method/form cells')
for n in ['web-general','nlab','ncatlab','stacks','mathoverflow','arxiv','arxiv-refined','primary','primary-locators','recent-primary']:
 x=load(n+'.json');assert x['request']and x['summary']and x['status']and re.fullmatch('[0-9a-f]{64}',x['raw_response_sha256'])and x['raw_response_bytes']>0 and x['full_web_body_archived']is False
 for l in x['locators']:assert l['url'].startswith('https://')and '?'not in l['url']and '...'not in l['url']and '…'not in l['url']and not l['url'].endswith((':',',',';','.'))
assert len({x['q']for x in load('web-general.json')['request']['search_query']})>=3
assert 'site:ncatlab.org/ncatlab'in load('ncatlab.json')['request']['search_query'][0]['q']
for n in ['arxiv','arxiv-refined']:
 for q in load(n+'.json')['request']['search_query']:assert 'after:2021-10-28'in q['q']and 'before:2026-10-29'in q['q']
for n in ['source-search','tracked-source-search','inline-audit']:
 x=load(n+'.json');assert x['exit_code']==0 and not x['stderr']
gate(True,'full literature and ignore-independent caller protocol')
e=load('overview-entry.json');keys=['type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'];assert all(k in e for k in keys)
for k in keys:
 if k not in ['project_dependencies','caller_summary']:assert isinstance(e[k],str)and e[k].strip()
assert e['project_dependencies']==row['project_body_refs']==row['project_type_refs']==[]
assert all(n in e['how'] for n in ["Real.sqrt_lt'",'Real.rpow_mul_natCast'])
assert e['caller_summary']['source_callers']==[x['name']for x in load('callers.json')]
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md';text=report.read_text();assert typ in text
assert 1<=len(re.findall(r'^\d\. .+\?$',text,re.M))<=5
gate(True,'required overview keys/full type/bounded future questions')
manifest=load('copy-manifest.json');assert manifest['completed']and manifest['declaration']==N
for x in manifest['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
gate({p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in manifest['files']}|{'report.md'},'current artifact manifest coverage')
for l in re.findall(r'\]\(([^)]+)\)',text):
 if l.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert l.startswith(prefix)and(D/l[len(prefix):]).is_file(),l
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS COMPLETE FROZEN219:five clean native runs,17 inputs,293 ordered audit,15search,all phases/currentmanifest')
