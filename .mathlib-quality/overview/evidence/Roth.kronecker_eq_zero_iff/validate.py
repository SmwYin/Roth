#!/usr/bin/env python3
"""Read-only worker/integrated validator; current manifest is authoritative."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

D = Path(__file__).resolve().parent
R = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
N = 'Roth.kronecker_eq_zero_iff'

def load(n):
    return json.loads((D / n).read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def native(receipt):
    x = receipt['result']
    assert not x.get('isError', False)
    x = x.get('structuredContent') or json.loads(x['content'][0]['text'])
    return x.get('result', x)

def report():
    return D / 'report.md' if (D / 'report.md').exists() else (
        R / '.mathlib-quality/overview/mathlibable' / (N + '.md'))

a = load('assessment.json')
assert a['declaration'] == N and a['canonical_index'] == 110
assert a['verdict'] == 'BORDERLINE-needs-human'
assert a['completed'] and a['allphases'] == 'PASS' and a['unresolved'] == []
assert a['production_unchanged'] and a['root_acceptance'] in ['pending', 'PASS']
assert set(a['phases']) == {'0', '1', '2', '3', '4a', '4b', '4c', '4.5', '4.6', '5',
                            '5.5', '6.0', '6', '7', '8'}
assert all(v == 'PASS' or (k == '4.5' and v.startswith('n/a: theorem'))
           for k, v in a['phases'].items())
assert len(a['questions']) == 3 and a['parent_reaim']['replacement'] == 'MvPolynomial.aeval'
assert a['parent_reaim']['analogous_law_verified'] is False

m = load('copy-manifest.json')
assert m['declaration'] == N
for x in m['files']:
    p = report() if '/mathlibable/' in x['destination'] else D / Path(x['destination']).name
    assert p.is_file() and sha(p) == x['sha256'] and p.stat().st_size == x['bytes'], p
exempt = {'copy-manifest.json', 'worker-copy-manifest.json', 'root-acceptance.json'}
assert {p.name for p in D.iterdir() if p.is_file() and p.name not in exempt} <= {
    Path(x['destination']).name for x in m['files']} | {'report.md'}

baseline = json.loads((R / '.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
xs = load('inputs.json')
assert len(xs) == 17 and {x['path'] for x in xs} == set(baseline['sources_and_pins'])
for x in xs:
    assert x['match'] and x['sha256'] == x['baseline_sha256'] == (
        baseline['sources_and_pins'][x['path']]['sha256'])
for x in xs + load('source-inputs.json'):
    p = R / x['path']
    assert sha(p) == x['sha256'] and p.stat().st_size == x['bytes'], p
    if 'archive' in x:
        assert sha(D / x['archive']) == x['sha256']
assert '2467 jobs' in (D / 'baseline-build.txt').read_text()

order = json.loads((R / '.mathlib-quality/overview/declaration-order.json').read_text())
assert order == load('canonical-snapshot.json') and len(order) == 293
assert len({x['name'] for x in order}) == 293
assert order[109] == load('canonical-entry.json') and order[109]['name'] == N
names = []
for x in order:
    n = '`' + x['name']
    if x['visibility'] == 'private':
        n = 'Lean.mkPrivateNameCore `' + x['file'][:-5].replace('/', '.') + ' ' + n
    names.append(n)
array = 'let names : Array Lean.Name := #[' + ','.join(names) + ']'
norm = lambda s: re.sub(r'\s+', '', s)
assert norm((D / 'canonical-audit-array.lean.txt').read_text()) == norm(array)

v = load('verification.json')
assert v['declaration'] == N and v['unresolved'] == [] and v['production_unchanged']
assert {x['label'] for x in v['accepted']} == {
    'original', 'audit', 'abstract', 'consumer', 'isolated', 'restriction'}
assert set(v['standard_axioms']) == {'propext', 'Classical.choice', 'Quot.sound'}
for x in v['accepted']:
    s = (D / x['source']).read_text()
    assert sha(D / x['source']) == x['source_sha256']
    assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|'
                         r'set_option\s+(maxHeartbeats|maxRecDepth)', s)
    receipt = load(x['receipt'])
    assert receipt['request'] == x['original_execution_request']
    nr = native(receipt)
    assert nr['success'] and not nr.get('timed_out') and not nr.get('failed_dependencies')
    assert not nr.get('partial', False)
    if x['execution_kind'] == 'persistent-disk':
        assert nr['partial'] is False
    ds = nr.get('items', nr.get('diagnostics', []))
    assert not [z for z in ds if z.get('severity') in ['error', 'warning'] or
                z.get('category') == 'sorry']
    txt = '\n'.join(z.get('message', '') for z in ds)
    assert not any(t in txt for t in ['sorryAx', 'PANIC', '_inhabitedExprDummy'])
    for ax in re.findall(r'depends on axioms: \[([^]]*)\]', txt):
        assert {t.strip() for t in ax.split(',') if t.strip()} <= set(v['standard_axioms'])
    fresh = [z for z in ds if z.get('line', 0) >= x['native_region_start_line']]
    msg = '\n'.join(z.get('message', '') for z in fresh)
    for n in x['expected_axiom_declarations']:
        assert "'" + n + "' depends on axioms:" in msg, n
    if 'code' in receipt['request']:
        assert receipt['request']['code'] == s
        assert not re.search(r'^import Roth\b', s, re.M)
    if x['label'] == 'original':
        assert '@Roth.kronecker_eq_zero_iff' in msg and 'Field K' in msg
        assert 'theorem Roth.kronecker_eq_zero_iff' in msg
    if x['label'] == 'audit':
        arrays = re.findall(r'let names : Array Lean.Name := #\[.*?\]', s, re.S)
        assert len(arrays) == 1 and norm(arrays[0]) == norm(array)
        assert 'KRONECKER_ZERO_IFF_AUDIT: requested=293; unique=293' in msg
        assert 'KRONECKER_ZERO_IFF_AUDIT_PRESENT: present=293; values=293' in msg
        actual = [z['message'].split(': ', 1)[1] for z in fresh if z.get('message', '').startswith(
            'KRONECKER_ZERO_IFF_DIRECT_CONSUMER: ')]
        assert actual == v['canonical_direct_consumers'] == ['Roth.linearIndependent_kronecker']
    if x['label'] in ['abstract', 'isolated']:
        assert 'Finsupp.mapDomain_injOn' in s and '[CommSemiring R]' in s
        assert 'KroneckerExpInjOnNoBase.no_base e k' in s
        assert '(hk :' not in s[s.index('namespace KroneckerZeroIffProbe'):]
    if x['label'] == 'isolated':
        assert '#check_failure Roth.kronecker_eq_zero_iff' in s
        assert 'theorem bridge' in s and 'theorem no_base' in s
    if x['label'] == 'consumer':
        assert '(zero_replay (k := k)' in s and '(kronecker_eq_zero_iff' not in s
        assert 'Nat.zero_lt_of_lt hk' in s
    if x['label'] == 'restriction':
        assert 'Finsupp.mapDomain_support_of_injOn P.coeff hi' in s
        assert 'Finsupp.mapDomain_injOn S hi hP hQ' in s
assert [x['declaration_index'] for x in v['prerequisites']] == [108, 109]
assert len(v['rejected']) == 4
for x in v['rejected']:
    assert (D / x['source']).is_file() and x['reason']
    nr = native(load(x['receipt']))
    ds = nr.get('items', nr.get('diagnostics', []))
    assert any(z.get('severity') in ['error', 'warning'] for z in ds)
    if x['label'] == 'absence':
        s = (D / x['source']).read_text()
        assert 'exact?' in s and not re.search(r'^import Roth\b', s, re.M)
        assert '#check_failure Roth.kronecker_eq_zero_iff' in s
        assert any('could not close' in z.get('message', '') for z in ds)
        assert not nr.get('timed_out')

f = load('formal-search.json')
assert len(f) == 12
for method in ['Finder', 'Loogle', 'LeanSearch', 'local']:
    rows = [x for x in f if x['method'] == method]
    assert {x['form'] for x in rows} == {'current', 'standard', 'abstract'}
    assert all('request' in x and 'response' in x and not x['response'].get('isError') for x in rows)
for form in ['current', 'standard', 'abstract', 'callers', 'inline', 'local-literature']:
    x = load('rg-' + form + '.json')
    assert x['exit_code'] in [0, 1] and x['request'][0] == 'rg'
queries = []
for name in ['literature-0.json', 'literature-3.json', 'literature-6.json',
             'literature-direct.json', 'literature-find.json']:
    w = load(name)
    assert len(w['sha256']) == 64 and w['bytes'] > 0 and w['status'] and w['summary']
    assert 'response' not in w and 'result' not in w
    assert all(len(z['title']) <= 200 and '\n' not in z['title'] for z in w['locators'])
    queries += [z['q'] for z in w['request'].get('search_query', [])]
assert len(set(queries[:3])) == 3
for domain in ['site:ncatlab.org/nlab', 'site:ncatlab.org/ncatlab',
               'site:stacks.math.columbia.edu', 'site:mathoverflow.net', 'site:arxiv.org']:
    assert any(domain in q for q in queries)
assert any('after:2021-10-27' in q and 'before:2026-10-28' in q for q in queries)
c = load('callers.json')
assert c['named_count'] == 1 and c['callers'] == ['Roth.linearIndependent_kronecker']
assert c['external_to_declaring_file'] == 0 and c['inline_rederivations'] == []
o = load('overview-entry.json')
assert o['type'].startswith('∀') and 'Field K' in o['type'] and '1 < k' in o['type']
assert all(x['verdict'].startswith('YES') for x in load('accepted-yes.json'))
assert any(x['declaration'] == 'Roth.kroneckerExp_injOn' for x in load('accepted-yes.json'))
s = report().read_text()
for t in ['## Phase 8', 'BORDERLINE-needs-human', 'SMALL', 'RESTATE-BEFORE-SHIP',
          '293', 'MathOverflow', 'nCatLab', 'arXiv', 'Automatic NO parent gate',
          'mapDomain_injOn', 'mapDomain_support_of_injOn']:
    assert t in s, t
for link in re.findall(r'\]\(([^)]+)\)', s):
    if link.startswith('http'):
        continue
    prefix = '../evidence/' + N + '/'
    assert link.startswith(prefix), link
    assert (D / link[len(prefix):]).is_file(), link
r = subprocess.run(['python3', str(R / '.mathlib-quality/overview/evidence/shared/'
    'scan_evidence_secrets.py'), str(D)], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
print('PASS: all phases;17 inputs;6 clean native sources;isolated prerequisites;canonical293;'
      'sole caller;all search methods/channels;current manifest;links;secret guard')
