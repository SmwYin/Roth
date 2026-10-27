"""Freeze only after all native receipts are complete and successful."""
import pathlib,json,hashlib,shutil,re
b=pathlib.Path(__file__).resolve().parent;r=pathlib.Path('/Users/ramin/LEAN/Roth');tmp=pathlib.Path('/private/tmp/roth-overview');t='MvPolynomial.uniqueAlgEquiv_hasseDeriv'
def put(n,x):(b/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
accepted=[]
for kind in ['complete','minimal']:
 src=tmp/f'hasseUnique-{kind}-executed.lean.txt';rec=tmp/f'hasseUnique-{kind}-success.json'
 z=json.loads(rec.read_text());x=z['result'].get('structuredContent',{});out=x.get('result',x)
 assert out.get('success') and not out.get('partial',False) and not out.get('timed_out',False)
 assert not any(i.get('severity') in ['error','warning'] for i in out.get('items',out.get('diagnostics',[])))
 sn=kind+'-executed.lean.txt';rn=kind+'-success.json';shutil.copyfile(src,b/sn);shutil.copyfile(rec,b/rn)
 e=dict(source=sn,source_sha256=sha(b/sn),receipt=rn)
 if 'file_path' in z['request']:
  p=r/z['request']['file_path'];c=dict(original_execution_path=str(p),retained_sha256=sha(b/sn),disk_sha256=sha(p),matched_at_freeze=p.read_bytes()==(b/sn).read_bytes())
  # Earlier target source has a complete exact receipt; subsequent accepted disk extras append statements.
  if not c['matched_at_freeze']:
   c['matching_prefix_of_current_disk']=p.read_bytes().startswith((b/sn).read_bytes())
   assert c['matching_prefix_of_current_disk'];c['explanation']='Exact complete source retained by root at execution. Subsequent disk execution appended declarations; retained source is an unchanged prefix of current disk.'
  cn=kind+'-source-check.json';put(cn,c);e['source_check']=cn
 accepted.append(e)
for p in tmp.glob('hasseUnique-*-rejected*'):
 n=p.name.replace('hasseUnique-','');shutil.copyfile(p,b/n)
required=['MvPolynomial.uniqueAlgEquiv_hasseDeriv','HasseUniqueAssessment.replay','HasseUniqueAssessment.linear_square','HasseUniqueAssessment.inverse','RawHasseUniqueDirect.linear_square','HasseUniqueExtra.from_coordinate_bridge','HasseUniqueExtra.index_key_caller','HasseUniqueChosen.chosen','HasseUniquePinnedAndGuard.arbitrary_equiv_false']
put('verification.json',dict(declaration=t,accepted=accepted,required_axiom_checks=required,root_native_complete=True,unresolved=[],baseline='shared full build reused under fresh 17 source/pin SHA256 match',rejected_attempts=[p.name for p in b.glob('*rejected*.json')]))
questions=['Should unique-variable Hasse transport be a public rewrite lemma despite its closing-simp basis proof and one current consumer?','Should the broader coordinate aeval bridge be primary, with this transport derived locally, or should both orientations be public?','Include inverse or bundled commuting-square forms, or only the pointwise form used by index_unique?']
ph={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};ph['4.5']='N/A: theorem introduces no computational definition, instance or coercion; all six risk rows justified'
put('assessment.json',dict(declaration=t,file='Roth/HasseDeriv.lean',line=266,canonical_index=23,kind='theorem',mode='full-mathlibable',verdict='BORDERLINE-needs-human',completed=True,phases=ph,unresolved=[],root_acceptance='pending',production_edits=False,pins_unchanged=True,questions=questions,explicit_callers=1,generality='MAXIMALLY GENERAL within canonical interface; chosen-variable/Subsingleton packaging equivalent',composition='Phase6b: closing definition simp after basis extensionality; not an existing-call NO',literature_channels=9,formal_search_methods=5,statement_forms=3))
put('overview-entry.json',dict(declaration=t,type='theorem',what='Canonical identification of a singleton-variable polynomial algebra commutes with every Hasse derivative.',how='Coefficient extensionality and singleton-binomial normalization; isolated raw basis proof also closes by definitions.',hypotheses=['CommSemiring R','Unique σ'],project_dependencies=['MvPolynomial.hasseDeriv','MvPolynomial.coeff_hasseDeriv','MvPolynomial.hasseCoeff'],caller_summary=dict(count=1,callers=['Roth.index_unique at Roth/Index.lean:239'],scope='explicit source references, not opaque kernel or simp closure'),mathlib_api_audit='Univariate Hasse and canonical polynomial equivalence exist; no named pinned multivariate compatibility. All five methods on three forms; local index unavailable.',moral_duplications='Equivalent to coordinate aeval compatibility in the unique-variable case, but that bridge is project API. Generic linear conjugacy needs normalization.',generalization='No strict weakening verified; Subsingleton plus a chosen variable repackages Unique. Inverse/bundled forms equivalent.',missing_api='Public API choice for unique-variable Hasse transport beside proposed multivariate Hasse operator.',junk=False,action='BORDERLINE: retain locally pending three upstream API questions; if omitted inline exact local bridge at the single Index caller.',verdict='BORDERLINE-needs-human'))
files=[]
for p in sorted(b.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{t}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{t}/{p.name}'
 files.append(dict(source=p.name,destination=dest,sha256=sha(p),bytes=p.stat().st_size))
put('copy-manifest.json',dict(declaration=t,files=files))
print('Frozen',len(files),'artifacts; root acceptance pending')
