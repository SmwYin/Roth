#!/usr/bin/env python3
"""Read-only portable validator: scratch or integrated evidence, current manifest only."""
from pathlib import Path
import sys,json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.index_mul_left_weights'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] is True and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  ds=z['diagnostics'];assert r['request']['code']==s
  assert '#check_failure '+e['guard'] in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies') and not z.get('still_elaborating_lines')
  ds=z['items'];assert r['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 return ds
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==148
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='NO-mathlib-has-it'
assert not A['unresolved'] and A['root_acceptance'] in ['pending','PASS']
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(phases) and set(A['phases'].values())=={'PASS'}
O=read('overview-entry.json');assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert all(t in O['type'] for t in [N,'σ : Type','Fintype','P : MvPolynomial','α :','r :','l : ℕ'])
manifest=read('copy-manifest.json');assert manifest['declaration']==N;seen=set()
for e in manifest['files']:
 p=D/'report.md' if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 if not p.exists() and '/mathlibable/' in e['destination']:p=ROOT/e['destination']
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==7 and len(v['rejected'])==3
for e in v['accepted']:
 p=D/e['source'];assert sha(p)==e['source_sha256'];s=p.read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for m in e['required_info']:assert m in info,(e['label'],m)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['label']!='canonical-audit':assert axs,e['label']
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for e in v['rejected']:assert (D/e['source']).is_file() and (D/e['receipt']).is_file() and e['reason']
assert not ({x['receipt'] for x in v['accepted']}&{x['receipt'] for x in v['rejected']})
inputs=read('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['expected_sha256'] for x in inputs)
base=read('input-manifest.json')['sources_and_pins'];assert set(base)=={x['path'] for x in inputs}
for x in inputs:assert base[x['path']]['sha256']==x['expected_sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q),(p,q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[147]==read('canonical-target.json') and order[147]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t);terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/v['audit']['whole_source']).read_text();assert '\n'.join(whole.splitlines()[3996:])==s.rstrip('\n')
e=next(e for e in v['accepted'] if e['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=3998 and x['message'].startswith('INDEX_SCALE148_DIRECT_CONSUMER:')]
assert cons==['_private.Roth.Theta.0.Roth.index_separated_mul_le_aux']
assert read('direct-consumers.json')['consumers']==['Roth.index_separated_mul_le_aux']
assert len(read('callers.json'))==1 and read('callers.json')[0]['line']==447 and read('callers.json')[0]['applications']==2
search=read('complete-caller-search.json');assert len(search['searches'])==2 and all(e['exit_code']==0 and len(e['stdout'].splitlines())==2 for e in search['searches'])
assert {x['file'] for x in order}==set(search['canonical_source_inventory'])
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
occ=[(x['path'],c['line'],c['kind']) for x in lex['files'] for c in x['occurrences']];assert occ==[('Roth/Index.lean',200,'declaration'),('Roth/Theta.lean',447,'body')]
assert lex['applications']==lex['proof_body_applications']==2 and lex['source_reference_lines']==1 and lex['statement_applications']==0
s='\n'.join((D/v['target_source']).read_text().splitlines()[4352:]);assert not re.search(r'\bindex_mul_left_weights\b',s)
for t in ['theorem replacement','theorem zeroScale','theorem zeroPolynomial','fail_if_success rfl','open scoped Pointwise']:assert t in s,t
p=(ROOT/'Roth/Theta.lean').read_text();a=p.index('private lemma index_separated_mul_le_aux ');b=p.index('\nomit [DecidableEq τ] in',a)
caller=p[a:b].replace('private lemma index_separated_mul_le_aux ','theorem callerReplay ').replace('index_mul_left_weights','IndexScale148.replacement')
assert caller.strip() in s
b='\n'.join((D/v['bridge_source']).read_text().splitlines()[4424:]);assert 'IndexConsumers133.targetBridge' in b and 'IndexScaleMathlib148.scale' in b and 'weight_mul_left' in b and not re.search(r'\bindex_mul_left_weights\b',b)
g='\n'.join((D/v['guard_source']).read_text().splitlines()[4439:]);assert '[IsOrderedRing K]' in g and 'zeroFixingNecessary' in g and 'negativeScalingGuard' in g
m=(D/'index-scale-mathlib-clean-executed.lean.txt').read_text();assert 'map_finset_inf h f.coeff.support D' in m and '(h0 : φ 0 = 0)' in m and 'WithTop.map φ' in m
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
formal=read('formal-search.json');assert len(formal)==3 and {e['form'] for e in formal}=={'current','literature','abstract'}
for row in formal:
 assert len(row['methods'])==4 and {e['method'] for e in row['methods']}=={'finder','loogle','leansearch','local'}
 for e in row['methods']:assert e['request']['query'] and ('response' in e)
assert not read('search-literature-loogle-success.json')['response'].get('isError',False)
assert 'Real.sInf_smul_of_nonneg' in json.dumps(read('search-literature-loogle-success.json'))
assert 'map_finset_inf' in json.dumps(formal)
assert read('local-literature-search.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)==10
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for target in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(target in q for q in queries)
assert len(set(q for q in queries if not q.startswith('site:')))>=3
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['locators'] and not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
assert (D/'clean-index-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:642])+'\n'
t=read('warm-session-trim-after-index148.json');assert sha(D/t['archive'])==t['archive_sha256']=='67eecdb8061c7ee0a9d9be3dc8f6053a293f6a43953cc5246171667aafa5bb17'
assert sha(D/v['supporting_trim']['after'])==t['trimmed_sha256']
trim=dict(source=v['supporting_trim']['after'],receipt=v['supporting_trim']['receipt'],format='disk');native(trim)
# Confirm trim removes only whole obsolete diagnostic namespaces.
a=(D/t['archive']).read_text()
for ns in t['removed_audit_only_namespaces']:
 pattern=r'\nnamespace '+re.escape(ns)+r'\n.*?\nend '+re.escape(ns)+r'\n';a,n=re.subn(pattern,'\n',a,flags=re.S);assert n==1
assert a==(D/v['supporting_trim']['after']).read_text()
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text()
for n in phases:assert '## Phase '+n in s
for t in ['NO-mathlib-has-it','BORDERLINE','not definitional','no elision','All17','not a claim of a single mechanical edit','map_finset_inf','two proof applications','Salami']:assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: full phases; current manifest; clean native proofs; standard axioms; exact293 ordered canonical audit; fresh17 hashes; sole caller two-application full replay; one-call generic law and actual zero-preserving representation bridge; ordered-semiring scaling and counterguards; complete searches/literature; portable links; diagnostic-only trim; secret scan')
