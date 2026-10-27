#!/usr/bin/env python3
"""Portable read-only declaration173 assessment validator, scratch or integrated."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_int_eq_of_gcd_eq_one'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=rd('assessment.json');V=rd('verification.json');O=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert A['declaration']==N and A['canonical_index']==173 and A['completed']
assert A['verdict']=='YES-but-generalise-first'and A['reason']=='MODERN-IDIOM'
assert A['allphases']=='PASS'and A['phases']==dict.fromkeys(ph,'PASS')
assert A['root_acceptance']in['pending','PASS']and not A['unresolved']and not V['unresolved']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert O['type']==rd('native-type.json')['type']
for t in ['{ι : Type','{s : Finset ι}','{u : ι → ℤ}','s.gcd u = 1','{v : ℚ}','∀ a ∈ s','∃ (z : ℤ)']:
 assert t in O['type']
assert not any(t in O['type']for t in ['Fintype','DecidableEq'])
M=rd('copy-manifest.json');assert M['declaration']==N
seen=set()
for x in M['files']:
 p=D/'report.md'if'/mathlibable/'in x['destination']else D/Path(x['destination']).name
 if not p.exists()and'/mathlibable/'in x['destination']:p=R/x['destination']
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 seen.add('report.md'if'/mathlibable/'in x['destination']else p.name)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms'])==allowed

def native(e):
 r=rd(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success']and not z.get('timed_out')
 s=(D/e['source']).read_text();assert sha(D/e['source'])==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and len(re.findall(r'^import ',s,re.M))==14
  ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('failed_dependencies')and not z.get('still_elaborating_lines')
  ds=z['items']
 assert not[x for x in ds if x.get('severity')in['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 return ds
assert len(V['accepted'])==3
for e in V['accepted']:native(e)
for e in V['rejected']:
 r=rd(e['receipt']);z=r['result']['structuredContent'];z=z.get('result',z)
 assert any(x.get('severity')in['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 assert e['source']not in{x['source']for x in V['accepted']}
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('baseline-hashes.json')
assert len(base)==len(fresh)==17 and set(base)==set(fresh)
for f,d in fresh.items():assert d['sha256']==d['expected']==base[f]['sha256']==sha(R/f)
for x in rd('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Separation.lean')==sha(D/'source-context.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-order.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[172]==rd('canonical-target.json')and order[172]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/V['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());h=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',h[1],h[2])if h else('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/V['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[V['audit']['start_line']-1:])==s.rstrip('\n')
ds=native(V['accepted'][0]);cons=[x['message'].split(': ',1)[1]for x in ds if x.get('line',0)>=147 and x['message'].startswith('INTEGRAL173_DIRECT_CONSUMER:')]
assert cons==O['caller_summary']['direct_kernel_value_consumers']==['_private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux']
lex=rd('lexical-enumeration.json');assert {x['path']for x in lex}=={x['file']for x in order}
for f in lex:
 assert sha(R/f['path'])==f['sha256']
 occ=[{'line':i,'text':l}for i,l in enumerate((R/f['path']).read_text().splitlines(),1)if'exists_int_eq_of_gcd_eq_one'in l]
 assert occ==f['occurrences']
assert sum(len(f['occurrences'])for f in lex)==2 and O['caller_summary']['explicit_use_count']==1
core=(D/'integral-combined-executed.lean.txt').read_text()
assert 'theorem gcd_smul_mem_all'in core and 'theorem of_isUnit_gcd'in core
assert '[AddCommMonoid M] [Module R M]'in core
assert '(hv : ∀ i ∈ s, u i • v ∈ N) : s.gcd u • v ∈ N'in core
assert 'N.mem_of_span_top_of_smul_mem s hs v hv'in core
assert 'fail_if_success exact?'not in core
caller=(D/V['accepted'][2]['source']).read_text()
assert 'gcd_smul_mem_all (LinearMap.range (Algebra.linearMap ℤ ℚ))'in caller
assert 'rw [hu, one_smul] at h'in caller
assert 'theorem nonunit_counterexample'in caller and 'theorem empty_guard'in caller
original=(D/'source-context.lean.txt').read_text().split('private lemma exists_int_polynomial_of_primitive_factor_aux',1)[1].split('omit [Fintype τ]',1)[0].strip()
replay=caller.split('theorem exists_int_polynomial_of_primitive_factor_aux',1)[1].split('#print axioms exists_int_polynomial_of_primitive_factor_aux',1)[0].strip()
assert replay==original.replace('exists_int_eq_of_gcd_eq_one hgcd','Integral173Strong.original hgcd')
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  r=rd(form+'-'+method+'.json');assert r['form']==form and r['method']==method and r['request']['query']
  assert not r['response'].get('isError',False)
 r=rd(form+'-rg.json');assert r['command'][0]=='rg'and r['exit_code']in[0,1]
for f in['callers-rg.json','callers-git-grep.json']:
 r=rd(f);assert r['exit_code']==0 and len(r['stdout'].splitlines())>=2
queries=[]
for i in range(5):
 w=rd(f'literature-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['status']and not w['body_archived']and w['urls']and w['titles']and w['summary']
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-27'in q and'before:2026-10-28'in q for q in queries)
groups=rd('accepted-grouping.json');assert {x['declaration']for x in groups}==set(O['action']['grouping'])
assert all(x['verdict'].startswith('YES')and x['acceptance']=='PASS'for x in groups)
assert O['action']['upstream_file']=='Mathlib/RingTheory/PrincipalIdealDomain.lean'
assert rd('reviewers.json')['exit_code']==0 and rd('reviewers.json')['reviewer_candidates']
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:173 full phases; fresh17; exact293; clean native; strongest generic/specialization/fullcaller/guards;15 search cells; exhaustive literature; current manifest/links.')
