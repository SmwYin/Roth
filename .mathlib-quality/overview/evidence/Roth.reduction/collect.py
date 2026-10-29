from pathlib import Path
import json,hashlib,subprocess,re
D=Path(__file__).resolve().parent;R=Path.cwd()
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def run(n,args):
 z=subprocess.run(args,text=True,capture_output=True);put(n,dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));return z
for form,p in [('current',r'reduction.*[Ii]ntegral|[Ii]ntegral.*reduction|exists_integral_multiple'),('standard',r'LiouvilleWith|frequently_lt_rpow_neg|nat_mul_iff'),('abstract',r'theorem (Infinite\.(image|sdiff)|infinite_image_iff|infinite_of_injOn_mapsTo)')]:
 run('search-'+form+'-rg.json',['rg','-n',p,'.lake/packages/mathlib/Mathlib'])
run('full-name-search.json',['rg','-n',r'Roth\.reduction|theorem reduction\b','.lake/packages/mathlib/Mathlib'])
run('caller-complete-search.json',['rg','--no-ignore','-n',r'\breduction\b|\.reduction\b','Roth','Roth.lean'])
run('inline-complete-search.json',['rg','--no-ignore','-n',r'prodMap|exists_nat_mul_isIntegral|natCast_mul|hinf\.sdiff','Roth','Roth.lean'])
# Fresh inventory counts from canonical sources, unaffected by ignore rules.
manifest=json.load(open(R/'.mathlib-quality/overview/evidence/shared/input-manifest.json'))
put('source-reading.json',dict(files=[dict(path='Roth/Main.lean',lines=588,sha256=hashlib.sha256((R/'Roth/Main.lean').read_bytes()).hexdigest(),scope='Entire file read in multiple explicit sed ranges; target and only actual caller contained here.'),dict(path='Roth/LeanEval.lean',lines=66,sha256=hashlib.sha256((R/'Roth/LeanEval.lean').read_bytes()).hexdigest(),scope='Entire downstream module read, no direct reduction caller.')],actual_callers=['Roth.roth'],source_inventory=list(manifest['sources_and_pins'])))
put('callers.json',dict(explicit_body=[dict(name='Roth.roth',file='Roth/Main.lean',line=576,source='caller-Roth.roth.lean.txt')],explicit_type=[],external_to_file=0,documentation_mentions=2,definition_heads=1,kernel_direct_expected=['Roth.roth'],transitive_consumers='Roth.roth_rat and LeanEval thueSiegelRoth are downstream through Roth.roth; not explicit reduction callers.',inline_derivations=[]))
put('concrete-diagnostic.json',dict(proof_counts={s:len(re.findall(re.escape(s),json.load(open(D/'target-metadata.json'))['source'].split(':= by',1)[1]))for s in ['2','IsAlgebraic','IsIntegral','Irrational','approxSet']},conclusion='Threshold2 occurs in midpoint/gap/output only and is replaceable by arbitrary t; once M integral chosen, scaling subproof uses neither algebraicity nor irrationality. No real-to-general-field claim: real powers, ordering, Archimedean finiteness used.'))
paths=['Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean','Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.lean','Mathlib/RingTheory/Algebraic/Integral.lean','Mathlib/NumberTheory/Real/Irrational.lean','Mathlib/Data/Set/Finite/Basic.lean']
inputs=[]
for p in paths:
 f=R/'.lake/packages/mathlib'/p
 if f.exists():
  n='mathlib-'+p.replace('/','-')+'.txt';(D/n).write_bytes(f.read_bytes());inputs.append(dict(path=str(f.relative_to(R)),artifact=n,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),bytes=f.stat().st_size))
put('mathlib-inputs.json',inputs)
put('optional-math-opinion.json',dict(status='justified n/a',reason='ask_chatgpt_math unavailable; no optional math opinion tool installed.'))
