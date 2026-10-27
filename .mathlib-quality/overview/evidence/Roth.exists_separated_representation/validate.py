#!/usr/bin/env python3
"""Portable read-only validator: current manifest is authoritative."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_separated_representation'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=rd('assessment.json');V=rd('verification.json');O=rd('overview-entry.json')
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert A['declaration']==N and A['canonical_index']==168 and A['completed']
assert A['allphases']=='PASS' and A['phases']==dict.fromkeys(ph,'PASS')
assert not A['unresolved'] and not V['unresolved'] and A['root_acceptance'] in ['pending','PASS']
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'}<=set(O)
assert O['type']==rd('native-type.json')['type']
for t in ['φ : Fin l → Polynomial K','ψ : Fin l → MvPolynomial τ K',
          'LinearIndependent K φ','LinearIndependent K ψ','(φ ν).natDegree ≤ n']:
    assert t in O['type']
assert 'Fintype' not in O['type'] and 'DecidableEq' not in O['type']
M=rd('copy-manifest.json');assert M['declaration']==N
seen=set()
for x in M['files']:
    p=D/'report.md' if '/mathlibable/' in x['destination'] else D/Path(x['destination']).name
    if not p.exists() and '/mathlibable/' in x['destination']:p=R/x['destination']
    assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
    seen.add('report.md' if '/mathlibable/' in x['destination'] else p.name)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()}-excluded<=seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'}<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms'])==allowed
def native(e):
    r=rd(e['receipt']);assert not r['result'].get('isError',False)
    z=r['result']['structuredContent'];z=z.get('result',z)
    assert z['success'] and not z.get('timed_out')
    s=(D/e['source']).read_text();assert sha(D/e['source'])==e['source_sha256']
    if e['format']=='raw':
        assert r['request']['code']==s and not re.search(r'^import Roth\b',s,re.M)
        assert '#check_failure '+N in s
        ds=z['diagnostics']
    else:
        assert z['partial'] is False and not z.get('failed_dependencies')
        assert not z.get('still_elaborating_lines')
        ds=z['items']
    assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
    assert not any('sorryAx' in x['message'] for x in ds)
    for ax in re.findall(r'depends on axioms: \[([^]]*)\]','\n'.join(x['message'] for x in ds)):
        assert {x.strip() for x in ax.split(',') if x.strip()}<=allowed
    info='\n'.join(x['message'] for x in ds if x.get('line',0)>=e['native_region_start_line'])
    for t in e['required_info']:assert t in info,(e['label'],t)
    assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
    return ds
assert len(V['accepted'])==10
assert isinstance(O['junk'],str) and O['junk'].startswith('Not junk:')
for e in V['accepted']:native(e)

pid=(D/'separated-repr-isolated-pid-executed.lean.txt').read_text()
fs=(D/'separated-repr-isolated-free-span-executed.lean.txt').read_text()
assert len(re.findall(r'^import ',pid,re.M))==11
assert len(re.findall(r'^import ',fs,re.M))==10
assert 'import Mathlib.LinearAlgebra.FreeModule.PID' in pid
assert '[IsPrincipalIdealRing K]' in pid and '[Module.Free K' not in pid
assert '[Module.Free K' in fs and 'IsPrincipalIdealRing' not in fs
for s in [pid,fs]:
    for t in ['LinearIndependent K φ','LinearIndependent K ψ','(φ ν).natDegree ≤ n',
              '∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P',
              '1 ≤ l ∧ l ≤ n + 1','Polynomial.aeval','rename some (ψ ν)']:
        assert t in s,t
    assert not re.search(r'^import Roth',s,re.M)
caller=(D/'separated-repr-pid-caller-executed.lean.txt').read_text().splitlines()[12336:]
caller='\n'.join(caller)
assert 'Separated168Context.pidRepresentation' in caller
assert 'exists_separated_representation' not in caller
assert 'exists_genWronskian_ne_zero hψ' in caller
assert 'wronskian_ne_zero_of_linearIndependent hφ' in caller

for e in V['rejected']:
    r=rd(e['receipt']);z=r['result']['structuredContent'];z=z.get('result',z)
    ds=z.get('items',z.get('diagnostics',[]))
    assert not z['success'] and any(x.get('severity')=='error' for x in ds)
    assert e['source'] not in {x['source'] for x in V['accepted']}
inputs=rd('inputs.json');base=rd('input-manifest.json')['sources_and_pins']
assert len(inputs)==17 and set(base)=={x['path'] for x in inputs}
for x in inputs:
    assert x['match'] and x['sha256']==x['expected_sha256']==base[x['path']]['sha256']
for x in inputs+rd('mathlib-inputs.json'):
    p=R/x['path'];assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes']
for p,q in rd('source-links.json').items():assert sha(R/p)==sha(D/q)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-order.json') and len(order)==293
assert len({x['name'] for x in order})==293 and order[167]==rd('canonical-target.json')
assert order[167]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name']) if x['visibility']=='private'
          else ('public',x['name']) for x in order]
s=(D/V['audit']['source']).read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S)
assert len(arrays)==1
terms=[]
for t in arrays[0].split(','):
    t=' '.join(t.split());h=re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)',t)
    terms.append(('private',h[1],h[2]) if h else ('public',t[1:]))
assert terms==expected and len(set(terms))==293 and 'let target := `'+N in s
whole=(D/V['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[V['audit']['start_line']-1:])==s.rstrip('\n')
ds=native(next(x for x in V['accepted'] if x['label']=='canonical-audit'))
cons=[x['message'].split(': ',1)[1] for x in ds if x.get('line',0)>=11852 and
      x['message'].startswith('SEPARATED_REPR168_DIRECT_CONSUMER:')]
assert cons==rd('canonical-consumers.json')['consumers']==O['caller_summary']['direct_kernel_value_consumers']
assert cons==['_private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux']
lex=rd('lexical-enumeration.json')
assert {x['path'] for x in lex['files']}=={x['file'] for x in order}
for f in lex['files']:
    assert sha(R/f['path'])==f['sha256']
    occ=[{'line':i,'text':l} for i,l in enumerate((R/f['path']).read_text().splitlines(),1)
         if 'exists_separated_representation' in l]
    assert occ==f['occurrences']
assert sum(len(f['occurrences']) for f in lex['files'])==3
for n in ['caller-rg.json','caller-git-grep.json']:
    r=rd(n);assert r['exit_code']==0 and len(r['stdout'].splitlines())==3
assert O['caller_summary']['explicit_use_count']==1
rows=rd('formal-search.json');assert len(rows)==15
for form in ['current','standard','abstract']:
    for method in ['Finder','Loogle','LeanSearch','local','rg']:
        rs=[x for x in rows if x['form']==form and x['method']==method];assert len(rs)==1
        r=rd(rs[0]['receipt'])
        if method=='rg':assert r['exit_code'] in [0,1]
        else:assert not r.get('response',r).get('isError',False)
w=rd('literature-individual.json');assert len(w)==8
queries=[]
for x in w:
    assert len(x['response_sha256'])==64 and x['response_bytes']>0
    assert x['status'] and not x['body_archived'] and x['locators'] and x['titles'] and x['summary']
    queries.extend(q['q'] for q in x['request']['search_query'])
for t in ['site:ncatlab.org/nlab ','site:ncatlab.org/ncatlab ','site:stacks.math.columbia.edu ',
          'site:mathoverflow.net ','site:arxiv.org/abs/ ']:
    assert any(q.startswith(t) for q in queries)
assert len({q for q in queries if not q.startswith('site:')})>=3
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
assert rd('local-literature-search.json')['exit_code']==0
rp=D/'report.md'
if not rp.exists():rp=R/'.mathlib-quality/overview/mathlibable'/(N+'.md')
s=rp.read_text()
for n in ph:assert '## Phase '+n in s
assert 'PID_RESULT' not in s and 'VERDICT_BLOCK' not in s and 'FULL_NATIVE_TYPE' not in s
for link in re.findall(r'\]\(([^)]+)\)',s):
    if link.startswith('https://'):continue
    prefix='../evidence/'+N+'/'
    assert link.startswith(prefix) and (D/link[len(prefix):]).is_file(),link
subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],check=True)
print('PASS:168 all phases, fresh17, exact293 audit, full statement/both LI/degree/caller native evidence,15 formal cells, literature, manifest/links.')
