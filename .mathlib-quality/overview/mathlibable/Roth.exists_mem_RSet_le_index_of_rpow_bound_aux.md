---
decl: Roth.exists_mem_RSet_le_index_of_rpow_bound_aux
file: Roth/MainLemma.lean
line: 581
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 numeric assembly (C := floor B^c, J := low-weight box indices, counting via pigeonhole_count) feeding exists_mem_RSet_le_index_aux; single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:639 (exists_mem_RSet_le_index_of_log_bound_aux); optionally add a docstring citing paper section 6 Lemma 9; no other change.
---

# Roth.exists_mem_RSet_le_index_of_rpow_bound_aux

## Inventory entry

### `theorem Roth.exists_mem_RSet_le_index_of_rpow_bound_aux`
- **Type**: `∀ {f : Polynomial ℤ} {α A : ℝ}, f.Monic → Polynomial.aeval α f = 0 → (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∀ {c β : ℝ} {B s : ℕ}, 0 < B → ∑ j, r j ≤ s → (1 + A) ^ s ≤ β → (B : ℝ) * β ^ 3 ≤ (B : ℝ) ^ c → ∃ P : MvPolynomial (Fin m) ℤ, P ∈ RSet B r ∧ ((m : ℝ) - 4 * c * f.natDegree * √(m : ℝ)) / 2 ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r`
- **What**: Let f be a monic integer polynomial with root α and coefficients bounded in absolute value by A. Let m ≥ 1, r_1, …, r_m ≥ 1 with ∑ r_j ≤ s, let B ≥ 1 be an integer, and let β, c be reals with (1+A)^s ≤ β and B·β³ ≤ B^c. Then there is a nonzero integer polynomial P in X_1, …, X_m with deg_{X_j} P ≤ r_j and coefficients bounded by B (P ∈ RSet B r) whose index at (α, …, α) relative to r is at least (m − 4c·deg f·√m)/2. This is the numerical core of §6, proof of Lemma 9 (the auxiliary polynomial via Siegel's lemma), with the exponent c left abstract (the caller takes c = 1 + 3δ, β = B^δ).
- **How**: First derives 1 ≤ A (from the leading coefficient 1, `hf.coeff_natDegree`), 2^s ≤ β (`pow_le_pow_left₀`), and 1 ≤ c by contradiction (if c < 1 then B^c ≤ B by `Real.rpow_le_rpow_of_exponent_le`, while β > 1 forces B < B·β³ ≤ B^c, using `one_lt_pow₀`, `lt_mul_of_one_lt_right`, and s > 0 from `Finset.single_le_sum`). Sets C := ⌊B^c⌋₊ and bounds every remainder coefficient of diag(Δ_j W) mod f for W ∈ `boxFamily r B` by C via `abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` followed by `Nat.floor_mono hpow`. Sets J := box multi-indices of weight ≤ (m − 4c·deg f·√m)/2, gets c·deg f·|J| ≤ ∏(r_j+1)/2 from `mul_card_filter_weight_le_aux`, converts it into the counting inequality by `pigeonhole_count`, and closes with `exists_mem_RSet_le_index_aux` (J covers weight < γ via `Finset.mem_filter`, `mem_box`).
- **Hypotheses**: `hf`, `hfα` (passed to `exists_mem_RSet_le_index_aux`); `hA` (coefficient bound for the remainder estimate, and gives 1 ≤ A); `hm`, `hr` (for `mul_card_filter_weight_le_aux` and to get s > 0); `hB` (B > 0 for `pigeonhole_count` and for the c ≥ 1 argument); `hs`, `hAβ` (remainder estimate and 2^s ≤ β); `hpow` (C bound and c ≥ 1). All are used; `1 ≤ c` is derived rather than assumed, which is a nice touch.
- **Uses from project**: `Roth.RSet` (Roth/Theta.lean:56), `Roth.index` (Roth/Index.lean:58), `Roth.boxFamily` (Roth/MainLemma.lean:275), `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.box` (Roth/Box.lean:47), `Roth.mem_box` (Roth/Box.lean:51), `Roth.weight` (Roth/Box.lean:71), `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` (Roth/MainLemma.lean:515), `Roth.mul_card_filter_weight_le_aux` (Roth/MainLemma.lean:569), `Roth.pigeonhole_count` (Roth/MainLemma.lean:334), `Roth.exists_mem_RSet_le_index_aux` (Roth/MainLemma.lean:550). Mathlib names used: `Polynomial.Monic.coeff_natDegree`, `pow_le_pow_left₀`, `Real.rpow_le_rpow_of_exponent_le`, `Finset.single_le_sum`, `one_lt_pow₀`, `lt_mul_of_one_lt_right`, `Nat.floor_mono`, `Finset.prod_pos`, `Finset.mem_filter`, `Nat.cast_pos`.
- **Used by**: Roth/MainLemma.lean:639 `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (private, l.619), with B := mainCoeffBound δ q₁ r₁, c := 1 + 3δ, β := B^δ. Transitively: → `exists_auxiliary_polynomial_of_log_bound_aux` → `exists_auxiliary_polynomial_with_index_gap_aux` → main lemma. `grep -rn exists_mem_RSet_le_index_of_rpow_bound_aux Roth/` gives only l.581 (definition) and l.639 (use).
- **Visibility**: private
- **Lines**: 581–617, proof length 31 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. Specialised to `Fin m` variables (needed by `mul_card_filter_weight_le_aux`, whose weight count is over `Fin m`).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:639 in `exists_mem_RSet_le_index_of_log_bound_aux`.
- Wrapper of 1–2 mathlib calls? No. It is a 31-line assembly of four project lemmas (`abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux`, `mul_card_filter_weight_le_aux`, `pigeonhole_count`, `exists_mem_RSet_le_index_aux`) plus the derivation of 1 ≤ c.
- Does mathlib have it? No. It is stated in terms of the project-defined index, RSet, box weight and multivariate Hasse derivatives (mathlib has `hasseDeriv` only for univariate `Polynomial` and no index notion). Siegel's lemma in mathlib (`Mathlib/NumberTheory/SiegelsLemma.lean`, `Int.Matrix.exists_ne_zero_int_vec_norm_le`) is a linear-algebra statement with a different shape; the project's pigeonhole route is specific to the Roth argument.
- Too specific (inline?)? Single call site, but the caller (`exists_mem_RSet_le_index_of_log_bound_aux`) does the separate job of translating the log hypothesis into the rpow bound via `three_small_factors`; merging would produce a ~55-line proof mixing two unrelated numeric phases. The abstract c, β, s parametrisation cleanly isolates the Lemma 9 counting argument. Keep factored.
- Well-chosen statement? Yes. Hypotheses are minimal for the composed lemmas; 1 ≤ c is derived internally rather than assumed. A docstring citing §6 Lemma 9 would be a small improvement.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site Roth/MainLemma.lean:639; optionally add a short docstring.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:581; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable ingredients (`pigeonhole_count`, `boxFamily`, multivariate `hasseDeriv`, `index`, `RSet`) are assessed under their own entries.

## Evidence
- `grep -rn exists_mem_RSet_le_index_of_rpow_bound_aux Roth/`: definition Roth/MainLemma.lean:581, single use Roth/MainLemma.lean:639.
- Read the body (Roth/MainLemma.lean:581–617), the composed lemmas (`pigeonhole_count` l.334, `abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` l.515, `exists_mem_RSet_le_index_aux` l.550, `mul_card_filter_weight_le_aux` l.569) and the call site (l.619–643).
- Located project defs by grep: `index` (Roth/Index.lean:58), `RSet` (Roth/Theta.lean:56), `weight`/`box`/`mem_box` (Roth/Box.lean:71/47/51), `diag` (Roth/CoeffNorm.lean:161), `boxFamily` (Roth/MainLemma.lean:275), `hasseDeriv` (Roth/HasseDeriv.lean:57), `mainCoeffBound`/`gam`/`lam` (Roth/MainLemma.lean:69/63/60).
- Earlier report consulted: `Roth.exists_mem_RSet_le_index_aux.md` (format; mathlib absence of multivariate Hasse derivatives and index).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
