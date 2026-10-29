from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.exists_nat_mul_isIntegral';O=R/'.mathlib-quality/overview'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
order=json.loads((O/'declaration-order.json').read_text());assert order[267]['name']==N
put('canonical-snapshot.json',order);put('canonical-entry.json',order[267]);meta=next(x for x in json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))if x['name']==N);put('target-metadata.json',meta)
b=json.load(open(O/'evidence/shared/input-manifest.json'));put('input-manifest.json',b);xs=[]
for p,v in b['sources_and_pins'].items():
 h=sha(R/p);assert h==v['sha256'];xs.append(dict(path=p,sha256=h,bytes=(R/p).stat().st_size,match=True))
put('inputs.json',xs);(D/'baseline-build.txt').write_bytes((O/'evidence/shared/baseline-build.txt').read_bytes())
put('accepted-verdict-snapshot.json',json.load(open(O/'progress.json')))
(D/'source-Main.lean.txt').write_bytes((R/'Roth/Main.lean').read_bytes())
for n,args in [('source-search',['rg','--no-ignore','-n',r'\bexists_nat_mul_isIntegral\b','Roth','Roth.lean']),('tracked-source-search',['git','grep','-n','-w','exists_nat_mul_isIntegral','--','Roth','Roth.lean']),('source-inventory',['rg','--files','--no-ignore','Roth']),('inline-search',['rg','--no-ignore','-n',r'exists_integral_multiple|natAbs_pos|Int.sign_mul_self|exists_nsmul_eq|integralNormalization','Roth','Roth.lean']),('local-literature',['rg','-n',r'algebraic number|integer.*multiple|M>0|M> 0|M > 0|algebraic integer','.mathlib-quality/references/clean.tex'])]:
 z=subprocess.run(args,text=True,capture_output=True);put(n+'.json',dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr))
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1147:1189])+'\n')
math=[]
for p in ['Mathlib/RingTheory/Algebraic/Integral.lean','Mathlib/RingTheory/Localization/Integral.lean','Mathlib/RingTheory/IntegralClosure/Basic.lean','Mathlib/RingTheory/IntegralClosure/IsIntegral/Basic.lean']:
 f=R/'.lake/packages/mathlib'/p
 if f.is_file():
  arch='mathlib-'+p.replace('/','-')+'.txt';(D/arch).write_bytes(f.read_bytes());math.append(dict(path=p,archive=arch,sha256=sha(f),bytes=f.stat().st_size))
put('mathlib-inputs.json',math)
scratch=R/'.lake/roth-overview-session/GenWronskianChecks.lean';prefix='\n'.join(scratch.read_text().splitlines()[:15])+'\n';assert len(re.findall('^import ',prefix,re.M))==9
(D/'disk-prefix.lean.txt').write_text(prefix);(D/'isolated-prefix.lean.txt').write_bytes(Path('/private/tmp/roth-overview/current-isolated-prefix.lean.txt').read_bytes())
s=(R/'Roth/Main.lean').read_text();body=s[s.index('namespace Roth'):].replace('namespace Roth','namespace NatIntegral268Original\nopen Roth',1).replace('end Roth','end NatIntegral268Original');body=re.sub(r'\bexists_nat_mul_isIntegral\b','replay',body)
full='''
#check @Roth.exists_nat_mul_isIntegral
set_option pp.all true in
#print Roth.exists_nat_mul_isIntegral
#print axioms Roth.exists_nat_mul_isIntegral
#print axioms NatIntegral268Original.replay
example : @Roth.exists_nat_mul_isIntegral = @NatIntegral268Original.replay :=
  Subsingleton.elim _ _
run_cmd Lean.Elab.Command.liftTermElabM do
  let ci ← Lean.getConstInfo `Roth.exists_nat_mul_isIntegral
  Lean.logInfo m!"NAT268_BODY_CONSTANTS: {ci.value?.map (·.getUsedConstants.toList)}"
  Lean.logInfo m!"NAT268_TYPE_CONSTANTS: {ci.type.getUsedConstants.toList}"
  Lean.withOptions (fun o ↦ o.setBool `pp.funBinderTypes true) do
    Lean.logInfo m!"NAT268_FULL_TYPE: {← Lean.Meta.ppExpr ci.type}"
'''
names=[]
for d in order:
 if d['visibility']=='private':
  t='Lean.mkPrivateNameCore `'+d['file'][:-5].replace('/','.')+' `'+d['name']
  if len('    '+t+',')>100:t=t.replace(' `'+d['name'],'\n      `'+d['name'])
 else:t='`'+d['name']
 names.append('    '+t)
audit='''
namespace NatIntegral268Audit
run_cmd do
  let env ← Lean.getEnv
  let target := `Roth.exists_nat_mul_isIntegral
  let names : Array Lean.Name := #[
'''+',\n'.join(names)+''']
  unless names.size == 293 && names.toList.eraseDups.length == 293 do
    throwError "NAT268_BAD_CANONICAL_ARRAY"
  let mut present : Nat := 0
  let mut values : Nat := 0
  for n in names do
    match env.find? n with
    | none => throwError "NAT268_NOT_LOADED: {n}"
    | some ci =>
      present := present + 1
      if ci.type.getUsedConstants.any (fun c ↦ c == target) then
        Lean.logInfo m!"NAT268_DIRECT_TYPE_CONSUMER: {n}"
      match ci.value? (allowOpaque := true) with
      | none => pure ()
      | some val =>
        values := values + 1
        if val.getUsedConstants.any (fun c ↦ c == target) then
          Lean.logInfo m!"NAT268_DIRECT_CONSUMER: {n}"
  Lean.logInfo m!"NAT268_AUDIT: requested={names.size}; unique={names.toList.eraseDups.length}"
  Lean.logInfo m!"NAT268_AUDIT_PRESENT: present={present}; values={values}"
end NatIntegral268Audit
'''
whole=prefix+body+full+audit;assert max(map(len,whole.splitlines()))<=100
(D/'original-executed.lean.txt').write_text(whole);scratch.write_text(whole)
print('Prepared original full Main replay',len(whole.splitlines()),'lines; fresh17; exact293; nine imports')
