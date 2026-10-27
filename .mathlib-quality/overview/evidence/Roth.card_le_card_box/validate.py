"""Read-only validator for scratch and integrated layouts; current copy-manifest is authoritative."""
import pathlib,json,hashlib,re,sys
b=pathlib.Path(__file__).resolve().parent
r=pathlib.Path(sys.argv[1]).resolve() if len(sys.argv)>1 else pathlib.Path.cwd()
t='Roth.card_le_card_box'
def read(n):return json.loads((b/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report=b/'report.md'
if not report.exists():report=r/'.mathlib-quality/overview/mathlibable'/f'{t}.md'
a=read('assessment.json')
assert a['declaration']==t and a['file']=='Roth/Box.lean' and a['line']==65
assert a['completed'] and a['root_acceptance'] in ['pending','PASS'] and not a['production_edits']
assert a['verdict']=='BORDERLINE-needs-human' and a['unresolved']==[] and 1<=len(a['questions'])<=5
assert set(a['phases'])=={'0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8'}
assert all(v=='PASS' or(k=='4.5' and v.startswith('n/a')) for k,v in a['phases'].items())
m=read('input-manifest.json');assert len(m['sources_and_pins'])==17
for p,e in m['sources_and_pins'].items():assert sha(r/p)==e['sha256'],p
for e in read('source-hashes.json'):
 p=r/e['path'];assert len(p.read_bytes())==e['bytes'] and sha(p)==e['sha256'],p
assert 'Exit code: 0' in (b/'baseline-build.txt').read_text()
manifest=read('copy-manifest.json');assert isinstance(manifest,dict) and isinstance(manifest['files'],list)
for e in manifest['files']:
 assert not pathlib.Path(e['source']).is_absolute()
 p=report if e['source']=='report.md' else b/e['source']
 assert len(p.read_bytes())==e['bytes'] and sha(p)==e['sha256'],e['source']
v=read('verification.json');assert v['unresolved']==[] and len(v['accepted'])==2
for e in v['accepted']:
 p=b/e['source'];code=p.read_text();assert sha(p)==e['source_sha256']
 assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b|set_option\s+(maxHeartbeats|maxRecDepth)',code)
 z=read(e['receipt']);native=z['result'];assert not native.get('isError',False)
 sc=native.get('structuredContent',native);out=sc.get('result',sc)
 assert out['success'] and not out.get('partial',False) and not out.get('timed_out',False) and not out.get('failed_dependencies')
 ds=out.get('items',out.get('diagnostics',[]));assert not any(d.get('severity') in ['error','warning'] for d in ds)
 if 'code' in z['request']:assert z['request']['code']==code
 c=read(e['source_check']);assert c['matched_at_freeze'] and c['disk_sha256']==c['retained_sha256']==e['source_sha256']
 ax=0
 for d in ds:
  msg=d.get('message','');assert 'sorryAx' not in msg
  if 'depends on axioms:' in msg:
   ns=re.search(r'depends on axioms: \[([^\]]*)\]',msg).group(1).split(',')
   assert {x.strip() for x in ns if x.strip()}<={'propext','Classical.choice','Quot.sound'};ax+=1
 assert ax>=5
raw=(b/'raw-executed.lean.txt').read_text();assert 'import Roth' not in raw
for s in ['#check_failure Roth.card_le_card_box','theorem expanded_original','theorem fin_injection','Nat.lt_succ_of_le','theorem function_family','theorem support_interval','theorem support_finite_bound','Finsupp.card_Iic']:assert s in raw,s
project=(b/'project-executed.lean.txt').read_text()
for s in ['#check @Roth.card_le_card_box','namespace CardLeBoxAssessment','theorem replay','theorem strict_shape','theorem support_local_shape','theorem real_product_caller','theorem natural_product_caller','Finset.card_pair']:assert s in project,s
for method in ['finder','leansearch','loogle','local_search']:
 for form in ['current','standard','abstract']:
  z=read(f'{method}-{form}.json');assert z['request'] and z['response']['status']=='fulfilled'
  assert not z['response']['value'].get('isError',False)
for form in ['current','standard','abstract']:
 z=read(f'rg-{form}.json');assert z['command'] and z['exit_code']==0 and z['stdout']
assert read('full-name-source-search.json')['exit_code']==1
queries=[]
for i in range(13):
 z=read(f'web-{i}.json');assert z['request'] and z['status'] and re.fullmatch('[a-f0-9]{64}',z['response_sha256']) and z['response_bytes']>0
 queries.extend(x['q'] for x in z['request'].get('search_query',[]))
assert len(set(queries))>=10
lit=read('literature-summary.json');assert len(lit['channels'])==8 and lit['synthesis']
assert read('q8-diagnostic.json')['fired']
c=read('explicit-callers.json');assert c['count']==2 and c['declaration_callers']==2 and len(c['external_files'])==2
s=report.read_text()
for token in ['Phase 4.5','Phase 4.6','Phase 5.5','Phase 6.0','Phase6b','three-existing-fact','Nat.lt_succ_of_le','logically equivalent','2 occurrences','four-fact','seven existing','BORDERLINE-needs-human']:assert token in s,token
for link in re.findall(r'\]\(([^)]+)\)',s):
 if link.startswith(('https:','http:')):continue
 prefix=f'../evidence/{t}/';assert link.startswith(prefix),link
 assert (b/link[len(prefix):]).is_file(),link
print('PASS: complete phases;17 source/pin hashes; exact native success/standard axioms; actual5x3 methods; all literature channels;2 actual callers; generic3/original4/expanded7 facts; current manifest and links')
