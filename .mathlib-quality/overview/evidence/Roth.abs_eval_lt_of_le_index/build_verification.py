from pathlib import Path
import json,hashlib
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.abs_eval_lt_of_le_index');N='Roth.abs_eval_lt_of_le_index'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((D/n).read_text())
def result(n):
 q=read(n)['result'];q=q.get('structuredContent')or json.loads(q['content'][0]['text']);return q.get('result',q)
accepted=[]
for label,source,receipt,fmt,required in [
 ('original','original-executed.lean.txt','original-receipt.json','disk',['TAY281_FULL_TYPE:','TAY281_AUDIT: requested=293; unique=293','TAY281_AUDIT_PRESENT: present=293; values=293']),
 ('generic','generic-executed.lean.txt','generic01-receipt.json','isolated',["'Taylor281Generic.expansion_bound' depends on axioms"]),
 ('project','project2-executed.lean.txt','project02-receipt.json','disk',["'Taylor281Project.cost_bound' depends on axioms","'Taylor281Project.original_recovery' depends on axioms"]),
 ('normed-field','normed2-executed.lean.txt','normed02-receipt.json','isolated',["'Taylor281Normed.expansion_bound' depends on axioms"]),
 ('normed-ring','normedring-executed.lean.txt','normedring01-receipt.json','isolated',["'Taylor281Ring.expansion_bound' depends on axioms"]),
 ('callers','callers2-executed.lean.txt','callers02-receipt.json','disk',['TAY281_CALLER_TARGET_FREE: Taylor281Caller.caller_inline','TAY281_CALLER_TARGET_FREE: Taylor281Caller.caller_generic']),
 ('shape','shape2-executed.lean.txt','shape02-receipt.json','disk',["'Taylor281Shape.zero_polynomial' depends on axioms","'Taylor281Shape.exact_original' depends on axioms"]),
 ('fullMain','fullmain2-executed.lean.txt','fullmain02-receipt.json','disk',["'Taylor281Full.roth_rat' depends on axioms"])]:
 q=read(receipt);z=result(receipt);items=z.get('items',z.get('diagnostics',[]));assert z['success']and not[x for x in items if x['severity']in['error','warning']]
 accepted.append(dict(label=label,source=source,receipt=receipt,format=fmt,source_sha256=sha(D/source),original_execution_request=q['request'],elapsed_ms=q['elapsed_ms'],native_region_start_line=16 if fmt=='disk'else 19,required_info=required,axiom_print_required=True))
other=[]
for source,receipt in [('project-executed.lean.txt','project01-receipt.json'),('shape-executed.lean.txt','shape01-receipt.json'),('fullmain-executed.lean.txt','fullmain01-receipt.json')]:
 q=read(receipt);z=result(receipt);assert any(x['severity']=='warning'for x in z['items']);other.append(dict(source=source,receipt=receipt,source_sha256=sha(D/source),reason='Successful mathematical elaboration with warnings, rejected from accepted gates; warning-free new source and receipt retained.'))
dump('preparation-only.json',{'unexecuted_root_requests':['callers01','normed01'],'reason':'Root width guards rejected before native execution; no native receipt exists for these requests. Worker also fixed failed preparation width assertions before notifying root. Immutable actually executed sources are distinct.','sources':['callers-executed.lean.txt','normed-executed.lean.txt']})
dump('verification.json',{'declaration':N,'canonical_index':281,'completed':False,'unresolved':[],'accepted':accepted,'other_executions':other,'attempt_accounting':{'native_executions':len(accepted)+len(other),'accepted':len(accepted),'warning_rejected':len(other),'preexecution_only':2},'standard_axioms':['propext','Classical.choice','Quot.sound'],'native_executor':'root persistent session only','no_extra_imports':True,'actual_scope':'focused exact target/private-helper original replay; whole original Main and LeanEval read; complete original sole caller twice target-free; fullMain inline replay','build':'shared baseline2467 jobs with fresh17 hashes; next fileendbuild289; no declaration281 build required'})
fresh=read('inputs.json');assert all(sha(R/x['path'])==x['sha256']for x in fresh);dump('fresh-final-inputs.json',dict(inputs=fresh,unchanged=True))
fm=read('formal-search-matrix.json');fm['supplemental_normed5']=[{'form':'normed-ring','method':m,'receipt':f'formal-normed-{m}.json','retry':'formal-normed-loogle-retry.json'if m=='loogle'else None}for m in ['leanfinder','leansearch','loogle','rg','local']];dump('formal-search-matrix.json',fm)
l=read('literature.json');l['sources'][1]['locator']='January2022 exposition, §6 p12 (PDF page11), Taylor expansion lines1719–1800';dump('literature.json',l)
p=D/'report.md';s=p.read_text().replace('§6 final contradiction','§6 p12 (PDF page11), Taylor upper bound').replace('All15 cells (three forms','All15 original cells (three forms');s=s.replace('Current form queries use the exact target/evaluation/index,','A supplemental five-method normed-ring form was also executed (Finder/Search/Loogle, pinned rg, root local); Loogle’s initial unqualified norm name failed and a quoted-name retry returned no items. Finder/Search returned only univariate Gauss/Mahler or analytic-series bounds, not this exact weighted multivariate estimate. Local normed index also errored with10 hits, not a healthy exhaustive result. Current form queries use the exact target/evaluation/index,');p.write_text('\n'.join(x.rstrip()for x in s.splitlines()).rstrip()+'\n')
print('Built actual verification native8+warning3 and supplemental5')
