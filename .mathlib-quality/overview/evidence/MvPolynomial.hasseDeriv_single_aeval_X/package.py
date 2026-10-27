from pathlib import Path
import json, hashlib
p=Path(__file__).resolve().parent
r=Path('/Users/ramin/LEAN/Roth')
tmp=Path('/private/tmp/roth-overview')
target='MvPolynomial.hasseDeriv_single_aeval_X'
def dump(n,v): (p/n).write_text(json.dumps(v,indent=2,ensure_ascii=True)+'\n')
def sha(f): return hashlib.sha256(f.read_bytes()).hexdigest()
for src,dst in [('hasseSingle-pinned-success.json','disk-success.json'),('hasseSingle-pinned-executed.lean.txt','disk-executed.lean.txt'),('hasseSingle-minimal-success.json','minimal-success.json'),('hasseSingle-minimal-executed.lean.txt','minimal-executed.lean.txt'),('hasseSingle-guard-rejected.json','guard-rejected.json'),('hasseSingle-guard-rejected.lean.txt','guard-rejected.lean.txt')]:
 (p/dst).write_bytes((tmp/src).read_bytes())
disk=r/'.lake/roth-overview-session/NextHasseChecks.lean'
dump('disk-source-check.json',{'original_execution_path':str(disk.relative_to(r)),'matched_at_freeze':disk.read_bytes()==(p/'disk-executed.lean.txt').read_bytes(),'disk_sha256':sha(disk),'retained_sha256':sha(p/'disk-executed.lean.txt')})
assert disk.read_bytes()==(p/'disk-executed.lean.txt').read_bytes()
progress=json.loads((r/'.mathlib-quality/overview/progress.json').read_text())
dump('progress-read.json',progress)
accepted=[]
for stem,desc in [('disk','Full target replay, bundled square, actual Option.none caller and arbitrary-image counterexample'),('raw','Mathlib-only raw operator and monomial/induction proof'),('minimal','Mathlib-only raw definition, existing basis extensionality and closing definition simp')]:
 e={'source':stem+'-executed.lean.txt','source_sha256':sha(p/(stem+'-executed.lean.txt')),'receipt':stem+'-success.json','description':desc,'original_execution_path':str(disk.relative_to(r)) if stem=='disk' else 'virtual mathlib-only lean_run_code'}
 if stem=='disk':e['source_check']='disk-source-check.json'
 accepted.append(e)
dump('verification.json',{'declaration':target,'accepted':accepted,'rejected':[{'source':'guard-rejected.lean.txt','receipt':'guard-rejected.json','reason':'Arbitrary-image counterexample needed explicit Polynomial Nat annotations; failed version is not accepted proof evidence.'}],'unresolved':[],'root_native_complete':True,'standard_axioms_only':['propext','Classical.choice','Quot.sound'],'caller_scope':'One literal Option.none bridge instantiation; no full downstream module rebuild claimed.'})
phases={x:'PASS' for x in ['0','1','2','3','4a','4b','4c','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='N/A: theorem introduces no definition, instance, coercion, or typeclass infrastructure'
group=['MvPolynomial.hasseDeriv','MvPolynomial.coeff_hasseDeriv','MvPolynomial.hasseDeriv_map','MvPolynomial.hasseDeriv_rename','MvPolynomial.hasseDeriv_hasseDeriv','MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint','MvPolynomial.pderiv_hasseDeriv','MvPolynomial.degreeOf_hasseDeriv_le','MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt','MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero']
dump('assessment.json',{'schema_version':1,'declaration':target,'source':'Roth/HasseDeriv.lean','line':253,'canonical_index':22,'kind':'theorem','mode':'full-mathlibable','verdict':'BORDERLINE-needs-human','completed':True,'root_acceptance':'pending','production_edits':False,'pins_unchanged':True,'unresolved':[],'phases':phases,'size':'BIG','generality':'MAXIMALLY GENERAL within fixed canonical parent interface','modern_idiom':'Equivalent bundled linear-map square; no verified semantic weakening','composition':'Phase6b closing-definition-simp after existing polynomial monomial-basis extensionality','explicit_callers':1,'questions':['Expose public coordinate compatibility despite closing-simp proof?','Use aeval X or toMvPolynomial as primary spelling?','Include bundled square alongside pointwise rewrite?'],'missing_api':'A public compatibility lemma for the proposed multivariate Hasse operator and existing univariate Hasse derivative','upstream':{'file':'Mathlib/Algebra/MvPolynomial/HasseDeriv.lean','pr_title':'feat(Algebra/MvPolynomial): add multivariate Hasse derivatives and univariate compatibility','group_with':group,'reviewer_candidates':['Moritz Firsching','Yael Dillies','Nathanael Thompson'],'checklist':['/generalise '+target,'/cleanup Roth/HasseDeriv.lean '+target,'/pre-submit']}})
dump('overview-entry.json',{'declaration':target,'type':'theorem','what':'The coordinate embedding of univariate polynomials intertwines Hasse derivatives.','how':'Additive/monomial induction; alternatively existing monomial-basis extensionality and closing definition simp.','hypotheses':['arbitrary sigma and R universes','CommSemiring R','j : sigma','n : Nat','f : Polynomial R'],'project_dependencies':['MvPolynomial.hasseDeriv','MvPolynomial.hasseDeriv_monomial','MvPolynomial.hasseCoeff'],'caller_summary':{'count':1,'sites':['Roth/Separation.lean:160'],'detail':'Roth.hasseDeriv_rename_mul_aeval uses j=none; compiled literal instance.'},'mathlib_api_audit':'All five methods on current/literature/abstract forms; positive toMvPolynomial and monomial/ext API, no existing Hasse bridge; local indexes unavailable.','moral_duplications':'A short basis-ext and definition-simp proof exists; Phase6b review case.','generalization':'No verified weakening under canonical parent; bundled square is equivalent.','missing_api':'Public coordinate compatibility API for new multivariate Hasse derivatives, subject to packing decision.','junk':'Not dead: one explicit consumer; no inline duplicate located.','action':'BORDERLINE-needs-human: settle three public API questions; retain local theorem meanwhile, or localize verified basis proof at Separation:160.'})
entries=[]
for f in sorted(p.iterdir()):
 if f.is_file() and f.name not in ['copy-manifest.json','worker-copy-manifest.json','root-review.json']:
  dest='.mathlib-quality/overview/'+('mathlibable/'+target+'.md' if f.name=='report.md' else 'evidence/'+target+'/'+f.name)
  entries.append({'source':f.name,'destination':dest,'sha256':sha(f),'bytes':f.stat().st_size})
dump('copy-manifest.json',{'declaration':target,'files':entries})
