#!/usr/bin/env python3
"""Read-only scratch/integrated assessment validation; validates current manifest."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.eq_mapDomain_some_add_single'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return ' '.join(s.split())
A=read('assessment.json');V=read('verification.json');O=read('overview-entry.json')
assert A['declaration']==N and A['canonical_index']==153 and A['completed'] and A['allphases']=='PASS'
assert A['verdict']=='NO-composable-from-mathlib' and A['root_acceptance'] in ['pending','PASS']
assert not A['unresolved'] and not V['unresolved'] and not V['rejected']
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(ph) and set(A['phases'].values())=={'PASS'}
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
for t in [N,'Option τ','ℕ','Type u_1']:assert t in O['type']
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
assert set(V['standard_axioms'])==allowed and len(V['accepted'])==4
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
 return ds
for e in V['accepted']:
 assert sha(D/e['source'])==e['source_sha256']
 s=(D/e['source']).read_text();assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['label']!='canonical-audit':assert axs
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
base=read('input-manifest.json')['sources_and_pins'];inputs=read('inputs.json')
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:
 assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[152]==read('canonical-target.json') and order[152]['name']==N
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
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('OPTION_EXPONENTS153_DIRECT_CONSUMER:')]
assert cons==O['caller_summary']['direct_kernel_value_consumers']==['Roth.eq_sum_X_none_pow_mul_coeffNone']
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}=={x['file'] for x in order}
for f in lex['files']:
 assert sha(ROOT/f['path'])==f['sha256']
 occ=[{'line':i,'text':l} for i,l in enumerate((ROOT/f['path']).read_text().splitlines(),1) if re.search(r'\beq_mapDomain_some_add_single\b',l)]
 assert occ==f['occurrences']
for n in ['caller-rg.json','caller-git-grep.json']:
 r=read(n);assert r['exit_code']==0 and len(r['stdout'].splitlines())==2
s=(D/'caller-preparation.lean.txt').read_text();assert 'eq_mapDomain_some_add_single' not in s
assert 'rw [Roth.coeffNone, optionEquivLeft_coeff_some_coeff_none]' in s
assert s.strip() in (D/'option-exponents-caller-executed.lean.txt').read_text()
for form in ['current','literature','modern']:
 for method in ['finder','loogle','leansearch','local']:
  r=read('search-'+form+'-'+method+('.json' if (form,method)!=('modern','loogle') else '-retry.json'))
  assert r['request']['query'] and not r['response'].get('isError',False)
for n in ['current','literature','modern','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
queries=[]
for n in ['web-specific','web-general','web-alias','nlab','ncatlab','stacks','mo','arxiv']:
 w=read('literature-'+n+'.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['body_archived'] is False and w['locators'];queries.extend(q['q'] for q in w['request']['search_query'])
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t) for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
b=read(V['full_build']['receipt']);assert b['exit_code']==0 and 'Build completed successfully' in b['output']
assert b['input_hashes']=={x['path']:x['sha256'] for x in inputs}
assert sha(D/V['full_build']['log'])==b['log_sha256']
s=(D/'option-exponents-isolated-executed.lean.txt').read_text()
for t in ['[Zero M]','[AddZeroClass M]','[AddCommMonoid M]','theorem mapped','theorem bridge','theorem omission_guard','Finsupp.update_eq_add_single (Finsupp.embDomain_some_none d.some)']:assert t in s
report=D/'report.md'
if not report.exists():report=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=report.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: current manifest,17input hashes, exact canonical293 order, sole source/kernel caller, native original/generalized/bridge/guard and full caller, all literature/formal methods, links and credential guard.')
