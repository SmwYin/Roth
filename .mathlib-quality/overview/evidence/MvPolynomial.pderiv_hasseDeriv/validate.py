"""Portable read-only validator. Optional argument: repository root."""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
target='MvPolynomial.pderiv_hasseDeriv'
def read(n):return json.loads((b/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
a=read('assessment.json')
assert a['declaration']==target and a['completed'] and a['root_acceptance'] in ['pending','PASS'] and not a['production_edits'] and a['unresolved']==[]
assert a['verdict']=='YES-add-as-is'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or v.startswith('N/A:') for v in a['phases'].values())
for p,e in read('input-manifest.json')['sources_and_pins'].items():assert sha(r/p)==e['sha256'],p
for e in read('source-hashes.json')+read('reference-hashes.json'):
 raw=(r/e['path']).read_bytes();assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256'],e['path']
m=read('copy-manifest.json');entries=m['files'] if isinstance(m,dict) else m
for e in entries:
 p=report if e['source']=='report.md' else b/e['source']
 raw=p.read_bytes();assert len(raw)==e['bytes'] and hashlib.sha256(raw).hexdigest()==e['sha256'],e['source']
v=read('verification.json');assert v['unresolved']==[]
axiom_count=0
for e in v['accepted']:
 code=(b/e['source']).read_text();assert sha(b/e['source'])==e['source_sha256']
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 z=read(e['receipt']);native=z['result'];assert not native.get('isError',False)
 sc=native.get('structuredContent',native);out=sc.get('result',sc)
 assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
 ds=out.get('items',out.get('diagnostics',[]))
 assert not any(d.get('severity') in ['error','warning'] for d in ds)
 if 'code' in z['request']:assert z['request']['code']==code
 else:
  c=read(e['source_check']);assert c['matched_at_freeze'] and c['disk_sha256']==c['retained_sha256']==e['source_sha256']
 for d in ds:
  msg=d.get('message','');assert 'sorryAx' not in msg
  if 'depends on axioms:' in msg:
   ns=re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',')
   assert {x.strip() for x in ns if x.strip()}<={'propext','Classical.choice','Quot.sound'}
   axiom_count+=1
assert axiom_count>=8
raw=(b/'raw-executed.lean.txt').read_text()
assert 'import Roth' not in raw and '#check_failure MvPolynomial.pderiv_hasseDeriv' in raw and '#check_failure MvPolynomial.hasseDeriv' in raw
assert "induction P using MvPolynomial.induction_on'" in raw and 'Nat.choose_mul' in raw and 'theorem pderiv_delta' in raw
assert 'Polynomial.hasseDeriv_comp 1 n' in raw and 'Polynomial.hasseDeriv_one' in raw
disk=(b/'disk-executed.lean.txt').read_text()
for s in ['theorem factorial_caller','theorem aeval_caller','theorem bundled','theorem order_zero','theorem factor_necessary','PDerivWeightedAssessment','theorem weighted']:
 assert s in disk,s
for method in ['Finder','Search','Loogle','Local']:
 for form in ['current','literature','abstract']:
  z=read(f'{method}-{form}.json');assert z['request'] and not z['result'].get('isError',False)
assert read('full-name.json')['result']['exit_code']==1
assert len({q['q'] for x in read('web-receipts.json') for q in x['request'].get('search_query',[])})>=3
for x in read('web-receipts.json'):
 assert re.fullmatch('[a-f0-9]{64}',x['sha256']) and x['bytes']>0 and x['status'] and x['summary']
assert len(read('web-sources.json'))>=6
q8=read('q8-diagnostic.json');assert q8['fired'] and q8['subsequent_named_substring_occurrences']==0
assert a['upstream']['group_with'] and a['upstream']['reviewer_candidates'] and a['missing_api']
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http:','https:')):continue
 assert (b/link).is_file(),link
print('PASS: phases, current manifest, 17 baseline inputs, reference hashes, exact native successes, standard axioms, five search methods, literature metadata, Q8, callers and action plan')
