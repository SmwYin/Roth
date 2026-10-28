from pathlib import Path
import re,json
D=Path(__file__).resolve().parent;R=Path.cwd();rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
s=(D/'source-MainLemma.lean.txt').read_text();b=s[s.index('namespace Roth'):]
b=b.replace('namespace Roth','namespace Box233Inline\nopen Roth',1).replace('end Roth','end Box233Inline')
start=b.index('/-- Integer polynomials with coordinate degrees')
end=b.index('/- The polynomial with coefficient',start)
b=b[:start]+b[end:]
b=re.sub(r'\bboxFamily r B\b','({W : MvPolynomial _ ℤ | (∀ j, degreeOf j W ≤ r j) ∧\n      ∀ d, 0 ≤ W.coeff d ∧ W.coeff d ≤ (B : ℤ)})',b)
assert not re.search(r'\bboxFamily\b',b)
checks='\nrun_cmd Lean.Elab.Command.liftTermElabM do\n'
cs=json.load(open(D/'target-metadata.json'))['source_callers']
for c in cs:
 x=next(x for x in rows if x['name']==c['name']and x['file']==c['file']);nm=x['name'].split('.')[-1]
 old='`'+x['name']if x['visibility']!='private'else '(Lean.mkPrivateNameCore `Roth.MainLemma\n      `'+x['name']+')'
 checks+='  do\n    let old ← Lean.getConstInfo '+old+'\n    let new ← Lean.getConstInfo ``Box233Inline.'+nm+'\n    unless ← Lean.Meta.isDefEq old.type new.type do\n      throwError "BOX233_INLINE_SIGNATURE_MISMATCH {old.name}"\n'
checks+='  Lean.logInfo "BOX233_INLINE_ALL7_ORIGINAL_SIGNATURES: PASS"\n'
checks+='namespace Box233Inline\n'
for x in rows:
 if x['file']=='Roth/MainLemma.lean' and x['name']!='Roth.boxFamily':checks+='#print axioms '+x['name'].split('.')[-1]+'\n'
checks+='end Box233Inline\n'
code=(D/'disk-prefix.lean.txt').read_text()+b+checks
lines=[]
for l in code.splitlines():
 while len(l)>100:
  p=l.rfind(' ',0,99);lines.append(l[:p]);l='      '+l[p+1:]
 lines.append(l)
code='\n'.join(lines)+'\n';assert max(map(len,code.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print('Full actual MainLemma inline replay prepared',len(lines),'lines; seven signatures')
print('\n'.join(lines[-100:]))
