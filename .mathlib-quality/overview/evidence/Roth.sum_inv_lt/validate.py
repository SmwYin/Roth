#!/usr/bin/env python3
"""Read-only validation of scratch or integrated current assessment evidence."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.sum_inv_lt'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(rec):
 x=rec['result'];assert not x.get('isError',False)
 x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
rp=D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==123
assert a['completed'] and a['allphases']=='PASS' and a['unresolved']==[]
assert a['root_acceptance'] in ['pending','PASS'] and a['production_unchanged']
assert a['classification']=='SMALL' and a['verdict']=='BORDERLINE-needs-human'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
m=load('copy-manifest.json');assert m['declaration']==N
for f in m['files']:
 p=rp if '/mathlibable/' in f['destination'] else D/Path(f['destination']).name
 assert p.is_file() and sha(p)==f['sha256'] and p.stat().st_size==f['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(f['destination']).name for f in m['files']}|{'report.md'}
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
rows=load('source-inputs.json');assert len(rows)==17 and {x['path'] for x in rows}==set(b['sources_and_pins'])
for x in rows:assert x['matches'] and x['sha256']==b['sources_and_pins'][x['path']]['sha256']==sha(R/x['path']) and (R/x['path']).stat().st_size==x['bytes']
assert sha(D/'declaring-module.lean.txt')==sha(R/'Roth/Lattice.lean')
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==load('canonical-snapshot.json')
assert len(order)==293 and len({x['name'] for x in order})==293 and order[122]==load('canonical-entry.json') and order[122]['name']==N
terms=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 terms.append(n)
expected='let names : Array Lean.Name := #['+','.join(terms)+']';norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(expected)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[]
assert v['production_unchanged'] and set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'}
assert {x['label'] for x in v['accepted']}=={'original','audit','real-generalization','actual-caller','helpers','guards','raw-generalization','abstract-convex'}
for x in v['accepted']:
 s=(D/x['source']).read_text();assert sha(D/x['source'])==x['source_sha256']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 rec=load(x['receipt']);assert rec['request']==x['original_execution_request'];nr=native(rec)
 assert nr['success'] and not nr.get('partial',False) and not nr.get('timed_out') and not nr.get('failed_dependencies')
 if x['execution_kind']=='persistent-disk':assert nr['partial'] is False
 ds=nr.get('items',nr.get('diagnostics',[]));assert not [y for y in ds if y.get('severity') in ['error','warning'] or y.get('category')=='sorry']
 txt='\n'.join(y.get('message','') for y in ds);assert not any(t in txt for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',txt):assert {t.strip() for t in ax.split(',') if t.strip()}<=set(v['standard_axioms'])
 fresh=[y for y in ds if y.get('line',0)>=x['native_region_start_line']];msg='\n'.join(y.get('message','') for y in fresh)
 for name in x['expected_axiom_declarations']:assert "'"+name+"' depends on axioms:" in msg or "'"+name+"' does not depend on any axioms" in msg
 if 'code' in rec['request']:assert rec['request']['code']==s and not re.search(r'^import Roth\b',s,re.M) and '#check_failure Roth.sum_inv_lt' in s
 if x['label']=='original':assert 'Roth.sum_inv_lt {r m : ℕ}' in msg and '2 * √↑m < lam' in msg and '53225 characters elided' in msg
 if x['label']=='audit':
  arrs=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S);assert len(arrs)==1 and norm(arrs[0])==norm(expected)
  assert 'SUM_INV_LT_AUDIT: requested=293; unique=293' in msg and 'SUM_INV_LT_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[y['message'].split(': ',1)[1] for y in fresh if y.get('message','').startswith('SUM_INV_LT_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['_private.Roth.Lattice.0.Roth.card_filter_weight_le_succ_aux']
 if x['label']=='real-generalization':assert 'hm : 1 < m' in s and 'hlam : 2 * √m ≤ lam' in s and 'sumInvPrivateBound%' in s
 if x['label']=='actual-caller':assert 'Roth.SumInvAssessment.realWeak' in s and 'sumInvPrivateFiber%' in s
 if x['label']=='helpers':assert s.count('(hlam : 1 < lam)')==2
 if x['label']=='raw-generalization':assert 'hm : 1 < m' in s and 'hlam : 2 * √m ≤ lam' in s and 'sum_inv_le hr (by linarith : 1 < lam)' in s
 if x['label']=='abstract-convex':assert 'convexOn_zpow (𝕜 := ℝ) (-1)' in s and 'push_cast at hh' in s
assert {x['label'] for x in v['rejected']}=={'direct-search','initial-raw-generalization','initial-abstract-convex'}
for x in v['rejected']:
 assert x['reason'] and (D/x['source']).is_file();rec=load(x['receipt']);assert rec['request']==x['original_execution_request']
 nr=native(rec);ds=nr.get('items',nr.get('diagnostics',[]));assert not nr.get('success',False) and any(y.get('severity') in ['error','warning'] for y in ds)
 if x['label']=='direct-search':
  txt='\n'.join(y.get('message','') for y in ds)
  assert txt.count('`exact?` could not close the goal')==3 and not nr.get('timed_out',False)
f=load('formal-search.json');assert len(f)==12
for method in ['Finder','LeanSearch','Loogle','local']:
 rs=[x['value'] for x in f if x['status']=='fulfilled' and x['value']['method']==method]
 assert {x['form'] for x in rs}=={'current','literature','abstract'}
ss=load('source-search-raw.json');assert len(ss['commands'])==len(ss['results'])==5
assert all(x['status']=='fulfilled' and x['value']['exit_code'] in [0,1] and 'truncated' not in x['value']['output'].lower() for x in ss['results'])
for i in range(6):
 w=load(f'web{i}-metadata.json');assert len(w['response_sha256'])==64 and w['response_bytes']>0 and w['status']=='returned' and w['summaries']
 assert all('?' not in u for u in w['urls'])
assert len(load('web0-metadata.json')['request']['search_query'])==3
assert load('web5-metadata.json')['request']['search_query']==[{'q':'site:ncatlab.org/ncatlab "convex function" "finite sum"'}]
assert len(load('web4-metadata.json')['request']['open'])==4
assert load('optional-tool-availability.json')['ask_chatgpt_math']=='unavailable'
t=rp.read_text()
for l in re.findall(r'\]\(([^)]+)\)',t):
 if l.startswith('../evidence/'+N+'/'):assert (D/l.split('/')[-1]).is_file(),l
 elif not l.startswith('https://'):raise AssertionError(l)
for token in ['**SMALL**','| 9 |','RESTATE-BEFORE-SHIP','STRICTLY NARROWER THAN STANDARD','NOT-COMPOSABLE','53225','Phase 8','instance-priority collision','trivial simp composition','site:ncatlab.org/ncatlab']:
 assert token in t,token
assert len(re.findall(r'^\d\. Should|^\d\. If that',t,re.M))==4
ov=load('overview-entry.json');assert ov['type'].startswith('Roth.sum_inv_lt {r m : ℕ}') and '∑' in ov['type'] and ov['canonical_index']==123
scan=load('secrets-scan.json');assert scan['returncode']==0 and scan['script_sha256']==sha(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py')
print('PASS: current manifest, complete phases,17 source/pin hashes, exact293 canonical order, all native accepted/rejected receipts, real weakening, rational helpers, guards, convex/reflection probes, sole caller, all five methods ×three forms, all named literature channels')
