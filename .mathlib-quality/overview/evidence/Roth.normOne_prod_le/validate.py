#!/usr/bin/env python3
"""Portable read-only declaration86 validator; current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.normOne_prod_le'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():
 return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==86 and a['completed']
assert a['allphases']=='PASS' and a['verdict']=='BORDERLINE-needs-human'
assert a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS']
phases={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(a['phases'])==phases
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem'))
 for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N and m['files']
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {
 Path(x['destination']).name for x in m['files']}|{'report.md'}
v=load('verification.json');assert v['unresolved']==[] and v['production_unchanged']
assert {x['label'] for x in v['accepted']}=={'original','raw','consumers','infrastructure'}
assert len(v['rejected'])==1
expected={
 'original':['Roth.normOne_prod_le','MvPolynomial.NormProdAssessment.replay'],
 'raw':['NormProdRaw.triangle','NormProdRaw.finiteTriangle','NormProdRaw.monomialSize',
        'NormProdRaw.genericMul','NormProdRaw.direct','NormProdRaw.genericProd',
        'NormProdRaw.directProd'],
 'consumers':['MvPolynomial.NormProdConsumers.normOne_det_le_inline'],
 'infrastructure':['MvPolynomial.NormProdInfrastructure.abstractProd']}
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert len(order)==293 and len({x['name'] for x in order})==293
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':
  n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
array='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(array)
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert all(len(l)<=100 for l in s.splitlines()),src
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|'
  r'set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 successes=[z for z in nodes(r['result'].get('structuredContent',r['result']))
  if isinstance(z,dict) and z.get('success') is True]
 assert successes
 messages=[]
 for z in successes:
  assert z.get('partial',False) is False and not z.get('timed_out',False)
  assert not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]))
  assert not [q for q in ds if q.get('severity') in ['error','warning']
   or q.get('category')=='sorry']
  msg='\n'.join(q.get('message','') for q in ds);messages.append(msg)
  assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg)
  if x['label']!='infrastructure':assert axs
  for ax in axs:
   assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 msg='\n'.join(messages)
 for name in expected[x['label']]:
  assert re.search("'"+re.escape(name)+r"' depends on axioms:",msg),name
 if x['label']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s
  assert not re.search(r'^import Roth\b',s,re.M)
  assert len(re.findall(r'^import ',s,re.M))==13
  for t in ['[CommSemiring R]','(hmul : ∀ a b, size (a * b) ≤ size a * size b)',
   'change (P.coeff + Q.coeff).sum','theorem genericMul','theorem direct']:
   assert t in s,t
 elif x['label']=='original':
  assert '#print '+N in s and 'theorem Roth.normOne_prod_le.' in msg
 elif x['label']=='consumers':
  arr=re.search(r'let names : Array Lean.Name := #\[.*?\]\n',s,re.S)
  assert arr and norm(arr.group())==norm(array)
  assert 'names.toList.eraseDups.length' in s and 'unique == 293' in s
  assert 'PROD_AUDIT_UNIQUE: 293' in msg
  assert 'PROD_AUDIT_CANONICAL: requested=293; present=293; values=293' in msg
  cs=re.findall(r'PROD_DIRECT_PROOF_CONSUMER: ([^\n]+)',msg)
  assert cs==['Roth.normOne_det_le'],cs
  assert 'PROD_AUDIT_NOT_LOADED:' not in msg
  assert 'normOne_prod_le' not in s[:s.index('run_cmd do')]
 elif x['label']=='infrastructure':
  for t in ['#check @Finset.norm_prod_le',
   "#check @Finset.norm_prod_le'",'#check @Finset.le_prod_of_submultiplicative_of_nonneg',
   '#check_failure (inferInstance : Norm (MvPolynomial σ ℤ))',
   '#check_failure (inferInstance : NormedCommRing (MvPolynomial σ ℤ))']:
   assert t in s,t
  assert '@Finset.norm_prod_le' in msg and 'NormOneClass' in msg
  assert 's.Nonempty' in msg
for x in v['rejected']:
 assert (D/x['source']).is_file() and (D/x['receipt']).is_file()
 assert x['reason'] and 'sorryAx' in json.dumps(load(x['receipt']))
inputs=load('inputs.json')
assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('mathlib-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256']
 assert p.stat().st_size==x['bytes']
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert load('input-hash-check.json')['all_pass']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
l=load('local-literature-source.json');p=R/l['path']
assert sha(p)==l['sha256'] and p.stat().st_size==l['bytes']
f=load('formal-search.json');assert len(f)==12
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 for form in ['current','standard','abstract']:
  ms=[x for x in f if x['method']==method and x['form']==form]
  assert len(ms)==1 and not ms[0]['result'].get('isError',False),(method,form)
  assert ms[0]==load(method+'-'+form+'.json')
for tag in ['current','literature','abstract','full-name','callers','inline','local-literature']:
 x=load('rg-'+tag+'.json')
 assert x['exit_code'] in [0,1] and x['command'][0]=='rg' and not x['stderr']
assert len(load('rg-callers.json')['stdout'].splitlines())==2
qs=[]
for i in range(7):
 w=load(f'web-{i}.json')
 assert len(w['response_sha256'])==64 and w['response_bytes_utf8']>0
 assert w['summaries'] and w['urls'] and not w['full_bodies_archived']
 assert 'response' not in w and 'result' not in w
 assert all('?' not in u for u in w['urls'])
 qs.extend(z['q'] for z in w['request'].get('search_query',[]))
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab',
 'site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(site in q for q in qs),site
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json')
assert c['named_count']==1 and c['occurrence_count']==1 and c['external_to_declaring_file']==0
assert c['native_audit']['unique']==293 and c['native_audit']['values']==293
assert c['native_audit']['status']=='PASS'
g=load('generality.json')
assert len(g['modern_rows'])==9 and len(g['strategy_rows'])==5
assert len(g['infrastructure_rows'])==6 and len(g['future_questions'])==2
assert all(x['verified'] and x['status'].startswith('PASS') for x in g['expanded_forms'])
assert load('canonical-entry.json')['name']==N
c=load('canonical-order.json')
assert c['index']==86 and c['total']==293 and c['entry']==order[85]
assert c['source_sha256']==sha(R/'.mathlib-quality/overview/declaration-order.json')
e=load('overview-entry.json');assert e['type'].startswith('∀') and e['declaration']==N
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action']:assert e[k]
s=report().read_text()
for phase in phases:assert 'Phase '+phase in s
for t in ['**SMALL**','BORDERLINE-needs-human','MAXIMALLY GENERAL','False-generalization',
 'no Mode B parent re-aim override','293','newly proved','NOT-COMPOSABLE']:
 assert t.lower() in s.lower(),t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,
 str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: declaration86 all phases,current manifest,17 inputs,4 clean native sets,'
 'exact293 unique canonical order,12 formal calls,all literature,links,secrets')
