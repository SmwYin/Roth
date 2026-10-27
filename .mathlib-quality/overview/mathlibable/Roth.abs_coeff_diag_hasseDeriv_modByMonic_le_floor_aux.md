---
decl: Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux
file: Roth/MainLemma.lean
line: 515
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 bookkeeping step absorbing the explicit remainder bound of abs_coeff_diag_hasseDeriv_modByMonic_le_aux into the integer cutoff floor(B beta^3) used by the Siegel counting step; single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:606 (exists_mem_RSet_le_index_of_rpow_bound_aux, inside hC); no change.
---

# Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux

## Inventory entry

### `theorem Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`
- **Type**: `∀ {σ : Type*} [Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ} {r : σ → ℕ} {A B β : ℝ} {s : ℕ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → (∀ k, degreeOf k P ≤ r k) → (∀ d, |(P.coeff d : ℝ)| ≤ B) → ∑ k, r k ≤ s → 2 ^ s ≤ β → (1 + A) ^ s ≤ β → ∀ (j : σ →₀ ℕ) (i : ℕ), |(diag (hasseDeriv j P) %ₘ f).coeff i| ≤ (⌊B * β ^ 3⌋₊ : ℤ)`
- **What**: Let f be an integer polynomial with coefficients bounded in absolute value by A, and P an integer polynomial in variables X_k (k ∈ σ) with deg_{X_k} P ≤ r_k and coefficients bounded by B. If ∑ r_k ≤ s, 2^s ≤ β and (1 + A)^s ≤ β, then for every multi-index j every coefficient of the remainder of the diagonal substitution Δ_j P(x, …, x) on division by f (Lean `modByMonic`) is an integer of absolute value at most ⌊B β³⌋. This is the crude form of the remainder bound in §6, proof of Lemma 9: each of the three factors (1+A)^{…}, ∏(r_k+1), 2^{∑ r_k} of the exact bound is bounded by β, and integrality allows passing to the floor.
- **How**: Derives `0 ≤ B` (from `hc 0`), `1 ≤ β` (via `one_le_pow₀` and `h2`), `2^{∑ r_k} ≤ β` (`pow_le_pow_right₀` with `hs`, then `h2`), and `∏ (r_k + 1) ≤ β` (`Finset.prod_pow_eq_pow_sum`, `Finset.prod_le_prod` with `Nat.lt_two_pow_self`). A local `bound` helper, for an arbitrary divisor g with coefficient bound C and (1+C)^{∑ r_k + 1 − deg g} ≤ β, chains `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` with `mul_le_mul` three times and `ring` to get ≤ B β³. The real bound `hreal` then splits on `f.natDegree = 0`: if f is monic it is 1 (`Polynomial.eq_one_of_monic_natDegree_zero`) and the remainder is 0; if f is not monic `Polynomial.modByMonic_eq_of_not_monic` reduces to the divisor g := 0 with C := 0; otherwise the exponent ∑ r_k + 1 − deg f ≤ s (`lia`) and `pow_le_pow_right₀` plus `hpow` feed `bound hA`. The integer conclusion follows by `simpa` with `Int.natCast_floor_eq_floor`, `Int.le_floor`, `Int.cast_abs`.
- **Hypotheses**: `hA` (divisor coefficient bound; also gives 0 ≤ A for the exponent step), `hd` (degree bounds, passed to the `_aux` lemma), `hc` (coefficient bound for P; gives 0 ≤ B), `hs` (links ∑ r_k to s), `h2` (gives β ≥ 1 and absorbs 2^{∑ r_k} and ∏ (r_k+1)), `hpow` (absorbs the elimination factor in the deg f ≥ 1 case). All are used. `h2` is not derivable from `hpow` in general (needs A ≥ 1, which the caller gets from monicity). No `f.Monic` hypothesis; the nonmonic branch exists only for generality, since the sole caller has `hf : f.Monic` (adding it would save about 3 lines but narrow the statement, not worth it).
- **Uses from project**: `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` (Roth/MainLemma.lean:497). All other names are mathlib (`one_le_pow₀`, `pow_le_pow_right₀`, `Finset.prod_pow_eq_pow_sum`, `Finset.prod_le_prod`, `Nat.lt_two_pow_self`, `mul_le_mul`, `mul_le_mul_of_nonneg_right`, `Polynomial.eq_one_of_monic_natDegree_zero`, `Polynomial.modByMonic_eq_of_not_monic`, `le_add_of_nonneg_right`, `Int.natCast_floor_eq_floor`, `Int.le_floor`, `Int.cast_abs`).
- **Used by**: Roth/MainLemma.lean:606 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (private, l.581), in its `hC` step, composed with `Nat.floor_mono hpow` to bound the remainders by ⌊B^c⌋₊. Transitively: → `exists_mem_RSet_le_index_of_log_bound_aux` (l.618) → `exists_auxiliary_polynomial_of_log_bound_aux` → `main_lemma`. `grep -rn abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux Roth/` gives only the definition (l.515) and the use (l.606).
- **Visibility**: private
- **Lines**: 515–548, proof length 29 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`. The conclusion is phrased over ℤ with a ℕ-floor cast because the caller and `exists_mem_RSet_le_index_aux` work with an integer cutoff `(C : ℤ)`, `C : ℕ`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:606 in `exists_mem_RSet_le_index_of_rpow_bound_aux`, producing the hypothesis `hC` (remainder coefficient cutoff) of the pigeonhole step `exists_mem_RSet_le_index_aux`.
- Wrapper of 1–2 mathlib calls? No. It is 29 lines of β-absorption bookkeeping on top of the project lemma `abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, with a three-way case split on the divisor and a real-to-integer floor transfer.
- Does mathlib have it? No. Mathlib has no multivariate Hasse derivative (`hasseDeriv` only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean), no diagonal substitution map, and no coefficient bound for `modByMonic` (checked for the sibling `_aux` lemma; same searches apply). The specific β-cutoff form is Roth-specific.
- Too specific (inline?)? It has one call site and could be inlined into `hC` of the caller, but the caller is already a long orchestration lemma (counting, pigeonhole, choice of J); inlining 29 lines of numeric bookkeeping there would hurt readability. Keeping it separate mirrors the paper's "the coefficients of the remainders are at most B_1^{1+3δ}" step. Keep factored.
- Well-chosen statement? Yes. Hypotheses are minimal for the stated generality (no monicity needed); the β-form decouples the estimate from the specific choice β = B^δ made in the caller. A possible minor variant (state the real bound `≤ B * β ^ 3` and let the caller floor) would move the floor transfer to the caller without saving anything overall.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site Roth/MainLemma.lean:606; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:515; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the mathlib-relevant ingredients (`norm_coeff_modByMonic_le`, `abs_coeff_diag_le`, multivariate Hasse derivatives) are assessed under their own entries.

## Evidence
- `grep -rn abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux Roth/`: definition Roth/MainLemma.lean:515, single use Roth/MainLemma.lean:606.
- Read the body (Roth/MainLemma.lean:515–548), the dependency `abs_coeff_diag_hasseDeriv_modByMonic_le_aux` (l.497–513) and the call site (l.581–616).
- Located mathlib lemmas used: `Polynomial.eq_one_of_monic_natDegree_zero` (Mathlib/Algebra/Polynomial/Degree/Operations.lean:495), `Polynomial.modByMonic_eq_of_not_monic` (Mathlib/Algebra/Polynomial/Div.lean:207); project defs `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57).
- Earlier report consulted: `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux.md` (format and mathlib-absence searches for the shared ingredients).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
