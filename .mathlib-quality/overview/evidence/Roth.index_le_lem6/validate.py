#!/usr/bin/env python3
"""Read-only validation of scratch or integrated completed213 evidence."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.index_le_lem6'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(x,m):assert x,m;print('PASS',m)
a=load('assessment.json');gate(a['declaration']==N and a['canonical_index']==213 and a['completed'] and a['allphases']=='PASS' and not a['unresolved'],'complete213')
gate(a['verdict']=='BORDERLINE-needs-human' and a['root_acceptance']in['pending','PASS'] and not a['production_edits'],'disposition')
gate(set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and set(a['phases'].values())=={'PASS'},'all phases')
ph=load('phase-evidence.json')
for k,n in [('literature_channels',10),('modern_nine',9),('strategy_five',5),('shape_three',3),('infra_six',6)]:gate(len(ph[k])==n and all(ph[k]),k)
gate(1<=len(ph['questions'])<=5 and ph['generality'] and ph['composition'] and ph['reaim'],'scope questions and synthesis')
row=load('target-metadata.json');callers=load('callers.json');gate(len(callers)==1 and callers[0]['name']=='Roth.Θ_option_le','complete caller inventory')
for x in[row]+callers:
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);gate(s==x['source'] and hashlib.sha256(s.encode()).hexdigest()==x['sha256'],'exact source '+x['name'])
gate((D/'source-module.lean.txt').read_bytes()==(R/'Roth/Theta.lean').read_bytes(),'whole module exact')
gate((D/'target-excerpt.lean.txt').read_text()==row['source']+'\n','target excerpt exact')
b=load('input-manifest.json')['sources_and_pins'];xs=load('inputs.json');gate(len(xs)==len(b)==17,'17 production/pin inputs')
for x in xs:assert x['match'] and sha(R/x['path'])==x['sha256']==x['baseline_sha256']==b[x['path']]['sha256'] and (R/x['path']).stat().st_size==x['bytes']
gate('2467 jobs'in(D/'baseline-build.txt').read_text(),'reusable clean baseline')
for x in load('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']
gate(True,'pinned ingredient sources')
v=load('verification.json');gate(v['declaration']==N and not v['unresolved'] and set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'},'exact standard axiom allowlist')
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256']
 assert all(len(l)<=100 for l in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rr=load(x['receipt']);assert rr['request']==x['original_execution_request'] and rr['elapsed_ms']>=0
 raw=rr['result'];assert not raw.get('isError',False);z=raw['structuredContent'];z=z if x['format']=='raw'else z['result']
 assert z['success'] and not z.get('timed_out') and not z.get('failed_dependencies')
 if x['format']=='disk':
  assert z['partial']is False and s.splitlines()[:9]==(D/'disk-prefix.lean.txt').read_text().splitlines()
  assert rr['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
 else:
  assert rr['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len([l for l in s.splitlines()if l.startswith('import ')])==18 and not re.search(r'^import Roth',s,re.M)
  assert '#check_failure Roth.index_le_lem6'in s
 items=z['diagnostics']if x['format']=='raw'else z['items'];assert not any(y['severity']in['error','warning']or y.get('category')=='sorry'for y in items)
 msg='\n'.join(y['message']for y in items);assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip()for t in ax.split(',')if t.strip()}<=set(v['standard_axioms'])
 fresh='\n'.join(y['message']for y in items if y['line']>=x['native_region_start_line']);assert all(t in fresh for t in x['required_info'])
 gate(True,'clean exact native '+x['label'])
gate(not v['rejected'] and len(v['accepted'])==6,'accepted executions distinguished from incomplete warmup')
gate(load('original-warming-receipt.json')['result']['structuredContent']['result']['partial']is True,'warmup explicitly incomplete')
orig=(D/'original-executed.lean.txt').read_text();src=(R/'Roth/Theta.lean').read_text();expected=src[src.index('namespace Roth'):].replace('namespace Roth','namespace LemSix213\nopen Roth',1).replace('end Roth','end LemSix213');expected=re.sub(r'\bindex_le_lem6\b','replay',expected)
gate(expected in orig,'whole original module with only namespace/target rename')
items=load('original-receipt.json')['result']['structuredContent']['result']['items'];msg='\n'.join(y['message']for y in items if y['line']>=16)
m=next(y['message']for y in items if y['message'].startswith('theorem Roth.index_le_lem6.'));typ=m.split(' : ',1)[1].split(' :=\n',1)[0]
gate(typ==load('native-type.json')['type']==load('overview-entry.json')['type'] and '3237 characters elided'in m,'full original type; printer elision disclosed')
for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',expected,re.M):assert "'LemSix213."+n+"' depends on axioms:" in msg
gate(True,'all public original module axiom checks')
order=json.loads((O/'declaration-order.json').read_text());gate(len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[212],'exact canonical source order')
terms=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',orig,re.S);assert len(arr)==1;actual=[]
for t in arr[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
gate(actual==terms and len(set(actual))==293,'exact293 unique canonical names')
gate('LEMSIX213_AUDIT: requested=293; unique=293'in msg and 'LEMSIX213_AUDIT_PRESENT: present=293; values=293'in msg,'runtime293 present/value audit')
gate(re.findall(r'LEMSIX213_DIRECT_CONSUMER: ([^\n]+)',msg)==load('canonical-consumers.json')==['Roth.Θ_option_le'],'direct kernel-value consumers')
noq=(D/'noq-executed.lean.txt').read_text();low=(D/'lowdegree-executed.lean.txt').read_text();inline=(D/'inline-executed.lean.txt').read_text()
gate('(_hq : ∀ j, 0 < q j)'not in noq[noq.index('theorem replay'):noq.index('theorem Θ_option_le')],'q premise removed from actual target')
gate('theorem replay' in low and '(hrp : 1 ≤ (r none : ℝ))'in low and '(hrp : 3 ≤ (r none : ℝ))'in low[low.index('theorem Θ_option_le'):],'broader target and original caller premise distinct')
gate('LemSix213Finite.generic'in low and '(rp * θ ^ 2 / 2)'in low and '2 * l ≤ 4 * rp'in low,'new half-quadratic/numerical proof retained')
gate('index_le_lem6'not in inline and 'theorem inlineCaller'in inline,'complete caller proof inlined without original target')
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+f+'-'+meth+'.json');assert x['form']==f and x['method']==meth
  if meth=='rg':assert x['command'][0]=='rg'and x['exit_code']in[0,1]and not x['stderr']
  else:assert x['request']['query']and 'result'in x
for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
 x=load('reaim-'+meth+'.json');assert x['form']=='parent re-aim'and x['method']==meth
gate(True,'15 search cells and5 parent reaims')
gate(load('search-current-loogle-retry.json')['request']['query']=='"index_le_lem6"','failed current Loogle search retried')
for n in ['web-specific','web-general','web-aliases','nlab','ncatlab','stacks','mathoverflow','arxiv','primary','primary-extra']:
 x=load(n+'.json');assert x['request']and x['summary']and x['status']and re.fullmatch('[0-9a-f]{64}',x['raw_response_sha256'])and x['raw_response_bytes']>0 and not x['full_web_body_archived']
gate(len(load('web-general.json')['request']['search_query'])>=3,'three distinct general web queries')
gate('site:ncatlab.org/ncatlab'in load('ncatlab.json')['request']['search_query'][0]['q'],'distinct nCatLab query')
q=load('arxiv.json')['request']['search_query'][0]['q'];gate('after:2021-10-28'in q and 'before:2026-10-29'in q,'five-year recent window')
for n in ['source-search.json','tracked-source-search.json','inline-audit.json']:
 x=load(n);assert x['exit_code']==0 and not x['stderr']
e=load('overview-entry.json');keys=['type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'];gate(all(k in e for k in keys),'exact overview keys')
for k in ['type','what','how','hypotheses','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert isinstance(e[k],str)and e[k].strip()
deps=e['project_dependencies'];canonical={x['name']for x in order};gate(isinstance(deps,list)and len(deps)==len(set(deps))and set(deps)<=canonical and set(deps)==set(row['project_body_refs']+row['project_type_refs']),'canonical dependency list')
gate(all(n in e['how']for n in ['exists_det_eq_mul','sum_max_sub_le_index_det','index_det_le','min_le_sum_max','index_numeric_bound_aux']),'How names actual mathematical stages')
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md';m=load('copy-manifest.json');gate(m['completed']and m['declaration']==N,'current complete manifest')
for x in m['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
gate({p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'},'complete current artifact coverage')
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS COMPLETE FROZEN213 all phases,6native,exact293,20search,17inputs,manifest')
