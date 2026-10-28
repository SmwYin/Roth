#!/usr/bin/env python3
# coding: utf-8
"""Portable, read-only assessment193 validation; current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.Θ_equiv'
def rd(n): return json.loads((D/n).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==193 and a['completed']
assert a['allphases']=='PASS' and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='BORDERLINE-needs-human' and a['root_acceptance']in['pending','PASS']
assert not a['unresolved'] and not v['unresolved'] and 1<=len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type'] and 'Fintype σ'in o['type']
assert 'DecidableEq'not in o['type'] and 'Roth.Θ B (q ∘ ⇑e) (r ∘ ⇑e) = Roth.Θ B q r'in o['type']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==4 and len(v['rejected'])==1
assert {x['label']for x in v['accepted']}=={'original','project','isolated','callers'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(r);assert not r['result'].get('isError',False)
 assert z['success'] and not z.get('timed_out');src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256'] and r['request']==e['original_execution_request']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
  assert len(re.findall(r'^import ',s,re.M))==15
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not[x for x in ds if x.get('severity')in['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']or'LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
for e in v['rejected']:
 assert (D/e['source']).is_file() and (D/e['receipt']).is_file()
 assert not result(rd(e['receipt']))['success']
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline'] and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
loc=rd('local-literature-input.json');assert sha(R/loc['source'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0 and'2467 jobs'in(D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name']for x in order})==293 and order[192]==rd('canonical-target.json')
assert order[192]['name']==N and order[192]['line']==159
assert set(o['project_dependencies'])<={x['name']for x in order}
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
 else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in[('THETAEQUIV193_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
 ('THETAEQUIV193_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['_private.Roth.Theta.0.Roth.theta_lt_succ_aux']
assert not v['canonical_direct_type_consumers']
f=rd('formal-search.json');assert len(f)==12 and all(x['status']=='fulfilled'for x in f)
f=[x['value']for x in f]
assert {x['id']for x in f}=={m+'-'+fm for m in['finder','loogle','search','local']
 for fm in['current','standard','abstract']}
assert [x['id']for x in f if x['response'].get('isError',False)]==['loogle-standard']
assert not rd('loogle-standard-retry.json')['response'].get('isError',False)
assert 'Equiv.iSup_congr'in json.dumps(rd('loogle-standard-retry.json')['response'])
assert any('unavailable'in json.dumps(x['response'])for x in f if x['id']=='local-current')
for fm in['current','literature','abstract','transport']:assert rd('rg-'+fm+'.json')['exit_code']in[0,1]
assert len(rd('transport-search.json'))==2
rg=rd('callers-rg.json');gg=rd('callers-git.json')
assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
assert len(rg['stdout'].splitlines())==3
assert all(':'+str(i)+':'in rg['stdout']for i in[34,159,919])
cs=rd('callers.json');assert cs['call_occurrences']==cs['distinct_declarations']==1
for c in cs['callers']:assert c['reference']in(R/c['file']).read_text().splitlines()[c['line']-1]
inv=rd('source-inventory.json');assert inv['exit_code']==0
assert {x['file']for x in order}<=(set(inv['stdout'].splitlines())|{'Roth.lean'})
qs=[]
for w in rd('web-search.json'):
 assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status']=='fulfilled'
 assert w['locators'] and w['summary'];qs.extend(w['requests'])
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
 'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
wp=rd('web-primary.json');assert len(wp['response_sha256'])==64 and wp['response_bytes']>0
assert 'after:2021-10-27'in json.dumps(wp['request']) and '400'in wp['summary']
proj='\n'.join((D/'theta-equiv193-project-executed.lean.txt').read_text().splitlines()[343:])
assert N not in proj and 'lemma inclusion193'in proj and 'lemma fullBridge'in proj
assert 'Finsupp.mapDomain_surjective e.surjective d'in proj
assert 'degreeOf_rename_of_injective'in proj and 'coeff_rename_mapDomain'in proj
assert 'Roth.index_rename e.injective'in proj and 'hh (e.symm j)'in proj
assert 'inclusion193 e.symm B'in proj
caller='\n'.join((D/'theta-equiv193-callers-executed.lean.txt').read_text().splitlines()[382:])
assert N not in caller and 'Θ_equiv'not in caller and 'ThetaEquiv193.replay e.symm'in caller
assert 'lemma caller193'in caller and 'Θ_option_le'in caller
iso=(D/'theta-equiv193-isolated-executed.lean.txt').read_text()
assert 'congrArg sSup h'in iso and 'e.iSup_congr h'in iso and '[SupSet α]'in iso
c=v['composition'];assert c['parent_reaim_checked'] and not c['bridge_definitional']
assert c['full_arithmetic_family_bridge_verified'] and not c['strict_three_existing_call_term_verified']
assert not c['parent_project_lemma_counted_as_mathlib_block'] and c['actual_caller_replays']==1
assert c['no_circular_use_of_target_in_new_proof'] and c['no_global_absence_claim']
prior=rd('accepted-verdict-snapshot.json')['completed_declarations'];assert len(prior)==192
assert all(x['acceptance']=='PASS'for x in prior)
for n in['Roth.Θ','Roth.indexSet']:
 assert next(x['verdict']for x in prior if x['declaration']==n)=='NO-mathlib-has-it'
assert next(x['verdict']for x in prior if x['declaration']=='Roth.RSet')=='BORDERLINE-needs-human'
p=D/'report.md'
if not p.exists():p=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=p.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and(D/link[len(prefix):]).is_file(),link
assert 'BORDERLINE-needs-human'in s and 'parent re-aim'in s
assert 'Four complete clean native evidence sets'in s
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS193: all phases; fresh17; exact ordered293; 1value/0type; four clean native sets; full arithmetic bridge/caller; formal15+retry; currentmanifest/links/secrets.')
