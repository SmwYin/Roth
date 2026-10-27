from pathlib import Path
import json,hashlib,subprocess,re,shutil
ROOT=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):D.joinpath(n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
base=json.loads((ROOT/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=[dict(path=p,sha256=sha(ROOT/p),bytes=(ROOT/p).stat().st_size,expected_sha256=v['sha256'],match=sha(ROOT/p)==v['sha256']) for p,v in base['sources_and_pins'].items()];save('inputs.json',inputs);save('input-hash-check.json',dict(all_pass=all(x['match'] for x in inputs),count=len(inputs)))
shutil.copy(ROOT/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
shutil.copy(ROOT/'.mathlib-quality/overview/declaration-order.json',D/'canonical-order.json')
for f in Path('/private/tmp/roth-overview').glob('index-le-weight-*'):
 if f.is_file():shutil.copy(f,D/f.name)
for n in ['index-expanded-mathlib-executed.lean.txt','index-expanded-mathlib-receipt.json']:
 shutil.copy(ROOT/'.mathlib-quality/overview/evidence/Roth.index'/n,D/n)
# Complete declaring and explicit-caller modules, exact unchanged files.
for p,n in [('Roth/Index.lean','Index-source.lean.txt'),('Roth/Main.lean','Main-source.lean.txt')]:shutil.copy(ROOT/p,D/n)
save('source-links.json',{'Roth/Index.lean':'Index-source.lean.txt','Roth/Main.lean':'Main-source.lean.txt'})
# Every explicit reference, independent of gitignore, mapped to top-level declarations.
callers=[]
for p in sorted(ROOT.glob('Roth/*.lean')):
 s=p.read_text();heads=list(re.finditer(r'^(?:private\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+(\w+)',s,re.M))
 for i,m in enumerate(heads):
  end=heads[i+1].start() if i+1<len(heads) else len(s);frag=s[m.start():end]
  # Match after signature/body split; target declaration excluded.
  if m[1]=='index_le_weight':continue
  matches=list(re.finditer(r'\b(?:Roth\.)?index_le_weight\b',frag))
  if matches:
   callers.append(dict(declaration='Roth.'+m[1],file=str(p.relative_to(ROOT)),line=s[:m.start()].count('\n')+1,source_sha256=sha(p),identifier_occurrences=len(matches),reference_lines=[s[:m.start()+a.start()].count('\n')+1 for a in matches],source_fragment=frag,plan='Replace the indicated index_le_weight application with the projected infDegree bound after rewriting IndexConsumers133.targetBridge and converting the nonzero evaluated Hasse derivative to Taylor support via coeff_taylor. Preserve all caller hypotheses and subsequent transitivity/simp arithmetic; caller replay uses this exact replacement locally.'))
save('callers.json',callers)
patterns={'current':r'index_le_weight|index.*weight|weight.*index', 'literature':r'weightedOrder_le|natTrailingDegree_le_of_ne_zero|order.*coeff', 'abstract':r'@\[to_dual inf_le\]|@\[to_dual untopD_le\]|abbrev infDegree|theorem infDegree_withTop_some_comp', 'inline':r'csInf_le|Finset\.inf_le|weightedOrder_le|index_le_weight'}
for label,pattern in patterns.items():
 args=['rg','-n','--no-ignore',pattern,'Roth','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean'];r=subprocess.run(args,cwd=ROOT,text=True,capture_output=True);save('rg-'+label+'.json',dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
args=['rg','-n',r'index|minimum|attained','.mathlib-quality/references/clean.tex'];r=subprocess.run(args,cwd=ROOT,text=True,capture_output=True);save('local-literature-search.json',dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
s=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();D.joinpath('clean-excerpt.tex.txt').write_text('\n'.join(s[529:556])+'\n')
paths=['.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Defs.lean','.mathlib-quality/references/clean.tex'];save('mathlib-inputs.json',[dict(path=p,sha256=sha(ROOT/p),bytes=(ROOT/p).stat().st_size) for p in paths])
print('fresh inputs',len(inputs),all(x['match'] for x in inputs),'callers',len(callers),sum(x['identifier_occurrences'] for x in callers))
