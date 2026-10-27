---
decl: Roth.two_lt_rpow_aux
file: Roth/MainLemma.lean
line: 156
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private numerical helper giving q1^(delta r1) > 2 from log 2 < delta^2 log q1 (delta at least 0, r1 positive), used once in three_small_factors; mathlib has only the reduction Real.lt_rpow_of_log_lt, the rest is a source-specific nlinarith estimate.
action: Keep as private helper for its single call site Roth/MainLemma.lean:193 (three_small_factors); no mathlib PR; optionally note it shares the proof skeleton of Roth.four_lt_rpow (l.122) but neither subsumes the other.
---

# Roth.two_lt_rpow_aux

## Inventory entry

### `theorem Roth.two_lt_rpow_aux`
- **Type**: `∀ {δ : ℝ}, 0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → Real.log 2 < δ ^ 2 * Real.log ↑q₁ → 2 < (↑q₁ : ℝ) ^ (δ * ↑r₁)`
- **What**: If `δ ≥ 0`, `r₁ ≥ 1` and `log 2 < δ² log q₁`, then `X = q₁^{δ r₁} > 2`. Mathematically: the hypothesis forces `log q₁ > 0`, hence `q₁ ≥ 2` and `log q₁ ≥ log 2`, so `δ log q₁ = √(δ² log q₁ · log q₁) > √(log 2 · log 2) = log 2`, and multiplying by `r₁ ≥ 1` gives `δ r₁ log q₁ > log 2`.
- **How**: `hlog2 : 0 < log 2` (`Real.log_pos`); `hL : 0 < log q₁` (`pos_of_mul_pos_right` with `sq_nonneg δ`); `hq : 2 ≤ q₁` (`Real.log_pos_iff`, cast); `hr : 1 ≤ (r₁ : ℝ)`; `hprod : log 2 < δ log q₁` by contradiction with `nlinarith only` fed `mul_self_le_mul_self`, `mul_lt_mul_of_pos_right h1 hL` and `mul_le_mul_of_nonneg_left (Real.log_le_log ...)`; finally `Real.lt_rpow_of_log_lt` reduces the goal to `log 2 < δ r₁ log q₁`, closed by `nlinarith only [hprod, le_mul_of_one_le_right ...]`.
- **Hypotheses**: `hδ0 : 0 ≤ δ` (necessary: δ = -1, q₁ = 3, r₁ = 1 satisfies `log 2 < log 3` but `3^{-1} < 2`); `hr₁ : 0 < r₁` (necessary: r₁ = 0 gives `X = 1`); `h1 : log 2 < δ² log q₁` (essentially sharp shape: at δ² log q₁ = log 2 with q₁ = 2, δ = 1, r₁ = 1 one gets X = 2, so strictness is needed for the strict conclusion).
- **Uses from project**: `[]` (only mathlib lemmas)
- **Used by**: Roth/MainLemma.lean:193 in `Roth.three_small_factors` (`have hX := (two_lt_rpow_aux hδ0 hr₁ (hlog2.trans_le h1)).le`) only; `grep -rn two_lt_rpow_aux Roth/` gives the definition (l.156) and this use. Transitively everything downstream of `three_small_factors`.
- **Visibility**: private
- **Lines**: 156–170, proof length 13 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); no docstring. The caller only uses `.le` (`2 ≤ X`). Same proof skeleton as the public `Roth.four_lt_rpow` (l.122, hypothesis `3 ≤ δ² log q₁`, conclusion `4 < X`), but neither implies the other at the caller: `three_small_factors` has only `1 ≤ δ² log q₁`, too weak for `four_lt_rpow`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.three_small_factors` (Roth/MainLemma.lean:193).
- Wrapper of 1–2 mathlib calls? No: 13-line proof; the only mathlib reduction is `Real.lt_rpow_of_log_lt`, the core is the nlinarith estimate `log 2 < δ log q₁`.
- Does mathlib have it? No. loogle `Real.log _ < _ → _ < (_ : ℝ) ^ (_ : ℝ)` returns only `Real.lt_rpow_of_log_lt` and its alias `Real.rpow_lt_of_lt_log`; leansearch (natural-language form of the statement) returns only `Real.rpow_le_of_le_log`, `Real.le_zpow_of_log_le`, `Real.lt_pow_of_log_lt`, `Real.lt_rpow_iff_log_lt`, `Real.logb_lt_iff_lt_rpow` — the generic log/power reductions, not this estimate.
- Too specific (inline?)? It is source-specific (§6 parameter estimate) and has a single caller, but inlining 13 lines into the already long `three_small_factors` proof would hurt readability; a private helper is the right factoring. Could be merged with `four_lt_rpow` into one lemma `Real.log c < δ log q₁`-style only by complicating both callers; not worth it.
- Well-chosen? Yes: both sign hypotheses are necessary (counterexamples above, elementary arithmetic), statement matches the caller's need.
- Conclusion: `KEEP` — action: keep as private helper for `three_small_factors`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:156; also name ends `_aux`).

## Evidence
- `grep -rn two_lt_rpow_aux Roth/`: definition l.156, single use l.193.
- `lean_loogle "Real.log _ < _ → _ < (_ : ℝ) ^ (_ : ℝ)"`: `Real.lt_rpow_of_log_lt`, `Real.rpow_lt_of_lt_log` only.
- `lean_leansearch "if log 2 < δ^2 log q and δ ≥ 0 then 2 < q ^ (δ r) real power"`: generic log/power reductions only (listed above).
- Compared with sibling report `Roth.four_lt_rpow.md` (same proof skeleton, different constants).
- No Lean runs and no evidence Lean files (private SKIP; counterexamples for necessity are elementary arithmetic; the project builds clean so the lemma compiles as stated).
