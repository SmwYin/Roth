from pathlib import Path
import json,hashlib,subprocess,re
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.exists_monic_aeval_eq_zero'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,args):
 z=subprocess.run(args,text=True,capture_output=True);put(n,dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr));return z
for form,pat in [('current',r'exists_monic_aeval_eq_zero|one_lt_natDegree_of_irrational_root'),('standard',r'exists.*monic.*aeval|IsIntegral.*natDegree|natDegree.*IsIntegral'),('abstract',r'natDegree_mul_X_pow|theorem Monic.mul|theorem monic_X_pow|theorem Monic.ne_zero')]:
 run('search-'+form+'-rg.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib'])
run('full-name-search.json',['rg','-n',r'Roth\.exists_monic_aeval_eq_zero|\bexists_monic_aeval_eq_zero\b','.lake/packages/mathlib/Mathlib'])
run('caller-complete-search.json',['rg','--no-ignore','-n',r'\bexists_monic_aeval_eq_zero\b','Roth','Roth.lean'])
run('inline-complete-search.json',['rg','--no-ignore','-n',r'monic_X_pow|natDegree_mul_X_pow|IsIntegral|\.Monic|Polynomial.X','Roth','Roth.lean'])
run('local-literature.json',['rg','-n',r'algebraic integer|monic|degree.*least|irrational','.mathlib-quality/references/clean.tex'])
p=R/'.mathlib-quality/references/clean.tex';lines=p.read_text().splitlines();inds=[i for i,l in enumerate(lines)if 'Since $'in l and 'algebraic integer'in l]
# Relevant section around polynomial choice; exact local text does not have web restrictions.
inds += [i for i,l in enumerate(lines)if 'Its degree'in l or 'since $' in l and 'irrational'in l]
ex=[]
for i in inds:ex.append(dict(line=i+1,text='\n'.join(lines[max(0,i-3):i+7])))
put('local-excerpts.json',ex)
mathfiles=['Mathlib/RingTheory/IntegralClosure/IsIntegral/Defs.lean','Mathlib/RingTheory/IntegralClosure/IsIntegral/Basic.lean','Mathlib/Algebra/Polynomial/Degree/Operations.lean','Mathlib/Algebra/Polynomial/Degree/Defs.lean','Mathlib/Algebra/Polynomial/Monic.lean','Mathlib/NumberTheory/Real/Irrational.lean','Mathlib/FieldTheory/Minpoly/Basic.lean']
xs=[]
for n in mathfiles:
 p=R/'.lake/packages/mathlib'/n;out='mathlib-'+n.replace('/','-')+'.txt';(D/out).write_bytes(p.read_bytes());xs.append(dict(path=str(p.relative_to(R)),archive=out,sha256=sha(p),bytes=p.stat().st_size))
put('mathlib-inputs.json',xs)
paths=['/private/tmp/roth-overview/next-worker272-prompt.txt','/private/tmp/roth-overview/WORKER_CONTRACT.md','/private/tmp/roth-overview/EXCLUSIVE_NATIVE_WORKER_ADDENDUM.md','/private/tmp/roth-overview/ROOT_NATIVE_EXECUTOR_ADDENDUM.md','/private/tmp/roth-overview/MINIMAL_ORIGINAL_REPLAY_ADDENDUM.md','/Users/ramin/.codex/skills/lean4/SKILL.md','/Users/ramin/.codex/skills/mathlib-quality/SKILL.md','/Users/ramin/.local/share/roth-mathlib-quality/commands/overview.md','/Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md']
paths += ['/Users/ramin/.codex/skills/mathlib-quality/references/'+x+'.md' for x in ['mathlib-search','mathlibable-verdicts','generalisation-patterns','mathlib-review-stages']]
put('instructions-read.json',[dict(path=s,sha256=sha(Path(s)),bytes=Path(s).stat().st_size)for s in paths])
put('source-reading.json',dict(full_modules=['Roth/Main.lean','Roth/LeanEval.lean'],target_lines=[142,147],direct_written_caller=dict(name='Roth.exists_roth_parameters_aux',visibility='private',file='Roth/Main.lean',line=410),original_replay_scope='Exact target only in Monic272Original; no private helper closure needed; only declaration head renamed replay and namespace introduced. Public original mathlib/project environment remains loaded.',caller_replay_scope='Full actual private parameter caller with padding inlined. Four unrelated private helper bodies copied exactly apart from private visibility. Full roth_of_isIntegral, roth, roth_rat and final LeanEval theorem. No production mutation.',original_kernel_project_dependencies=[]))
put('optional-math-opinion.json',dict(status='n/a',reason='ask_chatgpt_math unavailable; optional channel only, all named remaining channels executed'))
print('collected exact search/source evidence')
