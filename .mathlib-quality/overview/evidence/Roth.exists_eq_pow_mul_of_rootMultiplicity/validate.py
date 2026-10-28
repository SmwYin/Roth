#!/usr/bin/env python3
"""Read-only validation of the current scratch or integrated factor196 package."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_eq_pow_mul_of_rootMultiplicity'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert a['declaration']==N and a['canonical_index']==196 and a['completed']
assert a['verdict']=='YES-but-generalise-first' and a['allphases']=='PASS'
assert a['phases']==dict.fromkeys(ph,'PASS') and not a['unresolved'] and not v['unresolved']
assert a['root_acceptance'] in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']
assert '∀ {R : Polynomial ℤ} {h : ℤ} {q : ℕ}' in o['type']
assert '∃ (Q : Polynomial ℤ)' in o['type'] and '0 < q' in o['type']
assert o['project_dependencies']==['Roth.isPrimitive_linear','Roth.isPrimitive_pow']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 if '/mathlibable/' in x['destination']:
  p=D/'report.md'
  if not p.exists():p=R/x['destination']
  seen.add('report.md')
 else:p=D/Path(x['destination']).name;seen.add(p.name)
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert len(v['accepted'])==4
for e in v['accepted']:
 r=rd(e['receipt']);assert not r['result'].get('isError',False);z=result(r)
 assert z['success'] and not z.get('timed_out')
 src=D/e['source'];s=src.read_text();assert sha(src)==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s;ds=z['diagnostics']
 else:
  assert z['partial'] is False and not z.get('still_elaborating_lines')
  assert not z.get('failed_dependencies');ds=z['items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message'] for x in ds)):
  assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
 info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
assert len(v['rejected'])>=8
for e in v['rejected']:
 src=D/e['source'];assert src.is_file() and sha(src)==e['source_sha256']
 z=result(rd(e['receipt']));assert not z['success']
 ds=z.get('diagnostics',z.get('items',[]))
 assert any(x.get('severity') in ['error','warning'] for x in ds)
 assert e['reason'] and e['accepted_as_proof'] is False
s=(D/'root-factor196-stronger-executed.lean.txt').read_text()
assert '[IsGCDMonoid A]' in s and '(hcop : IsRelPrime h q)' in s
assert 'let : NormalizedGCDMonoid A := Classical.choice inferInstance' in s
for t in ['theorem generic_nonzero','theorem generic','theorem original_without_hq',
 'theorem no_coprime_dvd','theorem current_form','theorem zero_polynomial',
 'theorem counterexample_multiplicity','fail_if_success']:
 assert t in s
s=(D/'root-factor196-project-executed.lean.txt').read_text()
assert 'theorem caller_pow_rootMultiplicity_le' in s
assert 'Factor196ProjectGCD.original_without_hq (R := R) hcop' in s
assert 'exact generic (K := ℚ) hcop.isRelPrime' in s
assert 'Polynomial.leadingCoeff_mul' in s and 'Int.one_le_abs' in s
assert '[IsGCDMonoid A]' in rd('generic-native-type.json')['native_message']
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('source-hashes.json')
assert len(base)==len(fresh)==17 and set(base)=={x['source'] for x in fresh}
for x in fresh:assert x['matches_baseline'] and x['sha256']==base[x['source']]['sha256']==sha(R/x['source'])
for x in rd('mathlib-inputs.json'):
 p=R/'.lake/packages/mathlib'/x['path']
 assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'] and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Theta.lean')==sha(D/'source-Theta.lean.txt')
assert sha(R/'.mathlib-quality/references/clean.tex')==rd('local-literature.json')['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert len({x['name'] for x in order})==293 and order[195]==rd('canonical-target.json')
assert order[195]['name']==N and order[195]['line']==184
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private'
 else ('public',x['name']) for x in order]
s=(D/v['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.\']+)\s+`([\w.\']+)|`([\w.\']+)",arrays[0])
actual=[('private',mod,nm) if mod else ('public',pub) for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
assert v['canonical_direct_consumers']==['Roth.pow_rootMultiplicity_le']
assert v['canonical_direct_type_consumers']==[]
z=result(rd('root-factor196-original-receipt.json'))
for marker,ns in [('ROOTFACTOR196_DIRECT_CONSUMER: ',v['canonical_direct_consumers']),
 ('ROOTFACTOR196_DIRECT_TYPE_CONSUMER: ',v['canonical_direct_type_consumers'])]:
 assert [x['message'][len(marker):] for x in z['items'] if x['message'].startswith(marker)]==ns
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
f=rd('formal-search.json');assert len(f)==12
assert {(x['form'],x['method']) for x in f}=={(fm,m) for fm in ['current','standard','abstract']
 for m in ['finder','loogle','leansearch','local']}
for x in f:assert not x['response'].get('isError',False)
for fm in ['current','standard','abstract']:assert rd('rg-'+fm+'.json')['exit_code'] in [0,1]
assert sorted(rd('callers.json')['stdout'].splitlines())==sorted(rd('root-factor196-git-callers.json')['stdout'].splitlines())
cs=rd('callers-structured.json');assert len(cs)==1 and cs[0]['declaration']=='Roth.pow_rootMultiplicity_le'
for x in cs:assert x['excerpt']==(R/x['file']).read_text().splitlines()[x['line']-1]
lex=rd('lexical-enumeration.json');assert lex['canonical_entries']==293
assert [x['name'] for x in lex['callers']]==v['canonical_direct_consumers']
qs=[]
for n in ['web-0.json','web-1.json','web-2.json','web-3.json','web-primary.json','web-primary2.json']:
 w=rd(n);assert len(w['response_sha256'])==64 and w['response_bytes']>0
 assert w['status'] and w['urls'] and w['summary'];qs.extend(x['q'] for x in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
 'site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t) for q in qs)
assert len({q for q in qs if not q.startswith('site:')})>=3
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in qs)
assert len(rd('web-primary2.json')['request']['open'])==3
assert not rd('import-layering.json')['reaches_rationalroot']
graph=rd('root-factor196-import-layer-check.json')
assert graph['visited_count']==len(graph['modules'])==1881 and not graph['target_reachable']
assert graph['path'] is None and graph['target'] not in graph['modules']
for name,entry in graph['modules'].items():
 p=R/entry['source'];assert sha(p)==entry['sha256']
 imports=[]
 for line in p.read_text().splitlines():
  hit=re.match(r'^\s*(?:(?:public|private|meta)\s+)*import\s+(.+)$',line)
  if hit:imports.extend(hit[1].split('--',1)[0].strip().split())
 assert sorted({x for x in imports if x.startswith('Mathlib.')})==sorted(entry['imports']),name
 for imp in entry['imports']:
  if imp.startswith('Mathlib.'):assert imp in graph['modules'],imp
seen_graph=set();todo=[graph['start']]
while todo:
 name=todo.pop()
 if name in seen_graph:continue
 seen_graph.add(name)
 todo.extend(x for x in graph['modules'][name]['imports'] if x.startswith('Mathlib.'))
assert seen_graph==set(graph['modules'])

g=rd('accepted-grouping.json')['records'];assert len(g)==2
assert all(x['verdict'].startswith('YES') and x['acceptance']=='PASS' for x in g)
p=json.loads((R/'.mathlib-quality/overview/progress.json').read_text())['completed_declarations']
for x in g:assert x in p
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
assert 'YES-but-generalise-first' in s and 'no ≤3-existing-mathlib-call proof' in s
assert '/generalise '+N in s and '/cleanup Roth/Theta.lean '+N in s
assert v['composition']['strict_three_existing_call_term_verified'] is False
assert v['composition']['parent_project_helpers_counted_as_mathlib_blocks'] is False
assert v['composition']['no_global_absence_claim'] and v['composition']['exact_search_timeout_is_absence_evidence'] is False
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:196; all phases; fresh17; ordered293; 1value/0type; 4clean native; rejected retained;15search cells; fullcaller; current manifest/links/secrets.')
