from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
exec((D/'prepare_requests.py').read_text().split("req('original01'")[0])
old=Path('/private/tmp/roth-overview/assess/Roth.reduction/consumer-scope-executed.lean.txt').read_text()
# Only replace outside canonical inventory.
a,b=old.split('  let names : Array Lean.Name := #[',1);arr,c=b.split(']\n',1)
a=a.replace('Roth.reduction','Roth.exists_monic_aeval_eq_zero');c=c.replace('RED271','MONIC272')
s=a+'  let names : Array Lean.Name := #['+arr+']\n'+c
(D/'consumer-scope-executed.lean.txt').write_text(s)
req('consumer-scope01','diagnostics','consumer-scope-executed.lean.txt','consumer-scope-receipt.json',dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45),original_audit=True)
meta=json.load(open('/private/tmp/roth-overview/review/corrected-manifest.json'))
def src(n):return next(x['source']for x in meta if x['name']==n)
main=(D/'source-Main.lean.txt').read_text()
start=main.index('private lemma exists_roth_parameters_aux');end=main.index('\n-- Choose reduced approximants',start)
caller=main[start:end].replace('private lemma','theorem',1)
(D/'caller-original.lean.txt').write_text(main[start:end]+'\n')
t=src('Roth.exists_monic_aeval_eq_zero')
inline=caller.replace('  obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint',
'''  obtain ⟨p, hp, hp0⟩ := hint
  let f := p * Polynomial.X ^ 2
  have hf : f.Monic := hp.mul (Polynomial.monic_X_pow 2)
  have hfα : Polynomial.aeval α f = 0 := by
    rw [map_mul, Polynomial.aeval_def, hp0, zero_mul]
  have hdeg : 2 ≤ f.natDegree := by simp [f, hp.ne_zero]''')
# Reproduce unrelated private dependencies as exact-source copies. This avoids opaque private aliases.
ns='namespace Monic272Inline\nopen Roth\n'
s=(D/'disk-prefix.lean.txt').read_text()+ns+inline+'\n'
for name,nextmarker in [('exists_roth_approximants_aux','-- Compare the nonzero'),('one_lt_roth_eval_bound_aux','-- Bound the common'),('roth_product_bound_aux','-- Compare logarithms'),('roth_log_bound_aux',"/-- Roth's theorem for irrational")]:
 a=main.index('private lemma '+name);b=main.index(nextmarker,a)
 s+=main[a:b].replace('private lemma','theorem',1)+'\n'
for n in ['Roth.roth_of_isIntegral','Roth.roth','Roth.roth_rat']:s+=src(n)+'\n'
s+='''#print axioms exists_roth_parameters_aux
#print axioms roth_of_isIntegral
#print axioms roth_rat
end Monic272Inline
example : @Roth.roth_of_isIntegral = @Monic272Inline.roth_of_isIntegral := Subsingleton.elim _ _
example : @Roth.roth_rat = @Monic272Inline.roth_rat := Subsingleton.elim _ _
run_cmd do
  let env ← Lean.getEnv
  for n in #[`Monic272Inline.exists_roth_parameters_aux, `Monic272Inline.roth_of_isIntegral,
      `Monic272Inline.roth, `Monic272Inline.roth_rat] do
    let mut todo := [n]
    let mut seen : List Lean.Name := []
    while !todo.isEmpty do
      let k := todo.head!
      todo := todo.tail!
      unless seen.contains k do
        seen := k :: seen
        if k == `Roth.exists_monic_aeval_eq_zero || k == `Roth.roth_of_isIntegral ||
            k == `Roth.roth || k == `Roth.roth_rat then
          throwError "MONIC272_CIRCULAR: {n} reaches {k}"
        if k.toString.startsWith "Roth." || k.toString.startsWith "_private.Roth." ||
            k.toString.startsWith "Monic272Inline." then
          if let some ci := env.find? k then
            if let some v := ci.value? (allowOpaque := true) then
              todo := v.getUsedConstants.toList ++ todo
    Lean.logInfo m!"MONIC272_NONCIRCULAR: {n}; checked={seen.length}"
'''
(D/'caller-executed.lean.txt').write_text(s)
req('caller01','diagnostics','caller-executed.lean.txt','caller-receipt.json',dict(file_path='.lake/roth-overview-session/GenWronskianChecks.lean',timeout_s=45))
# Existing-only automation/normalization composition probe, before any scratch same-result lemma.
s=(D/'isolated-prefix.lean.txt').read_text()+'''#check_failure Roth.exists_monic_aeval_eq_zero
namespace Monic272Composition
open Polynomial
example {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : Polynomial ℤ, f.Monic ∧ aeval α f = 0 ∧ 2 ≤ f.natDegree := by
  fail_if_success solve | exact?
  fail_if_success solve | simp [IsIntegral, RingHom.IsIntegralElem]
  obtain ⟨f, hf, hf0⟩ := hint
  refine ⟨f * X ^ 2, hf.mul (monic_X_pow 2), ?_, ?_⟩
  · rw [map_mul, aeval_def, hf0, zero_mul]
  · simp [hf.ne_zero]
end Monic272Composition
'''
(D/'composition-executed.lean.txt').write_text(s)
req('composition01','run_code','composition-executed.lean.txt','composition-receipt.json')
print('scope and actual fullcaller plus transitive replays prepared')
