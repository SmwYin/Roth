---
decl: Roth.exists_hasseDeriv_index_eval_bound_aux
file: Roth/MainLemma.lean
line: 477
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private final step of Lemma 9 that passes from the auxiliary polynomial W to a nonvanishing Hasse derivative Q = Delta_k W, transporting degree, index-gap and value bounds across the Int-to-Real coefficient map; used once by main_lemma; mathlib has no multivariate Hasse derivative or index.
action: Keep as private helper of its single call site Roth/MainLemma.lean:752 (main_lemma); no change.
---

# Roth.exists_hasseDeriv_index_eval_bound_aux

## Inventory entry

### `theorem Roth.exists_hasseDeriv_index_eval_bound_aux`
- **Type**: `∀ {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {α z : σ → ℝ} {C γ c : ℝ}, P ≠ 0 → (∀ j, degreeOf j P ≤ r j) → (∀ i k : σ →₀ ℕ, |eval α (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))| < C) → γ ≤ index (map (Int.castRingHom ℝ) P) α r → index (map (Int.castRingHom ℝ) P) z r < c → ∃ Q : MvPolynomial σ ℤ, Q ≠ 0 ∧ (∀ j, degreeOf j Q ≤ r j) ∧ γ - c < index (map (Int.castRingHom ℝ) Q) α r ∧ eval z (map (Int.castRingHom ℝ) Q) ≠ 0 ∧ ∀ i : σ →₀ ℕ, |eval α (hasseDeriv i (map (Int.castRingHom ℝ) Q))| < C`
- **What**: Let P be a nonzero integer polynomial with deg_{X_j} P ≤ r_j, whose iterated Hasse derivatives Δ_i Δ_k P all have absolute value < C at α. If the index of P at α is at least γ and the index of P at z is less than c, then there is a nonzero integer polynomial Q (namely Q = Δ_k P for a suitable k) with the same degree bounds, index at α greater than γ − c, Q(z) ≠ 0, and |Δ_i Q (α)| < C for every i. This is the closing step of §6, proof of Lemma 9: "W* has some derivative Q = Δ_k W* with ∑ k_j/r_j < η such that Q(h/q) ≠ 0", followed by ind(Q) ≥ ind(W*) − ∑ k_j/r_j.
- **How**: (1) `Roth.exists_hasseDeriv_eval_ne_zero` applied to the real image of P (nonzero by `map_ne_zero_iff` with `MvPolynomial.map_injective _ Int.cast_injective`) at z gives k with `weight r k < c` and Δ_k(map P)(z) ≠ 0. (2) `hQev`: rewrite with `MvPolynomial.hasseDeriv_map` to move the Hasse derivative inside the coefficient map. (3) `refine` with Q = Δ_k P: nonzeroness from `hQev` and `map_zero`; degree bounds from `MvPolynomial.degreeOf_hasseDeriv_le` and `hd`; index bound by rewriting `← hasseDeriv_map` and chaining `sub_lt_sub_left hkw γ`, `sub_le_sub_right hγ _` and `Roth.index_sub_weight_le_index_hasseDeriv`; the value bound from `hbound i k` via `simpa [hasseDeriv_map]`.
- **Hypotheses**: `hP` (needed so the real image is nonzero, required by `exists_hasseDeriv_eval_ne_zero`), `hd` (propagated to the degree conjunct), `hbound` (propagated to the value conjunct; the double-derivative form is exactly what the caller's `exists_auxiliary_polynomial_with_index_gap_aux` provides), `hγ` and `hz` (the index gap). All are used; none is redundant.
- **Uses from project**: `Roth.exists_hasseDeriv_eval_ne_zero` (Roth/MainLemma.lean:454; assessed NO-composable-from-mathlib), `Roth.index_sub_weight_le_index_hasseDeriv` (Roth/Index.lean:109), `Roth.index` (Roth/Index.lean:58), `Roth.weight` (Roth/Box.lean:71, implicit through `hkw`), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `MvPolynomial.degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210).
- **Used by**: Roth/MainLemma.lean:752 `Roth.main_lemma` (public, Lemma 9), with γ := gam − eta + c, c := (index W − (gam − eta) + Θ)/2, z := (h_j/q_j)_j, closed by `simpa only [add_sub_cancel_right]`. `grep -rn exists_hasseDeriv_index_eval_bound Roth/` gives only the definition (l.477) and that use.
- **Visibility**: private
- **Lines**: 477–495, proof length 13 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`. The γ/c split (instead of stating the conclusion as `index P α r − c < index Q α r`) lets the caller choose c as the midpoint of the gap and discharge both side conditions by `linarith`; the stronger form would be equally easy to prove but the current shape matches the call site directly.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:752 inside `Roth.main_lemma`, as the final step producing Q from W.
- Wrapper of 1–2 mathlib calls? No. It composes four project lemmas (`exists_hasseDeriv_eval_ne_zero`, `hasseDeriv_map`, `degreeOf_hasseDeriv_le`, `index_sub_weight_le_index_hasseDeriv`) and packages a five-part conclusion.
- Does mathlib have it? No. Mathlib's `hasseDeriv` exists only for one-variable `Polynomial` and `LaurentSeries` (`grep -rln hasseDeriv .lake/packages/mathlib/Mathlib` lists only Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean), and there is no weighted vanishing index of a multivariate polynomial; the statement is specific to Roth's Lemma 9.
- Too specific (inline?)? It is specific to the single call site, but inlining would place the 13-line derivative-selection argument inside `main_lemma`, mixing it with the γ/c parameter bookkeeping there; the factoring (abstract "pass to a nonvanishing derivative" step vs. concrete numerics) improves readability of the main theorem. Keep factored.
- Well-chosen statement? Yes; hypotheses are minimal and the conclusion exactly matches `main_lemma`'s conclusion after substitution. Possible optional polish only: replace γ by the index of P itself (conclusion `index P α r − c < index Q α r`), which would drop `hγ` but force the caller to add a `lt_of_le_of_lt`; not worth changing.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:477; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the mathlib-relevant ingredients behind this lemma (multivariate Hasse derivatives in Roth/HasseDeriv.lean, the index and `index_sub_weight_le_index_hasseDeriv` in Roth/Index.lean, `exists_hasseDeriv_eval_ne_zero`) are assessed under their own entries.

## Evidence
- `grep -rn exists_hasseDeriv_index_eval_bound Roth/`: definition Roth/MainLemma.lean:477, single use Roth/MainLemma.lean:752.
- Read the body and the call site (Roth/MainLemma.lean:728–773); read dependency locations: `index` (Roth/Index.lean:58, namespace Roth at l.48), `index_sub_weight_le_index_hasseDeriv` (Roth/Index.lean:109), `weight` (Roth/Box.lean:71, namespace Roth), `hasseDeriv_map` (Roth/HasseDeriv.lean:134) and `degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210) in namespace MvPolynomial.
- `grep -rln hasseDeriv .lake/packages/mathlib/Mathlib`: only the three one-variable / Laurent series files (no multivariate Hasse derivative).
- Earlier reports consulted: `Roth.exists_hasseDeriv_eval_ne_zero.md`, `Roth.abs_eval_iterated_hasseDeriv_lt_aux.md` (format and sibling verdicts).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
