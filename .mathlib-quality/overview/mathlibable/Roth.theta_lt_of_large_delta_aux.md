---
decl: Roth.theta_lt_of_large_delta_aux
file: Roth/Theta.lean
line: 932
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private large-delta case of Lemma 7 (delta at least 1/(n+1)) closed by the trivial bound Theta at most card via Θ_le_card and (n+1)^2 < 4^(n+1); project-specific Theta estimate extending the source beyond its delta < 1/m hypothesis, no mathlib home.
action: Keep as private helper for its two uses in Roth.Θ_lt (Roth/Theta.lean:975 and :980); optionally add a docstring noting it covers the delta range excluded by clean.tex eq. (19).
---

# Roth.theta_lt_of_large_delta_aux

## Inventory entry

### `theorem Roth.theta_lt_of_large_delta_aux`
- **Type**: `∀ {n : ℕ} {δ : ℝ}, 1 / ((n : ℝ) + 1) ≤ δ → ∀ {r q : Fin (n + 1) → ℕ}, Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))` (declared `private lemma`).
- **What**: For `m = n + 1` variables and `δ ≥ 1/m`, the Lemma 7 conclusion `Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}` holds unconditionally (no hypotheses on `r`, `q`). This is the range `δ ≥ 1/m` excluded by the source's hypothesis (19) `0 < δ < m^{-1}` (clean.tex l.935–960); the project's `Θ_lt` drops that upper bound, and this lemma discharges the extra case.
- **How**: A `calc` chain: `Θ ≤ m` by `Θ_le_card` (with `Fintype.card_fin` via `simpa`); `m < 10^m / m` via `lt_div_iff₀` and `m·m < 2^m·2^m = 4^m ≤ 10^m` (`Nat.lt_two_pow_self`, `mul_self_lt_mul_self`, `mul_pow`, `pow_le_pow_left₀`); rewrite `10^m / m = 10^m · (1/m)` (`mul_one_div`); finally `1/m ≤ (1/m)^{(1/2)^m} ≤ δ^{(1/2)^m}` by `Real.self_le_rpow_of_le_one` (base `1/m ≤ 1` via `div_le_one`, exponent `≤ 1` via `pow_le_one₀`) and `Real.rpow_le_rpow` with `hδ`, under `mul_le_mul_of_nonneg_left`.
- **Hypotheses**: Only `hδ`, and it is used (last `calc` step, `Real.rpow_le_rpow`). It is essential in the sense that for small `δ` the right side tends to `0` while `Θ` can be positive; no hypotheses on `r`, `q` are needed (the bound `Θ ≤ card` is unconditional).
- **Uses from project**: `Roth.Θ` (Roth/Theta.lean:68), `Roth.Θ_le_card` (l.114). Mathlib names: `Nat.lt_two_pow_self`, `lt_div_iff₀`, `mul_self_lt_mul_self`, `mul_pow`, `pow_le_pow_left₀`, `mul_one_div`, `mul_le_mul_of_nonneg_left`, `Real.self_le_rpow_of_le_one`, `div_le_one`, `pow_le_one₀`, `Real.rpow_le_rpow`, `Nat.cast_nonneg`.
- **Used by**: Roth/Theta.lean `Roth.Θ_lt` only, twice: l.975 (`zero` case, `δ > 1`) and l.980 (`succ` case, `δ > 1/(n+2)`). `grep -rn theta_lt_of_large_delta_aux Roth/` returns only the definition (l.932) and these two uses. Transitively feeds every user of public Lemma 7 `Roth.Θ_lt`.
- **Visibility**: private
- **Lines**: 932–953, proof length 19 lines (935–953; statement 932–934)
- **Notes**: No docstring. Name ends in `_aux`. Not in the source paper as such: it is the formalisation's extension of Lemma 7 to all `δ > 0` (the public `Θ_lt` docstring says "No upper bound on `δ` is required"). The bound is very lossy but suffices.

## Junk check (Step 8)
- Used anywhere? Yes, twice, both in public `Roth.Θ_lt` (base and inductive case).
- Wrapper of 1–2 mathlib calls? No. It combines project `Θ_le_card` with a ~15-line real-analysis inequality `m < 10^m · δ^{(1/2)^m}` for `δ ≥ 1/m`.
- Does mathlib have it? No: the head symbol `Roth.Θ` is a project definition with no mathlib counterpart. The purely numeric core (`m < 10^m (1/m)^{(1/2)^m}`) is too specific to be a mathlib lemma.
- Too specific / inline? Specific, but used twice; inlining would duplicate 19 lines in both branches of the induction. Extraction is justified.
- Well-chosen? Yes; statement takes no superfluous hypotheses (no conditions on `r`, `q`), which lets both call sites apply it directly.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring explaining it covers `δ ≥ 1/m`, the range excluded by source eq. (19).

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:932); additionally the name ends in `_aux`.

Side note: even public, it is an internal case split of Lemma 7 about the project-specific quantity `Θ` from the proof of Roth's theorem; no mathlib home.

## Evidence
- Read Roth/Theta.lean l.880–985 (declaration, neighbouring `theta_lt_succ_aux`, both uses in `Θ_lt`) and the signature of `Θ_le_card` (l.114).
- `grep -rn theta_lt_of_large_delta_aux Roth/`: definition l.932, uses l.975 and l.980.
- Read `.mathlib-quality/references/clean.tex` l.935–975 (Lemma `roth:lem7`): source assumes `0 < δ < m^{-1}` (eq. 19), confirming this lemma covers the complementary range added by the formalisation.
- Prior report read: `.mathlib-quality/overview/mathlibable/Roth.theta_lt_succ_aux.md`.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
