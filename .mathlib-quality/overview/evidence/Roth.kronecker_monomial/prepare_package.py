from pathlib import Path
import json,hashlib,subprocess,re,shutil
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent;N='Roth.kronecker_monomial'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,v):D.joinpath(n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
manifest=json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());inputs=[]
for name,old in manifest['sources_and_pins'].items():
 p=R/name;inputs.append(dict(path=name,sha256=sha(p),bytes=p.stat().st_size,baseline_sha256=old['sha256'],match=sha(p)==old['sha256']))
assert len(inputs)==17 and all(x['match'] for x in inputs);put('inputs.json',inputs)
shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',D/'baseline-build.txt')
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-snapshot.json',order);put('canonical-entry.json',order[106]);assert order[106]['name']==N
names=[]
for x in order:
 n='`'+x['name']
 if x['visibility']=='private':n='Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+' '+n
 names.append(n)
D.joinpath('canonical-audit-array.lean.txt').write_text('let names : Array Lean.Name := #['+','.join(names)+']\n')
paths=['Roth/GenWronskian.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Eval.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean','.mathlib-quality/references/clean.tex','/Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlib-search.md','/Users/ramin/.codex/skills/mathlib-quality/references/mathlibable-verdicts.md']
sources=[]
for i,name in enumerate(paths):
 p=R/name;dest=f'source-{i}.lean.txt' if i<3 else f'reference-{i}.txt';shutil.copyfile(p,D/dest);sources.append(dict(path=name,sha256=sha(p),bytes=p.stat().st_size,archive=dest))
put('source-inputs.json',sources)
queries={'current':['rg','-n','kronecker_monomial|Roth.kronecker_monomial', 'Roth','.lake/packages/mathlib/Mathlib'], 'standard':['rg','-n','aeval_monomial|eval₂_monomial|eval₂Hom_monomial','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial'], 'abstract':['rg','-n','weight_eq_sum|weight_apply|prod_pow_eq_pow_sum|prod_fintype','.lake/packages/mathlib/Mathlib/Data/Finsupp','.lake/packages/mathlib/Mathlib/Algebra/BigOperators'], 'callers':['rg','-n','kronecker_monomial','Roth','Roth.lean'], 'inline':['rg','-n','aeval_monomial|prod_pow_eq_pow_sum|kroneckerExp','Roth'], 'local-literature':['rg','-n','Kronecker|strictly smaller|h_\\\\nu|roth:lem1','.mathlib-quality/references/clean.tex']}
for label,cmd in queries.items():
 a=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('rg-'+label+'.json',dict(command=cmd,cwd=str(R),exit_code=a.returncode,stdout=a.stdout,stderr=a.stderr))
D.joinpath('local-literature.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[226:271])+'\n')
put('callers.json',dict(declaration=N,named_count=1,callers=['Roth.coeff_kronecker'],occurrence_count_excluding_def_doc=1,external_to_declaring_file=0,native_direct_consumers=['Roth.coeff_kronecker'],inline_derivations=[],notes='Source caller93; no attribute on target. Opaque/full downstream closure not claimed.'))
for label in ['original','probes','raw','consumer','audit','probes-rejected','bridge']:
 for suffix in ['executed.lean.txt','receipt.json']:
  p=Path('/private/tmp/roth-overview')/f'kronecker-monomial-{label}-{suffix}'
  if p.exists():shutil.copyfile(p,D/p.name)
