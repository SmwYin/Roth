#!/usr/bin/env python3
"""Portable read-only assessment validator; current copy manifest is authoritative."""
from pathlib import Path
import hashlib, json, re, subprocess, sys
D = Path(__file__).resolve().parent
R = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
N = 'Roth.degreeOf_rename_mul_aeval'
def read(n): return json.loads((D / n).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
A = read('assessment.json'); V = read('verification.json'); O = read('overview-entry.json')
ph = ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
assert A['declaration'] == N and A['canonical_index'] == 163 and A['completed']
assert A['verdict'] == 'BORDERLINE-needs-human' and A['allphases'] == 'PASS'
assert A['phases'] == dict.fromkeys(ph, 'PASS') and not A['unresolved'] and not V['unresolved']
assert A['root_acceptance'] in ['pending','PASS'] and 1 <= A['design_questions'] <= 5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
        'moral_duplications','generalization','missing_api','junk','action'} <= set(O)
assert O['type'] == read('native-type.json')['type']
assert O['project_dependencies'] == ['Roth.aeval_X_eq_rename']
for t in [N, 'Type u_1', 'Type u_2', 'CommRing R', 'IsDomain R', '(U : MvPolynomial τ R)']:
    assert t in O['type']
assert not any(t in O['type'] for t in ['Fintype', 'DecidableEq'])
M = read('copy-manifest.json'); assert M['declaration'] == N; seen = set()
for x in M['files']:
    p = D / 'report.md' if '/mathlibable/' in x['destination'] else D / Path(x['destination']).name
    if not p.exists() and '/mathlibable/' in x['destination']: p = R / x['destination']
    assert p.is_file() and sha(p) == x['sha256'] and p.stat().st_size == x['bytes'], p
    seen.add('report.md' if '/mathlibable/' in x['destination'] else p.name)
excluded = {'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file()} - excluded <= seen
assert {'assessment.json','verification.json','overview-entry.json','validate.py'} <= seen
assert not list(D.glob('*.lean'))
allowed = {'propext','Classical.choice','Quot.sound'}
assert set(V['standard_axioms']) == allowed and len(V['accepted']) == 5
def native(e):
    r = read(e['receipt']); assert not r['result'].get('isError', False)
    z = r['result']['structuredContent']; z = z.get('result', z)
    assert z['success'] and not z.get('timed_out')
    s = (D / e['source']).read_text()
    if e['format'] == 'raw':
        assert r['request']['code'] == s
        assert not re.search(r'^import Roth\b', s, re.M)
        assert '#check_failure ' + N in s
        ds = z['diagnostics']
    else:
        assert z['partial'] is False and not z.get('failed_dependencies')
        assert not z.get('still_elaborating_lines')
        assert r['request']['file_path'] == '.lake/roth-overview-session/GenWronskianChecks.lean'
        ds = z['items']
    assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category') == 'sorry']
    assert not any('sorryAx' in x['message'] for x in ds)
    for ax in re.findall(r'depends on axioms: \[([^]]*)\]', '\n'.join(x['message'] for x in ds)):
        assert {x.strip() for x in ax.split(',') if x.strip()} <= allowed
    return ds
for e in V['accepted']:
    assert sha(D / e['source']) == e['source_sha256']
    s = (D / e['source']).read_text()
    assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)', s)
    ds = native(e)
    info = '\n'.join(x['message'] for x in ds if x.get('line', 0) >= e['native_region_start_line'])
    for t in e['required_info']: assert t in info, (e['label'], t)
    if e['label'] != 'canonical-audit': assert 'depends on axioms:' in info
assert len(V['rejected']) == 2
for e in V['rejected']:
    r = read(e['receipt']); z = r['result']['structuredContent']; z = z.get('result', z)
    assert not z['success'] and any(x.get('severity') == 'error' for x in z['diagnostics'])
    assert r['request']['code'] == (D / e['source']).read_text()
    assert e['source'] not in {x['source'] for x in V['accepted']}
base = read('input-manifest.json')['sources_and_pins']; inputs = read('inputs.json')
assert len(inputs) == 17 and set(base) == {x['path'] for x in inputs}
for x in inputs:
    assert x['match'] and x['sha256'] == x['expected_sha256'] == base[x['path']]['sha256']
for x in inputs + read('mathlib-inputs.json'):
    p = R / x['path']; assert sha(p) == x['sha256'] and p.stat().st_size == x['bytes']
for p, q in read('source-links.json').items(): assert sha(R / p) == sha(D / q)
order = json.loads((R / '.mathlib-quality/overview/declaration-order.json').read_text())
assert order == read('canonical-order.json') and len(order) == 293
assert len({x['name'] for x in order}) == 293
assert order[162] == read('canonical-target.json') and order[162]['name'] == N
assert read('corrected-target.json')['line'] == 197
expected = [('private', x['file'][:-5].replace('/','.'), x['name']) if x['visibility'] == 'private'
            else ('public', x['name']) for x in order]
s = (D / V['audit']['source']).read_text()
arrays = re.findall(r'let names : Array Lean.Name := #\[(.*?)\]', s, re.S)
assert len(arrays) == 1; terms = []
for t in arrays[0].split(','):
    t = ' '.join(t.split()); hit = re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)', t)
    terms.append(('private', hit[1], hit[2]) if hit else ('public', t[1:]))
assert terms == expected and len(set(terms)) == 293 and 'let target := `' + N in s
whole = (D / V['audit']['whole_source']).read_text()
assert '\n'.join(whole.splitlines()[V['audit']['start_line'] - 1:]) == s.rstrip('\n')
ds = native(next(x for x in V['accepted'] if x['label'] == 'canonical-audit'))
cons = [x['message'].split(': ', 1)[1] for x in ds if x.get('line', 0) >= 8519
        and x['message'].startswith('SEPARATED_DEGREE163_DIRECT_CONSUMER:')]
assert cons == O['caller_summary']['direct_kernel_value_consumers'] == ['Roth.exists_det_eq_mul']
lex = read('lexical-enumeration.json')
assert {x['path'] for x in lex['files']} == {x['file'] for x in order}
for f in lex['files']:
    assert sha(R / f['path']) == f['sha256']
    occ = [{'line':i,'text':l} for i,l in enumerate((R / f['path']).read_text().splitlines(),1)
           if 'degreeOf_rename_mul_aeval' in l]
    assert occ == f['occurrences']
assert sum(len(f['occurrences']) for f in lex['files']) == 2
for n in ['caller-rg.json','caller-git-grep.json']:
    r = read(n); assert r['exit_code'] == 0 and len(r['stdout'].splitlines()) == 2
assert O['caller_summary']['explicit_use_count'] == 1
assert O['caller_summary']['external_to_file_use_count'] == 0
assert len(O['caller_summary']['explicit_call_sites']) == 1
assert O['caller_summary']['inline_derivations'] == []
s = '\n'.join((D / 'separated-degree-callers-executed.lean.txt').read_text().splitlines()[8836:])
assert 'degreeOf_rename_mul_aeval' not in s
for t in ['theorem exists_det_eq_mul [Finite τ]', 'Lean.mkPrivateNameCore `Roth.Separation',
          'have hdegree', 'Polynomial.toMvPolynomial_eq_rename_comp']:
    assert t in s
rows = read('formal-search.json'); assert len(rows) == 15
for form in ['current','standard','abstract']:
    for method in ['Finder','Loogle','LeanSearch','local','rg']:
        rs = [x for x in rows if x['form'] == form and x['method'] == method]; assert len(rs) == 1
        x = rs[0]
        if method == 'rg': assert read(x['receipt'])['exit_code'] in [0,1]
        else: assert x['request']['query'] and not x['response'].get('isError',False)
for n in ['current','literature','modern','inline']: assert read('rg-' + n + '.json')['exit_code'] in [0,1]
w = read('literature-individual.json'); assert len(w) == 8
queries = []
for x in w:
    assert len(x['response_sha256']) == 64 and x['response_bytes'] > 0 and x['status']
    assert x['body_archived'] is False and x['locators'] and x['titles'] and x['summary']
    assert 'Pending' not in x['summary']
    queries.extend(q['q'] for q in x['request']['search_query'])
for t in ['site:ncatlab.org/nlab ', 'site:ncatlab.org/ncatlab ', 'site:stacks.math.columbia.edu ',
          'site:mathoverflow.net ', 'site:arxiv.org/abs/ ']:
    assert any(q.startswith(t) for q in queries)
assert len({q for q in queries if not q.startswith('site:')}) >= 3
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
assert read('local-literature-search.json')['exit_code'] == 0
assert '2024' in read('literature-availability.json')['recent_primary']
a = read('literature-primary-access.json'); assert len(a) == 4
for x in a:
    assert len(x['response_sha256']) == 64 and x['response_bytes'] > 0 and not x['body_archived']
    assert 'Pending' not in x['summary']
assert a[0]['status'] == 'fetch failed'
b = read(V['full_build']['receipt']); assert b['exit_code'] == 0
assert 'Build completed successfully' in b['output']
assert b['input_hashes'] == {x['path']:x['sha256'] for x in inputs}
assert sha(D / V['full_build']['log']) == b['log_sha256']
s = (D / 'separated-degree-isolated-executed.lean.txt').read_text()
for t in ['theorem semiring', 'theorem abstract_degree_zero', 'theorem nonzeroNecessary',
          'theorem noZeroDivisorsNecessary', '(ℤ × ℤ)', '[CommSemiring R] [NoZeroDivisors R]',
          'by_cases hU : U = 0', 'Polynomial.toMvPolynomial_eq_rename_comp']:
    assert t in s
assert '[Fintype' not in s and '[DecidableEq' not in s
s = (D / 'separated-degree-composition-executed.lean.txt').read_text()
assert s.count('fail_if_success') == 2 and 'theorem normalizationGap' in s
assert 'simpa only [degreeOf_rename_of_injective' in s
report = D / 'report.md'
if not report.exists(): report = R / '.mathlib-quality/overview/mathlibable' / (N + '.md')
s = report.read_text()
for n in ph: assert '## Phase ' + n in s
for link in re.findall(r'\]\(([^)]+)\)',s):
    if link.startswith('https://'): continue
    prefix = '../evidence/' + N + '/'
    assert link.startswith(prefix) and (D / link[len(prefix):]).is_file(), link
subprocess.run([sys.executable, str(R / '.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),
                str(D)], check=True)
print('PASS: all phases; fresh17 inputs; exact293 audit/sole caller; formal15/literature; '
      'native original, semiring proof, two false guards, full caller, composition; hashes/links/secrets.')
