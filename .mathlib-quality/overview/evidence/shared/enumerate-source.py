"""Read-only Lean source inventory repair. Not a Lean elaborator or dependency oracle.
Handles nested comments, strings, brackets, named arguments, statement-level lets;
asserts the precise restricted source grammar used by this frozen project.
"""
import json,re,hashlib
from pathlib import Path
BASE=Path.cwd()

def mask(s):
    out=list(s); i=0; comment=0; string=False
    while i<len(s):
        if comment:
            if s[i:i+2]=='/-':out[i:i+2]='  ';comment+=1;i+=2;continue
            if s[i:i+2]=='-/':out[i:i+2]='  ';comment-=1;i+=2;continue
            if s[i]!='\n':out[i]=' '
            i+=1;continue
        if string:
            if s[i]=='\\':
                out[i]=' '; i+=1
                if i<len(s) and s[i]!='\n':out[i]=' '
                i+=1;continue
            if s[i]=='"':string=False
            if s[i]!='\n':out[i]=' '
            i+=1;continue
        if s[i:i+2]=='/-':out[i:i+2]='  ';comment=1;i+=2;continue
        if s[i:i+2]=='--':
            j=s.find('\n',i); j=len(s) if j<0 else j;out[i:j]=' '*(j-i);i=j;continue
        if s[i]=='"':string=True;out[i]=' '
        i+=1
    assert comment==0 and not string
    return ''.join(out)

def delimiter(source):
    clean=mask(source); depth=[]; pending_lets=0
    # Quotes in identifiers (foo') are not strings; Lean quoted names aren't used here.
    token=re.compile(r':=|[()\[\]{}⟨⟩]|\b(?:let|letI|letM)\b')
    for m in token.finditer(clean):
        t=m.group()
        if t in ['(', '[', '{', '⟨']:depth.append(t)
        elif t in [')',']','}','⟩']:
            assert depth, (t,source[:m.start()]); depth.pop()
        elif not depth:
            if t in ['let','letI','letM']:pending_lets+=1
            elif pending_lets:pending_lets-=1
            else:return m.start()
    raise AssertionError('No declaration delimiter: '+source)

def tests():
    samples=[
      ('theorem x : F (R := R) = y := by\n  exact h','theorem x : F (R := R) = y'),
      ('theorem x : let M := f (R := R)\n let N := M\n N = M := by\n  rfl','theorem x : let M := f (R := R)\n let N := M\n N = M'),
      ('def x (h : F (R := R)) : A := f h','def x (h : F (R := R)) : A'),
      ('theorem x : P :=\n  have h : Q := by exact q\n  h','theorem x : P'),
      ('theorem x /- := /- nested := -/ -/ : P := by\n  exact p','theorem x /- := /- nested := -/ -/ : P'),
      ('def x : String := "named := by"','def x : String')]
    for source,expected in samples:assert source[:delimiter(source)].rstrip()==expected

def scan():
    result=[]
    for path in [BASE/'Roth.lean']+sorted((BASE/'Roth').glob('*.lean')):
        original=path.read_text();clean=mask(original);lines=original.splitlines();masked=clean.splitlines();ns=[];stack=[];decl=[]
        for n,line in enumerate(masked):
            if m:=re.match(r'^namespace\s+(\S+)',line):ns.append(m[1]);stack.append('namespace');continue
            if re.match(r'^section(?:\s|$)',line):stack.append('section');continue
            if re.match(r'^end(?:\s|$)',line):
                assert stack,(path,n);kind=stack.pop()
                if kind=='namespace':ns.pop()
                continue
            m=re.match(r'^(?P<mod>(?:(?:private|protected|noncomputable|unsafe)\s+)*)(?P<kind>def|lemma|theorem|instance|abbrev|structure|class)\s+(?P<short>[^\s:(\[{]+)',line)
            if m:decl.append(dict(file=str(path.relative_to(BASE)),line=n+1,name='.'.join(ns+[m['short']]),short=m['short'],kind=m['kind'],visibility='private' if 'private' in m['mod'] else 'public'))
        for index,d in enumerate(decl):
            start=d['line']-1;end=decl[index+1]['line']-1 if index+1<len(decl) else len(lines)
            for k in range(start+1,end):
                if re.match(r'^(?:@\[|(?:end|section|namespace|variable|omit|include|open|attribute|set_option)\b)',masked[k]):end=k;break
            while end>start+1 and not masked[end-1].strip():end-=1
            source='\n'.join(lines[start:end]);p=delimiter(source);body=source[p+2:].strip()
            d.update(end_line=end,source=source,signature=source[:p].rstrip(),body=body,proof_lines=body.count('\n')+1,sha256=hashlib.sha256(source.encode()).hexdigest(),assignment_offset=p)
            result.append(d)
    return result

if __name__=='__main__':
    tests()
    print(json.dumps([{k:r[k] for k in ['name','file','line','kind','visibility','sha256']} for r in scan()],ensure_ascii=False,indent=2))
