from pathlib import Path
import json,hashlib,shutil,subprocess,re
D=Path(__file__).parent;ROOT=Path('/Users/ramin/LEAN/Roth');N='Roth.coeff_coeffNone'
def dump(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def receipt(n,cmd):
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);dump(n,{'command':cmd,'cwd':str(ROOT),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr});return r
for n in ['input-manifest.json','baseline-build.txt']:
 shutil.copyfile(ROOT/'.mathlib-quality/overview/evidence/shared'/n,D/n)
for p in Path('/private/tmp/roth-overview').glob('coeff-coeffnone-*'):
 if p.is_file():shutil.copyfile(p,D/p.name)
for n in ['index-file-completion-2026-10-27.json','index-file-completion-2026-10-27.log']:
 shutil.copyfile(Path('/private/tmp/roth-overview')/n,D/n)
base=json.loads((D/'input-manifest.json').read_text())['sources_and_pins'];inputs=[]
for f,v in base.items():
 p=ROOT/f;inputs.append({'path':f,'sha256':sha(p),'expected_sha256':v['sha256'],'bytes':p.stat().st_size,'match':sha(p)==v['sha256']})
assert len(inputs)==17 and all(x['match'] for x in inputs);dump('inputs.json',inputs)
order=json.loads((ROOT/'.mathlib-quality/overview/declaration-order.json').read_text());dump('canonical-order.json',order);dump('canonical-target.json',order[154]);assert order[154]['name']==N
src={}
for f in ['Roth/Separation.lean']:
 out=f.replace('/','-')+'.txt';shutil.copyfile(ROOT/f,D/out);src[f]=out
dump('source-links.json',src)
files=sorted(set(x['file'] for x in order));lex=[]
for f in files:
 p=ROOT/f;occ=[{'line':i,'text':l} for i,l in enumerate(p.read_text().splitlines(),1) if re.search(r'\bcoeff_coeffNone\b',l)]
 lex.append({'path':f,'sha256':sha(p),'occurrences':occ})
dump('lexical-enumeration.json',{'files':lex})
receipt('caller-rg.json',['rg','--no-ignore','-n',r'\bcoeff_coeffNone\b','Roth','Roth.lean'])
receipt('caller-git-grep.json',['git','grep','-n','-w','coeff_coeffNone','--','Roth/*.lean','Roth.lean'])
for form,pat in [('current','coeff_coeffNone|optionEquivLeft_coeff_coeff'),('literature','optionEquivLeft_coeff_some_coeff_none|optionEquivLeft_monomial'),('modern','coeff_coeff_optionEquivLeft|optionElim|embDomain_eq_mapDomain')]:
 receipt('rg-'+form+'.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Equiv.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Option.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Defs.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Equiv.lean'])
receipt('rg-inline.json',['rg','--no-ignore','-n','optionEquivLeft_coeff|coeffNone.*coeff|mapDomain some.*single none','Roth','Roth.lean'])
receipt('local-literature-search.json',['rg','-n','collecting|roth:lem2|coefficient','.mathlib-quality/references/clean.tex'])
lines=(ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines();(D/'clean-separation-excerpt.tex.txt').write_text('\n'.join(lines[346:396])+'\n')
paths=['.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Equiv.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Option.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Defs.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries/Equiv.lean','.mathlib-quality/references/clean.tex']
dump('mathlib-inputs.json',[{'path':f,'sha256':sha(ROOT/f),'bytes':(ROOT/f).stat().st_size} for f in paths])
raw=json.loads((D/'coeff-coeffnone-original-audit-receipt.json').read_text());z=raw['result']['structuredContent']['result'];typ=next(x['message'] for x in z['items'] if x.get('line')==5354);dump('native-type.json',{'type':typ})
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
dump('assessment.json',{'declaration':N,'canonical_index':155,'source':'Roth/Separation.lean:85','kind':'theorem','verdict':'NO-mathlib-has-it','completed':True,'allphases':'PASS','phases':{x:'PASS' for x in ph},'phase_justifications':{'2b':'n/a theorem','3.optional':'ask_chatgpt_math unavailable','4.5':'n/a theorem; no new definitional equality or instance path','4b':'MAXIMALLY GENERAL for fixed coeffNone/optionEquivLeft surface; no verified weakening proposed','6':'Existing canonical coefficient law independently verified. Old expanded coordinate spelling requires four named mathlib ingredients and a real normalization bridge; not claimed a <=3-call old-form composition.'},'unresolved':[],'root_acceptance':'pending'})
callers=['Roth.eq_sum_X_none_pow_mul_coeffNone','Roth.coeff_rename_mul_aeval']
dump('overview-entry.json',{'kind':'theorem','type':typ,'what':'Extracting exponent d from the coefficient polynomial at distinguished exponent ν recovers the original coefficient at those combined exponents.','how':'Unfold coeffNone, rewrite optionEquivLeft_coeff_coeff, normalize the Option multi-index pointwise.','hypotheses':['τ : Type u_1, R : Type u_2','CommSemiring R','P : MvPolynomial (Option τ) R; ν : ℕ; d : τ →₀ ℕ','No Fintype τ or DecidableEq τ'], 'project_dependencies':['Roth.coeffNone'],'caller_summary':{'explicit_call_sites':[{'file':'Roth/Separation.lean','line':107,'caller':callers[0]},{'file':'Roth/Separation.lean','line':129,'caller':callers[1]}],'internal_use_count_excluding_declaring_file':0,'same_file_count':2,'direct_kernel_value_consumers':callers,'inline_derivations':'Private coeff_X_none_pow_mul_rename and degreeOf_coeffNone_le use canonical coefficient/support API, not duplicate full target.'},'mathlib_api_audit':{'canonical':'MvPolynomial.optionEquivLeft_coeff_coeff','canonical_path':'Mathlib/Algebra/MvPolynomial/Equiv.lean:610','canonical_existing_calls':1,'old_form_existing_calls':4,'old_form_ingredients':['MvPolynomial.optionEquivLeft_coeff_coeff','Finsupp.update_eq_add_single','Finsupp.embDomain_some_none','Finsupp.embDomain_eq_mapDomain'],'representation':'optionElim versus mapDomain some + single none is propositional normalization, not definitional equality'},'moral_duplications':['The existing canonical coefficient correspondence is the same mathematical law under normalized exponent coordinates.'],'generalization':{'status':'MAXIMALLY GENERAL for fixed parent interface','canonical_surface':'CommSemiring R; arbitrary variable type and independent universes','expanded_representation':'Underlying finitely supported coefficient slicing can be considered under weaker algebraic data, but this changes the parent representation and is not a verified weakening of coeffNone.'},'missing_api':'No missing coefficient law. An optional named Option-index bridge is a separate normal-form API question.','junk':'Useful: two explicit callers and two direct kernel-value consumers.','action':'Delete only after refactoring both callers: eqsum uses optionEquivLeft_coeff_some_coeff_none; coefficient product uses optionElim normalization then optionEquivLeft_coeff_coeff. Both full caller replays passed. Optional local exposition belongs in Roth/Separation.lean.'})
accepted=[]
for label,src,rec,fmt,start,infos in [
 ('original','coeff-coeffnone-original-executed.lean.txt','coeff-coeffnone-original-audit-receipt.json','disk',5354,['@Roth.coeff_coeffNone',"'Roth.coeff_coeffNone' depends on axioms:"]),
 ('canonical-audit','coeff-coeffnone-original-executed.lean.txt','coeff-coeffnone-original-audit-receipt.json','disk',5357,['COEFF_COEFF_NONE155_AUDIT: requested=293; unique=293','COEFF_COEFF_NONE155_AUDIT_PRESENT: present=293; values=293']+['COEFF_COEFF_NONE155_DIRECT_CONSUMER: '+x for x in callers]),
 ('isolated','coeff-coeffnone-isolated-executed.lean.txt','coeff-coeffnone-isolated-receipt.json','raw',1,["'CoeffCoeffNone155."+x+"' depends on axioms:" for x in ['canonical','embedding','mapped','omission_guard','wrong_power_guard']]),
 ('both-callers','coeff-coeffnone-callers-executed.lean.txt','coeff-coeffnone-callers-receipt.json','disk',5676,["'CoeffCoeffNone155Replay."+x+"' depends on axioms:" for x in ['eq_sum_X_none_pow_mul_coeffNone','coeff_rename_mul_aeval']])]:
 accepted.append({'label':label,'source':src,'receipt':rec,'format':fmt,'native_region_start_line':start,'required_info':infos,'source_sha256':sha(D/src)})
dump('verification.json',{'declaration':N,'accepted':accepted,'rejected':[{'source':'coeff-coeffnone-isolated-initial-executed.lean.txt','receipt':'coeff-coeffnone-isolated-initial-receipt.json','reason':'Omission guard parsed mapDomain partially; recovered sorryAx not accepted. Root repaired parentheses; substantive replacement proofs unchanged.'}],'unresolved':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'audit':{'source':'coeff-coeffnone-audit-executed.lean.txt','whole_source':'coeff-coeffnone-original-executed.lean.txt','start_line':5357,'canonical_order':'canonical-order.json'},'full_build':{'receipt':'index-file-completion-2026-10-27.json','log':'index-file-completion-2026-10-27.log','source_hashes_match_baseline':True},'read_only':True})
for n in ['coeff-none-pullback-guarded-executed.lean.txt','coeff-none-pullback-guarded-receipt.json']:
 shutil.copyfile(Path('/private/tmp/roth-overview')/n,D/n)
v=json.loads((D/'verification.json').read_text());s='coeff-none-pullback-guarded-executed.lean.txt'
v['accepted'].append({'label':'prior152-zero-pullback','source':s,'receipt':'coeff-none-pullback-guarded-receipt.json','format':'raw-prior152','native_region_start_line':1,'source_sha256':sha(D/s),'required_info':["'CoeffNonePullbackGuarded152."+x+"' depends on axioms:" for x in ['coordinateInjective','slice','slice_apply','direct_coeff']]});dump('verification.json',v)
o=json.loads((D/'overview-entry.json').read_text());o['generalization']['expanded_representation']='Zero A suffices for underlying coefficient slicing by Finsupp.comapDomain; prior152 actual slice_apply and direct_coeff bridge reused with freshly matching17source/pin hashes. This is a wider representation, not a mechanical weakening of the fixed coeffNone interface.';o['mathlib_api_audit']['abstract']='Finsupp.comapDomain_apply at Mathlib/Data/Finsupp/Basic.lean:517';dump('overview-entry.json',o)
paths.append('.lake/packages/mathlib/Mathlib/Algebra/Group/Finsupp.lean');dump('mathlib-inputs.json',[{'path':f,'sha256':sha(ROOT/f),'bytes':(ROOT/f).stat().st_size} for f in paths])
receipt('rg-zero.json',['rg','-n','comapDomain_apply|def comapDomain|theorem comapDomain','.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean'])
