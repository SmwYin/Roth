---
decl: Roth.theta_lt_base_aux
file: Roth/Theta.lean
line: 818
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private m = 1 base case of Lemma 7 (Theta_1(q^{delta r}; q; r) at most delta, hence below 10 delta^{1/2}) via Lemma 5 Θ_unique_le; tied to the project-specific Theta, no mathlib home.
action: Keep as private helper for its sole use in the zero case of Roth.Θ_lt (Roth/Theta.lean:973); optionally add a docstring citing clean.tex l.964-967 and use Real.self_le_rpow_of_le_one for h1.
---

# Roth.theta_lt_base_aux

## Inventory entry

### `theorem Roth.theta_lt_base_aux`
- **Type**: `∀ {δ : ℝ}, 0 < δ → δ ≤ 1 → ∀ {r q : Fin 1 → ℕ}, 0 < r 0 → 1 < q 0 → Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ 1 * δ ^ ((1 / 2 : ℝ) ^ 1)` (declared `private lemma`).
- **What**: The `m = 1` base case of Lemma 7: for one variable with `r_1 > 0`, `q_1 > 1` and `0 < δ ≤ 1`, `Θ_1(q_1^{δ r_1}; q_1; r_1) < 10 δ^{1/2}`. Mirrors clean.tex l.964–967: by Lemma 5, `Θ_1 ≤ δ r_1 log q_1 / (r_1 log q_1) = δ < 10 δ^{1/2}`. The conclusion is stated in the literal shape `10 ^ 1 * δ ^ ((1/2) ^ 1)` of `Θ_lt` at `n = 0`, so it plugs in without rewriting.
- **How**: Step `h`: `Θ_unique_le` (Lemma 5) with `B = q_0^{δ r_0}`, `1 ≤ B` from `Real.one_le_rpow`, gives `Θ ≤ log B / (r_0 log q_0)`; then `Subsingleton.elim (default : Fin 1) 0`, `Real.log_rpow` and `field_simp` (nonvanishing of `r_0` and of `log q_0` via `Real.log_pos`) reduce the right side to `δ`. Step `h1`: `δ ≤ δ^{1/2}` from `Real.rpow_le_rpow_of_exponent_ge hδ0 hδ` (needs `δ ≤ 1`). Finally `norm_num only [pow_one]` and `lt_mul_of_one_lt_left (Real.rpow_pos_of_pos hδ0 _)` with `1 < 10`.
- **Hypotheses**: `hδ0` for `Real.rpow_pos_of_pos`, positivity of the exponent, and `rpow_le_rpow_of_exponent_ge`; `hδ : δ ≤ 1` for `δ ≤ δ^{1/2}` (the call site handles `δ > 1` separately via `theta_lt_of_large_delta_aux`); `hrlast : 0 < r 0` for cancelling `r_0` in `field_simp`; `hq1 : 1 < q 0` for `Θ_unique_le`, `1 ≤ B` and `log q_0 ≠ 0`. All used.
- **Uses from project**: `Roth.Θ` (def, Roth/Theta.lean:68), `Roth.Θ_unique_le` (Lemma 5, Roth/Theta.lean:256). All other names are mathlib (`Real.one_le_rpow`, `Real.log_rpow`, `Real.log_pos`, `Real.rpow_le_rpow_of_exponent_ge`, `Real.rpow_pos_of_pos`, `lt_mul_of_one_lt_left`, `Subsingleton.elim`, `ne_of_gt`; tactics `field_simp`, `norm_num`, `positivity`, `simpa`, `exact_mod_cast`).
- **Used by**: Roth/Theta.lean `Roth.Θ_lt` only (l.973, `zero` case of the induction, branch `δ ≤ 1`, with `hq1` supplied by `theta_denominators_one_lt_aux`). `grep -rn theta_lt_base_aux Roth/` returns only the definition (l.818) and this use.
- **Visibility**: private
- **Lines**: 818–831, proof length 11 lines (821–831; statement 818–820)
- **Notes**: No docstring. Name ends in `_aux`, so the Step 9a pre-filter would also fire. Faithful to the source base case; the `δ ≤ 1` restriction is an artefact of the Lean statement of `Θ_lt` dropping the source's `δ < 1/m` (the large-δ case is handled trivially elsewhere). Cosmetic: `h1` could be `Real.self_le_rpow_of_le_one hδ0.le hδ (by norm_num)` (as used at l.951), avoiding the `simpa`.

## Junk check (Step 8)
- Used anywhere? Yes, exactly once: the base case of the public `Roth.Θ_lt` (Lemma 7, l.973).
- Wrapper of 1–2 mathlib calls? No. It is a short computation on top of the project lemma `Θ_unique_le`; the core content is about the project's own `Θ`, which mathlib does not have.
- Does mathlib have it? No: the head symbol `Roth.Θ` (sSup of indices over the project's `indexSet`) is project-defined; a mathlib search is moot.
- Too specific / inline? It could be inlined (11 lines) into the `zero` case of `Θ_lt`, but extraction keeps the induction skeleton of `Θ_lt` readable and parallels `theta_lt_succ_aux` for the succ case; it corresponds to a self-contained sentence of the source proof. Better kept separate.
- Well-chosen? Yes. Hypotheses are minimal for the argument; the conclusion shape matches the call site exactly.
- Conclusion: `KEEP`. Action: none required; optionally add a docstring citing clean.tex l.964–967 and simplify `h1` with `Real.self_le_rpow_of_le_one`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:818); additionally the name ends in `_aux`.

Side note: even public, it is an internal base-case lemma about the project-specific quantity `Θ` from the proof of Roth's theorem; no mathlib home.

## Evidence
- Read Roth/Theta.lean l.818–831 (declaration), l.962–979 (`Θ_lt`, sole use at l.973), l.250–260 (`Θ_unique_le`), l.68 (`Θ` def), l.951 (`Real.self_le_rpow_of_le_one` usage).
- `grep -rn theta_lt_base_aux Roth/`: definition l.818, sole use l.973.
- Read `.mathlib-quality/references/clean.tex` l.935–967: statement of Lemma 7 and its `m = 1` case via Lemma 5, matching this lemma.
- Hypothesis usage determined by reading the proof; no Lean runs and no evidence Lean files (a private SKIP needs no weakening experiments; the project builds clean so the lemma compiles as stated).
