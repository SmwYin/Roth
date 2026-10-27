from pathlib import Path
import json,hashlib,shutil,subprocess
P=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.sum_inv_lt'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def write(n,x):(P/n).write_text(json.dumps(x,indent=2)+'\n')
for f in Path('/private/tmp/roth-overview').glob('sum-inv-lt-*'):
 if f.is_file():shutil.copy2(f,P/f.name)
accepted=[];rejected=[]
def add(label,prefix,region,axioms,kind='persistent-disk',good=True,reason=None):
 s='sum-inv-lt-'+prefix+'-executed.lean.txt';rc='sum-inv-lt-'+prefix+'-receipt.json';r=load(P/rc)
 x={'label':label,'source':s,'source_sha256':sha(P/s),'receipt':rc,'original_execution_request':r['request'],'execution_kind':kind,'native_region_start_line':region,'expected_axiom_declarations':axioms}
 if reason:x['reason']=reason
 (accepted if good else rejected).append(x)
add('original','original',10991,[N])
add('audit','audit',10995,[])
add('real-generalization','real',11314,['Roth.SumInvAssessment.realWeak'])
add('actual-caller','consumer',11349,['Roth.SumInvCaller.actualCaller'])
add('helpers','helpers',1,['SumInvHelpers.inv_add_inv_le','SumInvHelpers.sum_inv_le'],'run-code')
add('guards','guards',1,['SumInvGuards.r_zero_false','SumInvGuards.m_one_false','SumInvGuards.no_lambda_bound'],'run-code')
add('raw-generalization','raw-generalization-clean',1,['SumInvHelpers.inv_add_inv_le','SumInvHelpers.sum_inv_le','SumInvHelpers.sqrtWeak','SumInvHelpers.realWeak'],'run-code')
add('abstract-convex','abstract-convex-clean',1,['SumInvAbstract.inverseConvex','SumInvAbstract.convexPair','SumInvAbstract.reflectedSum'],'run-code')
add('direct-search','direct-search',1,[],'run-code',False,'Three limited exact? attempts on original, rational-grid and abstract reflected-pair shapes failed; not proof of global absence.')
add('initial-raw-generalization','raw-generalization',1,[],'run-code',False,'New helper requires 1<lam but initial argument was hlam2:2<lam. Failed theorem contains recovered sorryAx and is rejected. Explicit linarith implication is used in accepted clean run.')
add('initial-abstract-convex','abstract-convex',1,[],'run-code',False,'ReflectedSum initial arithmetic goal retained Nat.cast(r+1) rather than cast(r)+1. Failed theorem contains recovered sorryAx and is rejected. Accepted rerun adds push_cast at hh.')
write('verification.json',{'declaration':N,'accepted':accepted,'rejected':rejected,'unresolved':[],'production_unchanged':True,'standard_axioms':['propext','Classical.choice','Quot.sound'],'canonical_direct_consumers':['_private.Roth.Lattice.0.Roth.card_filter_weight_le_succ_aux'],'notes':['Full type/check/standard axioms/kernel value verified; original print body internally elides53225 characters at MCP output limit. Complete production source preserved.','Required fresh assertions scoped to native_region_start_line; full native error/warning/axiom checks retained.','Fully isolated accepted raw theorem guards missing Roth target and independently reproves all helpers; original Roth not imported.','Abstract inverse convexity uses existing convexOn_zpow; convexPair/reflectedSum are NEW proof content, not existing replacements.','Sole actual consumer fully replayed with only target-call replacement and actual private fiber access elaborator.']})
a=load(P/'assessment.json');a.update(completed=True,allphases='PASS',unresolved=[]);write('assessment.json',a)
type_='Roth.sum_inv_lt {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √↑m < lam) : ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ < lam⁻¹ * (√(↑m - 1))⁻¹ * √↑m * (↑r + 1)'
write('overview-entry.json',{'declaration':N,'canonical_index':123,'kind':'theorem','type':type_,'what':'Strict bound for reciprocal arithmetic-grid sum by (r+1)√m/(λ√(m−1)), for r≥1,m≥2,λ>2√m.','how':'Pair j with r−j to obtain rational endpoint bound; compare 1−λ⁻² with √(1−1/m), then normalize roots/inverses.','hypotheses':['r,m:ℕ','1≤r','2≤m','lam:ℝ','2√m<lam'],'project_dependencies':['private Roth.sum_inv_le','Roth.sqrt_one_sub_inv_lt'],'caller_summary':{'explicit_source_callers':[{'file':'Roth/Lattice.lean','line':173,'declaration':'Roth.card_filter_weight_le_succ_aux','visibility':'private'}],'external_to_file':0,'canonical_kernel_direct_consumers':['_private.Roth.Lattice.0.Roth.card_filter_weight_le_succ_aux'],'scope':'Source refs and exact canonical direct value dependencies; not transitive simp/kernel closure.'},'mathlib_api_audit':'All five methods on current, convex-endpoint literature and abstract symmetric-pair forms; local index unavailable. Pinned convexOn_zpow, chord and reflection APIs provide partial blocks; no existing ≤3-call replacement established. Three exact? failures not treated as absence proof.','moral_duplications':'Reciprocal convexity already follows from convexOn_zpow(-1); sum reindexing exists. Grid rational upper bound and sqrt comparison still need proof.','generalization':'Verified real m>1 and weak2√m≤lam preserve strict conclusion; both private pair/grid proofs work for1<lam. Independent raw proof and sole caller replay clean.','missing_api':'Candidate generic convex symmetric-average endpoint theorem or positive reciprocal-grid rational bound; exact sqrt corollary may remain downstream.','junk':'Not dead: one private induction caller supports public lattice-count estimate. No duplicate full inline derivation found.','action':'BORDERLINE-needs-human: decide generic convex versus rational-grid API and whether sqrt corollary belongs upstream; preserve verified real/weak threshold if exposed.','verdict':'BORDERLINE-needs-human'})
script=R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py';z=subprocess.run(['python3',str(script),str(P)],capture_output=True,text=True);write('secrets-scan.json',{'command':['python3',str(script),str(P)],'returncode':z.returncode,'stdout':z.stdout,'stderr':z.stderr,'script_sha256':sha(script)});assert z.returncode==0,z.stdout
files=[]
for f in sorted(P.iterdir()):
 if not f.is_file() or f.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst='.mathlib-quality/overview/mathlibable/'+N+'.md' if f.name=='report.md' else '.mathlib-quality/overview/evidence/'+N+'/'+f.name
 files.append({'source':str(f),'destination':dst,'sha256':sha(f),'bytes':f.stat().st_size})
write('copy-manifest.json',{'declaration':N,'files':files})
