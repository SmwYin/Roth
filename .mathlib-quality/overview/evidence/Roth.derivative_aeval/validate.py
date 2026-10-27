#!/usr/bin/env python3
"""Read-only portable assessment validation; validates current copy manifest."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.derivative_aeval'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(receipt):
 x=receipt['result']; assert not x.get('isError',False)
 x=x.get('structuredContent') or json.loads(x['content'][0]['text'])
 return x.get('result',x)
def report():
 return D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==112
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
assert a['verdict']=='YES-but-generalise-first'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
m=load('copy-manifest.json'); assert m['declaration']==N
for x in m['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],str(p)
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {Path(x['destination']).name for x in m['files']}|{'report.md'}
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
x=load('inputs.json');assert len(x)==17 and {y['path'] for y in x}==set(b['sources_and_pins'])
for y in x:
 assert y['match'] and y['sha256']==y['baseline_sha256']==b['sources_and_pins'][y['path']]['sha256']
for y in x+load('source-inputs.json'):
 p=R/y['path'];assert sha(p)==y['sha256'] and p.stat().st_size==y['bytes']
 if 'archive' in y:assert sha(D/y['archive'])==y['sha256']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==load('canonical-snapshot.json') and len(order)==293
assert len({x['name'] for x in order})==293 and order[111]==load('canonical-entry.json')
assert order[111]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
expected='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(expected)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[]
assert v['production_unchanged']
assert set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'}
assert {'original','audit','raw','finite-support','no-tower','consumer','specialization','kaehler'} <= {x['label'] for x in v['accepted']}
for x in v['accepted']:
 s=(D/x['source']).read_text();assert sha(D/x['source'])==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rec=load(x['receipt']);assert rec['request']==x['original_execution_request']
 nr=native(rec);assert nr['success'] and not nr.get('timed_out') and not nr.get('failed_dependencies') and not nr.get('partial',False)
 if x['execution_kind']=='persistent-disk':assert nr['partial'] is False
 ds=nr.get('items',nr.get('diagnostics',[]))
 assert not [z for z in ds if z.get('severity') in ['error','warning'] or z.get('category')=='sorry']
 txt='\n'.join(z.get('message','') for z in ds)
 assert not any(t in txt for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',txt):
  assert {t.strip() for t in ax.split(',') if t.strip()} <= set(v['standard_axioms'])
 fresh=[z for z in ds if z.get('line',0)>=x['native_region_start_line']]
 msg='\n'.join(z.get('message','') for z in fresh)
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if 'code' in rec['request']:
  assert rec['request']['code']==s
  assert not re.search(r'^import Roth\b',s,re.M)
 if x['label']=='original':assert '@'+N in msg and 'Field K' in msg
 if x['label']=='audit':
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert len(arrays)==1 and norm(arrays[0])==norm(expected)
  assert 'DERIVATIVE_AEVAL_AUDIT: requested=293; unique=293' in msg
  assert 'DERIVATIVE_AEVAL_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[z['message'].split(': ',1)[1] for z in fresh if z.get('message','').startswith('DERIVATIVE_AEVAL_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['_private.Roth.GenWronskian.0.Roth.derivative_kronHasse_aux']
 if x['label'] in ['raw','finite-support','no-tower']:
  assert '[CommSemiring R]' in s and '#check_failure Roth.derivative_aeval' in s
  assert 'theorem abstract' in s and '∑ j, aeval γ (pderiv j P) • D (γ j)' in s
 if x['label']=='no-tower':
  assert '[IsScalarTower R A M]' not in s and '∑ j ∈ P.vars' in s
 if x['label']=='consumer':assert 'Lean.mkPrivateNameCore `Roth.GenWronskian' in s
assert len(v['accepted']) == 8 and len(v['rejected']) == 6
for x in v['rejected']:
 assert (D/x['source']).is_file() and x['reason']
 rec=load(x['receipt']);assert rec['request']==x['original_execution_request']
 ds=native(rec).get('items',native(rec).get('diagnostics',[]))
 assert any(z.get('severity') in ['error','warning'] for z in ds)
for x in v.get('incomplete_native',[]):
 assert x['reason'] and native(load(x['receipt'])).get('partial') is True
f=load('formal-search-raw.json');assert len(f)==12
for method in ['finder','loogle','leansearch','local']:
 assert {x['key'].split('-')[1] for x in f if x['key'].startswith(method+'-')}=={'current','standard','abstract'}
 assert all('request' in x and 'response' in x for x in f if x['key'].startswith(method+'-'))
sr=load('source-search-raw.json')
assert {'rg-current','rg-standard','rg-abstract','callers','inline','full-names','recent-commits'} <= {x['label'] for x in sr}
assert all(x['returncode'] in [0,1] for x in sr)
w=load('web-receipts.json');assert len(w)>=5
assert len(w[0]['request']['search_query'])>=3
for x in w:assert len(x['response_sha256'])==64 and x['response_bytes']>0 and x['status']=='returned'
assert not any(re.search(r'(?i)(?:AWSAccessKeyId|Signature|x-amz-security-token)=',u) for x in w for u in x['urls'])
text=report().read_text()
for link in re.findall(r'\]\(([^)]+)\)',text):
 if link.startswith('../evidence/'+N+'/'):
  assert (D/link.split('/')[-1]).is_file(),link
 elif not link.startswith('https://'):raise AssertionError(link)
assert text.count('| 9 |')>=1 and 'NOT-COMPOSABLE' in text and 'SMALL' in text
assert 'YES-but-generalise-first' in text and 'map_mv_aeval' in text
entry=load('overview-entry.json');assert entry['type'].startswith('@'+N) and 'Field K' in entry['type']
print('PASS: derivative_aeval full phases, current manifest, hashes, exact293, native proofs, callers, literature and 5×3 searches')
