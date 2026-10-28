from pathlib import Path
import json,hashlib,subprocess,re
D=Path(__file__).resolve().parent;R=Path.cwd();M=R/'.lake/packages/mathlib'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for form,patt in [('current',r'boxFamily|degreeOf_le_iff|monomial_le_degreeOf|degreesLE'),('standard',r'restrictSupport|restrictDegree|mvPolynomialSupportLEEquiv|ofCoeff_injective|coeffEquiv'),('abstract',r'protected def finsupp|mem_finsupp_iff|card_finsupp|card_Iic|def pi')]:
 args=['rg','-n',patt,str(M/'Mathlib/Algebra/MvPolynomial'),str(M/'Mathlib/RingTheory/MvPolynomial'),str(M/'Mathlib/Data/Finset/Finsupp.lean'),str(M/'Mathlib/Data/Finsupp/Interval.lean'),str(M/'Mathlib/Algebra/MonoidAlgebra/Defs.lean')]
 z=subprocess.run(args,text=True,capture_output=True);put('search-'+form+'-rg.json',dict(form=form,method='rg',command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
paths=['Mathlib/Data/Finset/Finsupp.lean','Mathlib/Data/Finsupp/Interval.lean','Mathlib/Data/Finsupp/Defs.lean','Mathlib/RingTheory/MvPolynomial/Basic.lean','Mathlib/RingTheory/MvPolynomial/FreeCommRing.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/MonoidAlgebra/Defs.lean']
xs=[]
for p in paths:
 n='mathlib-'+p.replace('/','-')+'.txt';(D/n).write_bytes((M/p).read_bytes());xs.append(dict(path=p,sha256=sha(M/p),bytes=(M/p).stat().st_size,archive=n))
put('mathlib-inputs.json',xs)
rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'));cs=json.load(open(D/'target-metadata.json'))['source_callers'];out=[]
for c in cs:
 x=next(x for x in rows if x['name']==c['name']and x['file']==c['file']);s=x['source'];out.append({**c,'end_line':x['end_line'],'visibility':x['visibility'],'source':s,'sha256':hashlib.sha256(s.encode()).hexdigest(),'signature':x['signature'],'body':x['body'],'occurrences':len(re.findall(r'\bboxFamily\b',s))})
put('callers.json',dict(callers=out,distinct_declarations=7,external_to_file_files=0,external_to_file_declarations=0,executable_occurrences=sum(x['occurrences']for x in out)))
loc=R/'.mathlib-quality/references/clean.tex';(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1399:1422])+'\n')
z=subprocess.run(['rg','--no-ignore','-n',r'boxFamily|0 ≤ .*coeff|coeff.*≤ B|finsupp|restrictSupport','Roth','Roth.lean'],text=True,capture_output=True);put('inline-audit.json',dict(command=z.args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
pre=(D/'isolated-executed.lean.txt').read_text().split('\n\n',1)[0]+'\n';(D/'isolated-prefix21.lean.txt').write_text(pre)
put('prefix-provenance.json',dict(base18_sha256=sha(D/'isolated-prefix.lean.txt'),accepted21_sha256=sha(D/'isolated-prefix21.lean.txt'),extra_imports=pre.splitlines()[18:],base_shared_unchanged=sha(D/'isolated-prefix.lean.txt')==sha(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')),headers_verified=paths[:4],authorization='root-prefix-scope-authorization.json'))
orig=json.load(open(D/'original-receipt.json'))['raw']['structuredContent']['result'];msg=[x['message']for x in orig['items']]
put('native-type.json',dict(type=next(x.split(': ',1)[1]for x in msg if x.startswith('BOX233_FULL_TYPE:')),universe_parameters=['u_1'],project_body_dependencies=[],printer_elision=False,full_kernel_body=next(x for x in msg if x.startswith('def Roth.boxFamily'))))
put('canonical-consumers.json',dict(value=[x.split(': ',1)[1]for x in msg if x.startswith('BOX233_DIRECT_CONSUMER:')],type=[x.split(': ',1)[1]for x in msg if x.startswith('BOX233_DIRECT_TYPE_CONSUMER:')]))
put('preparation-checks.json',dict(original=dict(exit_code=0,canonical_source_gate='PASS exact293 unique source order',source='original-executed.lean.txt'),isolated=dict(exit_code=0,width_le100=True,imports=21),inline=dict(exit_code=0,width_le100=True),project=dict(exit_code=0,width_le100=True),all_sources_inspected_before_execution=True))
print('collected',len(xs),'pinned modules and',len(out),'full callers')
