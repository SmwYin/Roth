#!/usr/bin/env python3
"""Portable, read-only validator for scratch and integrated completed assessment."""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd();N='Roth.exists_genWronskian_ne_zero'
def load(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(rec):
 x=rec['result'];assert not x.get('isError',False);x=x.get('structuredContent') or json.loads(x['content'][0]['text']);return x.get('result',x)
rp=D/'report.md' if (D/'report.md').exists() else R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
a=load('assessment.json');assert a['declaration']==N and a['canonical_index']==119 and a['completed']
assert a['allphases']=='PASS' and a['unresolved']==[] and a['production_unchanged'] and a['root_acceptance'] in ['pending','PASS']
assert a['verdict']=='YES-but-generalise-first' and a['classification']=='BIG'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or (k=='4.5' and v.startswith('n/a: theorem')) for k,v in a['phases'].items())
manifest=load('copy-manifest.json');assert manifest['declaration']==N
for f in manifest['files']:
 p=rp if '/mathlibable/' in f['destination'] else D/Path(f['destination']).name
 assert p.is_file() and sha(p)==f['sha256'] and p.stat().st_size==f['bytes'],p
exempt={'copy-manifest.json','worker-copy-manifest.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt}<={Path(f['destination']).name for f in manifest['files']}|{'report.md'}
b=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());ins=load('inputs.json')
assert ins['baseline_commit']==b['baseline_commit'];rows=ins['fresh_hashes'];assert len(rows)==17 and {x['path'] for x in rows}==set(b['sources_and_pins'])
for x in rows:assert x['sha256']==b['sources_and_pins'][x['path']]['sha256']
for x in rows+load('source-inputs.json'):
 p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
 if x.get('archive'):assert sha(D/x['archive'])==x['sha256']
assert '2467 jobs' in (D/'baseline-build.txt').read_text()
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==load('canonical-snapshot.json')
assert len(order)==293 and len({x['name'] for x in order})==293 and order[118]==load('canonical-entry.json') and order[118]['name']==N
terms=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 terms.append(n)
expected='let names : Array Lean.Name := #['+','.join(terms)+']';norm=lambda s:re.sub(r'\s+','',s)
assert norm((D/'canonical-audit-array.lean.txt').read_text())==norm(expected)
v=load('verification.json');assert v['declaration']==N and v['unresolved']==[] and v['production_unchanged']
assert set(v['standard_axioms'])=={'propext','Classical.choice','Quot.sound'}
assert {x['label'] for x in v['accepted']}=={'original','audit','support-clean','actual-consumer','candidates','jacobian','characteristic-final'}
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
 for name in x['expected_axiom_declarations']:assert "'"+name+"' depends on axioms:" in msg
 if 'code' in rec['request']:assert rec['request']['code']==s and not re.search(r'^import Roth\b',s,re.M) and '#check_failure Roth.exists_genWronskian_ne_zero' in s
 if x['label']=='original':assert N+'.' in msg and '[Field K]' in msg and '[Finite σ]' in msg and '[CharZero K]' in msg
 if x['label']=='audit':
  arrs=re.findall(r'let names : Array Lean.Name := #\[.*?\]',s,re.S);assert len(arrs)==1 and norm(arrs[0])==norm(expected)
  assert 'EXISTS_GEN_WRONSKIAN_AUDIT: requested=293; unique=293' in msg and 'EXISTS_GEN_WRONSKIAN_AUDIT_PRESENT: present=293; values=293' in msg
  actual=[y['message'].split(': ',1)[1] for y in fresh if y.get('message','').startswith('EXISTS_GEN_WRONSKIAN_DIRECT_CONSUMER: ')]
  assert actual==v['canonical_direct_consumers']==['_private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux']
 if x['label']=='support-clean':
  region=s;assert 'theorem arbitrary_variables' in region and '[Finite σ]' not in region
  for token in ['Finset.univ.biUnion','LinearIndependent.of_comp','Finsupp.degree_mapDomain','hasseDeriv_rename','AlgHom.map_det','rename_injective']:
   assert token in region,token
  assert 'ExistsGenSupportProbe.arbitrary_variables' in msg
 if x['label']=='actual-consumer':
  region=s;assert 'ExistsGenSupportProbe.arbitrary_variables hψ' in region
  for token in ['set PQ :=','exists_separated_representation','set F :=','have hFmap','det_hasseDeriv_separated','wronskian_ne_zero_of_linearIndependent']:
   assert token in region,token
 if x['label']=='candidates':
  for token in ['Matrix.det_mvPolynomialX_ne_zero','Polynomial.wronskian','IsCoprime.wronskian_eq_zero_iff']:
   assert token in msg,token
 if x['label']=='jacobian':
  for token in ['Algebra.PreSubmersivePresentation.isUnit_jacobian_of_linearIndependent_of_span_eq_top','Algebra.SubmersivePresentation.linearIndependent_aeval_val_pderiv_relation']:
   assert token in msg,token
 if x['label']=='characteristic-final':assert 'square_mod_two' in msg and 'ZMod 2' in s and 'decide' in s
assert {x['label'] for x in v['rejected']}=={'support','drop-finite','drop-field','composition','characteristic','characteristic-clean'}
for x in v['rejected']:
 assert (D/x['source']).is_file() and x['reason'];rec=load(x['receipt']);assert rec['request']==x['original_execution_request'];nr=native(rec)
 assert any(y.get('severity') in ['error','warning'] for y in nr.get('items',nr.get('diagnostics',[])))
f=load('formal-search-raw.json');assert len(f)==4 and [x['form'] for x in f[:3]]==['current','literature','abstract']
for x in f[:3]:assert len(x['results'])==3 and all(y['status']=='fulfilled' for y in x['results'])
assert f[3]['method']=='Loogle' and len(f[3]['results'])==3
src=load('source-search-raw.json');assert len(src['commands'])==len(src['results'])==5
assert all(x['status']=='fulfilled' and x['value']['exit_code']==0 for x in src['results'])
w=load('web-receipts.json');assert len(w)==6 and len(w[0]['request']['search_query'])==3
for x in w:
 assert len(x['response_sha256'])==64 and x['response_bytes']>0 and x['status'].startswith('returned')
 for u in x['urls']:assert '?' not in u
text=rp.read_text();assert 'PENDING' not in text
for l in re.findall(r'\]\(([^)]+)\)',text):
 if l.startswith('../evidence/'+N+'/'):assert (D/l.split('/')[-1]).is_file(),l
 elif not l.startswith('https://'):raise AssertionError(l)
for token in ['**BIG**','| 9 |','RESTATE-BEFORE-SHIP','STRICTLY NARROWER THAN STANDARD','NOT-COMPOSABLE','/generalise Roth.exists_genWronskian_ne_zero','/cleanup Roth/GenWronskian.lean Roth.exists_genWronskian_ne_zero','Mathlib/RingTheory/MvPolynomial/Wronskian.lean','631b214f7']:
 assert token in text,token
e=load('overview-entry.json');assert e['type'].startswith('@'+N) and '[Field K]' in e['type'] and '[Finite σ]' in e['type'] and '[CharZero K]' in e['type']
review=load('exists-gen-wronskian-reviewer-git.json');assert review['exit_code']==0 and '631b214f7' in review['stdout']
scan=load('secrets-scan.json');assert scan['returncode']==0 and scan['stdout'].startswith('PASS: targeted credential/signed-URL scan')
assert scan['script_sha256']==sha(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py')
# The boundary build receipt is checked as actual execution, independently of baseline reuse.
build=load('gen-wronskian-file-completion-2026-10-27.json');assert build['exit_code']==0 and 'Build completed successfully' in build['stdout'] and build['stderr']==''
assert build['log_sha256']==sha(D/'gen-wronskian-file-completion-2026-10-27.log') and build['command']==['/Users/ramin/.elan/bin/lake','build']
print('PASS: current manifest, full phases,17 pins, exact293 order, verified Finite removal, actual caller, native signatures, rejected drafts,5×3 searches, literature, full boundary build')
