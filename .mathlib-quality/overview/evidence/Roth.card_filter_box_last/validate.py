#!/usr/bin/env python3
"""Portable read-only validator for scratch and integrated assessment layouts."""
from pathlib import Path
import hashlib,json,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.card_filter_box_last';O=R/'.mathlib-quality/overview'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unwrap(z):
 z=z['result'];z=z.get('structuredContent',z)
 if 'result'in z:z=z['result']
 if 'success'not in z:z=json.loads(z['content'][0]['text'])
 return z
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==127
assert A['completed']and A['unresolved']==[]and A['root_acceptance']in['pending','PASS']
assert not A['production_edits']and A['verdict']=='BORDERLINE-needs-human'
assert set(A['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS'or k=='4.5'and v.startswith('n/a')for k,v in A['phases'].items())
assert 1<=len(A['questions'])<=5
M=read('input-manifest.json')['sources_and_pins'];assert len(M)==17
for x in read('source-hashes.json'):
 p=R/x['path'];assert sha(p)==x['sha256']==M[x['path']]['sha256']and p.stat().st_size==x['bytes']
assert len(read('source-hashes.json'))==17 and '2467 jobs'in(D/'baseline-build.txt').read_text()
assert (D/'Roth-Lattice.lean.txt').read_bytes()==(R/'Roth/Lattice.lean').read_bytes()
assert (D/'Roth-Box.lean.txt').read_bytes()==(R/'Roth/Box.lean').read_bytes()
V=read('verification.json');assert not V['unresolved']and len(V['accepted'])==8
for e in V['accepted']:
 s=(D/e['source']).read_text();assert sha(D/e['source'])==e['source_sha256']and e['source_matches_actual_execution']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s),e['source']
 z=read(e['receipt']);assert not z['result'].get('isError',False)
 out=unwrap(z);assert out['success']and not out.get('timed_out')and not out.get('partial',False)and not out.get('failed_dependencies')
 if e['native_region_start_line']is not None:assert out['partial']is False
 ds=out.get('items',out.get('diagnostics',[]))
 assert not any(x['severity']in['error','warning']or x.get('category')=='sorry'for x in ds)
 msg='\n'.join(x['message']for x in ds)
 assert not any(x in msg for x in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=set(V['standard_axioms'])
 fresh='\n'.join(x['message']for x in ds if e['native_region_start_line']is None or x['line']>=e['native_region_start_line'])
 for name in e['expected_axioms']:assert "'"+name+"' depends on axioms:"in fresh,(e['role'],name)
 if 'code'in z['request']:
  assert z['request']['code']==s and '#check_failure Roth.card_filter_box_last'in s and 'import Roth'not in s
 else:assert z['request']['file_path']==e['original_execution_path']
for e in V['rejected']:
 assert not e['accepted']and(D/e['source']).is_file()and(D/e['receipt']).is_file()
order=json.loads((O/'declaration-order.json').read_text());assert len(order)==293
assert read('canonical-snapshot.json')==order and read('canonical-entry.json')==order[126]
assert order[126]['name']==N
s=(D/'card-filter-box-last-audit-executed.lean.txt').read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
actual=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
assert actual==expected and len(set(actual))==293
out=unwrap(read('card-filter-box-last-original-audit-receipt.json'))
fresh='\n'.join(x['message']for x in out['items']if x['line']>=12976)
assert 'CARD_FILTER_BOX_LAST_AUDIT: requested=293; unique=293'in fresh
assert 'CARD_FILTER_BOX_LAST_AUDIT_PRESENT: present=293; values=293'in fresh
assert re.findall('CARD_FILTER_BOX_LAST_DIRECT_CONSUMER: ([^\n]+)',fresh)==read('canonical-consumers.json')
printed=next(x['message']for x in out['items']if x['line']>=12976 and x['message'].startswith('theorem '+N))
assert printed.split(' : ',1)[1].split(' :=\n',1)[0]==read('native-type.json')['type']==read('overview-entry.json')['type']
assert not read('native-type.json')['kernel_body_elided']
original=(R/'Roth/Lattice.lean').read_text();original=original[original.index('namespace Roth'):]
expected=original.replace('namespace Roth','namespace CardFilterBoxLastReplay\nopen Roth',1).replace('end Roth','end CardFilterBoxLastReplay')
expected=re.sub(r'\bcard_filter_box_last\b','replay',expected)
assert (D/'card-filter-box-last-module-replay-executed.lean.txt').read_text().startswith(expected)
assert read('explicit-callers.json')['count']==1 and read('explicit-callers.json')['external_files']==[]
assert read('full-name-source-search.json')['exit_code']==1
for form in ['current','standard','abstract']:
 q=read('rg-'+form+'.json');assert q['command'][0]=='rg'and q['exit_code']==0 and q['stdout']and not q['stderr']
 for method in ['leanfinder','loogle','leansearch','local_search']:
  q=read('lean_'+method+'-'+form+'.json');assert q['request']['query']and not q['response'].get('isError',False)
assert len(read('formal-search-index.json')['receipts'])==12
queries=[]
for f in ['web-0.json','web-3.json','web-6.json','web-open.json']:
 q=read(f);assert q['response_status']=='returned'and q['response_bytes']>0
 assert re.fullmatch('[a-f0-9]{64}',q['response_sha256'])and q['locator_summary']
 queries.extend(x['q']for x in q['request'].get('search_query',[]))
assert len(set(queries))>=9 and not any('site.ncatlab' in x for x in queries)
channels=read('literature-summary.json')['channels'];assert len(channels)==10
assert {x['channel']for x in channels}>={'nLab','nCatLab','Stacks','MathOverflow','recent arXiv','local clean.tex','ChatGPT math MCP'}
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md'
text=report.read_text()
for token in ['Phase 4.5','Phase 4.6','Phase 5.5','Phase 6.0','Phase6b','BORDERLINE-needs-human','No complete specialization','no complete specialization','1 explicit source occurrence']:
 if token=='No complete specialization':continue
 assert token in text,token
for link in re.findall(r'\]\(([^)]+)\)',text):
 if link.startswith(('https:','http:','#')):continue
 prefix=f'../evidence/{N}/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
manifest=read('copy-manifest.json');assert manifest['completed']
for e in manifest['files']:
 p=report if '/mathlibable/'in e['destination']else D/e['source']
 assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],e['source']
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json','root-review.json'}
assert {p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={e['source']for e in manifest['files']}|{'report.md'}
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: full phases;17 current inputs;8 accepted native sources; standard axioms;293 exact canonical order;5 methods×3 forms; literature;actual caller;current manifest;links;credential guard')
