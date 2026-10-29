#!/usr/bin/env python3
"""Portable read-only canonical279 assessment validator; validates current manifest."""
from pathlib import Path
import sys,json,hashlib,re
draft='--draft'in sys.argv
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else Path.cwd();N='Roth.one_le_prod_pow_mul_abs_eval'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 q=rd(n)['result'];q=q.get('structuredContent')or json.loads(q['content'][0]['text']);return q.get('result',q)
def diags(n):
 r=result(n);return r.get('items',r.get('diagnostics',[]))
def msg(n):return '\n'.join(x['message']for x in diags(n))
def report():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.exists():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json');nt=rd('native-type.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==279
assert a['verdict']=='YES-but-generalise-first'
if not draft:assert a['completed']and v['completed']and a['allphases']=='PASS'
assert a['root_acceptance']in['pending','PASS'] and not a['unresolved']and not v['unresolved']
assert not a['cost_based_verdict']and not a['parent_verdict_inherited']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS'or(draft and k=='8'and x=='pending')for k,x in a['phases'].items())
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit','moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==nt['full_type']==nt['type']and o['type'].startswith('∀ {m : ℕ}')
assert o['project_dependencies']==nt['original_project_dependencies']==[]
assert not nt['full_kernel_printer_body']and nt['elided_characters']==[89281]
assert o['generalization']['verified']and '[Fintype ι]'in o['generalization']['proposed_type']and '[IsStrictOrderedRing K]'in o['generalization']['proposed_type']
assert '[CommSemiring R]'in o['generalization']['algebraic_helper_type']and 'hbi'in o['generalization']['algebraic_helper_type']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text());assert order==rd('canonical-snapshot.json')and len(order)==293 and order[278]==rd('canonical-entry.json')and order[278]['name']==N
s=(D/'original-executed.lean.txt').read_text();ars=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(ars)==1
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
ts=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",ars[0]);actual=[('private',m,n)if m else('public',p)for m,n,p in ts];assert actual==expected and len(actual)==len(set(actual))==293
original=rd('target-metadata.json')['source'];assert original.replace('theorem one_le_prod_pow_mul_abs_eval','theorem replay')in s
assert 'example : @Roth.one_le_prod_pow_mul_abs_eval = @Integer279Original.replay := Subsingleton.elim _ _'in s
assert 'INT279_AUDIT: requested=293; unique=293'in msg('original-receipt.json')and 'INT279_AUDIT_PRESENT: present=293; values=293'in msg('original-receipt.json')
assert 'INT279_DIRECT_CONSUMER: _private.Roth.Main.0.Roth.one_lt_roth_eval_bound_aux'in msg('original-receipt.json')and 'INT279_DIRECT_TYPE_CONSUMER:'not in msg('original-receipt.json')
base=rd('input-manifest.json');assert base==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
fresh=rd('inputs.json');assert len(fresh)==len(base['sources_and_pins'])==17
for x in fresh:assert x['match']and x['sha256']==base['sources_and_pins'][x['path']]['sha256']==sha(R/x['path'])and x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')==dict(inputs=fresh,unchanged=True)
for m,lines in [('Main',588),('LeanEval',66)]:
 p=D/f'source-{m}.lean.txt';assert sha(p)==sha(R/f'Roth/{m}.lean')and len(p.read_text().splitlines())==lines
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']==sha(D/x['archive'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
pc=rd('prefix-controls.json');prefixes={}
for k,count in [('isolated',18),('disk',9)]:
 p=D/(k+'-prefix.lean.txt');assert sha(p)==pc[k+'_sha256'];prefixes[k]=re.findall(r'^import (.+)$',p.read_text(),re.M);assert len(prefixes[k])==pc[k+'_import_count']==count
assert not pc['extra_imports']and pc['root_exclusive_native']
assert pc['isolated_sha256']=='21ab5855caf720fa179e2823c041474682e949f2c298e3096be6e1877dd55217'
assert pc['disk_sha256']=='363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593'
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {x['label']for x in v['accepted']}=={'original','generic','signed','recovery','edges','clearing','composition','callers','shape','semiring-clearing'}
for e in v['accepted']:
 p=D/e['source'];s=p.read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(p)==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 assert q['executor']['owner']=='root'and q['request']==e['original_execution_request']and q['elapsed_ms']==e['elapsed_ms']
 assert not q['result'].get('isError',False)and z['success']and not z.get('timed_out',False)
 assert not[x for x in diags(e['receipt'])if x['severity']in['error','warning']or x.get('category')=='sorry']
 assert max(map(len,s.splitlines()))<=100
 imports=re.findall(r'^import (.+)$',s,re.M)
 if e['format']=='disk':assert z['partial']is False and not z['failed_dependencies']and s.startswith((D/'disk-prefix.lean.txt').read_text())and imports==prefixes['disk']
 else:assert q['request']['code']==s and '#check_failure '+N in s and imports==prefixes['isolated']and s.startswith((D/'isolated-prefix.lean.txt').read_text())
 t='\n'.join(x['message']for x in diags(e['receipt'])if x['line']>=e['native_region_start_line']);assert 'sorryAx'not in t and 'PANIC'not in t
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',t)
 if e['axiom_print_required']:assert ax
 for xs in ax:assert{x.strip()for x in xs.split(',')if x.strip()}<=allowed
 assert all(x in t for x in e['required_info']),e['label']
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 if 'code'in q['request']:assert q['request']['code']==(D/e['source']).read_text()
 assert any(x['severity']in['error','warning']for x in diags(e['receipt']))
assert v['attempt_accounting']['native_executions']==14==len(v['accepted'])+len(v['other_executions'])
# Reconstruct fullMain inlining from exact source, including only advertised substitutions.
main=(D/'source-Main.lean.txt').read_text();main=main[main.index('namespace Roth'):].replace('namespace Roth','namespace Integer279Full\nopen Roth',1).replace('end Roth','end Integer279Full');main=main.replace(original.strip(),'')
body=original[original.index(':= by')+len(':= by'):].strip('\n').replace('hQ j','hQd j').replace('hq j','hq0 j')
call='(one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne)';typ='1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)|'
assert main.count(call)==1
main=main.replace(call,'(show '+typ+' from by\n'+'\n'.join('  '+l for l in body.splitlines())+')')
main=main.replace('* |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| from by','*\n      |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| from by')
a=main.index('/-- If an integer polynomial `Q` of multidegree');b=main.index('-- Denominator growth',a);main=main[:a]+main[b:]
assert (D/'callers3-executed.lean.txt').read_text()==(D/'disk-prefix.lean.txt').read_text()+'\n'+main+'\n#print axioms Integer279Full.roth_rat\n'
rec=(D/'recovery-executed.lean.txt').read_text()
assert original.split(':= by')[0].replace('theorem one_le_prod_pow_mul_abs_eval','theorem recovery')+':= by\n  exact Integer279.generic Q hQ h hq hne'in rec
c=rd('callers.json');assert len(c['explicit_proof_callers'])==1 and c['explicit_proof_callers'][0]['call']==476 and c['external_to_file_count']==0
ph=rd('phase-checks.json');assert len(ph['modern9'])==9 and len(ph['proofstrategy5'])==5 and len(ph['statement_shape3'])==3 and len(ph['infrastructure_risks'])==6
fm=rd('formal-search-matrix.json');assert len(fm['cells'])==15 and {(x['form'],x['method'])for x in fm['cells']}=={(f,m)for f in ['current','standard','abstract']for m in ['leanfinder','loogle','leansearch','rg','local']}
for x in fm['cells']:assert(D/x['receipt']).is_file()
for f in ['current','standard','abstract','semiring']:
 assert result('formal-'+f+'-local.json')['index']in['error','warming','consulted','unavailable']
 for m in ['leanfinder','leansearch','loogle']:assert not rd('formal-'+f+'-'+m+'.json')['result'].get('isError',False)
 assert(D/('formal-'+f+'-rg.json')).is_file()
lit=rd('literature.json');assert len(lit['general_queries'])>=3 and len({x['q']for x in lit['general_queries']})>=3
assert{x['channel']for x in lit['channels']}=={'web-specific','web-general','web-alias','nlab','ncatlab','stacks','mathoverflow','arxiv'}and not lit['third_party_bodies_persisted']
for n in ['web-batch0.json','web-batch3.json','web-batch6.json','primary.json','reviewer-web.json']:
 z=rd(n);assert re.fullmatch('[0-9a-f]{64}',z['response_sha256'])and z['response_bytes']>0 and z['request']
assert 'site:ncatlab.org/ncatlab'in lit['channels'][4]['query']and 'after:2021-10-29 before:2026-10-30'in lit['channels'][7]['query']
assert lit['optional_channel']['channel']=='ask_chatgpt_math'and lit['local_channel']['channel']=='local'
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
print('PASS canonical279 currentmanifest/phases17inputs/exact293/native10+rejected4/fullMaincaller/formal15+semiring5/links')
