---
decl: Roth.sum_inv_le
file: Roth/Lattice.lean
line: 47
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private pairing bound sum_{j=0}^r (λ-1+2j/r)⁻¹ ≤ (r+1)λ/(λ²-1), the first calc step of Roth.sum_inv_lt (Lemma 8); specialised to Lemma 8's parametrisation, no mathlib counterpart, one call site.
action: Keep as private helper for its single call site Roth.sum_inv_lt (Roth/Lattice.lean:83); optional polish: use Finset.sum_flip instead of sum_range_reflect to drop the r+1-1-j rewrite, and 2 < lam may be weakened to 1 < lam (compiled in evidence/Roth.sum_inv_le/weaken.lean), not required.
---

# Roth.sum_inv_le

## Inventory entry

### `theorem Roth.sum_inv_le`
- **Type**: `∀ {r : ℕ}, 1 ≤ r → ∀ {lam : ℝ}, 2 < lam → ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ ≤ (r + 1) * (lam / (lam ^ 2 - 1))`
- **What**: For an integer r ≥ 1 and real λ > 2, the harmonic-type sum ∑_{j=0}^r 1/(λ - 1 + 2j/r) is at most (r + 1)·λ/(λ² - 1). Proof idea (source §6, Lemma 8): pair the term j with the term r - j; each pair is bounded by 2λ/(λ² - 1), so twice the sum is at most 2(r + 1)λ/(λ² - 1).
- **How**: Applies `Finset.sum_le_sum` termwise to the bound `inv_add_inv_le` (with x = 2j/r, after rewriting 2 - 2j/r as 2(r - j)/r via `Nat.add_sub_cancel`, `Nat.cast_sub`, `field_simp`; x ≤ 2 by `div_le_iff₀` + `gcongr`), giving ∑ (f j + f (r - j)) ≤ ∑ 2λ/(λ² - 1). Then rewrites with `Finset.sum_add_distrib`, `Finset.sum_range_reflect` (so the reflected sum equals the original), `Finset.sum_const`, `card_range`, `nsmul_eq_mul`, `mul_div_assoc`, normalises casts by `push_cast`, and closes with `linarith`.
- **Hypotheses**: `hr : 1 ≤ r` (necessary: at r = 0, λ = 3 the left side is 1/2 and the right side 3/8, refuted by `norm_num` in evidence); `hlam : 2 < lam` (only `1 < lam` is used, verified in evidence by recompiling with the helper weakened the same way).
- **Uses from project**: `Roth.inv_add_inv_le` (private, Roth/Lattice.lean:40)
- **Used by**: `Roth.sum_inv_lt` (Roth/Lattice.lean:68, first `calc` step at l.83). `grep -rn sum_inv_le Roth/` finds only l.47 and l.83. Transitively feeds Lemma 8 (lattice count estimate).
- **Visibility**: private
- **Lines**: 47–61, proof length 13 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); no docstring (the public `sum_inv_lt` carries the source citation). `Finset.sum_flip` (`∑ r ∈ range (n+1), f (n - r) = ∑ k ∈ range (n+1), f k`) matches the indexing better than `sum_range_reflect` and would let the `r + 1 - 1 - j` rewrite be simplified to `r - j`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.sum_inv_lt` (Roth/Lattice.lean:83).
- Wrapper of 1–2 mathlib calls? No: a 13-line argument combining `Finset.sum_le_sum`, the project helper `inv_add_inv_le`, a reflection of the sum and arithmetic normalisation.
- Does mathlib have it? No. `lean_leansearch` ("sum over range of reciprocals bounded by pairing terms j and n - j ... harmonic sum upper bound") returns only the reindexing lemmas `Finset.sum_range_reflect`, `Finset.sum_flip`, `Finset.sum_Ico_reflect` and harmonic-number bounds (`harmonic_le_one_add_log`), none of which is this bound. The statement is specific to Lemma 8's parametrisation.
- Too specific (inline?)? It is specific, but inlining 13 lines into the first `calc` step of `sum_inv_lt` (which already has its own algebraic setup) would hurt readability; the separation mirrors the source's two-stage argument (pairing bound, then comparison with √(1 - 1/m)).
- Well-chosen statement? Yes. `2 < lam` is stronger than needed (`1 < lam` suffices) but matches the caller, which derives `2 < lam` from `2√m < lam`.
- Conclusion: `KEEP`. Action: keep as private helper for `Roth.sum_inv_lt`; optional polish via `Finset.sum_flip`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:47).

Even if made public it would not be a mathlib candidate: it is a one-off numeric estimate tailored to the sum appearing in the lattice-count Lemma 8, with no standard literature form.

## Evidence
- `grep -rn sum_inv_le Roth/`: definition l.47, single use l.83 (in `Roth.sum_inv_lt`).
- `lean_leansearch` (query above, 6 results): `Finset.sum_Ico_reflect`, `harmonic_eq_sum_Icc`, `harmonic_le_one_add_log`, `Finset.sum_range_reflect`, `Complex.sum_div_factorial_le`, `Finset.sum_flip`; no counterpart.
- Evidence file `.mathlib-quality/overview/evidence/Roth.sum_inv_le/weaken.lean` (imports `Mathlib.Algebra.BigOperators.Fin`, `Mathlib.Analysis.Real.Sqrt` only), checked once with `lean_diagnostic_messages`: compiles, only a header-linter style warning. It shows (1) the statement with `1 < lam` holds with the identical proof, using the helper `inv_add_inv_le` weakened to `1 < lam`; (2) `norm_num` refutes the statement at r = 0, λ = 3, so `1 ≤ r` is necessary.
