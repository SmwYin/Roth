from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.approxSet'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for f,pat in [('current',r'\bRoth\.approxSet\b|\bapproxSet\b'),('standard',r'infinite_rat_abs_sub|finite_rat_abs_sub|exists_rat_abs_sub_le_and_den_le|den_dvd'),('abstract',r'^def LiouvilleWith|^theorem exists_pos|frequently_lt_rpow_neg|^theorem frequently_atTop')]:
 req=['rg','-n',pat,'.lake/packages/mathlib/Mathlib'];z=subprocess.run(req,text=True,capture_output=True)
 put('search-'+f+'-rg.json',dict(request=dict(argv=req),result=dict(exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr)))
mat=[]
for f in ['current','standard','abstract']:
 for m in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=json.load(open(D/('search-'+f+'-'+m+'.json')));z=q['result'].get('structuredContent',q['result']);mat.append(dict(form=f,method=m,receipt='search-'+f+'-'+m+'.json',results=len(z.get('items',[]))if m!='rg'else None,index_status=z.get('index'),error=q['result'].get('isError',False)))
put('formal-search-matrix.json',mat)
paths=['Mathlib/NumberTheory/DiophantineApproximation/Basic.lean','Mathlib/NumberTheory/DiophantineApproximation/ContinuedFractions.lean','Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean','Mathlib/NumberTheory/Transcendental/Liouville/Basic.lean','Mathlib/NumberTheory/Transcendental/Liouville/Residual.lean','Mathlib/Order/Filter/AtTopBot/Basic.lean','Mathlib/Data/Set/Finite/Lattice.lean']
x=[]
for p in paths:
 s=R/'.lake/packages/mathlib'/p;n='mathlib-'+p.replace('/','-')+'.txt';(D/n).write_bytes(s.read_bytes());x.append(dict(path=p,archive=n,sha256=sha(s),bytes=s.stat().st_size))
put('mathlib-inputs.json',x)
# exact full-name search, all source output retained
req=['rg','-n',r'\bRoth\.approxSet\b|\bLiouvilleWith\b|infinite_rat_abs_sub_lt_one_div_den_sq','.lake/packages/mathlib/Mathlib'];z=subprocess.run(req,text=True,capture_output=True);put('full-name-search.json',dict(request=req,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
orig=json.load(open(D/'original-receipt.json'))['result']['structuredContent']['result'];ds=orig['items'];msgs=[x['message']for x in ds]
put('native-type.json',dict(type=next(x.split(': ',1)[1]for x in msgs if x.startswith('APPROX267_FULL_TYPE:')),full_type=True,full_written_source_body=True,full_kernel_printer_body=True,printer_elision=any('LEAN_MCP_MAX_OUTPUT_CHARS'in x for x in msgs),kernel_print=next(x for x in msgs if x.startswith('def Roth.approxSet'))))
put('dependencies.json',dict(canonical_body=[],canonical_type=[],raw_kernel_body_constants_message=next(x for x in msgs if x.startswith('APPROX267_BODY_CONSTANTS')),raw_kernel_type_constants_message=next(x for x in msgs if x.startswith('APPROX267_TYPE_CONSTANTS')),transitive_project_dependencies=[],scope='Target definition has no project constants in type or body. Direct canonical consumers are separately enumerated; this is not a simp closure.'))
put('canonical-consumers.json',dict(requested=293,unique=293,present=293,values=293,direct_value=[x.split(': ',1)[1]for x in msgs if x.startswith('APPROX267_DIRECT_CONSUMER:')],direct_type=[x.split(': ',1)[1]for x in msgs if x.startswith('APPROX267_DIRECT_TYPE_CONSUMER:')]))
rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'));callers=[]
for x in rows:
 if x['name']==N:continue
 if re.search(r'\bapproxSet\b',x['source']):
  (D/('caller-'+x['name']+'.lean.txt')).write_text(x['source']+'\n');callers.append(dict(name=x['name'],file=x['file'],line=x['line'],end_line=x['end_line'],visibility=x['visibility'],archive='caller-'+x['name']+'.lean.txt',sha256=hashlib.sha256((x['source']+'\n').encode()).hexdigest(),target_occurrences=len(re.findall(r'\bapproxSet\b',x['source']))))
assert len(callers)==10
put('callers.json',dict(source_explicit=callers,source_explicit_count=10,external_file_count=1,external_declaration_count=2,kernel_direct_value_count=12,kernel_direct_type_count=10,full_inline_original_signatures=12,inline_scope='Full original Main and LeanEval bodies replayed with raw literal replacing explicit approxSet references,9 public +3 private signature equalities. Roth.roth_rat and thueSiegelRoth have kernel target constants via elaborated parameters but no source-explicit approxSet. Whole transitive target elimination not claimed.'))
put('inline-audit.json',dict(search='inline-search.json',findings=[dict(declaration='Roth.roth_rat',shape='Reduced rational-height condition on input, pair condition on generated num/den; bridge by den_pos/cast_def.',duplicate=False),dict(declaration='Roth.abs_eval_lt_of_le_index',shape='Coordinatewise weak ≤ approximation premise at Fin m; different shape and weak inequality, no denominator-positivity conjunction.',duplicate=False),dict(declaration='LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine',shape='Uniform positive lower-bound constant for every ε; dual quantified endpoint, not same set.',duplicate=False)],verdict='No exact bypassing redefinition of the fixed pair-set. Related formulations have actual downstream semantic roles.'))
put('optional-math-opinion.json',dict(status='justified n/a',reason='ask_chatgpt_math unavailable in available tools; all other channels executed.'))
put('preparation-checks.json',dict(original_preexecution=dict(command=['python3','/private/tmp/roth-overview/check_audit_source.py',str(D/'original-executed.lean.txt')],exit_code=0,stdout='PASS exact293 unique source order: '+str(D/'original-executed.lean.txt'),source_sha256=sha(D/'original-executed.lean.txt')),width_preparation_failures=[dict(script='prepare_inline.py initial draft',exit_code=1,max_width=168,native_queried_after_failure=False,reason='Draft literal expansion exceeded width; no file written or native query after failed prep. Revised closing-parenthesis placement before actual execution.')],all_accepted_preparations_exit_zero=True,shared18_unchanged=sha(D/'isolated-prefix.lean.txt')==sha(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt'))))
put('concrete-diagnostic.json',dict(definition_body_project_identifiers=0,concrete_via_abstract='The definition has no proof and no named real α witness. Concrete coefficient1 is semantic: constants_differ proves C1≠C2. Arbitrary ψ supplies the radius, not just a trivial function renaming; isolated bounded_den_finite and LiouvilleWith bridge verify reusable API. Real exponent arithmetic is meaningful, unrestricted Set.ofPred is construction infrastructure rather than an exact named concept.'))
# Historical exact source receipts include a genuine failed preparation, four rejected native attempts.
put('fresh-final-inputs.json',dict(unchanged=True,inputs=[dict(path=x['path'],sha256=sha(R/x['path']),bytes=(R/x['path']).stat().st_size,match=sha(R/x['path'])==x['sha256'])for x in json.load(open(D/'inputs.json'))]))
print('Collected15formal,7pinnedfiles,10source/12kernel callers,full native type/body,inputs')
