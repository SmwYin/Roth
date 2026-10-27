#!/usr/bin/env python3
"""Read-only scratch/integrated validator; current copy-manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
NAME='Roth.le_index_sum'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] is True and not z.get('timed_out')
 if e['format']=='raw':
  ds=z['diagnostics'];s=(D/e['source']).read_text();assert r['request']['code']==s
  assert '#check_failure '+e['guard'] in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies')
  assert not z.get('still_elaborating_lines');ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 return ds
assert D.is_dir()
a=read('assessment.json');assert a['declaration']==NAME and a['canonical_index']==141
assert a['completed'] and a['allphases']=='PASS' and a['verdict']=='NO-mathlib-has-it'
assert not a['unresolved'] and a['root_acceptance'] in ['pending','PASS']
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(a['phases'])==set(phases) and all(x=='PASS' for x in a['phases'].values())
e=read('overview-entry.json')
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(e)
assert all(t in e['type'] for t in ['∀ {σ : Type','Fintype','MvPolynomial','σ → ℕ','∑ i ∈ s, f i ≠ 0','c ≤ Roth.index'])
assert {'Roth.index','Roth.le_index_iff','MvPolynomial.hasseDeriv'}<=set(e['project_dependencies'])
seen=set()
for e in read('copy-manifest.json')['files']:
 if '/mathlibable/' in e['destination']:
  p=D/'report.md'
  if not p.exists():p=ROOT/e['destination']
 else:p=D/Path(e['destination']).name
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
actual={p.name for p in D.iterdir() if p.is_file()}
assert actual-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==9
for e in v['accepted']:
 p=D/e['source'];assert sha(p)==e['source_sha256'];s=p.read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for m in e['required_info']:assert m in info,(e['label'],m)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info);assert axs,e['label']
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
assert len(v['rejected'])==5
for e in v['rejected']:assert (D/e['source']).is_file() and (D/e['receipt']).is_file() and e['reason']
assert not ({x['receipt'] for x in v['accepted']}&{x['receipt'] for x in v['rejected']})
inputs=read('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['expected_sha256'] for x in inputs)
baseline=read('input-manifest.json')['sources_and_pins']
assert set(baseline)=={x['path'] for x in inputs}
for x in inputs:
 assert baseline[x['path']]['sha256']==x['expected_sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
assert read('input-hash-check.json')=={'all_pass':True,'count':17}
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293
assert 'let target := `'+NAME in s
cs=read('callers.json');assert len(cs)==1 and sum(c['identifier_occurrences'] for c in cs)==1
for c in cs:
 assert sha(ROOT/c['file'])==c['source_sha256'] and c['source_fragment'] in (ROOT/c['file']).read_text() and c['plan']
 for line in c['reference_lines']:assert NAME.split('.')[-1] in (ROOT/c['file']).read_text().splitlines()[line-1]
cons=read('direct-consumers.json');assert cons['count']==1
search=read('complete-caller-search.json');assert len(search['searches'])==2
assert all(e['exit_code']==0 and len(e['stdout'].splitlines())==3 for e in search['searches'])
assert {x['file'] for x in order}<=set(search['canonical_source_inventory'])
lex=read('lexical-enumeration.json')
assert {x['path'] for x in lex['files']}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
assert lex['applications']==lex['proof_body_applications']==1 and lex['statement_applications']==0
assert [(x['file'],x['line'],x['kind']) for x in lex['occurrences']]==[('Roth/Index.lean',118,'declaration'),('Roth/Theta.lean',398,'proof-body application')]
orig=next(e for e in v['accepted'] if e['label']=='original-and-audit');ds=native(orig)
new=[x for x in ds if x.get('line',0)>=v['audit']['native_region_start_line']]
actualcons=[x['message'].split(': ',1)[1] for x in new if x['message'].startswith('LE_INDEX_SUM141_DIRECT_CONSUMER:')]
assert actualcons==cons['consumers']
s=(D/v['caller_source']).read_text();assert not re.search(r'\ble_index_sum\b',s)
assert s.count('IndexSumTarget141.replacement')==1
for c in cs:assert c['source_fragment'].replace('le_index_sum','IndexSumTarget141.replacement') in s
isolated=(D/'le-index-sum-mathlib-final-executed.lean.txt').read_text()
assert 'AddMonoidAlgebra.supDegree_sum_le (B := OrderDual T)' in isolated
assert '(Finset.le_inf_iff.mpr hf).trans (finiteInfLaw D s f)' in isolated
formal=read('formal-search.json');assert len(formal)==3 and {e['form'] for e in formal}=={'current','literature','abstract'}
for row in formal:
 assert len(row['methods'])==4
 assert {e['method'] for e in row['methods']}=={'lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search'}
 for e in row['methods']:
  assert e['response']['status']=='fulfilled' and e['response']['value'].get('isError') is False
  assert e['request']['query']
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code']==0
assert read('local-literature-search.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web-*-metadata.json')];assert len(web)==5
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
assert len({q['q'] for q in read('web-0-metadata.json')['request']['search_query']})>=3
for target in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org/abs/ ']:assert any(target in q for q in queries)
for w in web:
 assert len(w['response']['sha256'])==64 and w['response']['bytes']>0 and w['response']['status']
 assert w['titles'] and not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
s=(D/'clean-excerpt.tex.txt').read_text();assert s=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:618])+'\n'
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
s=p.read_text();assert '## Phase 8' in s and a['verdict'] in s
for marker in ['## Phase '+n for n in ['0','1','2','3','4a','4c','4.5','4.6','5','5.5','6.0','6','7','8']]:assert marker in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: phases/schema, current manifest, nine accepted native sources, standard axioms, exact293 canonical order, fresh17 input hashes, sole full caller replay, five-method/three-form formal search, literature channels, portable links and credential guard')
