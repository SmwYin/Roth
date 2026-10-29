from pathlib import Path
import json
D=Path(__file__).resolve().parent
for n in ['validation-draft-scratch.json','validation-draft-integrated.json','secret-scan-draft.json']:
 assert json.loads((D/n).read_text())['result']['exit_code']==0
for n in ['assessment.json','verification.json']:
 p=D/n;x=json.loads(p.read_text());x['completed']=True
 if n=='assessment.json':x['phases']['8']='PASS';x['allphases']='PASS'
 p.write_text(json.dumps(x,indent=2)+'\n')
(D/'freeze-status.json').write_text(json.dumps(dict(declaration='Roth.roth_rat',completed=True,root_acceptance='pending',draft_gates='actual scratch/integrated-layout/secret PASS before completiontrue',native_release=True,native_owner='root',note='No further native requests needed; original/generality/shape/edges/modern accepted and immutable. Root independently reviews/publishes.'),indent=2)+'\n')
print('Completedtrue after actual draft gates; native requests released; final gates required')
