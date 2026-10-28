from pathlib import Path
import re,json
D=Path(__file__).resolve().parent;R=Path.cwd()
def transform(s,ns):
 b=s[s.index('namespace Roth'):].replace('namespace Roth','namespace '+ns+'\nopen Roth',1).replace('end Roth','end '+ns)
 b=b.replace('/-- The coefficient bound `B_1 = ⌊q_1^{δ r_1}⌋`. Source: §6, eq. (37). -/\n','')
 b=re.sub(r'^noncomputable def mainCoeffBound .*\n','',b,flags=re.M)
 b=b.replace('mainCoeffBound δ q₁ r₁','⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊')
 b=b.replace('mainCoeffBound δ (q 0) (r 0)','⌊(q 0 : ℝ) ^ (δ * r 0)⌋₊')
 b=b.replace('[mainCoeffBound, ','[')
 if ns=='Coeff232MainInline':
  for n in ['main_lemma','three_small_factors','mul_log_div_two_lt_log_mainCoeffBound']:
   b=re.sub(r'\b'+n+r'\b','Coeff232Inline.'+n,b)
 b=b.replace('mainCoeffBound^δ','the natural floor to δ')
 assert not re.search(r'\bmainCoeffBound\b',b)
 return b
code=(D/'disk-prefix.lean.txt').read_text()+transform((D/'source-MainLemma.lean.txt').read_text(),'Coeff232Inline')+'\n'+transform((D/'source-Main.lean.txt').read_text(),'Coeff232MainInline')
checks='\nrun_cmd Lean.Elab.Command.liftTermElabM do\n'
cs=json.load(open(D/'target-metadata.json'))['source_callers']
rows=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
for c in cs:
 x=next(x for x in rows if x['name']==c['name']and x['file']==c['file']);nm=x['name'].split('.')[-1];ns='Coeff232Inline'if x['file'].endswith('MainLemma.lean')else'Coeff232MainInline'
 old='`'+x['name']if x['visibility']!='private'else '(Lean.mkPrivateNameCore `'+x['file'][:-5].replace('/','.')+'\n      `'+x['name']+')'
 checks+='  do\n    let old ← Lean.getConstInfo '+old+'\n    let new ← Lean.getConstInfo ``'+ns+'.'+nm+'\n    unless ← Lean.Meta.isDefEq old.type new.type do\n      throwError "COEFF232_INLINE_SIGNATURE_MISMATCH"\n'
 checks+=''
checks+='  Lean.logInfo "COEFF232_INLINE_ALL8_ORIGINAL_SIGNATURES: PASS"\n'
for ns,mod in [('Coeff232Inline','MainLemma'),('Coeff232MainInline','Main')]:
 checks+='namespace '+ns+'\n'
 for x in rows:
  if x['file']=='Roth/'+mod+'.lean' and x['name']!='Roth.mainCoeffBound':checks+='#print axioms '+x['name'].split('.')[-1]+'\n'
 checks+='end '+ns+'\n'
code+='\n'+checks
lines=[]
for l in code.splitlines():
 while len(l)>100:
  p=l.rfind(' ',0,99);lines.append(l[:p]);l='      '+l[p+1:]
 lines.append(l)
code='\n'.join(lines)+'\n';assert max(map(len,code.splitlines()))<=100
(D/'inline-executed.lean.txt').write_text(code);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(code)
print('Full actual two-module inline replay prepared',len(lines),'lines; eight signatures')
print('\n'.join(lines[-85:]))
