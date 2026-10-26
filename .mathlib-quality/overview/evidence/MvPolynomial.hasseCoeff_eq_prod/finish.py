import pathlib,json,hashlib,shutil
base=pathlib.Path(__file__).resolve().parent
outer=pathlib.Path('/private/tmp/roth-overview')
for a,b in [('target-lsp.json','target-lsp.json'),('target-executed.lean','target-executed.lean'),('virtual-success.json','mathlib-lsp.json'),('virtual-executed.lean','probes.lean'),('caller-lsp.json','caller-lsp.json'),('caller-executed.lean','caller-executed.lean'),('virtual-initial-failure.json','rejected-initial.json')]:
 shutil.copyfile(outer/('hasseCoeff_eq_prod-'+a),base/b)
rejected=json.loads((base/'rejected-initial.json').read_text())
(base/'rejected-initial.lean').write_text(rejected['request']['code'])
accepted=[];summary={}
for kind,receipt,source in [('target','target-lsp.json','target-executed.lean'),('mathlib','mathlib-lsp.json','probes.lean'),('caller','caller-lsp.json','caller-executed.lean')]:
 raw=json.loads((base/receipt).read_text());native=raw['result'];sc=native['structuredContent'];res=sc.get('result',sc)
 assert res['success'] and not res.get('partial') and not res.get('timed_out') and not res.get('failed_dependencies') and not native.get('isError')
 messages=res.get('items',res.get('diagnostics',[]))
 assert not [x for x in messages if x['severity']=='error']
 assert not [x for x in messages if 'sorryAx' in x.get('message','')]
 summary[kind]={'success':True,'partial':bool(res.get('partial',False)),'timed_out':bool(res.get('timed_out',False)),'errors':0,'warnings':len([x for x in messages if x['severity']=='warning']),'failed_dependencies':0}
 accepted.append({'kind':kind,'receipt':receipt,'source':source,'source_sha256':hashlib.sha256((base/source).read_bytes()).hexdigest(),'observed':summary[kind]})
verification={'accepted':accepted,'rejected':[{'receipt':'rejected-initial.json','source':'rejected-initial.lean','reason':'Minimal imports lacked Mathlib.Data.Nat.Choose.Bounds for whole caller; Unknown constant Nat.choose_le_two_pow, recovered caller contains sorryAx. Rejected entire run; no accepted witness relies on recovery.','resolution':'Final mathlib-only source adds existing production Choose.Bounds import; all five witnesses succeed with standard axioms.'}],'axioms':['propext','Classical.choice','Quot.sound'],'notes':['Persistent target disk includes earlier unrelated diagnostics and two historical style warnings. Current block resolves correct target and has no error.','Mathlib-only source has no Roth import; check_failure controls confirm project symbols unavailable, not mathematical absence.','No negative automation claim is used in verdict; positive existing composition establishes result.']}
(base/'verification.json').write_text(json.dumps(verification,indent=2)+'\n')
a={'declaration':'MvPolynomial.hasseCoeff_eq_prod','file':'Roth/HasseDeriv.lean','line':106,'category':'NO-composable-from-mathlib','verdict':'NO-composable-from-mathlib','completed':True,'root_acceptance':'pending','production_edits':False,'baseline_hashes_matched':17,'phases':{k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.6','5','5.5','6.0','6','7','8']},'unresolved':[],'upstream_design_questions':[],'axioms':['propext','Classical.choice','Quot.sound'],'diagnostics':summary,'limitations':['Optional ask_chatgpt_math unavailable','Local symbol index unavailable; positive pinned candidates checked, no negative inference','nLab direct XHTML unsupported; nCatLab path inaccessible; indexed nLab context inspected','External math search versions differ from pinned toolchain; actual candidates tested in pin','Explicit source caller scope excludes opaque tactic/kernel dependency closure'],'composition':'COMPOSABLE: Finsupp.prod_fintype supplied Nat.choose_zero_right; original alias target, isolated expanded target and whole sole-caller rewrites verified.','generality':'Fixed alias interface is general for stated finite variables; expanded upper-function version and existing generic/finite-superset versions verified. No new product construction needed.','web_evidence_policy':'Exact requests, SHA256 of returned representation, access outcomes, titles/URLs/locators, original concise summaries; no raw response/article text persisted.'}
a['phases']['4.5']='N/A: theorem, no definition/class/instance infrastructure'
(base/'assessment.json').write_text(json.dumps(a,indent=2)+'\n')
# Preserve precise actual search requests alongside full native returned objects.
requests={
'finder-current':{'query':'For finitely supported natural multiindices d k over finite variables the product of binomial choose k j d j over support d equals the full product','num_results':5},
'finder-abstract':{'query':'Finsupp product over support equals product over fintype when g i 0 = 1','num_results':5},
'loogle-current':{'query':'Nat.choose, Finsupp.prod','num_results':10},
'loogle-abstract':{'query':'Finsupp.prod, Finset.prod','num_results':10},
'search-current':{'query':'product of multiindex binomial coefficients over its finite support equals product over all variables','num_results':5},
'search-abstract':{'query':'finitely supported function product equals product over a finite type if zero maps to one','num_results':5},
'local-current':{'query':'hasseCoeff_eq_prod','project_root':'/Users/ramin/LEAN/Roth','limit':30},
'local-abstract':{'query':'prod_fintype','project_root':'/Users/ramin/LEAN/Roth','limit':30}}
for name,req in requests.items():
 p=base/(name+'.json');v=json.loads(p.read_text());v=v.get('response',v)
 p.write_text(json.dumps({'request':req,'response':v},indent=2)+'\n')
# Record session source identities, not copied skill documents.
root=pathlib.Path('/Users/ramin/LEAN/Roth')
paths=[pathlib.Path('/Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md'),pathlib.Path('/Users/ramin/.codex/skills/mathlib-quality/SKILL.md'),pathlib.Path('/Users/ramin/.codex/skills/lean4/SKILL.md')]+list(pathlib.Path('/Users/ramin/.codex/skills/mathlib-quality/references').glob('mathlib*md'))
(base/'worker-source-manifest.json').write_text(json.dumps({'files':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]},indent=2)+'\n')
