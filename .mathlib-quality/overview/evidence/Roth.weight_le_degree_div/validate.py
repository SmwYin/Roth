#!/usr/bin/env python3
"""Read-only validation of current scratch or integrated weight/degree evidence."""
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path('/Users/ramin/LEAN/Roth')
DECL = 'Roth.weight_le_degree_div'


def read(name):
    return json.loads((HERE / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_destination(destination):
    if destination.endswith('/mathlibable/' + DECL + '.md'):
        scratch = HERE / 'report.md'
        return scratch if scratch.exists() else HERE.parent.parent / 'mathlibable' / (DECL + '.md')
    return HERE / Path(destination).name


def payload(receipt):
    assert not receipt['result'].get('isError', False)
    result = receipt['result']['structuredContent']
    return result.get('result', result)


def native_check(receipt):
    result = payload(receipt)
    assert result['success'] is True
    assert not result.get('partial', False)
    assert not result.get('timed_out', False)
    assert not result.get('failed_dependencies', [])
    for d in result.get('items', result.get('diagnostics', [])):
        assert d.get('severity') not in ['error', 'warning'], d
        message = d.get('message', '')
        assert 'sorryAx' not in message
        match = re.search(r'depends on axioms: \[(.*?)\]', message)
        if match:
            assert {a.strip() for a in match[1].split(',') if a.strip()} <= {
                'propext', 'Classical.choice', 'Quot.sound'}


def main():
    manifest = read('copy-manifest.json')
    rows = manifest['files'] if isinstance(manifest, dict) else manifest
    assert rows
    for row in rows:
        path = local_destination(row['destination'])
        assert path.is_file(), path
        assert sha(path) == row['sha256'], path
        assert path.stat().st_size == row['bytes'], path
    assessment = read('assessment.json')
    assert assessment['declaration'] == DECL and assessment['canonical_order'] == 38
    assert assessment['completed'] is True and assessment['unresolved'] == []
    assert assessment['root_acceptance'] in ['pending', 'PASS']
    assert assessment['verdict'] == 'BORDERLINE-needs-human'
    for phase in ['0', '1', '2', '3', '4a', '4b', '4c', '4.5', '4.6', '5', '5.5', '6.0', '6', '7', '8']:
        assert assessment['phases'][phase] == 'PASS' or assessment['phases'][phase].startswith('n/a:')
    for name, item in read('source-hashes.json').items():
        assert sha(REPO / name) == item['sha256'], name
        assert (REPO / name).stat().st_size == item['bytes'], name
    inputs = read('input-manifest.json')['sources_and_pins']
    assert len(inputs) == 17 and read('input-check.json')['all_17_match'] is True
    assert all(sha(REPO / name) == item['sha256'] for name, item in inputs.items())
    assert 'Exit code: 0' in (HERE / 'baseline-build.txt').read_text()
    verification = read('verification.json')
    assert verification['unresolved'] == []
    for item in verification['accepted']:
        source = HERE / item['source']
        assert sha(source) == item['source_sha256']
        receipt = read(item['receipt'])
        native_check(receipt)
        check = read(item['source_check'])
        assert check['source_sha256'] == sha(source)
        assert check['matches_request_or_current_disk'] is True
        if 'code' in receipt['request']:
            assert source.read_text() == receipt['request']['code']
        else:
            assert check['original_execution_path'] == receipt['request']['file_path']
    native_check(read(verification['supplementary_target_receipt']))
    assert verification['original_distinct_nondefinitional_facts_at_least'] == 5
    assert verification['reaim_existing_law'] is None
    raw = (HERE / verification['accepted'][0]['source']).read_text()
    assert '#check_failure Roth.weight_le_degree_div' in raw
    assert not re.search(r'^import Roth', raw, re.M)
    assert not re.search(r'\b(sorry|unsafe|native_decide|axiom)\b', raw)
    assert '[Semifield K]' in (HERE / 'semifield-executed.lean.txt').read_text()
    assert read('canonical-metadata.json')['canonical_order'] == 38
    assert read('canonical-metadata.json')['actual_source']['line'] == 118
    overview = read('overview-entry.json')
    assert overview['type'].startswith('∀ {σ : Type u}') and '0 < m' in overview['type']
    for i in range(11):
        meta = read(f'web{i}-metadata.json')
        assert meta['request'] and meta['status'] == 'returned'
        assert len(meta['response_sha256']) == 64 and meta['response_bytes'] > 0
        assert all('?' not in x['url'] for x in meta['locators'])
    for method in ['finder', 'loogle', 'leansearch', 'local']:
        for form in ['current', 'literature', 'abstract']:
            assert read(f'{method}-{form}.json')['request']['query']
    report = local_destination('.mathlib-quality/overview/mathlibable/' + DECL + '.md')
    for target in re.findall(r'\]\(([^)]+)\)', report.read_text()):
        if target.startswith('https://'):
            continue
        prefix = '../evidence/' + DECL + '/'
        assert target.startswith(prefix), target
        assert (HERE / target[len(prefix):]).is_file(), target
    assert not assessment['production_edited']
    print('PASS: current manifest, all phases, baseline/hash freshness, exact native sources/receipts, axioms, links')


if __name__ == '__main__':
    main()
