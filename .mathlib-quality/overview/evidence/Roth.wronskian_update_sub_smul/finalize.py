from pathlib import Path
import json,hashlib,re,shutil,subprocess
p=Path(__file__).resolve().parent;repo=Path('/Users/ramin/LEAN/Roth');name='Roth.wronskian_update_sub_smul'
def write(f,x):(p/f).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
sha=lambda b:hashlib.sha256(b).hexdigest()
# Exact raw responses; API-request snippets take precedence over local transport newline.
accepted=[]
for label in ['target','ring','abstract','finite','caller']:
 base=Path('/private/tmp/roth-overview')/('wronskian-update-'+label)
 r=json.loads(Path(str(base)+'-success.json').read_text());write('native-'+label+'-success.json',r)
 code=r['request'].get('code',Path(str(base)+'-executed.lean.txt').read_text())
 source='native-'+label+'-executed.lean.txt';(p/source).write_text(code)
 accepted.append(dict(label=label,source=source,source_sha256=sha(code.encode()),receipt='native-'+label+'-success.json',original_execution_path=r['request'].get('file_path','lean_run_code virtual document')))
for tag in ['ring-rejected','ring-rejected-2','ring-rejected-3','abstract-rejected','abstract-warnings-rejected']:
 src=Path('/private/tmp/roth-overview')/('wronskian-update-'+tag+'.json');r=json.loads(src.read_text());write('native-'+tag+'.json',r)
 raw=Path('/private/tmp/roth-overview')/('wronskian-update-'+tag+'.lean.txt');code=r['request'].get('code',raw.read_text());(p/('native-'+tag+'.lean.txt')).write_text(code)
expected={'target':"'WronskianUpdateAssessment.replay' depends on axioms:",'ring':"'roth48_ring' depends on axioms:",'abstract':"'roth48_abstract' depends on axioms:",'finite':"'WronskianUpdateFinite.generic' depends on axioms:",'caller':"'WronskianUpdateRecover.caller_rebuilt' depends on axioms:"}
write('verification.json',dict(declaration=name,accepted=accepted,rejected=[dict(source='native-'+x+'.lean.txt',receipt='native-'+x+'.json') for x in ['ring-rejected','ring-rejected-2','ring-rejected-3','abstract-rejected','abstract-warnings-rejected']],standard_axioms=['propext','Classical.choice','Quot.sound'],expected_axiom_messages=expected,isolated_target_guard=['ring','abstract','finite'],inputs='source-pin-hashes.json',mathlib_inputs='source-mathlib-hashes.json',source_links=json.loads((p/'source-links.json').read_text()),web_metadata=[f.name for f in p.glob('web-*-metadata.json')],unresolved=[]))
phases={x:'PASS' for x in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']}
write('assessment.json',dict(declaration=name,canonical=48,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,phase_explanations={'2b':'n/a theorem','4.5':'n/a theorem; no new definitional or instance paths'},unresolved=[],root_acceptance='pending'))
type_="∀ {K : Type u_1} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l}, ν ≠ ν' → ∀ (c : K), Roth.wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = Roth.wronskian φ"
write('overview-entry.json',dict(declaration=name,canonical=48,kind='theorem',type=type_,what='Subtracting a constant multiple of one distinct family member preserves its Hasse-Wronskian.',how='Identify the updated Hasse matrix entrywise using coefficient linearity, then apply Matrix.det_updateCol_add_smul_self with negative constant scalar.',hypotheses='Field K fixed by parent interface; distinct Fin l indices; any constant c. No CharZero, independence, degree or nonzero assumptions.',project_dependencies=['Roth.wronskian','Roth.wronskianMatrix'],caller_summary='One explicit executable reference, Wronskian.lean:212 inside wronskian_ne_zero_of_linearIndependent; no external-to-file callers; documentation reference at 38 excluded.',mathlib_api_audit='Generic column law exists at Matrix/Determinant/Basic.lean:478. Binary Polynomial.wronskian differs. Three actual direct simpa routes fail; explicit representation bridge verified.',moral_duplications='Elementary determinant transvection, but not a defeq or strict <=3-existing-call replacement for the family statement.',generalization='Raw [CommRing R], arbitrary finite index and selected Hasse orders verified; existing parent interface remains Field-bound.',missing_api='Conditional on parent acceptance: finite-family Hasse-Wronskian alternating-map interface or family-to-matrix update compatibility. No missing generic determinant column law.',junk='Useful sole induction caller; not dead code.',action='Retain local theorem pending three concrete upstream family-API questions; do not submit a duplicate generic determinant law.',verdict='BORDERLINE-needs-human'))
channels=[]
for file in p.glob('web-*-metadata.json'):
 d=json.loads(file.read_text())
 for q in d['request'].get('search_query',[]):channels.append(dict(channel=file.name,query=q,status='executed',artifact=file.name))
 for o in d['request'].get('open',[]):channels.append(dict(channel='primary open',request=o,status='executed; nLab XHTML unsupported-content-type',artifact=file.name))
channels += [dict(channel='ChatGPT MCP',status='n/a',reason='ask_chatgpt_math unavailable; historical-form/generality channel optional when unavailable'),dict(channel='local clean.tex',status='executed',artifact='rg-local-reference.json',locator='Wronskians section lines 157-201; column operations 174-194')]
write('literature.json',channels)
# Guard output is recorded without claims beyond actual script status.
r=subprocess.run(['python3',str(repo/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(p)],capture_output=True,text=True)
write('secret-scan-receipt.json',dict(request=['python3','.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py',str(p)],result=dict(exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr)))
assert r.returncode==0,(r.stdout,r.stderr)
files=[]
for f in sorted(p.iterdir()):
 if not f.is_file() or f.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dst=f'.mathlib-quality/overview/mathlibable/{name}.md' if f.name=='report.md' else f'.mathlib-quality/overview/evidence/{name}/{f.name}'
 files.append(dict(source=str(f),destination=dst,sha256=sha(f.read_bytes()),bytes=len(f.read_bytes())))
write('copy-manifest.json',dict(declaration=name,files=files))
print(json.dumps(dict(files=len(files),accepted=len(accepted),guard=r.returncode)))
