#!/usr/bin/env python3
"""Read-only portable canonical237 validator for current scratch/integrated evidence."""
from pathlib import Path
import json,hashlib,re,sys,subprocess
D=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
N='Roth.sqrt_lt_floor'
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(x):
 z=x['result']['structuredContent'];return z.get('result',z)
a=rd('assessment.json');v=rd('verification.json');o=rd('overview-entry.json')
assert a['declaration']==N and a['canonical_index']==237 and a['completed']
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert a['allphases']=='PASS' and all(x=='PASS' for x in a['phases'].values())
assert a['root_acceptance']in['pending','PASS'] and not a['unresolved'] and not v['unresolved']
assert a['verdict']=='BORDERLINE-needs-human' and 0<len(a['questions'])<=5
assert {'type','what','how','hypotheses','project_dependencies','caller_summary','mathlib_api_audit',
 'moral_duplications','generalization','missing_api','junk','action'}<=set(o)
assert o['type']==rd('native-type.json')['type']
assert o['project_dependencies']==['Roth.sqrt_lt_nat_floor_aux']
assert not rd('native-type.json')['printer_elision']
m=rd('copy-manifest.json');assert m['declaration']==N;seen=set()
for x in m['files']:
 name='report.md' if '/mathlibable/'in x['destination'] else Path(x['destination']).name
 p=D/name
 if not p.exists():p=R/x['destination']
 assert p.is_file() and sha(p)==x['sha256'] and p.stat().st_size==x['bytes'],p
 seen.add(name)
excluded={'copy-manifest.json','worker-copy-manifest.json','root-review.json','root-acceptance.json'}
assert {p.name for p in D.iterdir()if p.is_file()}-excluded<=seen
assert not list(D.glob('*.lean'))
allowed={'propext','Classical.choice','Quot.sound'}
assert set(v['standard_axioms'])==allowed
assert {e['label']for e in v['accepted']}=={'original','isolated','inline','sqrt-route','candidates-cli','power-route'}
for e in v['accepted']:
 r=rd(e['receipt']);s=(D/e['source']).read_text();assert sha(D/e['source'])==e['source_sha256']
 assert r['request']==e['original_execution_request'] and isinstance(r['elapsed_ms'],int)
 if e['format']=='cli':
  z=r['result'];assert z['exit_code']==0 and not z['stderr']
  assert r['request']['stdin']==s and r['request']['command']==['/Users/ramin/.elan/bin/lake','env','lean','--stdin']
  info=z['stdout'];assert ': error:' not in info and ': warning:' not in info
  assert s.startswith((D/'isolated-prefix.lean.txt').read_text())
  assert len(re.findall(r'^import ',s,re.M))==19
  assert 'import Mathlib.Algebra.Order.Floor.Semifield' in s
 else:
  assert not r['result'].get('isError',False);z=result(r)
  assert z['success'] and not z.get('timed_out')
  if e['format']=='raw':
   assert r['request']['code']==s and s.startswith((D/'isolated-prefix.lean.txt').read_text())
   assert len(re.findall(r'^import ',s,re.M))==18
   ds=z['diagnostics']
  else:
   assert z['partial']is False and not z.get('failed_dependencies')
   assert s.startswith((D/'disk-prefix.lean.txt').read_text())
   assert len(re.findall(r'^import ',s,re.M))==9
   ds=z['items']
  assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry']
  info='\n'.join(x['message']for x in ds if x['line']>=e['native_region_start_line'])
 assert 'sorryAx'not in info and 'LEAN_MCP_MAX_OUTPUT_CHARS'not in info
 for ax in re.findall(r'depends on axioms: \[([^]]*)\]',info):
  assert {x.strip()for x in ax.split(',')if x.strip()}<=allowed
 for t in e['required_info']:assert t in info,(e['label'],t)
 assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b|\baxiom\s|set_option\s+(maxHeartbeats|maxRecDepth)',s)
 assert max(map(len,s.splitlines()))<=100
 if e['format']in['raw','cli']:
  assert not re.search(r'^import Roth\b',s,re.M) and '#check_failure '+N in s
assert len(v['rejected'])==4
for e in v['rejected']:
 r=rd(e['receipt']);s=(D/e['source']).read_text()
 if e['format']=='cli':assert r['result']['exit_code']!=0 and r['request']['stdin']==s
 else:
  assert not result(r)['success'] and r['request']['code']==s
  assert any(x['severity']=='error'for x in result(r)['diagnostics'])
base=rd('input-manifest.json')['sources_and_pins'];fresh=rd('inputs.json')
assert len(base)==len(fresh)==17
assert len({x['path']for x in fresh})==17 and {x['path']for x in fresh}==set(base)
for x in fresh:
 assert x['match'] and x['sha256']==base[x['path']]['sha256']==sha(R/x['path'])
 assert x['bytes']==(R/x['path']).stat().st_size
for mod in['MainLemma','Main']:
 assert sha(R/('Roth/'+mod+'.lean'))==sha(D/('source-'+mod+'.lean.txt'))
for x in rd('mathlib-inputs.json'):
 assert sha(R/'.lake/packages/mathlib'/x['path'])==x['sha256']==sha(D/x['archive'])
local=rd('literature-local-input.json');assert sha(R/local['path'])==local['sha256']
order=json.loads((R/'.mathlib-quality/overview/declaration-order.json').read_text())
assert order==rd('canonical-snapshot.json') and len(order)==293 and order[236]==rd('canonical-entry.json')
assert order[236]['name']==N and order[236]['line']==115
expected=[('private',x['file'][:-5].replace('/','.'),x['name'])if x['visibility']=='private'
 else('public',x['name'])for x in order]
s=(D/'original-executed.lean.txt').read_text()
arrays=re.findall(r'let names : Array Lean.Name := #\[(.*?)\]',s,re.S);assert len(arrays)==1
items=re.findall(r"Lean\.mkPrivateNameCore\s+`([\w.']+)\s+`([\w.']+)|`([\w.']+)",arrays[0])
actual=[('private',mod,nm)if mod else('public',pub)for mod,nm,pub in items]
assert actual==expected and len(actual)==len(set(actual))==293
z=result(rd('original-receipt.json'));ds=z['items']
cs=rd('canonical-consumers.json');assert all(cs[k]==293 for k in['requested','unique','present','values'])
for marker,key in[('SQRT237_DIRECT_CONSUMER: ','direct_value'),('SQRT237_DIRECT_TYPE_CONSUMER: ','direct_type')]:
 assert[x['message'][len(marker):]for x in ds if x['message'].startswith(marker)]==cs[key]
assert len(cs['direct_value'])==3 and not cs['direct_type']
prep=rd('preparation-checks.json')
assert prep['exit_code']==prep['original_pre_execution_provenance']['observed_exit_code']==0
assert prep['source_sha256']==sha(D/'original-executed.lean.txt')
assert 'Read-only freeze-time recheck'in prep['scope'] and 'PASS exact293'in prep['stdout']
source=(D/'source-MainLemma.lean.txt').read_text();b=source[source.index('namespace Roth'):]
b=b.replace('namespace Roth','namespace Sqrt237Original\nopen Roth',1).replace('end Roth','end Sqrt237Original')
b=re.sub(r'\bsqrt_lt_floor\b','replay',b)
assert s.startswith((D/'disk-prefix.lean.txt').read_text()+b)
inline=(D/'inline-executed.lean.txt').read_text()
assert inline.count('namespace Sqrt237Inline')==2
inlineBodies=inline.split('\nrun_cmd Lean.Elab.Command.liftTermElabM do',1)[0]
assert 'sqrt_lt_floor'not in inlineBodies and 'sqrt_lt_nat_floor_aux'not in inlineBodies
assert inline.count('have sqrtLower {X : ℝ}')==3
assert 'theorem roth_product_bound_aux'in inline and '#print axioms Sqrt237Inline.roth_rat'in inline
# Reconstruct both entire caller modules from the pinned originals and exact local edits.
low="""  have sqrtLower {X : ℝ} (hX : 2 ≤ X) : √X < (⌊X⌋₊ : ℝ) :=
    have hfloor : (2 : ℝ) ≤ ⌊X⌋₊ := by exact_mod_cast Nat.le_floor hX
    (Real.sqrt_lt' (by positivity)).2 (by nlinarith only [Nat.lt_floor_add_one X, hfloor])
"""
b=(D/'source-MainLemma.lean.txt').read_text();b=b[b.index('namespace Roth'):]
b=b.replace('namespace Roth','namespace Sqrt237Inline\nopen Roth',1).replace('end Roth','end Sqrt237Inline')
start=b.index('private lemma sqrt_lt_nat_floor_aux');end=b.index('/-- The bound `3 ≤',start)
b=b[:start]+b[end:]
for name in ['mul_log_div_two_lt_log_mainCoeffBound','three_small_factors']:
 start=b.index('theorem '+name);i=b.index(':= by\n',start)+len(':= by\n');b=b[:i]+low+b[i:]
b=b.replace('(sqrt_lt_floor hX).1','(sqrtLower hX)')
c=(D/'source-Main.lean.txt').read_text();c=c[c.index('namespace Roth'):]
c=c.replace('namespace Roth','namespace Sqrt237Inline\nopen Roth',1).replace('end Roth','end Sqrt237Inline')
c=c.replace('private lemma roth_product_bound_aux','theorem roth_product_bound_aux')
start=c.index('theorem roth_product_bound_aux');i=c.index(':= by\n',start)+len(':= by\n')
c=c[:i]+low+c[i:]
old="""  obtain ⟨hsqB, hBX⟩ := sqrt_lt_floor ((by norm_num : (2 : ℝ) ≤ 4).trans
    (four_lt_rpow hδ0 hr0 h32').le)"""
new="""  have hX : 2 ≤ (q 0 : ℝ) ^ (δ * r 0) := (by norm_num : (2 : ℝ) ≤ 4).trans
    (four_lt_rpow hδ0 hr0 h32').le
  have hsqB := sqrtLower hX
  have hBX := Nat.floor_le (show 0 ≤ (q 0 : ℝ) ^ (δ * r 0) by positivity)"""
assert old in c;c=c.replace(old,new)
assert inline.startswith((D/'disk-prefix.lean.txt').read_text()+b+'\n'+c+'\n')
cs=rd('callers.json');assert cs['executable_occurrences']==3 and len(cs['callers'])==3
assert cs['external_to_file_declarations']==cs['external_to_file_files']==1
for c in cs['callers']:
 src='\n'.join((R/c['file']).read_text().splitlines()[c['line']-1:c['end_line']])+'\n'
 assert src==c['source'] and hashlib.sha256(src.encode()).hexdigest()==c['sha256']
 assert src.count('sqrt_lt_floor')==1 and c['full_proof_replayed'] and c['signature_checked']
for f in['source-search','tracked-source-search','inline-search','sqrt-floor-full-source-search','full-name-search']:
 x=rd(f+'.json');assert x['exit_code']in[0,1]and not x['stderr']
assert rd('source-search.json')['stdout']==rd('tracked-source-search.json')['stdout']
for form in['current','standard','abstract']:
 for method in['leanfinder','loogle','leansearch','local_search']:
  x=rd('search-'+form+'-'+method+'.json');assert x['form']==form and x['method']==method
  assert x['request']['query']and not x['result'].get('isError',False)
  assert 'items'in x['result']['structuredContent']
 x=rd('search-'+form+'-rg.json');assert x['exit_code']in[0,1]and not x['stderr']
for label in['general','nlab','ncatlab','stacks','mathoverflow','arxiv','primary']:
 x=rd('web-'+label+'.json');assert x['request']and x['summary']
 assert x['response']['status']=='returned'and x['response']['bytes']>0
 assert re.fullmatch('[a-f0-9]{64}',x['response']['sha256'])
 assert all(y['title'].strip()and y['url'].startswith('https://')for y in x['locators'])
 assert not any('...'in y['url']or re.search(r'(?i)(signature|token|credential)=',y['url'])for y in x['locators'])
assert len(rd('web-general.json')['request']['search_query'])>=3
assert 'site:ncatlab.org/ncatlab'in rd('web-ncatlab.json')['request']['search_query'][0]['q']
q=rd('web-arxiv.json')['request']['search_query'][0]['q']
assert 'after:2021-10-28'in q and'before:2026-10-29'in q
assert (D/'isolated-prefix.lean.txt').read_bytes()==Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes() if Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').exists() else True
report=D/'report.md'
if not report.exists():report=R/'.mathlib-quality/overview/mathlibable'/f'{N}.md'
s=report.read_text()
for target in re.findall(r'\]\((\.\./evidence/[^)]+)\)',s):
 assert(D/target.split('/'+N+'/',1)[1]).is_file(),target
guard=subprocess.run([sys.executable,str(R/'.mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py'),str(D)],capture_output=True,text=True)
assert guard.returncode==0,(guard.stdout,guard.stderr)
print('PASS canonical237 completed phases, current manifest, exact sources, native proofs, signatures, hashes, searches and links')
