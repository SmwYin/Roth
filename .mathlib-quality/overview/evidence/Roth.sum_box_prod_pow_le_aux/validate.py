#!/usr/bin/env python3
"""Portable read-only validation of a completed private-prefilter assessment."""
from pathlib import Path
import json,hashlib,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.sum_box_prod_pow_le_aux';O=R/'.mathlib-quality/overview'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',s)
report=D/'report.md' if (D/'report.md').exists() else O/'mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==97 and a['completed'] and not a['unresolved']
assert a['mode']=='overview-private-prefilter' and a['verdict']=='SKIP' and a['root_acceptance'] in ['pending','PASS'] and not a['production_edits']
assert all(v=='PASS' or k=='full_mathlibable' and v.startswith('n/a: explicit B1')for k,v in a['phases'].items())
row=load('target-metadata.json');caller=load('caller-metadata.json')
assert row['visibility']=='private' and row['name']==N and row['source'].startswith('private theorem ')
for x in [row,caller]:
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert s==x['source'] and hashlib.sha256(s.encode()).hexdigest()==x['sha256']
assert sha(D/'source-module.lean.txt')==sha(R/row['file'])
assert (D/'target-excerpt.lean.txt').read_text()==row['source']+'\n'
assert (D/'caller-excerpt.lean.txt').read_text()==caller['source']+'\n'
inputs=load('inputs.json');base=load('input-manifest.json')['sources_and_pins'];assert len(inputs)==len(base)==17
for x in inputs:
 p=R/x['path'];assert x['match'] and sha(p)==x['sha256']==x['baseline_sha256']==base[x['path']]['sha256'] and p.stat().st_size==x['bytes']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
assert 'private' in (D/'prefilter-rule.md').read_text() and 'They do NOT get a full Agent run' in (D/'prefilter-rule.md').read_text()
assert load('prefilter-provenance.json')['actual_private']
v=load('verification.json');s=(D/v['source']).read_text();assert sha(D/v['source'])==v['source_sha256'] and v['unresolved']==[] and v['rejected']==[]
assert all(len(l)<=100 for l in s.splitlines())
assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
a_src=row['source'].replace('private theorem sum_box_prod_pow_le_aux','theorem replay',1)
c_src=caller['source'].replace('theorem abs_eval_le','theorem caller',1).replace('sum_box_prod_pow_le_aux','replay')
assert a_src in s and c_src in s and N.split('.')[-1] not in s.split('#check @replay')[0]
r=load(v['receipt']);assert not r['result'].get('isError',False)
z=r['result']['structuredContent']['result'];assert z['success'] and z['partial'] is False and not z.get('timed_out',False) and not z.get('failed_dependencies')
items=z['items'];assert not any(x['severity'] in ['error','warning'] or x.get('category')=='sorry'for x in items)
messages=[x['message']for x in items];msg='\n'.join(messages)
assert not any(w in msg for w in ['sorryAx','PANIC','_inhabitedExprDummy'])
for n in [v['replay'],v['dependent']]:assert "'"+n+"' depends on axioms:"in msg
for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {x.strip()for x in ax.split(',')if x.strip()}<=set(v['standard_axioms'])
fresh=[x['message']for x in items if x['line']>=v['native_region_start_line']]
t1=next(x.split('PRIVATE_BOX_ORIGINAL_TYPE: ',1)[1]for x in fresh if x.startswith('PRIVATE_BOX_ORIGINAL_TYPE: '));t2=next(x.split('@replay : ',1)[1]for x in fresh if x.startswith('@replay : '))
alpha=lambda x:norm(re.sub(r'u_\d+','u',x));assert alpha(t1)==alpha(t2)
assert load('native-type.json')['type']==t1 and load('overview-entry.json')['type']==t1.replace('∈ box r','∈ Roth.box r')
order=json.loads((O/'declaration-order.json').read_text());assert len(order)==293 and len({x['name']for x in order})==293
assert load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[96]
ns=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 ns.append(n)
array='let names : Array Lean.Name := #['+','.join(ns)+']'
assert norm((D/'canonical-array.lean.txt').read_text())==norm(array)
arrays=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S);assert len(arrays)==1 and norm(arrays[0])==norm(array)
assert 'PRIVATE_BOX_AUDIT: requested=293; unique=293'in msg and 'PRIVATE_BOX_VALUES: present=293; values=293'in msg
assert re.findall(r'PRIVATE_BOX_DIRECT_CONSUMER: ([^\n]+)',msg)==['Roth.abs_eval_le'] and 'PRIVATE_BOX_NOT_LOADED:'not in msg
q=load('source-search.json');assert q['command'][0]=='rg' and q['exit_code']==0 and not q['stderr']
assert q['stdout'].count('sum_box_prod_pow_le_aux')==2
for k in ['what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action']:assert load('overview-entry.json')[k]
m=load('copy-manifest.json');assert m['completed']
for x in m['files']:
 p=report if '/mathlibable/'in x['destination'] else D/Path(x['destination']).name
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json','root-review.json'}
assert {p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS declaration97 private prefilter: exact original/replay types; full caller;293 canonical order+unique;17 inputs;current hashes/links/secrets')
