---
decl: Roth.theta_delta_succ_lt_aux
file: Roth/Theta.lean
line: 767
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private elementary real inequality delta(1+1/(n+2)) < 1/(n+1) for delta at most 1/(n+2), the step delta_1 < 1/(p-1) in the source proof of Lemma 7 feeding the induction hypothesis; too specific for mathlib.
action: Keep as private helper for its sole use in theta_phi_lt_aux (Roth/Theta.lean:889); optionally add a one-line docstring citing the source inequality (p-1) delta_1 < (p-1)(p+1)/p^2 < 1.
---

# Roth.theta_delta_succ_lt_aux

## Inventory entry

### `theorem Roth.theta_delta_succ_lt_aux`
- **Type**: `∀ (n : ℕ) {δ : ℝ}, δ ≤ 1 / ((n : ℝ) + 1 + 1) → δ * (1 + 1 / ((n : ℝ) + 1 + 1)) < 1 / ((n : ℝ) + 1)` (declared `private lemma`).
- **What**: With `p = n + 2`, if `δ ≤ 1/p` then `δ_1 := δ(1 + 1/p) < 1/(p-1)`. Mathematically: `δ(1 + 1/p) ≤ (p+1)/p² < 1/(p-1)` because `(p-1)(p+1) = p² - 1 < p²`. This is the source inequality `0 < (p-1)δ_1 < (p-1)(p+1)/p² < 1` (clean.tex l.995, proof of Lemma 7), which certifies that the enlarged parameter `δ_1` satisfies the induction hypothesis' bound `δ_1 ≤ 1/(p-1)`.
- **How**: Records `0 < n+1` and `0 < n+2` by `positivity`; bounds the left side by `(1/(n+2)) * (1 + 1/(n+2))` via `mul_le_mul_of_nonneg_right hδ (by positivity)`; rewrites the target with `lt_div_iff₀`; closes with `nlinarith only [one_div_mul_cancel (ne_of_gt hN2), sq_pos_of_pos (one_div_pos.mpr hN2)]`.
- **Hypotheses**: The single hypothesis `hδ` is necessary (for large `δ` the conclusion fails). No sign condition on `δ` is needed: the factor `1 + 1/(n+2)` is positive, so negative `δ` is covered by the same monotonicity step. `n` is explicit because it cannot be inferred from the conclusion's use site otherwise (it is passed as `theta_delta_succ_lt_aux n hδ`).
- **Uses from project**: `[]` (only mathlib lemmas: `mul_le_mul_of_nonneg_right`, `lt_div_iff₀`, `one_div_mul_cancel`, `sq_pos_of_pos`, `one_div_pos`, tactics `positivity`, `nlinarith`).
- **Used by**: Roth/Theta.lean `Roth.theta_phi_lt_aux` only (l.889, as `(theta_delta_succ_lt_aux n hδ).le`, the `δ`-bound argument to the induction hypothesis `ih` at `ε = δ(1 + 1/(n+2))`). `grep -rn theta_delta_succ_lt_aux Roth/` returns only the definition (l.767) and this use. Transitively: `theta_phi_lt_aux` (l.840) → `theta_lt_succ_aux` (l.891) → public `Roth.Θ_lt` (Lemma 7, l.962).
- **Visibility**: private
- **Lines**: 767–774, proof length 6 lines (769–774)
- **Notes**: No docstring. Name ends in `_aux`, so the Step 9a pre-filter would also fire. A natural generalisation (real `N > 0`, `δ ≤ 1/(N+1)` implies `δ(1 + 1/(N+1)) < 1/N`) exists but has no use.

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: in the private `theta_phi_lt_aux` (l.889), on the path to the public `Roth.Θ_lt` (Lemma 7).
- Wrapper of 1–2 mathlib calls? No single mathlib lemma gives it; it is a monotonicity step plus a nonlinear arithmetic finish (`nlinarith` with two hints). Not a thin wrapper.
- Does mathlib have it? No. `lean_leansearch` for the inequality returned only unrelated lemmas (`Nat.one_div_lt_one_div`, `Nat.one_div_le_one_div`, `one_div_pow_lt_one_div_pow_of_lt`, ...); this is a bespoke numeric inequality, not a named fact.
- Too specific / inline? It is very specific, and could in principle be inlined at its single use. But the use site is a long `exact` term combining several terms; inlining a 6-line `nlinarith` proof there would hurt readability. A separate helper matching one displayed inequality of the source is the better style.
- Well-chosen? Yes: minimal hypotheses (no unnecessary `0 ≤ δ`), stated in the exact casted form `(n : ℝ) + 1 + 1` used at the call site, so no rewriting is required there.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring citing the source inequality `(p-1)δ_1 < (p-1)(p+1)/p² < 1` (proof of Lemma 7).

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:767); additionally the name ends in `_aux`.

Side note: even public, this is an ad hoc numeric inequality with no natural mathlib home; `nlinarith`/`field_simp` dispatch such facts on demand.

## Evidence
- `grep -rn theta_delta_succ_lt_aux Roth/`: definition l.767, sole use l.889 (inside `theta_phi_lt_aux`, l.840).
- `grep -n` for `theta_phi_lt_aux`, `theta_lt_succ_aux`, `Θ_lt` in Roth/Theta.lean: chain l.840 → l.891 → l.962.
- Read `.mathlib-quality/references/clean.tex` l.981–995: `δ_1 = δ(1+p^{-1})` and `0 < (p-1)δ_1 < (p-1)(p+1)/p^2 < 1` match this lemma with `p = n+2`.
- `lean_leansearch` ("(n+1)(n+3) < (n+2)^2, so (1/(n+2))(1+1/(n+2)) < 1/(n+1)"): no matching mathlib lemma.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
