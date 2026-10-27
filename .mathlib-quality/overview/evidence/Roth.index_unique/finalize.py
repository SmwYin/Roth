from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).resolve().parent;S=D.parent.parent

def j(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p in S.glob('index-unique-*'):
 if p.is_file():shutil.copyfile(p,D/p.name)
for n in ['index-file-completion-2026-10-27.json','index-file-completion-2026-10-27.log']:
 p=S/n
 if p.exists():shutil.copyfile(p,D/n)
# All actual native successes, separately from rejected elaborator attempts.
accepted=[]
def add(label,source,receipt,start,required,fmt='disk'):
 r=json.loads((D/receipt).read_text());z=r['result']['structuredContent'];z=z.get('result',z)
 assert z['success'] and not z.get('timed_out')
 if fmt=='disk':assert z['partial'] is False
 ds=z['diagnostics' if fmt=='raw' else 'items']
 assert not [x for x in ds if x.get('severity') in ['error','warning'] or x.get('category')=='sorry']
 assert not any('sorryAx' in x['message'] for x in ds)
 info='\n'.join(x['message'] for x in ds if x.get('line',0)>=start)
 assert all(x in info for x in required)
 accepted.append(dict(label=label,source=source,receipt=receipt,format=fmt,native_region_start_line=start,required_info=required,source_sha256=sha(D/source)))
orig='index-unique-original-executed.lean.txt';oriRec='index-unique-original-audit-receipt.json'
add('original',orig,oriRec,2807,['Roth.index_unique.{u_1}',"'Roth.index_unique' depends on axioms:"])
add('canonical-audit',orig,oriRec,2810,['INDEX_UNIQUE151_AUDIT: requested=293; unique=293','INDEX_UNIQUE151_AUDIT_PRESENT: present=293; values=293','INDEX_UNIQUE151_DIRECT_CONSUMER: _private.Roth.Theta.0.Roth.index_unique_le_log_div'])
add('independent-target','index-unique-target-executed.lean.txt','index-unique-target-receipt.json',3129,["'IndexUniqueAssessment151."+x+"' depends on axioms:" for x in ['independentNonzero','allPolynomials','noAutomaticClosure','zeroDenominator']])
add('callers-guards','index-unique-callers-guards-clean-executed.lean.txt','index-unique-callers-guards-clean-receipt.json',3181,["'IndexUniqueCallers151.logBoundReplay' depends on axioms:"]+["'IndexUniqueGuards151."+x+"' depends on axioms:" for x in ['zeroPolynomial','arbitraryFintype','uniqueProvidesFinite','negativeScaleGuard','wrongZeroInfinityGuard']])
add('isolated-minimum','index-unique-mathlib-executed.lean.txt','index-unique-mathlib-receipt.json',1,["'IndexUniqueMathlib151."+x+"' depends on axioms:" for x in ['minimumSupport','taylorMinimum','existingReaim']],'raw')
add('isolated-canonical-normalization','index-unique-infdegree-executed.lean.txt','index-unique-infdegree-receipt.json',1,["'IndexUniqueInfDegree151."+x+"' depends on axioms:" for x in ['trailingInf','rootInf','finsetBridge','realInfSupport','realRootInf']],'raw')
add('collapse-guard','index-unique-collapse-executed.lean.txt','index-unique-collapse-receipt.json',3257,["'IndexUniqueCollapse151.collapseCancellation' depends on axioms:"])
rejected=[dict(source='index-unique-callers-guards-initial-executed.lean.txt',receipt='index-unique-callers-guards-initial-receipt.json',reason='Unknown Fintype.ofUnique; unused ambient Fintype/Unique warnings. Clean replay infers Unique.fintype and omits unused section variables.'),dict(source='index-unique-infdegree-initial-executed.lean.txt',receipt='index-unique-infdegree-initial-receipt.json',reason='Three HDiv ℝ ℕ inference errors and recovered sorryAx. Clean source gives explicit real denominator and real quotient annotations before WithTop coercion; initial artifacts never accepted.')]
build=json.loads((D/'index-file-completion-2026-10-27.json').read_text());assert build['exit_code']==0 and 'Build completed successfully' in build['output']
j('verification.json',dict(declaration='Roth.index_unique',accepted=accepted,rejected=rejected,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],audit=dict(source='index-unique-audit-executed.lean.txt',whole_source=orig,start_line=2810,canonical_order='canonical-order.json'),target_source='index-unique-target-executed.lean.txt',target_start_line=3129,callers_source='index-unique-callers-guards-clean-executed.lean.txt',callers_start_line=3181,guards_start_line=3216,normalization_source='index-unique-infdegree-executed.lean.txt',collapse_source='index-unique-collapse-executed.lean.txt',collapse_start_line=3257,full_build=dict(receipt='index-file-completion-2026-10-27.json',log='index-file-completion-2026-10-27.log',source_hashes_match_baseline=True),original_kernel_printer='complete, no MCP elision; raw receipt retained',read_only=True))
A=json.loads((D/'assessment.json').read_text());A.update(completed=True,allphases='PASS');j('assessment.json',A)
p=D/'report.md';s=p.read_text();s=s.replace('All phases complete, verification unresolved=[]','The [collapse guard](../evidence/Roth.index_unique/index-unique-collapse-executed.lean.txt) and [clean native receipt](../evidence/Roth.index_unique/index-unique-collapse-receipt.json) additionally verify that X₀−X₁ is nonzero before both variables are renamed to the same Unit variable, where it becomes0. This confirms the cancellation obstruction behind the Unique restriction. The [fresh full lake build receipt](../evidence/Roth.index_unique/index-file-completion-2026-10-27.json) and [complete log](../evidence/Roth.index_unique/index-file-completion-2026-10-27.log) establish the final Index-module completion build, exit0, with unchanged source/pin hashes.\n\nAll phases complete, verification unresolved=[]');p.write_text(s)
