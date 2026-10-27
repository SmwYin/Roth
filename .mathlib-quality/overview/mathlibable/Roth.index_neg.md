---
decl: Roth.index_neg
file: Roth/Index.lean
line: 190
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Unused anywhere in the project (the source step "multiplication by a sign does not change the index" is formalised at Theta.lean:402-406 via index_C_mul with c = sign s), it is the c = -1 case of Roth.index_C_mul (compiled) and a one-line simp with support_neg; its mathlib analogue MvPowerSeries.weightedOrder_neg already exists; Step 8 REMOVE fires the Step 9a pre-filter.
action: Delete Roth.index_neg from Roth/Index.lean:189-192 (no call sites); if a negation lemma is wanted later, derive it from index_C_mul (c = -1) or, after a weightedOrder rebase of index, from MvPowerSeries.weightedOrder_neg.
---

# Roth.index_neg

## Inventory entry

### `theorem Roth.index_neg`
- **Type**: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (-P) α r = Roth.index P α r`
- **What**: The index of a real polynomial at `α` with weights `r` is unchanged when the polynomial is negated.
- **How**: `simp [index, support_neg]`: unfold `Roth.index` (an `sInf` of `weight r` over `(taylor α P).support`); `taylor α` is a ring hom so `taylor α (-P) = -taylor α P` (`map_neg`), and `MvPolynomial.support_neg` gives equal supports.
- **Hypotheses**: none beyond the section variable `[Fintype σ]`; no nonvanishing or positivity hypothesis is needed (both sides are `0` for `P = 0`).
- **Uses from project**: `Roth.index` (and implicitly `MvPolynomial.taylor` through its unfolding)
- **Used by**: unused in project (`grep -rnw index_neg Roth/` returns only the declaration at Roth/Index.lean:190)
- **Visibility**: public
- **Lines**: 189-192 (docstring 189, statement 190-191, proof 192), proof length 1 line
- **Notes**: Docstring cites §5, proof of Lemma 6 ("Multiplication by a sign does not change the index", clean.tex:825). In the formalisation of that step (Roth/Theta.lean:402-406, `sum_max_sub_le_index_det`) the sign is the integer cast `Equiv.Perm.sign s`, and the step is discharged with `Roth.index_C_mul`, not with `index_neg`.

## Junk check (Step 8)
- Used anywhere? No (project-wide grep; not listed in the module docstring's Main results).
- Wrapper of 1-2 mathlib calls? Yes: unfolding plus `map_neg` and `MvPolynomial.support_neg` in one `simp`.
- Does mathlib have it? Not for the project-only `Roth.index`; the mathlib counterpart for the weighted order is `MvPowerSeries.weightedOrder_neg` (Mathlib/RingTheory/MvPowerSeries/Order.lean:358, `@[simp]`), and `Roth.index_eq_weightedOrder_div` (assessed NO-composable-from-mathlib) transports it, as the Roth.index report's action already notes.
- Subsumed in project? Yes: it is the `c = -1` instance of `Roth.index_C_mul` (`rw [show -P = C (-1) * P by simp]; exact index_C_mul (by norm_num) P α r`, compiled).
- Too specific (inline)? No call site to inline into.
- Conclusion: `REMOVE` -- delete Roth/Index.lean:189-192. (If the authors want to keep it as source-cited API, it is harmless, cheap and correct; then KEEP with the same NO-composable classification as its siblings index_mul/index_prod.)

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: Step 8 said REMOVE (unused in the project, and the `c = -1` case of `Roth.index_C_mul`), so the Step 9a pre-filter fires.

Pre-filter details: not private; name does not end `_aux`; docstring does not start internal/auxiliary; qualified name `Roth.index_neg` is not in mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`). Not treated as INHERITED: although a one-line simp about the BORDERLINE parent `Roth.index`, the pre-filter applies first. Comparison with mathlib: `MvPowerSeries.weightedOrder_neg` is the canonical general form (any ring, any weights, no hypotheses); this statement adds nothing upstream.

## Evidence
- `grep -rnw index_neg Roth/`: only Roth/Index.lean:190.
- `grep -rn index_C_mul Roth/`: used at Roth/Theta.lean:405 for the source's sign step.
- `grep -rn weightedOrder_neg .lake/packages/mathlib/Mathlib/RingTheory/`: `MvPowerSeries.weightedOrder_neg` (Order.lean:358) and `MvPowerSeries.order_neg` (Order.lean:532).
- `grep -rn "namespace Roth" .lake/packages/mathlib/Mathlib/`: no hits.
- Evidence file `.mathlib-quality/overview/evidence/Roth.index_neg/subsumed.lean`: (1) derives the statement from `Roth.index_C_mul` with `c = -1`; (2) reproduces the project proof. Checked with `lean_run_code` (import Roth.Index): no errors, no warnings.
