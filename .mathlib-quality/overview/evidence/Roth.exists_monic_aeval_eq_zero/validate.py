#!/usr/bin/env python3
"""Read-only canonical272 validation against the CURRENT recursive manifest in either layout."""
from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.exists_monic_aeval_eq_zero';draft='--draft' in sys.argv

def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
def info(n):
 z=result(n);return '\n'.join(x['message']for x in z.get('items',z.get('diagnostics',[])))
def report():
 for p in [D/'report.md',D.parent.parent/'mathlibable'/(N+'.md')]:
  if p.is_file():return p
 raise AssertionError('missing report')
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==v['declaration']==N and a['canonical_index']==v['canonical_index']==272
assert a['verdict']=='BORDERLINE-needs-human' and a['root_acceptance']in ['pending','PASS']
assert not a['parent_verdict_inherited'] and not a['cost_based_verdict']
assert not a['unresolved'] and not v['unresolved']
assert len(a['questions'])==3
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(x=='PASS' or (draft and k=='8' and x=='pending')for k,x in a['phases'].items())
if not draft:assert a['completed'] and v['completed'] and a['allphases']=='PASS'
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type'] and o['type'].startswith('∀ {α : ℝ}')
assert o['generalization']['verified'] and 'Nontrivial R' in o['generalization']['proposed_type']
assert rd('native-type.json')['elided_characters']==[109933]
assert not rd('native-type.json')['full_kernel_printer_body']
assert o['project_dependencies']==rd('native-type.json')['original_project_dependencies']==[]
m=rd('copy-manifest.json');assert m['declaration']==N;covered=set()
for x in m['files']:
 pref='.mathlib-quality/overview/evidence/'+N+'/'
 if x['destination']=='.mathlib-quality/overview/mathlibable/'+N+'.md':p=report();rel='report.md'
 else:
  assert x['destination'].startswith(pref);rel=x['destination'][len(pref):];p=D/rel
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 assert rel not in covered;covered.add(rel)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
files={str(p.relative_to(D))for p in D.rglob('*')if p.is_file()and p.name not in excluded}
assert files<=covered,files-covered
assert not list(D.rglob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'};assert set(v['standard_axioms'])==allowed
assert {e['label']for e in v['accepted']}=={'original','isolated','callers','composition','consumers'}
for e in v['accepted']:
 s=(D/e['source']).read_text();q=rd(e['receipt']);z=result(e['receipt'])
 assert sha(D/e['source'])==e['source_sha256']==q['executor']['worker_request']['source_sha256']
 assert q['executor']['owner']=='root' and q['request']==e['original_execution_request']
 assert isinstance(q['elapsed_ms'],int) and not q['result'].get('isError',False)
 assert z['success'] and not z.get('timed_out',False)
 if e['format']=='disk':
  assert z['partial']is False and not z['failed_dependencies']
  assert s.startswith((D/'disk-prefix.lean.txt').read_text())
  assert len(re.findall('^import ',s,re.M))==9
 else:
  assert q['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
  ims=re.findall('^import (.+)$',s,re.M);assert len(ims)==18
  assert not any(x.startswith('Roth')for x in ims) and '#check_failure '+N in s
 ds=z.get('items',z.get('diagnostics',[]))
 assert not [x for x in ds if x['severity']in ['error','warning']or x.get('category')=='sorry']
 text='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in text and 'PANIC'not in text
 ax=re.findall(r'depends on axioms: \[([^]]*)\]',text)
 if e['axiom_print_required']:assert ax
 for x in ax:assert {t.strip()for t in x.split(',')if t.strip()}<=allowed
 assert all(x in text for x in e['required_info']),e['label']
 assert max(map(len,s.splitlines()))<=100
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
for e in v['other_executions']:
 q=rd(e['receipt']);assert sha(D/e['source'])==e['source_sha256']
 assert q['executor']['worker_request']['source_sha256']==e['source_sha256']
 if 'code'in q['request']:assert q['request']['code']==(D/e['source']).read_text()
assert len(list(D.glob('*-receipt.json')))==v['attempt_accounting']['native_executions']==8
assert not result('isolated-receipt.json')['success']
assert result('isolated2-receipt.json')['success']
assert any(x['severity']=='warning'for x in result('isolated2-receipt.json')['diagnostics'])
b=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(b)==len(fresh)==17
assert rd('input-manifest.json')==json.loads((R/'.mathlib-quality/overview/evidence/shared/input-manifest.json').read_text())
for x in fresh:
 assert x['match'] and x['sha256']==b[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
assert rd('fresh-final-inputs.json')['inputs']==fresh and rd('fresh-final-inputs.json')['unchanged']
for mod in ['Main','LeanEval']:assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):assert sha(R/x['path'])==x['sha256']==sha(D/x['archive'])
l=rd('literature-source.json');assert sha(R/l['path'])==l['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293
assert order[271]==rd('canonical-entry.json') and order[271]['name']==N
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'else('public',x['name'])for x in order]
for n in ['original-executed.lean.txt','consumer-scope-executed.lean.txt']:
 s=(D/n).read_text();ars=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(ars)==1
 terms=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",ars[0])
 actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in terms]
 assert actual==expected and len(actual)==len(set(actual))==293
x=info('original-receipt.json')
assert 'MONIC272_AUDIT: requested=293; unique=293'in x
assert 'MONIC272_AUDIT_PRESENT: present=293; values=293'in x
assert re.findall('MONIC272_DIRECT_CONSUMER: ([^\n]+)',x)==['_private.Roth.Main.0.Roth.exists_roth_parameters_aux']
assert 'MONIC272_DIRECT_TYPE_CONSUMER:'not in x
x=info('consumer-scope-receipt.json');c=rd('callers.json')
assert re.findall('MONIC272_TRANSITIVE_CONSUMER: ([^\n]+)',x)==c['transitive_canonical_consumers']
assert 'MONIC272_SIMP_MEMBER: false'in x
meta=rd('target-metadata.json');assert meta['source']in(R/'Roth/Main.lean').read_text()
replay='namespace Monic272Original\nopen Roth\n'+meta['source'].replace('theorem exists_monic_aeval_eq_zero','theorem replay',1)+'\nend Monic272Original\n'
assert (D/'original-executed.lean.txt').read_text().startswith((D/'disk-prefix.lean.txt').read_text()+replay)
caller=(D/'caller2-executed.lean.txt').read_text();main=(R/'Roth/Main.lean').read_text()
assert (D/'caller-original.lean.txt').read_text().strip()in main
for name,end in [('exists_roth_approximants_aux','-- Compare the nonzero'),('one_lt_roth_eval_bound_aux','-- Bound the common'),('roth_product_bound_aux','-- Compare logarithms'),('roth_log_bound_aux',"/-- Roth's theorem for irrational")]:
 start=main.index('private lemma '+name);stop=main.index(end,start)
 assert main[start:stop].replace('private lemma','theorem',1)in caller
assert 'example : originalParameters272 = @Monic272Inline.exists_roth_parameters_aux'in caller
assert 'example : @Roth.roth_of_isIntegral = @Monic272Inline.roth_of_isIntegral'in caller
assert 'example : @Roth.roth_rat = @Monic272Inline.roth_rat'in caller
assert caller.index('MONIC272_NONCIRCULAR')<caller.index('open LeanEval.NumberTheory.ThueSiegelRothProblem')
iso=(D/'isolated3-executed.lean.txt').read_text()
for token in ['[CommSemiring R] [Nontrivial R] [Semiring A]','[CommRing R] [Nontrivial R] [Ring A]',
 'integral hint 2','aeval (0 : PUnit)','aeval (0 : ℚ)','isIntegral_algebraMap','¬ ∃ f : PUnit[X]']:
 assert token in iso,token
com=(D/'composition-executed.lean.txt').read_text()
assert com.index('fail_if_success solve | exact?')<com.index('obtain ⟨f, hf, hf0⟩')
mat=rd('formal-search-matrix.json');assert mat['all15'] and len(mat['cells'])==15
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  q=rd(f'search-{form}-{method}.json')
  if method=='rg':assert q['command']and q['exit_code']in[0,1]
  else:
   assert q['request']and q['result']
   if method!='local_search':assert not q['result'].get('isError',False)
web=[rd(f'web-batch{i}.json')for i in range(4)]
for q in web:
 assert q['request'] and q['response_bytes']>0 and not q['full_response_persisted']
 assert re.fullmatch('[0-9a-f]{64}',q['response_sha256'])and'result'not in q
 for x in q['returned_titles_urls']:assert x['title'] and x['url'].startswith('https://')and'…'not in x['url']
assert len({x['q']for x in web[0]['request']['search_query']})==3
for domain in ['site:ncatlab.org/nlab','site:ncatlab.org/ncatlab','site:stacks.math.columbia.edu','site:mathoverflow.net','site:arxiv.org']:
 assert any(domain in x['q']for q in web for x in q['request'].get('search_query',[]))
assert any('after:2021-10-29'in x['q']and'before:2026-10-30'in x['q']for q in web for x in q['request'].get('search_query',[]))
assert len(rd('literature.json')['channels'])==10
assert sha(D/'isolated-prefix.lean.txt')==v['controls']['shared_prefix_sha256']
assert sha(D/'disk-prefix.lean.txt')==v['controls']['disk_prefix_sha256']
p=Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt')
if p.is_file():assert sha(p)==v['controls']['shared_prefix_sha256']
r=report().read_text()
for href in re.findall(r'\]\(([^)]+)\)',r):
 if href.startswith('../evidence/'+N+'/'):assert(D/href[len('../evidence/'+N+'/'):]).is_file(),href
 else:assert href.startswith('https://'),href
for token in ['BORDERLINE-needs-human','NOT-COMPOSABLE','Phase4.5','Phase4.6','Phase5.5','Phase6.0',
 'four Main roots','109933','three concrete future upstream questions','Nontrivial R']:
 assert token in r,token
assert rd('secret-guard.json')['exit_code']==0
print('PASS canonical272'+(' DRAFT'if draft else' FINAL')+': current recursive manifest; fresh17; exact293;5clean primary/8native; full actual caller; arbitrary-N semiring/ring guards; standard axioms;15formal; named literature; links')
