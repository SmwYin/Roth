# Index: compiled public-hypothesis proposal

Status: **groups1+2 explicitly approved by user via root/parent on2026-10-16;
application scheduled at each dedicated declaration checkpoint. Group3 remains
unapproved and unapplied.** See the application ledger below for current verified progress.
This proposal concerns Index only; earlier approvals in CoeffNorm and GenWronskian
were not reused as authorization.

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
Keep both Theta public contracts unchanged. A subsequent exact ambient-scope
compile confirms that both old decidable-equality binders remain automatically
included; no additional caller-scope command is needed. Removing Theta's own
positivity binders is outside this proposal and belongs to its later audit.

## 3. Remove unnecessary positive scaling factor

Further owner audit found that `index_mul_left_weights.hl : 0 < l` is also
unnecessary: Box's current `weight_mul_left` works for every natural `l`, and
the existing infimum-scaling proof only needs nonnegativity of its reciprocal.
The unchanged proof compiles after dropping `hl`, including the new `l = 0`
case under the existing totalized division/zero-index conventions.

Proposed signature (independent of decision1 about decidability):

```lean
theorem index_mul_left_weights {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ)
    (r : σ → ℕ) : index P α (fun j ↦ l * r j) = index P α r / l
```

Exactly two Theta rewrites (currently500/506) change
`rw [index_mul_left_weights hl0]` to `rw [index_mul_left_weights]`.
Their existing positive-scaling assumptions remain needed for later cancellation;
no Theta theorem statement changes. This is a separate scoped decision, not
authorization inferred from decisions1/2 or other-file approvals.

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

Ambient-scope follow-up: `/private/tmp/roth-index-api-proposal-caller-scope.lean`,
session35306 exit0, log of the same prefix. All original Index adapters and both
original Theta type equalities also pass with the original automatic section
instance inclusion. The resulting unused-section warning is deliberately retained.

Decision3 evidence: `/private/tmp/roth-index-scaling-proposal.lean`, actual
`lake env lean` session81861 exit0, `/private/tmp/roth-index-scaling-proposal.log`.
It independently proves the stronger scaling theorem from the original proof,
checks recovery of the original full public type by eta equality, and compiles
both exact Theta rewrite/cancellation subproofs with the removed argument.
The stronger theorem has only the three standard axioms. No source edit applied.

Apply only approved groups1+2 and corresponding caller repairs, preserve
definitions/docs/names/conclusions/other hypotheses, and rerun complete module,
caller, original-type, standard-axiom, full-project and separate LeanEval gates.
The dedicated declaration audits continue sequentially. Keep group3's `hl` unchanged
unless a separate explicit user approval arrives; the root has not included it in
the approved enumeration.

## Application ledger

Verified σ-DecidableEq omissions: 6/17.

- [index_le_weight](Index-index_le_weight.md)
- [exists_weight_eq_index](Index-exists_weight_eq_index.md)
- [le_index_iff](Index-le_index_iff.md)
- [index_nonneg](Index-index_nonneg.md)
- [index_eq_zero_iff](Index-index_eq_zero_iff.md)
- [index_hasseDeriv_ge](Index-index_hasseDeriv_ge.md)

Rename τ-DecidableEq removed: False.
index_le_card.hr removed: False.
Group3 scaling hl removed: False; scope requires separate approval.
