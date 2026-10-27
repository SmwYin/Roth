from pathlib import Path
import json,hashlib,shutil,subprocess
P=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.sqrt_one_sub_inv_lt'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def write(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
for f in Path('/private/tmp/roth-overview').glob('sqrt-one-sub-inv-*'):
 if f.is_file():shutil.copy2(f,P/f.name)
accepted=[];rejected=[]
def add(label,prefix,region,axioms,kind='persistent-disk',good=True,reason=None):
 s='sqrt-one-sub-inv-'+prefix+'-executed.lean.txt';rc='sqrt-one-sub-inv-'+prefix+'-receipt.json';r=load(P/rc)
 x={'label':label,'source':s,'source_sha256':sha(P/s),'receipt':rc,'original_execution_request':r['request'],'execution_kind':kind,'native_region_start_line':region,'expected_axiom_declarations':axioms}
 if reason:x['reason']=reason
 (accepted if good else rejected).append(x)
add('original','original',9545,[N])
add('audit','audit',9549,[])
add('raw-clean','raw-clean',1,['SqrtAssessment.realWeak','SqrtAssessment.tangent','SqrtAssessment.originalViaTangent'],'run-code')
add('actual-caller','consumer',9898,['Roth.SqrtActualCaller.actualCaller'])
add('warm-support','warm',9868,['SqrtAssessment.realWeak','SqrtAssessment.tangent','SqrtAssessment.originalViaTangent'])
add('guards','guards',1,['SqrtGuards.zero_m_false','SqrtGuards.no_lambda_bound','SqrtGuards.generic_square'],'run-code')
add('initial-proof','raw',1,[],'run-code',False,'Initial realWeak and Bernoulli proof omitted explicit positivity of 1/m needed by arithmetic automation; theorem indentation linter warning. Rejected receipt contains recovered sorryAx; no part is accepted proof evidence. Clean rerun includes one_div_pos.')
# Root supplies an isolated direct-search native receipt; expected errors remain rejected experiments.
if (P/'sqrt-one-sub-inv-direct-search-receipt.json').exists():
 add('direct-search','direct-search',1,[],'run-code',False,'Direct exact? experiments on original and real-m shape; these do not prove absence. Existing standard tangent query is a positive search within the same run.')
write('verification.json',{'declaration':N,'accepted':accepted,'rejected':rejected,'unresolved':[],'production_unchanged':True,'standard_axioms':['propext','Classical.choice','Quot.sound'],'canonical_direct_consumers':['Roth.sum_inv_lt'],'notes':['Persistent disk includes historical info: required assertions scoped to fresh region; full-file errors/warnings/axioms still checked.','Original print body elides94563 characters at MCP output limit; complete source, full type, standard axioms and canonical kernel-value existence audited.','Minimal isolated Mathlib.Analysis.Real.Sqrt+Tactic has guarded missing Roth target.','No self-import supplies accepted generic realWeak proof. Actual caller uses its already verified independent proof.','Preparation-only guards changed obsolete LinearOrderedField syntax before native execution; the old guards.lean.txt is preparation, not a rejected native run.','Exact? failures are limited direct search experiments, not proofs of absence.']})
a=load(P/'assessment.json');a.update(completed=True,allphases='PASS',unresolved=[]);write('assessment.json',a)
script=R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'
z=subprocess.run(['python3',str(script),str(P)],capture_output=True,text=True)
write('secrets-scan.json',{'command':['python3',str(script),str(P)],'returncode':z.returncode,'stdout':z.stdout,'stderr':z.stderr,'script_sha256':sha(script)})
assert z.returncode==0,z.stdout
files=[]
for f in sorted(P.iterdir()):
 if not f.is_file() or f.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst='.mathlib-quality/overview/mathlibable/'+N+'.md' if f.name=='report.md' else '.mathlib-quality/overview/evidence/'+N+'/'+f.name
 files.append({'source':str(f),'destination':dst,'sha256':sha(f),'bytes':f.stat().st_size})
write('copy-manifest.json',{'declaration':N,'files':files})
