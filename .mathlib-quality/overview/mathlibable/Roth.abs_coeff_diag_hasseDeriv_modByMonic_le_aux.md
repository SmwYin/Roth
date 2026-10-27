---
decl: Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux
file: Roth/MainLemma.lean
line: 497
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 bookkeeping step chaining the Hasse-derivative, diagonal-substitution and modByMonic coefficient bounds into one explicit remainder bound; used once by the floor variant; mathlib has no multivariate Hasse derivative, no diag map and no modByMonic coefficient bound.
action: Keep as private helper of its single call site Roth/MainLemma.lean:533 (abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux, inside its local bound); no change.
---

# Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux

## Inventory entry

### `theorem Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
- **Type**: `∀ {σ : Type*} [Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ} {r : σ → ℕ} {A B : ℝ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → (∀ k, degreeOf k P ≤ r k) → (∀ d, |(P.coeff d : ℝ)| ≤ B) → ∀ (j : σ →₀ ℕ) (i : ℕ), |((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)| ≤ (1 + A) ^ ((∑ k, r k) + 1 - f.natDegree) * (((∏ k, (r k + 1) : ℕ) : ℝ) * (2 ^ (∑ k, r k) * B))`
- **What**: Let f be an integer polynomial with coefficients of absolute value at most A, and P an integer polynomial in the variables X_k (k ∈ σ) with deg_{X_k} P ≤ r_k and coefficients of absolute value at most B. For every multi-index j, every coefficient of the remainder of the diagonal substitution Δ_j P(x, …, x) on division by f (Lean `modByMonic`) has absolute value at most (1 + A)^{∑ r_k + 1 − deg f} · ∏_k (r_k + 1) · 2^{∑ r_k} · B. This is the explicit remainder bound of §6, proof of Lemma 9: abc(Δ_j W) ≤ 2^{∑ r_j} B_1, the diagonal substitution multiplies by at most the number of terms, and each leading-term elimination by f multiplies by at most 1 + A.
- **How**: `hB : 0 ≤ B` from `hc 0`; `hdP` degree bounds for `hasseDeriv j P` via `MvPolynomial.degreeOf_hasseDeriv_le`; `hsupp` bounds `#support (hasseDeriv j P)` by ∏ (r_k + 1) via `Roth.card_le_card_box` and mathlib's `MvPolynomial.monomial_le_degreeOf`; `hcD` bounds the coefficients of `diag (hasseDeriv j P)` by chaining `Roth.abs_coeff_diag_le` with `Roth.abs_coeff_hasseDeriv_le` and `mul_le_mul_of_nonneg_right hsupp`; the conclusion is `Roth.norm_coeff_modByMonic_le` (over the seminormed ring ℤ) with degree bound `Roth.natDegree_diag_le`, transported from ‖·‖ to |·| by `simpa only [Int.norm_eq_abs, Nat.cast_prod, Nat.cast_add, Nat.cast_one]`.
- **Hypotheses**: `hA` (coefficient bound for the divisor, fed to `norm_coeff_modByMonic_le`), `hd` (degree bounds, needed by `abs_coeff_hasseDeriv_le`, the support count and `natDegree_diag_le`), `hc` (coefficient bound for P, also gives `0 ≤ B`). No monicity of f is required (for nonmonic f, `modByMonic` returns the dividend, handled inside `norm_coeff_modByMonic_le`). All hypotheses are used; none is redundant.
- **Uses from project**: `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210), `Roth.card_le_card_box` (Roth/Box.lean:65), `Roth.abs_coeff_diag_le` (Roth/CoeffNorm.lean:174), `Roth.abs_coeff_hasseDeriv_le` (Roth/CoeffNorm.lean:134), `Roth.natDegree_diag_le` (Roth/CoeffNorm.lean:183), `Roth.norm_coeff_modByMonic_le` (Roth/MainLemma.lean:252).
- **Used by**: Roth/MainLemma.lean:533 `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` (private, l.515), inside its local `bound` helper (first `calc` step), applied both to f and, in the nonmonic degree-zero case, to g := 0. Transitively: floor_aux → `exists_mem_RSet_le_index_of_rpow_bound_aux` (l.581, use at l.606) → `exists_mem_RSet_le_index_of_log_bound_aux` (l.618) → `exists_auxiliary_polynomial_of_log_bound_aux` (l.643) → `main_lemma`. `grep -rn abs_coeff_diag_hasseDeriv_modByMonic_le_aux Roth/` gives only the definition (l.497) and the use at l.533.
- **Visibility**: private
- **Lines**: 497–513, proof length 12 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`. The non-simplified product form of the bound is deliberate: the caller bounds each of the three factors by β separately (`mul_le_mul he (mul_le_mul hNR ...)`).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:533 in `abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`, which feeds the remainder bound C of the Siegel-type counting step of Lemma 9.
- Wrapper of 1–2 mathlib calls? No. It composes five project lemmas (`abs_coeff_hasseDeriv_le`, `card_le_card_box`, `abs_coeff_diag_le`, `natDegree_diag_le`, `norm_coeff_modByMonic_le`) plus `degreeOf_hasseDeriv_le` and mathlib's `monomial_le_degreeOf`.
- Does mathlib have it? No. Mathlib's `hasseDeriv` exists only for one-variable `Polynomial` and `LaurentSeries` (`grep -rln hasseDeriv .lake/packages/mathlib/Mathlib`: Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean); there is no diagonal-substitution map `MvPolynomial σ ℤ → Polynomial ℤ` named as such, and no coefficient-norm bound for `modByMonic` (`grep -rn modByMonic Mathlib | grep -i "norm\|abs\|coeff_le"`: no hits). The statement is a Roth-specific composite.
- Too specific (inline?)? Specific to one call site; it could be inlined into the `bound` helper of floor_aux, but that helper already handles the rounding/β-absorption and the monic/nonmonic case split, and inlining would merge the exact Lemma 9 coefficient estimate with the crude β bookkeeping. The separation (exact bound here, coarse floor bound in the caller) is readable and the lemma is short. Keep factored.
- Well-chosen statement? Yes; minimal hypotheses (notably no `f.Monic`), conclusion shaped to the caller's factor-by-factor estimate.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site (Roth/MainLemma.lean:533); no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:497; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the mathlib-relevant ingredients (`norm_coeff_modByMonic_le`, `abs_coeff_diag_le`, multivariate Hasse derivatives) are assessed under their own entries (see `Roth.norm_coeff_modByMonic_le.md`, `Roth.abs_coeff_diag_le.md`).

## Evidence
- `grep -rn abs_coeff_diag_hasseDeriv_modByMonic_le_aux Roth/`: definition Roth/MainLemma.lean:497, single use Roth/MainLemma.lean:533; caller chain located via `grep -n` (l.515, 581/606, 618/639, 643/653).
- Read the body and the call site (Roth/MainLemma.lean:497–557) and the dependency statements: `norm_coeff_modByMonic_le` (Roth/MainLemma.lean:252), `abs_coeff_hasseDeriv_le`, `diag`, `abs_coeff_diag_le`, `natDegree_diag_le` (Roth/CoeffNorm.lean:134–190, namespace Roth), `card_le_card_box` (Roth/Box.lean:65), `monomial_le_degreeOf` (Mathlib/Algebra/MvPolynomial/Degrees.lean:268).
- `grep -rln hasseDeriv .lake/packages/mathlib/Mathlib`: only the three one-variable / Laurent series files; `grep -rn modByMonic` filtered for norm/abs/coeff bounds: no hits.
- Earlier reports consulted: `Roth.exists_hasseDeriv_index_eval_bound_aux.md` (format), `Roth.norm_coeff_modByMonic_le.md`, `Roth.abs_coeff_diag_le.md` (sibling entries exist).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
