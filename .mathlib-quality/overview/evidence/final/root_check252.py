from pathlib import Path
import json
D=Path('/private/tmp/roth-overview/assess/Roth.le_index_of_forall_eval_eq_zero');R=Path('/Users/ramin/LEAN/Roth');p=(D/'disk-prefix.lean.txt').read_text();m=(R/'Roth/MainLemma.lean').read_text().split('namespace Roth\n',1)[1].rsplit('end Roth',1)[0]
assert(D/'original-executed.lean.txt').read_text().startswith(p+'namespace Cutoff252Original\nopen Roth\n'+m.replace('le_index_of_forall_eval_eq_zero','replay')+'\nend Cutoff252Original\n')
a=m.index('/-- Vanishing of box Hasse');b=m.index('/-- The bound `m(2m');mi=m[:a]+m[b:];a=mi.index('  exact le_index_of_forall_eval_eq_zero');b=mi.index('\nprivate lemma mul_card_filter_weight_le_aux',a)
body='''  have hn : map (Int.castRingHom ℝ) (W' - W'') ≠ 0 :=
    ((map_ne_zero_iff _ (MvPolynomial.map_injective _ Int.cast_injective)).2 hP.1)
  have hdP : ∀ j, degreeOf j (map (Int.castRingHom ℝ) (W' - W'')) ≤ r j := by
    simpa only [degreeOf,
      degrees_map_of_injective _ (f := Int.castRingHom ℝ) Int.cast_injective] using hP.2.1
  refine (le_index_iff hn).2 fun d he ↦ le_of_not_gt fun hw ↦ ?_
  have hd : ∀ j, d j ≤ r j := by
    intro j
    by_contra! hj
    exact he <| by rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hdP j).trans_lt hj), map_zero]
  exact he (eval_hasseDeriv_sub_eq_zero hfα (hWeq d (hJ d hd hw)))
'''
mi=mi[:a]+body+mi[b:];assert(D/'inline-executed.lean.txt').read_text().startswith(p+'namespace Cutoff252Inline\nopen Roth\n'+mi+'\nend Cutoff252Inline\n')
v=json.loads((D/'verification.json').read_text())
for e in v['accepted']:
 r=json.loads((D/e['receipt']).read_text());z=r['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False)
 print(e['label'],r['elapsed_ms'],'ms',len(ds),'messages',sum('depends on axioms'in x['message']for x in ds),'axiom prints')
print('PASS root exact full original and sole-caller inline reconstruction; eight native receipts inspected')
