#!/usr/bin/env python3
"""Read-only validator for scratch and integrated evidence; current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.coeff_uniqueAlgEquiv_symm'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=read('assessment.json');V=read('verification.json');O=read('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert A['declaration']==N and A['canonical_index']==161 and A['completed']
assert A['allphases']=='PASS' and A['verdict']=='NO-mathlib-has-it'
assert A['root_acceptance'] in ['pending','PASS'] and not A['unresolved'] and not V['unresolved']
assert A['phases']==dict.fromkeys(ph,'PASS')
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert O['type']==read('native-type.json')['type'] and O['project_dependencies']==[]
for t in [N,'Type u_1','Type u_2','CommSemiring R','Unique σ','(f : Polynomial R)','(n : ℕ)']:assert t in O['type']
assert not any(t in O['type'] for t in ['Fintype','DecidableEq','IsDomain'])
M=read('copy-manifest.json');assert M['declaration']==N;seen=set()
for x in M['files']:
 p=D/'report.md' if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 if not p.exists() and '/mathlibable/' in x['destination']:p=R/x['destination']
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add('report.md' if '/mathlibable/' in x['destination'] else p.name)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms'])==allowed and len(V['accepted'])==4

def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] and not z.get('timed_out')
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
 s=(D/e['source']).read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e);info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 if e['label']!='canonical-audit':assert 'depends on axioms:' in info
assert len(V['rejected'])==1
for e in V['rejected']:
 r=read(e['receipt']);z=r['result']['structuredContent'];z=z.get('result',z)
 assert not z['success'] and any('sorryAx' in x['message'] for x in z['diagnostics'])
 assert r['request']['code']==(D/e['source']).read_text()
 assert e['source'] not in {x['source'] for x in V['accepted']}
base=read('input-manifest.json')['sources_and_pins'];inputs=read('inputs.json')
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(R/p)==sha(D/q)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[160]==read('canonical-target.json') and order[160]['name']==N
assert read('corrected-target.json')['line']==169
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/V['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S)
assert len(arrays)==1;terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());hit=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',hit[1],hit[2]) if hit else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/V['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[V['audit']['start_line']-1:])==s.rstrip('\n')
e=next(x for x in V['accepted'] if x['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('UNIQUE_COEFF161_DIRECT_CONSUMER:')]
assert cons==O['caller_summary']['direct_kernel_value_consumers']==[]
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}=={x['file'] for x in order}
for f in lex['files']:
 assert sha(R/f['path'])==f['sha256']
 occ=[{'line':i,'text':l} for i,l in enumerate((R/f['path']).read_text().splitlines(),1) if re.search(r'\bcoeff_uniqueAlgEquiv_symm\b',l)]
 assert occ==f['occurrences']
assert sum(len(f['occurrences']) for f in lex['files'])==5
for n in ['caller-rg.json','caller-git-grep.json']:
 r=read(n);assert r['exit_code']==0 and len(r['stdout'].splitlines())==5
assert O['caller_summary']['explicit_call_sites']==[] and O['caller_summary']['explicit_use_count']==0
assert len(O['caller_summary']['inline_derivations'])==1
s='\n'.join((D/'unique-coeff-context-executed.lean.txt').read_text().splitlines()[8096:])
assert 'Roth.coeff_uniqueAlgEquiv_symm' not in s and 'theorem thetaBound' in s
assert 'rw [MvPolynomial.coeff_uniqueAlgEquiv_symm]' in s and 'exact hVc _' in s
rows=read('formal-search.json');assert len(rows)==14
for form in ['current','standard','abstract']:
 for method in ['Finder','Loogle','LeanSearch','local']:
  rs=[x for x in rows if x['form']==form and x['method']==method]
  assert rs and all(x['request']['query'] for x in rs)
  assert any(not x.get('response',{}).get('isError',False) for x in rs)
assert next(x for x in rows if x.get('retry'))['form']=='standard'
for n in ['current','literature','modern','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
queries=[];w=read('literature-individual.json');assert len(w)==8
for x in w:
 assert len(x['response_sha256'])==64 and x['response_bytes']>0 and x['status'] and x['body_archived'] is False
 assert x['locators'] and x['titles'] and x['summary'];queries.extend(q['q'] for q in x['request']['search_query'])
for t in ['site:ncatlab.org/nlab/','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org/abs/ ']:assert any(q.startswith(t) for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert read('local-literature-search.json')['exit_code']==0
assert '2023' in read('literature-availability.json')['recent_primary']
for n in ['literature-primary-access.json','literature-primary-locators.json']:
 for x in read(n):assert len(x['sha256'])==64 and x['bytes']>0 and not x['body_archived']
b=read(V['full_build']['receipt']);assert b['exit_code']==0 and 'Build completed successfully' in b['output']
assert b['input_hashes']=={x['path']:x['sha256'] for x in inputs} and sha(D/V['full_build']['log'])==b['log_sha256']
s=(D/'unique-coeff-isolated-executed.lean.txt').read_text()
for t in ['theorem oldForm','theorem generalForm','theorem arbitraryCoordinate','theorem representationBridge','theorem falseGeneralization','(congrArg f.coeff Finsupp.single_eq_same)','#check_failure (MvPolynomial.uniqueAlgEquiv ℕ Bool)','#check_failure (MvPolynomial.uniqueAlgEquiv S Unit)']:assert t in s
assert '[DecidableEq' not in s and '[Fintype' not in s
report=D/'report.md'
if not report.exists():report=R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=report.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: all phases, fresh17 inputs, exact293 ordered audit, existing general coefficient law, full representation bridge, guards, zero actual callers, independent Theta coefficient branch, all15search cells and all literature channels; current manifest and credential guard.')
