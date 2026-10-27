#!/usr/bin/env python3
"""Portable read-only validator of current manifest, native evidence and full assessment."""
from pathlib import Path
import json, hashlib, re, sys, subprocess
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.index_rename'
def read(n): return json.loads((D/n).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s): return ' '.join(s.split())
def native(e):
 r=read(e['receipt']); assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] is True and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  ds=z['diagnostics'];assert r['request']['code']==s
  assert '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies')
  assert not z.get('still_elaborating_lines')
  ds=z['items'];assert r['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 return ds
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==149
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='NO-composable-from-mathlib'
assert A['root_acceptance'] in ['pending','PASS'] and not A['unresolved']
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(phases) and set(A['phases'].values())=={'PASS'}
O=read('overview-entry.json')
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
for t in [N,'σ : Type','τ : Type','Function.Injective','Fintype','r : τ → ℕ']:assert t in O['type']
manifest=read('copy-manifest.json'); assert manifest['declaration']==N;seen=set()
for e in manifest['files']:
 p=D/'report.md' if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 if not p.exists() and '/mathlibable/' in e['destination']:p=ROOT/e['destination']
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed and len(v['accepted'])==7 and len(v['rejected'])==4
for e in v['accepted']:
 assert sha(D/e['source'])==e['source_sha256'];s=(D/e['source']).read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for m in e['required_info']:assert m in info,(e['label'],m)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['label']!='canonical-audit':assert axs,e['label']
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for e in v['rejected']:assert (D/e['source']).is_file() and (D/e['receipt']).is_file() and e['reason']
assert not ({e['receipt'] for e in v['accepted']}&{e['receipt'] for e in v['rejected']})
inputs=read('inputs.json');base=read('input-manifest.json')['sources_and_pins']
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:
 assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q),(p,q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[148]==read('canonical-target.json') and order[148]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=norm(t);m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/v['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[v['audit']['start_line']-1:])==s.rstrip('\n')
e=next(x for x in v['accepted'] if x['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('INDEX_RENAME149_DIRECT_CONSUMER:')]
assert cons==['_private.Roth.Theta.0.Roth.indexSet_comp_subset','_private.Roth.Theta.0.Roth.index_separated_mul_le_aux']
assert read('direct-consumers.json')['consumers']==['Roth.indexSet_comp_subset','Roth.index_separated_mul_le_aux']
search=read('complete-caller-search.json');assert len(search['searches'])==2
for r in search['searches']:assert r['exit_code']==0 and len(r['stdout'].splitlines())==4
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}=={x['file'] for x in order}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
occ=[(x['path'],c['line']) for x in lex['files'] for c in x['occurrences']]
assert occ==[('Roth/Index.lean',39),('Roth/Index.lean',212),('Roth/Theta.lean',154),('Roth/Theta.lean',442)]
assert lex['applications']==lex['proof_body_applications']==3 and lex['source_reference_lines']==2 and lex['statement_applications']==0
assert len(read('callers.json'))==2 and sum(x['applications'] for x in read('callers.json'))==3
s=(D/v['target_source']).read_text().splitlines();s='\n'.join(s[v['target_start_line']-1:])
assert 'IndexExpanded133.fullyExpandedBridge' in s and 'IndexRenameMathlib149.transport hf' in s
assert not re.search(r'\b(index_rename|taylor_rename|weight_mapDomain)\b',re.sub(r'--[^\n]*','',s))
s='\n'.join((D/v['callers_source']).read_text().splitlines()[v['callers_start_line']-1:])
p=(ROOT/'Roth/Theta.lean').read_text()
for old,new,sep in [('indexSet_comp_subset','equivCallerReplay','σ'),('index_separated_mul_le_aux','separatedCallerReplay','τ')]:
 a=p.index('private lemma '+old+' ');b=p.index('\nomit [DecidableEq '+sep+'] in',a)
 caller=p[a:b].replace('private lemma '+old+' ','theorem '+new+' ').replace('index_rename','IndexRenameBridge149.replacement')
 assert norm(caller) in norm(s),old
assert not re.search(r'\bindex_rename\b',s)
for t in ['theorem collision','theorem zeroPolynomial','theorem zeroWeights','Ne.symm hn','theorem weighted','[CommSemiring R] [AddCommMonoid M] [SemilatticeInf M]']:assert t in s,t
m=(D/'index-rename-mathlib-final-executed.lean.txt').read_text()
for t in ['support_rename_of_injective (p := P) hf','Finset.inf_image P.support (Finsupp.mapDomain f) D','linearCombination_mapDomain ℕ (v\' := w) f d','comp_aeval_apply','algebraMap_eq']:assert t in m,t
assert len(re.findall(r'Fintype',m))==0
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
formal=read('formal-search.json');assert len(formal)==3 and {x['form'] for x in formal}=={'current','literature','abstract'}
for row in formal:
 assert {x['method'] for x in row['methods']}=={'finder','loogle','leansearch','local'}
 for e in row['methods']:assert e['request']['query'] and 'response' in e
assert 'Finset.inf_image' in json.dumps(formal) and 'linearCombination_mapDomain' in json.dumps(formal)
assert read('local-literature-search.json')['exit_code']==0
assert (D/'clean-index-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:642])+'\n'
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)==5
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(t in q for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
for w in web:
 assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['locators'] and w['titles']
 assert not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text()
for n in phases:assert '## Phase '+n in s
for t in ['NO-composable-from-mathlib','BORDERLINE','not definitional','no elision','All17','not a claim of a single mechanical edit','two existing mathlib','Salami','three proof applications']:assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: all phases; current manifest; fresh17 hashes; ordered canonical293 audit; clean native proofs and standard axioms; exact two-call infDegree composition, noncircular bridge, both full caller replays, collision and zero guards, arbitrary expanded coefficients/weights/variables; complete formal/literature searches; portable links; secret scan')
