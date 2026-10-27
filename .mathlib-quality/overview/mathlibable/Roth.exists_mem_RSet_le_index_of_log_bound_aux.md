---
decl: Roth.exists_mem_RSet_le_index_of_log_bound_aux
file: Roth/MainLemma.lean
line: 618
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 specialisation (B := mainCoeffBound, c := 1 + 3 delta, beta := B^delta) turning the log hypothesis (32 without the alpha term) into the rpow bound for exists_mem_RSet_le_index_of_rpow_bound_aux; single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:653 (exists_auxiliary_polynomial_of_log_bound_aux); optionally deduplicate the hpow identity and the 0 < r1 derivation that the caller repeats at l.656-665; no other change.
---

# Roth.exists_mem_RSet_le_index_of_log_bound_aux

## Inventory entry

### `theorem Roth.exists_mem_RSet_le_index_of_log_bound_aux`
- **Type**: `∀ {f : Polynomial ℤ} {α A : ℝ}, f.Monic → Polynomial.aeval α f = 0 → (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m q₁ r₁ : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∑ j, r j ≤ m * r₁ → ∀ {δ : ℝ}, 0 ≤ δ → 2 * m + 1 + 2 * m * Real.log (1 + A) ≤ δ ^ 2 * Real.log q₁ → ∃ P : MvPolynomial (Fin m) ℤ, P ∈ RSet (mainCoeffBound δ q₁ r₁) r ∧ gam δ f.natDegree m ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r`
- **What**: Let f be a monic integer polynomial with root α and coefficients bounded in absolute value by A. Let m ≥ 1, r_1, …, r_m ≥ 1 with ∑ r_j ≤ m·r₁, δ ≥ 0, and assume 2m + 1 + 2m·log(1+A) ≤ δ²·log q₁ (the part of the paper's condition (32) not involving α). Then there is a nonzero integer polynomial P in X_1, …, X_m with deg_{X_j} P ≤ r_j and coefficients bounded by B₁ = ⌊q₁^{δ r₁}⌋ (P ∈ RSet B₁ r) whose index at (α, …, α) relative to r is at least γ = (m − 4(1+3δ)·deg f·√m)/2. This is §6, Lemma 9 (auxiliary polynomial via Siegel/pigeonhole) with the paper's concrete parameters plugged in.
- **How**: Derives 1 ≤ A from the leading coefficient (`Polynomial.Monic.coeff_natDegree`), r₁ > 0 from `Finset.single_le_sum` and `Nat.pos_of_mul_pos_left`, and 3 ≤ δ² log q₁ by `nlinarith` (using `Real.log_nonneg`). Gets (1+A)^{m r₁} < B₁^δ from `three_small_factors` (with α := 0, so the α-term vanishes by `simpa`), proves the identity B₁^{1+3δ} = B₁·(B₁^δ)³ via `Real.rpow_add_of_nonneg`, `Real.rpow_one`, `Real.rpow_mul_natCast`, and B₁ > 0 via `Nat.floor_pos` and `four_lt_rpow`; then closes with `exists_mem_RSet_le_index_of_rpow_bound_aux` (B := B₁, c := 1 + 3δ, β := B₁^δ, s := m r₁), unfolding `gam`, `lam`.
- **Hypotheses**: `hf`, `hfα`, `hA`, `hm`, `hr`, `hs` (all passed to `exists_mem_RSet_le_index_of_rpow_bound_aux`; `hA` also gives 1 ≤ A, `hm`/`hr`/`hs` also give r₁ > 0); `hδ0` (for `three_small_factors`, `four_lt_rpow`, and rpow positivity); `hL` (for `three_small_factors` and for 3 ≤ δ² log q₁). All used.
- **Uses from project**: `Roth.RSet` (Roth/Theta.lean:56), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.lam` (Roth/MainLemma.lean:60), `Roth.index` (Roth/Index.lean:58), `Roth.three_small_factors` (Roth/MainLemma.lean:180), `Roth.four_lt_rpow` (Roth/MainLemma.lean:122), `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (Roth/MainLemma.lean:581). Mathlib names used: `Polynomial.Monic.coeff_natDegree`, `Nat.pos_of_mul_pos_left`, `Finset.single_le_sum`, `Real.log_nonneg`, `Real.rpow_add_of_nonneg`, `Real.rpow_one`, `Real.rpow_mul_natCast`, `Nat.floor_pos`, `MvPolynomial.map`, `Int.castRingHom`.
- **Used by**: Roth/MainLemma.lean:653 `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (private, l.643), which first weakens its full (32) hypothesis (with the α-term) to this one's `hL`. Transitively → `exists_auxiliary_polynomial_with_index_gap_aux` (l.692) → main lemma. `grep -rn exists_mem_RSet_le_index_of_log_bound_aux Roth/` gives only l.618 (definition) and l.653 (use).
- **Visibility**: private
- **Lines**: 618–641, proof length 18 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. The caller repeats three pieces of this proof: the r₁ > 0 derivation (l.656–658 vs l.625–626), a second `three_small_factors` call (l.656 vs l.631), and the identical `hpow` rpow identity (l.662–665 vs l.633–637).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:653 in `exists_auxiliary_polynomial_of_log_bound_aux`.
- Wrapper of 1–2 mathlib calls? No. It is an 18-line parameter specialisation combining three project lemmas (`three_small_factors`, `four_lt_rpow`, `exists_mem_RSet_le_index_of_rpow_bound_aux`) with an rpow identity and two small numeric derivations.
- Does mathlib have it? No. The statement is in terms of the project-defined `index`, `RSet`, `mainCoeffBound`, `gam` and multivariate Hasse-derivative machinery, none of which mathlib has; mathlib's Siegel lemma (`Mathlib/NumberTheory/SiegelsLemma.lean`) is a linear-algebra statement of a different shape. No search could plausibly hit this Roth-specific numeric specialisation.
- Too specific (inline?)? Single call site, and there is some duplication with the caller (r₁ > 0, `three_small_factors`, `hpow`, about 8 lines). Inlining would remove that duplication but give a ~40-line caller mixing the Lemma 9 existence step with the coefficient-of-derivative bounds; the current split (existence-with-index here, extra derivative bound in the caller) mirrors the paper. Keeping it factored is reasonable; the cheaper improvement is to share the `hpow` identity (e.g. a small private lemma `mainCoeffBound ^ (1 + 3δ) = B * (B^δ)^3`) or have this lemma also return the facts the caller recomputes.
- Well-chosen statement? Yes. Hypotheses are exactly those needed; `hL` deliberately omits the α-term (only the A-term is needed for existence), which is the minimal form. A docstring citing §6 Lemma 9 would help.
- Conclusion: `KEEP`. Action: keep as private helper of Roth/MainLemma.lean:653; optionally deduplicate the `hpow` identity and r₁ > 0 derivation repeated in the caller at l.656–665.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:618; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable ingredients (`index`, `RSet`, multivariate `hasseDeriv`, `pigeonhole_count`, `three_small_factors`, `four_lt_rpow`) are assessed under their own entries.

## Evidence
- `grep -rn exists_mem_RSet_le_index_of_log_bound_aux Roth/`: definition Roth/MainLemma.lean:618, single use Roth/MainLemma.lean:653.
- Read the body (Roth/MainLemma.lean:618–641), the callee `exists_mem_RSet_le_index_of_rpow_bound_aux` (l.581–616), the caller (l.643–669), `four_lt_rpow` (l.122) and `three_small_factors` (l.180).
- Located project defs by grep: `lam`/`gam`/`mainCoeffBound` (Roth/MainLemma.lean:60/63/69), `index` (Roth/Index.lean:58), `RSet` (Roth/Theta.lean:56).
- Earlier report consulted: `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux.md` (format, mathlib absence of the index/RSet machinery).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
