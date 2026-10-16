# Index: compiled public-hypothesis proposal

Status: **awaiting scoped user decision; no source API change applied**.
This proposal concerns Index only; earlier approvals in CoeffNorm and GenWronskian
do not authorize it.

## 1. Remove unused decidable-equality binders

Remove `[DecidableEq σ]` from these17 public theorem signatures:

`index_le_weight`, `exists_weight_eq_index`, `le_index_iff`, `index_nonneg`,
`index_eq_zero_iff`, `index_hasseDeriv_ge`, `le_index_sum`,
`weight_eq_finsuppWeight_div`, `index_eq_weightedOrder_div`, `index_mul`,
`index_prod`, `index_neg`, `index_C_mul`, `index_mul_left_weights`,
`index_rename`, `index_le_card`, `index_unique`.

Also remove `[DecidableEq τ]` from `index_rename`. Its proof needs `classical`
for support-image manipulation. The other16 proofs compile without adding
classical reasoning to their bodies. The index definition already has no
decidable-equality binder and is unchanged.

This removes18 unnecessary public instance arguments. Ordinary theorem callers
continue to infer the remaining arguments. Fully explicit `@` applications change
arity; preserving the old types therefore requires the eta adapters verified below.

## 2. Remove unused positivity from index_le_card

Proposed signature:

```lean
theorem index_le_card {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ}
    (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) : index P α r ≤ Fintype.card σ
```

The weights may be zero: the existing totalized division convention makes their
contribution zero. The proof uses `weight_le_card`, which was previously
generalized in Box, and needs no positivity assumption.

Exactly two explicit project call sites need removal of the `hr` argument:
`Roth/Theta.lean` in `indexSet_bddAbove` (currently90) and `Θ_le_card` (currently113).
Keep both Theta public contracts unchanged. In particular, retain the existing
decidable-equality binder of `indexSet_bddAbove` with an `include` command if it
would otherwise disappear from automatic section-variable inclusion. Removing its
own positivity binder is outside this proposal and belongs to Theta's later audit.

## Compiled evidence

Isolated full source clone: `/private/tmp/roth-index-api-proposal.lean`.
It imports the existing project but declares its stronger results in
`Roth.IndexAPIProposal`; no tracked Lean source was changed.

Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-index-api-proposal.lean`,
session20355, exited0. Log:
`/private/tmp/roth-index-api-proposal-confirmed.log`.

The compiled clone independently reproves all17 stronger theorems from the original
proof bodies; only `index_rename` gains `classical`. It compiles both exact Theta
caller bodies with the removed argument and original caller types. All18 original
public Index type/value equalities are checked against explicit eta adapters;
both original Theta theorem types are also recovered by proof equality. All19
proposed theorem/caller constants have only `propext`, `Classical.choice`, and
`Quot.sound`. The compile has no errors or sorry axiom. Its only warning is the
deliberately retained unused Theta `hr` in the preserved caller contract.

If approved, apply only these removals and the two caller repairs, preserve
definitions/docs/names/conclusions/other hypotheses, and rerun complete module,
caller, original-type, standard-axiom, full-project and separate LeanEval gates.
The ongoing dedicated declaration audits can continue while a decision is pending.
