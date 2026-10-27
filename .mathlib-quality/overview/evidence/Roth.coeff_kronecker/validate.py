#!/usr/bin/env python3
"""Read-only scratch/integrated validator. Current copy-manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.coeff_kronecker'
def load(n): return json.loads((D/n).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values(): yield from nodes(v)
 elif isinstance(x,list):
  for v in x: yield from nodes(v)
def report():
 return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==109
assert a['verdict']=='BORDERLINE-needs-human' and a['completed'] and a['allphases']=='PASS'
assert a['unresolved']==[] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
assert len(a['questions'])==3 and a['parent_reaim']['replacement']=='MvPolynomial.aeval'
m=load('copy-manifest.json');assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
baseline=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
xs=load('inputs.json');assert len(xs)==17 and set(x['path'] for x in xs)==set(baseline['sources_and_pins'])
for x in xs:
 assert x['match'] and x['sha256']==x['baseline_sha256']==baseline['sources_and_pins'][x['path']]['sha256']
for x in xs+load('source-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 if 'archive' in x: assert sha(D/x['archive'])==x['sha256']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==load('canonical-snapshot.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[108]==load('canonical-entry.json') and order[108]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private': n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert {x['label'] for x in v['accepted']}=={'original','audit','raw','consumer','generalized','hom'}
assert set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'}
for x in v['accepted']+v['prerequisites']:
 s=(D/x['source']).read_text();assert sha(D/x['source'])==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 rs=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and 'success' in z]
 assert rs and all(z['success'] for z in rs)
 ds=[]
 for z in rs:
  assert not z.get('partial',False) and not z.get('timed_out',False) and not z.get('failed_dependencies')
  if x.get('execution_kind')=='persistent-disk': assert z.get('partial') is False
  ds.extend(z.get('items',z.get('diagnostics',[])))
 assert not [z for z in ds if z.get('severity') in ['error','warning'] or z.get('category')=='sorry']
 txt='\n'.join(z.get('message','') for z in ds)
 assert not any(t in txt for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',txt):
  assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 fresh=[z for z in ds if z.get('line',0)>=x.get('native_region_start_line',1)]
 msg='\n'.join(z.get('message','') for z in fresh)
 for n in x['expected_axiom_declarations']: assert "'"+n+"' depends on axioms:" in msg,n
 if 'code' in r['request']:
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
 if x.get('label') in ['raw','hom']:
  assert '#check_failure Roth.coeff_kronecker' in s
 if x.get('label')=='raw':
  assert '[CommSemiring R]' in s and 'P.coeff.mapDomain (Finsupp.weight w)' in s
  assert "Finsupp.mapDomain_apply' S P.coeff hP hi hd" in s
 if x.get('label')=='hom':
  assert 'apply MvPolynomial.algHom_ext' in s and 'simp only [AlgHom.comp_apply, MvPolynomial.aeval_X]' in s
 if x.get('label')=='original':
  assert '@Roth.coeff_kronecker' in msg and 'Field K' in msg and 'theorem Roth.coeff_kronecker' in msg
 if x.get('label')=='generalized':
  assert 'KroneckerExpInjOnNoBase.no_base e k' in s and '[CommSemiring R]' in s and '(hk :' not in s
 if x.get('label')=='consumer':
  assert '(coeff_replay hk hP' in s and '(coeff_kronecker' not in s
 if x.get('label')=='audit':
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert len(arrays)==1 and norm(arrays[0])==norm(array)
  assert 'COEFF_KRONECKER_AUDIT: requested=293; unique=293' in msg
  assert 'COEFF_KRONECKER_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[z['message'].split(': ',1)[1] for z in fresh if z.get('message','').startswith('COEFF_KRONECKER_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['Roth.kronecker_eq_zero_iff']
assert len(v['prerequisites'])==1 and v['prerequisites'][0]['declaration_index']==108
assert len(v['rejected'])==7
for x in v['rejected']:
 assert (D/x['source']).is_file() and (D/x['receipt']).is_file() and x['reason']
 rr=load(x['receipt']);assert any(z.get('severity') in ['error','warning'] for z in nodes(rr) if isinstance(z,dict))
 if '-absence-' in x['source']:
  assert 'exact?' in (D/x['source']).read_text()
  assert any('could not close' in z.get('message','') for z in nodes(rr) if isinstance(z,dict))
  assert not any(z.get('timed_out') for z in nodes(rr) if isinstance(z,dict))
f=load('formal-search.json')
for method in ['Finder','Loogle','LeanSearch','local']:
 rows=[x for x in f if x['method']==method];assert {x['form'] for x in rows}=={'current','standard','abstract'}
 assert all('response' in x and 'request' in x for x in rows)
retry=load('formal-search-retry.json');assert {x['form'] for x in retry}=={'current','standard','abstract'}
assert all(not x['response'].get('isError') for x in retry)
for form in ['current','standard','abstract','callers','inline','local-literature']:
 assert load('rg-'+form+'.json')['exit_code'] in [0,1]
queries=[]
for w in load('literature-search.json')+[load('literature-direct.json'),load('literature-recent.json')]:
 assert len(w['sha256'])==64 and w['bytes']>0 and w['status'] and w['summary']
 assert 'response' not in w and 'result' not in w
 assert all(len(z['title'])<=200 and '\n' not in z['title'] for z in w['locators'])
 queries += [z['q'] for z in w['request'].get('search_query',[])]
assert len(set(queries[:3]))==3
for domain in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(domain in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c=load('callers.json');assert c['named_count']==1 and c['callers']==['Roth.kronecker_eq_zero_iff'] and c['external_to_declaring_file']==0
o=load('overview-entry.json');assert o['type'].startswith('∀') and 'Field K' in o['type'] and '1 < k' in o['type']
assert all(x['verdict'].startswith('YES') for x in load('accepted-yes.json'))
assert any(x['declaration']=='Roth.kroneckerExp_injOn' for x in load('accepted-yes.json'))
assert load('reviewer-history.json')['exit_code']==0
s=report().read_text()
for t in ['## Phase 8','BORDERLINE-needs-human','SMALL','RESTATE-BEFORE-SHIP','293','MathOverflow','nCatLab','arXiv','mapDomain_apply','automatic NO parent gate']:
 assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'): continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
r=subprocess.run(['python3',str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert r.returncode==0,r.stdout+r.stderr
print('PASS: all phases;17 fresh inputs;6 native sources+new108 prerequisite;canonical293;sole caller;all searches/channels;current manifest;secret guard')
