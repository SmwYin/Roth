#!/usr/bin/env python3
"""Read-only canonical228 validator, usable in scratch or integrated evidence layout."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.Θ_lt'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(ok,msg):assert ok,msg;print('PASS',msg)
a=load('assessment.json');v=load('verification.json');e=load('overview-entry.json')
gate(a['declaration']==N and a['canonical_index']==228 and a['completed'] and a['allphases']=='PASS' and not a['unresolved'],'complete228')
gate(a['root_acceptance']in['pending','PASS'] and a['verdict']=='BORDERLINE-needs-human' and not a['production_edits'],'disposition')
gate(set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and set(a['phases'].values())=={'PASS'},'all phases')
ph=load('phase-evidence.json')
for k,n in [('literature_channels',10),('modern_nine',9),('strategy_five',5),('shape_three',3),('infra_six',6)]:gate(len(ph[k])==n and all(ph[k]),k)
gate(1<=len(ph['questions'])<=5 and all(ph[k]for k in['generality','composition','reaim']),'bounded future upstream questions')
row=load('target-metadata.json');callers=load('callers.json')
gate(len(callers)==1 and callers[0]['name']=='Roth.theta_lt_eta_of_sq_log_bound_aux','sole source caller')
for x in[row]+callers:
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert s==x['source'] and hashlib.sha256(s.encode()).hexdigest()==x['sha256']
gate((D/'source-module.lean.txt').read_bytes()==(R/'Roth/Theta.lean').read_bytes()and(D/'caller-module.lean.txt').read_bytes()==(R/'Roth/MainLemma.lean').read_bytes(),'whole source/caller modules exact')
gate((D/'target-excerpt.lean.txt').read_text()==row['source']+'\n','exact target excerpt')
b=load('input-manifest.json')['sources_and_pins'];xs=load('inputs.json');gate(len(xs)==len(b)==17,'17 input manifest')
for x in xs:assert x['match']and sha(R/x['path'])==x['sha256']==x['baseline_sha256']==b[x['path']]['sha256']and(R/x['path']).stat().st_size==x['bytes']
for x in load('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']
lit=load('literature-source.json');gate(sha(R/lit['path'])==lit['sha256'],'local reference hash')
gate(not v['unresolved']and set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'},'standard axioms allowlist')
for x in v['accepted']:
 s=(D/x['source']).read_text();assert sha(D/x['source'])==x['source_sha256']and all(len(l)<=100 for l in s.splitlines())
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rr=load(x['receipt']);assert rr['request']==x['original_execution_request']and rr['elapsed_ms']>=0
 raw=rr['result'];assert not raw.get('isError',False);z=raw['structuredContent'];z=z if x['format']=='raw'else z['result']
 assert z['success']and not z.get('timed_out')and not z.get('failed_dependencies')
 if x['format']=='disk':
  assert z['partial']is False and s.splitlines()[:9]==(D/'disk-prefix.lean.txt').read_text().splitlines()
  assert rr['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean';items=z['items']
 else:
  assert rr['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len([l for l in s.splitlines()if l.startswith('import ')])==18 and not re.search(r'^import Roth',s,re.M)
  assert '#check_failure Roth.Θ_lt'in s;items=z['diagnostics']
 assert not any(y['severity']in['warning','error']or y.get('category')=='sorry'for y in items)
 msg='\n'.join(y['message']for y in items);assert not any(t in msg for t in['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip()for t in ax.split(',')if t.strip()}<=set(v['standard_axioms'])
 fresh='\n'.join(y['message']for y in items if y['line']>=x['native_region_start_line']);assert all(n in fresh for n in x['required_info'])
 gate(True,'exact clean native '+x['label'])
gate(len(v['accepted'])==6 and len(v['rejected'])==4,'six accepted/four separated rejected')
for x in v['rejected']:
 assert(D/x['source']).is_file()and x['reason'];rr=load(x['receipt'])['result']['structuredContent'];z=rr if 'success'in rr else rr['result'];assert not z['success']
gate(load('original-warming-receipt.json')['result']['structuredContent']['result']['partial']is True,'cold partial excluded')
orig=(D/'original-executed.lean.txt').read_text();src=(D/'source-module.lean.txt').read_text();expected=src[src.index('namespace Roth'):].replace('namespace Roth','namespace Theta228\nopen Roth',1).replace('end Roth','end Theta228');expected=re.sub(r'\bΘ_lt\b','replay',expected)
gate(expected in orig,'exact whole originalΘ replay only namespace/target renamed')
items=load('original-receipt.json')['result']['structuredContent']['result']['items'];fresh=[y for y in items if y['line']>=16];msg='\n'.join(y['message']for y in fresh)
for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',expected,re.M):assert "'Theta228."+n+"' depends on axioms:"in msg
gate(True,'all original public replay axioms')
typ=next(y['message'].split(v['full_type_tag'],1)[1]for y in fresh if y['message'].startswith(v['full_type_tag']))
gate(typ==load('native-type.json')['type']==e['type']and 'elided'not in typ,'complete direct kernel type')
order=json.loads((O/'declaration-order.json').read_text());gate(len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[227],'authoritative order snapshot')
terms=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for label in['original','inline']:
 s=(D/(label+'-executed.lean.txt')).read_text();arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arr)==1;actual=[]
 for t in arr[0].split(','):
  t=' '.join(t.split());m=re.fullmatch('Lean\\.mkPrivateNameCore '+chr(96)+'([^ ]+) '+chr(96)+'([^ ]+)',t)
  if m:actual.append(('private',m[1],m[2]))
  else:assert re.fullmatch(chr(96)+'[^ ]+',t);actual.append(('public',t[1:]))
 assert actual==terms and len(set(actual))==293
 zz=load(label+'-receipt.json')['result']['structuredContent']['result'];mm='\n'.join(y['message']for y in zz['items']if y['line']>=16)
 assert 'THETA228_AUDIT: requested=293; unique=293'in mm and 'THETA228_AUDIT_PRESENT: present=293; values=293'in mm
 assert re.findall(r'THETA228_DIRECT_CONSUMER: ([^\n]+)',mm)==load('canonical-consumers.json')==['_private.Roth.MainLemma.0.Roth.theta_lt_eta_of_sq_log_bound_aux']
 gate(True,'exact293 ordered private-aware runtime audit '+label)
for x in load('canonical-preflight.json'):assert x['exit_code']==0 and not x['stderr']and'PASS exact293 unique source order'in x['stdout']
broad=(D/'broader-executed.lean.txt').read_text();tail=broad[broad.index('section Lemma7'):]
gate('(hrlast : 1 ≤ (r (Fin.last n) : ℝ))'in tail and '(hrlast : 3 ≤'not in tail and'3 * 10 ^ (p - 1)'in tail and'lem7_numeric'in tail,'positive final weight; numeric3 retained')
gate('(rp * θ ^ 2 / 2)'in broad and'LemSix213Finite.generic'in broad and'(hrp : 1 ≤ (r none : ℝ))'in broad,'stronger finite-sum/Lemma6 ingredients present')
cs=(D/'callers-executed.lean.txt').read_text();inline=(D/'inline-executed.lean.txt').read_text();caller=callers[0]
gate(caller['signature']in cs and caller['signature']in inline and 'Theta228Broad.replay n hδpos'in cs and'Theta228Broad.bridge'in cs,'original caller signature and exact broader bridge')
helper=row['signature'].replace('theorem Θ_lt','have endpoint',1)+' := '+row['body'];helper='\n'.join('  '+l for l in helper.splitlines())
gate(helper in inline and 'simpa [eta] using endpoint n hδpos'in inline,'exact original endpoint body inside actual caller')
caller_module=(D/'caller-module.lean.txt').read_text();replayed=caller_module[caller_module.index('namespace Roth'):].replace('namespace Roth','namespace Theta228\nopen Roth',1).replace('end Roth','end Theta228');replayed=replayed.replace('  simpa [eta] using Θ_lt n hδpos',helper+'\n  simpa [eta] using endpoint n hδpos')
gate(replayed in inline,'complete actual MainLemma inline replay')
sh=(D/'shapes-executed.lean.txt').read_text();iso=(D/'isolated-executed.lean.txt').read_text()
gate(all('theorem '+n in sh for n in['positiveLast','oneVariable','deltaZeroGuard','individualIndex']),'native alternative shapes andδzero guard')
gate('aeval (fun j ↦ X j + C (α j)) P'in iso and'fail_if_success'in iso and'exact?'in iso and'theorem strictPointwiseNotEnough'in iso,'independent full-form attempt and strict-sup guard')
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+form+'-'+method+'.json');assert x['form']==form and x['method']==method
  if method=='rg':assert x['command'][0]=='rg'and x['exit_code']in[0,1]and not x['stderr']
  else:assert x['request']['query']and 'result'in x and not x['result'].get('isError',False)
gate(True,'all15 actual formal-search cells')
for n in['web-general','web-aliases','nlab','ncatlab','stacks','mathoverflow','arxiv','arxiv-retry','primary','primary-extra','primary-lemma']:
 x=load(n+'.json');assert x['request']and x['status']and x['summary']and re.fullmatch('[0-9a-f]{64}',x['raw_response_sha256'])and x['raw_response_bytes']>0 and x['full_web_body_archived']is False
 for u in x['locators']:assert u.startswith('http')and not u.endswith((':',';',','))and'...'not in u
assert len({q['q']for q in load('web-general.json')['request']['search_query']})>=3
assert'site:ncatlab.org/ncatlab'in load('ncatlab.json')['request']['search_query'][0]['q']
for n in['arxiv','arxiv-retry']:
 for q in load(n+'.json')['request']['search_query']:assert'after:2021-10-28'in q['q']and'before:2026-10-29'in q['q']
gate(True,'all named literature channels and primary/failure accounting')
for n in['source-search','tracked-source-search','inline-audit']:
 x=load(n+'.json');assert x['exit_code']==0 and not x['stderr']
keys=['type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'];gate(all(k in e for k in keys),'exact overview keys')
for k in keys:
 if k not in['project_dependencies','caller_summary']:assert isinstance(e[k],str)and e[k].strip()
assert set(e['project_dependencies'])==set(row['project_type_refs']+row['project_body_refs'])
assert all(n in e['how']for n in['theta_lt_base_aux','theta_denominators_one_lt_aux','theta_lt_of_large_delta_aux','theta_lt_succ_aux','Θ_option_le','theta_phi_lt_aux'])
build=load('full-build.json');gate(build['command']==['/Users/ramin/.elan/bin/lake','build']and build['exit_code']==0 and build['duration_seconds']>=0 and build['fresh17_inputs'],'file-end full build exit0')
assert build['input_manifest_sha256']==sha(D/'inputs.json')
for k in['stdout','stderr']:assert sha(D/build[k])==build[k+'_sha256']
gate((D/'full-build.stdout.txt').read_text().strip()=='Build completed successfully (2467 jobs).'and(D/'full-build.stderr.txt').stat().st_size==0,'complete exact build logs')
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md';manifest=load('copy-manifest.json');assert manifest['declaration']==N and manifest['completed']
for x in manifest['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
gate({p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in manifest['files']}|{'report.md'},'current manifest artifact hashes/bytes and coverage')
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS COMPLETE FROZEN228: six clean native,17 inputs,exact293audit,15 search cells,fullbuild,all phases')
