# Theta: concrete unused-contract candidate (unapplied)

Live source remains at its existing public contracts. This is a menu for an explicit decision,
not authorization to apply any row. Dedicated original-declaration audits remain mandatory;
none is counted from this exploratory whole-file compiler probe.

A full independent copy of current Theta was compiled in namespace ThetaContractCandidate,
using Roth's existing Index/Separation APIs and original mathematical proofs. Only the menu
below, corresponding routine internal call arguments, and scoped classical proof instances
changed. Candidate file `/private/tmp/roth-theta-contract-candidate.lean`; actual command
`lake env lean /private/tmp/roth-theta-contract-candidate.lean` exited0. Successful log:
`/private/tmp/roth-theta-contract-candidate-fixed.log`. The earlier first draft failed solely
because omit was placed between a docstring and theorem; its failed log is not pass evidence.
No profiling/performance claim follows from this ordinary compiler result.

## A. Remove unused decidable-equality instance binders

| Public theorem | Proposed instance removal |
|---|---|
| one_mem_RSet | DecidableEq σ |
| indexSet_nonempty | DecidableEq σ |
| indexSet_bddAbove | DecidableEq σ |
| index_le_Θ | DecidableEq σ |
| Θ_nonneg | DecidableEq σ |
| Θ_le_card | DecidableEq σ |
| Θ_le_of_forall_index_le | DecidableEq σ |
| Θ_mono | DecidableEq σ |
| Θ_equiv | DecidableEq σ and DecidableEq τ |
| Θ_unique_le | DecidableEq σ |
| sum_max_sub_le_index_det | DecidableEq τ |
| index_det_le | DecidableEq τ |
| index_le_lem6 | DecidableEq τ |
| Θ_option_le | DecidableEq τ |

Fourteen public theorems,fifteen instance binders. Where necessary,classical decidability is
selected inside proofs. No definition/signature of RSet,indexSet,Θ,lem6M or lem6Φ is changed.
Fintype remains everywhere except the single B row below. The private renaming helper's
corresponding decidability removals in the exploratory copy are routine internal changes;
its own dedicated audit must still check them separately before live application.

## B. Remove unused Fintype from one_mem_RSet

The constant polynomial1 meets all coordinate degree/coefficient bounds without requiring
finitely many variables. The same proof compiles with arbitrary σ and classical decidability.
No other public Fintype removal is proposed here.

## C. Remove explicit unused hypotheses

| Public theorem | Proposed removal | Resulting mathematical statement |
|---|---|---|
| indexSet_bddAbove | hr : ∀j,0<r j | Its defining indices are bounded above for arbitrary natural weights. |
| Θ_le_card | hr : ∀j,0<r j | The supremum bound by card σ holds for arbitrary natural weights,still1≤B. |
| exists_eq_pow_mul_of_rootMultiplicity | hR : R≠0 | The integer factorization also holds for the zero polynomial. |
| sum_max_sub_le_index_det | hR : R≠0 | The retained nonzero determinant hypothesis supplies the nonvanishing needed by the proof. |
| index_det_le | hl' : l≤r none+1; hδ : 0<δ; consequently the unused implicit δ parameter | This factorized-determinant upper bound does not require those restrictions;1≤l,positive weights and every factor/degree/coefficient hypothesis remain. |
| index_le_lem6 | hq : ∀j,0<q j | The polynomial bound's proof works without this separate denominator positivity assumption. |
| Θ_option_le | hq : ∀j,0<q j | The supremum bound's proof works without this separate denominator positivity assumption. |

The r parameters remain implicit where originally implicit. No argument reordering,no conclusion
change,no weaker result,new axiom,sorry,resource-limit raise or live edit was used. These are
strictly scoped options; approving one row/group does not authorize unrelated widenings.
The coefficient domain remains integers,with real indices/bounds and natural weights/denominators.
The q-positivity rows deserve an explicit choice because the paper states positive denominators;
the compiled extension is valid under the existing division-by-zero/index conventions.

Removing the first two C restrictions exposes further unused hr parameters in index_le_Θ and
Θ_mono in the candidate. Those remain deliberately intact and are not included in this menu;
any further removal needs its own concrete scoped audit/decision. Likewise no general Ring,
non-finite index theory,new companion API,renaming or module restructuring is proposed here.

Status: UNAPPLIED,awaiting explicit root/user decision. Routine authorized proof/style work can
continue with the existing public contracts. Each selected amendment will be independently
verified and published at its declaration checkpoint; this preview does not replace those gates.
