"""Final293-only validated report/evidence publication. No production mutations or force pushes."""
from pathlib import Path
import json,hashlib,subprocess,sys,re
R=Path('/Users/ramin/LEAN/Roth');B=Path('/private/tmp/roth-overview');O=R/'.mathlib-quality/overview';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text());run=lambda a:subprocess.run(a,cwd=R,check=True)
assert sys.argv[1:]==['--complete293']
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='ramin-cleanup'
p=load(O/'progress.json');assert p['status']=='complete'and len(p['completed_declarations'])==293 and p['next_declaration']is None
N=p['completed_declarations'][-1]['declaration'];D=O/'evidence'/N;F=O/'evidence/final'
ready=load(F/'final-readiness.json');assert ready['status']=='PASS'and ready['root_reviewed']and ready['declaration_count']==293
assert H(R/'PROJECT_OVERVIEW.md')==ready['final_overview_sha256']
post=load(F/'postintegration-validation.json');assert post['status']=='PASS'and all(x['exit_code']==0 for x in post['checks'])
for path,x in load(O/'evidence/shared/input-manifest.json')['sources_and_pins'].items():assert H(R/path)==x['sha256']
run(['python3',str(D/'validate.py'),str(R)])
run(['python3',str(F/'validate_portable_semantic_pairs.py'),str(R),str(F/'pairwise'),str(F/'final-completed-inventory-preparation.json'),'--require-complete'])
run(['python3',str(F/'validate_portable_global_evidence.py'),str(R),str(F),'--require-complete'])
paths=['PROJECT_OVERVIEW.md','.mathlib-quality/overview/README.md','.mathlib-quality/overview/progress.json','.mathlib-quality/overview/progress.md','.mathlib-quality/overview/mathlibable/'+N+'.md','.mathlib-quality/overview/evidence/'+N,'.mathlib-quality/overview/evidence/final']
run(['git','diff','--check']);run(['git','add','--',*paths])
white=subprocess.run(['git','diff','--cached','--check'],cwd=R,text=True,capture_output=True)
if white.returncode:
 assert white.stdout and not white.stderr
 findings=white.stdout.splitlines()
 for line in findings:
  match=re.fullmatch(r'(.+):(\d+): new blank line at EOF\.',line);assert match,line
  f=R/match[1];assert f.parent==D,line
  if f.name=='disk-prefix.lean.txt':
   assert H(f)=='363a6821de56e15a68978bcfef1f74e28eb837482667eba3b9ef498e98cea593'
  elif f.name=='local-source-section6.tex.txt':
   assert f.read_text()=='\n'.join((R/'.mathlib-quality/references/clean.tex').read_text().splitlines()[1138:1194])+'\n'
  else:raise AssertionError(line)
 accept=load(D/'root-acceptance.json');accept['whitespace_exception']=dict(reason='Preserve exact immutable copied disk9 prefix and exact reference excerpt bytes; only byte-verified final blank lines permitted, no trailing-space exception.',actual_findings=findings)
 (D/'root-acceptance.json').write_text(json.dumps(accept,indent=2,ensure_ascii=False)+'\n')
 run(['git','add','--',str((D/'root-acceptance.json').relative_to(R))])
 run(['git','-c','core.whitespace=-blank-at-eof','diff','--cached','--check'])
staged=subprocess.check_output(['git','diff','--cached','--name-only','-z'],cwd=R,text=True).rstrip('\0').split('\0');assert staged
for f in staged:assert f in paths or any(f.startswith(x+'/')for x in paths[-2:]),f
for f in staged:assert (R/f).stat().st_size<50_000_000,f
run(['python3',str(B/'verify_published.py')]);run(['git','diff','--cached','--stat']);run(['git','commit','--quiet','-m','Complete full Roth overview and all293 declaration assessments']);run(['git','push','origin','HEAD:ramin-cleanup'])
assert not subprocess.check_output(['git','status','--porcelain'],cwd=R,text=True)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=R)==subprocess.check_output(['git','rev-parse','origin/ramin-cleanup'],cwd=R)
run(['git','status','--short','--branch']);print('PASS complete293 review committed/pushed; production/pins unchanged; remote branch synced')
