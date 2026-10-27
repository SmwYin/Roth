---
decl: Roth.two_pow_lt_rpow_aux
file: Roth/Theta.lean
line: 621
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private real-analytic step of Lemma 7 showing 2^((2p+1) r1 l) < q^(delta/p * l r1) when log q is at least p(2p+1)/delta; a log/exp comparison built from Real.rpow_def_of_pos and log 2 < 1 whose shape is dictated by lem6M_lt, with no mathlib counterpart.
action: Keep as private helper for its sole use in lem6M_lt (Roth/Theta.lean:668); no upstream action.
---

# Roth.two_pow_lt_rpow_aux

## Inventory entry

### `theorem Roth.two_pow_lt_rpow_aux`
- **Type**: `∀ {p r₁ l : ℕ}, 0 < p → ∀ {δ q : ℝ}, 0 < δ → 0 ≤ q → (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q → 0 < l * r₁ → (2 : ℝ) ^ ((2 * p + 1) * r₁ * l) < q ^ (δ / p * (l * r₁))` (declared `private lemma`; left side is a natural-number power `Monoid.npow`, right side `Real.rpow`).
- **What**: If `p > 0`, `δ > 0`, `q ≥ 0`, `log q ≥ p(2p+1)/δ` and `l r₁ > 0`, then `2^{(2p+1) r₁ l} < q^{(δ/p) l r₁}`. This is the step of the source's proof of Lemma 7 (§5) that absorbs the factor `2^{(2p+1) r₁ l}` bounding the non-`B` part of `lem6M` into the extra `q₁^{δ l r₁ / p}`, giving `M < q₁^{δ(1+1/p) l r₁}`.
- **How**: First upgrades `0 ≤ q` to `0 < q` via `Real.log_pos_iff` (since `log q ≥ p(2p+1)/δ > 0`, so `q > 1`). Proves `log 2 < 1` from `Real.log_lt_sub_one_of_pos`, and `2p+1 ≤ log q · (δ/p)` from `hlog` by `mul_div_assoc'`, `le_div_iff₀`, `div_le_iff₀`, `linarith`. Then rewrites both sides as exponentials (`Real.rpow_natCast`, `Real.rpow_def_of_pos` twice, `Real.exp_lt_exp`) and closes the resulting `log 2 · (2p+1) r₁ l < log q · (δ/p) · l r₁` by a 3-step `calc` using `push_cast`/`ring`, `mul_lt_mul_of_pos_right` and `mul_lt_of_lt_one_left` chained with the bound `h3`.
- **Hypotheses**: `hp : 0 < p` (needed: the division `δ / p` and the `le_div_iff₀` step; for `p = 0` the right side is `q^0 = 1` while the left is `2^{r₁ l} > 1`). `hδ : 0 < δ` (used in `div_le_iff₀`). `hq : 0 ≤ q` (needed for `Real.log_pos_iff`; for negative `q` Mathlib's `log q = log |q|` and `Real.rpow` of a negative base involves a cosine factor, so the claim is not available in that form). `hlog` (the quantitative core). `hlr : 0 < l * r₁` (needed for strictness: if `l r₁ = 0` both sides equal 1). All hypotheses are used and natural for the call site.
- **Uses from project**: `[]` (only mathlib: `Real.log_pos_iff`, `Real.log_lt_sub_one_of_pos`, `le_div_iff₀`, `div_le_iff₀`, `mul_div_assoc'`, `Real.rpow_natCast`, `Real.rpow_def_of_pos`, `Real.exp_lt_exp`, `mul_lt_mul_of_pos_right`, `mul_lt_of_lt_one_left`, tactics `positivity`, `linarith`, `push_cast`, `ring`).
- **Used by**: Roth/Theta.lean `Roth.lem6M_lt` only (l.668, `two_pow_lt_rpow_aux hp hδ0 hq1pos.le hq₁ (Nat.mul_pos (by lia) (by lia))`, the strict step of its `calc`). `grep -rn two_pow_lt_rpow_aux Roth/` returns only the definition (l.621) and this use.
- **Visibility**: private
- **Lines**: 621–644, proof length 21 lines (624–644)
- **Notes**: Name ends in `_aux`, so the Step 9a pre-filter would also fire. Sibling of `factorial_coefficient_le_two_pow_aux` (l.609); together they split `lem6M_lt` into an ℕ-arithmetic part and a real-analytic part. Minor golf opportunity (not required): `hlog2` could come from mathlib's `Real.log_two_lt_d9` plus `norm_num` instead of `Real.log_lt_sub_one_of_pos`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.lem6M_lt` (public, Lemma 7 support), Roth/Theta.lean:668.
- Wrapper of 1–2 mathlib calls? No. It combines the exp/log representation of `rpow` (`Real.rpow_def_of_pos`), a numeric bound `log 2 < 1`, and field rearrangement of `hlog`; about 20 lines of genuine argument.
- Does mathlib have it? No. The ingredients are in mathlib (`Real.rpow_def_of_pos`, Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:51; `Real.log_pos_iff`, Mathlib/Analysis/SpecialFunctions/Log/Basic.lean:181; `Real.log_lt_sub_one_of_pos`, same file l.260), but the combined inequality has a project-specific exponent shape `(2p+1) r₁ l` vs `δ/p · l r₁` determined by `lem6M`. Not a general mathlib-style statement.
- Too specific / inline? It could be inlined as a `have` in `lem6M_lt`, but doing so would push a 20-line log/exp argument into an already long `calc`; keeping it separate mirrors the sibling helper and keeps `lem6M_lt` readable. Separate private helper is the right granularity.
- Well-chosen? Yes; hypotheses are minimal and each is used (see Hypotheses). `0 ≤ q` rather than `0 < q` is the weaker form and matches the call site (`hq1pos.le`).
- Conclusion: `KEEP`. Action: none (optional golf of `hlog2` via `Real.log_two_lt_d9`).

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:621); additionally the name ends in `_aux`.

Side note: any upstreamable content would be the generic ingredients (rpow as exp of log, `log 2 < 1`), which mathlib already has.

## Evidence
- `grep -rn two_pow_lt_rpow_aux Roth/`: definition l.621, sole use l.668 (`lem6M_lt`).
- Read Roth/Theta.lean l.600–675 (this lemma, sibling `factorial_coefficient_le_two_pow_aux`, and `lem6M_lt`) to confirm the "What", "How" and call site.
- `grep` of `.lake/packages/mathlib/Mathlib/`: `Real.rpow_def_of_pos` (Analysis/SpecialFunctions/Pow/Real.lean:51), `Real.log_pos_iff` (Analysis/SpecialFunctions/Log/Basic.lean:181), `Real.log_lt_sub_one_of_pos` (same file l.260); no combined inequality of this shape.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated. Necessity of `hp`, `hlr` is by hand (counterexamples `p = 0`, resp. `l r₁ = 0`, make both sides comparable as 2^n vs 1, resp. 1 vs 1).
