---
decl: Roth.exists_auxiliary_polynomial_of_log_bound_aux
file: Roth/MainLemma.lean
line: 643
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 assembly step adding the Hasse-derivative evaluation bound B1^(1+3 delta) to the auxiliary polynomial from exists_mem_RSet_le_index_of_log_bound_aux under full hypothesis (32); single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:719 (exists_auxiliary_polynomial_with_index_gap_aux); optionally share the hpow identity and the 0 < r1 derivation duplicated with exists_mem_RSet_le_index_of_log_bound_aux (l.625-637); no other change.
---

# Roth.exists_auxiliary_polynomial_of_log_bound_aux

## Inventory entry

### `theorem Roth.exists_auxiliary_polynomial_of_log_bound_aux`
- **Type**: `∀ {f : Polynomial ℤ} {α A : ℝ}, f.Monic → Polynomial.aeval α f = 0 → (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m q₁ r₁ : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∑ j, r j ≤ m * r₁ → ∀ {δ : ℝ}, 0 ≤ δ → 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log q₁ → ∃ P : MvPolynomial (Fin m) ℤ, P ∈ RSet ((q₁ : ℝ) ^ (δ * r₁)) r ∧ gam δ f.natDegree m ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r ∧ ∀ i k : Fin m →₀ ℕ, |eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))| < (mainCoeffBound δ q₁ r₁ : ℝ) ^ (1 + 3 * δ)`
- **What**: Let f be a monic integer polynomial with root α and coefficients bounded in absolute value by A; let m ≥ 1, r_1, …, r_m ≥ 1 with ∑ r_j ≤ m·r₁, δ ≥ 0, and assume the paper's condition (32): 2m + 1 + 2m·log(1+A) + 2m·log(1+|α|) ≤ δ²·log q₁. Then there is a nonzero integer polynomial P with deg_{X_j} P ≤ r_j and coefficients bounded by q₁^{δ r₁} (P ∈ RSet), whose index at (α, …, α) relative to r is at least γ = (m − 4(1+3δ)·deg f·√m)/2, and such that every iterated Hasse derivative ∂_i ∂_k P evaluated at (α, …, α) is smaller than B₁^{1+3δ} in absolute value, where B₁ = ⌊q₁^{δ r₁}⌋. This is the auxiliary-polynomial part of §6, Lemma 9 together with the derivative-size bound.
- **How**: Obtains P (in RSet B₁ r, index ≥ γ) from `exists_mem_RSet_le_index_of_log_bound_aux`, after dropping the α-term of (32) via `le_add_of_nonneg_right`, `mul_nonneg`, `Real.log_nonneg`. Gets 2^{m r₁} < B₁^δ and (1+|α|)^{m r₁} < B₁^δ from `three_small_factors` (r₁ > 0 via `Finset.single_le_sum`, `Nat.pos_of_mul_pos_left`). Shows B₁ > 0 from a nonzero coefficient of P (`MvPolynomial.exists_coeff_ne_zero`, `abs_pos`, `Int.cast_ne_zero`). Proves B₁^{1+3δ} = B₁·(B₁^δ)³ via `Real.rpow_add_of_nonneg`, `Real.rpow_one`, `Real.rpow_mul_natCast`. Relaxes the coefficient bound from B₁ to q₁^{δ r₁} with `Nat.floor_le`, and bounds the derivatives with `abs_eval_iterated_hasseDeriv_lt_aux` (β := B₁^δ, s := m r₁), closing the equality β·(β·B₁)·β = B₁^{1+3δ} by `linear_combination -hpow`.
- **Hypotheses**: `hf`, `hfα`, `hm`, `hr`, `hs` (passed to `exists_mem_RSet_le_index_of_log_bound_aux`; `hm`/`hr`/`hs` also give r₁ > 0, `hs` also feeds `abs_eval_iterated_hasseDeriv_lt_aux`); `hA` (callee, plus 0 ≤ A for `three_small_factors`); `hδ0` (callee, `three_small_factors`, rpow positivity); `hL` (weakened for the callee; used in full by `three_small_factors` for the α-bound). All used.
- **Uses from project**: `Roth.RSet` (Roth/Theta.lean:56), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.index` (Roth/Index.lean:58), `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57, multivariate), `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (Roth/MainLemma.lean:618), `Roth.three_small_factors` (Roth/MainLemma.lean:180), `Roth.abs_eval_iterated_hasseDeriv_lt_aux` (Roth/MainLemma.lean:459). Mathlib names used: `MvPolynomial.exists_coeff_ne_zero`, `MvPolynomial.map`, `MvPolynomial.eval`, `Int.castRingHom`, `Finset.single_le_sum`, `Nat.pos_of_mul_pos_left`, `Real.log_nonneg`, `Real.rpow_add_of_nonneg`, `Real.rpow_one`, `Real.rpow_mul_natCast`, `Nat.floor_le`, `abs_pos`, `Int.cast_ne_zero`.
- **Used by**: Roth/MainLemma.lean:719 `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (private, l.692), which feeds `Roth.main_lemma` (l.734). `grep -rn exists_auxiliary_polynomial_of_log_bound_aux Roth/` gives only l.643 (definition) and l.719 (use).
- **Visibility**: private
- **Lines**: 643–669, proof length 19 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. Duplication with the callee `exists_mem_RSet_le_index_of_log_bound_aux`: the r₁ > 0 derivation (l.657–658 vs l.625–626), a second `three_small_factors` call (l.656 vs l.631), and the same B^{1+3δ} = B·(B^δ)³ rpow identity (l.662–665 vs l.633–637). The `let β` is only used inside `hpow`. Positivity of B₁ is re-derived here from P ≠ 0 although the callee already establishes it via `Nat.floor_pos`/`four_lt_rpow`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:719 in `exists_auxiliary_polynomial_with_index_gap_aux`.
- Wrapper of 1–2 mathlib calls? No. It is a 19-line assembly of three project lemmas (`exists_mem_RSet_le_index_of_log_bound_aux`, `three_small_factors`, `abs_eval_iterated_hasseDeriv_lt_aux`) plus an rpow identity and positivity/relaxation steps.
- Does mathlib have it? No. The statement is about the project-defined `index`, `RSet`, `mainCoeffBound`, `gam` and multivariate `hasseDeriv`; mathlib has none of these (mathlib's `Polynomial.hasseDeriv` is univariate only, and `Mathlib/NumberTheory/SiegelsLemma.lean` is a linear-algebra statement of a different shape). A Roth-specific numerical specialisation cannot plausibly be in mathlib.
- Too specific (inline?)? Single call site. Inlining into `exists_auxiliary_polynomial_with_index_gap_aux` (already ~27 lines) would give a ~45-line proof mixing the Lemma 9 existence/derivative-bound step with the Lemma 7 index-gap step; the current split matches the paper's structure. Keep factored. The cheaper improvement is deduplication with the callee: either have `exists_mem_RSet_le_index_of_log_bound_aux` also return 0 < B₁ and the `three_small_factors` facts, or extract the `hpow` identity into a small private lemma.
- Well-chosen statement? Yes. Hypotheses are exactly those needed; the conclusion's coefficient bound is stated with the real q₁^{δ r₁} (the form `main_lemma`/`index_le_Θ` consume via `RSet ((q 0 : ℝ) ^ (δ * r 0))`), while the derivative bound uses B₁ = ⌊q₁^{δ r₁}⌋ as in the paper. A docstring citing §6 Lemma 9 would help.
- Conclusion: `KEEP`. Action: keep as private helper of Roth/MainLemma.lean:719; optionally deduplicate the `hpow` identity, r₁ > 0 derivation and B₁ > 0 with the callee at l.618–641.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:643; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable ingredients (`index`, `RSet`, multivariate `hasseDeriv`, `three_small_factors`, `mainCoeffBound`) are assessed under their own entries.

## Evidence
- `grep -rn exists_auxiliary_polynomial_of_log_bound_aux Roth/`: definition Roth/MainLemma.lean:643, single use Roth/MainLemma.lean:719.
- Read the body (Roth/MainLemma.lean:643–669), the callee `exists_mem_RSet_le_index_of_log_bound_aux` (l.618–641), `three_small_factors` (l.180), `abs_eval_iterated_hasseDeriv_lt_aux` (l.459), and the caller chain (l.692–733 and `main_lemma` l.734).
- Located project defs by grep: `lam`/`gam`/`mainCoeffBound` (Roth/MainLemma.lean:60/63/69), `index` (Roth/Index.lean:58), `RSet` (Roth/Theta.lean:56), `hasseDeriv` (Roth/HasseDeriv.lean:57).
- Earlier report consulted: `Roth.exists_mem_RSet_le_index_of_log_bound_aux.md` (format; mathlib absence of the index/RSet machinery).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
