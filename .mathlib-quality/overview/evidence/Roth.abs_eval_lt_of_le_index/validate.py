#!/usr/bin/env python3
"""Portable read-only canonical281 validator; current manifest is authoritative."""
from pathlib import Path
import sys,json,hashlib,re
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd()
N='Roth.abs_eval_lt_of_le_index';draft='--draft'in sys.argv
rd=lambda n:json.loads((D/n).read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 q=rd(n)['result'];q=q.get('structuredContent')or json.loads(q['content'][0]['text']);return q.get('result',q)
def diags(n):
 q=result(n);return q.get('items',q.get('diagnostics',[]))
def messages(n):return '\n'.join(x['message']for x in diags(n))
def report():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.exists():return p
 raise AssertionError('report missing')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');nt=rd('native-type.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==281
assert a['verdict']=='BORDERLINE-needs-human'and 1<=len(a['future_upstream_questions'])<=5
assert a['root_acceptance']in['pending','PASS']and not a['unresolved']and not v['unresolved']
assert not a['parent_verdict_inherited']and not a['cost_based_verdict']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==nt['type']==nt['full_type']and o['type'].startswith('∀ {m : ℕ}')
assert not nt['full_kernel_printer_body']and nt['elided_characters']==[89054]
assert o['generalization']['verified']and '[NormedCommRing K]'in o['generalization']['normed_ring_type']and '[NormOneClass K]'in o['generalization']['normed_ring_type']
assert '∀ d ∈ box r'in o['generalization']['project_type']and 'μ'in o['generalization']['proposed_type']
base=rd('input-manifest.json');assert base==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
inputs=rd('inputs.json');assert len(inputs)==len(base['sources_and_pins'])==17
for x in inputs:assert x['match']and x['sha256']==base['sources_and_pins'][x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')==dict(inputs=inputs,unchanged=True)
for mod,nlines in [('Main',588),('LeanEval',66)]:
 p=D/('source-'+mod+'.lean.txt');assert sha(p)==sha(R/('Roth/'+mod+'.lean'))and len(p.read_text().splitlines())==nlines
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==sha(D/x['archive'])==x['sha256']
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293 and order[280]==rd('canonical-entry.json')and order[280]['name']==N
assert set(o['project_dependencies']) <= {x['name'] for x in order}
s=(D/'original-executed.lean.txt').read_text();arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
ts=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0]);actual=[('private',m,n)if m else('public',p)for m,n,p in ts];assert actual==expected and len(actual)==len(set(actual))==293
original=rd('target-metadata.json')['source'];assert original.replace('theorem abs_eval_lt_of_le_index','theorem replay')in s
main=(D/'source-Main.lean.txt').read_text();helper=main[main.index('private lemma abs_prod_pow'):main.index('/-- If `Q` has index')];assert helper in s
assert 'example : @Roth.abs_eval_lt_of_le_index = @Taylor281Original.replay := Subsingleton.elim _ _'in s
msg=messages('original-receipt.json');assert all(x in msg for x in ['TAY281_FULL_TYPE:','TAY281_AUDIT: requested=293; unique=293','TAY281_AUDIT_PRESENT: present=293; values=293','TAY281_DIRECT_CONSUMER: _private.Roth.Main.0.Roth.one_lt_roth_eval_bound_aux'])and 'TAY281_DIRECT_TYPE_CONSUMER:'not in msg
pc=rd('prefix-controls.json');prefixes={}
for k,n in [('isolated',18),('disk',9)]:
 p=D/(k+'-prefix.lean.txt');prefixes[k]=re.findall(r'^import (.+)$',p.read_text(),re.M);assert len(prefixes[k])==pc[k+'_import_count']==n and sha(p)==pc[k+'_sha256']
assert pc['isolated_sha256']=='21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217'
assert pc['disk_sha256']=='363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593'
assert not pc['extra_imports']and pc['root_exclusive_native']and v['no_extra_imports']
assert {x['label']for x in v['accepted']}=={'original','generic','project','normed-field','normed-ring','callers','shape','fullMain'}
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
for e in v['accepted']:
 p=D/e['source'];s=p.read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(p)==e['source_sha256']==q['executor']['worker_request']['source_sha256']and q['executor']['owner']=='root'
 assert q['request']==e['original_execution_request']and q['elapsed_ms']==e['elapsed_ms']
 assert not q['result'].get('isError',False)and z['success']and not z.get('timed_out',False)
 assert not[x for x in diags(e['receipt'])if x['severity']in['error','warning']or x.get('category')=='sorry']
 assert max(map(len,s.splitlines()))<=100
 imports=re.findall(r'^import (.+)$',s,re.M)
 if e['format']=='disk':assert z['partial']is False and not z['failed_dependencies']and imports==prefixes['disk']and s.startswith((D/'disk-prefix.lean.txt').read_text())
 else:assert q['request']['code']==s and '#check_failure '+N in s and imports==prefixes['isolated']and s.startswith((D/'isolated-prefix.lean.txt').read_text())
 t='\n'.join(x['message']for x in diags(e['receipt'])if x['line']>=e['native_region_start_line']);assert 'sorryAx'not in t and 'PANIC'not in t
 assert all(x in t for x in e['required_info'])
 axs=re.findall(r'depends on axioms: \[([^]]*)\]',t);assert axs
 for xs in axs:assert{x.strip()for x in xs.split(',')if x.strip()}<=allowed
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']and any(x['severity']=='warning'for x in diags(e['receipt']))
assert v['attempt_accounting']['native_executions']==11==len(v['accepted'])+len(v['other_executions'])
assert len(rd('preparation-only.json')['unexecuted_root_requests'])==2
# Independently reconstruct exact full original caller inlining and whole Main scope.
caller='\n'.join(main.splitlines()[452:478])+'\n';assert caller==(D/'caller-excerpt.lean.txt').read_text()
target=(D/'target-excerpt.lean.txt').read_text().replace('theorem abs_eval_lt_of_le_index','have upper')
inline=caller.replace('  exact (one_le_prod_pow_mul_abs_eval','\n'.join('  '+l for l in target.splitlines())+'\n  exact (one_le_prod_pow_mul_abs_eval').replace('(abs_eval_lt_of_le_index hdmap','(upper hdmap')
cs=(D/'callers2-executed.lean.txt').read_text();assert inline.replace('private lemma one_lt_roth_eval_bound_aux','lemma caller_inline')in cs
assert caller.replace('private lemma one_lt_roth_eval_bound_aux','lemma caller_generic').split(' := by')[0]in cs
assert 'originalCaller281'in cs and 'TAY281_CALLER_STILL_USES_TARGET'in cs
full=main[main.index('namespace Roth'):].replace('namespace Roth','namespace Taylor281Full\nopen Roth',1).replace('end Roth','end Taylor281Full').replace(original.strip(),'')
assert full.count(caller.strip())==1;full=full.replace(caller.strip(),inline.strip())
aidx=full.index('/-- If `Q` has index');bidx=full.index('-- Choose the polynomial',aidx);full=full[:aidx]+full[bidx:]
assert (D/'fullmain2-executed.lean.txt').read_text()==(D/'disk-prefix.lean.txt').read_text()+'\n'+full+'\n#print axioms Taylor281Full.roth_rat\n'
c=rd('callers.json');assert len(c['explicit_proof_callers'])==1 and c['explicit_proof_callers'][0]['call']==477 and c['same_file_count']==1 and c['external_to_file_count']==0
ph=rd('phase-checks.json');assert len(ph['modern9'])==9 and len(ph['proofstrategy5'])==5 and len(ph['statement_shape3'])==3 and len(ph['infrastructure_risks'])==6 and len(ph['generality'])==9
fm=rd('formal-search-matrix.json');assert len(fm['cells'])==15 and {(x['form'],x['method'])for x in fm['cells']}=={(f,m)for f in ['current','standard','abstract']for m in ['leanfinder','leansearch','loogle','rg','local']}
assert len(fm['supplemental_normed5'])==5
for x in fm['cells']+fm['supplemental_normed5']:
 assert (D/x['receipt']).is_file()
 if x.get('retry'):assert(D/x['retry']).is_file()
for f in ['current','standard','abstract','normed']:
 for m in ['leanfinder','leansearch']:assert not rd('formal-'+f+'-'+m+'.json')['result'].get('isError',False)
 lf='formal-'+f+'-loogle'+('-retry'if f in['current','normed']else'')+'.json';assert not rd(lf)['result'].get('isError',False)
 assert result('formal-'+f+'-local.json')['index']in['error','warming','consulted','unavailable']
lit=rd('literature.json');assert len(lit['general_queries'])>=3 and len({x['q']for x in lit['general_queries']})>=3
assert{x['channel']for x in lit['channels']}=={'web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'}and not lit['third_party_bodies_persisted']
assert 'site:ncatlab.org/ncatlab'in next(x['query']for x in lit['channels']if x['channel']=='ncatlab')and 'after:2021-10-29 before:2026-10-30'in next(x['query']for x in lit['channels']if x['channel']=='arxiv')
assert lit['optional_channel']['status'].startswith('unavailable')and lit['local_channel']['channel']=='local'
for p in list(D.glob('web-batch*.json'))+[D/'primary-detail.json']:
 z=json.loads(p.read_text());assert re.fullmatch('[0-9a-f]{64}',z['response_sha256'])and z['response_utf8_bytes']>0 and z['request']
 assert not any('---'in u or'...'in u for u in z['urls'])
assert report().read_bytes().endswith(b'\n') and not report().read_bytes().endswith(b'\n\n')
for line in report().read_text().splitlines():assert line==line.rstrip()
for link in re.findall(r'\]\(([^)]+)\)',report().read_text()):
 if link.startswith('https://'):continue
 pref='../evidence/'+N+'/';assert link.startswith(pref)and(D/link[len(pref):]).is_file(),link
m=rd('copy-manifest.json');assert m['declaration']==N and m['recursive'];covered=set()
for e in m['files']:
 pref='.mathlib-quality/overview/evidence/'+N+'/'
 if e['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=report();rel='report.md'
 else:assert e['destination'].startswith(pref);rel=e['destination'][len(pref):];p=D/rel
 assert p.is_file()and sha(p)==e['sha256']and p.stat().st_size==e['bytes'],str(p)
 assert rel not in covered;covered.add(rel)
exclude={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in exclude and '_validation-layout'not in p.relative_to(D).parts}
if not(D/'report.md').exists():files.add('report.md')
assert files==covered,(files-covered,covered-files)
assert not list(p for p in D.rglob('*.lean')if '_validation-layout'not in p.relative_to(D).parts)
for n in ['validation-scratch.json','validation-integrated.json','secret-scan.json']:
 if(D/n).exists():assert rd(n)['result']['exit_code']==0
print('PASS canonical281 currentmanifest/phases17inputs/exact293/native8+warning3/fullcallers+fullMain/formal15+normed5/links')
