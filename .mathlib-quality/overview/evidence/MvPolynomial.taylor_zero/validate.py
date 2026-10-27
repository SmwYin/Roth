#!/usr/bin/env python3
"""Read-only verification of scratch or integrated evidence using the current manifest."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
NAME='MvPolynomial.taylor_zero'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=read('assessment.json')
assert a['declaration']==NAME and a['canonical_index']==66 and a['completed'] and a['allphases']=='PASS'
assert a['root_acceptance'] in ['pending','PASS'] and a['unresolved']==[] and a['production_unchanged']
assert a['verdict']=='NO-composable-from-mathlib'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' for v in a['phases'].values()) and set(a['justified_na'])=={'2b','4.5'}
seen=set()
for x in read('copy-manifest.json')['files']:
 dst=x['destination'];is_report='/mathlibable/' in dst
 p=(D/'report.md' if (D/'report.md').is_file() else ROOT/dst) if is_report else D/Path(dst).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add('report.md' if is_report else p.name)
assert {'report.md','assessment.json','overview-entry.json','verification.json','validate.py','formal-search.json'}<=seen
v=read('verification.json');assert v['unresolved']==[] and len(v['rejected'])==1
assert {x['label'] for x in v['accepted']}=={'target','raw','caller'}
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
messages={}
for x in v['accepted']:
 p=D/x['source'];s=p.read_text();assert sha(p)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=read(x['receipt']);assert not r['result'].get('isError',False)
 good=[n for n in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(n,dict) and n.get('success') is True];assert good
 for n in good:
  assert n.get('partial',False) is False and n.get('timed_out',False) is False and not n.get('failed_dependencies')
  ds=n.get('diagnostics',n.get('items',[]))
  assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msg='\n'.join(d.get('message','') for d in ds);assert 'sorryAx' not in msg
  axs=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axs
  for ax in axs:assert {s.strip() for s in ax.split(',') if s.strip()}<=allowed
  messages[x['label']]=msg
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+NAME in s and 'fail_if_success exact aeval_X_left_apply P' in s
  assert 'theorem perturb' in s and '[CommSemiring A] [Algebra R A]' in s
  frag=s[s.index('theorem composed'):s.index('theorem perturb')]
  assert all(t in frag for t in ['map_zero (C','add_zero (X j)','aeval_X_left_apply P','congrArg','funext'])
  assert not re.search(r'\b(simp|rw)\b',frag)
 else:assert r['request']['file_path'].endswith('.lean')
 if x['label']=='caller':
  frag=s[s.index('namespace MvPolynomial.TaylorZeroCallers'):]
  assert 'attribute [-simp] MvPolynomial.taylor_zero' in frag
  assert 'fail_if_success solve | simp [taylor_taylor]' in frag
  assert 'simpa only [neg_add_cancel] using TaylorZeroAssessment.composed P' in frag
  assert 'theorem injective' in frag and 'theorem zero_iff' in frag
  assert 'theorem bundled' in s and 'theorem pointzero' in s
  assert '#check_failure MvPolynomial.taylor (R := T)' in s
msg=messages['caller']
old=re.search(r'ZERO_ORIGINAL_NEGATIVE_CONSTANTS: (\[[^]]*\])',msg).group(1)
new=re.search(r'ZERO_REPLACEMENT_NEGATIVE_CONSTANTS: (\[[^]]*\])',msg).group(1)
assert 'MvPolynomial.taylor_zero' in old and 'MvPolynomial.taylor_zero' not in new
assert 'MvPolynomial.TaylorZeroAssessment.composed' in new
inputs=read(v['inputs']);assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+read(v['mathlib_inputs']):
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
for src,dst in v['source_links'].items():assert sha(ROOT/src)==sha(D/dst)
assert read('input-hash-check.json')['all_pass']
f=read('formal-search.json');assert len(f)==12
for method in ['Finder','Loogle','LeanSearch','local']:
 assert {x['form'] for x in f if x['method']==method}=={'current','literature','abstract'}
for x in f:assert not x['response'].get('isError',False)
for form in ['current','literature','abstract']:assert read('rg-'+form+'.json')['exit_code']==0
assert read('rg-full-name.json')['exit_code']==1
web=[read('web0-metadata.json'),read('web4-metadata.json')]
queries=[q['q'] for w in web for q in w['actual_request']['search_query']]
assert len(set(queries[:3]))==3
for term in ['site:ncatlab.org/nlab','site:ncatlab.org ','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(term in q for q in queries),term
for n in ['web0','web4','webprimary','webfollow','weblocator']:
 w=read(n+'-metadata.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and 'response' not in w
assert read('local-literature.json')['locator']
c=read('callers.json');assert c['all_explicit_callers']==0 and c['external']==0 and c['within_declaring_file']==0
assert len(c['implicit_simp_callers'])==1 and c['implicit_simp_callers'][0]['line']==184
assert read('overview-entry.json')['type'].startswith('∀ {σ : Type') and read('canonical-entry.json')['name']==NAME
report=D/'report.md'
if not report.exists():report=ROOT/'.mathlib-quality/overview/mathlibable'/f'{NAME}.md'
s=report.read_text();assert '## Phase 8' in s and '**NO-composable-from-mathlib**' in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+NAME+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(ROOT/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: complete phases; current copy manifest; clean complete native target/raw/caller; standard axioms; 17 fresh inputs; five methods × three forms; named literature channels; exact three-fact term plus counted structural transport; actual implicit simp dependency and migrated inverse/injective/zero_iff; links; credential guard')
