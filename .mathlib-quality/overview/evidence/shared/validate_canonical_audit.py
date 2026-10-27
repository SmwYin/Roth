#!/usr/bin/env python3
"""Validate a corrected audit's exact canonical order and complete native receipt."""
from pathlib import Path
import hashlib
import json
import re
import sys

root = Path(__file__).resolve().parents[4]
package = Path(sys.argv[1]).resolve()
record = json.loads((package / 'audit-correction.json').read_text())
source = package / record['source']
receipt = package / record['receipt']
assert hashlib.sha256(source.read_bytes()).hexdigest() == record['source_sha256']
assert hashlib.sha256(receipt.read_bytes()).hexdigest() == record['receipt_sha256']
text = source.read_text()
array = re.search(r'let names : Array Lean.Name := #\[(.*?)\]', text, re.S).group(1)
private = r'Lean\.mkPrivateNameCore\s+`([^\s,]+)\s+`([^\s,\]]+)'
array = re.sub(private, lambda m: '`' + m.group(2), array)
actual = re.findall(r'`([^\s,\]]+)', array)
order = json.loads((root / '.mathlib-quality/overview/declaration-order.json').read_text())
expected = [x['name'] for x in order]
assert actual == expected and len(actual) == len(set(actual)) == 293
assert 'names.toList.eraseDups.length == 293' in text
raw = json.loads(receipt.read_text())
result = raw['result']['structuredContent']['result']
assert result['success'] and not result.get('partial') and not result.get('timed_out')
assert not result.get('failed_dependencies') and not raw['result'].get('isError')
items = result['items']
assert not any(x['severity'] in ('error', 'warning') for x in items)
messages = '\n'.join(x['message'] for x in items)
target = record['declaration']
assert ('CORRECTED_CANONICAL ' + target +
        ': unique=293; requested=293; present=293; values=293') in messages
found = re.findall(r'CORRECTED_DIRECT_CONSUMER ' + re.escape(target) + r': ([^\n]+)', messages)
assert found == record['direct_consumers']
print('PASS: exact ordered 293 unique canonical entries and corrected direct audit:', target)
