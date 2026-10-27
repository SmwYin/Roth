"""Read-only validation in scratch or integrated layout; current manifest is authoritative."""
import hashlib
import json
import pathlib
import re
import sys

b = pathlib.Path(__file__).resolve().parent
r = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path.cwd()
t = 'Roth.weight_nonneg'

def read(n):
    return json.loads((b / n).read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

report = b / 'report.md'
if not report.exists():
    report = r / '.mathlib-quality/overview/mathlibable' / (t + '.md')
a = read('assessment.json')
assert a['declaration'] == t and a['canonical_order'] == 31
assert a['file'] == 'Roth/Box.lean' and a['line'] == 75
assert a['verdict'] == 'NO-composable-from-mathlib'
assert a['completed'] and a['unresolved'] == [] and not a['production_edits']
assert a['root_acceptance'] in ['pending', 'PASS']
assert set(a['phases']) == {'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v == 'PASS' or (k == '4.5' and v.startswith('n/a: theorem'))
           for k, v in a['phases'].items())
assert a['composition'] == {'distinct_mathlib_facts': 3, 'expanded_applications': 4,
                             'universal_cast_fact_references': 1,
                             'local_cast_fact_applications': 2}
m = read('input-manifest.json')
assert len(m['sources_and_pins']) == 17
for p, e in m['sources_and_pins'].items():
    assert sha(r / p) == e['sha256'], p
for e in read('source-pin-hashes.json'):
    assert e['match'] and sha(r / e['path']) == e['sha256'] == e['expected_sha256']
for e in read('source-hashes.json'):
    assert sha(r / e['path']) == e['sha256'], e['path']
    assert (r / e['path']).stat().st_size == e['bytes']
assert 'Exit code: 0' in (b / 'baseline-build.txt').read_text()
manifest = read('copy-manifest.json')
assert isinstance(manifest['files'], list) and manifest['files']
for e in manifest['files']:
    assert not pathlib.Path(e['source']).is_absolute()
    p = report if e['source'] == 'report.md' else b / e['source']
    assert p.stat().st_size == e['bytes'] and sha(p) == e['sha256'], e['source']
    expected = ('.mathlib-quality/overview/mathlibable/' + t + '.md'
                if e['source'] == 'report.md' else
                '.mathlib-quality/overview/evidence/' + t + '/' + e['source'])
    assert e['destination'] == expected
v = read('verification.json')
assert v['unresolved'] == [] and len(v['accepted']) == 2
assert v['distinct_existing_library_facts'] == 3
assert v['expanded_instantiated_theorem_applications'] == 4
for e in v['accepted']:
    p = b / e['source']
    code = p.read_text()
    assert sha(p) == e['source_sha256']
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|'
                         r'set_option\s+(maxHeartbeats|maxRecDepth)', code)
    z = read(e['receipt'])
    native = z['result']
    assert not native.get('isError', False)
    sc = native.get('structuredContent', native)
    out = sc.get('result', sc)
    assert out['success'] and not out.get('partial', False)
    assert not out.get('timed_out', False) and not out.get('failed_dependencies')
    ds = out.get('items', out.get('diagnostics', []))
    assert not any(d.get('severity') in ['error', 'warning'] for d in ds)
    if 'code' in z['request']:
        assert z['request']['code'] == code
    c = read(e['source_check'])
    assert c['matched_at_freeze']
    assert c['retained_sha256'] == c['disk_sha256'] == e['source_sha256']
    ax = 0
    for d in ds:
        msg = d.get('message', '')
        assert 'sorryAx' not in msg
        if 'depends on axioms:' in msg:
            names = re.search(r'depends on axioms: \[([^\]]*)\]', msg).group(1).split(',')
            assert {x.strip() for x in names if x.strip()} <= {
                'propext', 'Classical.choice', 'Quot.sound'}
            ax += 1
    assert ax >= 7
raw = (b / 'raw-executed.lean.txt').read_text()
assert 'import Roth' not in raw and '#check_failure Roth.weight_nonneg' in raw
for token in ['theorem original_three_facts', 'theorem finite_nat_sum',
              'theorem finite_functions', 'theorem real_denominators',
              'theorem ordered_field', 'theorem weighted_nonneg',
              'theorem weighted_nonneg_support', 'Finsupp.sum_nonneg\'',
              'nsmul_nonneg', 'Finsupp.weight_apply', '(1 : ℝ) / (-1)']:
    assert token in raw, token
project = (b / 'project-executed.lean.txt').read_text()
for token in ['#check @Roth.weight_nonneg', 'theorem three_named_facts',
              'theorem nonpositive_zero_parameters', 'theorem infimum_image',
              'theorem negative_filter', 'theorem max_caller',
              'Mathlib.Algebra.Order.Archimedean.Real.Basic']:
    assert token in project, token
formal = read('formal-search.json')
assert len(formal) == 12
for method in ['finder', 'loogle', 'leansearch', 'local']:
    for form in ['current', 'standard', 'abstract']:
        rows = [x for x in formal if x['name'] == method + '-' + form]
        assert len(rows) == 1 and rows[0]['request']
        assert not rows[0]['response'].get('isError', False)
for row in formal:
    if row['name'].startswith('local-'):
        assert row['response']['structuredContent']['index'] == 'unavailable'
search = read('source-search.json')
assert len(search) >= 7 and all(x['command'][0] == 'rg' for x in search)
assert read('full-name-source-search.json')['exit_code'] == 1
assert read('cast-source-search.json')['exit_code'] == 0
lit = read('literature-search.json')
assert len(lit) == 8
assert {x['name'] for x in lit} == {'literature-specific', 'literature-general',
    'literature-alias', 'literature-nlab', 'literature-ncatlab',
    'literature-stacks', 'literature-mo', 'literature-arxiv'}
assert len({x['request']['search_query'][0]['q'] for x in lit[:3]}) == 3
for x in lit + [read('literature-open.json')] + read('literature-recent.json'):
    assert x['request'] and x['status'] and x['response_bytes'] > 0
    assert re.fullmatch('[a-f0-9]{64}', x['response_sha256'])
    assert 'response' not in x
c = read('explicit-callers.json')
assert c['count'] == c['declaration_callers'] == len(c['sites']) == 3
assert len(c['external_files']) == 3 and c['inline_audit']
s = report.read_text()
for token in ['Phase 4.5', 'Phase 4.6', 'Phase 5.5', 'Phase 6.0', 'Phase6b',
              'four instantiated theorem applications', 'three distinct existing',
              'application/xhtml+xml', 'ask_chatgpt_math', 'MAXIMALLY GENERAL',
              'zero proof-body lines', 'NO-composable-from-mathlib']:
    assert token in s, token
for link in re.findall(r'\]\(([^)]+)\)', s):
    if link.startswith(('http:', 'https:')):
        continue
    prefix = '../evidence/' + t + '/'
    assert link.startswith(prefix), link
    assert (b / link[len(prefix):]).is_file(), link
print('PASS: all phases;17 source/pin hashes; exact successful native inputs;standard axioms;'
      '5x3 formal methods;all named literature channels;3 callers;3 facts/4 instantiations;'
      'current manifest bytes/hashes and portable links')
