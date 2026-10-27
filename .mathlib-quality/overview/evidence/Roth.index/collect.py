from pathlib import Path
import re,json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,x): (D/n).write_text(json.dumps(x,indent=2))
base=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=[dict(path=p,sha256=sha(R/p),baseline_sha256=v['sha256'],bytes=(R/p).stat().st_size,match=sha(R/p)==v['sha256']) for p,v in base['sources_and_pins'].items()]
write('inputs.json',inputs);write('input-hash-check.json',{'all_pass':all(x['match'] for x in inputs),'count':len(inputs)})
(D/'baseline-build.txt').write_bytes((R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_bytes())
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());write('canonical-entry.json',next(x for x in order if x['name']=='Roth.index'))
write('canonical-order.json',order)
# Nested Lean comments removed while preserving line positions.
def clean(s):
 out=[];i=0;depth=0
 while i<len(s):
  if s[i:i+2]=='/-':depth+=1;out+=[' ',' '];i+=2
  elif depth and s[i:i+2]=='-/':depth-=1;out+=[' ',' '];i+=2
  elif depth:out.append('\n' if s[i]=='\n' else ' ');i+=1
  elif s[i:i+2]=='--':
   j=s.find('\n',i);j=len(s) if j<0 else j;out+=[' ']*(j-i);i=j
  else:out.append(s[i]);i+=1
 return ''.join(out)
callers=[];source_links={}
for f in R.glob('Roth/*.lean'):
 text=f.read_text();c=clean(text);lines=text.splitlines();cl=c.splitlines();decls=list(re.finditer(r'(?m)^(?:private |noncomputable |protected )*(?:def|theorem|lemma|abbrev|structure|instance)\s+([\w.\u0370-\u03ff]+)',c))
 for k,m in enumerate(decls):
  end=decls[k+1].start() if k+1<len(decls) else len(c);block=c[m.start():end]
  refs=[c[:m.start()+x.start()].count('\n')+1 for x in re.finditer(r'(?<![\w.])(?:Roth\.)?index\b',block)]
  if not refs or m.group(1)=='index':continue
  line=c[:m.start()].count('\n')+1;endline=c[:end].count('\n')+1
  name=next((x['name'] for x in order if x['file']==str(f.relative_to(R)) and x['line']==line),'Roth.'+m.group(1))
  callers.append({'name':name,'file':str(f.relative_to(R)),'line':line,'reference_lines':refs,'identifier_occurrences':len(refs),'source_sha256':sha(f),'source_fragment':'\n'.join(lines[line-1:endline-1]),'plan':'Retain project-local index API; if migrating its implementation, rewrite by the verified whole-function index/infDegree bridge. If deleting the name, expand to that exact expression in statement and body; preserve nonvanishing and zero-weight hypotheses.'})
  source_links[str(f.relative_to(R))]=f.name+'.txt'
write('callers.json',callers)
for p,a in source_links.items():(D/a).write_bytes((R/p).read_bytes())
for p in ['Roth/Index.lean','Roth/Taylor.lean','Roth/Box.lean']:source_links[p]=Path(p).name+'.txt';(D/source_links[p]).write_bytes((R/p).read_bytes())
write('source-links.json',source_links)
for label,pattern in [('current',r'\bindex\b|Taylor.*order'),('literature',r'weightedOrder|infDegree'),('abstract',r'sInf.*support|inf.*support|inf._eq_csInf_image'),('inline',r'sInf.*weight|weight.*support')]:
 cmd=['rg','-n',pattern,'.lake/packages/mathlib/Mathlib','Roth'];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);write('rg-'+label+'.json',{'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
cmd=['rg','-n',r'index|P_\\alpha|weightedOrder', '.mathlib-quality/references/clean.tex'];p=subprocess.run(cmd,cwd=R,text=True,capture_output=True);write('local-literature.json',{'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
(D/'clean-index-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[527:561])+'\n')
paths=['.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/Order/ConditionallyCompleteLattice/Finset.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean']
write('mathlib-inputs.json',[dict(path=p,sha256=sha(R/p),bytes=(R/p).stat().st_size) for p in paths])
print('callers',len(callers),'occurrences',sum(x['identifier_occurrences'] for x in callers),'byfile',{p:sum(x['file']==p for x in callers) for p in sorted({x['file'] for x in callers})})
