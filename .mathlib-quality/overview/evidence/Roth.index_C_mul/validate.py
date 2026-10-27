#!/usr/bin/env python3
"""Portable read-only validator: current manifest, exact evidence and hashes."""
from pathlib import Path
import sys,json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.index_C_mul'
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
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==147
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='NO-composable-from-mathlib'
assert not A['unresolved'] and A['root_acceptance'] in ['pending','PASS']
phases=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(phases) and set(A['phases'].values())=={'PASS'}
O=read('overview-entry.json');assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert all(t in O['type'] for t in [N,'σ : Type','Fintype','P : MvPolynomial','α :','r :','hc : c ≠ 0'])
manifest=read('copy-manifest.json');assert manifest['declaration']==N;seen=set()
for e in manifest['files']:
 p=D/'report.md' if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 if not p.exists() and '/mathlibable/' in e['destination']:p=ROOT/e['destination']
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'];allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==7 and len(v['rejected'])==1
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
assert order[146]==read('canonical-target.json') and order[146]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t);terms.append(('private',m[1],m[2]) if m else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/'index-c-mul-original-executed.lean.txt').read_text();assert '\n'.join(whole.splitlines()[3601:])==s.rstrip('\n')
e=next(e for e in v['accepted'] if e['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=3603 and x['message'].startswith('INDEX_C_MUL147_DIRECT_CONSUMER:')]
assert cons==read('direct-consumers.json')['consumers']==['Roth.sum_max_sub_le_index_det']
assert len(read('callers.json'))==1 and read('callers.json')[0]['line']==405
search=read('complete-caller-search.json');assert len(search['searches'])==2 and all(e['exit_code']==0 and len(e['stdout'].splitlines())==2 for e in search['searches'])
assert {x['file'] for x in order}==set(search['canonical_source_inventory'])
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}==set(search['canonical_source_inventory'])
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
occ=[(x['path'],c['line'],c['kind']) for x in lex['files'] for c in x['occurrences']];assert occ==[('Roth/Index.lean',195,'declaration'),('Roth/Theta.lean',405,'body')]
assert lex['applications']==lex['proof_body_applications']==1 and lex['statement_applications']==0
s='\n'.join((D/v['target_source']).read_text().splitlines()[3920:]);assert not re.search(r'\bindex_C_mul\b',s)
for t in ['theorem replacement','theorem zero','zeroScalarGuard','support_X','support_smul_eq hc']:assert t in s,t
s=(D/'index-c-mul-explicit-composition-executed.lean.txt').read_text()
for t in ['fail_if_success exact?','exact congrArg (fun s : Finset A ↦ s.inf D)','Finsupp.support_smul_eq hc (g := f.coeff)']:assert t in s,t
assert 'simp only [AddMonoidAlgebra.infDegree' not in s
s='\n'.join((D/v['bridge_source']).read_text().splitlines()[3979:]);assert 'IndexConsumers133.targetBridge' in s and 'congrArg (WithTop.untopD 0)' in s and not re.search(r'\bindex_C_mul\b',s)
s='\n'.join((D/v['caller_source']).read_text().splitlines()[3936:]);assert 'IndexCMul147.replacement' in s and not re.search(r'\bindex_C_mul\b',s)
# Verify full caller statement/body equals production modulo only name and target replacement.
p=(ROOT/'Roth/Theta.lean').read_text();a=p.index('theorem sum_max_sub_le_index_det ');b=p.index('\nomit [DecidableEq τ] in',a)
caller=p[a:b].replace('theorem sum_max_sub_le_index_det ','theorem callerReplay ').replace('index_C_mul (Int.cast_ne_zero.2 (Units.ne_zero (Equiv.Perm.sign s)))','IndexCMul147.replacement (Int.cast_ne_zero.2 (Units.ne_zero (Equiv.Perm.sign s)))')
assert caller.strip() in s
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
formal=read('formal-search.json');assert len(formal)==3 and {e['form'] for e in formal}=={'current','literature','abstract'}
for row in formal:
 assert len(row['methods'])==4 and {e['method'] for e in row['methods']}=={'finder','loogle','leansearch','local'}
 for e in row['methods']:assert e['request']['query'] and not e['response'].get('isError',False)
assert 'Finsupp.support_smul_eq' in json.dumps(formal)
assert read('local-literature-search.json')['exit_code']==0
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)==9
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for target in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(target in q for q in queries)
assert len(set(q for q in queries if not q.startswith('site:')))>=3
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['locators'] and not any('body' in k for k in w)
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
assert (D/'clean-index-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:642])+'\n'
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text()
for n in phases:assert '## Phase '+n in s
for t in ['NO-composable-from-mathlib','BORDERLINE','not falsely counted as a three-existing-call','no elision','all17','not a logical minimality claim','3980' if False else 'congrArg']:assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: full phases; current manifest; clean native proofs; standard axioms; exact293 ordered audit; fresh17 hashes; sole caller full replay; explicit generic congruence composition; canonical133 bridge transport; searches/literature; portable links; secret scan')
