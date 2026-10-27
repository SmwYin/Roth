import pathlib,json,hashlib,re,subprocess
p=pathlib.Path(__file__).resolve().parent;repo=pathlib.Path('/Users/ramin/LEAN/Roth')
commands={'current':['rg','-n','wronskian|hasseDeriv','.lake/packages/mathlib/Mathlib/RingTheory/Polynomial/Wronskian.lean'],'literature':['rg','-n','det_updateCol|det_updateRow_add_smul_self','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean'],'abstract':['rg','-n','map_update_sub|map_update_smul|map_update_self|compLinearMap','.lake/packages/mathlib/Mathlib/LinearAlgebra/Alternating/Basic.lean'],'callers':['rg','-n','wronskian_update_sub_smul|det_updateCol_add_smul_self|updateCol','Roth','Roth.lean'],'local-reference':['rg','-n','Wronskians|column operations|new Wronskian','.mathlib-quality/references/clean.tex']}
for n,c in commands.items():
 r=subprocess.run(c,cwd=repo,capture_output=True,text=True);(p/('rg-'+n+'.json')).write_text(json.dumps(dict(request=c,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr),indent=2)+'\n')
sources={'Roth/Wronskian.lean':'source-wronskian.lean.txt','.mathlib-quality/references/clean.tex':'source-clean.tex.txt','.lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean':'source-mathlib-det.lean.txt','.lake/packages/mathlib/Mathlib/LinearAlgebra/Alternating/Basic.lean':'source-mathlib-alternating.lean.txt','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/HasseDeriv.lean':'source-mathlib-hasse.lean.txt','.lake/packages/mathlib/Mathlib/RingTheory/Polynomial/Wronskian.lean':'source-mathlib-wronskian.lean.txt'}
for src,dst in sources.items():(p/dst).write_bytes((repo/src).read_bytes())
manifest=json.loads((repo/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text());rows=[]
for src,v in manifest['sources_and_pins'].items():
 b=(repo/src).read_bytes();s=hashlib.sha256(b).hexdigest();rows.append(dict(path=src,sha256=s,baseline_sha256=v['sha256'],bytes=len(b),match=s==v['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows)
(p/'source-pin-hashes.json').write_text(json.dumps(rows,indent=2)+'\n');(p/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(p/'baseline-build.txt').write_bytes((repo/'.mathlib-quality/overview/evidence/shared/baseline-build.txt').read_bytes())
(p/'source-mathlib-hashes.json').write_text(json.dumps([dict(path=src,sha256=hashlib.sha256((repo/src).read_bytes()).hexdigest(),bytes=len((repo/src).read_bytes())) for src in sources if src.startswith('.lake')],indent=2)+'\n')
(p/'source-links.json').write_text(json.dumps(sources,indent=2)+'\n')
print('All 17 source/pin hashes freshly match baseline')
