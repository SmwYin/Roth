#!/usr/bin/env python3
"""Read-only current-package validator for scratch or integrated evidence layouts."""
from pathlib import Path
import argparse, hashlib, json, re

parser = argparse.ArgumentParser()
parser.add_argument('--repo', type=Path, default=Path.cwd())
args = parser.parse_args()
base = Path(__file__).resolve().parent
repo = args.repo.resolve()
report_path = base / 'report.md'
if not report_path.exists():
    report_path = base.parent.parent / 'mathlibable' / 'Roth.abs_eval_le.md'

def artifact_path(name):
    return report_path if name == 'report.md' else base / name

def read(name):
    return json.loads((base / name).read_text())

def sha(data):
    return hashlib.sha256(data).hexdigest()

def diagnostic(raw):
    while 'items' not in raw and 'diagnostics' not in raw:
        assert not raw.get('isError', False), 'native tool error'
        if 'result' in raw:
            raw = raw['result']
        elif 'structuredContent' in raw:
            raw = raw['structuredContent']
        elif 'content' in raw:
            raw = json.loads(raw['content'][0]['text'])
        else:
            raise AssertionError('Unknown native receipt shape')
    if 'diagnostics' in raw:
        raw = {**raw, 'items': raw['diagnostics'], 'partial': raw.get('partial', False)}
    return raw

assessment = read('assessment.json')
assert assessment['declaration'] == 'Roth.abs_eval_le'
assert assessment['completed'] is True
assert assessment['unresolved'] == []
assert assessment['root_acceptance'] in ('pending', 'PASS')
assert all(v == 'PASS' or v.startswith('n/a:') for v in assessment['phases'].values())
manifest = read('copy-manifest.json')
entries = manifest['artifacts']
assert len({e['destination'] for e in entries}) == len(entries)
for e in entries:
    path = artifact_path(e['artifact'])
    b = path.read_bytes()
    assert sha(b) == e['sha256'], e['artifact']
    assert len(b) == e['bytes'], e['artifact']
expected = {e['artifact'] for e in entries if artifact_path(e['artifact']).parent == base}
exempt = {'copy-manifest.json', 'worker-copy-manifest.json', 'root-acceptance.json', 'root-review.json'}
assert {p.name for p in base.iterdir() if p.is_file()} - exempt == expected
inputs = read('input-manifest.json')['sources_and_pins']
assert len(inputs) == 17
for path, meta in inputs.items():
    assert sha((repo / path).read_bytes()) == meta['sha256'], path
assert (base / 'source-module.lean.txt').read_bytes() == (repo / 'Roth/CoeffNorm.lean').read_bytes()
assert (base / 'source-callers.lean.txt').read_bytes() == (repo / 'Roth/MainLemma.lean').read_bytes()

canonical = json.loads((repo / '.mathlib-quality/overview/declaration-order.json').read_text())
names = [{'name':d['name'], 'file':d['file'], 'visibility':d['visibility']} for d in canonical]
assert read('canonical-names.json') == names
assert len(names) == len({d['name'] for d in names}) == 293
expected_terms = []
for d in names:
    if d['visibility'] == 'private':
        expected_terms.append(('private', d['file'].replace('/', '.').removesuffix('.lean'), d['name']))
    else:
        expected_terms.append(('public', d['name']))
for filename in read('verification.json')['canonical_array_sources']:
    code = (base / filename).read_text()
    block = code.split('let names : Array Lean.Name := #[',1)[1].split(']',1)[0]
    actual = []
    for term in block.split(','):
        term = ' '.join(term.split())
        m = re.fullmatch(r'Lean\.mkPrivateNameCore `([^ ]+) `([^ ]+)', term)
        if m:
            actual.append(('private',m[1],m[2]))
        else:
            assert re.fullmatch(r'`[^ ]+',term), term
            actual.append(('public',term[1:]))
    assert actual == expected_terms, filename

verification = read('verification.json')
for item in verification['accepted_native']:
    source = (base / item['source']).read_text()
    assert not re.search(r'\b(sorry|unsafe|native_decide|axiom)\b', source), item['source']
    assert not re.search(r'set_option\s+(maxHeartbeats|maxRecDepth)', source)
    raw = read(item['receipt'])
    diag = diagnostic(raw)
    assert diag.get('success') is True and diag.get('partial') is False
    assert diag.get('timed_out') is False
    assert not diag.get('failed_dependencies')
    assert not [m for m in diag['items'] if m['severity'] in ('error', 'warning')]
    messages = '\n'.join(m['message'] for m in diag['items'])
    assert 'sorryAx' not in messages
    for m in re.finditer(r'depends on axioms: \[([^]]*)\]', messages):
        axioms = {x.strip() for x in m[1].split(',') if x.strip()}
        assert axioms <= {'propext','Classical.choice','Quot.sound'}, axioms
    fresh_items = [m for m in diag['items']
                   if m.get('line', 0) >= item.get('native_region_start_line', 0)]
    fresh_messages = '\n'.join(m['message'] for m in fresh_items)
    for required in item.get('required_messages',[]):
        assert required in fresh_messages, required
report = report_path.read_text()
for link in re.findall(r'\]\(([^)]+)\)', report):
    if link.startswith('https://'):
        continue
    prefix = '../evidence/Roth.abs_eval_le/'
    assert link.startswith(prefix), link
    assert (base / link[len(prefix):]).is_file(), link
assert '∀ {σ : Type' in read('overview-entry.json')['type']
assert 'Draft for independent' not in report
primary = verification['primary_generalization']
code = (base / primary['source']).read_text()
for required in primary['signature_checks']:
    assert required in code, required
assert 'Project declarations unexpectedly loaded' in code
assert all(line.startswith('import Mathlib.') for line in code.splitlines() if line.startswith('import '))
print('PASS: phases, current manifest, all17 source/pins, ordered293 canonical arrays, native success/axioms, links')
