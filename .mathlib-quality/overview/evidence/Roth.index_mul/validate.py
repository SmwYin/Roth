#!/usr/bin/env python3
"""Portable read-only validator; current copy manifest governs scratch/integrated packages."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
NAME='Roth.index_mul'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] is True and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  ds=z['diagnostics'];assert r['request']['code']==s
  assert '#check_failure '+e['guard'] in s
  assert not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies')
  assert not z.get('still_elaborating_lines')
  ds=z['items'];assert r['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 return ds
A=read('assessment.json');assert A['declaration']==NAME and A['canonical_index']==144
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='BORDERLINE-needs-human'
assert not A['unresolved'] and A['root_acceptance'] in ['pending','PASS']
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(phases) and set(A['phases'].values())=={'PASS'}
assert 1<=len(A['questions'])<=5 and 'unverified' in A['broader_design']
O=read('overview-entry.json')
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert all(t in O['type'] for t in ['Roth.index_mul','σ : Type','Fintype','P Q : MvPolynomial σ ℝ','hP : P ≠ 0','hQ : Q ≠ 0','r : σ → ℕ','hr :'])
assert any('taylor_eq_zero_iff' in x for x in O['project_dependencies'])
manifest=read('copy-manifest.json');assert manifest['declaration']==NAME
seen=set()
for e in manifest['files']:
 if '/mathlibable/' in e['destination']:
  p=D/'report.md'
  if not p.exists():p=ROOT/e['destination']
 else:p=D/Path(e['destination']).name
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved']
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==10 and len(v['rejected'])==6
for e in v['accepted']:
 p=D/e['source'];assert sha(p)==e['source_sha256'];s=p.read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for m in e['required_info']:assert m in info,(e['label'],m)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['label']!='canonical-audit' and not e.get('signatures_only'):assert axs,e['label']
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for e in v['rejected']:assert (D/e['source']).is_file() and (D/e['receipt']).is_file() and e['reason']
assert not ({x['receipt'] for x in v['accepted']}&{x['receipt'] for x in v['rejected']})
inputs=read('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['expected_sha256'] for x in inputs)
base=read('input-manifest.json')['sources_and_pins'];assert set(base)=={x['path'] for x in inputs}
for x in inputs:assert base[x['path']]['sha256']==x['expected_sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[143]==read('canonical-target.json') and order[143]['name']==NAME
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+NAME in s
whole=(D/'index-mul-original-executed.lean.txt').read_text()
assert '\n'.join(whole.splitlines()[2402:])==s.rstrip('\n')
cs=read('callers.json');assert len(cs)==2 and sum(c['identifier_occurrences'] for c in cs)==2
for c in cs:
 assert sha(ROOT/c['file'])==c['source_sha256'] and c['source_fragment'] in (ROOT/c['file']).read_text() and c['plan']
 for line in c['reference_lines']:assert 'index_mul' in (ROOT/c['file']).read_text().splitlines()[line-1]
cons=read('direct-consumers.json');assert cons['consumers']==['Roth.index_prod','Roth.index_separated_mul_le_aux'] and cons['count']==2 and cons['second_is_private']
orig=next(e for e in v['accepted'] if e['label']=='canonical-audit');ds=native(orig)
new=[x for x in ds if x.get('line',0)>=v['audit']['native_region_start_line']]
actual=[x['message'].split(': ',1)[1] for x in new if x['message'].startswith('INDEX_MUL144_DIRECT_CONSUMER:')]
assert actual==['Roth.index_prod','_private.Roth.Theta.0.Roth.index_separated_mul_le_aux']
search=read('complete-caller-search.json');assert len(search['searches'])==2
assert all(e['exit_code']==0 and len(e['stdout'].splitlines())==4 for e in search['searches'])
assert {x['file'] for x in order}==set(search['canonical_source_inventory'])
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
occ=[(x['path'],c['line'],c['kind']) for x in lex['files'] for c in x['occurrences']]
assert occ==[('Roth/Index.lean',37,'docstring'),('Roth/Index.lean',162,'declaration'),('Roth/Index.lean',185,'proof-body application'),('Roth/Theta.lean',438,'proof-body application')]
assert lex['applications']==lex['proof_body_applications']==2 and lex['statement_applications']==0
s='\n'.join((D/v['target_source']).read_text().splitlines()[2721:])
assert all(t in s for t in ['theorem clearedWeight','theorem comparison','theorem replacement','max 1 (r i)','theorem zeroLeftGuard','theorem zeroRightGuard','IndexConsumers133.targetBridge','IndexWeightedScale143.scaledInfDegree'])
assert not re.search(r'\bindex_mul\b|\bindex_eq_weightedOrder_div\b',s)
replacement=s[s.index('theorem replacement'):s.index('theorem zeroLeftGuard')]
assert 'hr' not in replacement
s='\n'.join((D/v['caller_source']).read_text().splitlines()[2780:])
assert s.count('IndexMul144.replacement')==2 and '(_hr0 : ∀ j, 0 < r j)' in s
assert not re.search(r'\bindex_mul\b',s)
s='\n'.join((D/v['composition_source']).read_text().splitlines()[2838:])
assert 'fail_if_success\n    exact MvPowerSeries.weightedOrder_mul' in s
assert 'fail_if_success (solve | simp only [index, map_mul])' in s
for n in ['current','literature','abstract','inline','graded']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
formal=read('formal-search.json');assert len(formal)==3 and {e['form'] for e in formal}=={'current','literature','abstract'}
for row in formal:
 assert len(row['methods'])==4 and {e['method'] for e in row['methods']}=={'finder','loogle','leansearch','local'}
 for e in row['methods']:
  assert e['request']['query'] and 'response' in e
  if e['response'].get('isError'):assert (row['form'],e['method']) in [('abstract','leansearch'),('literature','finder')]
retry=read('search-abstract-leansearch-retry.json');assert retry['response'].get('isError') is False
assert 'MvPolynomial.IsWeightedHomogeneous.mul' in json.dumps(retry)
retry=read('search-literature-finder-retry.json');assert retry['response'].get('isError') is False
assert 'MvPowerSeries.weightedOrder_mul' in json.dumps(retry)
assert read('local-literature-search.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)>=10
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for target in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(target in q for q in queries)
assert len(set(q for q in queries if not q.startswith('site:')))>=3
for w in web:
 assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status']
 assert not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
assert (D/'clean-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:616])+'\n'
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
s=p.read_text()
for n in phases:assert '## Phase '+n in s
for needle in ['BORDERLINE-needs-human','**not a compiled weakening','minimum','supDegree_mul','injectiv','all nine','all proof-strategy','not a proof of absence','509']:assert needle in s,needle
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: complete phases/schema; current manifest hashes/bytes; native clean proofs/signatures; standard axioms; exact293 audit/order; fresh17 inputs; hr-free law/zero guards; both complete callers; explicit unverified broader design; actual methods and literature; portable links and credential scan')
