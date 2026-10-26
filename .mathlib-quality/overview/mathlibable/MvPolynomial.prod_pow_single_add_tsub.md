---
decl: MvPolynomial.prod_pow_single_add_tsub
file: Roth/Taylor.lean
line: 92
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private splitting lemma ((single i n + k') - d).prod (α j ^ ·) = α i ^ (n - d i) * (k' - d.erase i).prod (α j ^ ·) for k' i = 0, a 5-line Finsupp ext plus prod_add_index' computation used once in the monomial induction step of coeff_taylor; mathlib has no ready-made form.
action: Keep as private helper for its single call site Roth/Taylor.lean:117 (coeff_taylor_monomial_single_add_aux); if coeff_taylor is upstreamed, carry it along as a private helper beside hasseCoeff_single_add_eq.
---

# MvPolynomial.prod_pow_single_add_tsub

## Inventory entry

### `theorem MvPolynomial.prod_pow_single_add_tsub`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) {i : σ} {n : ℕ} {k' : σ →₀ ℕ}, k' i = 0 → ∀ (d : σ →₀ ℕ), (Finsupp.single i n + k' - d).prod (fun j e ↦ α j ^ e) = α i ^ (n - d i) * (k' - d.erase i).prod (fun j e ↦ α j ^ e)`
- **What**: The evaluated monomial α^(k - d) = ∏_j α_j^(k_j - d_j) splits off the i-th variable: if k = n·e_i + k' with k' not involving i, then α^(k - d) = α_i^(n - d_i) · α^(k' - d') where d' is d with its i-th entry erased.
- **How**: Proves the exponent identity `single i n + k' - d = single i (n - d i) + (k' - d.erase i)` pointwise (`ext j`, case split `eq_or_ne j i`, `simp [*, Finsupp.erase_ne]`), then rewrites with it and closes by `simp [h, Finsupp.prod_add_index', pow_add, -Finsupp.single_tsub]` (the product over a sum of finsupps splits multiplicatively; `Finsupp.prod_single_index` handles the single part; `Finsupp.single_tsub` must be excluded so simp does not split `single i (n - d i)`).
- **Hypotheses**: `hi : k' i = 0` (k' does not involve variable i); `classical`. Only the commutative-monoid structure of R is used (powers and products); `[CommSemiring R]` comes from the section variable.
- **Uses from project**: `[]` (only mathlib `Finsupp` API: `Finsupp.single`, `Finsupp.erase`, `Finsupp.erase_ne`, `Finsupp.prod_add_index'`, `pow_add`, `Finsupp.single_tsub`)
- **Used by**: Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.101; `rw [..., prod_pow_single_add_tsub α hi]` at l.117) only — `grep -rn prod_pow_single_add_tsub Roth/` gives the definition (l.92) and that single use. Transitively: `coeff_taylor_monomial_aux` -> `coeff_taylor` and everything downstream of Taylor's theorem.
- **Visibility**: private
- **Lines**: 92–99, proof length 5 lines
- **Notes**: Declared with `private lemma` (kind recorded as theorem). Companion of `hasseCoeff_single_add_eq` (l.82), which does the same i-th-variable splitting for the binomial factor `hasseCoeff`; both are used together in the same `rw` chain at l.117 after `eval_monomial`. Name lives in namespace `MvPolynomial` though the statement is purely about `Finsupp.prod` in a commutative monoid (irrelevant while private).

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_taylor_monomial_single_add_aux` (Roth/Taylor.lean:117), the inductive step of the monomial case of `coeff_taylor`.
- Wrapper of 1–2 mathlib calls? It is a Finsupp exponent identity plus `Finsupp.prod_add_index'`; 5 lines. Inlining into the call site would need the same `have` inside a long `rw` chain (the rewrite target appears only after `eval_monomial`), so no saving and worse readability.
- Does mathlib have it? No. `lean_leansearch` ("Finsupp single i n + k minus d equals single i (n - d i) + (k - d.erase i) when k i = 0") returned only `DFinsupp.single_tsub`, `Finsupp.single_sub`, `Finsupp.add_sub_single_one`, `Finsupp.erase`, `DFinsupp.single_sub`, `Finsupp.erase_sub` — generic pieces, none giving the split exponent or the product form. `lean_loogle` `Finsupp.single _ _ + _ - _` returned only unrelated presentation lemmas (exterior power / tautological presentations). The generic tools `Finsupp.prod_add_index'` (Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:364) and `Finsupp.single_tsub` (Mathlib/Data/Finsupp/Order.lean:281) are already what the proof uses.
- Too specific / inline? Specific to the variable-by-variable induction in `coeff_taylor`, but cleanly factored and mirrors `hasseCoeff_single_add_eq`; keeping it separate is right.
- Well-chosen? Yes as a private helper. (A slightly cleaner alternative would state the pure Finsupp identity `single i n + k' - d = single i (n - d i) + (k' - d.erase i)` as the helper, but the product form is what the call site rewrites with; no change recommended.)
- Conclusion: `KEEP` — action: keep as private helper for `coeff_taylor_monomial_single_add_aux`; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Taylor.lean:92).

Note for the parent upstreaming (`coeff_taylor` / `MvPolynomial.taylor`): porting `coeff_taylor` with its current proof needs this lemma; it would travel as a private helper alongside it and `hasseCoeff_single_add_eq`.

## Evidence
- `grep -rn prod_pow_single_add_tsub Roth/`: definition l.92, single use l.117.
- `lean_leansearch` (query above, 6 results): no specialised mathlib statement.
- `lean_loogle` `Finsupp.single _ _ + _ - _`: only unrelated presentation lemmas.
- `grep` in `.lake/packages/mathlib/Mathlib/`: `Finsupp.single_tsub` at Data/Finsupp/Order.lean:281, `Finsupp.prod_add_index'` at Algebra/BigOperators/Finsupp/Basic.lean:364.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
