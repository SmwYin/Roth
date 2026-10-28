#!/usr/bin/env python3
"""Portable read-only validator for scratch and integrated declaration217 evidence."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.lem6M_lt'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(ok,label):
 assert ok,label
 print('PASS',label)
a=load('assessment.json');gate(a['declaration']==N and a['completed']and not a['unresolved']and a['root_acceptance']in['pending','PASS']and not a['production_edits'],'complete read-only assessment')
gate(a['verdict']=='BORDERLINE-needs-human'and all(x=='PASS'or x.startswith('n/a:')for x in a['phases'].values()),'all mandatory phases')
base=load('input-manifest.json')['sources_and_pins'];inputs=load('inputs.json');assert len(inputs)==len(base)==17
for x in inputs:
 p=R/x['path'];assert x['match']and p.stat().st_size==x['bytes']and sha(p)==x['sha256']==x['baseline_sha256']==base[x['path']]['sha256']
gate('2467 jobs'in(D/'baseline-build.txt').read_text(),'17 fresh production/pin hashes and baseline')
for x in load('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']
x=load('literature-source.json');assert sha(R/x['path'])==x['sha256']
row=load('target-metadata.json');src=(R/row['file']).read_text();assert(D/'source-module.lean.txt').read_text()==src
for x in [row]+load('callers.json'):
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert s==x['source']and hashlib.sha256(s.encode()).hexdigest()==x['sha256']
gate(True,'target and all caller source hashes')
v=load('verification.json');allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed and v['declaration']==N and not v['unresolved']
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256']and all(len(l)<=100 for l in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rr=load(x['receipt']);assert rr['request']==x['original_execution_request']and rr['elapsed_ms']>=0;raw=rr['result'];assert not raw.get('isError',False)
 z=raw['structuredContent'];z=z if x['format']=='raw'else z['result'];assert z['success']and not z.get('timed_out')and not z.get('failed_dependencies')
 if x['format']=='disk':
  assert z['partial']is False and s.splitlines()[:9]==(D/'disk-prefix.lean.txt').read_text().splitlines()
  assert rr['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
 else:
  assert rr['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len([l for l in s.splitlines()if l.startswith('import ')])==18 and not re.search(r'^import Roth',s,re.M)
  assert '#check_failure Roth.lem6M_lt'in s and '#check_failure Roth.lem6M'in s
 items=z['diagnostics']if x['format']=='raw'else z['items'];assert not any(y['severity']in['error','warning']or y.get('category')=='sorry'for y in items)
 msg='\n'.join(y['message']for y in items);assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip()for t in ax.split(',')if t.strip()}<=allowed
 fresh='\n'.join(y['message']for y in items if y['line']>=x['native_region_start_line']);assert all(t in fresh for t in x['required_info'])
 gate(True,'exact clean native '+x['label'])
gate(len(v['accepted'])==5 and len(v['rejected'])==2,'five accepted, rejected attempts excluded')
for x in v['rejected']+v['supplementary']:assert(D/x['source']).is_file()and(D/x['receipt']).is_file()and x['reason']
s=(D/'original-executed.lean.txt').read_text();expected=src[src.index('namespace Roth'):].replace('namespace Roth','namespace LemSixM217\nopen Roth',1).replace('end Roth','end LemSixM217');expected=re.sub(r'\blem6M_lt\b','replay',expected);gate(expected in s,'entire original module replay')
items=load('original-receipt.json')['result']['structuredContent']['result']['items'];msg='\n'.join(x['message']for x in items);printed=next(x['message']for x in items if x['message'].startswith('theorem Roth.lem6M_lt :'));typ=printed.split(' : ',1)[1].split(' :=\n',1)[0]
gate('elided'not in typ and typ==load('native-type.json')['type']==load('overview-entry.json')['type'],'full exact native type')
for name in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',expected,re.M):assert "'LemSixM217."+name+"' depends on axioms:"in msg
gate(True,'all public module replay axioms')
order=json.loads((O/'declaration-order.json').read_text());assert len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[216]
terms=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order];arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1;actual=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
gate(actual==terms and len(set(actual))==293,'canonical293 exact private-aware source order')
gate('LEMSIXM217_AUDIT: requested=293; unique=293'in msg and 'LEMSIXM217_AUDIT_PRESENT: present=293; values=293'in msg,'runtime293 names/presence/values')
gate(re.findall(r'LEMSIXM217_DIRECT_CONSUMER: ([^\n]+)',msg)==load('canonical-consumers.json')==['_private.Roth.Theta.0.Roth.theta_phi_lt_aux'],'one direct canonical kernel consumer')
b=(D/'broader-executed.lean.txt').read_text();t=b[b.index('theorem realEnvelope'):b.index('\n\ntheorem replay')]
gate('{q₁ : ℝ}'in t and '(hq₁nonneg : 0 ≤ q₁)'in t and "(hl' : l ≤ 2 ^ r₁)"in t and '(hr₁ : 0 < r₁)'in t,'compiled broader real-base/range/degree guard')
for caller in ['private lemma theta_phi_lt_aux','private lemma theta_lt_succ_aux','theorem Θ_lt']:
 original=src[src.index(caller):].split(' := by',1)[0];new=b[b.index(caller):].split(' := by',1)[0];assert original==new
inline=(D/'inline-guards-executed.lean.txt').read_text();part=inline[inline.index('private lemma theta_phi_lt_aux'):inline.index('private lemma theta_lt_succ_aux')]
gate('have absorbed'in part and '      absorbed (p :='in part and 'replay ('not in part,'whole actual caller proof local inline')
for n in ['zeroSize','zeroDegree','zeroDimension','zeroDelta','negativeLog']:assert 'theorem '+n in inline
c=(D/'composition-executed.lean.txt').read_text();gate('fail_if_success exact?'in c and 'exact Real.pow_div_factorial_le_exp'in c and 'theorem abstractAbsorb'in c,'actual composition and generic transport probes')
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+form+'-'+method+'.json');assert x['form']==form and x['method']==method
  if method=='rg':assert x['command'][0]=='rg'and x['exit_code']in[0,1]and not x['stderr']
  else:assert x['request']['query']and not x['result'].get('isError',False)
gate(True,'15 actual formal method/form cells')
for n in ['web-general','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-locators']:
 x=load(n+'.json');assert x['request']and x['summary']and x['status']and re.fullmatch('[0-9a-f]{64}',x['raw_response_sha256'])and x['raw_response_bytes']>0 and x['full_web_body_archived']is False
 for q in x['locators']:assert q['url'].startswith('https://')and '?'not in q['url']
gate(len({x['q']for x in load('web-general.json')['request']['search_query']})>=3,'three distinct general literature queries')
gate('site:ncatlab.org/ncatlab'in load('ncatlab.json')['request']['search_query'][0]['q'],'distinct nCatLab namespace')
for q in load('arxiv.json')['request']['search_query']:assert 'after:2021-10-28'in q['q']and 'before:2026-10-29'in q['q']
for n in ['source-search','tracked-source-search','inline-audit']:
 x=load(n+'.json');assert x['exit_code']==0 and not x['stderr']
gate(True,'literature/source/caller protocol')
e=load('overview-entry.json');keys=['type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'];assert all(k in e for k in keys)
for k in keys:
 if k not in ['project_dependencies','caller_summary']:assert isinstance(e[k],str)and e[k].strip()
deps=e['project_dependencies'];assert isinstance(deps,list)and len(deps)==len(set(deps))and set(deps)<={x['name']for x in order}and set(deps)==set(row['project_body_refs']+row['project_type_refs'])
for n in ['factorial_coefficient_le_two_pow_aux','two_pow_lt_rpow_aux','Real.rpow_mul_natCast','Real.rpow_add']:assert n in e['how']
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md';text=report.read_text();questions=re.findall(r'^\d\. .+\?$',text,re.M);gate(1<=len(questions)<=5,'concrete bounded future API questions')
manifest=load('copy-manifest.json');assert manifest['completed']and manifest['declaration']==N
for x in manifest['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
gate({p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in manifest['files']}|{'report.md'},'current artifact manifest coverage')
for link in re.findall(r'\]\(([^)]+)\)',text):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS COMPLETE FROZEN217: five clean native runs,17 inputs,293 ordered audit,15search,all phases/currentmanifest')
