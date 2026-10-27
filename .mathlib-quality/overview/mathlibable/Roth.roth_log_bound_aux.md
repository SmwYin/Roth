---
decl: Roth.roth_log_bound_aux
file: Roth/Main.lean
line: 505
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private final step of the section 7 proof of Roth's theorem that takes logarithms of the evaluation bound 1 < P N B^(1+3 delta) q_0^(-r_0 G kappa) and combines it with (53), B at most q_0^(delta r_0) and N < B^delta to get G kappa < m (1 + 4 delta); Roth-specific real-analysis bookkeeping, used once by roth_of_isIntegral, nothing for mathlib.
action: Keep as private helper of its single call site Roth/Main.lean:561 (roth_of_isIntegral); no change.
---

# Roth.roth_log_bound_aux

## Inventory entry

### `theorem Roth.roth_log_bound_aux`
- **Type**: `∀ {m : ℕ} [NeZero m], 2 ≤ m → ∀ {δ G κ B : ℝ}, δ ≤ 1 → ∀ {q r : Fin m → ℕ}, (∀ j, 1 < q j) → (∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))) → 0 < B → B ≤ (q 0 : ℝ) ^ (δ * r 0) → (∏ j, ((r j : ℝ) + 1)) < B ^ δ → 1 < (∏ j, (q j : ℝ) ^ r j) * ((∏ j, ((r j : ℝ) + 1)) * B ^ (1 + 3 * δ) * (q 0 : ℝ) ^ (-(r 0 : ℝ) * G * κ)) → G * κ < m * (1 + 4 * δ)`
- **What**: Let m ≥ 2, δ ≤ 1, integers q_j > 1 and degrees r_j with r_j log q_j < (1 + δ/10) r_0 log q_0 for every j (inequality (53) of the source), and B > 0 with B ≤ q_0^{δ r_0} and N := ∏ (r_j + 1) < B^δ. If 1 < (∏ q_j^{r_j}) · N · B^{1+3δ} · q_0^{-r_0 G κ}, then G κ < m (1 + 4δ). This is the logarithmic comparison closing §7 of the source; combined with (49) it yields the contradiction in `roth_of_isIntegral`.
- **How**: First derives r_0 > 0 (else (53) at j = 0 reads 0 < 0), K := r_0 log q_0 > 0 (`Real.log_pos`, `Nat.one_lt_cast`), and δ ≥ 0 from (53) at j = 0 (`mul_lt_mul_iff_left₀`, `lt_add_iff_pos_right`, `div_pos_iff_of_pos_right`). Takes `Real.log_pos` of `hone` and splits it with three `Real.log_mul` and two `Real.log_rpow` rewrites (positivity side goals via `Finset.prod_pos`, `Real.rpow_pos_of_pos`, `Nat.cast_add_one_pos`). Bounds log ∏ q_j^{r_j} < m (1 + δ/10) K by `Real.log_prod`, `Real.log_pow` and `Finset.sum_lt_sum_of_nonempty` summing (53). Then `linarith only` with log N < δ log B (`Real.log_lt_log`, `Real.log_rpow`) and (1 + 4δ) log B ≤ (1 + 4δ) δ K (`Real.log_le_log`, `mul_le_mul_of_nonneg_left`) gives K · (m(1 + δ/10) + (1 + 4δ)δ - Gκ) > 0, cancelled by `mul_pos_iff_of_pos_left`. Finally (1 + 4δ)δ ≤ (39/10) m δ (from δ ≤ 1, m ≥ 2, δ ≥ 0, `mul_le_mul_of_nonneg_right`) and `linarith` give Gκ < m(1 + 4δ).
- **Hypotheses**: hm2 and hδ1 (only in the last step, to get 1 + 4δ ≤ (39/10) m); hq1 (positivity of q_j and log q_0 > 0); h53 (bound on log ∏ q_j^{r_j}, and source of r_0 > 0 and δ ≥ 0); hBpos (positivity for the logarithm rewrites); hBX (log B ≤ δ K); hN (log N < δ log B); hone (the inequality being logged); `[NeZero m]` (index 0 and nonemptiness of `Finset.univ` for `Finset.sum_lt_sum_of_nonempty`). All used. G and κ occur only through the product G κ (κ is named explicitly at the call site, G is inferred by unification from the evaluation bound).
- **Uses from project**: `[]` (no project identifiers in the statement or proof; all lemmas are from mathlib/core).
- **Used by**: Roth/Main.lean:561 `Roth.roth_of_isIntegral` (fed the conclusion of `one_lt_roth_eval_bound_aux` as `hone` and the three outputs of `roth_product_bound_aux` as hBpos, hBX, hN; its result contradicts (49)). `grep -rn roth_log_bound_aux Roth/` gives only the definition (l.505) and this use. Transitively feeds `Roth.roth` and `Roth.roth_rat`.
- **Visibility**: private
- **Lines**: 505–541, proof length 31 lines (511–541; statement 505–510)
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; preceded by a plain `--` comment, not a docstring (acceptable for private). The constants hm2/hδ1 are slack: any hypotheses giving 1 + 4δ ≤ (39/10) m would do (for example m ≥ 1 with δ ≤ 29/40); not worth changing since the caller has both facts at hand.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Main.lean:561 in `roth_of_isIntegral`.
- Wrapper of 1–2 mathlib calls? No. About ten substantive steps: three derived positivity facts, a five-rewrite logarithm split, a summed bound over `Fin m`, and two `linarith` combinations.
- Does mathlib have it? No. The statement is an inequality with Roth-specific constants (1 + δ/10, 1 + 3δ, 1 + 4δ, 39/10) between quantities defined in the §7 proof; there is no general mathematical content beyond `Real.log_mul`/`Real.log_rpow`/`Real.log_prod` and linear arithmetic, all of which the proof already uses directly from mathlib.
- Too specific (inline?)? Specific to its one call site and could be inlined into `roth_of_isIntegral`, but it is deliberately factored out together with its sibling `_aux` lemmas (`exists_roth_parameters_aux`, `exists_roth_approximants_aux`, `roth_product_bound_aux`, `one_lt_roth_eval_bound_aux`) so the main proof is a short chain mirroring §7; inlining would add ~31 lines to `roth_of_isIntegral` with no gain.
- Well-chosen statement? Yes: hypotheses match exactly what the caller has (h53 and hq1 from `exists_roth_approximants_aux`, hBpos/hBX/hN verbatim from `roth_product_bound_aux`, hone from `one_lt_roth_eval_bound_aux`), and δ ≥ 0 and r_0 > 0 are derived internally rather than demanded. Minor possible tidy-up (not recommended): G κ could be a single real variable, but keeping κ separate makes the call site's `(κ := κ)` match (49) directly.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site (Roth/Main.lean:561); no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Main.lean:505; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

## Evidence
- `grep -rn roth_log_bound_aux Roth/`: definition Roth/Main.lean:505, single use Roth/Main.lean:561.
- Read the body (Roth/Main.lean:504–541) and the call site in `roth_of_isIntegral` (Roth/Main.lean:545–563), including the sibling outputs it consumes.
- Checked by hand the final arithmetic: G κ < m(1 + δ/10) + (1 + 4δ)δ and (1 + 4δ)δ ≤ (39/10) m δ give G κ < m(1 + 4δ); 1 + 4δ ≤ 5 ≤ 7.8 ≤ (39/10) m uses both hδ1 and hm2.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
