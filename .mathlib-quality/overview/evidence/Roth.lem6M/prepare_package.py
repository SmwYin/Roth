from pathlib import Path
import json,hashlib,re,shutil
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.lem6M'
def put(n,x): (D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=json.loads((D/n).read_text())['result']['structuredContent'];return z.get('result',z)
z=result('lem6m182-original-receipt.json');msgs=[x['message']for x in z['items']]
for typ,marker in [('direct-consumers','LEM6M182_DIRECT_CONSUMER: '),('direct-type-consumers','LEM6M182_DIRECT_TYPE_CONSUMER: ')]:put(typ+'.json',[x[len(marker):]for x in msgs if x.startswith(marker)])
put('native-type.json',{'type':'ℕ → ℕ → ℝ → ℕ → ℝ','body':'fun p r₁ B l ↦ (↑r₁ + 1) ^ (p * l) * ↑l.factorial * B ^ l * 2 ^ (p * l * r₁)','axioms':['propext','Classical.choice','Quot.sound']})
put('local-literature.json',{'source':'.mathlib-quality/references/clean.tex','sha256':sha(R/'.mathlib-quality/references/clean.tex'),'locator':'§5 Lemma6,eq16,lines704–744','summary':'Exact stated formula, followed by comparison with product of individual degree bounds. It is a chosen convenient envelope, not a minimal constant.','ask_chatgpt_math':'unavailable'})
cs=[];s=(R/'Roth/Theta.lean').read_text().splitlines()
for line in json.loads((D/'callers.json').read_text())['stdout'].splitlines():
 f,num,txt=line.split(':',2);i=int(num)
 if i in [29,270]:continue
 start=max(j for j in range(i)if re.match(r'(?:private )?(?:lemma|theorem|noncomputable def) ',s[j]))
 decl=re.search(r'(?:lemma|theorem|def) (\S+)',s[start]).group(1)
 cs.append({'file':f,'line':i,'declaration':decl,'excerpt':txt})
put('callers-structured.json',cs)
put('inline-audit.json',{'inventory':['Roth.lean']+[str(p)for p in sorted((R/'Roth').glob('*.lean'))],'target_pattern':'\\blem6M\\b','all_explicit_callers_in':'Roth/Theta.lean','inline_rederivations':'No independent full-form redefinition. Definitional normalization at280,473,662; partial natural prefactor at609 is an inequality helper, not duplicate definition.','source_caller_declarations':sorted(set(x['declaration']for x in cs)),'semantic_calls':len(cs),'external_to_declaring_file':0})
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
put('assessment.json',{'declaration':N,'canonical_index':182,'source':'Roth/Theta.lean:270','verdict':'BORDERLINE-needs-human','completed':True,'allphases':'PASS','phases':dict.fromkeys(ph,'PASS'),'unresolved':[],'root_acceptance':'pending','classification':'SMALL','one_line':'WITH-EXEMPTION: local semantic API','risk':'LOW'})
accepted=[]
for label,fmt,req in [('original','disk',['LEM6M182_FULL_TYPE: ℕ → ℕ → ℝ → ℕ → ℝ','LEM6M182_AUDIT: requested=293; unique=293','LEM6M182_AUDIT_PRESENT: present=293; values=293']),('project','disk',["'Lem6M182.one_le_inline' depends on axioms:"]),('isolated','raw',["'Lem6M182Isolated.formula' depends on axioms: [propext]",'@Nat.cast_pow','Nat.factorial : ℕ → ℕ'])]:
 source=f'lem6m182-{label}-executed.lean.txt';region=1 if fmt=='raw'else int((D/f'lem6m182-{label}-region.txt').read_text())
 accepted.append({'label':label,'format':fmt,'source':source,'source_sha256':sha(D/source),'receipt':f'lem6m182-{label}-receipt.json','native_region_start_line':region,'required_info':req})
put('verification.json',{'declaration':N,'accepted':accepted,'rejected':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'unresolved':[],'audit':{'source':'lem6m182-audit-executed.lean.txt','exact_order':True,'count':293,'unique':293},'canonical_direct_consumers':json.loads((D/'direct-consumers.json').read_text()),'canonical_direct_type_consumers':json.loads((D/'direct-type-consumers.json').read_text()),'composition':'No <=3-existing-call term identified; arithmetic formula expansion is not such a term.'})
put('overview-entry.json',{'declaration':N,'kind':'def','type':'ℕ → ℕ → ℝ → ℕ → ℝ','what':'Auxiliary coefficient envelope M=(r₁+1)^(pl) l! B^l 2^(plr₁) for Roth Lemma6.','how':'One arithmetic expression using natural casts, powers, factorial and multiplication.','hypotheses':'p,r₁,l natural; B arbitrary real; no positivity, finiteness or DecidableEq assumptions.','project_dependencies':[],'caller_summary':'Six explicit caller declarations, all Theta; seven direct kernel-value and six direct kernel-type consumers.','mathlib_api_audit':'Five methods on current/standard/abstract forms; arithmetic primitives confirmed; no identified existing parameterized bound.','moral_duplications':'Chosen majorant of determinant coefficient estimate; not Matrix.det_le, whose hypotheses and object differ.','generalization':'Semiring expression compiles; representation expansion only, not literature-standard replacement or suggested new upstream definition.','missing_api':'Upstream packaging of auxiliary polynomial height/index infrastructure is a design question; later declarations assessed independently.','junk':'Retain locally: live semantic API used on19 source lines by six declarations; not dead code.','action':'Retain locally; BORDERLINE standalone upstream status pending concrete scope decisions.'})
inputs=[]
for path in ['Mathlib/Data/Nat/Factorial/Basic.lean','Mathlib/Algebra/Order/GroupWithZero/Basic.lean','Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean']:
 p=R/'.lake/packages/mathlib'/path;archive='mathlib-'+path.replace('/','-')+'.txt';shutil.copyfile(p,D/archive);inputs.append({'path':path,'archive':archive,'sha256':sha(p),'bytes':p.stat().st_size})
put('mathlib-inputs.json',inputs)
print('callers',len(cs),'decls',sorted(set(x['declaration']for x in cs)))
