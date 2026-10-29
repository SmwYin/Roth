from pathlib import Path
import json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index')
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2)+'\n')
def run(n,args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);dump(n,dict(request=args,status=p.returncode,stdout=p.stdout,stderr=p.stderr));return p.stdout
for form,pat in [('current','abs_eval_lt_of_le_index|abs.*eval.*index|index.*eval.*bound'),('standard','taylor.*(bound|coeff)|eval.*(bound|le)|weightedOrder'),('abstract','sum_lt_sum_of_nonempty|abs_sum_le_sum_abs|rpow_sum_of_pos|rpow_le_rpow_of_nonpos')]:
 run('formal-'+form+'-rg.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/Taylor.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPowerSeries','.lake/packages/mathlib/Mathlib/Algebra/Order','.lake/packages/mathlib/Mathlib/Analysis/SpecialFunctions/Pow'])
run('source-search.json',['rg','--no-ignore','-n','abs_eval_lt_of_le_index','Roth','Roth.lean'])
run('tracked-source-search.json',['git','grep','-n','abs_eval_lt_of_le_index','--','Roth','Roth.lean'])
run('inline-search.json',['rg','--no-ignore','-n','abs_sum_le_sum_abs|sum_lt_sum_of_nonempty|eval_eq_sum_box|abs_prod_pow_le_rpow_of_le_weight','Roth','Roth.lean'])
run('literature-local.json',['rg','-n','By \\(1\\)|Taylor expansion|Taylor.s expansion|terms with|gamma.*eta|r_1.*1.*r_m','.mathlib-quality/references/clean.tex'])
run('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-8','--format=%H %ad %an %s','--date=short','--','Mathlib/Algebra/Polynomial/Taylor.lean','Mathlib/Algebra/MvPolynomial/Eval.lean','Mathlib/Analysis/SpecialFunctions/Pow/Real.lean'])
main=(R/'Roth/Main.lean').read_text().splitlines();(D/'caller-excerpt.lean.txt').write_text('\n'.join(main[452:478])+'\n')
(D/'source-LeanEval.lean.txt').write_text((R/'Roth/LeanEval.lean').read_text())
(D/'local-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[1650:1710])+'\n')
for j,p in enumerate(['Mathlib/Algebra/Polynomial/Taylor.lean','Mathlib/Algebra/MvPolynomial/Eval.lean','Mathlib/RingTheory/MvPowerSeries/Order.lean']):
 (D/f'mathlib-source-{j}.lean.txt').write_text((R/'.lake/packages/mathlib'/p).read_text())
dump('progress-snapshot.json',json.loads((R/'.mathlib-quality/overview/progress.json').read_text()))
raw=json.loads((D/'original-receipt.json').read_text());messages=[x['message']for x in raw['result']['structuredContent']['result']['items']]
dump('native-type.json',{'full_type':next(x.split('TAY281_FULL_TYPE: ')[1]for x in messages if x.startswith('TAY281_FULL_TYPE: ')), 'printer_elision':'89054 characters elided','actual_scope':'exact target replay plus one exact private monomial decay helper; full loaded original type/value constant inventory; pp.all kernel body printer explicitly elided','axioms':[x for x in messages if 'depends on axioms:'in x]})
dump('canonical-consumers.json',{'type_consumers':[x for x in messages if x.startswith('TAY281_DIRECT_TYPE_CONSUMER:')],'body_consumers':[x for x in messages if x.startswith('TAY281_DIRECT_CONSUMER:')],'audit':[x for x in messages if x.startswith('TAY281_AUDIT')]})
dump('callers.json',{'explicit_proof_callers':[{'name':'Roth.one_lt_roth_eval_bound_aux','private':True,'file':'Roth/Main.lean','start':453,'end':478,'call':477,'uses':1}],'source_scopes':'Main38 documentary reference,380 declaration,477 actual call; no other tracked production source occurrences','full_files_read':['Roth/Main.lean:1-588','Roth/LeanEval.lean:1-66'],'external_to_file_count':0,'same_file_count':1,'transitive_public_chain':['Roth.roth_of_isIntegral','Roth.roth','Roth.roth_rat','LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth'],'simp_scope':'No target simp attribute; direct source refs and exact canonical direct kernel refs separately audited; arbitrary tactic/transitive closure not claimed','inline_derivations':'Taylor expansion and finite sum primitives occur in target and Taylor.lean; no duplicate full quantitative weighted upper estimate found'})
dump('prefix-controls.json',{'isolated_import_count':18,'disk_import_count':9,'isolated_sha256':hashlib.sha256((D/'isolated-prefix.lean.txt').read_bytes()).hexdigest(),'disk_sha256':hashlib.sha256((D/'disk-prefix.lean.txt').read_bytes()).hexdigest(),'extra_imports':[],'root_exclusive_native':True})
print('Saved complete searches/source/metadata/prefix controls')
