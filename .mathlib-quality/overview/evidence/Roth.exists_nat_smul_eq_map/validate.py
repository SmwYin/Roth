#!/usr/bin/env python3
"""Portable, read-only declaration171 assessment validation."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_nat_smul_eq_map'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=rd('assessment.json');V=rd('verification.json');O=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert A['declaration']==N and A['canonical_index']==171 and A['completed']
assert A['verdict']=='BORDERLINE-needs-human'
assert A['allphases']=='PASS' and A['phases']==dict.fromkeys(ph,'PASS')
assert A['root_acceptance'] in ['pending','PASS'] and not A['unresolved'] and not V['unresolved']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert O['type']==rd('native-type.json')['type']
for t in ['{σ : Type','(G : MvPolynomial σ ℚ)','(N : ℕ)','(U : MvPolynomial σ ℤ)','0 < N','↑N • G']:assert t in O['type']
assert not any(x in O['type']for x in ['Fintype','DecidableEq','Finite'])
M=rd('copy-manifest.json');assert M['declaration']==N
seen=set()
for x in M['files']:
 p=D/'report.md'if'/mathlibable/'in x['destination']else D/Path(x['destination']).name
 if not p.exists()and'/mathlibable/'in x['destination']:p=R/x['destination']
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
 seen.add('report.md'if'/mathlibable/'in x['destination']else p.name)
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-exclude<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms'])==allowed

def native(e):
 r=rd(e['receipt']);assert not r['result'].get('isError',False)
 z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success']and not z.get('timed_out')
 s=(D/e['source']).read_text();assert sha(D/e['source'])==e['source_sha256']
 if e['format']=='raw':
  assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
  assert '#check_failure '+N in s and len(re.findall(r'^import ',s,re.M))==14
  ds=z['diagnostics']
 else:
  assert z['partial']is False and not z.get('failed_dependencies')and not z.get('still_elaborating_lines')
  ds=z['items']
 assert not[x for x in ds if x.get('severity')in['error','warning']or x.get('category')=='sorry']
 assert not any('sorryAx'in x['message']for x in ds)
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message']for x in ds)):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 info='\n'.join(x['message']for x in ds if x.get('line',0)>=e['native_region_start_line'])
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 return ds
assert len(V['accepted'])==3 and len(V['rejected'])==4
for e in V['accepted']:native(e)
for e in V['rejected']:
 r=rd(e['receipt']);z=r['result']['structuredContent'];z=z.get('result',z)
 assert any(x.get('severity')in['error','warning']for x in z.get('items',z.get('diagnostics',[])))
 assert e['source']not in{x['source']for x in V['accepted']}
inputs=rd('baseline-hashes.json');base=rd('input-manifest.json')['sources_and_pins']
assert len(inputs)==17 and set(base)=={x['path']for x in inputs}
for x in inputs:
 assert x['matches']and x['sha256']==x['expected']==base[x['path']]['sha256']==sha(R/x['path'])
for x in rd('mathlib-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']and sha(D/x['archive'])==sha(p)
assert sha(R/'Roth/Separation.lean')==sha(D/'source-context.lean.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-order.json')and len(order)==293
assert len({x['name']for x in order})==293 and order[170]==rd('canonical-target.json')and order[170]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
s=(D/V['audit']['source']).read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());h=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 terms.append(('private',h[1],h[2])if h else('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/V['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[V['audit']['start_line']-1:])==s.rstrip('\n')
ds=native(V['accepted'][0]);cons=[x['message'].split(': ',1)[1]for x in ds if x.get('line',0)>=13360 and x['message'].startswith('CLEAR_DENOMS171_DIRECT_CONSUMER:')]
assert cons==O['caller_summary']['direct_kernel_value_consumers']==['Roth.exists_primitive_smul_eq']
lex=rd('lexical-enumeration.json');assert {x['path']for x in lex}=={x['file']for x in order}
for f in lex:
 assert sha(R/f['path'])==f['sha256']
 occ=[{'line':i,'text':l}for i,l in enumerate((R/f['path']).read_text().splitlines(),1)if'exists_nat_smul_eq_map'in l]
 assert occ==f['occurrences']
assert sum(len(f['occurrences'])for f in lex)==2
assert O['caller_summary']['explicit_use_count']==1
core=(D/'clear-denoms-combined-executed.lean.txt').read_text()
assert 'theorem clear (G : MvPolynomial σ S)'in core
assert '[CommRing R] [CommRing S] [Algebra R S]'in core
assert 'theorem finiteFamily'in core and '[CommSemiring A] [CommSemiring B]'in core
assert 'Int.natAbs_of_nonneg'in core and 'Int.natAbs_pos'in core and 'smul_eq_C_mul'in core
source=(D/'source-context.lean.txt').read_text()
original=source.split('theorem exists_primitive_smul_eq',1)[1].split('/-- If integers `u_a`',1)[0]
caller=core.split('namespace Clear171Caller',1)[1].split('#print axioms',1)[0]
caller=caller.split('theorem exists_primitive_smul_eq',1)[1]
assert caller.strip()==original.replace('exists_nat_smul_eq_map G','ClearDenoms171.originalProbe171 G').strip()
assert 'theorem zero'in core and 'theorem vacuous'in core
rows=rd('formal-search-receipts.json');assert len(rows)==12
for form in ['current','standard','abstract']:
 for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
  rs=[x for x in rows if x['form']==form and x['method']==method];assert len(rs)==1
  assert not rs[0]['response'].get('isError',False)and rs[0]['args']['query']
cmds=rd('source-search-receipts.json');assert len(cmds)==5
for c in cmds[:3]:assert c['command'][0]=='rg'and c['exit']in[0,1]
for c in cmds[3:]:assert c['exit']==0 and len(c['stdout'].splitlines())>=2
queries=[]
for i in range(1,5):
 w=rd(f'web-{i}-metadata.json');assert len(w['response']['sha256'])==64 and w['response']['bytes']>0
 assert w['status']and not w['body_archived']and w['locators']and w['titles']and w['summary']
 queries.extend(q['q']for q in w['request'].get('search_query',[]))
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ','site:mathoverflow.net ','site:arxiv.org ']:assert any(q.startswith(t)for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-27'in q and'before:2026-10-28'in q for q in queries)
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith('https://'):continue
 prefix='../evidence/'+N+'/'
 assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:171 full phases; fresh17; exact293; accepted native;15 formal cells; exhaustive literature; manifest/links.')
