"""Read-only validation in scratch or integrated layout; current copy manifest only."""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
t='MvPolynomial.hasseDeriv_single_aeval_X'
def read(n):return json.loads((b/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/(t+'.md')
a=read('assessment.json');assert a['declaration']==t and a['line']==253 and a['completed'] and a['root_acceptance'] in ['pending','PASS']
assert a['verdict']=='BORDERLINE-needs-human' and a['unresolved']==[] and not a['production_edits'] and a['pins_unchanged']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS' or x.startswith('N/A:') for x in a['phases'].values())
assert 1<=len(a['questions'])<=5 and a['explicit_callers']==1
m=read('input-manifest.json')['sources_and_pins'];assert len(m)==17
for p,e in m.items():assert sha(r/p)==e['sha256'],p
fresh=read('input-check.json');assert len(fresh)==17 and all(x['match'] and x['expected']==x['actual'] for x in fresh)
assert 'Exit code: 0' in (b/'baseline-build.txt').read_text()
for e in read('source-hashes.json'):
 p=r/e['path'];assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],e['path']
manifest=read('copy-manifest.json');es=manifest['files'] if isinstance(manifest,dict) else manifest
assert es and len({x['source'] for x in es})==len(es)
for e in es:
 p=report if e['source']=='report.md' else b/e['source'];assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],e['source']
v=read('verification.json');assert len(v['accepted'])==3 and v['unresolved']==[] and v['root_native_complete']
names=set()
for e in v['accepted']:
 code=(b/e['source']).read_text();assert sha(b/e['source'])==e['source_sha256']
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 z=read(e['receipt']);res=z['result'];assert not res.get('isError',False)
 sc=res.get('structuredContent',res);out=sc.get('result',sc)
 assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
 ds=out.get('items',out.get('diagnostics',[]));assert not any(d.get('severity') in ['error','warning'] for d in ds)
 if 'code' in z['request']:assert code==z['request']['code']
 else:
  c=read(e['source_check']);assert c['matched_at_freeze'] and c['disk_sha256']==c['retained_sha256']==e['source_sha256']
 for d in ds:
  msg=d.get('message','');assert 'sorryAx' not in msg
  if 'depends on axioms:' in msg:
   ns={x.strip() for x in re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',') if x.strip()}
   assert ns<={'propext','Classical.choice','Quot.sound'};names.add(msg.split("'")[1])
for n in ['MvPolynomial.hasseDeriv_single_aeval_X','HasseSingleAevalAssessment.replay','HasseSingleAevalAssessment.linear_square','HasseSingleAevalAssessment.option_none_caller','RawHasseSingleAeval.replay','RawHasseSingleDirect.linear_square']:assert n in names,n
minimal=(b/'minimal-executed.lean.txt').read_text();assert 'import Roth' not in minimal and 'theorem independent' not in minimal and 'monomial_delta' not in minimal and 'induction' not in minimal
for s in ["apply Polynomial.lhom_ext'",'apply LinearMap.ext','CoeffAssessment.delta, Polynomial.hasseDeriv','#check_failure MvPolynomial.hasseDeriv_single_aeval_X']:assert s in minimal,s
raw=(b/'raw-executed.lean.txt').read_text();assert 'import Roth' not in raw and '#check_failure MvPolynomial σ S' in raw
search=read('formal-search.json');assert len(search)==12
for form in ['current','literature','abstract']:
 rows=[x['value'] for x in search if x['status']=='fulfilled' and x['value']['form']==form]
 assert {x['method'] for x in rows}=={'Finder','LeanSearch','Loogle','local'}
rg=read('source-search.json');assert {'current','literature','abstract'}<={x['form'] for x in rg}
web=read('web-receipts.json');assert len(web)>=5
for x in web:assert re.fullmatch('[a-f0-9]{64}',x['response_sha256']) and x['response_bytes']>0 and x['status']
q=read('q8-diagnostic.json');assert q['fired'] and q['named_substring_lines']==1 and q['exact_identifier_X_j_occurrences']==0
prefix='../evidence/'+t+'/'
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http:','https:')):continue
 assert link.startswith(prefix),link
 p=b/link[len(prefix):] if (b/'report.md').is_file() else report.parent/link
 assert p.is_file(),link
assert read('overview-entry.json')['caller_summary']['count']==1
assert 'Pending final' not in report.read_text()
print('PASS: phases, current manifest, 17 baseline inputs, source hashes, 3 complete native receipts, standard axioms, five methods x three forms, literature channels, Q8, caller and Phase6b verdict.')
