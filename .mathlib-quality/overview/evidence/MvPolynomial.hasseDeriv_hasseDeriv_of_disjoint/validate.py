"""Portable read-only validation of scratch or integrated assessment."""
from pathlib import Path
import hashlib,json,re,sys
b=Path(__file__).resolve().parent
r=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
target='MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint'
report=b/'report.md'
if not report.is_file():report=r/'.mathlib-quality/overview/mathlibable'/(target+'.md')
a=json.loads((b/'assessment.json').read_text())
assert a['declaration']==target and a['completed'] and a['root_acceptance'] in ['pending','PASS'] and a['unresolved']==[]
assert a['verdict']=='YES-add-as-is'
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or v.startswith('N/A:') for v in a['phases'].values())
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
for path,e in json.loads((b/'input-manifest.json').read_text())['sources_and_pins'].items():assert sha(r/path)==e['sha256'],path
for e in json.loads((b/'reference-hashes.json').read_text()):assert sha(r/e['path'])==e['sha256'] and len((r/e['path']).read_bytes())==e['bytes']
for e in json.loads((b/'copy-manifest.json').read_text())['files']:
    f=report if e['source']=='report.md' else b/e['source']
    assert sha(f)==e['sha256'] and len(f.read_bytes())==e['bytes'],e['source']
for link in re.findall(r'\]\(([^)]+)\)',report.read_text()):
    if not link.startswith(('https:','http:')):assert (b/link).is_file(),link
v=json.loads((b/'verification.json').read_text());assert v['unresolved']==[] and len(v['accepted'])==2
axioms=0
for e in v['accepted']:
    code=(b/e['source']).read_text();assert sha(b/e['source'])==e['source_sha256']
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
    d=json.loads((b/e['receipt']).read_text());assert not d['result'].get('isError',False)
    sc=d['result']['structuredContent'];out=sc.get('result',sc)
    assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
    ds=out.get('items',out.get('diagnostics',[]));assert not any(x.get('severity') in ['error','warning'] for x in ds)
    if 'code' in d['request']:assert d['request']['code']==code
    else:
        c=json.loads((b/e['source_check']).read_text());assert c['matched_at_freeze'] and c['retained_sha256']==e['source_sha256']==c['disk_sha256']
    for item in ds:
        msg=item.get('message','');assert 'sorryAx' not in msg
        if 'depends on axioms:' in msg:
            names=re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',')
            assert {x.strip() for x in names if x.strip()}<={'propext','Classical.choice','Quot.sound'};axioms+=1
assert axioms>=10
raw=(b/'raw-executed.lean.txt').read_text();assert 'import Roth' not in raw and 'theorem disjoint' in raw and 'Nat.choose_mul' in raw
assert '#check_failure MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint' in raw and '#check_failure MvPolynomial.hasseDeriv' in raw and '#check_failure MvPolynomial σ S' in raw
final=(b/'final-executed.lean.txt').read_text()
for s in ['theorem scalar_one','theorem bundled','theorem separated_caller','theorem nat_factor_one','theorem swapped','theorem overlap_counterexample','theorem overlap_char_two','theorem lattice_shape']:assert s in final,s
formal=json.loads((b/'formal-search.json').read_text())
for method in ['Finder','LeanSearch','local']:
    for form in ['current','literature','abstract']:assert any(x['method']==method and x['form']==form and not x['result'].get('isError',False) for x in formal)
assert any(x['method']=='Loogle' and x['form'].startswith('abstract') and not x['result'].get('isError',False) for x in formal)
assert len(json.loads((b/'source-search.json').read_text()))>=5
web=json.loads((b/'web-receipts.json').read_text())
assert len({q['q'] for x in web for q in x['request'].get('search_query',[])})>=3
for x in web:assert x['response']['bytes']>0 and re.fullmatch('[a-f0-9]{64}',x['response']['sha256']) and x['summary'] and x['status']
assert len(json.loads((b/'web-sources.json').read_text()))>=7
assert a['upstream']['group_with'] and a['upstream']['reviewer_candidates'] and a['missing_api']
print('PASS: complete phases, hashes/current manifest, exact native sources, zero errors/warnings, standard axioms, five searches and literature metadata')
