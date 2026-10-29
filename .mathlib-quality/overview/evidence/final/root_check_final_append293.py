"""Append ONLY final293 root-authored semantic judgments using explicit candidate report paths.
The explicit reviewed JSON supplies mathematical comparisons/actions. No Git/native execution.
"""
from pathlib import Path
import json,hashlib,itertools,sys,ast
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text())
S=Path(sys.argv[1]).resolve();assert S.parent==B;s=load(S);I=load(B/'final-completed-inventory-preparation.json');n=s['canonical_index'];assert I['completed_count']==n and s['root_reviewed']is True
assert n==293 and I['published_count']==292 and I['has_unpublished_final_candidate']
rows=I['rows'];y=rows[-1];assert y['root_reviewed_unpublished_final_candidate'];N=y['declaration'];assert N==s['declaration']and y['report_sha256']==s['accepted_report_sha256']and y['verdict']==s['verdict']
notes=None
for node in ast.parse((B/'review_mainlemma_tail_pairs.py').read_text()).body:
 if isinstance(node,ast.Assign)and any(isinstance(v,ast.Name)and v.id=='module_notes'for v in node.targets):notes=ast.literal_eval(node.value)
assert notes;notes.update(s.get('module_context_overrides',{}))
f=B/'final-completed-cross-module-pairwise-preparation.json';d=load(f);t=load(B/'final-completed-theta-pairwise-preparation.json');seen={tuple(sorted((x['a'],x['b'])))for x in d['rows']+t['rows']};assert len(seen)==(n-1)*(n-2)//2
assert set(s['specific_comparisons'])<={x['declaration']for x in rows[:-1]}
def txt(x):
 if isinstance(x,list):return '; '.join(txt(v)for v in x)
 if isinstance(x,dict):return '; '.join(k+': '+txt(v)for k,v in x.items())
 return str(x)
for x in rows[:-1]:
 a=x['declaration'];key=tuple(sorted((a,N)));assert key not in seen
 reason='A fact: '+x['what']+' A mechanism: '+x['how']+' A hypotheses: '+txt(x['hypotheses'])+' B reviewed content: '+s['mathematical_content']+' Module contrast for A: '+notes[x['file']]
 c=s['specific_comparisons'].get(a,{});ev=[]
 for z in[x,y]:assert H(Path(z.get('report_source',str(R/z['report']))))==z['report_sha256'];ev.append({k:z[k]for k in['declaration','canonical_index','file','start_line','end_line','source_sha256','report','report_sha256']})
 d['rows'].append(dict(a=a,b=N,same_statement=c.get('same_statement',False),same_proof=c.get('comparison',reason),action=c.get('action',s['pair_action']),review_method=s['root_review_method'],evidence=ev));seen.add(key)
assert seen=={tuple(sorted(x['declaration']for x in p))for p in itertools.combinations(rows,2)}
d['completed_count']=n;f.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
a=dict(s['action_synthesis']);a.update(status='ROOT-REVIEWED'+str(n)+' action supplement; final293 acceptance separate',completed_count=n,accepted_assessment={k:y[k]for k in['canonical_index','declaration','verdict','report','report_sha256']},semantic_pair_review_spec={'source':S.name,'sha256':H(S)},pair_generator={'source':Path(__file__).name,'sha256':H(Path(__file__))},module_context_source={'source':'review_mainlemma_tail_pairs.py','sha256':H(B/'review_mainlemma_tail_pairs.py')},production_changes=False)
(B/s['synthesis_artifact']).write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n')
if s.get('new_yes_group'):
 assert y['verdict'].startswith('YES');p=B/'final-completed-yes-mathematical-groups-preparation.json';g=load(p);assert not any(z['declaration']==N for q in g['groups']for z in q['assessments']);g['groups'].append({'mathematical_group':s['new_yes_group'],'assessments':[{k:y[k]for k in['canonical_index','declaration','what','verdict','report','report_sha256','native_direct_body_dependencies']}]});p.write_text(json.dumps(g,indent=2,ensure_ascii=False)+'\n')
print('PASS',n-1,'new explicit root-reviewed comparisons;',len(seen),'exact accepted-prefix pairs; action supplement recorded')
