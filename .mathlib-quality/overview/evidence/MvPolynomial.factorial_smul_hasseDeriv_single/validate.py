"""Portable read-only assessment validator; argument is repository root."""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
t='MvPolynomial.factorial_smul_hasseDeriv_single'
def read(n):return json.loads((b/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/f'{t}.md'
a=read('assessment.json')
assert a['declaration']==t and a['completed'] and a['root_acceptance'] in ['pending','PASS']
assert a['verdict']=='YES-add-as-is' and a['unresolved']==[] and not a['production_edits']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or v.startswith('N/A:') for v in a['phases'].values())
assert len(read('input-manifest.json')['sources_and_pins'])==17
for p,e in read('input-manifest.json')['sources_and_pins'].items():assert sha(r/p)==e['sha256'],p
for e in read('source-hashes.json'):
 raw=(r/e['path']).read_bytes();assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256'],e['path']
m=read('copy-manifest.json');entries=m['files']if isinstance(m,dict)else m
for e in entries:
 p=report if e['source']=='report.md' else b/e['source'];raw=p.read_bytes()
 assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256'],e['source']
v=read('verification.json');assert v['unresolved']==[]
naxioms=0
for e in v['accepted']:
 code=(b/e['source']).read_text();assert sha(b/e['source'])==e['source_sha256']
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 z=read(e['receipt']);native=z['result'];assert not native.get('isError',False)
 sc=native.get('structuredContent',native);out=sc.get('result',sc)
 assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
 ds=out.get('items',out.get('diagnostics',[]));assert not any(d.get('severity') in ['error','warning']for d in ds)
 if 'code'in z['request']:assert z['request']['code']==code
 else:
  c=read(e['source_check']);assert c['matched_at_freeze'] and c['disk_sha256']==c['retained_sha256']==e['source_sha256']
 for d in ds:
  msg=d.get('message','');assert 'sorryAx'not in msg
  if 'depends on axioms:'in msg:
   ns=re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',')
   assert {x.strip()for x in ns if x.strip()}<={'propext','Classical.choice','Quot.sound'};naxioms+=1
assert naxioms>=12
raw=(b/'raw-executed.lean.txt').read_text();disk=(b/'consumer-executed.lean.txt').read_text()
for s in ['#check_failure MvPolynomial.hasseDeriv','#check_failure MvPolynomial.factorial_smul_hasseDeriv_single','theorem independent_factorial','theorem recurrence','theorem univariate_from_recurrence','Polynomial.hasseDeriv_comp 1 m','#check_failure MvPolynomial.pderiv']:
 assert s in raw,s
assert 'import Roth'not in raw
for s in ['theorem replay','theorem natural_scalar','theorem function_shape','theorem bundled','theorem different_coordinate','theorem natural_factor_needed','theorem characteristic_two_guard','theorem from_recurrence']:
 assert s in disk,s
for method in ['finder','search','loogle','local']:
 for form in ['current','standard','abstract']:
  z=read(f'{method}-{form}.json');assert z['request'] and 'result'in z
for n in ['loogle-current-retry.json','loogle-abstract-final.json']:
 assert not read(n)['result'].get('isError',False)
assert read('full-name-source-search.json')['exit_code']==1
assert len({q[1] for x in read('web-requests.json') if isinstance(x['requests'],list)for q in x['requests']})>=3
for x in read('web-requests.json')+[read('web-open.json'),read('ncatlab-explicit.json')]:
 d=x['response_digest'];assert re.fullmatch('[a-f0-9]{64}',d['sha256']) and d['bytes']>0 and x['status']
assert 'ncatlab.org/ncatlab/'in json.dumps(read('ncatlab-explicit.json'))
assert read('q8-diagnostic.json')['fired'] and a['upstream']['group_with'] and a['upstream']['reviewer_candidates']
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http:','https:')):continue
 prefix=f'../evidence/{t}/'
 assert link.startswith(prefix),link
 assert (b/link[len(prefix):]).is_file(),link
print('PASS: all phases, current copy manifest, 17 inputs and source hashes, exact native proofs, standard axioms, search receipts, nine literature channels, Q8/callers and links')
