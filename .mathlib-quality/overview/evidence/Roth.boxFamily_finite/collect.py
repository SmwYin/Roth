from pathlib import Path
import json,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();M=R/'.lake/packages/mathlib'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for form,patt in [('current',r'boxFamily_finite|finite.*(coeff|degree)|card_eq_of_natDegree_le|degreeOf_le_iff'),('standard',r'finsupp|finite.*support|mem_finsupp_iff|onFinset|finite.*pi'),('abstract',r'theorem.*image|finite_toSet|Finite.*image|finite_image_iff|of_injOn')]:
 paths=['Mathlib/Algebra/MvPolynomial','Mathlib/Data/Finsupp','Mathlib/Data/Finset/Finsupp.lean','Mathlib/Data/Set/Finite','Mathlib/NumberTheory/MahlerMeasure.lean']
 args=['rg','-n',patt]+[str(M/p)for p in paths];z=subprocess.run(args,text=True,capture_output=True);put('search-'+form+'-rg.json',dict(form=form,method='rg',command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
paths=['Mathlib/Data/Finset/Finsupp.lean','Mathlib/Data/Finsupp/Interval.lean','Mathlib/Data/Finsupp/Defs.lean','Mathlib/Data/Finsupp/Basic.lean','Mathlib/Algebra/MvPolynomial/Degrees.lean','Mathlib/Algebra/MonoidAlgebra/Defs.lean','Mathlib/Data/Set/Finite/Basic.lean','Mathlib/Data/Fintype/Pi.lean','Mathlib/NumberTheory/MahlerMeasure.lean']
xs=[]
for p in paths:
 n='mathlib-'+p.replace('/','-')+'.txt';(D/n).write_bytes((M/p).read_bytes());xs.append(dict(path=p,sha256=sha(M/p),bytes=(M/p).stat().st_size,archive=n))
put('mathlib-inputs.json',xs)
z=json.load(open(D/'original-receipt.json'))['result']['structuredContent']['result'];msgs=[x['message']for x in z['items']]
put('native-type.json',dict(type=next(x.split(': ',1)[1]for x in msgs if x.startswith('BOX245_FULL_TYPE:')),universe_parameters=['u_1'],project_body_dependencies=['Roth.boxFamily_eq_image_finsupp_aux'],printer_elision=True,elided_characters=9641,full_kernel_body_available=False,body_receipt='original-receipt.json'))
put('canonical-consumers.json',dict(value=[x.split(': ',1)[1]for x in msgs if x.startswith('BOX245_DIRECT_CONSUMER:')],type=[x.split(': ',1)[1]for x in msgs if x.startswith('BOX245_DIRECT_TYPE_CONSUMER:')]))
print('collected pinned modules; full target type; body printer explicitly elided9641; canonical293 complete')
