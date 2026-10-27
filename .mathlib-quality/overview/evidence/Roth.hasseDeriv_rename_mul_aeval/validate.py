#!/usr/bin/env python3
"""Portable read-only validator: current manifest, exact native evidence, canonical293."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.hasseDeriv_rename_mul_aeval'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=read('assessment.json');V=read('verification.json');O=read('overview-entry.json')
assert A['declaration']==N and A['canonical_index']==160
assert A['completed'] and A['allphases']=='PASS' and A['verdict']=='YES-but-generalise-first'
assert A['root_acceptance'] in ['pending','PASS'] and not A['unresolved'] and not V['unresolved']
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(ph) and set(A['phases'].values())=={'PASS'}
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert O['type']==read('native-type.json')['type']
for t in [N,'Type u_1','Type u_2','CommSemiring','(d : Finsupp','(ν : ℕ)','(U : MvPolynomial','(V : Polynomial']:assert t in O['type'],t
assert not any(t in O['type'] for t in ['Fintype','DecidableEq','IsDomain','Field'])
M=read('copy-manifest.json');assert M['declaration']==N;seen=set()
for x in M['files']:
 p=D/'report.md' if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 if not p.exists() and '/mathlibable/' in x['destination']:p=ROOT/x['destination']
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms'])==allowed and len(V['accepted'])==8 and len(V['rejected'])==3

def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  assert r['request']['code']==s and '#check_failure '+N in s
  assert '#check_failure MvPolynomial.hasseDeriv' in s
  assert not re.search(r'^import Roth\b',s,re.M);ds=z['diagnostics']
  assert len(re.findall(r'^import ',s,re.M))==9
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
for e in V['rejected']:
 assert (D/e['source']).is_file() and (D/e['receipt']).is_file()
 assert e['receipt'] not in {x['receipt'] for x in V['accepted']}
base=read('input-manifest.json')['sources_and_pins'];inputs=read('inputs.json')
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[159]==read('canonical-target.json') and order[159]['name']==N
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
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('HASSE_SEPARATION160_DIRECT_CONSUMER:')]
assert cons==O['caller_summary']['direct_kernel_value_consumers']==['Roth.det_hasseDeriv_separated']
lex=read('lexical-enumeration.json');assert {x['path'] for x in lex['files']}=={x['file'] for x in order}
for f in lex['files']:
 assert sha(ROOT/f['path'])==f['sha256']
 occ=[{'line':i,'text':l} for i,l in enumerate((ROOT/f['path']).read_text().splitlines(),1) if re.search(r'\bhasseDeriv_rename_mul_aeval\b',l)]
 assert occ==f['occurrences']
assert sum(len(f['occurrences']) for f in lex['files'])==2
for n in ['caller-rg.json','caller-git-grep.json']:
 r=read(n);assert r['exit_code']==0 and len(r['stdout'].splitlines())==2
assert len(O['caller_summary']['explicit_call_sites'])==1 and not O['caller_summary']['inline_derivations']
s='\n'.join((D/'hasse-separation-generalized-caller-executed.lean.txt').read_text().splitlines()[7751:])
assert 'theorem generalizedCaller' in s and 'freshCoordinate some' in s
assert 'hasseDeriv_rename_mul_aeval' not in s and '[Field K]' in s
s='\n'.join((D/'hasse-separation-generality-executed.lean.txt').read_text().splitlines()[7710:])
for t in ['theorem freshCoordinate','(hf : Function.Injective f)','(hi : ∀ j, f j ≠ i)','hasseDeriv_rename hg','factorwise d ν U V','fun o ↦ Option.elim o i f']:assert t in s,t
assert 'Roth.hasseDeriv_rename_mul_aeval' not in s
s='\n'.join((D/'hasse-separation-specialization-executed.lean.txt').read_text().splitlines()[7740:])
assert 'theorem originalFormAgain' in s and 'freshCoordinate some' in s
rows=read('formal-search.json');assert len(rows)==15
for form in ['current','standard','abstract']:
 for method in ['Finder','Loogle','LeanSearch','local','rg']:
  e=next(x for x in rows if x['form']==form and x['method']==method)
  if method=='rg':assert e['response']['exit_code'] in [0,1]
  else:assert e['request']['query'] and not e['response'].get('isError',False)
queries=[];w=read('literature-search.json');assert len(w)==8
for x in w:
 assert len(x['response_sha256'])==64 and x['response_bytes']>0 and x['status'] and x['body_archived'] is False
 assert x['locators'] and x['titles'] and x['summary'];queries.extend(q['q'] for q in x['request']['search_query'])
for t in ['site:ncatlab.org/nlab/','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org/abs/ ']:assert any(q.startswith(t) for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert read('local-literature-search.json')['exit_code']==0
assert any('2305.04537' in x for x in read('literature-availability.json')['recent_primary'])
for x in read('literature-primary.json'):
 assert len(x['response_sha256'])==64 and x['response_bytes']>0 and not x['body_archived']
b=read(V['full_build']['receipt']);assert b['exit_code']==0 and 'Build completed successfully' in b['output']
assert b['input_hashes']=={x['path']:x['sha256'] for x in inputs} and sha(D/V['full_build']['log'])==b['log_sha256']
s=(D/'hasse-separation-isolated-executed.lean.txt').read_text()
for t in ['theorem constantFactor','theorem separatedCoefficients','theorem semiringLaw','theorem overlapCounterexample','[Semiring S]','Polynomial.hasseDeriv_coeff','Polynomial.hasseDeriv_map','Polynomial.coeff_one']:assert t in s
s=(D/'hasse-separation-sum-guard-executed.lean.txt').read_text()
for t in ['theorem overlapSumOrderCounterexample','Polynomial.hasseDeriv 2','Polynomial.hasseDeriv 1','have hp','by ring']:assert t in s,t
report=D/'report.md'
if not report.exists():report=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=report.read_text()
for n in ph:assert '## Phase '+n in s
assert 'requested separately' not in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: all phases; fresh17 inputs; exact ordered293 audit; verified fresh-coordinate generalization, original specialization and sole complete generalized caller; isolated mathlib partial proofs/guard; all15 formal searches and literature channels; current manifest and credential guard.')
