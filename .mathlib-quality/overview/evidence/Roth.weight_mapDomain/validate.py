#!/usr/bin/env python3
"""Read-only scratch/integrated validator for Roth.weight_mapDomain."""
from pathlib import Path
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path('/Users/ramin/LEAN/Roth')
DECL = 'Roth.weight_mapDomain'


def read(name):
    return json.loads((HERE / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def destination(row):
    if row['destination'].endswith('/mathlibable/' + DECL + '.md'):
        scratch = HERE / 'report.md'
        return scratch if scratch.exists() else HERE.parent.parent / 'mathlibable' / (DECL + '.md')
    return HERE / Path(row['destination']).name


def payload(receipt):
    result = receipt['result']
    assert not result.get('isError', False)
    data = result['structuredContent']
    data = data.get('result', data)
    assert data['success'] is True
    assert not data.get('partial', False) and not data.get('timed_out', False)
    assert not data.get('failed_dependencies', [])
    for item in data.get('items', data.get('diagnostics', [])):
        assert item.get('severity') not in ['error', 'warning'], item
        msg = item.get('message', '')
        assert 'sorryAx' not in msg
        match = re.search(r'depends on axioms: \[(.*?)\]', msg)
        if match:
            assert {x.strip() for x in match[1].split(',') if x.strip()} <= {
                'propext', 'Classical.choice', 'Quot.sound'}
    return data


def main():
    manifest = read('copy-manifest.json')
    rows = manifest['files'] if isinstance(manifest, dict) else manifest
    for row in rows:
        path = destination(row)
        assert path.is_file(), path
        assert sha(path) == row['sha256'], path
        assert path.stat().st_size == row['bytes'], path
    assessment = read('assessment.json')
    assert assessment['declaration'] == DECL and assessment['completed'] is True
    assert assessment['root_acceptance'] in ['pending', 'PASS']
    assert assessment['unresolved'] == [] and assessment['verdict'] == 'NO-mathlib-has-it'
    for phase in ['0', '1', '2', '3', '4a', '4b', '4c', '4.5', '4.6', '5', '5.5', '6.0', '6', '7', '8']:
        assert assessment['phases'][phase] == 'PASS' or assessment['phases'][phase].startswith('n/a:')
    for name, record in read('source-hashes.json').items():
        path = REPO / name
        assert sha(path) == record['sha256'] and path.stat().st_size == record['bytes'], name
    inputs = read('input-manifest.json')['sources_and_pins']
    assert len(inputs) == 17 and read('input-check.json')['all_17_match'] is True
    for name, record in inputs.items():
        assert sha(REPO / name) == record['sha256'], name
    verification = read('verification.json')
    assert verification['unresolved'] == []
    assert verification['reaim_existing_call_count'] == 1
    assert verification['original_distinct_nondefinitional_facts_lower_bound'] == 4
    assert verification['bridge_definitional'] is False
    for entry in verification['accepted']:
        path = HERE / entry['source']
        assert sha(path) == entry['source_sha256']
        receipt = read(entry['receipt'])
        payload(receipt)
        check = read(entry['source_check'])
        assert check['source_sha256'] == sha(path)
        assert check['matches_request_or_current_disk'] is True
        if 'code' in receipt['request']:
            assert path.read_text() == receipt['request']['code']
        else:
            assert check['original_execution_path'] == receipt['request']['file_path']
    payload(read(verification['supplementary_target_receipt']))
    raw = (HERE / verification['accepted'][0]['source']).read_text()
    assert '#check_failure Roth.weight_mapDomain' in raw
    assert not re.search(r'^import Roth|\b(?:sorry|unsafe|native_decide|axiom)\b', raw, re.M)
    for i in range(10):
        meta = read(f'web{i}-metadata.json')
        assert meta['request'] and meta['status'].startswith('returned')
        assert len(meta['response_sha256']) == 64 and meta['response_bytes'] > 0
    for form in ['current', 'literature', 'abstract']:
        searches = read(f'search-{form}.json')
        assert len(searches['results']) == 4
        assert all(x['status'] == 'fulfilled' for x in searches['results'])
    overview = read('overview-entry.json')
    assert overview['type'].startswith('∀ {σ : Type') and 'Injective f' in overview['type']
    assert overview['caller_summary']['explicit_references'] == 3
    assert read('canonical-metadata.json')['canonical_order'] == 39
    report = destination({'destination': '.mathlib-quality/overview/mathlibable/' + DECL + '.md'})
    for target in re.findall(r'\]\(([^)]+)\)', report.read_text()):
        if target.startswith('https://'):
            continue
        prefix = '../evidence/' + DECL + '/'
        assert target.startswith(prefix), target
        assert (HERE / target[len(prefix):]).is_file(), target
    print('PASS: current manifest, all phases, 17 baseline inputs, source hashes, exact native receipts, standard axioms, links')


if __name__ == '__main__':
    main()
