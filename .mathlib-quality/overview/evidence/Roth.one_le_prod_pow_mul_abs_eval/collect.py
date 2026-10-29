from pathlib import Path
import json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.one_le_prod_pow_mul_abs_eval')
def dump(n,x): (D/n).write_text(json.dumps(x,indent=2)+'\n')
def run(n,args):
 p=subprocess.run(args,cwd=R,text=True,capture_output=True);dump(n,dict(request=args,status=p.returncode,stdout=p.stdout,stderr=p.stderr));return p.stdout
for form,pat in [('current','one_le_prod_pow_mul_abs_eval|prod.*abs.*eval|abs.*eval.*prod'),('standard','[Dd]enomsClearable|one_le_pow_mul_abs_eval_div|denom.*eval|eval.*denom'),('abstract','theorem.*one_le_abs|lemma.*one_le_abs|cast_abs|isLocalization')]:
 run('formal-'+form+'-rg.json',['rg','-n',pat,'.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial','.lake/packages/mathlib/Mathlib/Algebra/Polynomial/DenomsClearable.lean','.lake/packages/mathlib/Mathlib/RingTheory/MvPolynomial','.lake/packages/mathlib/Mathlib/Data/Int','.lake/packages/mathlib/Mathlib/NumberTheory/Transcendental/Liouville'])
run('source-search.json',['rg','--no-ignore','-n','one_le_prod_pow_mul_abs_eval','Roth','Roth.lean'])
run('tracked-source-search.json',['git','grep','-n','one_le_prod_pow_mul_abs_eval','--','Roth','Roth.lean'])
run('inline-search.json',['rg','--no-ignore','-n','Int.one_le_abs|set N : ℤ|denomsClearable|pow_sub_mul_pow','Roth','Roth.lean'])
run('literature-local.json',['rg','-n','nonzero|non-zero|integer|54|denominator','.mathlib-quality/references/clean.tex'])
run('reviewer-commits.json',['git','-C','.lake/packages/mathlib','log','-8','--format=%H %ad %an %s','--date=short','--','Mathlib/Algebra/Polynomial/DenomsClearable.lean','Mathlib/Algebra/MvPolynomial/Eval.lean','Mathlib/RingTheory/MvPolynomial/Localization.lean'])
main=(R/'Roth/Main.lean').read_text().splitlines();(D/'caller-excerpt.lean.txt').write_text('\n'.join(main[452:478])+'\n')
(D/'source-LeanEval.lean.txt').write_text((R/'Roth/LeanEval.lean').read_text())
(D/'local-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[1645:1656])+'\n')
for j,p in enumerate(['Mathlib/Algebra/Polynomial/DenomsClearable.lean','Mathlib/RingTheory/MvPolynomial/Localization.lean','Mathlib/Algebra/MvPolynomial/Eval.lean']):
 (D/f'mathlib-source-{j}.lean.txt').write_text((R/'.lake/packages/mathlib'/p).read_text())
dump('progress-snapshot.json',json.loads((R/'.mathlib-quality/overview/progress.json').read_text()))
raw=json.loads((D/'original-receipt.json').read_text());result=raw['result']['structuredContent']['result'];messages=[x['message']for x in result['items']]
dump('native-type.json',{'full_type':next(x.split('INT279_FULL_TYPE: ')[1]for x in messages if x.startswith('INT279_FULL_TYPE: ')), 'printer_elision':'89281 characters elided','actual_scope':'exact target replay without helpers; full loaded original kernel type and value constant inventory; pp.all kernel body printer elided explicitly','axioms':[x for x in messages if 'depends on axioms:'in x]})
dump('canonical-consumers.json',{'type_consumers':[x for x in messages if x.startswith('INT279_DIRECT_TYPE_CONSUMER:')],'body_consumers':[x for x in messages if x.startswith('INT279_DIRECT_CONSUMER:')],'audit':[x for x in messages if x.startswith('INT279_AUDIT')]})
dump('callers.json',{'all_production_files':[str(p)for p in json.loads((D/'input-manifest.json').read_text())['sources_and_pins']if p.endswith('.lean')],'source_occurrences':[{'file':'Roth/Main.lean','line':38,'scope':'doc reference'},{'file':'Roth/Main.lean','line':324,'scope':'declaration'},{'file':'Roth/Main.lean','line':476,'scope':'proof call'}],'explicit_proof_callers':[{'name':'Roth.one_lt_roth_eval_bound_aux','private':True,'file':'Roth/Main.lean','start':453,'end':478,'call':476,'uses':1,'proof':'full original body; lower bound trans_lt with Taylor upper bound'}],'external_to_file_count':0,'same_file_count':1,'skill_count_excluding_declaring_file':0,'transitive_public_chain':['Roth.roth_of_isIntegral','Roth.roth','Roth.roth_rat','LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth'],'simp_scope':'target is not simp-tagged; no proof of arbitrary simp closure; source refs and canonical direct kernel refs separately audited','inline_derivations':'none found apart from actual target; Int.one_le_abs analogues elsewhere concern coefficient norms and nonempty polynomial families, not denominator-clearing evaluation'})
dump('prefix-controls.json',{'isolated_import_count':18,'disk_import_count':9,'isolated_sha256':hashlib.sha256((D/'isolated-prefix.lean.txt').read_bytes()).hexdigest(),'disk_sha256':hashlib.sha256((D/'disk-prefix.lean.txt').read_bytes()).hexdigest(),'extra_imports':[],'root_exclusive_native':True})
print('Saved all source/formal rg/lexical/caller/local literature/history receipts')
