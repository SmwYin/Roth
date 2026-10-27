---
decl: Roth.abs_eval_iterated_hasseDeriv_lt_aux
file: Roth/MainLemma.lean
line: 459
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 value estimate for a doubly Hasse-differentiated integer polynomial at the diagonal point, chaining abs_coeff_hasseDeriv_le twice into abs_eval_le and absorbing 2^s and (1+|alpha|)^s into beta; used once; mathlib has no multivariate Hasse derivative.
action: Keep as private helper of its single call site Roth/MainLemma.lean:668 (exists_auxiliary_polynomial_of_log_bound_aux); no change.
---

# Roth.abs_eval_iterated_hasseDeriv_lt_aux

## Inventory entry

### `theorem Roth.abs_eval_iterated_hasseDeriv_lt_aux`
- **Type**: `∀ {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {B α β : ℝ} {s : ℕ}, (∀ j, degreeOf j P ≤ r j) → 0 < B → ∑ j, r j ≤ s → (2 : ℝ) ^ s < β → (1 + |α|) ^ s ≤ β → (∀ d, |(P.coeff d : ℝ)| ≤ B) → ∀ i k : σ →₀ ℕ, |eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))| < β * (β * B) * β`
- **What**: If an integer polynomial P has coordinate degrees deg_{X_j} P ≤ r_j and all coefficients bounded by B > 0, and β exceeds both 2^s and (1+|α|)^s where s ≥ ∑ r_j, then every iterated Hasse derivative Δ_i Δ_k P, evaluated at the diagonal point (α, …, α), has absolute value < β·(β·B)·β, i.e. < B·β³. This is the "|(Δ_i Q)(α, …, α)| < B^{1+3δ}" estimate of §6, Lemma 9, with β = B^δ.
- **How**: (1) `hdQ`: degree bound for Δ_k P from the project lemma `MvPolynomial.degreeOf_hasseDeriv_le` and `hP`. (2) `heval`: the project value bound `Roth.abs_eval_le` applied to Δ_i Δ_k P with degree bound `degreeOf_hasseDeriv_le` ∘ `hdQ` and coefficient bound obtained by applying `Roth.abs_coeff_hasseDeriv_le` twice (giving 2^{∑r}·(2^{∑r}·B)); then `Finset.prod_pow_eq_pow_sum` rewrites ∏_j (1+|α|)^{r_j} to (1+|α|)^{∑ r_j}. (3) `h2'`: 2^{∑ r_j} < β from `pow_le_pow_right₀` and `h2`. (4) Close with `heval.trans_lt` and `mul_lt_mul_of_nonneg_of_pos`, whose factors come from `mul_lt_mul''` (with `mul_lt_mul_of_pos_right h2' hB`), `pow_le_pow_right₀ (le_add_of_nonneg_right (abs_nonneg α)) hs` chained with `hα`, `positivity`, and `pow_pos`.
- **Hypotheses**: `hP` (coordinate degree bounds; needed for the 2^{∑r} binomial bound and the evaluation bound), `hB : 0 < B` (needed for strictness: with P = 0, B = 0 the conclusion 0 < 0 fails), `hs` (lets the caller use the uniform exponent s = m·r₁), `h2` strict (gives the strict inequality), `hα` (non-strict suffices; caller passes `hα.le`), `hc` (coefficient bound). All are used.
- **Uses from project**: `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210), `Roth.abs_eval_le` (Roth/CoeffNorm.lean:223), `Roth.abs_coeff_hasseDeriv_le` (Roth/CoeffNorm.lean:134).
- **Used by**: Roth/MainLemma.lean:668 `exists_auxiliary_polynomial_of_log_bound_aux` (private), as the last conjunct `∀ i k, |…| < B^{1+3δ}` after `trans_eq` with `hpow : B^{1+3δ} = B·β³`; `grep -rn abs_eval_iterated_hasseDeriv_lt_aux Roth/` gives only the definition (l.459) and that use.
- **Visibility**: private
- **Lines**: 459–476, proof length 14 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem). Name ends in `_aux`. The right-hand side β * (β * B) * β mirrors the shape of the chained bound (2^{∑r}·(2^{∑r}·B))·(1+|α|)^{∑r} so that `mul_lt_mul_of_nonneg_of_pos` / `mul_lt_mul''` apply factorwise; the caller converts it to B^{1+3δ} by `linear_combination`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:668 in `exists_auxiliary_polynomial_of_log_bound_aux`, which feeds the construction of the auxiliary polynomial in the proof of the main lemma (Lemma 9).
- Wrapper of 1–2 mathlib calls? No. It composes three project lemmas (`abs_eval_le`, `abs_coeff_hasseDeriv_le` twice, `degreeOf_hasseDeriv_le` twice) and a four-factor strict-inequality argument.
- Does mathlib have it? No. Mathlib's `hasseDeriv` exists only for one-variable `Polynomial` (Mathlib/Algebra/Polynomial/HasseDeriv.lean, Taylor.lean) and `LaurentSeries`; `grep -rln hasseDeriv .lake/packages/mathlib/Mathlib` lists only those three files, so no multivariate Hasse derivative estimate can be in mathlib. The general ingredient (value bound from coefficient and degree bounds) is `Roth.abs_eval_le`, assessed separately as YES-but-generalise-first; this lemma is a Roth-specific numerical specialisation and not a mathlib candidate.
- Too specific (inline?)? It is specific to Lemma 9, but inlining would put a 14-line inequality chain inside the final `refine` of `exists_auxiliary_polynomial_of_log_bound_aux` under a `fun i k ↦`, hurting readability; the factoring into "analytic estimate" vs "parameter bookkeeping (hpow, three_small_factors)" is sound. Keep factored.
- Well-chosen statement? Yes. Hypotheses are minimal for the conclusion (see Hypotheses); taking the abstract β, s instead of B^δ and m·r₁ keeps the lemma free of rpow and of `mainCoeffBound`. Minor possible polish (not required): state the bound as `B * β ^ 3` directly, which would remove the `linear_combination` at the call site but complicate the internal proof; not worth changing.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:459; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the mathlib-relevant content behind this lemma lives in `Roth.abs_eval_le` (YES-but-generalise-first) and `Roth.abs_coeff_hasseDeriv_le` / `MvPolynomial.degreeOf_hasseDeriv_le`, assessed under their own entries.

## Evidence
- `grep -rn abs_eval_iterated_hasseDeriv_lt_aux Roth/`: definition Roth/MainLemma.lean:459, single use Roth/MainLemma.lean:668.
- Read dependency signatures: `Roth.abs_coeff_hasseDeriv_le` (Roth/CoeffNorm.lean:134), `Roth.abs_eval_le` (Roth/CoeffNorm.lean:223), `MvPolynomial.degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210); namespaces checked (`namespace Roth` at MainLemma.lean:55, `namespace MvPolynomial` at HasseDeriv.lean:45).
- `grep -rln hasseDeriv .lake/packages/mathlib/Mathlib`: only RingTheory/LaurentSeries.lean, Algebra/Polynomial/Taylor.lean, Algebra/Polynomial/HasseDeriv.lean (no multivariate Hasse derivative).
- Earlier report `.mathlib-quality/overview/mathlibable/Roth.abs_eval_le.md` consulted (verdict YES-but-generalise-first, junk KEEP).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
