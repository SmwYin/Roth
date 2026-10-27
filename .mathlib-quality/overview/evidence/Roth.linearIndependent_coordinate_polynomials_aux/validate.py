#!/usr/bin/env python3
"""Portable read-only private-prefilter validator; no public phases claimed."""
from pathlib import Path
import json,hashlib,re,subprocess,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();O=R/'.mathlib-quality/overview'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=load('assessment.json');N=a['declaration'];index=a['canonical_index'];short=N.split('.')[-1]
assert a['completed'] and not a['unresolved'] and a['verdict']=='SKIP' and a['mode']=='overview-private-prefilter'
assert a['root_acceptance']in['pending','PASS'] and not a['production_edits']
assert all(v=='PASS' or k=='full_mathlibable'and v.startswith('n/a: explicit B1')for k,v in a['phases'].items())
row=load('target-metadata.json');assert row['name']==N and row['visibility']=='private' and row['kind']=='lemma'
assert row['source'].startswith('private lemma '+short)
callers=load('callers.json');assert {x['name']for x in callers}=={x['name']for x in row['project_callers']}
for x in [row]+callers:
 s='\n'.join((R/x['file']).read_text().splitlines()[x['line']-1:x['end_line']]);assert s==x['source']and hashlib.sha256(s.encode()).hexdigest()==x['sha256']
assert (D/'source-module.lean.txt').read_bytes()==(R/row['file']).read_bytes()
assert (D/'target-excerpt.lean.txt').read_text()==row['source']+'\n'
b=load('input-manifest.json')['sources_and_pins'];checks=load('inputs.json');assert len(checks)==len(b)==17
for x in checks:
 p=R/x['path'];assert x['match']and sha(p)==x['sha256']==x['baseline_sha256']==b[x['path']]['sha256'] and p.stat().st_size==x['bytes']
assert '2467 jobs'in(D/'baseline-build.txt').read_text()
assert 'private' in(D/'prefilter-rule.md').read_text()and 'They do NOT get a full Agent run'in(D/'prefilter-rule.md').read_text()
assert load('prefilter-provenance.json')['actual_private']
v=load('verification.json');assert v['declaration']==N and not v['unresolved']and not v['rejected']
s=(D/v['source']).read_text();assert sha(D/v['source'])==v['source_sha256']
assert all(len(l)<=100 for l in s.splitlines())
assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
ns=v['replay_namespace'];original=(R/row['file']).read_text();original=original[original.index('namespace Roth'):]
expected=original.replace('namespace Roth','namespace '+ns,1).replace('end Roth','end '+ns).replace('namespace '+ns,'namespace '+ns+'\nopen Roth',1)
expected=re.sub(r'\b'+short+r'\b','replay',expected).replace('private lemma replay','theorem replay',1)
assert s.startswith(expected+'\n')
whole=(D/v['whole_source']).read_text();assert '\n'.join(whole.splitlines()[v['native_region_start_line']-1:])==s.rstrip('\n')
r=load(v['receipt']);assert not r['result'].get('isError',False)
z=r['result']['structuredContent']['result'];assert z['success']and z['partial']is False and not z.get('timed_out')and not z.get('failed_dependencies')
items=z['items'];assert not any(x['severity']in['error','warning']or x.get('category')=='sorry'for x in items)
msg='\n'.join(x['message']for x in items);assert not any(w in msg for w in ['sorryAx','PANIC','_inhabitedExprDummy'])
for ax in re.findall(r'depends on axioms: \[([^]]*)\]',msg):assert {x.strip()for x in ax.split(',')if x.strip()}<=set(v['standard_axioms'])
fresh='\n'.join(x['message']for x in items if x['line']>=v['native_region_start_line'])
for name in re.findall(r'^(?:noncomputable )?(?:def|theorem) (\w+)',expected,re.M):assert "'"+ns+'.'+name+"' depends on axioms:"in fresh
assert "'_private.Roth.Separation.0."+N+"' depends on axioms:"in fresh
printed=next(x['message']for x in items if x['line']>=v['native_region_start_line']and x['message'].startswith('private theorem '+N))
assert load('native-type.json')['type']==printed.split(' : ',1)[1].split(' :=\n',1)[0]==load('overview-entry.json')['type']
order=json.loads((O/'declaration-order.json').read_text());assert len(order)==293 and load('canonical-snapshot.json')==order and load('canonical-entry.json')==order[index-1]
expected_terms=[]
for x in order:
 expected_terms.append(('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name']))
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
actual=[]
for t in arrays[0].split(','):
 t=' '.join(t.split());m=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
 if m:actual.append(('private',m[1],m[2]))
 else:
  assert re.fullmatch(r'`[^ ]+',t);actual.append(('public',t[1:]))
assert actual==expected_terms and len(set(actual))==293
tag=v['tag'];assert tag+'_AUDIT: requested=293; unique=293'in fresh and tag+'_AUDIT_PRESENT: present=293; values=293'in fresh
assert re.findall(re.escape(tag)+'_DIRECT_CONSUMER: ([^\n]+)',fresh)==load('canonical-consumers.json')
q=load('source-search.json');assert q['exit_code']==0 and not q['stderr']and q['command'][0]=='rg'
e=load('overview-entry.json');assert all(e[k]for k in ['type','what','how','hypotheses','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'])
assert isinstance(e['project_dependencies'],list)
assert set(e['project_dependencies'])==set(row['project_body_refs']+row['project_type_refs'])
report=D/'report.md'if(D/'report.md').exists()else O/'mathlibable'/f'{N}.md'
m=load('copy-manifest.json');assert m['completed']
for x in m['files']:
 p=report if '/mathlibable/'in x['destination']else D/Path(x['destination']).name
 assert p.is_file()and sha(p)==x['sha256']and p.stat().st_size==x['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json','root-review.json'}
assert {p.name for p in D.iterdir()if p.is_file()and p.name not in exempt}<={Path(x['destination']).name for x in m['files']}|{'report.md'}
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
 if link.startswith(('http','#')):continue
 prefix='../evidence/'+N+'/';assert link.startswith(prefix)and(D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(O/'evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS private prefilter:',N,'exact original type/body, complete module replay/axioms, canonical293 order,17 inputs,current evidence')
