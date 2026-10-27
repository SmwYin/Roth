#!/usr/bin/env python3
"""Portable read-only scratch/integrated validator; current manifest is authoritative."""
from pathlib import Path
import sys,json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.index_neg'
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
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==146
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='NO-mathlib-has-it'
assert not A['unresolved'] and A['root_acceptance'] in ['pending','PASS']
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(phases) and set(A['phases'].values())=={'PASS'}
O=read('overview-entry.json');assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert all(t in O['type'] for t in [N,'σ : Type','Fintype','P : MvPolynomial','α :','r :'])
manifest=read('copy-manifest.json');assert manifest['declaration']==N;seen=set()
for e in manifest['files']:
 p=D/'report.md' if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 if not p.exists() and '/mathlibable/' in e['destination']:p=ROOT/e['destination']
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==5 and len(v['rejected'])==1
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
assert order[145]==read('canonical-target.json') and order[145]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t);terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/'index-neg-original-executed.lean.txt').read_text();assert '\n'.join(whole.splitlines()[3261:])==s.rstrip('\n')
assert read('callers.json')==[] and read('direct-consumers.json')['consumers']==[]
e=next(e for e in v['accepted'] if e['label']=='canonical-audit');ds=native(e)
assert not [x for x in ds if x.get('line',0)>=3263 and x['message'].startswith('INDEX_NEG146_DIRECT_CONSUMER:')]
search=read('complete-caller-search.json');assert len(search['searches'])==2 and all(e['exit_code']==0 and len(e['stdout'].splitlines())==1 for e in search['searches'])
assert {x['file'] for x in order}==set(search['canonical_source_inventory'])
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
occ=[(x['path'],c['line'],c['kind']) for x in lex['files'] for c in x['occurrences']];assert occ==[('Roth/Index.lean',190,'declaration')]
assert lex['applications']==lex['proof_body_applications']==lex['statement_applications']==0
s='\n'.join((D/v['target_source']).read_text().splitlines()[3580:]);assert not re.search(r'\bindex_neg\b',s)
for t in ['IndexConsumers133.targetBridge','map_neg','AddMonoidAlgebra.supDegree_neg','OrderDual (WithTop ℝ)','simp only [index, map_neg, support_neg]','theorem zero']:assert t in s,t
s=(D/'index-neg-mathlib-clean-executed.lean.txt').read_text()
for t in ['[Ring R]','[SemilatticeInf T] [OrderTop T]','(D : A → T)','(B := OrderDual T)','#check_failure AddMonoidAlgebra.infDegree_neg']:assert t in s,t
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
formal=read('formal-search.json');assert len(formal)==3 and {e['form'] for e in formal}=={'current','literature','abstract'}
for row in formal:
 assert len(row['methods'])==4 and {e['method'] for e in row['methods']}=={'finder','loogle','leansearch','local'}
 for e in row['methods']:assert e['request']['query'] and not e['response'].get('isError',False)
assert 'AddMonoidAlgebra.supDegree_neg' in json.dumps(formal)
assert read('local-literature-search.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)==9
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for target in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(target in q for q in queries)
assert len(set(q for q in queries if not q.startswith('site:')))>=3
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
assert (D/'clean-index-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:642])+'\n'
assert (D/'clean-sign-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[819:829])+'\n'
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text()
for n in phases:assert '## Phase '+n in s
for t in ['NO-mathlib-has-it','BORDERLINE','OrderDual','not falsely counted as a three-existing-call','no elision','all17']:assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: full phases; current manifest; clean native proofs; standard axioms; exact293 ordered audit; fresh17 hashes; zero consumers; independent generic negation re-aim and projection; all searches/literature; portable links; secret scan')
