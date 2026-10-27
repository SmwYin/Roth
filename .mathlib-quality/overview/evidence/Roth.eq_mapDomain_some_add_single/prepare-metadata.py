from pathlib import Path
import json,hashlib,shutil,subprocess,re
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.eq_mapDomain_some_add_single'
def put(n,v): (D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def receipt(n,cmd):
 p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);put(n,dict(command=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr));return p
for n in ['input-manifest.json','baseline-build.txt']:
 shutil.copyfile(R/'.mathlib-quality/overview/evidence/shared'/n,D/n)
for n in ['index-file-completion-2026-10-27.json','index-file-completion-2026-10-27.log']:
 shutil.copyfile(Path('/private/tmp/roth-overview')/n,D/n)
base=json.loads((D/'input-manifest.json').read_text())['sources_and_pins'];rows=[]
for p,x in base.items():
 f=R/p;rows.append(dict(path=p,sha256=sha(f),expected_sha256=x['sha256'],bytes=f.stat().st_size,match=sha(f)==x['sha256']))
assert len(rows)==17 and all(x['match'] for x in rows);put('inputs.json',rows)
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());put('canonical-order.json',order);put('canonical-target.json',order[152]);assert order[152]['name']==N
sources=['Roth/Separation.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Option.lean','.lake/packages/mathlib/Mathlib/Data/Finsupp/Basic.lean','.lake/packages/mathlib/Mathlib/Algebra/Group/Finsupp.lean','.lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Equiv.lean']
links={};mi=[]
for p in sources:
 f=R/p;q=p.replace('/','-')+'.txt';shutil.copyfile(f,D/q);links[p]=q
 if p.startswith('.lake'):mi.append(dict(path=p,sha256=sha(f),bytes=f.stat().st_size))
put('source-links.json',links);put('mathlib-inputs.json',mi)
files=sorted({x['file'] for x in order});lex=[]
for p in files:
 f=R/p;occ=[dict(line=i,text=l) for i,l in enumerate(f.read_text().splitlines(),1) if re.search(r'\beq_mapDomain_some_add_single\b',l)]
 lex.append(dict(path=p,sha256=sha(f),occurrences=occ))
put('lexical-enumeration.json',dict(files=lex))
receipt('caller-rg.json',['rg','--no-ignore','-n',r'\beq_mapDomain_some_add_single\b','Roth','Roth.lean'])
receipt('caller-git-grep.json',['git','grep','-n','-w','eq_mapDomain_some_add_single','--','Roth','Roth.lean'])
for label,pat in [('current','eq_mapDomain_some_add_single|mapDomain.*some|some.*mapDomain'),('literature','optionElim_some|optionEquiv|sumFinsupp|sum.*Equiv'),('modern','embDomain_some_none|update_eq_add_single|embDomain_eq_mapDomain'),('inline','mapDomain some.*single none|some.*optionElim|optionElim_some')]:
 receipt('rg-'+label+'.json',['rg','--no-ignore','-n',pat,*(['Roth','Roth.lean'] if label=='inline' else ['.lake/packages/mathlib/Mathlib/Data/Finsupp','.lake/packages/mathlib/Mathlib/Algebra/Group/Finsupp.lean'])])
receipt('local-literature-search.json',['rg','-n','collecting the terms|multi.index|finite.support|roth:lem2','.mathlib-quality/references/clean.tex'])
(D/'clean-separation-excerpt.tex.txt').write_text('\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[346:435])+'\n')
formal=[]
for f in ['current','literature','modern']:
 for m in ['finder','loogle','leansearch','local']:
  x=json.loads((D/f'search-{f}-{m}.json').read_text());z=x['response'];z=z.get('structuredContent',z);formal.append(dict(form=f,method=m,query=x['request']['query'],response=z))
put('formal-search.json',formal)
for suffix in ['original-executed.lean.txt','original-audit-receipt.json','audit-executed.lean.txt','original-region.txt','audit-region.txt','isolated-executed.lean.txt','isolated-receipt.json','caller-executed.lean.txt','caller-receipt.json']:
 shutil.copyfile(Path('/private/tmp/roth-overview')/('option-exponents-'+suffix),D/('option-exponents-'+suffix))
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
put('assessment.json',dict(declaration=N,canonical_index=153,source='Roth/Separation.lean:57',kind='theorem',verdict='NO-composable-from-mathlib',completed=True,allphases='PASS',phases=dict.fromkeys(ph,'PASS'),phase_justifications={'2b':'n/a theorem','3.optional':'ask_chatgpt_math unavailable','4.5':'n/a theorem: six infrastructure risks do not apply','6':'3 existing-call embedding form verified; original mapDomain spelling needs extra representation theorem, explicitly not claimed 3 calls'},unresolved=[],root_acceptance='pending'))
entries=[]
def add(label,src,rec,fmt,line,info):entries.append(dict(label=label,source=src,receipt=rec,format=fmt,native_region_start_line=line,required_info=info,source_sha256=sha(D/src)))
add('original','option-exponents-original-executed.lean.txt','option-exponents-original-audit-receipt.json','disk',4142,['@Roth.eq_mapDomain_some_add_single',"'Roth.eq_mapDomain_some_add_single' depends on axioms:"])
add('canonical-audit','option-exponents-original-executed.lean.txt','option-exponents-original-audit-receipt.json','disk',4145,['OPTION_EXPONENTS153_AUDIT: requested=293; unique=293','OPTION_EXPONENTS153_AUDIT_PRESENT: present=293; values=293','OPTION_EXPONENTS153_DIRECT_CONSUMER: Roth.eq_sum_X_none_pow_mul_coeffNone'])
add('isolated','option-exponents-isolated-executed.lean.txt','option-exponents-isolated-receipt.json','raw',1,["'OptionExponents153."+t+"' depends on axioms:" for t in ['canonical','embedding','mapped','bridge','composed','omission_guard']])
add('sole-caller','option-exponents-caller-executed.lean.txt','option-exponents-caller-receipt.json','disk',4464,["'OptionExponents153Replay.eq_sum_X_none_pow_mul_coeffNone' depends on axioms:"])
put('verification.json',dict(declaration=N,accepted=entries,rejected=[],unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],audit=dict(source='option-exponents-audit-executed.lean.txt',whole_source='option-exponents-original-executed.lean.txt',start_line=4145,canonical_order='canonical-order.json'),full_build=dict(receipt='index-file-completion-2026-10-27.json',log='index-file-completion-2026-10-27.log',source_hashes_match_baseline=True),read_only=True))
# Full native type is read directly from fresh target diagnostics.
r=json.loads((D/'option-exponents-original-audit-receipt.json').read_text());z=r['result']['structuredContent'];z=z.get('result',z);ds=z['items'];typ=next(x['message'] for x in ds if x.get('line')==4142)
put('overview-entry.json',dict(kind='theorem',type=typ,what='Rebuild an Option-indexed natural multi-index from restriction and distinguished coordinate.',how='Pointwise extensionality, two Option cases, mapDomain evaluation.',hypotheses=['τ : Type u_1','d : Option τ →₀ ℕ; no Fintype, DecidableEq, or coefficient-ring instance'],project_dependencies=[],caller_summary=dict(explicit_call_sites=[dict(file='Roth/Separation.lean',line=107,caller='Roth.eq_sum_X_none_pow_mul_coeffNone')],internal_use_count_excluding_declaring_file=0,same_file_count=1,direct_kernel_value_consumers=['Roth.eq_sum_X_none_pow_mul_coeffNone'],inline_derivations='coeff_coeffNone at86 independently normalizes inserted coordinates; not a duplicate full reconstruction'),mathlib_api_audit=dict(canonical='Finsupp.optionElim_some',building_blocks=['Finsupp.optionElim_some','Finsupp.update_eq_add_single','Finsupp.embDomain_some_none'],representation='Finsupp.embDomain_eq_mapDomain',old_form_existing_calls=4,embedding_form_existing_calls=3),moral_duplications=['Finsupp.optionElim_some expresses reconstruction at Zero generality; expanded additive form requires bridge'],generalization=dict(status='STRICTLY NARROWER THAN STANDARD',fixed_surface='AddCommMonoid M (mapDomain interface)',embedding_surface='AddZeroClass M',canonical_surface='Zero M',native_verified=True),missing_api='No missing reconstruction law; optional naming question for additive Option normal form is not a blocking gap.',junk='Not dead: one explicit and direct-kernel caller.',action='Delete project theorem after replacing sole caller true branch with rw [Roth.coeffNone, optionEquivLeft_coeff_some_coeff_none]; complete caller replay verified. Retain optional exposition in Roth/Separation.lean docstring.'))
