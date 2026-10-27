#!/usr/bin/env python3
"""Portable read-only scratch/integrated assessment validator."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_hasseDeriv_kronecker_eq_sum'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(rec):
 x=rec['result'];assert not x.get('isError',False)
 x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
rp=D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json')
assert a['declaration']==N and a['canonical_index']==116 and a['completed']
assert a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged']
assert a['root_acceptance'] in ['pending','PASS'] and a['verdict']=='BORDERLINE-needs-human'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
assert len(a['future_api_questions'])==3 and a['composition']=='NOT-COMPOSABLE'
m=load('copy-manifest.json');assert m['declaration']==N
for f in m['files']:
 p=rp if '/mathlibable/' in f['destination'] else D/Path(f['destination']).name
 assert p.is_file() and sha(p)==f['sha256'] and p.stat().st_size==f['bytes'],str(p)
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {Path(f['destination']).name for f in m['files']}|{'report.md'}
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
ins=load('inputs.json');assert len(ins)==17 and {x['path'] for x in ins}==set(b['sources_and_pins'])
for x in ins:
 assert x['match'] and x['sha256']==x['baseline_sha256']==b['sources_and_pins'][x['path']]['sha256']
for x in ins+load('source-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if 'archive' in x:assert sha(D/x['archive'])==x['sha256']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==load('canonical-snapshot.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[115]==load('canonical-entry.json') and order[115]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
expected='let names : Array Lean.Name := #['+','.join(names)+']'
norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(expected)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'}
required={'original','audit','finite-gamma','consumer','rational-clean','semiring','semiring-consumer-clean','extraction','span-candidates','semiring-first-order-prerequisite'}
assert {x['label'] for x in v['accepted']}==required
for x in v['accepted']:
 s=(D/x['source']).read_text();assert sha(D/x['source'])==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rec=load(x['receipt']);assert rec['request']==x['original_execution_request']
 nr=native(rec);assert nr['success'] and not nr.get('timed_out') and not nr.get('failed_dependencies') and not nr.get('partial',False)
 if x['execution_kind']=='persistent-disk':assert nr['partial'] is False
 ds=nr.get('items',nr.get('diagnostics',[]))
 assert not [y for y in ds if y.get('severity') in ['error','warning'] or y.get('category')=='sorry']
 txt='\n'.join(y.get('message','') for y in ds)
 assert not any(t in txt for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',txt):
  assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 fresh=[y for y in ds if y.get('line',0)>=x['native_region_start_line']]
 msg='\n'.join(y.get('message','') for y in fresh)
 for n in x['expected_axiom_declarations']:assert "'"+n+"' depends on axioms:" in msg,n
 if 'code' in rec['request']:
  assert rec['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
 if x['label']=='original':assert N+'.' in msg and '[Field K]' in msg and '[CharZero K]' in msg
 if x['label']=='audit':
  arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S)
  assert len(arrays)==1 and norm(arrays[0])==norm(expected)
  assert 'EXISTS_HASSE_KRONECKER_AUDIT: requested=293; unique=293' in msg
  assert 'EXISTS_HASSE_KRONECKER_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[y['message'].split(': ',1)[1] for y in fresh if y.get('message','').startswith('EXISTS_HASSE_KRONECKER_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['Roth.exists_genWronskian_ne_zero']
 if x['label']=='semiring':
  assert '[CommSemiring R]' in s and '[Algebra ℚ R]' in s and '[Finite σ]' in s
  assert '[Field R]' not in s and '[CharZero R]' not in s
  assert 'restrictScalars ℚ' in s and 'DerivativeAEvalNoTower.semiring' in s
  assert "'ExistsHasseSemiringProbe.exists_hasseDeriv_aeval_eq_sum' depends on axioms:" in msg
 if x['label']=='semiring-consumer-clean':
  assert 'ExistsHasseSemiringProbe.exists_hasseDeriv_aeval_eq_sum' in s
  assert 'Lean.mkPrivateNameCore `Roth.GenWronskian' in s and '(R := K)' in s
  assert "'Roth.ExistsHasseSemiringConsumer.caller_replay' depends on axioms:" in msg
 if x['label']=='extraction':
  assert '#check_failure Roth.exists_hasseDeriv_kronecker_eq_sum' in s
  assert 'hF : F ∈ Submodule.span A' in s and '[CommSemiring A]' in s
  assert '@Polynomial.hasseDeriv_comp' in msg and '@Finsupp.mem_span_image_iff_linearCombination' in msg
 if x['label']=='span-candidates':
  assert '@Submodule.mem_span_image_iff_exists_fun' in msg
  assert "@Submodule.mem_span_image_finset_iff_exists_fun'" in msg
assert len(v['rejected'])==3
for x in v['rejected']:
 assert (D/x['source']).is_file() and x['reason']
 rec=load(x['receipt']);assert rec['request']==x['original_execution_request']
 nr=native(rec);ds=nr.get('items',nr.get('diagnostics',[]))
 assert any(y.get('severity') in ['error','warning'] for y in ds)
f=load('formal-search-raw.json');assert len(f)==14
for method in ['finder','loogle','leansearch','local']:
 assert {x['key'].split('-')[1] for x in f if x['key'].startswith(method+'-')}=={'current','standard','abstract'}
 assert all('request' in x and 'response' in x for x in f if x['key'].startswith(method+'-'))
assert any(x['key']=='loogle-standard-valid' and not x['response'].get('isError') for x in f)
sr=load('source-search-raw.json')
assert {'rg-current','rg-standard','rg-abstract','full-names','callers','inline','recent-commits'}<={x['label'] for x in sr}
assert all(x['returncode'] in [0,1] for x in sr)
w=load('web-receipts.json');assert len(w)==6 and len(w[0]['request']['search_query'])>=3
for x in w:
 assert len(x['response_sha256'])==64 and x['response_bytes']>0 and x['status']=='returned'
 for u in x['urls']:assert not re.search(r'(?i)(?:AWSAccessKeyId|Signature|x-amz-security-token)=',u)
text=rp.read_text()
for link in re.findall(r'\]\(([^)]+)\)',text):
 if link.startswith('../evidence/'+N+'/'):assert (D/link.split('/')[-1]).is_file(),link
 elif not link.startswith('https://'):raise AssertionError(link)
for token in ['SMALL','| 9 |','NOT-COMPOSABLE','RESTATE-BEFORE-SHIP','STRICTLY NARROWER THAN STANDARD','Lemma 5.5','Submodule.mem_span_image_iff_exists_fun']:
 assert token in text,token
assert len(re.findall(r'^\d\. Should|^\d\. If a rational',text,re.M))==3
e=load('overview-entry.json');assert e['type'].startswith('@'+N) and '∀' in e['type'] and '[Field K]' in e['type'] and '[CharZero K]' in e['type']
scan=load('secrets-scan.json')
assert scan['returncode']==0 and scan['stdout'].startswith('PASS: targeted credential/signed-URL scan')
assert scan['script_sha256']==sha(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py')
print('PASS: current manifest, full phases, 17 pins, exact293 order, ten accepted native experiments, three rejected drafts, searches and literature')
