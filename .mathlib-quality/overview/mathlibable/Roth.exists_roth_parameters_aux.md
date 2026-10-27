---
decl: Roth.exists_roth_parameters_aux
file: Roth/Main.lean
line: 410
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private parameter-selection step of the proof of Roth's theorem (choose f, A, m, delta satisfying eqs. 29-30, 47-49 of the source) bundling exists_monic_aeval_eq_zero, exists_m and exists_delta; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
action: Keep as private helper of its single call site Roth/Main.lean:551 (roth_of_isIntegral); no change.
---

# Roth.exists_roth_parameters_aux

## Inventory entry

### `theorem Roth.exists_roth_parameters_aux`
- **Type**: `∀ {α κ : ℝ}, IsIntegral ℤ α → 2 < κ → ∃ (f : Polynomial ℤ) (A : ℝ) (m : ℕ) (δ : ℝ), f.Monic ∧ Polynomial.aeval α f = 0 ∧ 1 ≤ A ∧ (∀ i, |(f.coeff i : ℝ)| ≤ A) ∧ 2 ≤ m ∧ 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * f.natDegree * √(m : ℝ) < m / 2 ∧ (m : ℝ) * (1 + 4 * δ) / (gam δ f.natDegree m - eta δ m) < κ`
- **What**: Let α be a real algebraic integer and κ > 2. Then there are a monic integer polynomial f with f(α) = 0, a real A ≥ 1 bounding all |coefficients| of f, an integer m ≥ 2 and a real δ with 0 < δ < 1/m such that η(δ, m) + 2(1 + 3δ) n √m < m/2 and m(1 + 4δ)/(γ(δ, n, m) − η(δ, m)) < κ, where n = deg f, η(δ, m) = 10^m δ^{(1/2)^m} and γ = (m − λ)/2. This is the opening parameter choice of §7 of the source (eqs. (29), (30), (47)–(49)), packaged for the proof by contradiction of Roth's theorem for algebraic integers.
- **How**: `Roth.exists_monic_aeval_eq_zero` gives f monic with f(α) = 0 and 2 ≤ natDegree f; A := 1 + ∑_{i ∈ support f} |coeff i|; `Roth.exists_m` (with n = natDegree f) gives m with 16 n² < m and the (47') inequality; `Roth.exists_delta` gives δ with the four δ-conditions. The remaining goals: 1 ≤ A by `le_add_of_nonneg_right` + `Finset.sum_nonneg`; the coefficient bound by mathlib's `Finsupp.single_eval_le_sum` applied to `f.toFinsupp.coeff` with g = |·| (same pattern as `Roth.abs_coeff_le_normOne`), then `le_add_of_nonneg_left zero_le_one`; 2 ≤ m by `nlinarith only [hm, hdeg]` (16 n² < m with n ≥ 2).
- **Hypotheses**: `hint : IsIntegral ℤ α` (gives f via `exists_monic_aeval_eq_zero`), `hκ : 2 < κ` (needed by `exists_m`). Both used, neither redundant. Irrationality of α is not needed here (the `2 ≤ natDegree` is manufactured by multiplying by X²).
- **Uses from project**: `Roth.exists_monic_aeval_eq_zero` (Roth/Main.lean:142), `Roth.exists_m` (Roth/Main.lean:196), `Roth.exists_delta` (Roth/Main.lean:227), `Roth.eta` (Roth/MainLemma.lean:66), `Roth.gam` (Roth/MainLemma.lean:63).
- **Used by**: Roth/Main.lean:551 `Roth.roth_of_isIntegral` (destructured into f, A, m, δ and all nine facts). `grep -rn exists_roth_parameters_aux Roth/` gives only the definition (l.410) and this use. Transitively feeds `Roth.roth` (main theorem).
- **Visibility**: private
- **Lines**: 410–427, proof length 13 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; preceded by a plain `--` comment rather than a docstring (fine for a private lemma). The coefficient-bound part repeats the `Finsupp.single_eval_le_sum` idiom of `Roth.abs_coeff_le_normOne` for univariate polynomials; harmless (one line).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Main.lean:551 in `roth_of_isIntegral`, where it supplies all parameters of the contradiction argument.
- Wrapper of 1–2 mathlib calls? No. It bundles three project lemmas (`exists_monic_aeval_eq_zero`, `exists_m`, `exists_delta`) plus the definition of A and three small side goals.
- Does mathlib have it? No: the statement involves the project-specific quantities `eta` and `gam` (constants of Roth's Lemma 9 / §7) and is a pure parameter-choice existence statement with no general content. The only mathlib ingredient, `Finsupp.single_eval_le_sum` (Mathlib/Data/Finsupp/Order.lean:165), is used directly.
- Too specific (inline?)? Specific to one call site; it could be inlined into `roth_of_isIntegral`, but it was deliberately factored out (together with sibling `_aux` lemmas `exists_roth_approximants_aux`, `one_lt_roth_eval_bound_aux`, `roth_product_bound_aux`, `roth_log_bound_aux`) to keep the main proof a short, readable chain mirroring §7. Keep factored.
- Well-chosen statement? Yes: minimal hypotheses, conclusion shaped exactly to what the caller destructures. Minor: `1 ≤ A` is only used downstream as `0 ≤ A` (via `zero_le_one.trans hA1`); harmless.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site (Roth/Main.lean:551); no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Main.lean:410; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable-looking ingredients are assessed under their own entries (`Roth.exists_monic_aeval_eq_zero.md`, `Roth.exists_m.md`, `Roth.exists_delta.md`).

## Evidence
- `grep -rn exists_roth_parameters_aux Roth/`: definition Roth/Main.lean:410, single use Roth/Main.lean:551.
- Read the body (Roth/Main.lean:409–427), the call site (Roth/Main.lean:547–563) and the dependency statements: `exists_monic_aeval_eq_zero` (Roth/Main.lean:142), `exists_m` (l.196), `exists_delta` (l.227), `gam`/`eta` (Roth/MainLemma.lean:63, 66), `eta_lt_gam_iff` (Roth/MainLemma.lean:100, used by the caller with h30).
- `grep -rn single_eval_le_sum`: mathlib Mathlib/Data/Finsupp/Order.lean:165; project uses at Roth/Main.lean:424 and Roth/CoeffNorm.lean:73 (`abs_coeff_le_normOne`).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
