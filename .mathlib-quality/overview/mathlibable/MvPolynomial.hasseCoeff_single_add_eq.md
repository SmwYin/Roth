---
decl: MvPolynomial.hasseCoeff_single_add_eq
file: Roth/Taylor.lean
line: 82
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private splitting lemma hasseCoeff d (single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k' for k' i = 0, a 6-line Finsupp.mul_prod_erase' computation used once in the monomial induction step of coeff_taylor; mathlib has no hasseCoeff and no ready-made instance.
action: Keep as private helper for its single call site Roth/Taylor.lean:117 (coeff_taylor_monomial_single_add_aux); if hasseCoeff and coeff_taylor are upstreamed, carry it along next to them (Mathlib/Algebra/MvPolynomial/HasseDeriv-style file).
---

# MvPolynomial.hasseCoeff_single_add_eq

## Inventory entry

### `theorem MvPolynomial.hasseCoeff_single_add_eq`
- **Type**: `∀ {σ : Type*} {i : σ} {n : ℕ} {k' : σ →₀ ℕ}, k' i = 0 → ∀ (d : σ →₀ ℕ), hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k'`
- **What**: The multinomial binomial factor hasseCoeff d k = ∏_{j ∈ supp d} C(k_j, d_j) splits off the i-th variable: if k = n·e_i + k' with k' not involving i, then hasseCoeff d k = C(n, d_i) · hasseCoeff (d with i-th entry removed) k'.
- **How**: Unfolds `hasseCoeff` and rewrites the product with `← Finsupp.mul_prod_erase' d i _ (by simp)` (valid since `(k j).choose 0 = 1`), giving `(single i n + k') i).choose (d i) * (d.erase i).prod ...`; `congr 1`: the first factor closes by `simp [hi]`; the second by `Finsupp.prod_congr`, using `Finsupp.support_erase`, `Finset.ne_of_mem_erase` and `Finsupp.single_eq_of_ne` to see `(single i n + k') j = k' j` for `j ≠ i`.
- **Hypotheses**: `hi : k' i = 0` (k' does not involve variable i); `classical`. No ring needed (statement is in ℕ); the ambient `[CommSemiring R]` section variable is not used by this lemma's statement.
- **Uses from project**: `hasseCoeff` (Roth/HasseDeriv.lean:50)
- **Used by**: Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.99; `rw [..., hasseCoeff_single_add_eq hi, ...]` at l.117) only — `grep -rn hasseCoeff_single_add_eq Roth/` gives the definition and that use. Transitively: `coeff_taylor_monomial_aux` → `coeff_taylor` and everything downstream of Taylor's theorem.
- **Visibility**: private
- **Lines**: 82–89, proof length 6 lines
- **Notes**: Declared with `private lemma` (kind recorded as theorem). Companion of `prod_pow_single_add_tsub` (l.91), which does the same splitting for the `α ^ (k - d)` evaluation factor; both are used together at l.117.

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_taylor_monomial_single_add_aux` (Roth/Taylor.lean:117), the inductive step of the monomial case of `coeff_taylor`.
- Wrapper of 1–2 mathlib calls? Essentially `Finsupp.mul_prod_erase'` plus a `prod_congr` cleanup; 6 lines. Small, but it sits inside a long `rw` chain at the call site, where inlining would require a `have` with the same proof — no saving.
- Does mathlib have it? No: `hasseCoeff` is a project definition (Roth/HasseDeriv.lean:50), so mathlib cannot have this statement. The generic tool is `Finsupp.mul_prod_erase'` (Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:170), which the proof already uses; leansearch ("Finsupp.prod of choose over single i n + k splits ...") returned only `Finsupp.mul_prod_erase`, `Finsupp.mul_prod_erase'`, `Finsupp.multinomial_update`, `Finsupp.prod_option_index` — no specialised form. The project lemmas `hasseCoeff_eq_zero_iff`, `hasseCoeff_eq_prod`, `hasseCoeff_mul_hasseCoeff`, `hasseCoeff_mul_succ`, `hasseCoeff_le_two_pow` (Roth/HasseDeriv.lean) do not cover it.
- Too specific / inline? Specific to the variable-by-variable induction in `coeff_taylor`, but naturally stated and cleanly factored; keeping it separate keeps the call-site `rw` chain readable.
- Well-chosen? Yes as a private helper.
- Conclusion: `KEEP` — action: keep as private helper for `coeff_taylor_monomial_single_add_aux`; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Taylor.lean:82).

Note for the parent upstreaming (`MvPolynomial.hasseCoeff`, verdict YES-but-generalise-first; `coeff_taylor`): porting `coeff_taylor` with its current proof needs this lemma; it would travel as a private helper alongside it.

## Evidence
- `grep -rn hasseCoeff_single_add_eq Roth/`: definition l.82, single use l.117.
- `grep -n "lemma hasseCoeff\|theorem hasseCoeff" Roth/*.lean`: no existing project lemma subsumes it.
- `grep -rn "mul_prod_erase'" .lake/packages/mathlib/Mathlib/`: generic lemma at Algebra/BigOperators/Finsupp/Basic.lean:170 (also used analogously in RingTheory/DividedPowerAlgebra/Init.lean:274–278).
- `lean_leansearch` (query above, 6 results): no specialised mathlib statement.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
