#!/usr/bin/env python3
"""Read-only scratch/integrated assessment190 validation of the CURRENT copy manifest."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.Θ_le_of_forall_index_le'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==190 and a['completed']
assert a['allphases']=='PASS'and a['phases']==dict.fromkeys(ph,'PASS')
assert a['verdict']=='NO-mathlib-has-it'and a['root_acceptance']in ['pending','PASS']
assert not a['unresolved']and not v['unresolved']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']and'Fintype σ'in o['type']
assert 'DecidableEq'not in o['type']and 'Roth.Θ B q r ≤ c'in o['type']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/'in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==5 and len(v['rejected'])==1
assert {x['label']for x in v['accepted']}=={'original','project','isolated','callers-sharp','actual-guard'}
for e in v['accepted']:
 r=rd(e['receipt']);z=result(r);assert not r['result'].get('isError',False)
 assert z['success']and not z.get('timed_out');src=D/e['source'];s=src.read_text()
 assert sha(src)==e['source_sha256']and r['request']==e['original_execution_request']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not[x for x in ds if x.get('severity')in ['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
for e in v['rejected']:
 z=result(rd(e['receipt']));assert not z['success']and any(x.get('severity')=='error'for x in z['items'])
 assert e['source']not in{q['source']for q in v['accepted']}
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source']for x in fresh}
for x in fresh:assert x['matches_baseline']and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
assert sha(R/'Roth/Theta.lean')==sha(D/'Theta.lean.txt')
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path'];assert sha(p)==x['sha256']==sha(D/x['archive'])
 assert p.stat().st_size==x['bytes']
assert any(x['path']=='Mathlib/Algebra/Order/Archimedean/Real/Basic.lean' for x in rd('mathlib-inputs.json'))
assert 'protected lemma sSup_le' in (D/'mathlib-Mathlib-Algebra-Order-Archimedean-Real-Basic.lean.txt').read_text()
loc=rd('local-literature-input.json');assert sha(R/loc['source'])==loc['sha256']
assert rd('local-literature.json')['exit_code']==0
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[189]==rd('canonical-target.json')
assert order[189]['name']==N and order[189]['line']==124
assert set(o['project_dependencies'])<={x['name']for x in order}
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
 else('public',x['name'])for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert all(v['audit'][k]==293 for k in ['requested','unique','present','values'])
z=result(rd(v['audit']['receipt']))
for marker,ns in [('THETAUPPER190_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
 ('THETAUPPER190_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert[x['message'][len(marker):]for x in z['items']if x['message'].startswith(marker)]==ns
assert v['canonical_direct_consumers']==['Roth.Θ_unique_le','Roth.Θ_option_le']
assert not v['canonical_direct_type_consumers']
f=rd('formal-search.json');assert len(f)==13
assert {(x['form'],x['method'])for x in f if x['form']!='abstract-retry'}=={
 (fm,m)for fm in ['current','literature','abstract']for m in ['finder','loogle','leansearch','local_search']}
assert f[-1]['request']['query']=='Set.image2, "sSup"'and not f[-1]['response'].get('isError',False)
assert f[5]['response'].get('isError',False)
for fm in ['current','literature','abstract']:assert rd('rg-'+fm+'.json')['exit_code']in[0,1]
rg=rd('callers-rg.json');gg=rd('callers-git.json')
assert rg['exit_code']==gg['exit_code']==0
assert sorted(rg['stdout'].splitlines())==sorted(gg['stdout'].splitlines())
assert len(rg['stdout'].splitlines())==3
assert all(':'+str(i)+':'in rg['stdout']for i in[124,258,599])
cs=rd('callers.json');assert cs['call_occurrences']==cs['distinct_declarations']==2
for c in cs['callers']:assert c['reference']in(R/c['file']).read_text().splitlines()[c['line']-1]
qs=[]
for n in range(5):
 w=rd(f'web{n}-metadata.json');assert len(w['response_digest']['sha256'])==64
 assert w['response_digest']['bytes']>0 and w['status']and w['locators']and w['summary']
 qs.extend(x['q']for x in w['request'].get('search_query',[]))
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
 'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-27'in q for q in qs)
proj='\n'.join((D/'theta-upper190-project-executed.lean.txt').read_text().splitlines()[343:])
assert 'Roth.Θ B q r = sSup (Roth.indexSet B q r) := rfl'in proj
assert 'exact csSup_le (Roth.indexSet_nonempty hB q r)'in proj
assert 'Real.sSup_le'in proj
caller='\n'.join((D/'theta-upper190-callers-sharp-executed.lean.txt').read_text().splitlines()[373:])
assert N not in caller and 'caller_unique'in caller and 'caller_option'in caller
assert 'Lean.mkPrivateNameCore `Roth.Theta `Roth.index_unique_le_log_div'in caller
assert 'Roth.Θ B q r ≤ c ↔ 0 ≤ c'in caller
assert 'Roth.Θ_nonneg q'in caller and 'Real.sSup_le'in caller
actual='\n'.join((D/'theta-upper190-actual-guard-executed.lean.txt').read_text().splitlines()[418:])
assert 'Int.one_le_abs hd'in actual and '¬ Roth.Θ 0 q r ≤ (-1 : ℝ)'in actual
assert 'omit [Fintype σ] in'in actual
c=v['composition'];assert c['parent_reaim_checked']and c['bridge_definitional']
assert not c['strict_three_existing_call_term_verified']and not c['parent_project_lemma_counted_as_mathlib_block']
assert c['actual_caller_replays']==c['actual_call_occurrences']==2
assert c['no_circular_use_of_target_in_new_proof']and c['no_global_absence_claim']
p=D/'report.md'
if not p.exists():p=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=p.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
assert 'NO-mathlib-has-it'in s and 're-aim'in s and 'Five complete native evidence sets'in s
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS190: phases; fresh17; exact ordered293; 2value/0type; 5clean native; 1rejected excluded; formal15+retry; 2fullcallers; actualguard; currentmanifest/links/secrets.')
