"""Portable read-only validator: python3 validate.py [repository root].
Uses the CURRENT copy-manifest.json, never historical worker-copy-manifest.json.
"""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent;r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd();target='MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero';prefix='../evidence/'+target+'/'
def read(n):return json.loads((b/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/f'{target}.md'
def linkpath(x):return b/x[len(prefix):] if (b/'report.md').is_file() and x.startswith(prefix) else report.parent/x
a=read('assessment.json');assert a['declaration']==target and a['line']==243 and a['completed'] and a['root_acceptance'] in ['pending','PASS'] and not a['production_edits'] and a['unresolved']==[] and a['verdict']=='YES-add-as-is'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and all(v=='PASS' or v.startswith('N/A:') for v in a['phases'].values())
m0=read('input-manifest.json')['sources_and_pins'];assert len(m0)==17
for p,e in m0.items():assert sha(r/p)==e['sha256'],p
fresh=read('baseline-fresh-check.json');assert len(fresh)==17 and all(x['expected']==x['observed'] for x in fresh);assert 'Exit code: 0' in (b/'baseline-build.txt').read_text()
for e in read('source-hashes.json')+read('reference-hashes.json'):
 p=pathlib.Path(e['path']);p=p if p.is_absolute() else r/p;assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],e['path']
m=read('copy-manifest.json');entries=m['files'] if isinstance(m,dict) else m
assert entries and len({e['source'] for e in entries})==len(entries)
for e in entries:
 p=report if e['source']=='report.md' else b/e['source'];assert p.is_file();assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256'],e['source']
v=read('verification.json');assert v['unresolved']==[] and len(v['accepted'])==2
axiom_names=set()
for e in v['accepted']:
 code=(b/e['source']).read_text();assert sha(b/e['source'])==e['source_sha256'];assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 z=read(e['receipt']);native=z['result'];assert not native.get('isError',False);sc=native.get('structuredContent',native);out=sc.get('result',sc)
 assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
 ds=out.get('items',out.get('diagnostics',[]));assert not any(d.get('severity') in ['error','warning'] for d in ds)
 if 'code' in z['request']:assert z['request']['code']==code
 else:
  c=read(e['source_check']);assert c['matched_at_freeze'] and c['disk_sha256']==c['retained_sha256']==e['source_sha256']
 for d in ds:
  msg=d.get('message','');assert 'sorryAx' not in msg
  if 'depends on axioms:' in msg:
   ns={x.strip() for x in re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',') if x.strip()};assert ns<={'propext','Classical.choice','Quot.sound'};axiom_names.add(msg.split("'")[1])
for n in ['MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero','PrivateMonomialFactorAssessment.replay','HasseSeparatedFactorAssessment.replay','HasseSeparatedFactorExtra.vars_iff','HasseSeparatedFactorExtra.right_factor','HasseSeparatedFactorExtra.ordinary_derivative_guard','HasseSeparatedGeneric.sum_extension','HasseSeparatedTopComponentGuard.insufficient','HasseSeparatedCallers.none_block','HasseSeparatedCallers.some_block','CoeffAssessment.independent','RawHasseSeparated.monomial_delta','RawHasseSeparated.monomial_mul','RawHasseSeparated.separated']:assert n in axiom_names,n
raw=(b/'raw-executed.lean.txt').read_text();assert 'import Roth' not in raw
for s in ['#check_failure MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero','#check_failure MvPolynomial.hasseDeriv','#check_failure MvPolynomial σ S','#check @LinearMap.map_algebraMap_mul','#check @LinearMap.map_mul_algebraMap','noncomputable def delta','theorem monomial_mul','theorem separated',"induction g using MvPolynomial.induction_on'"] :assert s in raw,s
disk=(b/'disk-executed.lean.txt').read_text()
for s in ['theorem vars_iff','theorem right_factor','theorem ordinary_derivative_guard','theorem sum_extension','theorem none_block','theorem some_block','#check @Polynomial.hasseDeriv_mul','#check @LinearMap.map_smul','#check @MvPolynomial.linearMap_ext','(h : ∀ a ∈ f.support, T (monomial a (f.coeff a) * g) = monomial a (f.coeff a) * T g)']:assert s in disk,s
search=read('search-raw.json');assert len(search)==6 and {x['method'] for x in search}=={'lean_leanfinder','lean_leansearch'} and len({x['request']['query'] for x in search})==3 and all(not x['result'].get('isError',False) for x in search)
assert len(read('loogle-raw.json'))==3 and all(not x['result'].get('isError',False) for x in read('loogle-raw.json'))
assert len(read('local-raw.json'))==3 and all(not x['result'].get('isError',False) for x in read('local-raw.json'))
for n in ['full-name.json','rg-current.json','rg-literature.json','rg-abstract.json','callers.json','inline-audit.json','reviewer-commits.json','literature-local.json']:
 z=read(n);assert z['request'] and z['result']['exit_code'] in [0,1]
assert read('full-name.json')['result']['exit_code']==1
refs=read('callers.json')['result']['stdout'];assert len(refs.splitlines())==3 and all(s in refs for s in ['Roth/Separation.lean:157','Roth/Separation.lean:161','Roth/HasseDeriv.lean:243'])
web=read('web-receipts.json');assert len({q['q'] for x in web for q in x['request'].get('search_query',[])})>=10
for x in web:assert re.fullmatch('[a-f0-9]{64}',x['sha256']) and x['bytes']>0 and x['status'] and x['summary']
assert len(read('web-sources.json'))>=9
q8=read('q8-diagnostic.json');assert q8['fired'] and q8['named_substring_lines']==1 and q8['exact_identifier_occurrences']==0
progress=read('assessment.json')['upstream']['group_with'];assert progress and 'MvPolynomial.hasseDeriv_monomial' not in progress
assert a['upstream']['reviewer_candidates'] and a['missing_api']
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http:','https:')):continue
 assert link.startswith(prefix),link;assert linkpath(link).is_file(),link
assert read('overview-entry.json')['caller_summary']['count']==2
print('PASS: all phases; current manifest hashes/bytes; 17 unchanged baseline inputs; exact native complete successes/standard axioms; five methods x three forms; nine literature channels; Q8; two explicit caller fragments; actionable upstream plan.')
