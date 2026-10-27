---
decl: Roth.floor_rpow_count_lt_aux
file: Roth/MainLemma.lean
line: 320
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-use real inequality 2⌊x^c⌋+1 < (x+1)^(2c) for x>0, c≥1, the per-factor bound inside pigeonhole_count; proved via Real.add_rpow_le_rpow_add, Real.rpow_mul and nlinarith; too specific for mathlib, which has no such lemma.
action: Keep as private helper for its single call site Roth/MainLemma.lean:343 (pigeonhole_count, first calc step); no change.
---

# Roth.floor_rpow_count_lt_aux

## Inventory entry

### `theorem Roth.floor_rpow_count_lt_aux`
- **Type**: `∀ {x c : ℝ}, 0 < x → 1 ≤ c → ((2 * ⌊x ^ c⌋₊ + 1 : ℕ) : ℝ) < (x + 1) ^ (2 * c)`
- **What**: For real x > 0 and real exponent c ≥ 1, the number 2⌊x^c⌋ + 1 (the count of integers in [-⌊x^c⌋, ⌊x^c⌋]) is strictly less than (x + 1)^(2c).
- **How**: Set u = x^c > 0 (`Real.rpow_pos_of_pos`). Superadditivity of t ↦ t^c for c ≥ 1 (`Real.add_rpow_le_rpow_add`, Mathlib/Analysis/MeanInequalitiesPow.lean:190, with a = x, b = 1) gives u + 1 ≤ (x+1)^c. Rewrite (x+1)^(2c) = ((x+1)^c)^2 via `mul_comm`, `Real.rpow_mul` and `Real.rpow_two`; `push_cast`; then `nlinarith only` with `pow_le_pow_left₀` (squaring the superadditivity bound), `sq_pos_of_pos hu` and `Nat.floor_le`: 2⌊u⌋+1 ≤ 2u+1 < u^2+2u+1 = (u+1)^2 ≤ ((x+1)^c)^2.
- **Hypotheses**: `0 < x` (needed: at x = 0 the claim reads 1 < 1); `1 ≤ c` (needed: at c = 0 the claim reads 3 < 1, and superadditivity of t^c fails for c < 1).
- **Uses from project**: `[]` (only mathlib lemmas: `Real.rpow_pos_of_pos`, `Real.add_rpow_le_rpow_add`, `Real.rpow_mul`, `Real.rpow_two`, `pow_le_pow_left₀`, `sq_pos_of_pos`, `Nat.floor_le`).
- **Used by**: Roth/MainLemma.lean:343 `Roth.pigeonhole_count` (first `calc` step, via `pow_lt_pow_left₀`) only; `grep -rn floor_rpow_count_lt_aux Roth/` gives the definition (l.320) and that use. Transitively `pigeonhole_count` is used at Roth/MainLemma.lean:615 (Lemma 9 construction).
- **Visibility**: private
- **Lines**: 320–327, proof length 6 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). Name ends in `_aux`. Replaces the source's intermediate estimate `1 + 2B_1^c < [2(1+B_1)]^c` (§6, proof of Lemma 9) with a direct bound by (B+1)^(2c), as the comment in `pigeonhole_count` (l.336–338) explains.

## Junk check (Step 8)
- Used anywhere? Yes, once: `pigeonhole_count` (Roth/MainLemma.lean:343), which feeds Lemma 9 (l.615).
- Wrapper of 1–2 mathlib calls? No. It combines superadditivity of rpow, an rpow exponent rewrite and a nonlinear arithmetic step with the floor bound.
- Does mathlib have it? No. `lean_leansearch` ("2 * floor (x ^ c) + 1 < (x + 1) ^ (2 * c) for real x positive and c at least 1") returned only generic floor facts (`Nat.lt_floor_add_one`, `Int.lt_floor_add_one`, `Int.div_two_lt_floor`, `mul_pow_le_nat_floor_pow`) and `Int.self_le_zpow_clog`; none is this inequality. The key ingredient `Real.add_rpow_le_rpow_add` is in mathlib and already used.
- Too specific / inline? It is a very specific numeric inequality, but inlining it into the `calc` of `pigeonhole_count` would put a 6-line nonlinear argument inside a calc step and hurt readability; as a named private helper it is appropriate.
- Well-chosen? Yes; the statement is exactly the per-factor bound needed, with minimal hypotheses (both are necessary, see Hypotheses).
- Conclusion: `KEEP`. Action: keep as private helper of `pigeonhole_count`; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:320; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

## Evidence
- `grep -rn floor_rpow_count_lt_aux Roth/`: definition l.320, single use l.343 (`pigeonhole_count`); `pigeonhole_count` used at l.615.
- `grep -n add_rpow_le_rpow_add .lake/packages/mathlib/Mathlib/Analysis/MeanInequalitiesPow.lean`: `Real.add_rpow_le_rpow_add` l.190 (plus NNReal l.144, ENNReal l.282 versions); `Real.rpow_two` at Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:471.
- `lean_leansearch` (query above, 6 results): no matching lemma.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated. Necessity of both hypotheses checked by hand (x = 0 gives 1 < 1; c = 0 gives 3 < 1).
