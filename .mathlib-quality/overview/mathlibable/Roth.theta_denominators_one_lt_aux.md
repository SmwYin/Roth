---
decl: Roth.theta_denominators_one_lt_aux
file: Roth/Theta.lean
line: 833
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 3-line glue deriving 1 < q j from 0 < r 0, 0 < log q 0 and the Lemma 7 growth condition r 0 log q 0 at most r j log q j; Lemma-7-specific hypothesis shape, no mathlib home.
action: Keep as private helper for its three uses in Roth/Theta.lean (theta_phi_lt_aux l.862, theta_lt_succ_aux l.907, Θ_lt l.974); optionally add a docstring; the same argument is re-derived inline in theta_scaled_unique_le_aux (l.752-757) but entangled with hr₂, so no refactor needed.
---

# Roth.theta_denominators_one_lt_aux

## Inventory entry

### `theorem Roth.theta_denominators_one_lt_aux`
- **Type**: `∀ {n : ℕ} {r q : Fin (n + 1) → ℕ}, 0 < r 0 → 0 < Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → ∀ (j : Fin (n + 1)), 1 < q j` (declared `private lemma`).
- **What**: Under the Lemma 7 growth condition `r_1 log q_1 ≤ r_j log q_j` (clean.tex (21)-type hypothesis `hqr` of `Θ_lt`), together with `r_1 > 0` and `log q_1 > 0`, every denominator satisfies `q_j > 1`. Supplies the `1 < q` side conditions needed by Lemma 5 (`Θ_unique_le`) and by `Real.one_le_rpow`.
- **How**: One term: `mul_pos` gives `0 < r 0 * log (q 0)`; `.trans_le (hqr j)` gives `0 < r j * log (q j)`; `pos_of_mul_pos_right` (with `Nat.cast_nonneg (r j)`) gives `0 < log (q j)`; `Real.log_pos_iff (Nat.cast_nonneg (q j))` converts to `1 < (q j : ℝ)`; `exact_mod_cast` lands in `ℕ`.
- **Hypotheses**: `hrlast : 0 < r 0` and `hq1 : 0 < log (q 0)` both feed `mul_pos` and are necessary (with either zero the left side of `hqr` is `0` and nothing is forced); `hqr` used at index `j`. All used, none redundant. (`hrlast` is a misnomer here: it is positivity of `r 0`, not of the last entry.)
- **Uses from project**: `[]` (only mathlib names: `Real.log_pos_iff`, `pos_of_mul_pos_right`, `mul_pos`, `Nat.cast_nonneg`, `LT.lt.trans_le`; tactic `exact_mod_cast`).
- **Used by**: Roth/Theta.lean only: `Roth.theta_phi_lt_aux` (l.862, at `j = 0`), `Roth.theta_lt_succ_aux` (l.907, partially applied, used as `hq _` and `hq 0` at l.925-926), `Roth.Θ_lt` (l.974, zero case, at `j = 0`). `grep -rn theta_denominators_one_lt_aux Roth/` returns only these plus the definition.
- **Visibility**: private
- **Lines**: 833–838, proof length 3 lines (836–838; statement 833–835)
- **Notes**: No docstring. Name ends in `_aux` (Step 9a pre-filter would also fire). The same chain (`mul_pos`, `trans_le hqr`, `pos_of_mul_pos_right`, `Real.log_pos_iff`) is re-derived inline in `theta_scaled_unique_le_aux` (l.752–757) for a two-scalar version, where intermediate facts (`hL₂`, `hr₂`) are also reused, so sharing would not simplify it.

## Junk check (Step 8)
- Used anywhere? Yes, three call sites (theta_phi_lt_aux, theta_lt_succ_aux, Θ_lt), all in Roth/Theta.lean.
- Wrapper of 1–2 mathlib calls? Essentially a composition of four elementary mathlib lemmas (`mul_pos`, `pos_of_mul_pos_right`, `Real.log_pos_iff`, casting); not a single-call wrapper, and it packages the project-specific `hqr` hypothesis shape so the three callers avoid repeating it.
- Does mathlib have it? No: leansearch for "0 < a * log x, a * log x ≤ b * log y, b ≥ 0 implies 1 < y" returned only generic log/rpow monotonicity lemmas (`Real.log_lt_log_iff`, `Real.rpow_le_iff_le_log`, ...). The hypothesis shape is tied to Lemma 7.
- Too specific / inline? Specific, but used 3 times; inlining would triplicate a 3-line term at each site. Keep.
- Well-chosen? Yes; hypotheses minimal and match what callers have on hand (they derive `0 < log (q 0)` from the `hq1` lower bound by `positivity`).
- Conclusion: `KEEP`. Action: none required; optionally add a one-line docstring and rename `hrlast` to `hr0`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:833); additionally the name ends in `_aux`.

Side note: even public, it is an elementary consequence of `Real.log_pos_iff` under a Lemma-7-specific hypothesis; not mathlib material.

## Evidence
- Read Roth/Theta.lean l.742–764 (`theta_scaled_unique_le_aux`, inline duplicate of the argument), l.818–838 (declaration), l.840–931 (callers `theta_phi_lt_aux`, `theta_lt_succ_aux`), l.962–979 (`Θ_lt`).
- `grep -rn theta_denominators_one_lt_aux Roth/`: definition l.833, uses l.862, l.907, l.974.
- Confirmed `Real.log_pos_iff (hx : 0 ≤ x) : 0 < log x ↔ 1 < x` at Mathlib/Analysis/SpecialFunctions/Log/Basic.lean:181.
- `lean_leansearch` query for the statement shape: no matching mathlib lemma.
- No Lean runs and no evidence Lean files (private SKIP; no weakening claimed; project builds clean).
