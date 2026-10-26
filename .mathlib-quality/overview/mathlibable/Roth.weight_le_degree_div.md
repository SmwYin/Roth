---
decl: Roth.weight_le_degree_div
file: Roth/Box.lean
line: 118
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Unused anywhere in the project (the Lemma 6 proof uses the private real-ratio variant Theta.lean weight_le_delta_aux instead), and its content is a single gcongr after Finsupp.degree_eq_sum and Finset.sum_div; Step 8 REMOVE fires the Step 9a pre-filter.
action: Delete Roth.weight_le_degree_div from Roth/Box.lean:113-122 (no call sites to update); optionally, instead generalise it to a real lower bound 0 < c ≤ r j and reprove Roth/Theta.lean weight_le_delta_aux from it, in which case it would be KEEP.
---

# Roth.weight_le_degree_div

## Inventory entry

### `theorem Roth.weight_le_degree_div`
- **Type**: `{σ : Type*} [Fintype σ] {r : σ → ℕ} {m : ℕ} (hm : 0 < m) (hr : ∀ j, m ≤ r j) (d : σ →₀ ℕ) : Roth.weight r d ≤ ↑d.degree / ↑m`
- **What**: If every parameter `r j` is at least a positive natural `m`, then the weight `∑ j, d j / r j` of a multi-index `d` is at most its total degree divided by `m`.
- **How**: `rw [weight, Finsupp.degree_eq_sum, Nat.cast_sum, Finset.sum_div]` turns the goal into `∑ j, d j / r j ≤ ∑ j, d j / m`, closed by `gcongr with j` (termwise `div_le_div_of_nonneg_left`, positivity side goals discharged from `hm`) and `exact hr j`.
- **Hypotheses**: `hm : 0 < m` (needed so `d j / m` dominates `d j / r j`; with `m = 0` the RHS is `0`), `hr : ∀ j, m ≤ r j`; section variable `[Fintype σ]` (the `[DecidableEq σ]` section variable was omitted earlier in the file).
- **Uses from project**: `Roth.weight`
- **Used by**: unused in project (`grep -rn weight_le_degree_div Roth/ Roth.lean` returns only the declaration at Roth/Box.lean:118).
- **Visibility**: public
- **Lines**: 113–122 (docstring 113–117, statement 118–119, proof 120–122), proof length 3 lines
- **Notes**: Docstring cites §5, proof of Lemma 6 ("`∑_{j<p} i_j / r_j ≤ w / r_{p-1}`"). The formalised Lemma 6 (Roth/Theta.lean, `sum_max_sub_le_index_det` and its callers) instead uses the private helper `weight_le_delta_aux` (Roth/Theta.lean, ~l.493), which re-derives a closely related bound `weight (r ∘ some) d ≤ δ` from a real-ratio hypothesis `r none ≤ δ * r (some j)` and `d.degree ≤ r none`; that form is not an instance of `weight_le_degree_div` (the cleanup audit `.mathlib-quality/cleanup/Theta-index_le_lem6.md` already noted the lemma "requires a common NAT denominator lower bound; cannot directly express scaled ratio with arbitrary real δ").

## Junk check (Step 8)
- Used anywhere? No. Zero references outside its own declaration (project-wide grep), not listed in the Box.lean module docstring's Main results.
- Wrapper of 1–2 mathlib calls? Yes: `Finsupp.degree_eq_sum` + `Finset.sum_div` + one `gcongr` step.
- Does mathlib have it? Not for `Roth.weight`. Re-aimed at `Finsupp.weight` (parent `Roth.weight` is `NO-mathlib-has-it` = `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`): the analogue would be `Finsupp.weight w d ≤ d.degree • c` under `∀ i, w i ≤ c`; the theorem list of Mathlib/Data/Finsupp/Weight.lean (`weight_apply`, `weight_single*`, `weight_eq_sum`, `le_weight*`, `weight_eq_zero_iff_eq_zero`, `finite_of_nat_weight_*`, `degree_*`, `le_degree`, `degree_eq_weight_one`, `degree_mono`, ...) has no such upper bound. It would be `Finset.sum_le_sum` after `weight_eq_sum`/`degree_eq_sum`, i.e. composable, and is not needed by the project.
- Too specific (inline)? There is nothing to inline: no call site.
- Well-chosen? The natural-number lower bound `m` is the wrong shape for the one place the paper's estimate is actually formalised (Theta.lean needs a real ratio `δ`), which is why it went unused.
- Conclusion: `REMOVE` — action: delete Roth/Box.lean:113–122. (Alternative if the authors prefer to keep it: generalise `m : ℕ` to `c : ℝ` with `0 < c` and `∀ j, c ≤ r j`, and reprove `weight_le_delta_aux` from it — then it would be KEEP; this alternative is not verified here.)

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: Step 8 said REMOVE (unused anywhere in the project; a one-`gcongr` consequence of `Finsupp.degree_eq_sum` and `Finset.sum_div`), so the Step 9a pre-filter fires.

Pre-filter details: not private; name does not end `_aux`; docstring does not start internal/auxiliary; qualified name `Roth.weight_le_degree_div` not in mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`). Re-aim note for the parent refactor: if `Roth.weight` is redefined via `Finsupp.weight` (see Roth.weight.md), mathlib has no `Finsupp.weight w d ≤ d.degree • c` lemma, but the project does not need one; no upstreaming action.

## Evidence
- `grep -rn "weight_le_degree\|le_degree_div" Roth/ Roth.lean`: only Roth/Box.lean:118 (declaration).
- `grep -n "theorem\|lemma\|def " .lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean`: no upper bound of `weight` by `degree`.
- Read Roth/Theta.lean (`sum_max_sub_le_index_det`, private `weight_le_delta_aux`) to confirm the paper's Lemma 6 estimate is formalised there in a real-ratio form that does not use this lemma.
- `git log -S weight_le_degree_div`: introduced/simplified in Box cleanup commits (8268ad8 "Simplify the weight bound by total degree"); the Lemma 6 cleanup audit (6ac4373, `.mathlib-quality/cleanup/Theta-index_le_lem6.md`) considered and rejected it for Theta.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a REMOVE/SKIP; the project builds clean so the lemma compiles as stated).
