---
decl: Roth.linearIndependent_coordinate_polynomials_aux
file: Roth/Separation.lean
line: 235
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-use helper of exists_separated_representation proving the coordinate polynomials sum_nu C(a nu rho) X^nu are linearly independent in rho; a genuine linear-algebra step (dual of a spanning family) not stated in mathlib, though composable from Basis.linearIndependent_coord.
action: Keep as private helper for its single call site Roth/Separation.lean:339 (exists_separated_representation); optional golf via b.linearIndependent_coord.map' with an injective map Dual(span) to R[X] is possible but untested and not required.
---

# Roth.linearIndependent_coordinate_polynomials_aux

## Inventory entry

### `theorem Roth.linearIndependent_coordinate_polynomials_aux`
- **Type**: `∀ {R M : Type*} [CommRing R] [AddCommMonoid M] [Module R M] {n l : ℕ} (v : Fin (n + 1) → M) (b : Module.Basis (Fin l) R (Submodule.span R (Set.range v))), LinearIndependent R (fun ρ ↦ ∑ ν : Fin (n + 1), Polynomial.C (b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ))` (declared `private lemma`; the section variables `τ`, `Fintype τ`, `DecidableEq τ` are omitted and `K` is not used).
- **What**: Let `v_0, …, v_n` be vectors in an `R`-module and `b_1, …, b_l` a basis of their span, with `v_ν = ∑_ρ a_{νρ} b_ρ`. Then the `l` polynomials `φ_ρ(X) = ∑_ν a_{νρ} X^ν ∈ R[X]` are linearly independent over `R`. Equivalently, the columns of the `(n+1) × l` coordinate matrix `(a_{νρ})` are linearly independent, because the `v_ν` span. This is the "the `φ_ν` are linearly independent" claim in the separated decomposition of §2, proof of Lemma 2.
- **How**: `Fintype.linearIndependent_iff`; given `∑ ρ g ρ • φ ρ = 0`, take the `ν`-th coefficient (`Polynomial.finsetSum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`) to get `∑_ρ g ρ a_{νρ} = 0` for every `ν`. Then the functional `f = ∑_ρ g ρ • b.coord ρ` on the span vanishes on every `v ν`, hence is zero by `LinearMap.ext_on` with `Submodule.span_span_coe_preimage`. Evaluating `f` at `b ρ₀` (`Module.Basis.coord_apply`, `Module.Basis.repr_self`, `Finsupp.single_apply`, `Finset.sum_ite_eq`) gives `g ρ₀ = 0`.
- **Hypotheses**: `[CommRing R]` (ring, not just semiring, because `Fintype.linearIndependent_iff` is used; commutativity is needed for `g ρ • b.coord ρ` to be a linear map). `[AddCommMonoid M] [Module R M]`. No field assumption: it is stated in more generality than the caller needs (the caller uses a field `K`). No redundant hypotheses.
- **Uses from project**: `[]` (only mathlib: `Fintype.linearIndependent_iff`, `Polynomial.finsetSum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `Module.Basis.coord`, `LinearMap.ext_on`, `Submodule.span_span_coe_preimage`, `Module.Basis.repr_self`, `LinearMap.congr_fun`).
- **Used by**: Roth/Separation.lean:339 `Roth.exists_separated_representation` only (supplies `LinearIndependent K φ`); `grep -rn linearIndependent_coordinate_polynomials Roth/` returns only the definition (l.235) and this use. Transitively everything downstream of the separated representation (Lemma 2).
- **Visibility**: private
- **Lines**: 234–262 (including the `omit` line), proof length 22 lines
- **Notes**: Name ends in `_aux`, no docstring (usual for private helpers). The `⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩` subtype term is repeated verbatim in the caller and in `eq_sum_aeval_basis_coeffNone_aux`, so the three statements match syntactically.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Separation.lean:339 inside the public `exists_separated_representation`.
- Wrapper of 1–2 mathlib calls? No. It is a 22-line argument combining coefficient extraction with a dual-functional argument; a genuine (if standard) linear-algebra step.
- Does mathlib have it? Not as stated. `lean_leansearch` ("coordinate functions of a basis are linearly independent"; "polynomials with coefficients given by coordinates of spanning vectors in a basis are linearly independent") returned only `Module.Basis.coord`, `Module.Basis.linearIndependent`, `Polynomial.Sequence.linearIndependent`, `MvPolynomial.linearIndependent_X`, none of which match. `grep` found `Module.Basis.linearIndependent_coord` (Mathlib/LinearAlgebra/Basis/Basic.lean:134, `LinearIndependent R b.coord`). The lemma is composable from it: push `b.coord` through the linear map `Dual(span) → R[X]`, `f ↦ ∑_ν C (f ⟨v ν, _⟩) X^ν`, via `LinearIndependent.map'`; that map is injective by the same `LinearMap.ext_on` spanning argument. This would replace the coefficient step but not the injectivity step, so it is a possible golf, not a replacement by a mathlib lemma. Not tried in Lean.
- Too specific / inline? Specific to Lemma 2. Inlining into the already long `refine` of `exists_separated_representation` would hurt readability; keeping it separate is better. Already private.
- Well-chosen? Yes. The statement is the exact term the caller needs. It is stated over a general commutative ring and module, not only over the field `K`.
- Conclusion: `KEEP`. Action: none required; optional golf via `b.linearIndependent_coord.map'` noted above.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:235; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent: if `exists_separated_representation` is ever upstreamed, this helper must come along with it or be re-proved via `Module.Basis.linearIndependent_coord` plus `LinearIndependent.map'`.

## Evidence
- `grep -rn linearIndependent_coordinate_polynomials Roth/`: definition l.235, single use l.339.
- `lean_leansearch` (two queries above, 6 and 5 results): no match.
- `grep` in mathlib for `linearIndependent_coord` and dual-basis independence: `Module.Basis.linearIndependent_coord` (Mathlib/LinearAlgebra/Basis/Basic.lean:134) only.
- No Lean runs and no evidence Lean files. A private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated. The composition route above is a sketch and was not compiled.
