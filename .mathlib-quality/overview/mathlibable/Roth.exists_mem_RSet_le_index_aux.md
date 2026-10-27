---
decl: Roth.exists_mem_RSet_le_index_aux
file: Roth/MainLemma.lean
line: 550
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Lemma 9 assembly step (pigeonhole pair W' ne W'' gives W* = W' - W'' in RSet with index at least gamma) chaining four public project lemmas; single call site; Roth-specific, nothing in mathlib.
action: Keep as private helper of its single call site Roth/MainLemma.lean:613 (exists_mem_RSet_le_index_of_rpow_bound_aux); no change.
---

# Roth.exists_mem_RSet_le_index_aux

## Inventory entry

### `theorem Roth.exists_mem_RSet_le_index_aux`
- **Type**: `∀ {σ : Type*} [Fintype σ] {f : Polynomial ℤ} {α : ℝ}, f.Monic → Polynomial.aeval α f = 0 → ∀ (r : σ → ℕ) (B C : ℕ) (J : Finset (σ →₀ ℕ)) {γ : ℝ}, (∀ W ∈ boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(diag (hasseDeriv j W) %ₘ f).coeff i| ≤ (C : ℤ)) → ((2 * C + 1 : ℕ) : ℝ) ^ (f.natDegree * J.card) < ((B : ℝ) + 1) ^ (∏ k, (r k + 1) : ℕ) → (∀ d, (∀ k, d k ≤ r k) → weight r d < γ → d ∈ J) → ∃ P : MvPolynomial σ ℤ, P ∈ RSet B r ∧ γ ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r`
- **What**: Let f be a monic integer polynomial with root α, and 𝒲 the family of integer polynomials in the variables X_k (k ∈ σ) with deg_{X_k} ≤ r_k and coefficients in [0, B]. Suppose that for every W ∈ 𝒲 and every multi-index j ∈ J, the coefficients of the remainder of Δ_j W(x, …, x) on division by f are bounded by C, and that the counting inequality (2C+1)^{deg f · |J|} < (B+1)^{∏(r_k+1)} holds. If J contains every box multi-index of weight < γ, then there is a nonzero integer polynomial P with deg_{X_k} P ≤ r_k and coefficients bounded by B (i.e. P ∈ RSet B r) whose index at (α, …, α) relative to r is at least γ. This is the core of §6, proof of Lemma 9 (Siegel's lemma by pigeonhole): two distinct W', W'' with equal remainders, W* = W' − W''.
- **How**: `exists_ne_modByMonic_eq` (with `hcount` converted from `∏` to `∏ᶠ` via `finprod_eq_prod_of_fintype`) yields W' ≠ W'' in `boxFamily r B` with equal remainders for all j ∈ J; `sub_mem_RSet` gives W' − W'' ∈ RSet B r; `le_index_of_forall_eval_eq_zero` closes the index bound, fed with nonvanishing of the real image (`map_ne_zero_iff` + `MvPolynomial.map_injective` + `Int.cast_injective`), the degree bounds transported along the injective cast (`degreeOf`, `MvPolynomial.degrees_map_of_injective`), and the vanishing of Δ_d(W' − W'') at (α, …, α) for box d of weight < γ from `eval_hasseDeriv_sub_eq_zero` applied to `hWeq d (hJ d hd hw)`.
- **Hypotheses**: `hf` (monicity, needed by `exists_ne_modByMonic_eq`), `hfα` (α a root, used by `eval_hasseDeriv_sub_eq_zero`), `hC` and `hcount` (pigeonhole inputs to `exists_ne_modByMonic_eq`), `hJ` (J covers all box multi-indices of weight < γ). All are used; none is redundant.
- **Uses from project**: `Roth.boxFamily` (Roth/MainLemma.lean:275), `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.weight` (Roth/Box.lean:71), `Roth.RSet` (Roth/Theta.lean:56), `Roth.index` (Roth/Index.lean:58), `Roth.exists_ne_modByMonic_eq` (Roth/MainLemma.lean:359), `Roth.sub_mem_RSet` (Roth/MainLemma.lean:388), `Roth.le_index_of_forall_eval_eq_zero` (Roth/MainLemma.lean:419), `Roth.eval_hasseDeriv_sub_eq_zero` (Roth/MainLemma.lean:402). Mathlib names used: `finprod_eq_prod_of_fintype`, `map_ne_zero_iff`, `MvPolynomial.map_injective`, `Int.cast_injective`, `MvPolynomial.degreeOf`, `MvPolynomial.degrees_map_of_injective`.
- **Used by**: Roth/MainLemma.lean:613 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (private, l.581), as its final step with C := ⌊B^c⌋₊, J := box multi-indices of weight ≤ (m − 4c·deg f·√m)/2, and `hcount` from `pigeonhole_count`. Transitively: → `exists_mem_RSet_le_index_of_log_bound_aux` → `exists_auxiliary_polynomial_of_log_bound_aux` → `main_lemma`. `grep -rn exists_mem_RSet_le_index_aux Roth/` gives only l.550 (definition) and l.613 (use).
- **Visibility**: private
- **Lines**: 550–567, proof length 11 lines
- **Notes**: Declared `private lemma` (kind recorded as theorem); name ends in `_aux`; no docstring. Generic in the variable type σ (only `Fintype σ` needed, to state the product and the index), while the sole caller specialises to `Fin m`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:613, the closing `exact` of `exists_mem_RSet_le_index_of_rpow_bound_aux`.
- Wrapper of 1–2 mathlib calls? No. It composes four project lemmas (`exists_ne_modByMonic_eq`, `sub_mem_RSet`, `le_index_of_forall_eval_eq_zero`, `eval_hasseDeriv_sub_eq_zero`) plus cast-transport glue; none of these are mathlib.
- Does mathlib have it? No. The statement involves the project-defined index, RSet, box weight, diagonal substitution and multivariate Hasse derivatives; mathlib has no multivariate Hasse derivative (`hasseDeriv` exists only for `Polynomial`) and no index notion. The underlying combinatorial principle (pigeonhole, `Fintype.exists_ne_map_eq_of_card_lt`) is already used inside `exists_ne_modByMonic_eq`.
- Too specific (inline?)? Single call site and only 11 lines, so inlining into `exists_mem_RSet_le_index_of_rpow_bound_aux` is possible. However it cleanly separates the algebraic "pigeonhole pair gives a vanishing polynomial" step (paper: "W* ... index at least γ") from the numeric choice of C, J and the counting in the caller, which is already ~35 lines; it is stated in arbitrary σ and arbitrary J, γ, which documents exactly what the argument needs. Keep factored.
- Well-chosen statement? Yes. Hypotheses are exactly the inputs of the composed lemmas; the `∏` (rather than `∏ᶠ`) in `hcount` matches the caller's `pigeonhole_count` output. A docstring citing §6 Lemma 9 would be a small improvement but is optional for a private helper.
- Conclusion: `KEEP`. Action: keep as private helper of its single call site Roth/MainLemma.lean:613; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/MainLemma.lean:550; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note: the reusable ingredients (`exists_ne_modByMonic_eq`, `sub_mem_RSet`, `le_index_of_forall_eval_eq_zero`, `eval_hasseDeriv_sub_eq_zero`, multivariate `hasseDeriv`) are assessed under their own entries.

## Evidence
- `grep -rn exists_mem_RSet_le_index_aux Roth/`: definition Roth/MainLemma.lean:550, single use Roth/MainLemma.lean:613.
- Read the body (Roth/MainLemma.lean:550–567), the composed lemmas (l.359–429) and the call site (l.581–616).
- Located project defs by grep: `index` (Roth/Index.lean:58), `RSet` (Roth/Theta.lean:56), `weight` (Roth/Box.lean:71), `diag` (Roth/CoeffNorm.lean:161), `boxFamily` (Roth/MainLemma.lean:275), `hasseDeriv` (Roth/HasseDeriv.lean:57); mathlib `MvPolynomial.degrees_map_of_injective` (Mathlib/Algebra/MvPolynomial/Degrees.lean:196), `MvPolynomial.map_injective` (Mathlib/Algebra/MvPolynomial/Eval.lean:396).
- Earlier report consulted: `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux.md` (format; mathlib-absence of multivariate Hasse derivatives).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
