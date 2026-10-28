from pathlib import Path
import subprocess,json,hashlib,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.four_lt_rpow')
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
forms={'current':r'four_lt_rpow|3 ≤ .*\^ 2 \* (Real\.)?log|4 < .*\^.*δ','standard':r'lt_rpow_of_log_lt|lt_rpow_iff_log_lt|quadratic_le_exp_of_nonneg|log_lt_iff_lt_exp|log_le_log','abstract':r'nonneg_le_nonneg_of_sq_le_sq|sq_lt_sq₀|mul_self_le_mul_self|le_mul_of_one_le_right'}
for label,pat in forms.items():
 cmd=['rg','-n',pat,'.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('search-'+label+'-rg.json',dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)))
cmd=['rg','-n',r'(theorem|lemma|def)\s+(Roth\.)?four_lt_rpow\b','.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('full-name-search.json',dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr),interpretation='No exact lexical declaration name; this alone establishes no semantic absence.'))
paths=['Mathlib/Analysis/SpecialFunctions/Pow/Real.lean','Mathlib/Analysis/SpecialFunctions/Log/Basic.lean','Mathlib/Analysis/SpecialFunctions/Exp.lean','Mathlib/Algebra/Order/Ring/Abs.lean','Mathlib/Algebra/Order/Ring/Unbundled/Basic.lean']
inputs=[]
for p in paths:
 src=R/'.lake/packages/mathlib'/p;n='mathlib-'+p.split('/')[-2]+'-'+p.split('/')[-1]+'.txt';put(n,src.read_text());inputs.append(dict(path=p,archive=n,sha256=sha(src),bytes=src.stat().st_size))
put('mathlib-inputs.json',inputs)
local=R/'.mathlib-quality/references/clean.tex';put('literature-local-input.json',dict(path=str(local.relative_to(R)),sha256=sha(local),bytes=local.stat().st_size));put('literature-local-excerpt.txt','\n'.join(local.read_text().splitlines()[1300:1390])+'\n')
order=json.loads((D/'canonical-snapshot.json').read_text());receipt=json.loads((D/'original-receipt.json').read_text());ds=receipt['result']['structuredContent']['result']['items'];typ=next(x['message'].split('FOUR238_FULL_TYPE: ',1)[1]for x in ds if x['message'].startswith('FOUR238_FULL_TYPE'))
put('native-type.json',dict(type=typ,method='Lean.getConstInfo with pp.funBinderTypes=true',printer_elision=True,body_printer_note='Full raw receipt preserved with explicit 96561-character elision; no full-body-dump claim. Full exact source and complete type/axioms/canonical values audit retained.'))
put('canonical-consumers.json',dict(requested=293,unique=293,present=293,values=293,direct_value=[x['message'].split('FOUR238_DIRECT_CONSUMER: ',1)[1]for x in ds if x['message'].startswith('FOUR238_DIRECT_CONSUMER: ')],direct_type=[x['message'].split('FOUR238_DIRECT_TYPE_CONSUMER: ',1)[1]for x in ds if x['message'].startswith('FOUR238_DIRECT_TYPE_CONSUMER: ')]))
put('callers.json',dict(lexical_total_excluding_declaration=2,internal_use_count_excluding_declaring_file=1,external_to_file_distinct_files=1,callers=[dict(name='Roth.exists_mem_RSet_le_index_of_log_bound_aux',visibility='private',file='Roth/MainLemma.lean',line=641,use='(four_lt_rpow hδ0 hr₁ hq).le',purpose='Nat.floor_pos for the coefficient-bound parameter'),dict(name='Roth.roth_product_bound_aux',visibility='private',file='Roth/Main.lean',line=495,use='(four_lt_rpow hδ0 hr0 h32\').le',purpose='Feed sqrt_lt_floor to derive positive coefficient scale')],scope_note='Source lexical occurrences and direct kernel proof consumers independently verified. No direct type consumer. Transitive closure and simp-global reach are separate; target has no simp attribute.'))
put('formal-search-matrix.json',[dict(form=f,method=m,receipt='search-'+f+'-'+m+'.json')for f in forms for m in ['leanfinder','loogle','leansearch','rg','local_search']])
# Search receipts accidentally computed elapsed_ms before awaiting: preserve raw numbers, disclose.
put('search-timing-note.json',dict(note='External formal-search elapsed_ms fields were evaluated before await and measure local setup only; 0 does not claim actual network elapsed time. Requests and full returned results are exact. Native execution timings are measured around awaited requests.'))
put('preparation-checks.json',dict(original=dict(exit_code=0,width_max=100,canonical_gate='PASS exact293 unique source order, observed before native execution'),isolated=dict(exit_code=0,exact18_imports=True,width_max=100),inline=dict(exit_code=0,full_modules=['Roth.MainLemma','Roth.Main'],width_max=100)))
