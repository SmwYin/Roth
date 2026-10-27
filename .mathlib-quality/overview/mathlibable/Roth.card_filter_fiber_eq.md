---
decl: Roth.card_filter_fiber_eq
file: Roth/Lattice.lean
line: 147
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 6-line helper rewriting the last-coordinate fibre count of the Lemma 8 weight filter as a weight filter in the first n coordinates with shifted parameter lam - 1 + 2i/r_last; single use in card_filter_weight_le_succ_aux, entirely about the project def weight, nothing to upstream.
action: Keep as private helper for its single use in Roth.card_filter_weight_le_succ_aux (Roth/Lattice.lean:176); optional polish only (state for an arbitrary finset, since box membership is unused), no upstream target.
---

# Roth.card_filter_fiber_eq

## Inventory entry

### `theorem Roth.card_filter_fiber_eq`
- **Type**: `∀ {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ), (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight r (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last n) i) ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) = (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight (r ∘ Fin.castSucc) d ≤ ((n : ℝ) - (lam - 1 + 2 * (i : ℝ) / r (Fin.last n))) / 2).card : ℝ)` (declared `private lemma`).
- **What**: In the inductive step of Lemma 8, the fibre of the filtered box over last coordinate `i` (a multi-index `d` in the first `n` coordinates, extended by `i` in the last) satisfies `weight_r(d, i) ≤ (n + 1 - λ)/2` iff `weight_{r∘castSucc}(d) ≤ (n - λ')/2` with `λ' = λ - 1 + 2i/r_{n+1}`; hence the two filtered cards (cast to ℝ) agree. This is the "reduce λ to λ' in one dimension lower" step of the paper's induction.
- **How**: `congr 2` reduces to equality of the filtered finsets; `Finset.filter_congr` reduces to pointwise equivalence of the predicates; `rw [Roth.weight_add, Roth.weight_mapDomain (Fin.castSucc_injective n), Roth.weight_single, mul_div_assoc]` turns the left weight into `weight (r ∘ Fin.castSucc) d + i / r (Fin.last n)`, and `grind` closes the resulting linear-arithmetic equivalence (including the `((n + 1 : ℕ) : ℝ)` cast).
- **Hypotheses**: none beyond the data `r`, `lam`, `i`. No positivity of `r (Fin.last n)` is needed (if it is `0`, both `i / 0` and `2 * i / 0` are `0` in Lean, and the identity still holds). The box-membership binder in `filter_congr` (`fun d _`) is unused, so the statement holds for any `Finset (Fin n →₀ ℕ)` in place of `box (r ∘ Fin.castSucc)`; the call site does not need this.
- **Uses from project**: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71), `Roth.weight_add` (Roth/Box.lean:85), `Roth.weight_mapDomain` (Roth/Box.lean:127), `Roth.weight_single` (Roth/Box.lean:96).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_weight_le_succ_aux` only (l.176, inside `Finset.sum_congr rfl fun i _ ↦ card_filter_fiber_eq r lam i` to rewrite each summand after `card_filter_box_last`). `grep -rn card_filter_fiber_eq Roth/` returns only the definition (l.147) and this use.
- **Visibility**: private
- **Lines**: 147–155, proof length 4 lines (152–155)
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, once, in `Roth.card_filter_weight_le_succ_aux` (l.176), which feeds the public Lemma 8 `Roth.card_filter_weight_le`.
- Wrapper of 1–2 mathlib calls? No: it is a short computation combining mathlib's `Finset.filter_congr` with three project lemmas about `Roth.weight` (`weight_add`, `weight_mapDomain`, `weight_single`) and `grind`.
- Does mathlib have it? No: `Roth.weight` is a project definition (`∑ j, (d j : ℝ) / r j`), so no mathlib statement can mention it. The generic ingredient (`Finset.filter_congr`, Mathlib/Data/Finset/Filter.lean) is already in mathlib.
- Too specific / inline? It is single-use and could in principle be inlined as a `fun i _ ↦ by congr 2; ...` argument to `Finset.sum_congr` at l.176, but the statement is long (two full filter expressions) and the named lemma keeps the already long `rw` chain of `card_filter_weight_le_succ_aux` readable; it also records exactly the parameter shift `λ ↦ λ - 1 + 2i/r_{n+1}` from the paper. Keeping it is the cleaner choice.
- Well-chosen? Yes; its statement matches the summands produced by `card_filter_box_last` (with `p := fun d ↦ weight r d ≤ ...`) after `Nat.cast_sum`, and its right side matches the form the induction hypothesis `ih` consumes. Optional polish: generalise from `box (r ∘ Fin.castSucc)` to an arbitrary finset, since membership is unused; not needed by the caller.
- Conclusion: `KEEP`. Action: none required; keep private next to `card_filter_weight_le_succ_aux`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:147). Independently, its content is a statement about the project-specific `Roth.weight` in the Lemma 8 induction, so there is nothing upstreamable.

## Evidence
- `grep -rn card_filter_fiber_eq Roth/`: definition l.147, single use l.176 (in `Roth.card_filter_weight_le_succ_aux`).
- Read Roth/Lattice.lean l.100–205 (`card_filter_box_fiber_aux`, `card_filter_box_last`, `filter_weight_le_eq_empty`, this lemma, `card_filter_weight_le_succ_aux`) and Roth/Box.lean (`box` l.47, `weight` l.71, `weight_add` l.85, `weight_single` l.96, `weight_mapDomain` l.127).
- Read the earlier report .mathlib-quality/overview/mathlibable/Roth.filter_weight_le_eq_empty.md for format consistency.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated. The claims that no positivity of `r (Fin.last n)` is needed and that box membership is unused are read off the statement (no such hypothesis exists) and the `fun d _` binder in the proof.
