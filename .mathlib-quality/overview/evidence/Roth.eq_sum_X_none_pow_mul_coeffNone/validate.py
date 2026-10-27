#!/usr/bin/env python3
"""Read-only validator for scratch and integrated package; current manifest authoritative."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.eq_sum_X_none_pow_mul_coeffNone'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return ' '.join(s.split())
A=read('assessment.json');V=read('verification.json');O=read('overview-entry.json')
assert A['declaration']==N and A['canonical_index']==156 and A['completed'] and A['allphases']=='PASS'
assert A['verdict']=='NO-mathlib-has-it' and A['root_acceptance'] in ['pending','PASS']
assert not A['unresolved'] and not V['unresolved'] and len(V['rejected'])==1
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(ph) and set(A['phases'].values())=={'PASS'}
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert O['type']==read('native-type.json')['type']
for t in [N,'Option τ','Type u_1','Type u_2','CommSemiring R','{n : ℕ}','degreeOf none P ≤ n']:assert t in O['type']
assert 'Fintype' not in O['type'] and 'DecidableEq' not in O['type']
M=read('copy-manifest.json');assert M['declaration']==N;seen=set()
for x in M['files']:
 p=D/'report.md' if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 if not p.exists() and '/mathlibable/' in x['destination']:p=ROOT/x['destination']
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
allowed={'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms'])==allowed and len(V['accepted'])==5

def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z);assert z['success'] and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s
  assert not re.search(r'^import Roth\b',s,re.M);ds=z['diagnostics']
 else:
  assert z['partial'] is False and not z.get('failed_dependencies') and not z.get('still_elaborating_lines')
  assert r['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean';ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message'] for x in ds)):
  assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
 return ds
for e in V['accepted']:
 assert sha(D/e['source'])==e['source_sha256']
 s=(D/e['source']).read_text();assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 if e['label']!='canonical-audit':assert 'depends on axioms:' in info
for e in V['rejected']:
 assert (D/e['source']).is_file() and (D/e['receipt']).is_file()
 assert 'sorryAx' in (D/e['receipt']).read_text()
 assert e['receipt'] not in {x['receipt'] for x in V['accepted']}
base=read('input-manifest.json')['sources_and_pins'];inputs=read('inputs.json')
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[155]==read('canonical-target.json') and order[155]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/V['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S)
assert len(arrays)==1;terms=[]
for t in arrays[0].split(','):
 t=norm(t);hit=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',hit[1],hit[2]) if hit else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/V['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[V['audit']['start_line']-1:])==s.rstrip('\n')
e=next(x for x in V['accepted'] if x['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('COEFFICIENT_EXPANSION156_DIRECT_CONSUMER:')]
assert cons==O['caller_summary']['direct_kernel_value_consumers']==['Roth.exists_separated_representation']
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}=={x['file'] for x in order}
for f in lex['files']:
 assert sha(ROOT/f['path'])==f['sha256']
 occ=[{'line':i,'text':l} for i,l in enumerate((ROOT/f['path']).read_text().splitlines(),1) if re.search(r'\beq_sum_X_none_pow_mul_coeffNone\b',l)]
 assert occ==f['occurrences']
for n in ['caller-rg.json','caller-git-grep.json']:
 r=read(n);assert r['exit_code']==0 and len(r['stdout'].splitlines())==2
s=(D/'caller-preparation.lean.txt').read_text()
assert 'eq_sum_X_none_pow_mul_coeffNone' not in s and 'Expansion156.expanded P hn' in s
for t in ['Lean.mkPrivateNameCore `Roth.Separation `Roth.exists_coeffNone_basis_aux','Lean.mkPrivateNameCore `Roth.Separation `Roth.linearIndependent_coordinate_polynomials_aux','Lean.mkPrivateNameCore `Roth.Separation `Roth.eq_sum_aeval_basis_coeffNone_aux']:assert t in s
for form in ['current','literature','modern']:
 for method in ['finder','loogle','leansearch','local']:
  r=read('search-'+form+'-'+method+'.json');assert r['request']['query'] and not r['response'].get('isError',False)
  assert not r['response'].get('error')
for n in ['current','literature','modern','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
queries=[]
for n in ['web-specific','web-general','web-alias','nlab','ncatlab','stacks','mo','arxiv']:
 w=read('literature-'+n+'.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['body_archived'] is False and w['locators'] and w['titles'] and 'Pending' not in w['summary'];queries.extend(q['q'] for q in w['request']['search_query'])
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t) for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert read('local-literature-search.json')['exit_code']==0
b=read(V['full_build']['receipt']);assert b['exit_code']==0 and 'Build completed successfully' in b['output']
assert b['input_hashes']=={x['path']:x['sha256'] for x in inputs}
assert sha(D/V['full_build']['log'])==b['log_sha256']
s=(D/'coefficient-expansion-isolated-executed.lean.txt').read_text()
for t in ['theorem canonical','theorem inverse_C','theorem expanded',"Polynomial.as_sum_range_C_mul_X_pow'",'natDegree_optionEquivLeft R P','aevalTower']:assert t in s
s=(D/'coefficient-expansion-guards-executed.lean.txt').read_text()
for t in ['[Semiring A]','theorem semiring_expansion','theorem bound_guard','theorem endpoint_guard']:assert t in s
report=D/'report.md'
if not report.exists():report=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=report.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: current manifest,17fresh inputs, exact ordered293audit, sole complete source/kernel caller, native original/canonical/bridge/guards/caller, all literature and15formal searches, links and credential guard.')
