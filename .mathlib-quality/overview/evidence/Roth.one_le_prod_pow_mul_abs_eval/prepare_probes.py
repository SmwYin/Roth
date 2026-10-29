from pathlib import Path
import json,hashlib
D=Path('/private/tmp/roth-overview/assess/Roth.one_le_prod_pow_mul_abs_eval');R=Path('/Users/ramin/LEAN/Roth')
def write(n,s): (D/n).write_text(s)
def req(id,source,op='run_code'):
 p=D/source
 x=dict(id=id,operation=op,source=source,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=id+'-receipt.json',arguments={} if op=='run_code' else dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
 write('root-requests/'+id+'.json',json.dumps(x,indent=2)+'\n')
s=(D/'target-excerpt.lean.txt').read_text()
g=s.replace('theorem one_le_prod_pow_mul_abs_eval {m : ℕ}', 'theorem generic {ι K : Type*} [Fintype ι] [Field K] [LinearOrder K]\n    [IsStrictOrderedRing K]').replace('Fin m','ι').replace('ℝ','K')
write('generic-body.lean.txt',g)
prefix=(D/'isolated-prefix.lean.txt').read_text()+'\nopen MvPolynomial\n#check_failure Roth.one_le_prod_pow_mul_abs_eval\nnamespace Integer279\n'
write('generic-executed.lean.txt',prefix+g+'\n#print axioms generic\nend Integer279\n');req('generic01','generic-executed.lean.txt')
# Signed denominator variation of same proof; absolute product is necessary.
gs=g.replace('theorem generic','theorem signed').replace('{q : ι → ℕ} (hq : ∀ j, 0 < q j)','{q : ι → ℤ} (hq : ∀ j, q j ≠ 0)')
gs=gs.replace('1 ≤ (∏ j, (q j : K) ^ r j) *','1 ≤ |∏ j, (q j : K) ^ r j| *',1)
gs=gs.replace('have hqR : ∀ j, (0 : K) < q j := fun j ↦ by exact_mod_cast hq j','have hqR : ∀ j, (q j : K) ≠ 0 := fun j ↦ by exact_mod_cast hq j')
gs=gs.replace('have hP : (0 : K) < ∏ j, (q j : K) ^ r j := Finset.prod_pos fun j _ ↦ pow_pos (hqR j) _','have hP : (∏ j, (q j : K) ^ r j) ≠ 0 :=\n    Finset.prod_ne_zero_iff.mpr fun j _ ↦ pow_ne_zero _ (hqR j)')
gs=gs.replace('(hqR j).ne\'','(hqR j)').replace("hP.ne'","hP").replace('abs_mul, abs_of_pos hP','abs_mul')
write('signed-body.lean.txt',gs);write('signed-executed.lean.txt',prefix+gs+'\n#print axioms signed\nend Integer279\n');req('signed01','signed-executed.lean.txt')
# Exact recovery of original signature from new generalized theorem.
rs=s[:s.index(':= by')]+':= by\n  exact Integer279.generic Q hQ h hq hne\n'
rs=rs.replace('theorem one_le_prod_pow_mul_abs_eval','theorem recovery')
write('recovery-executed.lean.txt',prefix+g+'\n'+rs+'\n#print axioms recovery\nend Integer279\n');req('recovery01','recovery-executed.lean.txt')
# Full original Main proof audit with callsite proof literally inlined.
main=(R/'Roth/Main.lean').read_text();main=main[main.index('namespace Roth'):].replace('namespace Roth','namespace Integer279Full\nopen Roth',1).replace('end Roth','end Integer279Full')
# Delete local target so inlined caller cannot accidentally resolve local copy.
main=main.replace(s.strip(),'')
body=s[s.index(':= by')+len(':= by'):].strip('\n')
body=body.replace('hQ j','hQd j').replace('hq j','hq0 j')
call='(one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne)'
typ='1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)|'
replacement='(show '+typ+' from by\n'+ '\n'.join('  '+l for l in body.splitlines())+')'
assert main.count(call)==1
main=main.replace(call,replacement)
# Existing public project target absent from every proof lexical occurrence after deletion/inlining.
write('callers-executed.lean.txt',(D/'disk-prefix.lean.txt').read_text()+'\n'+main+'\n#print axioms Integer279Full.roth_rat\n')
req('callers01','callers-executed.lean.txt','diagnostics')
# Pinned candidates and targeted composition failures, not absence proofs.
comp=prefix+'''#check one_le_pow_mul_abs_eval_div
#check denomsClearable_of_natDegree_le
#check denomsClearable_natDegree
#check Int.one_le_abs
#check MvPolynomial.eval_eq'
#check MvPolynomial.monomial_le_degreeOf
#check MvPolynomial.isLocalization
'''
negative=s.replace('theorem one_le_prod_pow_mul_abs_eval','theorem compositionProbe')
negative=negative[:negative.index(':= by')]+''':= by
  fail_if_success
    exact one_le_pow_mul_abs_eval_div (by positivity) hne
  fail_if_success
    exact Int.one_le_abs hne
  fail_if_success
    simp only [eval_map]
  exact generic Q hQ h hq hne
'''
write('composition-executed.lean.txt',comp+g+'\n'+negative+'\n#print axioms compositionProbe\nend Integer279\n');req('composition01','composition-executed.lean.txt')
print('Prepared generic/signed/recovery/fullMain inline/candidates composition sources')
