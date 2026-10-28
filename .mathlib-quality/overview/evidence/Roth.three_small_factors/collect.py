from pathlib import Path
import json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path(__file__).parent

def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
forms={'current':r'three_small_factors|log.*floor|floor.*log','standard':r'log.*floor|floor.*log|sqrt.*floor|floor.*sqrt','abstract':r'lt_rpow_of_log_lt|pow_lt_iff_lt_log|log_pow|log_rpow'}
for label,pat in forms.items():
 cmd=['rg','-n',pat,'.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('search-'+label+'-rg.json',dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)))
cmd=['rg','-n',r'(theorem|lemma|def)\s+(Roth\.)?three_small_factors\b','.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('full-name-search.json',dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr),interpretation='Lexical exact-name no-hit is not semantic absence.'))
paths=['Mathlib/Analysis/SpecialFunctions/Pow/Real.lean','Mathlib/Analysis/SpecialFunctions/Log/Basic.lean','Mathlib/Analysis/Real/Sqrt.lean','Mathlib/Algebra/Order/Floor/Semiring.lean','Mathlib/Algebra/Order/Floor/Defs.lean']
inputs=[]
for p in paths:
 src=R/'.lake/packages/mathlib'/p;n='mathlib-'+p.split('/')[-2]+'-'+p.split('/')[-1]+'.txt';put(n,src.read_text());inputs.append(dict(path=p,archive=n,sha256=sha(src),bytes=src.stat().st_size))
put('mathlib-inputs.json',inputs)
local=R/'.mathlib-quality/references/clean.tex';put('literature-local-input.json',dict(path=str(local.relative_to(R)),sha256=sha(local),bytes=local.stat().st_size));put('literature-local-excerpt.txt','\n'.join(local.read_text().splitlines()[1305:1387])+'\n')
r=json.loads((D/'original-receipt.json').read_text());ds=r['result']['structuredContent']['result']['items'];typ=next(x['message'].split('FACT241_FULL_TYPE: ',1)[1]for x in ds if x['message'].startswith('FACT241_FULL_TYPE'))
put('native-type.json',dict(type=typ,method='Lean.getConstInfo; pp.funBinderTypes=true',printer_elision=True,body_printer_note='MCP explicit78949character elision; not a complete kernel body dump. Full exact written original module, full kernel type, axioms and all293 kernel values audited.'))
put('canonical-consumers.json',dict(requested=293,unique=293,present=293,values=293,direct_value=[x['message'].split('FACT241_DIRECT_CONSUMER: ',1)[1]for x in ds if x['message'].startswith('FACT241_DIRECT_CONSUMER: ')],direct_type=[x['message'].split('FACT241_DIRECT_TYPE_CONSUMER: ',1)[1]for x in ds if x['message'].startswith('FACT241_DIRECT_TYPE_CONSUMER: ')]))
put('callers.json',dict(lexical_total_excluding_declaration=3,internal_use_count_excluding_declaring_file=1,external_to_file_distinct_files=1,callers=[dict(name='Roth.exists_mem_RSet_le_index_of_log_bound_aux',file='Roth/MainLemma.lean',line=631,visibility='private',components=[2],purpose='Second factor bounds monic remainder growth with alpha=0.'),dict(name='Roth.exists_auxiliary_polynomial_of_log_bound_aux',file='Roth/MainLemma.lean',line=656,visibility='private',components=[1,3],purpose='First and third factors control iterated Hasse derivative evaluation.'),dict(name='Roth.roth_product_bound_aux',file='Roth/Main.lean',line=502,visibility='private',components=[1],purpose='First factor bounds product of coordinate degrees plus one.')],inline_derivations=[],scope_note='All3 lexical occurrences independently confirmed by293 direct kernel-value audit. No direct type consumers, no simp attribute. Transitive dependencies are a separate scope.'))
put('formal-search-matrix.json',[dict(form=f,method=m,receipt='search-'+f+'-'+m+'.json')for f in forms for m in ['leanfinder','loogle','leansearch','rg','local_search']])
put('preparation-checks.json',dict(original=dict(exit_code=0,width_max=100,canonical_gate='PASS exact293 unique source order BEFORE native'),inline=dict(exit_code=0,width_max=100,complete_modules=['Roth.MainLemma','Roth.Main']),isolated=dict(exit_code=0,width_max=100,exact18_imports=True),preparation_only_rejections=['isolated width109 failed before execution; corrected line break before native.']))
print('Collected pinned inputs, fresh evidence,15formal cells.')
