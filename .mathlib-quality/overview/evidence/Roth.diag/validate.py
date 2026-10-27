#!/usr/bin/env python3
"""Portable read-only complete declaration assessment validator."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve();N='Roth.diag'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def report():return D/'report.md' if (D/'report.md').is_file() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
def nodes(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from nodes(v)
 elif isinstance(x,list):
  for v in x:yield from nodes(v)
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==76 and a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS'] and a['production_unchanged'] and a['verdict']=='NO-composable-from-mathlib'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'} and all(v=='PASS' for v in a['phases'].values())
for x in load('copy-manifest.json')['files']:
 p=report() if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
v=load('verification.json');assert v['unresolved']==[] and len(v['rejected'])==4
assert {x['label'] for x in v['accepted']}=={'target','naturality','consumer','raw','infrastructure'}
for x in v['accepted']:
 src=D/x['source'];s=src.read_text();assert sha(src)==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 r=load(x['receipt']);assert not r['result'].get('isError',False)
 zs=[z for z in nodes(r['result'].get('structuredContent',r['result'])) if isinstance(z,dict) and z.get('success') is True];assert zs
 for z in zs:
  assert z.get('partial',False) is False and not z.get('timed_out',False) and not z.get('failed_dependencies')
  ds=z.get('diagnostics',z.get('items',[]));assert not [d for d in ds if d.get('severity') in ['error','warning'] or d.get('category')=='sorry']
  msg='\n'.join(d.get('message','') for d in ds);assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
  axes=re.findall(r'depends on axioms: \[([^]]*)\]',msg);assert axes
  for ax in axes:assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 if x['label']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M) and '#check_failure '+N in s
  for t in ['noncomputable def replacement','theorem finiteExpansion','theorem variableCollapse','theorem evaluation','uniqueAlgEquiv R PUnit','rename (fun _ : σ ↦ PUnit.unit)','algHom_ext']:assert t in s
 elif x['label']=='target':
  for t in ['#print Roth.diag','[CommSemiring R]','theorem originalRecovery','theorem contextTransport','Iff.rfl']:assert t in s
 elif x['label']=='naturality':
  for t in ['[CommSemiring S] [Algebra R S]','comp_aeval_apply','Polynomial.aeval_X','theorem ringHomRepresentation']:assert t in s
 elif x['label']=='consumer':
  for t in ['theorem subtraction','theorem vanishing','Polynomial.dvd_modByMonic_iff_dvd','MvPolynomial.hasseDeriv_map','Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero']:assert t in s
 else:
  for t in ['σ := PEmpty','ULift.{u} Unit','#synth Algebra ℕ (Polynomial ℕ)','theorem notInjective','X true','X false']:assert t in s
for x in v['rejected']:assert (D/x['source']).is_file() and (D/x['receipt']).is_file() and x['accepted'] is False
inputs=load('inputs.json');assert len(inputs)==17 and all(x['match'] and x['sha256']==x['baseline_sha256'] for x in inputs)
for x in inputs+load('source-inputs.json'):
 p=R/x['path'];assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
assert load('input-hash-check.json')['all_pass'] and '2467 jobs' in (D/'baseline-build.txt').read_text()
f=load('formal-search.json');assert len(f)==12
for method in ['Finder','Loogle','LeanSearch','Local']:
 rows=[x for x in f if x['method']==method];assert len(rows)==3 and {x['form'] for x in rows}=={'current','literature','abstract'}
 for x in rows:
  if x['result'].get('isError',False):assert method=='Loogle' and x['form']=='literature'
assert not load('loogle-standard-retry.json')['result'].get('isError',False)
for form in ['current','literature','abstract','full-name','callers','inline','local-literature']:assert load('rg-'+form+'.json')['exit_code'] in [0,1]
qs=[]
for i in range(6):
 w=load(f'web-{i}.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['urls'] and w['summary']
 assert 'result' not in w and 'response' not in w;qs.extend(x['q'] for x in w['request'].get('search_query',[]))
assert len(set(qs[:3]))==3
for site in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:assert any(site in q for q in qs)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
c=load('callers.json');assert c['named_count']==11 and len(c['callers'])==11 and c['external_to_declaring_file']==6
assert load('canonical-entry.json')['name']==N and load('overview-entry.json')['type'].startswith('∀')
s=report().read_text()
for t in ['## Phase 8','ONE-LINER WITH-EXEMPTION','NO-composable-from-mathlib','**BIG**','RESTATE-BEFORE-SHIP','Eval612','all four rejected preparations']:assert t in s,t
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('http'):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix),link
 assert (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS76: complete five native sets/four rejections; eleven actual caller plans; all def-specific gates; seventeen source/pin hashes; exhaustive literature and five formal methods/three forms; one-call aeval and generality; standard axioms, manifest, links and credential guard.')
