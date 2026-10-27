from pathlib import Path
import json,hashlib,subprocess,re,shutil
ROOT=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):D.joinpath(n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
base=json.loads((ROOT/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=[dict(path=p,sha256=sha(ROOT/p),bytes=(ROOT/p).stat().st_size,expected_sha256=v['sha256'],match=sha(ROOT/p)==v['sha256']) for p,v in base['sources_and_pins'].items()];save('inputs.json',inputs);save('input-hash-check.json',dict(all_pass=all(x['match'] for x in inputs),count=len(inputs)))
shutil.copy(ROOT/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
shutil.copy(ROOT/'.mathlib-quality/overview/declaration-order.json',D/'canonical-order.json')
for f in Path('/private/tmp/roth-overview').glob('exists-weight-eq-index-*'):
 if f.is_file():shutil.copy(f,D/f.name)
for n in ['index-expanded-mathlib-executed.lean.txt','index-expanded-mathlib-receipt.json','index-expanded-bridge-executed.lean.txt','index-expanded-bridge-receipt.json','index-consumers-executed.lean.txt','index-consumers-receipt.json']:
 shutil.copy(ROOT/'.mathlib-quality/overview/evidence/Roth.index'/n,D/n)
# Complete declaring and explicit-caller modules, exact unchanged files.
for p,n in [('Roth/Index.lean','Index-source.lean.txt'),('Roth/MainLemma.lean','MainLemma-source.lean.txt')]:shutil.copy(ROOT/p,D/n)
save('source-links.json',{'Roth/Index.lean':'Index-source.lean.txt','Roth/MainLemma.lean':'MainLemma-source.lean.txt'})
# Every explicit reference, independent of gitignore, mapped to top-level declarations.
callers=[]
for p in sorted(ROOT.glob('Roth/*.lean')):
 s=p.read_text();heads=list(re.finditer(r'^(?:private\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+(\w+)',s,re.M))
 for i,m in enumerate(heads):
  end=heads[i+1].start() if i+1<len(heads) else len(s);frag=s[m.start():end]
  # Match after signature/body split; target declaration excluded.
  if m[1]=='exists_weight_eq_index':continue
  matches=list(re.finditer(r'\b(?:Roth\.)?exists_weight_eq_index\b',frag))
  if matches:
   callers.append(dict(declaration='Roth.'+m[1],file=str(p.relative_to(ROOT)),line=s[:m.start()].count('\n')+1,source_sha256=sha(p),identifier_occurrences=len(matches),reference_lines=[s[:m.start()+a.start()].count('\n')+1 for a in matches],source_fragment=frag,plan='Choose d using Finset.exists_mem_eq_inf on nonempty Taylor support with WithTop-lifted weight; use coeff_taylor for nonvanishing and targetBridge plus untopD_coe to orient the attained equality. Keep subsequent consumer arithmetic. Complete caller replay replaces precisely this selection with the fresh originalReplacement.'))
save('callers.json',callers)
patterns={'current':r'exists_weight_eq_index|index.*weight|weight.*index', 'literature':r'exists_coeff_ne_zero_and_weightedOrder|exists_coeff_ne_zero_and_order', 'abstract':r'exists_mem_eq_sup|exists_mem_eq_inf|abbrev infDegree|csInf_mem', 'inline':r'csInf_mem|exists_mem_eq_inf|exists_coeff_ne_zero_and_weightedOrder|exists_weight_eq_index'}
for label,pattern in patterns.items():
 args=['rg','-n','--no-ignore',pattern,'Roth','.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean'];r=subprocess.run(args,cwd=ROOT,text=True,capture_output=True);save('rg-'+label+'.json',dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
args=['rg','-n',r'index|minimum|attained','.mathlib-quality/references/clean.tex'];r=subprocess.run(args,cwd=ROOT,text=True,capture_output=True);save('local-literature-search.json',dict(command=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
s=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();D.joinpath('clean-excerpt.tex.txt').write_text('\n'.join(s[529:556])+'\n')
paths=['.lake/packages/mathlib/Mathlib/Algebra/MonoidAlgebra/Degree.lean','.lake/packages/mathlib/Mathlib/Data/Finset/Lattice/Fold.lean','.lake/packages/mathlib/Mathlib/Order/WithBot.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Order.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Defs.lean','.mathlib-quality/references/clean.tex'];save('mathlib-inputs.json',[dict(path=p,sha256=sha(ROOT/p),bytes=(ROOT/p).stat().st_size) for p in paths])
print('fresh inputs',len(inputs),all(x['match'] for x in inputs),'callers',len(callers),sum(x['identifier_occurrences'] for x in callers))
