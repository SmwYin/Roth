---
decl: Roth.sum_box_prod_pow_le_aux
file: Roth/CoeffNorm.lean
line: 214
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-use helper giving the last calc step of abs_eval_le, namely sum over box r of B times prod of |x j|^(k j) is at most B times prod of (1+|x j|)^(r j), via Finset.prod_univ_sum plus geom_sum_le_one_add_pow; no mathlib analogue.
action: Keep as private helper for its single call site Roth/CoeffNorm.lean:239 (abs_eval_le, final calc step); if abs_eval_le is ever upstreamed, carry it along (or inline it there).
---

# Roth.sum_box_prod_pow_le_aux

## Inventory entry

### `theorem Roth.sum_box_prod_pow_le_aux`
- **Type**: `∀ {σ : Type*} [Fintype σ] (r : σ → ℕ) {B : ℝ}, 0 ≤ B → ∀ (x : σ → ℝ), ∑ k ∈ box r, B * ∏ j, |x j| ^ k j ≤ B * ∏ j, (1 + |x j|) ^ r j` (stated under `open scoped Classical in`, so the `DecidableEq σ` needed by `box` is the classical instance).
- **What**: Summing `B · ∏_j |x_j|^{k_j}` over all multi-indices `k` with `0 ≤ k_j ≤ r_j` gives at most `B · ∏_j (1 + |x_j|)^{r_j}`: the box sum factors as `B · ∏_j ∑_{s ≤ r_j} |x_j|^s`, and each truncated geometric sum is at most `(1 + |x_j|)^{r_j}`.
- **How**: single `simpa [← Finset.mul_sum, box, Finset.prod_univ_sum] using mul_le_mul_of_nonneg_left (Finset.prod_le_prod₀ (s := Finset.univ) (fun _ _ ↦ by positivity) fun j _ ↦ geom_sum_le_one_add_pow (abs_nonneg (x j)) (r j)) hB`. The `simpa` unfolds `box` (a `Finset.map` of `Fintype.piFinset fun j ↦ range (r j + 1)` along `Finsupp.equivFunOnFinite.symm`), pulls `B` out with `Finset.mul_sum`, and rewrites `∏_j ∑_{s ∈ range (r j + 1)}` into the sum over `piFinset` with mathlib's `Finset.prod_univ_sum` (Mathlib/Algebra/BigOperators/Ring/Finset.lean:157); the bound comes from `Finset.prod_le_prod₀` applied to the project lemma `geom_sum_le_one_add_pow`.
- **Hypotheses**: `[Fintype σ]` (needed for `box` and the finite products); `0 ≤ B` (needed to multiply the inequality by `B`; without it the inequality flips). No redundant hypotheses.
- **Uses from project**: `Roth.box` (Roth/Box.lean:47), `Roth.geom_sum_le_one_add_pow` (Roth/CoeffNorm.lean:204).
- **Used by**: Roth/CoeffNorm.lean:239 `Roth.abs_eval_le` (last step of its calc) only; `grep -rn sum_box_prod_pow_le_aux Roth/` returns only the definition (l.214) and that use. Transitively everything downstream of `abs_eval_le`.
- **Visibility**: private
- **Lines**: 213–218 (including the `open scoped Classical in` line), proof length 4 lines
- **Notes**: Name ends in `_aux`. Mirrors the source's step "`∏_j ∑_{s ≤ r_j} |α|^s ≤ ∏_j (1 + |α|)^{r_j}`" in §6, proof of Lemma 9 (quoted in the docstring of `abs_eval_le`). The `open scoped Classical in` is there because `box` needs `DecidableEq σ`, which the file's `variable {σ : Type*}` does not provide; `abs_eval_le` uses the `classical` tactic, which supplies the same classical instance, so the call typechecks.

## Junk check (Step 8)
- Used anywhere? Yes, once: final calc step of the public `abs_eval_le` (Roth/CoeffNorm.lean:239).
- Wrapper of 1–2 mathlib calls? Not purely: it combines `Finset.prod_univ_sum` (mathlib), `Finset.prod_le_prod₀` (mathlib), `mul_le_mul_of_nonneg_left` (mathlib) and the project lemma `geom_sum_le_one_add_pow`, plus unfolding of the project def `box`. Short (4 lines) but not a trivial wrapper.
- Does mathlib have it? No. `box` is a project def, so mathlib cannot state this verbatim. `lean_leansearch` ("sum over a box of multi-indices of product of powers |x j|^k j is at most product of (1 + |x j|)^r j") returned `Behrend.sum_sq_le_of_mem_box`, `ZLattice.sum_piFinset_Icc_rpow_le`, `Finset.sum_pow'` and unrelated degree lemmas; none is this bound. `grep` of `.lake/packages/mathlib/Mathlib` for `box_prod_pow` / `sum_le_prod_one_add_pow` found nothing.
- Too specific / inline? It is specific to `abs_eval_le` and could be inlined into that calc step (the `classical` tactic there provides the same decidability instance). Keeping it separate keeps the calc of `abs_eval_le` three readable lines and isolates the `simpa` unfolding of `box`; it is already private. Inlining is an optional cosmetic change, not a quality gain.
- Well-chosen? Yes: statement is exactly the third calc step, hypotheses minimal (`0 ≤ B` is necessary).
- Conclusion: `KEEP`. Action: none; keep as private helper of `abs_eval_le`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private theorem` at Roth/CoeffNorm.lean:214; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent: if `abs_eval_le` is upstreamed, this helper (and `geom_sum_le_one_add_pow`, `Roth.box`) must come along, or the step can be re-proved inline via `Finset.prod_univ_sum` over `Fintype.piFinset`.

## Evidence
- `grep -rn sum_box_prod_pow_le_aux Roth/`: definition l.214, single use l.239.
- `grep` in Roth/Box.lean: `box` l.47 (defined as a `Finset.map` of `Fintype.piFinset fun j ↦ Finset.range (r j + 1)`), `mem_box` l.51.
- `grep` in mathlib: `Finset.prod_univ_sum` at Mathlib/Algebra/BigOperators/Ring/Finset.lean:157; no matches for `box_prod_pow` or `sum_le_prod_one_add_pow`.
- `lean_leansearch` (query above, 6 results): no matching mathlib lemma.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
