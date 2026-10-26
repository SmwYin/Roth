import pathlib,json,hashlib,re
base=pathlib.Path(__file__).resolve().parent
root=next((p for p in [pathlib.Path.cwd(),*base.parents] if (p/'lakefile.toml').exists()),None)
assert root,'Run from project root or integrated project location'
target='MvPolynomial.coeff_hasseDeriv'; ev=base/'evidence'
def native(name):
 x=json.loads((ev/(name+'-lsp.json')).read_text())['result']
 assert not x.get('isError'), name
 sc=x['structuredContent'];r=sc.get('result',sc);items=r.get('items',r.get('diagnostics',[]))
 assert r['success'] and not r.get('partial') and not r.get('timed_out') and not r.get('failed_dependencies'),name
 errors=[i for i in items if i.get('severity')=='error'];assert not errors,(name,errors)
 return {'success':True,'partial':False,'timed_out':False,'errors':0,'warnings':sum(i.get('severity')=='warning' for i in items),'failed_dependencies':0}
diag={n:native(n) for n in ['target','shape','mathlib','route']}
manifest=json.loads((ev/'input-manifest.json').read_text())
assert len(manifest['sources_and_pins'])==17
for name,r in manifest['sources_and_pins'].items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==r['sha256'],name
for r in json.loads((ev/'pinned-sources.json').read_text()):assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['sha256'],r['path']
for p in ev.glob('*.json'):json.loads(p.read_text())
entry={
 'declaration':target,'type':'For arbitrary variable/coefficient types and CommSemiring R, d,e:σ→₀ℕ, P:MvPolynomial σ R: coeff e (hasseDeriv d P) = (hasseCoeff d (e+d):R) * coeff (e+d) P.',
 'what':'Computes each coefficient of a multivariate Hasse derivative as one shifted input coefficient multiplied by its natural binomial factor.',
 'how':'Additive polynomial induction; monomial coefficient evaluation; distinguish reconstructed exponent, dominating order and vanishing binomial cases.',
 'hypotheses':'Arbitrary variable type and commutative coefficient semiring, finite natural derivative/output multiindices and arbitrary polynomial; no finite-variable, field, characteristic, domain or nontriviality hypotheses.',
 'project_dependencies':['MvPolynomial.hasseDeriv','MvPolynomial.hasseCoeff','MvPolynomial.hasseDeriv_monomial','MvPolynomial.hasseCoeff_eq_zero_iff'],
 'caller_summary':'Eight explicit caller declarations (seven internal, one in CoeffNorm), eleven invocation tokens. Supplies zero/map/composition/pderiv/degree/vanishing/univariate-compatibility and absolute coefficient bound proofs. No identical inlined duplicate found in reviewed source; no opaque dependency closure claimed.',
 'mathlib_api_audit':'Univariate Polynomial.hasseDeriv_coeff is the direct analogue, not an arbitrary-variable replacement. LaurentSeries coefficient API, coeff_pderiv, lsum and comapDomain building blocks do not alone prove the truncated-subtraction collision/vanishing identity. All five search methods and isolated exact? guard executed; local symbol index unavailable.',
 'moral_duplications':'Natural multivariate extension of Polynomial.hasseDeriv_coeff; generic lowering characterization and weighted-pullback implementation are new alternatives rather than existing API duplicates.',
 'generalization':'Maximal for pinned MvPolynomial CommSemiring domain. A Semiring-only domain is compile-rejected. Generic weighted L helper verified but optional; bundled lcoeff/function forms verified and less convenient at current rewrite callers.',
 'missing_api':'Arbitrary-variable characteristic-free Hasse derivative coefficient interface, next to MvPolynomial.PDeriv and the multivariate Hasse operator.',
 'junk':'None: substantial coefficient interface, not glue, unused code or a three-call wrapper.',
 'action':'YES-add-as-is: include with multivariate Hasse operator in a focused upstream module; inline scalar alias in statement if hasseCoeff is omitted, retain shifted coefficient normal form.'}
(base/'overview-entry.json').write_text(json.dumps(entry,indent=2)+'\n')
assessment={'declaration':target,'file':'Roth/HasseDeriv.lean','line':89,'category':'YES-add-as-is','verdict':'YES-add-as-is','completed':True,'root_acceptance':'pending','production_edits':False,'baseline_hashes_matched':17,'phases':{k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.6','5','5.5','6.0','6','7','8']},'unresolved':[],'upstream_design_questions':[],'axioms':['propext','Classical.choice','Quot.sound'],'diagnostics':diag,'limitations':['Optional ask_chatgpt_math unavailable','Local symbol index unavailable; no negative inference from empty index','nLab direct XHTML unsupported; nCatLab direct path inaccessible; indexed context considered','Explicit source references do not claim opaque tactic/kernel closure'],'composition':'NOT-COMPOSABLE: no existing <=3-call route verified; new independent/generic witnesses do not count as mathlib replacements','generality':'Maximally general for pinned multivariate polynomial coefficient interface; optional new abstract helper and bundled equivalent tested','web_evidence_policy':'Exact requests, SHA256 of returned representation, access outcomes, titles/URLs/locators and concise original summaries only; no raw response/page text persisted.'}
assessment['phases']['4.5']='N/A: theorem, no new definition/class/instance'
(base/'assessment.json').write_text(json.dumps(assessment,indent=2)+'\n')
# Translate the final tracked link layout to this scratch package or integrated tree.
report=base/'report.md'
assert report.exists()
links=re.findall(r'\]\(([^)]+)\)',report.read_text())
for link in links:
 if link.startswith(('https:','http:')):continue
 prefix='../evidence/'+target+'/'
 if link.startswith(prefix): path=base/link[len(prefix):]
 else:path=(report.parent/link).resolve()
 assert path.is_file(),(link,str(path))
files=[]
for p in sorted(base.rglob('*')):
 if not p.is_file() or p.name in ['copy-manifest.json','validation.json']:continue
 rel=p.relative_to(base)
 dst='.mathlib-quality/overview/mathlibable/'+target+'.md' if str(rel)=='report.md' else '.mathlib-quality/overview/evidence/'+target+'/'+str(rel)
 data=p.read_bytes(); files.append({'source':str(rel),'destination':dst,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
(base/'copy-manifest.json').write_text(json.dumps({'declaration':target,'files':files},indent=2)+'\n')
(base/'validation.json').write_text(json.dumps({'source_hashes':'PASS:17/17','pinned_source_hashes':'PASS','native_success_gates':diag,'json_receipts':'PASS','report_links':len(links),'local_links':'PASS','manifest_files':len(files),'status':'PASS'},indent=2)+'\n')
print('PASS: source/pin/native/JSON/link/hash manifest gates; root acceptance pending')
