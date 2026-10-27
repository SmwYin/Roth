---
decl: Roth.inv_add_inv_le
file: Roth/Lattice.lean
line: 40
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private pairing inequality 1/(λ-1+x) + 1/(λ+1-x) ≤ 2λ/(λ²-1) for 0 ≤ x ≤ 2, the per-pair step of the j/(r-j) pairing in sum_inv_le; a 4-line field_simp/nlinarith fact with no mathlib counterpart and one call site.
action: Keep as private helper for its single call site Roth.sum_inv_le (Roth/Lattice.lean:57); optionally weaken 2 < lam to 1 < lam (same proof, compiled in evidence/Roth.inv_add_inv_le/weaken.lean), not required since the caller has 2 < lam.
---

# Roth.inv_add_inv_le

## Inventory entry

### `theorem Roth.inv_add_inv_le`
- **Type**: `∀ {lam x : ℝ}, 2 < lam → 0 ≤ x → x ≤ 2 → (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1)`
- **What**: For real λ > 2 and 0 ≤ x ≤ 2, the sum of reciprocals 1/(λ - 1 + x) + 1/(λ + 1 - x) is at most 2λ/(λ² - 1). Writing a = λ - 1 + x and b = λ + 1 - x, one has a + b = 2λ and ab = λ² - (1 - x)² ≥ λ² - 1, so 1/a + 1/b = 2λ/(ab) ≤ 2λ/(λ² - 1); the extreme case is x ∈ {0, 2}. It is the bound on one pair (j, r - j) of terms in the harmonic-type sum of Lemma 8 (clean.tex §6), applied with x = 2j/r.
- **How**: Establishes positivity of both denominators by `linarith`, rewrites the left side with `inv_add_inv` and clears denominators with `div_le_div_iff₀` (positivity of λ² - 1 by `nlinarith`), and closes the polynomial inequality by `nlinarith [mul_nonneg hx0 (sub_nonneg.2 hx2)]`, i.e. from x(2 - x) ≥ 0.
- **Hypotheses**: `hlam : 2 < lam` (only `1 < lam` is used, verified in evidence); `hx0 : 0 ≤ x` and `hx2 : x ≤ 2` (both necessary: the statement fails at x = -1 and at x = 3 with λ = 3, verified in evidence).
- **Uses from project**: `[]`
- **Used by**: `Roth.sum_inv_le` (private, Roth/Lattice.lean:47; use at l.57 inside the `Finset.sum_le_sum` step, with x = 2j/r and 2 - x rewritten as 2(r - j)/r). `grep -rn inv_add_inv_le Roth/ Roth.lean` finds only l.40 and l.57. Transitively feeds `Roth.sum_inv_lt` (l.68) and Lemma 8.
- **Visibility**: private
- **Lines**: 40–45, proof length 4 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); no docstring. The name collides in spirit with mathlib's `inv_add_inv` (an equality), but being private in namespace `Roth` it causes no clash.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.sum_inv_le` (Roth/Lattice.lean:57), the pairing step of the proof that the harmonic-type sum is at most (r + 1)λ/(λ² - 1).
- Wrapper of 1–2 mathlib calls? No in the sense of a named lemma: it is `inv_add_inv` + `div_le_div_iff₀` + an `nlinarith` certificate (x(2 - x) ≥ 0). Short (4 lines) but not a pure alias.
- Does mathlib have it? No. `lean_loogle` on `(?a)⁻¹ + (?b)⁻¹ ≤ _` returns no results; `lean_leansearch` ("sum of reciprocals 1/a + 1/b with a + b fixed ... bound") returns only the equalities `inv_add_inv`, `inv_add_inv'`, `one_div_add_one_div`, `Commute.one_div_add_one_div` and `one_div_le_one_div_of_le`. A general convexity route (`ConvexOn` of `x ↦ x⁻¹` on `Ioi 0`) exists in mathlib but would be longer than the current proof.
- Too specific (inline?)? It is specific to the call site, but inlining it into the `Finset.sum_le_sum` lambda of `sum_inv_le` (already carrying a `simpa` rewrite of `2 - 2j/r`) would make that proof harder to read; the separate pair bound mirrors the source's "pairing the terms j and r - j" argument.
- Well-chosen statement? Yes for its purpose. The hypothesis `2 < lam` is stronger than needed (`1 < lam` suffices), but matches the caller's hypothesis, so no change is required.
- Conclusion: `KEEP`. Action: keep as private helper for `Roth.sum_inv_le`; optional cosmetic weakening of `2 < lam` to `1 < lam`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:40).

Even if made public it would not be a mathlib candidate: it is a one-off numeric inequality specialised to the parametrisation of Lemma 8, provable in 4 lines from `inv_add_inv`, `div_le_div_iff₀` and `nlinarith`.

## Evidence
- `grep -rn inv_add_inv_le Roth/ Roth.lean`: definition l.40, single use l.57.
- `lean_loogle "(?a)⁻¹ + (?b)⁻¹ ≤ _"`: no results.
- `lean_leansearch` (query above, 8 results): only the reciprocal-sum equalities `inv_add_inv`, `inv_add_inv'`, `one_div_add_one_div`, `Commute.one_div_add_one_div`, `one_div_mul_add_mul_one_div_eq_one_div_add_one_div`, plus `one_div_le_one_div_of_le` and unrelated Hölder-conjugate lemmas.
- Evidence file `.mathlib-quality/overview/evidence/Roth.inv_add_inv_le/weaken.lean` (imports `Mathlib.Analysis.Real.Sqrt` only), checked once with `lean_run_code`: compiles with no diagnostics. It shows (1) the statement with `1 < lam` in place of `2 < lam` holds with the identical proof; (2) `norm_num` refutes the statement at λ = 3, x = -1 and at λ = 3, x = 3, so both `0 ≤ x` and `x ≤ 2` are necessary.
