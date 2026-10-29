from pathlib import Path
import json
D=Path('/private/tmp/roth-overview/assess/Roth.exists_hasseDeriv_eval_ne_zero');R=Path('/Users/ramin/LEAN/Roth')
p=(D/'disk-prefix.lean.txt').read_text();m=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
assert (D/'original-executed.lean.txt').read_text().startswith(p+'namespace Witness254Original\nopen Roth\n'+m.replace('exists_hasseDeriv_eval_ne_zero','replay')+'\nend Witness254Original\n')
a=m.index('/-- If the index of `P ≠ 0`');b=m.index('private lemma abs_eval_iterated_hasseDeriv_lt_aux');s=m[:a]+m[b:]
s=s.replace('private lemma exists_hasseDeriv_index_eval_bound_aux','theorem caller_inline').replace('exists_hasseDeriv_index_eval_bound_aux','caller_inline')
a=s.index('  obtain ⟨k, hkw, hkev⟩ := exists_hasseDeriv_eval_ne_zero');b=s.index('  have hQev',a)
new='''  have hPN : map (Int.castRingHom ℝ) P ≠ 0 :=
    (map_ne_zero_iff _ (MvPolynomial.map_injective _ Int.cast_injective)).2 hP
  have hn : (taylor z (map (Int.castRingHom ℝ) P)).support.Nonempty := by simpa using hPN
  have hcut : (taylor z (map (Int.castRingHom ℝ) P)).support.inf' hn (weight r) < c := by
    rw [Finset.inf'_eq_csInf_image]
    exact hz
  obtain ⟨k, hk, hkw⟩ := (Finset.inf'_lt_iff hn).mp hcut
  have hkev : eval z (hasseDeriv k (map (Int.castRingHom ℝ) P)) ≠ 0 := by
    rwa [mem_support_iff, coeff_taylor] at hk
'''
s=s[:a]+new+s[b:]
assert 'exists_hasseDeriv_eval_ne_zero' not in s
assert(D/'inline-executed.lean.txt').read_text().startswith(p+'namespace Witness254Inline\nopen Roth\n'+s+'\nend Witness254Inline\n')
v=json.loads((D/'verification.json').read_text())
for e in v['accepted']:
 q=json.loads((D/e['receipt']).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)
 print(e['label'],q['elapsed_ms'],'ms',len(ds),'messages',sum('depends on axioms'in x['message']for x in ds),'axiom prints')
print('PASS root independent exact whole original and caller-inline reconstruction, full continuation, four clean receipts')
