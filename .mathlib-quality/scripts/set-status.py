#!/usr/bin/env python3
"""usage: set-status.py TICKET STATUS [progress note]"""
import sys, re, datetime
tid, status = sys.argv[1], sys.argv[2]
note = sys.argv[3] if len(sys.argv) > 3 else None
p = '.mathlib-quality/tickets.md'
s = open(p).read()
start = s.index(f'### [{tid}]')
nxt = s.find('\n### [', start + 1)
end = nxt if nxt != -1 else len(s)
block = s[start:end]
block = re.sub(r'^- \*\*Status\*\*: .*$', f'- **Status**: {status}', block, count=1, flags=re.M)
if note:
    ts = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
    if '**Progress**:' in block:
        block = block.rstrip('\n') + f'\n- {ts}: {note}\n\n'
    else:
        block = block.rstrip('\n') + f'\n\n**Progress**:\n- {ts}: {note}\n\n'
s = s[:start] + block + s[end:]
open(p, 'w').write(s)
print(tid, '->', status)
