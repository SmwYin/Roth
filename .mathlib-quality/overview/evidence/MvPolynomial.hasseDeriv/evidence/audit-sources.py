from pathlib import Path
import json,re,hashlib,subprocess
root=Path.cwd()
out=Path(__file__).resolve().parent
manifest=json.load(open(out/'caller-boundaries.json'))
def strip_comments(s):
    r=[]; i=0; depth=0; line=False; string=False
    while i<len(s):
        c=s[i]; pair=s[i:i+2]
        if line:
            if c=='\n': line=False; r.append(c)
            else: r.append(' ')
            i+=1
        elif depth:
            if pair=='/-': depth+=1; r.extend('  '); i+=2
            elif pair=='-/': depth-=1; r.extend('  '); i+=2
            else: r.append('\n' if c=='\n' else ' '); i+=1
        elif string:
            r.append(c)
            if c=='\\' and i+1<len(s): r.append(s[i+1]); i+=2
            else:
                if c=='"': string=False
                i+=1
        elif pair=='/-': depth=1; r.extend('  '); i+=2
        elif pair=='--': line=True; r.extend('  '); i+=2
        else:
            r.append(c)
            if c=='"': string=True
            i+=1
    return ''.join(r)
pat=re.compile(r'(?<![\w.])(?:MvPolynomial\.)?hasseDeriv\b')
rows=[]; excluded=[]
for p in sorted((root/'Roth').glob('*.lean')):
    rel=str(p.relative_to(root)); original=p.read_text().splitlines()
    for n,line in enumerate(strip_comments(p.read_text()).splitlines(),1):
        hits=list(pat.finditer(line))
        if not hits: continue
        if rel=='Roth/HasseDeriv.lean' and n==57: continue
        decl=next((x for x in manifest if x['file']==rel and x['line']<=n<=x['end_line']),None)
        entry=dict(file=rel,line=n,caller=decl['name'] if decl else None,excerpt=original[n-1].strip(),occurrences=len(hits))
        if rel=='Roth/Wronskian.lean':
            entry['reason']='Univariate Polynomial.hasseDeriv: K[X] arguments and open Polynomial; not the assessed operator.'
            excluded.append(entry)
        else: rows.append(entry)
external=[x for x in rows if x['file']!='Roth/HasseDeriv.lean']
summary=dict(code_lines=len(rows),occurrences=sum(x['occurrences'] for x in rows),caller_declarations=len(set(x['caller'] for x in rows)),external_code_lines=len(external),external_occurrences=sum(x['occurrences'] for x in external),external_caller_declarations=len(set(x['caller'] for x in external)),external_files=len(set(x['file'] for x in external)))
json.dump(dict(provenance='Actual code grep after nested/line comment stripping; qualified Polynomial hits excluded lexically, unqualified Wronskian hits disambiguated by source; canonical manifest used only for caller boundaries. Direct explicit references, not opaque/simp dependency closure.',summary=summary,rows=rows,excluded=excluded),open(out/'call-sites.json','w'),indent=2)
with open(out/'caller-table.md','w') as f:
    f.write('| File:line | Caller | Actual code excerpt |\n|---|---|---|\n')
    for x in rows: f.write('| `'+x['file']+':'+str(x['line'])+'` | `'+x['caller']+'` | `'+x['excerpt'].replace('|','\\|')+'` |\n')
print(json.dumps(summary,indent=2))
