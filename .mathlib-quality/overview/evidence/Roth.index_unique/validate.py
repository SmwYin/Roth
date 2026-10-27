#!/usr/bin/env python3
"""Read-only portable assessment validator, scratch or integrated; current manifest authoritative."""
from pathlib import Path
import json,hashlib,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.index_unique'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return ' '.join(s.split())
def native(e):
 r=read(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] and not z.get('timed_out')
 s=(D/e['source']).read_text()
 if e['format']=='raw':
  ds=z['diagnostics'];assert r['request']['code']==s
  assert '#check_failure '+N in s and not re.search(r'^import Roth\b',s,re.M)
 else:
  assert z['partial'] is False and not z.get('failed_dependencies') and not z.get('still_elaborating_lines')
  assert r['request']['file_path']=='.lake/roth-overview-session/GenWronskianChecks.lean'
  ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 return ds
A=read('assessment.json')
assert A['declaration']==N and A['canonical_index']==151 and A['verdict']=='NO-mathlib-has-it'
assert A['completed'] and A['allphases']=='PASS' and not A['unresolved']
assert A['root_acceptance'] in ['pending','PASS']
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert set(A['phases'])==set(ph) and set(A['phases'].values())=={'PASS'}
O=read('overview-entry.json')
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(O)
for t in [N,'σ : Type','P ≠ 0','Fintype','Unique','rootMultiplicity']:assert t in O['type']
m=read('copy-manifest.json');assert m['declaration']==N;seen=set()
for e in m['files']:
 p=D/'report.md' if '/mathlibable/' in e['destination'] else D/Path(e['destination']).name
 if not p.exists() and '/mathlibable/' in e['destination']:p=ROOT/e['destination']
 assert p.is_file() and sha(p)==e['sha256'] and p.stat().st_size==e['bytes'],p
 seen.add(p.name)
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert {p.name for p in D.iterdir() if p.is_file()}-{'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}<=seen
v=read('verification.json');assert not v['unresolved'] and len(v['accepted'])>=6
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
for e in v['accepted']:
 assert sha(D/e['source'])==e['source_sha256']
 s=(D/e['source']).read_text()
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 ds=native(e)
 info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',info)
 if e['label']!='canonical-audit':assert axs
 for ax in axs:assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
for e in v['rejected']:
 assert (D/e['source']).is_file() and (D/e['receipt']).is_file() and e['reason']
assert not ({e['receipt'] for e in v['accepted']}&{e['receipt'] for e in v['rejected']})
base=read('input-manifest.json')['sources_and_pins'];inputs=read('inputs.json')
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+read('mathlib-inputs.json'):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in read('source-links.json').items():assert sha(ROOT/p)==sha(D/q)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==read('canonical-order.json') and len(order)==293 and len({x['name'] for x in order})==293
assert order[150]==read('canonical-target.json') and order[150]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private' else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=norm(t);hit=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',hit[1],hit[2]) if hit else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/v['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[v['audit']['start_line']-1:])==s.rstrip('\n')
e=next(x for x in v['accepted'] if x['label']=='canonical-audit');ds=native(e)
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=e['native_region_start_line'] and x['message'].startswith('INDEX_UNIQUE151_DIRECT_CONSUMER:')]
assert cons==['_private.Roth.Theta.0.Roth.index_unique_le_log_div']==O['caller_summary']['direct_kernel_value_consumers']
lex=read('lexical-enumeration.json')
assert {x['path'] for x in lex['files']}=={x['file'] for x in order}
for x in lex['files']:assert sha(ROOT/x['path'])==x['sha256']
assert [(x['path'],c['line']) for x in lex['files'] for c in x['occurrences']]==[('Roth/Index.lean',39),('Roth/Index.lean',234),('Roth/Theta.lean',242)]
assert lex['applications']==lex['proof_body_applications']==1 and lex['statement_applications']==0
for n in ['caller-rg.json','caller-git-grep.json']:
 r=read(n);assert r['exit_code']==0 and len(r['stdout'].splitlines())==3
cs=read('callers.json');assert len(cs)==1 and cs[0]['application_line']==242
p=(ROOT/'Roth/Theta.lean').read_text();a=p.index('private lemma index_unique_le_log_div');b=p.index('\nomit [DecidableEq σ] in',a)
assert cs[0]['source']==p[a:b]
s=(D/v['target_source']).read_text().splitlines()[v['target_start_line']-1:];s='\n'.join(s)
proof=s[:s.index('#check @Roth.index_unique')]
assert not re.search(r'\bindex_unique\b',proof)
for t in ['theorem independentNonzero','theorem allPolynomials','by_cases hP : P = 0','theorem noAutomaticClosure','fail_if_success rfl','solve | simp only [index]','theorem zeroDenominator']:assert t in proof
s='\n'.join((D/v['callers_source']).read_text().splitlines()[v['callers_start_line']-1:v['guards_start_line']-1])
caller=p[a:b].replace('private lemma index_unique_le_log_div','theorem logBoundReplay',1).replace('index_unique ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR)','IndexUniqueAssessment151.allPolynomials')
assert norm(caller) in norm(s) and not re.search(r'\bindex_unique\b',s)
s='\n'.join((D/v['callers_source']).read_text().splitlines()[v['guards_start_line']-1:])
for t in ['zeroPolynomial','arbitraryFintype','uniqueProvidesFinite','negativeScaleGuard','wrongZeroInfinityGuard']:assert t in s
start=s.index('theorem uniqueProvidesFinite');stop=s.index('theorem negativeScaleGuard')
assert '[Fintype' not in s[start:stop]
c='\n'.join((D/v['collapse_source']).read_text().splitlines()[v['collapse_start_line']-1:])
for t in ['theorem collapseCancellation','rename (fun _ : Fin 2 ↦ ())','X 0 - X 1','congrArg (eval']:assert t in c
s=(D/v['normalization_source']).read_text()
for t in ['theorem minimumSupport','theorem taylorMinimum','theorem existingReaim','theorem trailingInf','theorem rootInf','theorem realInfSupport','theorem realRootInf','theorem finsetBridge','untopD 0','Polynomial.rootMultiplicity_eq_natTrailingDegree.symm']:assert t in s
for n in ['current','literature','abstract','inline']:assert read('rg-'+n+'.json')['exit_code'] in [0,1]
f=read('formal-search.json');assert len(f)==12
for form in ['current','literature','abstract']:
 assert {x['method'].split('-')[0] for x in f if x['method'].endswith('-'+form)}=={'Finder','Loogle','LeanSearch','local'}
for x in f:assert x['request']['query'] and x['result']['status']=='fulfilled' and not x['result']['value'].get('isError',False)
assert read('local-literature-search.json')['exit_code']==0
assert (D/'clean-index-excerpt.tex.txt').read_text()=='\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:680])+'\n'
web=[read(p.name) for p in D.glob('web-*.json')];assert len(web)==5
queries=[q['q'] for w in web for q in w['request'].get('search_query',[])]
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org/abs/ ']:assert any(t in q for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
for w in web:assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status'] and w['locators'] and w['titles'] and w['body_archived'] is False
assert read('literature-summary.json')['chatgpt_math'].startswith('n/a:')
build=read(v['full_build']['receipt']);assert build['exit_code']==0 and 'Build completed successfully' in build['output']
assert build['command'].endswith('lake build') and build['cwd']==str(ROOT)
assert v['full_build']['source_hashes_match_baseline'] is True
p=D/'report.md'
if not p.exists():p=ROOT/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=p.read_text()
for n in ph:assert '## Phase '+n in s
for t in ['NO-mathlib-has-it','All 17','without MCP elision','proof applications 1','not a cost downgrade','rootMultiplicity_eq_natTrailingDegree','NOT-COMPOSABLE']:assert t in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: all phases; current manifest; fresh17 source/pin hashes; exact canonical293 audit; clean native proofs/stdaxes; independent hP weakening, full sole caller replay, isolated support and projected infDegree/trailing/root normalization, false-generalization guards; actual full lake build; exhaustive searches; portable links; secret scan.')
