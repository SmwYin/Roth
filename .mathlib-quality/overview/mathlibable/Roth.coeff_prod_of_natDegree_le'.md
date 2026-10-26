---
decl: Roth.coeff_prod_of_natDegree_le'
file: Roth/Wronskian.lean
line: 93
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private per-index-bound version of the top coefficient of a finite product of polynomials; mathlib's Polynomial.coeff_prod_of_natDegree_le only has a uniform bound n (coefficient at card s * n) and is the special case n i := n, so it does not cover this; used once in coeff_wronskian_of_natDegree_injective.
action: Keep as private helper for Roth/Wronskian.lean:131 (coeff_wronskian_of_natDegree_injective); optional small mathlib PR adding it (generalised to CommSemiring, verified) next to Polynomial.coeff_prod_of_natDegree_le in Mathlib/Algebra/Polynomial/BigOperators.lean.
---

# Roth.coeff_prod_of_natDegree_le'

## Inventory entry

### `theorem Roth.coeff_prod_of_natDegree_le'`
- **Type**: `∀ {K : Type*} [Field K] {ι : Type*} (s : Finset ι) (f : ι → K[X]) (n : ι → ℕ), (∀ i ∈ s, (f i).natDegree ≤ n i) → (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)`
- **What**: If each factor `f i` has degree at most `n i`, then the coefficient of `X^(∑ n i)` in `∏ f i` is the product of the coefficients of `X^(n i)` in the `f i` (the "top" coefficient of a product with per-factor degree bounds).
- **How**: `Finset.induction_on`; empty case `simp`; insert case rewrites with `Finset.prod_insert`, `Finset.sum_insert`, then `Polynomial.coeff_mul_add_eq_of_natDegree_le` applied with the bound `h.1` for the new factor and `(Polynomial.natDegree_prod_le _ _).trans (Finset.sum_le_sum h.2)` for the remaining product, then the induction hypothesis.
- **Hypotheses**: `h : ∀ i ∈ s, (f i).natDegree ≤ n i`; section variable `[Field K]` (only `CommSemiring` is needed, verified in evidence file).
- **Uses from project**: `[]` (only mathlib lemmas; `K[X]` from the section variable `{K : Type*} [Field K]`)
- **Used by**: Roth/Wronskian.lean:131 in `Roth.coeff_wronskian_of_natDegree_injective` (inside the `key` step) only (`grep -rn "coeff_prod_of_natDegree_le'" Roth/`). Transitively: `Roth.wronskian_ne_zero_of_natDegree_injective` (Roth/Wronskian.lean:148, uses it at l.152).
- **Visibility**: private
- **Lines**: 93–103, proof length 8 lines
- **Notes**: Declared with `private lemma` (kind recorded as theorem). The prime in the name distinguishes it from mathlib's `Polynomial.coeff_prod_of_natDegree_le` (opened via `open Polynomial`). No docstring.

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_wronskian_of_natDegree_injective` (Roth/Wronskian.lean:131), where the bounds are `natDegree (hasseDeriv (σ i) (φ i)) ≤ natDegree (φ i) - σ i`, which genuinely differ per index.
- Wrapper of 1–2 mathlib calls? No; it is an 8-line induction built on `coeff_mul_add_eq_of_natDegree_le` and `natDegree_prod_le`.
- Does mathlib have it? Not in this form. Mathlib has `Polynomial.coeff_prod_of_natDegree_le (f : ι → R[X]) (n : ℕ) (h : ∀ p ∈ s, natDegree (f p) ≤ n) : coeff (∏ i ∈ s, f i) (#s * n) = ∏ i ∈ s, coeff (f i) n` (Mathlib/Algebra/Polynomial/BigOperators.lean:230), plus the List/Multiset versions (l.113, l.225) — all with a single uniform bound `n`. That does not cover the project use (bounds `natDegree (φ i) - σ i` vary with `i`); mathlib's lemma is instead the special case `n i := n` of ours (derived in the evidence file via `Finset.sum_const`). loogle `Polynomial.coeff (Finset.prod _ _) (Finset.sum _ _)`: no results; leansearch returns only the uniform-bound lemmas and `MonomialOrder.coeff_mul_of_add_of_degree_le` (binary, MvPolynomial). The closest relatives `leadingCoeff_prod'`/`natDegree_prod'` need exact degrees and nonvanishing leading coefficients, not bounds.
- Too specific (inline)? No: it is a clean general fact; inlining the induction into the `key` step would lengthen an already dense proof.
- Well-chosen? Yes. The statement is the natural per-index generalisation of a mathlib lemma; it could be stated over `CommSemiring` rather than `Field`.
- Conclusion: `KEEP` — action: keep as private helper; optionally upstream as a public generalisation of `Polynomial.coeff_prod_of_natDegree_le` (over `CommSemiring R`) in Mathlib/Algebra/Polynomial/BigOperators.lean, after which the project would call the mathlib name.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Wronskian.lean:93).

Note: although skipped as private, it is a genuine (small) mathlib gap: the per-index-bound generalisation of `Polynomial.coeff_prod_of_natDegree_le`, valid over any `CommSemiring` with the same proof (compiled in the evidence file). If the Wronskian material is upstreamed, this lemma would go with it as a public lemma in Mathlib/Algebra/Polynomial/BigOperators.lean.

## Evidence
- `grep -rn "coeff_prod_of_natDegree_le'" Roth/`: definition l.93, single use l.131.
- `grep -rn coeff_wronskian_of_natDegree_injective Roth/`: used at Roth/Wronskian.lean:152 (`wronskian_ne_zero_of_natDegree_injective`).
- Mathlib grep of Mathlib/Algebra/Polynomial/BigOperators.lean: only uniform-bound `coeff_list_prod_of_natDegree_le` (l.113), `coeff_multiset_prod_of_natDegree_le` (l.225), `coeff_prod_of_natDegree_le` (l.230).
- lean_loogle `Polynomial.coeff (Finset.prod _ _) (Finset.sum _ _)`: no results. lean_leansearch "coefficient of product of polynomials at sum of degree bounds equals product of coefficients": only the uniform-bound lemmas above, `MonomialOrder.coeff_mul_of_add_of_degree_le`, `ComputeDegree.coeff_mul_add_of_le_natDegree_of_eq_ite`.
- Evidence file `.mathlib-quality/overview/evidence/Roth.coeff_prod_of_natDegree_le'/weaken_commsemiring.lean` (imports only `Mathlib.Algebra.Polynomial.BigOperators`; `lake env lean` compiles with no output, 16 s): (1) the project proof verbatim over `[CommSemiring R]`; (2) mathlib's `coeff_prod_of_natDegree_le` recovered as the special case `n i := n` by `simpa [Finset.sum_const, smul_eq_mul]`.
