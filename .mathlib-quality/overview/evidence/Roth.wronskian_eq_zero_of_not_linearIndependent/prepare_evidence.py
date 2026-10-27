from pathlib import Path
import json,hashlib,subprocess,shutil
d=Path("/private/tmp/roth-overview/assess/Roth.wronskian_eq_zero_of_not_linearIndependent")
repo=Path('/Users/ramin/LEAN/Roth')
sha=lambda b:hashlib.sha256(b).hexdigest()
shared=json.loads((repo/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
rows=[]
for p,v in shared['sources_and_pins'].items():
 b=(repo/p).read_bytes();rows.append(dict(path=p,sha256=sha(b),baseline_sha256=v['sha256'],bytes=len(b),matches=sha(b)==v['sha256']))
assert all(r['matches'] for r in rows)
(d/'source-pin-hashes.json').write_text(json.dumps(rows,indent=2)+'\n')
shutil.copyfile(repo/'.mathlib-quality/overview/evidence/shared/baseline-build.txt',d/'baseline-build.txt')
shutil.copyfile(repo/'Roth/Wronskian.lean',d/'source-wronskian.lean.txt')
(d/'local-literature.txt').write_text('\n'.join((repo/'.mathlib-quality/references/clean.tex').read_text().splitlines()[156:224])+'\n')
cmds=[
['rg','-n','wronskian_eq_zero_of_not_linearIndependent','Roth','Roth.lean'],
['rg','-n','wronskian_eq_zero_iff|exists_mulVec_eq_zero_iff|not_linearIndependent_iff|map_linearDependent','Roth','Roth.lean'],
['rg','-n','hasseDeriv.*det|det.*hasseDeriv|wronskian',' .lake/packages/mathlib/Mathlib'.strip()],
['rg','-n','map_linearDependent|det_eq_zero_of_not_linearIndependent|restrict_scalars\'|LinearIndependent.of_comp',' .lake/packages/mathlib/Mathlib/LinearAlgebra'.strip()],
['rg','-n','wronskian|linearDependent|not_linearIndependent',' .lake/packages/mathlib/Mathlib/RingTheory/Polynomial/Wronskian.lean'.strip()],
['rg','-n','Roth\\.wronskian_eq_zero_of_not_linearIndependent',' .lake/packages/mathlib/Mathlib'.strip()]]
out=[]
for cmd in cmds:
 p=subprocess.run(cmd,cwd=repo,text=True,capture_output=True);out.append(dict(command=cmd,cwd=str(repo),exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
(d/'source-search-raw.json').write_text(json.dumps(out,indent=2)+'\n')
files=['.lake/packages/mathlib/Mathlib/LinearAlgebra/Alternating/Basic.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/LinearIndependent/Basic.lean','.lake/packages/mathlib/Mathlib/LinearAlgebra/LinearIndependent/Defs.lean','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean','.lake/packages/mathlib/Mathlib/RingTheory/Polynomial/Wronskian.lean']
(d/'mathlib-source-hashes.json').write_text(json.dumps([dict(path=p,sha256=sha((repo/p).read_bytes()),bytes=(repo/p).stat().st_size) for p in files],indent=2)+'\n')
texts=[]
for p,lo,hi in [(files[0],780,804),(files[1],480,501),(files[2],65,99),(files[3],305,319),(files[5],1,170)]:
 texts += [p+':'+str(lo),* (repo/p).read_text().splitlines()[lo-1:hi]]
(d/'mathlib-source-excerpts.lean.txt').write_text('\n'.join(texts)+'\n')
(d/'canonical-metadata.json').write_text(json.dumps({'declaration':'Roth.wronskian_eq_zero_of_not_linearIndependent','canonical':42,'source':'Roth/Wronskian.lean:65','kind':'theorem','prefilter':'none; public non-glue theorem'},indent=2)+'\n')

