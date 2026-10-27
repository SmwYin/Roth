#!/usr/bin/env python3
"""Read-only validation of scratch or integrated Roth.weight_le_card evidence."""
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
REPO = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path('/Users/ramin/LEAN/Roth')


def read(name):
    return json.loads((HERE / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_destination(destination):
    if destination.endswith('/mathlibable/Roth.weight_le_card.md'):
        scratch = HERE / 'report.md'
        return scratch if scratch.exists() else HERE.parent.parent / 'mathlibable/Roth.weight_le_card.md'
    return HERE / Path(destination).name


def main():
    manifest = read('copy-manifest.json')
    rows = manifest['files'] if isinstance(manifest, dict) else manifest
    for row in rows:
        path = local_destination(row['destination'])
        assert path.is_file(), path
        assert sha(path) == row['sha256'], path
        assert path.stat().st_size == row['bytes'], path
        if path.name != 'validate.py':
            assert not re.search(r'(?:AKIA|ASIA)[A-Z0-9]{16}|(?i:X-Amz-(?:Credential|Signature|Security-Token)|AWSAccessKeyId|[?&](?:token|access_token|signature)=)', path.read_text()), path
    assessment = read('assessment.json')
    assert assessment['declaration'] == 'Roth.weight_le_card'
    assert assessment['completed'] is True and assessment['unresolved'] == []
    assert assessment['root_acceptance'] in ['pending', 'PASS']
    phases = assessment['phases']
    for phase in ['0', '1', '2', '3', '4a', '4b', '4c', '4.5', '4.6', '5', '5.5', '6.0', '6', '7', '8']:
        assert phases[phase] == 'PASS' or phases[phase].startswith('n/a:'), phase
    assert assessment['verdict'] == 'BORDERLINE-needs-human'
    for name, entry in read('source-hashes.json').items():
        assert sha(REPO / name) == entry['sha256'], name
        assert (REPO / name).stat().st_size == entry['bytes'], name
    for name, entry in read('input-manifest.json')['sources_and_pins'].items():
        assert sha(REPO / name) == entry['sha256'], name
    verification = read('verification.json')
    assert verification['unresolved'] == []
    for item in verification['accepted']:
        source = HERE / item['source']
        assert sha(source) == item['source_sha256']
        receipt = read(item['receipt'])
        result = receipt['result']
        assert not result.get('isError', False)
        payload = result['structuredContent']
        payload = payload.get('result', payload)
        assert payload['success'] is True
        assert not payload.get('partial', False)
        assert not payload.get('timed_out', False)
        assert not payload.get('failed_dependencies', [])
        diagnostics = payload.get('items', payload.get('diagnostics', []))
        assert all(d.get('severity') not in ['error', 'warning'] for d in diagnostics)
        for d in diagnostics:
            message = d.get('message', '')
            assert 'sorryAx' not in message
            match = re.search(r'depends on axioms: \[(.*?)\]', message)
            if match:
                axioms = {x.strip() for x in match[1].split(',') if x.strip()}
                assert axioms <= {'propext', 'Classical.choice', 'Quot.sound'}, axioms
        check = read(item['source_check'])
        assert check['source_sha256'] == sha(source)
        assert check['matches_request_or_current_disk'] is True
        if 'code' in receipt['request']:
            assert source.read_text() == receipt['request']['code']
        else:
            assert check['original_execution_path'] == receipt['request']['file_path']
    raw = (HERE / verification['accepted'][0]['source']).read_text()
    assert '#check_failure Roth.weight_le_card' in raw
    assert not re.search(r'^import Roth', raw, re.M)
    assert not re.search(r'\b(sorry|unsafe|native_decide|axiom)\b', raw)
    report = local_destination('.mathlib-quality/overview/mathlibable/Roth.weight_le_card.md')
    for target in re.findall(r'\]\(([^)]+)\)', report.read_text()):
        if target.startswith('https://'):
            continue
        prefix = '../evidence/Roth.weight_le_card/'
        assert target.startswith(prefix), target
        assert (HERE / target[len(prefix):]).is_file(), target
    print('PASS: current manifest, phases, hashes, exact native sources/receipts, axioms, links')


if __name__ == '__main__':
    main()
