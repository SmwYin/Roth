#!/usr/bin/env python3
"""Read-only scratch/integrated validation of complete canonical214."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.Θ_option_le'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(ok,msg):assert ok,msg;print('PASS',msg)
a=load('assessment.json')
gate(a['declaration']==N and a['canonical_index']==214 and a['completed'] and a['allphases']=='PASS' and not a['unresolved'],'complete214')
gate(a['verdict']=='BORDERLINE-needs-human' and a['root_acceptance']in['pending','PASS'] and not a['production_edits'],'disposition')
gate(set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and set(a['phases'].values())=={'PASS'},'all phases')
ph=load('phase-evidence.json')
for k,n in [('literature_channels',10),('modern_nine',9),('strategy_five',5),('shape_three',3),('infra_six',6)]:gate(len(ph[k])==n and all(ph[k]),k)
gate(1<=len(ph['questions'])<=5 and all(ph[k]for k in ['generality','composition','reaim']),'synthesis and future questions')
row=load('target-metadata.json');callers=load('callers.json')
gate(len(callers)==1 and callers[0]['name']=='Roth.theta_lt_succ_aux','complete source caller inventory')
for x in[row]+callers:
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']])
 gate(s==x['source'] and hashlib.sha256(s.encode()).hexdigest()==x['sha256'],'exact source '+x['name'])
gate((D/'source-module.lean.txt').read_bytes()==(R/'Roth/Theta.lean').read_bytes(),'whole production module exact')
gate((D/'target-excerpt.lean.txt').read_text()==row['source']+'\n','target excerpt')
b=load('input-manifest.json')['sources_and_pins'];xs=load('inputs.json')
gate(len(xs)==len(b)==17,'17 production/pin inputs')
for x in xs:assert x['match'] and sha(R/x['path'])==x['sha256']==x['baseline_sha256']==b[x['path']]['sha256'] and (R/x['path']).stat().st_size==x['bytes']
gate('2467 jobs'in(D/'baseline-build.txt').read_text(),'reusable build provenance')
for x in load('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']
lit=load('literature-source.json');gate(sha(R/lit['path'])==lit['sha256'],'local literature source')
v=load('verification.json')
gate(v['declaration']==N and not v['unresolved'] and set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'},'exact standard axiom allowlist')
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
  assert '#check_failure Roth.Θ_option_le'in s
 items=z['diagnostics']if x['format']=='raw'else z['items']
 assert not any(y['severity']in['error','warning']or y.get('category')=='sorry'for y in items)
 msg='\n'.join(y['message']for y in items)
 assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {t.strip()for t in ax.split(',')if t.strip()}<=set(v['standard_axioms'])
 fresh='\n'.join(y['message']for y in items if y['line']>=x['native_region_start_line'])
 assert all(t in fresh for t in x['required_info'])
 gate(True,'clean exact native '+x['label'])
gate(len(v['accepted'])==6 and len(v['rejected'])==2,'six accepted and separate rejected drafts')
for x in v['rejected']:
 assert (D/x['source']).is_file() and (D/x['receipt']).is_file() and x['reason']
 z=load(x['receipt'])['result']['structuredContent']['result'];assert not z['success']
gate(load('original-warming-receipt.json')['result']['structuredContent']['result']['partial']is True,'warmup excluded')
src=(R/'Roth/Theta.lean').read_text();orig=(D/'original-executed.lean.txt').read_text()
expected=src[src.index('namespace Roth'):].replace('namespace Roth','namespace ThetaOption214\nopen Roth',1).replace('end Roth','end ThetaOption214')
expected=re.sub(r'\bΘ_option_le\b','replay',expected)
gate(expected in orig,'complete original module replay only namespace/target renamed')
items=load('original-receipt.json')['result']['structuredContent']['result']['items'];msg='\n'.join(y['message']for y in items if y['line']>=16)
m=next(y['message']for y in items if y['message'].startswith('theorem Roth.Θ_option_le.'))
typ=m.split(' : ',1)[1].split(' :=\n',1)[0]
gate(typ==load('native-type.json')['type']==load('overview-entry.json')['type'] and 'characters elided'not in m,'full native original statement')
for n in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',expected,re.M):assert "'ThetaOption214."+n+"' depends on axioms:"in msg
gate(True,'every public original module axiom check')
order=json.loads((O/'declaration-order.json').read_text())
gate(len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[213],'canonical order snapshot')
terms=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
arr=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',orig,re.S);assert len(arr)==1;actual=[]
for t in arr[0].split(','):
 t=' '.join(t.split());m=re.fullmatch('Lean\\.mkPrivateNameCore '+chr(96)+'([^ ]+) '+chr(96)+'([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:assert re.fullmatch(chr(96)+'[^ ]+',t);actual.append(('public',t[1:]))
gate(actual==terms and len(set(actual))==293,'exact293 private-aware ordered names')
gate('THETAOPTION214_AUDIT: requested=293; unique=293'in msg and 'THETAOPTION214_AUDIT_PRESENT: present=293; values=293'in msg,'runtime293 present/value audit')
gate(re.findall(r'THETAOPTION214_DIRECT_CONSUMER: ([^\n]+)',msg)==load('canonical-consumers.json')==['_private.Roth.Theta.0.Roth.theta_lt_succ_aux'],'sole direct kernel-value consumer')
for label in ['broader','lowdegree']:
 s=(D/(label+'-executed.lean.txt')).read_text();target=s[s.index('theorem replay'):s.index('\nend Lemma6')]
 gate(not re.search(r'\(_?hq :',target) and '(hB : 1 ≤ B)'not in target and 'Real.sSup_le'in target and 'Θ_nonneg'in target,'arbitrary B/no-q '+label)
 for caller in ['private lemma theta_lt_succ_aux','theorem Θ_lt']:
  original_sig=src[src.index(caller):].split(' := by',1)[0];actual_sig=s[s.index(caller):].split(' := by',1)[0]
  gate(original_sig==actual_sig,'original caller/final statement '+label+' '+caller)
low=(D/'lowdegree-executed.lean.txt').read_text()
gate('(hrp : 1 ≤ (r none : ℝ))'in low[low.index('theorem replay'):] and 'LemSix213Finite.generic'in low and '(rp * θ ^ 2 / 2)'in low,'positive distinguished weight carries new proof')
inline=(D/'inline-executed.lean.txt').read_text()
gate('theorem callerInline'in inline and 'have optionBound {τ : Type}'in inline and '(Θ_option_le 'not in inline and 'index_le_lem6 hδ0'in inline,'entire actual caller with original target body inlined')
guards=(D/'guards-executed.lean.txt').read_text()
gate('theorem smallB_empty'in guards and 'Int.one_le_abs'in guards and 'Real.sSup_empty'in guards,'small-B proof exact')
for f in ['current','standard','abstract']:
 for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=load('search-'+f+'-'+meth+'.json');assert x['form']==f and x['method']==meth
  if meth=='rg':assert x['command'][0]=='rg'and x['exit_code']in[0,1]and not x['stderr']
  else:assert x['request']['query']and 'result'in x
for meth in ['leanfinder','loogle','leansearch','rg','local_search']:
 x=load('reaim-'+meth+'.json');assert x['form']=='parent re-aim'and x['method']==meth and x['request']['query']
gate(True,'15 actual cells and5 parent reaim searches')
gate(load('search-abstract-loogle.json')['result']['isError']is True and not load('search-abstract-loogle-retry.json')['result']['isError'],'failed Loogle query retried')
for n in ['web-specific','web-general','web-aliases','nlab','ncatlab','stacks','mathoverflow','arxiv','arxiv-retry','primary','primary-extra']:
 x=load(n+'.json');assert x['request']and x['summary']and x['status']and re.fullmatch('[0-9a-f]{64}',x['raw_response_sha256'])and x['raw_response_bytes']>0 and not x['full_web_body_archived']
gate(len({x['q']for x in load('web-general.json')['request']['search_query']})>=3,'three distinct general web queries')
gate('site:ncatlab.org/ncatlab'in load('ncatlab.json')['request']['search_query'][0]['q'],'distinct nCatLab namespace')
for x in [load('arxiv.json')]+[load('arxiv-retry.json')]:
 for q in x['request']['search_query']:assert 'after:2021-10-28'in q['q']and 'before:2026-10-29'in q['q']
gate(True,'five-year arXiv window and retry')
for n in ['source-search.json','tracked-source-search.json','inline-audit.json']:
 x=load(n);assert x['exit_code']==0 and not x['stderr']
e=load('overview-entry.json');keys=['type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']
gate(all(k in e for k in keys),'exact overview keys')
for k in keys:
 if k not in ['project_dependencies','caller_summary']:assert isinstance(e[k],str)and e[k].strip()
deps=e['project_dependencies'];canonical={x['name']for x in order}
gate(isinstance(deps,list)and len(deps)==len(set(deps))and set(deps)<=canonical and set(deps)==set(row['project_body_refs']+row['project_type_refs']),'canonical dependency list')
gate(all(n in e['how']for n in ['Θ_le_of_forall_index_le','index_le_lem6',"Finset.le_sup'",'mul_le_mul_of_nonneg_left']),'How names exact source stages')
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md'
manifest=load('copy-manifest.json');gate(manifest['completed']and manifest['declaration']==N,'current complete manifest')
for x in manifest['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
gate({p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in manifest['files']}|{'report.md'},'current artifact coverage')
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS COMPLETE FROZEN214 six native,17inputs,293audit,20search,all phases/currentmanifest')
