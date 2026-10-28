from pathlib import Path
import json,hashlib,subprocess
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.mul_log_div_two_lt_log_mainCoeffBound')
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
forms={'current':r'mul_log_div_two_lt_log_mainCoeffBound|log.*floor|floor.*log','standard':r'log.*floor|floor.*log|sqrt.*floor|floor.*sqrt|div_two_lt_floor','abstract':r'log_sqrt|log_lt_log|log_rpow|lt_log_of_rpow_lt|one_lt_rpow_iff'}
for label,pat in forms.items():
 cmd=['rg','-n',pat,'.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('search-'+label+'-rg.json',dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)))
cmd=['rg','-n',r'(theorem|lemma|def)\s+(Roth\.)?mul_log_div_two_lt_log_mainCoeffBound\b','.lake/packages/mathlib/Mathlib'];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put('full-name-search.json',dict(request=cmd,result=dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr),interpretation='No lexical exact-name hit; not a semantic absence proof.'))
paths=['Mathlib/Analysis/SpecialFunctions/Pow/Real.lean','Mathlib/Analysis/SpecialFunctions/Log/Basic.lean','Mathlib/Analysis/Real/Sqrt.lean','Mathlib/Algebra/Order/Floor/Defs.lean','Mathlib/Algebra/Order/Floor/Semiring.lean','Mathlib/Algebra/Order/Floor/Ring.lean']
inputs=[]
for p in paths:
 src=R/'.lake/packages/mathlib'/p;n='mathlib-'+p.split('/')[-2]+'-'+p.split('/')[-1]+'.txt';put(n,src.read_text());inputs.append(dict(path=p,archive=n,sha256=sha(src),bytes=src.stat().st_size))
put('mathlib-inputs.json',inputs)
local=R/'.mathlib-quality/references/clean.tex';put('literature-local-input.json',dict(path=str(local.relative_to(R)),sha256=sha(local),bytes=local.stat().st_size));put('literature-local-excerpt.txt','\n'.join(local.read_text().splitlines()[1339:1390])+'\n')
receipt=json.loads((D/'original-receipt.json').read_text());ds=receipt['result']['structuredContent']['result']['items'];typ=next(x['message'].split('LOG239_FULL_TYPE: ',1)[1]for x in ds if x['message'].startswith('LOG239_FULL_TYPE'))
put('native-type.json',dict(type=typ,method='Lean.getConstInfo with pp.funBinderTypes=true',printer_elision=False,body_printer_note='Full exact target kernel body printed without explicit elision; full exact source/full type/axioms/canonical values audit retained.'))
put('canonical-consumers.json',dict(requested=293,unique=293,present=293,values=293,direct_value=[x['message'].split('LOG239_DIRECT_CONSUMER: ',1)[1]for x in ds if x['message'].startswith('LOG239_DIRECT_CONSUMER: ')],direct_type=[x['message'].split('LOG239_DIRECT_TYPE_CONSUMER: ',1)[1]for x in ds if x['message'].startswith('LOG239_DIRECT_TYPE_CONSUMER: ')]))
put('callers.json',dict(lexical_total_excluding_declaration=1,internal_use_count_excluding_declaring_file=0,external_to_file_distinct_files=0,callers=[dict(name='Roth.three_small_factors',visibility='public',file='Roth/MainLemma.lean',line=205,use='mul_lt_mul_of_pos_left (mul_log_div_two_lt_log_mainCoeffBound hX) hδ',purpose='The local key multiplies the strict half-log lower bound by positive delta for each of three small-factor inequalities.')],inline_derivations=[],scope_note='Source lexical/body search and canonical direct kernel proof consumers independently agree; no direct type consumer. No simp attribute. Transitive consumers are not direct occurrences; main_lemma signature retained in replay too.'))
put('formal-search-matrix.json',[dict(form=f,method=m,receipt='search-'+f+'-'+m+'.json')for f in forms for m in ['leanfinder','loogle','leansearch','rg','local_search']])
put('preparation-checks.json',dict(original=dict(exit_code=0,width_max=100,canonical_gate='PASS exact293 unique source order; observed before native execution'),isolated=dict(exit_code=0,exact18_imports=True,width_max=100),inline=dict(exit_code=0,full_modules=['Roth.MainLemma'],width_max=100)))
# Omit incomplete returned URL text, retaining honest redaction note.
for p in D.glob('web-*.json'):
 x=json.loads(p.read_text());old=x['entries'];x['entries']=[e for e in old if '...'not in e['url'] and '…'not in e['url'] and not e['title'].startswith('<visual_element')];x['omitted_incomplete_urls']=len(old)-len(x['entries']);put(p.name,x)
print('Collected exact source/search/native inputs and 15 formal cells.')
