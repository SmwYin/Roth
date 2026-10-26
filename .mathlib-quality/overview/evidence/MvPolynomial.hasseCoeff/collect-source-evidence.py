#!/usr/bin/env python3
"""Read-only project inventory, preserving code positions while removing Lean comments."""
import hashlib,json,pathlib,re,subprocess
root=pathlib.Path.cwd(); here=pathlib.Path(__file__).resolve().parent
# Nested block comments and line comments removed; strings preserved (none in target expressions).
def strip(s):
    out=[];i=0;depth=0
    while i<len(s):
        if depth:
            if s[i:i+2]=='/-':depth+=1;out+=[' ',' '];i+=2
            elif s[i:i+2]=='-/':depth-=1;out+=[' ',' '];i+=2
            else:out.append('\n' if s[i]=='\n' else ' ');i+=1
        elif s[i:i+2]=='/-':depth=1;out+=[' ',' '];i+=2
        elif s[i:i+2]=='--':
            while i<len(s) and s[i]!='\n':out.append(' ');i+=1
        else:out.append(s[i]);i+=1
    return ''.join(out)
rows=[]
for p in sorted(root.glob('Roth/**/*.lean')):
    lines=p.read_text().splitlines(); clean=strip(p.read_text()).splitlines(); caller=''
    for i,line in enumerate(clean):
        m=re.match(r'\s*(?:private\s+)?(?:noncomputable\s+)?(?:def|theorem|lemma)\s+([^\s(:]+)',line)
        if m:caller=m.group(1)
        hits=list(re.finditer(r'\b(?:MvPolynomial\.)?hasseCoeff\b',line))
        if hits and not (m and m.group(1)=='hasseCoeff'):
            rows.append(dict(file=str(p.relative_to(root)),line=i+1,caller=caller,occurrences=len(hits),excerpt=lines[i].strip()))
(here/'call-sites.json').write_text(json.dumps(rows,indent=2)+'\n')
commands=[['rg','-n',r'\bhasseCoeff\b',str(root/'.lake/packages/mathlib/Mathlib'),'--glob','*.lean'],['rg','-n',r'prod.*choose|choose.*prod',str(root/'Roth'),'--glob','*.lean']]
receipts=[]
for cmd in commands:
    r=subprocess.run(cmd,text=True,capture_output=True)
    receipts.append(dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
(here/'grep-receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
files=['Roth/HasseDeriv.lean','lake-manifest.json','lean-toolchain','lakefile.toml']
manifest=dict(files={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in files})
manifest['mathlib_revision']=subprocess.run(['git','-C','.lake/packages/mathlib','rev-parse','HEAD'],text=True,capture_output=True).stdout.strip()
manifest['git_status']=subprocess.run(['git','status','--short'],text=True,capture_output=True).stdout
(here/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(total_code_lines=len(rows),external_code_lines=sum(x['file']!='Roth/HasseDeriv.lean' for x in rows),external_files=sorted(set(x['file'] for x in rows if x['file']!='Roth/HasseDeriv.lean')),rows=rows),indent=2))
