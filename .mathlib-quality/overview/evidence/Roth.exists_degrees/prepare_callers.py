from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
meta=json.loads(Path('/private/tmp/roth-overview/review/corrected-manifest.json').read_text())
t=next(x for x in meta if x['name']=='Roth.exists_degrees');c=next(x for x in meta if x['name']=='Roth.exists_roth_approximants_aux')
(D/'caller-excerpt.lean.txt').write_text(c['source']+'\n')
concl='∃ r'+t['source'].split(': ∃ r',1)[1].split(':= by',1)[0].strip()
call='exists_degrees hδ0 hδ1 hq1\n    (fun i j hij ↦ (h50 i j hij).le)'
inline='(show '+concl+' from by\n    have hq := hq1\n    have h50 := fun i j hij ↦ (h50 i j hij).le\n'+''.join('  '+l+'\n' for l in t['body'].removeprefix('by\n').splitlines()).rstrip()+')'
inlined=c['source'].replace('private lemma exists_roth_approximants_aux','theorem inlined').replace(call,inline)
replaced=c['source'].replace('private lemma exists_roth_approximants_aux','theorem replaced').replace('exists_degrees hδ0 hδ1 hq1','Degrees278Recovery.all_positive_delta hδ0 hq1')
s=(D/'disk-prefix.lean.txt').read_text()+'\n'+(D/'generic-body.lean.txt').read_text()+'\n'+(D/'recovery-body.lean.txt').read_text()+'\nnamespace Degrees278Callers\nopen Roth\nopen MvPolynomial\n'+inlined+'\n\n'+replaced+'\nend Degrees278Callers\n\n'
s+='''open Lean Elab Term in
elab "degrees278_original_caller" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.Main `Roth.exists_roth_approximants_aux)
example : degrees278_original_caller = @Degrees278Callers.inlined := Subsingleton.elim _ _
example : degrees278_original_caller = @Degrees278Callers.replaced := Subsingleton.elim _ _
#print axioms Degrees278Callers.inlined
#print axioms Degrees278Callers.replaced
'''
# Wrap only the newly composed show/conclusion line to <=100.
s=s.replace(' := (show ∃ r', ' :=\n    (show ∃ r')
assert max(map(len,s.splitlines()))<=100,[(i,len(l),l)for i,l in enumerate(s.splitlines(),1)if len(l)>100]
p=D/'callers-executed.lean.txt';p.write_text(s)
(D/'root-requests/callers01.json').write_text(json.dumps(dict(id='callers01',operation='diagnostics',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt='callers01-receipt.json',arguments=dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45)),indent=2)+'\n')
print('Full actual caller inline and all-positive replacement ready')
