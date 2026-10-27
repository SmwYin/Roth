#!/usr/bin/env python3
"""Read-only assessment validator, portable between scratch and integrated layouts."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();O=R/'.mathlib-quality/overview';N='Roth.card_filter_weight_le'
def read(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unwrap(z):
 z=z['result'];z=z.get('structuredContent',z);z=z.get('result',z)
 if 'success'not in z:z=json.loads(z['content'][0]['text'])
 return z
A=read('assessment.json');assert A['declaration']==N and A['canonical_index']==132 and A['completed']and not A['production_edits']
assert A['unresolved']==[]and A['root_acceptance']in['pending','PASS']and A['verdict']=='BORDERLINE-needs-human'
assert set(A['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS'or k=='4.5'and v.startswith('n/a')for k,v in A['phases'].items())and 1<=len(A['questions'])<=5
I=read('input-manifest.json')['sources_and_pins'];H=read('source-hashes.json');assert len(I)==len(H)==17
assert {x['path']for x in H}==set(I)
for x in H:
 p=R/x['path'];assert sha(p)==x['sha256']==I[x['path']]['sha256']and p.stat().st_size==x['bytes'],x['path']
for n in ['Lattice','Box','MainLemma']:assert(D/f'Roth-{n}.lean.txt').read_bytes()==(R/f'Roth/{n}.lean').read_bytes()
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
B=read('lattice-file-completion-2026-10-27.json');assert B['exit_code']==0 and B['command']==['lake','build']and B['stderr']==''
log=D/'lattice-file-completion-2026-10-27.log';assert sha(log)==B['log_sha256']and log.stat().st_size==B['log_bytes']and '2467 jobs'in log.read_text()
for x in read('candidate-source-hashes.json'):
 p=R/x['path'];assert sha(p)==x['sha256']and p.stat().st_size==x['bytes']
V=read('verification.json');assert V['unresolved']==[]and len(V['accepted'])==8 and len(V['rejected'])==6
for e in V['accepted']:
 s=(D/e['source']).read_text();assert sha(D/e['source'])==e['source_sha256']and e['source_matches_actual_execution']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s),e['source']
 z=read(e['receipt']);assert not z['result'].get('isError',False);o=unwrap(z)
 assert o['success']and not o.get('timed_out')and not o.get('partial',False)and not o.get('failed_dependencies'),e['source']
 if e['execution_kind']=='persistent-disk':assert o['partial']is False and e['native_region_start_line']is not None
 ds=o.get('items',o.get('diagnostics',[]));assert not any(x['severity']in['warning','error']or x.get('category')=='sorry'for x in ds),e['source']
 msg='\n'.join(x['message']for x in ds);assert not any(t in msg for t in ['sorryAx','PANIC','_inhabitedExprDummy'])
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {a.strip()for a in ax.split(',')if a.strip()}<=set(V['standard_axioms'])
 fresh='\n'.join(x['message']for x in ds if e['native_region_start_line']is None or x.get('line',0)>=e['native_region_start_line'])
 for name in e['expected_axioms']:assert "'"+name+"' depends on axioms:"in fresh,(e['role'],name)
 if 'code'in z['request']:assert z['request']['code']==s and '#check_failure Roth.card_filter_weight_le'in s and 'import Roth'not in s
 else:assert z['request']['file_path']==e['original_execution_path']
for e in V['rejected']:assert e['accepted']is False and sha(D/e['source'])==e['source_sha256']and(D/e['receipt']).is_file()and e['reason']
for e in V['additional_positive']:assert unwrap(read(e['receipt']))['success']and(D/e['source']).is_file()
order=json.loads((O/'declaration-order.json').read_text());assert len(order)==293 and read('canonical-snapshot.json')==order and read('canonical-entry.json')==order[131]and order[131]['name']==N
src=(D/'card-filter-weight-le-audit-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',src,re.S);assert len(arrays)==1
actual=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
assert actual==expected and len(set(actual))==293
out=unwrap(read('card-filter-weight-le-original-audit-receipt.json'));start=int((D/'card-filter-weight-le-audit-region.txt').read_text());fresh='\n'.join(x['message']for x in out['items']if x['line']>=start)
assert 'CARD_FILTER_WEIGHT_LE_AUDIT: requested=293; unique=293'in fresh and 'CARD_FILTER_WEIGHT_LE_AUDIT_PRESENT: present=293; values=293'in fresh
assert re.findall(r'CARD_FILTER_WEIGHT_LE_DIRECT_CONSUMER: ([^\n]+)',fresh)==read('canonical-consumers.json')==V['canonical_direct_consumers']
start=int((D/'card-filter-weight-le-original-region.txt').read_text());printed=next(x['message']for x in out['items']if x['line']>=start and x['message'].startswith('theorem '+N))
assert printed.split(' : ',1)[1].split(' :=\n',1)[0]==read('native-type.json')['type']==read('overview-entry.json')['type']
assert read('native-type.json')['kernel_body_elided']==('LEAN_MCP_MAX_OUTPUT_CHARS'in printed)
assert read('explicit-callers.json')['count']==1 and read('explicit-callers.json')['external_files']==['Roth/MainLemma.lean']
assert read('rg-full-name.json')['exit_code']==1
for form in ['current','literature','abstract']:
 q=read('rg-'+form+'.json');assert q['command'][0]=='rg'and q['exit_code']in[0,1]and not q['stderr']and q['untruncated']
 q=read('local-'+form+'.json');assert q['query']and not q['response'].get('isError',False)
idx=read('formal-search-index.json')['receipts'];assert len(idx)==12
for form in ['current','literature','abstract']:assert {x['method']for x in idx if x['form']==form}=={'lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search'}
for form in ['literature','abstract']:
 for x in read('search-'+form+'.json'):assert x['query']and not x['response'].get('isError',False)
assert set(read('search-current.json'))=={'lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search'}
for x in read('search-current.json').values():assert not x.get('isError',False)
queries=[]
for i in range(1,9):
 w=read(f'web{i}-metadata.json');assert w['response_bytes']>0 and re.fullmatch('[a-f0-9]{64}',w['response_sha256'])and w['locator_summary']
 req=w['request'];queries.extend(x['q']for x in(req.get('search_query',[])if isinstance(req,dict)else req))
assert len(set(queries))>=3 and any('site:ncatlab.org/ncatlab 'in x for x in queries)
channels=read('literature-summary.json')['channels'];assert len(channels)==10 and {x['channel']for x in channels}>={'nLab','nCatLab','Stacks','MathOverflow','recent arXiv','local clean.tex','ChatGPT math MCP'}
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md';txt=report.read_text();assert '@@NATIVE_TYPE@@'not in txt
for t in ['BIG','Phase 4.5','Phase 4.6','Phase 5.5','Phase 6.0','Phase6b','BORDERLINE-needs-human','no complete specialization','LEAN_MCP_MAX_OUTPUT_CHARS','DecidableEq σ','1 explicit source occurrence']:assert t in txt,t
for k in range(1,10):assert re.search(r'\|'+str(k)+r' ',txt),'modern row'+str(k)
for link in re.findall(r'\]\(([^)]+)\)',txt):
 if link.startswith(('https:','http:','#')):continue
 prefix=f'../evidence/{N}/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
manifest=read('copy-manifest.json');assert manifest['completed']and manifest['declaration']==N
for e in manifest['files']:
 p=report if '/mathlibable/'in e['destination']else D/e['source'];assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],e['source']
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json','root-review.json'}
assert {p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={x['source']for x in manifest['files']}|{'report.md'}
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS: phases;17 current inputs;fresh full build;8 accepted native sources;standard axioms;293 exact ordered canonical names;5 methods x3 forms;all named literature;actual caller;current manifest;links;secret guard')
