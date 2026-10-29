from pathlib import Path
import json,re,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_degrees'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,args):
 r=subprocess.run(args,cwd=R,text=True,capture_output=True);put(n,dict(request=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));return r
for m in ['Main','LeanEval']:(D/('source-'+m+'.lean.txt')).write_bytes((R/('Roth/'+m+'.lean')).read_bytes())
run('source-search.json',['rg','--no-ignore','-n','exists_degrees','Roth','Roth.lean'])
run('tracked-source-search.json',['git','grep','-n','exists_degrees','--','Roth/*.lean','Roth.lean'])
run('inline-search.json',['rg','--no-ignore','-n',r'ceil_lt_add_one|sup.*10.*δ|r j.*Real.log|⌈s \*','Roth','Roth.lean'])
forms={'current':r'exists_degrees|balanced.*degree|degree.*round',
 'standard':r'tendsto_nat_ceil_mul_div_atTop|ceil_lt_add_one|ceil_natCast|theorem le_ceil',
 'abstract':r'exists_nat_gt|sup.*univ|exists.*(ceil|balanced)|round.*(weight|finite)'}
for f,p in forms.items():run('formal-'+f+'-rg.json',['rg','-n',p,'.lake/packages/mathlib/Mathlib'])
run('name-search.json',['rg','-n',r'Roth\.exists_degrees|theorem exists_degrees|lemma exists_degrees|theorem exists_balanced_nat_multiples|theorem exists_separated_nat_multiples','.lake/packages/mathlib/Mathlib'])
run('literature-local.json',['rg','-n',r'roth:eq5[123]|rounding lemma|define.*r_j','.mathlib-quality/references/clean.tex'])
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1607:1646])+'\n')
paths=['Mathlib/Algebra/Order/Floor/Semiring.lean','Mathlib/Algebra/Order/Archimedean/Defs.lean','Mathlib/Order/ConditionallyCompleteLattice/Finset.lean','Mathlib/Analysis/SpecificLimits/Basic.lean','Mathlib/NumberTheory/DiophantineApproximation/Basic.lean']
xs=[]
for i,p in enumerate(paths):
 q=R/'.lake/packages/mathlib'/p;a='mathlib-source-'+str(i)+'.lean.txt';(D/a).write_bytes(q.read_bytes());xs.append(dict(path=str(q.relative_to(R)),archive=a,sha256=sha(q),bytes=q.stat().st_size))
put('mathlib-inputs.json',xs)
run('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-12','--format=%h %as %an %s','--','Mathlib/Algebra/Order/Floor','Mathlib/Algebra/Order/Archimedean','Mathlib/Analysis/SpecificLimits/Basic.lean'])
progress=json.loads((R/'.mathlib-quality/overview/progress.json').read_text());put('progress-snapshot.json',progress)
body=json.loads((D/'target-metadata.json').read_text())['body']
put('concrete-diagnostic.json',dict(identifiers={x:dict(lines=sum(x in l for l in body.splitlines()),occurrences=body.count(x))for x in ['Real.log','q ','hδ1','Finset.univ','Nat.ceil']},diagnostic='Real.log occurs only in positivity at the start after defining ℓ. The scale and rounding proof uses arbitrary positive weights; no integrality of q beyond log positivity. δ≤1 occurs only in final factor estimate.'))
put('callers.json',dict(explicit_caller_count=1,external_to_file_count=0,callers=[dict(name='Roth.exists_roth_approximants_aux',file='Roth/Main.lean',declaration_line=429,declaration_end_line=450,call_line=440)],reading=['Entire Roth/Main.lean1–588','Entire Roth/LeanEval.lean1–73'],verification_scope='Full actual caller literal inline and all-positive-delta replacement, exact original caller signature equality. hδ1 remains needed for caller antitonicity and last degree>=3; no claim it can be removed there.'))
print('Collected fresh source/formal/local receipts')
