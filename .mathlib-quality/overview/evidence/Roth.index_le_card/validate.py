#!/usr/bin/env python3
"""Read-only portable validator: current manifest, canonical audit, exact native evidence."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.index_le_card'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return ' '.join(s.split())
def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z);assert z['success'] and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  ds=z['diagnostics'];assert r['request']['code']==s
  assert '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies') and not z.get('still_elaborating_lines')
  assert r['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean';ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 return ds
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==150
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='BORDERLINE-needs-human'
assert A['root_acceptance'] in ['pending','PASS'] and not A['unresolved']
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'];assert set(A['phases'])==set(ph) and set(A['phases'].values())=={'PASS'}
O=read('overview-entry.json');assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
for t in [N,'σ : Type','P ≠ 0','Fintype','degreeOf','Fintype.card']:assert t in O['type']
m=read('copy-manifest.json');assert m['declaration']==N;seen=set()
for e in m['files']:
 p=D/'report.md' if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 if not p.exists() and '/mathlibable/' in e['destination']:p=ROOT/e['destination']
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','overview-entry.json','verification.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert len(v['accepted'])==6 and len(v['rejected'])==2 and not v['unresolved']
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
for e in v['accepted']:
 assert sha(D/e['source'])==e['source_sha256'];s=(D/e['source']).read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for token in e['required_info']:assert token in info,(e['label'],token)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['label']!='canonical-audit':assert axs
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for e in v['rejected']:assert (D/e['source']).is_file() and (D/e['receipt']).is_file() and e['reason']
assert not ({e['receipt'] for e in v['accepted']}&{e['receipt'] for e in v['rejected']})
inputs=read('inputs.json');base=read('input-manifest.json')['sources_and_pins'];assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==read('canonical-order.json')
assert len(order)==293 and len({x['name'] for x in order})==293 and order[149]==read('canonical-target.json') and order[149]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1;terms=[]
for t in arrays[0].split(','):
 t=norm(t);hit=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',hit[1],hit[2]) if hit else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/v['audit']['whole_source']).read_text();assert '\n'.join(whole.splitlines()[v['audit']['start_line']-1:])==s.rstrip('\n')
e=next(e for e in v['accepted'] if e['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('INDEX_CARD150_DIRECT_CONSUMER:')]
assert cons==read('direct-consumers.json')['consumers']==['Roth.indexSet_bddAbove','Roth.Θ_le_card']
search=read('complete-caller-search.json');assert len(search['searches'])==2
for r in search['searches']:assert r['exit_code']==0 and len(r['stdout'].splitlines())==3
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}=={x['file'] for x in order}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
occ=[(x['path'],c['line']) for x in lex['files'] for c in x['occurrences']];assert occ==[('Roth/Index.lean',224),('Roth/Theta.lean',91),('Roth/Theta.lean',117)]
assert lex['applications']==lex['proof_body_applications']==2 and lex['statement_applications']==0 and len(read('callers.json'))==2
s='\n'.join((D/v['target_source']).read_text().splitlines()[v['target_start_line']-1:]);assert not re.search(r'\bindex_le_card\b',s)
for t in ['theorem noNonzero','by_cases hP : P = 0','coeff_taylor','theorem oneWitness','theorem weightedWitness']:assert t in s
s='\n'.join((D/v['callers_source']).read_text().splitlines()[v['callers_start_line']-1:]);assert not re.search(r'\bindex_le_card\b',s)
p=(ROOT/'Roth/Theta.lean').read_text()
for old,new in [('indexSet_bddAbove','bddAboveReplay'),('Θ_le_card','cardReplay')]:
 a=p.index('theorem '+old+' ');b=p.index('\nomit [DecidableEq σ] in',a)
 caller=p[a:b].replace('theorem '+old+' ','theorem '+new+' ').replace('index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)','IndexCardBridge150.noNonzero').replace('⟨hR0, hRd, -⟩','⟨-, hRd, -⟩')
 assert norm(caller) in norm(s)
assert 'variable {σ : Type*} [Fintype σ] [DecidableEq σ]' not in s
s=(D/'index-card-mathlib-executed.lean.txt').read_text()
for t in ['theorem realSupport','theorem infDegreeWitness','theorem realWitness','Finset.inf_le hd','Finset.sum_le_sum','div_le_one_of_le₀','csInf_le','by_cases hs : s.Nonempty']:assert t in s
s='\n'.join((D/v['guards_source']).read_text().splitlines()[v['guards_start_line']-1:])
for t in ['zeroPolynomial','zeroWeights','squareIndex','degreeBoundNecessary','infDegreeZeroGuard','negativeEmptyGuard','IndexScale148.zeroScale']:assert t in s
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
f=read('formal-search.json');assert len(f)==12
for i in range(3):assert {x['method'] for x in f if x['form']==i}=={'lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search'}
for x in f:assert x['request']['query'] and 'response' in x
assert 'Finset.inf_le' in json.dumps(f) and 'monomial_le_degreeOf' in json.dumps(f)
assert read('local-literature-search.json')['exit_code']==0
assert (D/'clean-index-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:680])+'\n'
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)==4
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org/abs/ ']:assert any(t in q for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['locators'] and w['titles'] and not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text()
for n in ph:assert '## Phase '+n in s
for t in ['BORDERLINE-needs-human','All17','no elision','two proof applications','not a cost downgrade','Finset.inf_le','hP deletion']:assert t in s
assert len(re.findall(r'^\d\. Should ',s,re.M))==3
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: all phases; current manifest; fresh17 source/pin hashes; exact ordered canonical293 audit; native complete clean proofs/stdaxes; independent hP weakening, two full caller replays, isolated generic support/card estimate, exact canonical witness law and six guards; exhaustive searches; portable links; secret scan.')
