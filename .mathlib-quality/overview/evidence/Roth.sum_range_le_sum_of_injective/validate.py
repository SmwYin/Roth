#!/usr/bin/env python3
"""Read-only validation of scratch or integrated assessment; current manifest is authoritative."""
import hashlib
import json
from pathlib import Path
import re
import sys

NAME = 'Roth.sum_range_le_sum_of_injective'
HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()

def read(name):
    return json.loads((HERE / name).read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def nodes(value):
    yield value
    if isinstance(value, dict):
        for val in value.values():
            yield from nodes(val)
    elif isinstance(value, list):
        for val in value:
            yield from nodes(val)

assessment = read('assessment.json')
assert assessment['declaration'] == NAME
assert assessment['completed'] is True and assessment['allphases'] == 'PASS'
assert assessment['unresolved'] == []
assert assessment['root_acceptance'] in ('pending', 'PASS')
phases = ['0', '1', '2', '3', '4a', '4b', '4c', '4.5', '4.6', '5', '5.5', '6.0', '6', '7', '8']
assert all(assessment['phases'][phase] == 'PASS' for phase in phases)

manifest = read('copy-manifest.json')  # Never substitute historical worker-copy-manifest.json.
seen = set()
for item in manifest['files']:
    destination = Path(item['destination'])
    basename = destination.name
    if '/mathlibable/' in item['destination']:
        path = HERE / 'report.md' if (HERE / 'report.md').exists() else ROOT / destination
    else:
        path = HERE / basename
    assert path.exists(), path
    assert digest(path) == item['sha256'], path
    assert path.stat().st_size == item['bytes'], path
    seen.add(basename)
assert {'assessment.json', 'verification.json', 'validate.py', NAME + '.md'} <= seen

verification = read('verification.json')
assert verification['unresolved'] == []
allowed = set(verification['standard_axioms'])
assert allowed == {'propext', 'Classical.choice', 'Quot.sound'}
for accepted in verification['accepted']:
    source = HERE / accepted['source']
    assert digest(source) == accepted['source_sha256']
    text = source.read_text()
    assert not re.search(r'\b(?:sorry|admit|native_decide|unsafe)\b|\baxiom\s|set_option\s+(?:maxHeartbeats|maxRecDepth)', text)
    receipt = read(accepted['receipt'])
    assert receipt['result'].get('isError') is not True
    payloads = [n for n in nodes(receipt['result']) if isinstance(n, dict) and n.get('success') is True]
    assert payloads, accepted
    for payload in payloads:
        assert payload.get('partial', False) is False
        assert payload.get('timed_out', False) is False
        assert not payload.get('failed_dependencies')
        diagnostics = payload.get('diagnostics', payload.get('items', []))
        assert not [d for d in diagnostics if d.get('severity') in ('error', 'warning') or d.get('category') == 'sorry']
        messages = '\n'.join(d.get('message', '') for d in diagnostics)
        axioms = re.findall(r'depends on axioms: \[([^]]*)\]', messages)
        assert axioms
        for axiom in axioms:
            assert {a.strip() for a in axiom.split(',') if a.strip()} <= allowed
    if accepted['label'] == 'isolated':
        assert receipt['request']['code'] == text
        assert not re.search(r'^import Roth\b', text, re.M)
        assert '#check_failure ' + NAME in text

inputs = read(verification['inputs'])
assert len(inputs) == 17
for item in inputs + read(verification['mathlib_inputs']):
    path = ROOT / item['path']
    assert path.exists() and digest(path) == item['sha256'], path
    assert path.stat().st_size == item['bytes']
for original, archived in verification['source_links'].items():
    assert digest(ROOT / original) == digest(HERE / archived)

report = HERE / 'report.md'
if not report.exists():
    report = ROOT / '.mathlib-quality/overview/mathlibable' / (NAME + '.md')
prefix = '../evidence/' + NAME + '/'
for target in re.findall(r'\]\(([^)]+)\)', report.read_text()):
    if target.startswith('https://'):
        continue
    assert target.startswith(prefix), target
    assert (HERE / target[len(prefix):]).exists(), target
formal = read('formal-search.json')
assert len(formal) == 12 and all(x['status'] == 'fulfilled' for x in formal)
web = read('literature-web.json')
queries = [q['q'] for x in web for q in x['request'].get('search_query', [])]
assert len(set(queries)) >= 11
assert all(len(x['response_sha256']) == 64 and x['response_bytes'] > 0 for x in web)
assert all(x['archive_policy'] for x in web)
print('PASS: current manifest, all 15 phases, native success/axioms, sources/pins, links, search receipts')
