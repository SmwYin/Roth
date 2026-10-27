#!/usr/bin/env python3
"""Read-only audit; runs unchanged in scratch or integrated evidence layout."""
import argparse
import hashlib
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser()
parser.add_argument('--repo', type=Path)
args = parser.parse_args()
base = Path(__file__).resolve().parent
repo = args.repo
if repo is None:
    repo = next((p for p in [Path.cwd(), *base.parents] if (p / 'lakefile.toml').exists()), None)
assert repo is not None, 'Pass --repo to locate source inputs'
repo = repo.resolve()
load = lambda f: json.loads((base / f).read_text())
hash_bytes = lambda b: hashlib.sha256(b).hexdigest()
assessment = load('assessment.json')
assert assessment['declaration'] == 'Roth.wronskianMatrix'
assert assessment['completed'] is True and assessment['allphases'] == 'PASS'
assert assessment['unresolved'] == []
assert assessment['root_acceptance'] in ('pending', 'PASS')
required = {'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert set(assessment['phases']) == required
assert all(assessment['phases'][p] == 'PASS' for p in required)
assert len(assessment['future_api_questions']) <= 5
verification = load('verification.json')
assert verification['unresolved'] == []
for entry in verification['accepted']:
    source = base / entry['source']
    assert hash_bytes(source.read_bytes()) == entry['source_sha256']
    receipt = load(entry['receipt'])
    assert not receipt['result'].get('isError', False)
    data = receipt['result'].get('structuredContent')
    assert data is not None
    while 'result' in data:
        data = data['result']
    assert data.get('success') is True, entry['receipt']
    assert data.get('partial', False) is False
    assert data.get('timed_out', False) is False
    assert not data.get('failed_dependencies', [])
    diagnostics = data.get('items', data.get('diagnostics', []))
    assert not [d for d in diagnostics if d.get('severity') in ('error','warning')]
    axiom_messages = [d['message'] for d in diagnostics if 'depends on axioms:' in d.get('message','')]
    assert axiom_messages
    for message in axiom_messages:
        match = re.search(r'depends on axioms: \[([^\]]*)\]', message)
        assert match, message
        axioms = {a.strip() for a in match[1].split(',') if a.strip()}
        assert axioms <= set(verification['standard_axioms']), message
    code = source.read_text()
    assert not re.search(r'\b(sorry|unsafe|native_decide|axiom)\b', code)
    assert not re.search(r'set_option\s+(maxHeartbeats|maxRecDepth)', code)
    if 'code' in receipt['request']:
        assert code == receipt['request']['code'], entry['source']
        assert '#check_failure Roth.wronskianMatrix' in code
        assert not re.search(r'^import Roth', code, re.M)
inputs = load(verification['inputs'])
assert len(inputs) == 17
for row in inputs:
    data = (repo / row['path']).read_bytes()
    assert hash_bytes(data) == row['sha256'] == row['baseline_sha256']
    assert len(data) == row['bytes'] and row['matches']
for row in load(verification['mathlib_inputs']):
    data = (repo / row['path']).read_bytes()
    assert hash_bytes(data) == row['sha256'] and len(data) == row['bytes']
for source, archived in verification['source_links'].items():
    assert (repo / source).read_bytes() == (base / archived).read_bytes()
formal = load('formal-search-raw.json')
records = formal['first'] + formal['second']
assert len(records) == 12
for record in records:
    assert record['status'] == 'fulfilled'
    assert not record['value']['response'].get('isError', False)
assert {(r['value']['form'],r['value']['method']) for r in records} == {
    (f,m) for f in ('current','standard','abstract') for m in ('Finder','LeanSearch','Loogle','local')}
source_search = load('source-search-raw.json')
assert len(source_search) >= 4
assert source_search[0]['exit_code'] == 1  # exhaustive no-text-hit, not a proof of absence
assert all(r['exit_code'] == 0 for r in source_search[1:4])
web = [load(f) for f in verification['web_metadata']]
assert len(web[0]['request']['search_query']) >= 3
for record in web:
    assert record['status'] == 'success'
    assert re.fullmatch('[0-9a-f]{64}', record['response_sha256'])
    assert record['response_bytes'] > 0
# Current copy-manifest is authoritative, including after root acceptance changes.
manifest = load('copy-manifest.json')
assert manifest['declaration'] == assessment['declaration']
seen = set()
for row in manifest['files']:
    name = Path(row['source']).name
    local = base / name
    if name == 'report.md' and not local.exists():
        local = repo / row['destination']
    assert local.exists(), str(local)
    data = local.read_bytes()
    assert hash_bytes(data) == row['sha256'] and len(data) == row['bytes'], name
    seen.add(local.resolve())
expected = {p.resolve() for p in base.iterdir() if p.is_file() and p.name not in
            ('copy-manifest.json','worker-copy-manifest.json','root-acceptance.json')}
# In integrated layout the report is outside the evidence directory.
assert expected <= seen, 'Supporting artifacts missing from current manifest'
report_path = base / 'report.md'
if not report_path.exists():
    report_path = repo / '.mathlib-quality/overview/mathlibable/Roth.wronskianMatrix.md'
report = report_path.read_text()
for target in re.findall(r'\]\(([^)]+)\)', report):
    if target.startswith('https://'):
        continue
    prefix = '../evidence/Roth.wronskianMatrix/'
    assert target.startswith(prefix), target
    assert (base / target[len(prefix):]).is_file(), target
assert 'Build completed successfully (2467 jobs)' in (base/'baseline-build.txt').read_text()
print(json.dumps({'declaration':assessment['declaration'],'status':'PASS','phases':len(required),
                  'native_accepted':len(verification['accepted']),'source_pin_hashes':len(inputs),
                  'manifest_files':len(manifest['files']),'unresolved':[]},indent=2))
